import imagehash
from tqdm.notebook import tqdm
import numpy as np
import itertools
from multiprocessing import Pool
import random
import string

shared_dict = {}

hash_types = ['phash', 'whash', 'dhash', 'ahash']

def make_hashes (image):
    return {h:imagehash.hex_to_hash(image[h]) for h in hash_types}

def hashes_diff (hashes_x, hashes_y, hash_type=None):
    if hash_type:
        return hashes_x[hash_type] - hashes_y[hash_type]

    diffs = [abs(hashes_x[h] - hashes_y[h]) for h in hash_types]
    diff = (sum(diffs) - min(diffs) - max(diffs)) / 2
    return diff

def is_duplicated (image_x, image_y, duplicated_image_phash_pairs):
    image_x_phash = image_x['phash']
    image_y_phash = image_y['phash']

    if frozenset([image_x_phash, image_y_phash]) in duplicated_image_phash_pairs:
        return True

    # phash distance < 4 considered as the same
    if hashes_diff(make_hashes(image_x), make_hashes(image_y), 'phash') < 4:
        return True

    return False

def cal_distance (args):
    start_i, start_j, end_i, end_j, key, hash_type = args
    hashes = shared_dict[key]

    result = np.zeros((end_i-start_i, end_j-start_j))

    for i in range(start_i, end_i):
        for j in range(start_j, end_j):
            if j > i:
                continue
            result[i-start_i, j-start_j] = hashes_diff(hashes[i], hashes[j], hash_type)

    return (start_i, start_j, end_i, end_j, result)

def calculate_distance (hashes, hash_type=None):
    size = len(hashes)
    bs = size // 50

    idxs = [(i, j) for i, j in itertools.product(range(0, size, bs), range(0, size, bs))]

    distance = np.ndarray((size, size))

    key = ''.join(random.choices(string.ascii_uppercase, k=10))
    shared_dict[key] = hashes

    p = Pool()
    for r in tqdm(p.imap_unordered(cal_distance, [(i, j, min(i+bs, size), min(j+bs, size), key, hash_type) for i, j in idxs]), total=len(idxs)):
        start_i, start_j, end_i, end_j, result = r
        distance[start_i:end_i, start_j:end_j] = result
    p.close()
    p.join()

    del shared_dict[key]

    for i in tqdm(range(size)):
        for j in range(i):
            distance[j, i] = distance[i, j]

    return distance

# distance2 = np.ndarray([len(image_hashes), len(image_hashes)])
# for i in tqdm(range(len(image_hashes))):
#     for j in range(i+1):
#         diff = hashes_diff(image_hashes[i], image_hashes[j])
#         distance2[i, j] = diff
#         distance2[j, i] = diff
# np.array_equal(distance, distance2)
