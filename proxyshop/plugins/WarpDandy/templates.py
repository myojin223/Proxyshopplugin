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
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
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
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
 
 
class SamuraiTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Samurai"
    
    def template_suffix (self):
        return "Samurai"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
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
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
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
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
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
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
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
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
 
class NicknameSmallTemplate (temp.NormalTemplate):
    """
     * Requires manually adding the nickname
    """
    def template_file_name (self):
        return "WarpDandy/NicknameSmall"

    def template_suffix (self):
        return "Ikoria S"

    def __init__ (self, layout):
        # strip out reminder text for fullart
        super().__init__(layout)

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
     * Requires manually adding the nickname
    """
    def template_file_name (self):
        return "WarpDandy/NicknameMedium"

    def template_suffix (self):
        return "Ikoria M"

    def __init__ (self, layout):
        # strip out reminder text for fullart
        super().__init__(layout)

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
     * Requires manually adding the nickname
    """
    def template_file_name (self):
        return "WarpDandy/NicknameLarge"

    def template_suffix (self):
        return "Ikoria L"

    def __init__ (self, layout):
        # strip out reminder text for fullart
        super().__init__(layout)

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
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
       
class GoldenAge2Template (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/GoldenAge2"
    
    def template_suffix (self):
        return "Golden Age 2"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        
class zneExpeditionTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/zneExpedition"
    
    def template_suffix (self):
        return "Original Expedition"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        
class SkyscraperTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Skyscraper"
    
    def template_suffix (self):
        return "Skyscraper"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        
class GoldenAgeV2Template (temp.NormalTemplate):
    """
     * Created by MrOppsokopolis
    """
    def template_file_name (self):
        return "WarpDandy/GoldenAgeV2"
    
    def template_suffix (self):
        return "Golden Age V2"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        
class ArtDecoTemplate (temp.NormalTemplate):
    """
     * Created by MrOppsokopolis
    """
    def template_file_name (self):
        return "WarpDandy/ArtDeco"
    
    def template_suffix (self):
        return "Art Deco"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        
class UniversesBeyondTemplate (temp.NormalTemplate):
    """
     * Created by MrOppsokopolis
    """
    def template_file_name (self):
        return "WarpDandy/UniversesBeyond"
    
    def template_suffix (self):
        return "Universes Beyond"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        
"""
Planeswalker templates
"""
class ClassicPWTemplate (temp.PlaneswalkerTemplate):
    """
     * Planeswalker template - 3 or 4 loyalty abilities.
    """
    def template_file_name (self):
        return "WarpDandy/ClassicPW"

    def __init__ (self, layout):
        self.exit_early = True
        super().__init__(layout)

        if self.layout.is_colorless: self.art_reference = psd.getLayer(con.layers['FULL_ART_FRAME'])
        else: self.art_reference = psd.getLayer(con.layers['PLANESWALKER_ART_FRAME'])

        ability_array = self.layout.oracle_text.split("\n")
        num_abilities = 3
        if len(ability_array) > 3: num_abilities = 4

        # docref for everything but legal and art reference is based on number of abilities
        self.docref = psd.getLayerSet("pw-"+str(num_abilities))
        self.docref.visible = True

        # Basic text layers
        self.basic_text_layers(psd.getLayerSet(con.layers['TEXT_AND_ICONS'], self.docref))

        # planeswalker ability layers
        group_names = [con.layers['FIRST_ABILITY'], con.layers['SECOND_ABILITY'], con.layers['THIRD_ABILITY'], con.layers['FOURTH_ABILITY']]
        loyalty_group = psd.getLayerSet(con.layers['LOYALTY_GRAPHICS'], self.docref)

        for i, ability in enumerate(ability_array):
            if i == 4: break
            ability_group = psd.getLayerSet(group_names[i], loyalty_group)
            static_text_layer = psd.getLayer(con.layers['STATIC_TEXT'], ability_group)
            ability_text_layer = psd.getLayer(con.layers['ABILITY_TEXT'], ability_group)
            ability_layer = ability_text_layer
            colon_index = ability.find(": ")

            # determine if this is a static or activated ability by the presence of ":" in the start of the ability
            if colon_index > 0 < 5:
                # activated ability

                # determine which loyalty group to enable, and set the loyalty symbol's text
                loyalty_graphic = psd.getLayerSet(ability[0], ability_group)
                loyalty_graphic.visible = True
                self.tx_layers.append(
                    txt_layers.TextField(
                        layer = psd.getLayer(con.layers['COST'], loyalty_graphic),
                        text_contents = ability[0:int(colon_index)],
                        text_color = psd.rgb_black(),
                    )
                )
                ability = ability[int(colon_index)+2:]

            else:
                # static ability
                ability_layer = static_text_layer
                ability_text_layer.visible = False
                static_text_layer.visible = True
                psd.getLayer("Colon", ability_group).visible = False

            self.tx_layers.append(
                txt_layers.BasicFormattedTextField(
                    layer = ability_layer,
                    text_contents = ability,
                    text_color = psd.get_text_layer_color(ability_layer),
                )
            )

        # starting loyalty
        self.tx_layers.append(
            txt_layers.TextField(
                layer = psd.getLayer(con.layers['TEXT'], psd.getLayerSet(con.layers['STARTING_LOYALTY'], loyalty_group)),
                text_contents = self.layout.scryfall['loyalty'],
                text_color = psd.rgb_white(),
            )
        )

        # paste scryfall scan
        app.activeDocument.activeLayer = psd.getLayerSet(con.layers['TEXTBOX'], self.docref)
        self.paste_scryfall_scan(psd.getLayer(con.layers['SCRYFALL_SCAN_FRAME']))

    def enable_frame_layers (self):
        # Twins, pinlines, background
        psd.getLayer(self.layout.twins, psd.getLayerSet(con.layers['TWINS'], self.docref)).visible = True
        psd.getLayer(self.layout.pinlines, psd.getLayerSet(con.layers['PINLINES'], self.docref)).visible = True
        self.enable_background()

    def enable_background (self):
        """
        Enable card background
        """
        psd.getLayer(self.layout.background, psd.getLayerSet(con.layers['BACKGROUND'], self.docref)).visible = True
        
    def template_suffix (self):
        return "Classic PW"
        
class ArtDecoPWTemplate (temp.PlaneswalkerTemplate):
    """
     * Planeswalker template - 3 or 4 loyalty abilities.
    """
    def template_file_name (self):
        return "WarpDandy/ArtDecoPW"

    def __init__ (self, layout):
        self.exit_early = True
        super().__init__(layout)

        if self.layout.is_colorless: self.art_reference = psd.getLayer(con.layers['FULL_ART_FRAME'])
        else: self.art_reference = psd.getLayer(con.layers['PLANESWALKER_ART_FRAME'])

        ability_array = self.layout.oracle_text.split("\n")
        num_abilities = 3
        if len(ability_array) > 3: num_abilities = 4

        # docref for everything but legal and art reference is based on number of abilities
        self.docref = psd.getLayerSet("pw-"+str(num_abilities))
        self.docref.visible = True

        # Basic text layers
        self.basic_text_layers(psd.getLayerSet(con.layers['TEXT_AND_ICONS'], self.docref))

        # planeswalker ability layers
        group_names = [con.layers['FIRST_ABILITY'], con.layers['SECOND_ABILITY'], con.layers['THIRD_ABILITY'], con.layers['FOURTH_ABILITY']]
        loyalty_group = psd.getLayerSet(con.layers['LOYALTY_GRAPHICS'], self.docref)

        for i, ability in enumerate(ability_array):
            if i == 4: break
            ability_group = psd.getLayerSet(group_names[i], loyalty_group)
            static_text_layer = psd.getLayer(con.layers['STATIC_TEXT'], ability_group)
            ability_text_layer = psd.getLayer(con.layers['ABILITY_TEXT'], ability_group)
            ability_layer = ability_text_layer
            colon_index = ability.find(": ")

            # determine if this is a static or activated ability by the presence of ":" in the start of the ability
            if colon_index > 0 < 5:
                # activated ability

                # determine which loyalty group to enable, and set the loyalty symbol's text
                loyalty_graphic = psd.getLayerSet(ability[0], ability_group)
                loyalty_graphic.visible = True
                self.tx_layers.append(
                    txt_layers.TextField(
                        layer = psd.getLayer(con.layers['COST'], loyalty_graphic),
                        text_contents = ability[0:int(colon_index)],
                        text_color = psd.rgb_white(),
                    )
                )
                ability = ability[int(colon_index)+2:]

            else:
                # static ability
                ability_layer = static_text_layer
                ability_text_layer.visible = False
                static_text_layer.visible = True
                psd.getLayer("Colon", ability_group).visible = False

            self.tx_layers.append(
                txt_layers.BasicFormattedTextField(
                    layer = ability_layer,
                    text_contents = ability,
                    text_color = psd.get_text_layer_color(ability_layer),
                )
            )

        # starting loyalty
        self.tx_layers.append(
            txt_layers.TextField(
                layer = psd.getLayer(con.layers['TEXT'], psd.getLayerSet(con.layers['STARTING_LOYALTY'], loyalty_group)),
                text_contents = self.layout.scryfall['loyalty'],
                text_color = psd.rgb_white(),
            )
        )

        # paste scryfall scan
        app.activeDocument.activeLayer = psd.getLayerSet(con.layers['TEXTBOX'], self.docref)
        self.paste_scryfall_scan(psd.getLayer(con.layers['SCRYFALL_SCAN_FRAME']))

    def enable_frame_layers (self):
        # Twins, pinlines, background
        psd.getLayer(self.layout.twins, psd.getLayerSet(con.layers['TWINS'], self.docref)).visible = True
        psd.getLayer(self.layout.pinlines, psd.getLayerSet(con.layers['PINLINES'], self.docref)).visible = True
        self.enable_background()

    def enable_background (self):
        """
        Enable card background
        """
        psd.getLayer(self.layout.background, psd.getLayerSet(con.layers['BACKGROUND'], self.docref)).visible = True
        
    def template_suffix (self):
        return "Art Deco PW"