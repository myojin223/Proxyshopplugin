"""
WARPDANDY TEMPLATES
"""
import os
from functools import cached_property
from typing import Optional

import proxyshop.frame_logic as frame_logic
import proxyshop.format_text as format_text
import proxyshop.text_layers as text_classes
import proxyshop.templates as temp
import proxyshop.helpers as psd
from proxyshop.constants import con
from proxyshop.settings import cfg

from photoshop.api._artlayer import ArtLayer
import photoshop.api as ps
app = ps.Application()


class FullartTrixTemplate (temp.NormalTemplate):
    """
     * Port of TrixAreForScoot Proximity Template
     * Created by WarpDandy & TrixAreForScoot
    """
    template_file_name = "WarpDandy/FullartTrix"
    template_suffix = "FullartTrix"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    def create_expansion_symbol(self, centered=False):
        # Skip if common
        if self.layout.rarity == con.rarity_common:
            return

        # Only add the rarity overlay
        rarity = self.layout.rarity
        if self.layout.rarity in (con.rarity_bonus, con.rarity_special):
            rarity = con.rarity_mythic
        psd.getLayer(rarity.lower(), self.text_layers).visible = True


class SamuraiTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/Samurai"
    template_suffix = "Samurai"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return
        

class NinjaTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/Ninja"
    template_suffix = "Ninja"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return
 
 
class NinjaGlitchTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/NinjaGlitch"
    template_suffix = "Glitch Ninja"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    def load_artwork(self):
        super().load_artwork()

        # Content aware fill for extended art
        psd.content_fill_empty_area(self.art_layer)


class MirroredTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/Mirrored"
    template_suffix = "Mirrored"

    def basic_text_layers(self):
        # Flip scaling on text layers
        self.text.extend([
            text_classes.FormattedTextField(
                layer=self.text_layer_mana,
                contents=self.layout.mana_cost
            ),
            text_classes.ScaledTextField(
                layer=self.text_layer_name,
                contents=self.layout.name,
                reference=self.text_layer_mana,
                flip_scale=True
            ),
            text_classes.ScaledTextField(
                layer=self.text_layer_type,
                contents=self.layout.type_line,
                reference=self.expansion_symbol,
                flip_scale=True
            )
        ])

    @property
    def expansion_symbol_anchor(self) -> ps.AnchorPosition:
        return ps.AnchorPosition.MiddleLeft

    def load_artwork(self):
        super().load_artwork()
        self.active_layer.resize(-100, 100, ps.AnchorPosition.MiddleCenter)
         
 
class ClassicWhiteBorderTemplate (temp.NormalClassicTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/ClassicWhiteBorder"
    template_suffix = "Classic WB"


class NicknameSmallTemplate (temp.NormalTemplate):
    """
     * Requires manually adding the nickname
    """
    template_file_name = "WarpDandy/NicknameSmall"
    template_suffix = "Nickname S"

    def __init__(self, layout):
        cfg.exit_early = True
        cfg.remove_reminder = True
        cfg.remove_flavor = True
        super().__init__(layout)

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def art_reference_layer(self) -> Optional[ArtLayer]:
        return psd.getLayer(con.layers.ART_FRAME)

    def load_artwork(self):
        super().load_artwork()

        # Content aware fill for extended art
        psd.content_fill_empty_area(self.art_layer)
           

class NicknameMediumTemplate (temp.NormalTemplate):
    """
     * Requires manually adding the nickname
    """
    template_file_name = "WarpDandy/NicknameMedium"
    template_suffix = "Nickname M"

    def __init__(self, layout):
        cfg.exit_early = True
        cfg.remove_reminder = True
        super().__init__(layout)

    @property
    def is_nyx(self) -> bool:
        return False
    
    @property
    def is_companion(self) -> bool:
        return False
    
    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def art_reference_layer(self) -> Optional[ArtLayer]:
        return psd.getLayer(con.layers.ART_FRAME)

    def load_artwork(self):
        super().load_artwork()

        # Content aware fill for extended art
        psd.content_fill_empty_area(self.art_layer)


class GoldenAge2Template (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/GoldenAge2"
    template_suffix = "Golden Age 2"

    def __init__(self, layout):
        cfg.remove_flavor = True
        cfg.remove_reminder = True
        super().__init__(layout)

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class zneExpeditionTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/zneExpedition"
    template_suffix = "Original Expedition"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_legendary(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class SkyscraperTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/Skyscraper"
    template_suffix = "Skyscraper"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_legendary(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class GoldenAgeV2Template (temp.NormalTemplate):
    """
     * Created by MrOppsokopolis
    """
    template_file_name = "WarpDandy/GoldenAgeV2"
    template_suffix = "Golden Age V2"

    def __init__(self, layout):
        cfg.remove_flavor = True
        cfg.remove_reminder = True
        super().__init__(layout)

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class ArtDecoTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/ArtDeco"
    template_suffix = "Art Deco"

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class UniversesBeyondTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/UniversesBeyond"
    template_suffix = "Universes Beyond"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_legendary(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class EtchedTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/Etched"
    template_suffix = "Etched"

    @property
    def is_legendary(self) -> bool:
        return False

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class DestinyTemplate (temp.NormalTemplate):
    """
     * Created by Meeple, ported to Proxyshop by WarpDandy
    """
    template_file_name = "WarpDandy/Destiny"
    template_suffix = "Destiny"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

        
class PinlinesExtNeonTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/PinlinesExtNeon"
    template_suffix = "Neon Extended"

    def __init__(self, layout):
        # Strip extra text for small text box
        cfg.remove_flavor = True
        cfg.remove_reminder = True
        super().__init__(layout)

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def color_indicator_layer(self) -> Optional[ArtLayer]:
        return

    def load_artwork(self):
        # Content aware fill
        super().load_artwork()
        psd.content_fill_empty_area(self.art_layer)


class MysticalArchiveTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/MysticalArchive"
    template_suffix = "Mystical Archive"

    @property
    def is_legendary(self) -> bool:
        return False

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    def load_artwork(self):
        # Content aware fill
        super().load_artwork()
        psd.content_fill_empty_area(self.art_layer)


class FangExtendedTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/FangExtended"
    template_suffix = "Fang Extended"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    def load_artwork(self):
        # Content aware fill
        super().load_artwork()
        psd.content_fill_empty_area(self.art_layer)


class GoldenAgeFullArtTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/GoldenAgeFullArt"
    template_suffix = "Golden Age Full Art"

    def __init__(self, layout):
        cfg.remove_flavor = True
        cfg.remove_reminder = True
        super().__init__(layout)

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


"""
Planeswalker templates
"""


class ClassicPWTemplate (temp.PlaneswalkerTemplate):
    """
     * Planeswalker template - 3 or 4 loyalty abilities.
    """
    template_file_name = "WarpDandy/ClassicPW"
    template_suffix = "Classic PW"

    def __init__(self, layout):
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
                self.text.append(
                    text_classes.TextField(
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

            self.text.append(
                text_classes.BasicFormattedTextField(
                    layer = ability_layer,
                    text_contents = ability,
                    text_color = psd.get_text_layer_color(ability_layer),
                )
            )

        # starting loyalty
        self.text.append(
            text_classes.TextField(
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


class ArtDecoPWTemplate (temp.PlaneswalkerTemplate):
    """
     * Planeswalker template - 3 or 4 loyalty abilities.
    """
    template_file_name = "WarpDandy/ArtDecoPW"
    template_suffix = "Art Deco PW"

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
                self.text.append(
                    text_classes.TextField(
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

            self.text.append(
                text_classes.BasicFormattedTextField(
                    layer = ability_layer,
                    text_contents = ability,
                    text_color = psd.get_text_layer_color(ability_layer),
                )
            )

        # starting loyalty
        self.text.append(
            text_classes.TextField(
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
