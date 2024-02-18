
import os 
from typing import Optional

#from .reader_image_folder import ReaderImageFolder
from .reader_image_in_tar import ReaderImageInTar

def create_reader(
    name:str,
    root : Optional[str] = None,
    split:str = 'train',
    **kwargs,
):
    
    kwargs = {k : v for k,v in kwargs.items() if v is not None}
    
    
    #-------- ?? big data things  ------------
    name = name.lower()
    name = name.split("/",1)
    prefix = '' 
    if len(name) > 1 :
        prefix = name[0]
    if prefix == 'hfds':
        pass
    elif prefix == 'hfids':
        pass
    elif prefix == 'tfds':
        pass
    elif prefix == 'wds':
        pass
    # ---------- ?? ----------
    else : 
        assert os.path.exists(root)
        # TODO: Improving the comprssion files reading like .zip / .tar /
        # TODO: Creating Dataset reader that adapts to all kinds of data 
        if os.path.isfile(root) and os.path.splitext(root)[1] == ".tar" : 
          
            reader = ReaderImageInTar(root, **kwargs)
        else : 
            pass 
    
    
    
    