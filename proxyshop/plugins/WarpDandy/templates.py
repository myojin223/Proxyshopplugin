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
     * Not currently working
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
 
class NicknameSmallTemplate (temp.NormalTemplate):
    """
     * The showcase template first used on the Women's Day Secret Lair. The layer structure of this template and NormalTemplate are
     * similar, but this template doesn't have any background layers, and a layer mask on the pinlines group needs to be enabled when
     * the card is legendary.
    """
    def template_file_name (self):
        return "WarpDandy/NicknameSmall"

    def template_suffix (self):
        return "Ikoria S"

    def __init__ (self, layout, file):
        # strip out reminder text for fullart
        super().__init__(layout, file)

    def enable_frame_layers (self):

        # twins and pt box
        psd.getLayer(self.layout.twins, con.layers['TWINS']).visible = True
        if self.is_creature:
            psd.getLayer(self.layout.twins, con.layers['PT_BOX']).visible = True

        # pinlines
        pinlines = psd.getLayerSet(con.layers['PINLINES_TEXTBOX'])
        if self.is_land:
            pinlines = psd.getLayerSet(con.layers['LAND_PINLINES_TEXTBOX'])
        psd.getLayer(self.layout.pinlines, pinlines).visible = True

        if self.is_legendary:
            # legendary crown
            psd.getLayer(self.layout.pinlines, con.layers['LEGENDARY_CROWN']).visible = True
            app.activeDocument.activeLayer = pinlines
            psd.enable_active_layer_mask()
           


class NicknameMediumTemplate (temp.NormalTemplate):
    """
     * The showcase template first used on the Women's Day Secret Lair. The layer structure of this template and NormalTemplate are
     * similar, but this template doesn't have any background layers, and a layer mask on the pinlines group needs to be enabled when
     * the card is legendary.
    """
    def template_file_name (self):
        return "WarpDandy/NicknameMedium"

    def template_suffix (self):
        return "Ikoria M"

    def __init__ (self, layout, file):
        # strip out reminder text for fullart
        super().__init__(layout, file)

    def enable_frame_layers (self):

        # twins and pt box
        psd.getLayer(self.layout.twins, con.layers['TWINS']).visible = True
        if self.is_creature:
            psd.getLayer(self.layout.twins, con.layers['PT_BOX']).visible = True

        # pinlines
        pinlines = psd.getLayerSet(con.layers['PINLINES_TEXTBOX'])
        if self.is_land:
            pinlines = psd.getLayerSet(con.layers['LAND_PINLINES_TEXTBOX'])
        psd.getLayer(self.layout.pinlines, pinlines).visible = True

        if self.is_legendary:
            # legendary crown
            psd.getLayer(self.layout.pinlines, con.layers['LEGENDARY_CROWN']).visible = True
            app.activeDocument.activeLayer = pinlines
            psd.enable_active_layer_mask()
            
   
class NicknameLargeTemplate (temp.NormalTemplate):
    """
     * The showcase template first used on the Women's Day Secret Lair. The layer structure of this template and NormalTemplate are
     * similar, but this template doesn't have any background layers, and a layer mask on the pinlines group needs to be enabled when
     * the card is legendary.
    """
    def template_file_name (self):
        return "WarpDandy/NicknameLarge"

    def template_suffix (self):
        return "Ikoria L"

    def __init__ (self, layout, file):
        # strip out reminder text for fullart
        super().__init__(layout, file)

    def enable_frame_layers (self):

        # twins and pt box
        psd.getLayer(self.layout.twins, con.layers['TWINS']).visible = True
        if self.is_creature:
            psd.getLayer(self.layout.twins, con.layers['PT_BOX']).visible = True

        # pinlines
        pinlines = psd.getLayerSet(con.layers['PINLINES_TEXTBOX'])
        if self.is_land:
            pinlines = psd.getLayerSet(con.layers['LAND_PINLINES_TEXTBOX'])
        psd.getLayer(self.layout.pinlines, pinlines).visible = True

        if self.is_legendary:
            # legendary crown
            psd.getLayer(self.layout.pinlines, con.layers['LEGENDARY_CROWN']).visible = True
            app.activeDocument.activeLayer = pinlines
            psd.enable_active_layer_mask()
            
class GoldenAgeTemplate (temp.NormalFullartTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/GoldenAge"
    
    def template_suffix (self):
        return "Golden Age"
    
    # OPTIONAL
    def __init__ (self, layout, file):
        # DO STUFF
        super().__init__(layout, file)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()