"""
WARPDANDY TEMPLATES
"""
import os
import proxyshop.frame_logic as frame_logic
import proxyshop.format_text as format_text
import proxyshop.text_layers as txt_layers
import proxyshop.templates as temp
import proxyshop.constants as con
import proxyshop.settings as cfg
import proxyshop.helpers as psd
import photoshop.api as ps
app = ps.Application()

class FullartTrixTemplate (temp.NormalFullartTemplate):
    """
     * Port of TrixAreForScoot Proximity Template
     * Created by WarpDandy & TrixAreForScoot
    """
    def template_file_name (self):
        return "WarpDandy/FullartTrix"
    
    def template_suffix (self):
        return "FullartTrix"
    
    # OPTIONAL
    def __init__ (self, layout, file):
        # DO STUFF
        super().__init__(layout, file)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()

 
class LegendsTemplate (temp.NormalClassicTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Legends"
    
    def template_suffix (self):
        return "Legends"
    
    # OPTIONAL
    def __init__ (self, layout, file):
        # DO STUFF
        super().__init__(layout, file)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
 
 
class PortalTemplate (temp.NormalClassicTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Portal"
    
    def template_suffix (self):
        return "Portal"
    
    # OPTIONAL
    def __init__ (self, layout, file):
        # DO STUFF
        super().__init__(layout, file)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        

class NinjaTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Ninja"
    
    def template_suffix (self):
        return "Ninja"
    
    # OPTIONAL
    def __init__ (self, layout, file):
        # DO STUFF
        super().__init__(layout, file)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
 
 
class NinjaGlitchTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/NinjaGlitch"
    
    def template_suffix (self):
        return "Glitch Ninja"
    
    # OPTIONAL
    def __init__ (self, layout, file):
        # DO STUFF
        super().__init__(layout, file)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()   


class MirrorTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Mirror"
    
    def template_suffix (self):
        return "Left-Handed"
    
    # OPTIONAL
    def __init__ (self, layout, file):
        # DO STUFF
        super().__init__(layout, file)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
         
 
class ClassicWhiteBorderTemplate (temp.NormalClassicTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/ClassicWhiteBorder"
    
    def template_suffix (self):
        return "Classic WB"
    
    # OPTIONAL
    def __init__ (self, layout, file):
        # DO STUFF
        super().__init__(layout, file)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()