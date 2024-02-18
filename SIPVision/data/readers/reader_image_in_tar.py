""" A dataset reader that reads tarfile based datasets

This reader can extract image samples from:

* a single tar of image files
* a folder of multiple tarfiles containing imagefiles
* a tar of tars containing image files

Labels are based on the combined folder and/or tar name structure.
"""


import logging
import os 
import pickle
import tarfile
from glob import glob
from typing import List,Tuple,Dict,Set,Optional,Union

import numpy as np
import jax.numpy as jnp 

#from timm.utils.misc import natural_key

from .class_map import load_class_map
from .img_extensions import get_img_extensions
from .reader import Reader


_logger = logging.getLogger(__name__)
CACHE_FILENAME_SUFFIX = '_tarinfos.pickle'

def extract_tarinfos(
    root,
    class_name_to_idx : Optional[Dict] = None,
    cache_tarinfo : Optional[bool] = None,
    extensions:Optional[Union[List,Tuple,Set]] = None,
    sort:bool = True
):
    extensions = get_img_extensions(as_set=True) if not extensions else set(extensions)
    root_is_tar = False
    if os.path.isfile(root):
        assert os.path.splitext(root)[-1].lower() == '.tar'
        tar_filenames = [root]
        root , root_name = os.path.split(root)
        root_name = os.path.splitext(root_name)[0]
        root_is_tar = True
    # TODO : Problem in the case folder of tars should be treated 
    else:
        root_name = root.strip(os.path.sep).split(os.path.sep)[-1]
        print("ok")
        tar_filenames = glob(os.path.join(root, '*.tar'), recursive=True)
    
    num_tars = len(tar_filenames)
    tar_bytes = sum([os.path.getsize(f) for f in tar_filenames])
    assert num_tars ,  f'No .tar files found at specified path ({root}).'
    
    _logger.info(f'Scanning {tar_bytes/1024**2:.2f}MB of tar files...')
    info = dict(tartrees=[])
    cache_path = ''
    if cache_tarinfo is None:
        cache_tarinfo = True if tar_bytes > 10*1024**3 else False
    
    if cache_tarinfo:
        cache_filename = '_' + root_name + CACHE_FILENAME_SUFFIX
        cache_path = os.path.join(root, cache_filename)
    
    if os.path.exists(cache_path):
        _logger.info(f'Reading tar info from cache file {cache_path}.')
        
        
    
    
    
class ReaderImageInTar(Reader):
    """ 
    Multi-tarfile dataset reader where there is one .tar file per class
    """

    def __init__(self, root, class_map='', cache_tarfiles=True, cache_tarinfo=None):
        super().__init__()
        
        class_name_to_idx = None
        if class_map:
            class_name_to_idx  = load_class_map(class_map,root)
        
        assert os.path.isfile(root)
        self.root = root
        
        self.samples , self.targets,self.class_name_to_idx,tarfiles = extract_tarinfos(
            self.root,
            class_name_to_idx=class_name_to_idx,
            cache_tarinfo=cache_tarinfo
        )
        
        
