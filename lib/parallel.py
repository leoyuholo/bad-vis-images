from joblib import Parallel, delayed
from tqdm.notebook import tqdm

def parallel (f, params_list, params_dict={}, total=None, tqdm_postfix='', leave=True, n_jobs=-2):
    results = []
    with Parallel(n_jobs=n_jobs, require='sharedmem') as p:
        results = p(delayed(f)(params, **params_dict)
                    for params in tqdm(params_list, postfix=tqdm_postfix, leave=leave, total=total))
    return results