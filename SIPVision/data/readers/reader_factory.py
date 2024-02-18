
import os 
from typing import Optional

from .reader_image_folder import ReaderImageFolder
from .reader_image_in_tar import ReaderImageInTar

def create_reader(
    name:str,
    root : Optional[str] = None,
    split:str = 'train',
    **kwargs,
):
    
    kwargs = {k : v for k,v in kwargs.items() if v is not None}
    
    
    # TODO Understand each varant if usesfull in the future 
    name = name.lower()
    name = name.split("/",1)
    prefix = '' 
    if len(name) > 1 :
        prefix = name[0]
    if prefix == 'hfds':
        # hugging face datasets 
        pass
    elif prefix == 'hfids':
        # hugging face iterable datasets 
        pass
    elif prefix == 'tfds':
        # TFDS 
        pass
    elif prefix == 'wds':
        # webdatasets 
        pass

    else : 
        
        assert os.path.exists(root)
        # TODO: Improving the comprssion files reading like .zip / .tar /
        # TODO: Creating Dataset reader that adapts to all kinds of data 
        if os.path.isfile(root) and os.path.splitext(root)[1] == ".tar" : 
        
            pass 
        
        else : 
            
            reader = ReaderImageFolder(root,**kwargs)
    
    return reader
    
    
    