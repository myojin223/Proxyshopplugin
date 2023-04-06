"""
WARPDANDY TEMPLATES
"""
from functools import cached_property
from typing import Optional

from photoshop.api._layerSet import LayerSet

import src.format_text as ft
import src.text_layers as text_classes
import src.templates as temp
import src.helpers as psd
from src.constants import con
from src.settings import cfg

from photoshop.api._artlayer import ArtLayer
import photoshop.api as ps

from src.utils.enums_photoshop import Alignment

app = ps.Application()


class SamuraiTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
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
                reference=self.expansion_symbol_layer,
                flip_scale=True
            )
        ])

    @cached_property
    def expansion_symbol_alignments(self) -> list[Alignment]:
        return [Alignment.CenterVertical, Alignment.Left]

    def load_artwork(self):
        super().load_artwork()
        self.active_layer.resize(-100, 100, ps.AnchorPosition.MiddleCenter)


class NicknameSmallTemplate (temp.NormalTemplate):
    """
     * Requires manually adding the nickname
    """
    template_suffix = "Nickname S"

    def __init__(self, layout):
        cfg.exit_early = True
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
    template_suffix = "Nickname M"

    def __init__(self, layout):
        cfg.exit_early = True
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


class NicknameLargeTemplate (temp.NormalTemplate):
    """
     * Requires manually adding the nickname
    """
    template_suffix = "Nickname L"

    def __init__(self, layout):
        cfg.exit_early = True
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


class NicknameBaseTemplate (temp.NormalTemplate):
    """
     * Requires manually adding the nickname
    """
    template_suffix = "Nickname"

    def __init__(self, layout):
        cfg.exit_early = True
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


class NoBorderTemplate (temp.NormalTemplate):
    """
     A simple template without a border
    """
    template_suffix = "NB"

    def __init__(self, layout):
        cfg.exit_early = False
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


class GoldenAgeTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_suffix = "Golden Age"

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
    template_suffix = "Golden Age V2"

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


class EtchedTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
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
    template_suffix = "Neon Extended"

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
    template_suffix = "Golden Age Full Art"

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
    template_suffix = "Classic PW"

    def __init__(self, layout):
        cfg.real_collector = False
        super().__init__(layout)

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def group(self) -> LayerSet:
        return psd.getLayerSet("Planeswalker")

    @cached_property
    def ability_divider(self) -> Optional[ArtLayer]:
        div = cfg.get_setting(section="TEXT", key="Ability.Divider", default="Modern", is_bool=False)
        if div == "Modern":
            return psd.getLayer("Divider", self.loyalty_group)
        if div == "Classic":
            return psd.getLayer("Divider Block", self.loyalty_group)
        return

    def basic_text_layers(self):

        # Iterate through abilities to add text layers
        for i, ability in enumerate(self.abilities):

            # Get the colon index, determine if this is static or activated ability
            colon_index = ability.find(": ")
            if 5 > colon_index > 0:

                # Determine which loyalty group to enable, and set the loyalty symbol's text
                loyalty_graphic = psd.getLayer(con.layers.COST, self.loyalty_group).duplicate()
                loyalty_graphic.textItem.contents = ability[:int(colon_index)]
                if colon_index > 2:
                    loyalty_graphic.textItem.size = (
                            psd.get_text_scale_factor(loyalty_graphic) * loyalty_graphic.textItem.size
                    ) - 1
                    loyalty_graphic.translate(0, -4)
                ability_layer = psd.getLayer(con.layers.ABILITY_TEXT, self.loyalty_group).duplicate()

                # Add text layer, shields, and colons to list
                self.ability_layers.append(ability_layer)
                self.shields.append(loyalty_graphic)
                self.colons.append(psd.getLayer(con.layers.COLON, self.loyalty_group).duplicate())
                ability = ability[colon_index + 2:]

            else:

                # Hide default ability, switch to static
                ability_layer = psd.getLayer(con.layers.STATIC_TEXT, self.loyalty_group).duplicate()
                self.ability_layers.append(ability_layer)
                self.shields.append(None)
                self.colons.append(None)

                # Is this a double line ability?
                if "\n" in ability:
                    self.active_layer = ability_layer
                    ft.space_after_paragraph(2)

            # Add ability text
            self.text.append(
                text_classes.FormattedTextField(
                    layer=ability_layer,
                    contents=ability
                )
            )

        # Starting loyalty
        psd.getLayer(
            con.layers.TEXT, [self.loyalty_group, con.layers.STARTING_LOYALTY]
        ).textItem.contents = self.layout.loyalty

        # Add text layers.
        self.text.extend([
            text_classes.FormattedTextField(
                layer=self.text_layer_mana,
                contents=self.layout.mana_cost
            ),
            text_classes.ScaledTextField(
                layer=self.text_layer_name,
                contents=self.layout.name,
                reference=self.text_layer_mana
            ),
            text_classes.ScaledTextField(
                layer=self.text_layer_type,
                contents=self.layout.type_line,
                reference=self.expansion_symbol_layer
            )
        ])

    def pw_ability_mask(self):
        # Position a divider between each ability layer
        if self.ability_divider:
            for i in range(len(self.ability_layers) - 1):
                divider = self.ability_divider.duplicate()
                psd.position_between_layers(divider, self.ability_layers[i], self.ability_layers[i+1])
                if self.ability_divider.name != "Divider Block":
                    divider.translate(0, -6)


class ArtDecoPWTemplate (temp.PlaneswalkerTemplate):
    """
     * Planeswalker template - 3 or 4 loyalty abilities.
    """
    template_suffix = "Art Deco"
