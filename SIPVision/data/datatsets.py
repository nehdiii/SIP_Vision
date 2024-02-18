



import io 
import logging
from typing import Optional

import torch 
from torch.utils.data import Dataset
from PIL import Image


from .readers import create_reader 


_logger = logging.getLogger(__name__)

_ERROR_RETRY = 50



class ImageDataset(Dataset):
    
    def __init__(
            self,
            root : str,
            reader=None,
            split='train',
            class_map=None,
            load_bytes=False,
            input_img_mode='RGB',
            transform=None,
            target_transform=None,
            ):
        
        # if reader is None or a string 
        if reader is None or isinstance(reader,str):
            reader = create_reader(
                reader or '',
                root = root,
                split=split,
                class_map = class_map
            )
            
            