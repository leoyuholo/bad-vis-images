from functools import cmp_to_key
from datetime import datetime

# prioritize high numbers
source_ranks = {
    'dataisugly': 1,
    'wtf-viz': -1,
    'badvisualisations': -2
}

def get_source_rank (source):
    return source_ranks.get(source, 0)

def post_score (post):
    return post.get('ups', 0) + 5 * post.get('num_comments', 0)

def sort_posts (posts):
    def preferred (post_x, post_y):
        rank_x = get_source_rank(post_x['source'])
        rank_y = get_source_rank(post_y['source'])
        if rank_x != rank_y:
            return rank_y - rank_x
        return (datetime.fromisoformat(post_x['datetime']) - datetime.fromisoformat(post_y['datetime'])).total_seconds()
#         return post_score(post_y) - post_score(post_x)

    return sorted(posts, key=cmp_to_key(preferred))

# prioritize high numbers
image_type_ranks = {
    'manual': 4,
    'archive': 3,
    'external_link': 2,
    'external_link_alt': 1.5,
    'preview': 1,
    'preview_alt': 0.5
}

def get_image_type_rank (source):
    return image_type_ranks.get(source, 0)

def simple_sort_images (images):
    def preferred (image_x, image_y):
        image_type_rank_x = get_image_type_rank(image_x['image_type'])
        image_type_rank_y = get_image_type_rank(image_y['image_type'])
        # external over preview
        if image_type_rank_x != image_type_rank_y:
            return image_type_rank_y - image_type_rank_x
        else:
            return image_x['index_in_album'] - image_y['index_in_album']

    return sorted(images, key=cmp_to_key(preferred))

def sort_images (images):
    def preferred (image_x, image_y):
        # manual overrider everything else
        if image_x['image_type'] == 'manual':
            return -1
        if image_y['image_type'] == 'manual':
            return 1

        # animated over non-animated
        if image_x['animated'] != image_y['animated']:
            if image_x['animated']:
                return -1
            if image_y['animated']:
                return 1

        # high resolution over low
        if image_x['pixels'] != image_y['pixels']:
            return image_y['pixels'] - image_x['pixels']

        # png over others
        if image_x['ext'] != image_y['ext']:
            if image_x['ext'] == '.png':
                return -1
            if image_y['ext'] == '.png':
                return 1

        # file size indicates better quality for lossy formats
        if image_y['size'] != image_x['size']:
            return image_y['size'] - image_x['size']

        image_type_rank_x = get_image_type_rank(image_x['image_type'])
        image_type_rank_y = get_image_type_rank(image_y['image_type'])
        # external over preview
        if image_type_rank_x != image_type_rank_y:
            return image_type_rank_y - image_type_rank_x

        return get_source_rank(image_y['source']) - get_source_rank(image_x['source'])

    return sorted(images, key=cmp_to_key(preferred))
