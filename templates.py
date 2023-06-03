"""
WARPDANDY TEMPLATES
"""
# Standard Library Imports
from functools import cached_property
from typing import Optional, Union

# Third Party Imports
from photoshop.api._layerSet import LayerSet
from photoshop.api._artlayer import ArtLayer
import photoshop.api as ps

# Local Imports
from src.templates import (
    NormalTemplate,
    ExtendedTemplate,
    BorderlessTemplate,
    PlaneswalkerTemplate
)
import src.format_text as ft
import src.text_layers as text_classes
import src.helpers as psd
from src.settings import cfg
from src.enums.photoshop import Alignment
from src.enums.layers import LAYERS


class SamuraiTemplate (NormalTemplate):
    """
     * Created by WarpDandy.
     * Samurai frame introduced in Kamigawa Neon Dynasty.
    """
    template_suffix = "Samurai"

    """
    TOGGLE
    """

    @property
    def is_land(self) -> bool:
        return False

    """
    LAYERS
    """

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    def enable_crown(self) -> None:
        # No separate border, no hollow, enable pinlines mask
        self.crown_layer.visible = True


class NinjaTemplate (NormalTemplate):
    """
     * Created by WarpDandy.
     * Ninja frame introduced in Kamigawa Neon Dynasty.
    """
    template_suffix = "Ninja"

    """
    LAYERS
    """

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    """
    METHODS
    """

    def enable_crown(self) -> None:
        # No separate border, no hollow, enable pinlines mask
        self.crown_layer.visible = True

 
class NinjaGlitchTemplate (ExtendedTemplate):
    """
     * Created by WarpDandy.
     * Glitch version of the Ninja extended frame introduced in Kamigawa Neon Dynasty.
    """
    template_suffix = "Glitch Ninja"

    """
    LAYERS
    """

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    """
    METHODS
    """

    def enable_crown(self) -> None:
        # No separate border, no hollow, enable pinlines mask
        self.crown_layer.visible = True


class MirroredTemplate (NormalTemplate):
    """
     * Created by WarpDandy.
     * Mirrored frame introduced in the April Fool's Secret Lair reveal.
    """
    template_suffix = "Mirrored"

    """
    PROPERTIES
    """

    @cached_property
    def expansion_symbol_alignments(self) -> list[Alignment]:
        return [Alignment.CenterVertical, Alignment.Left]

    """
    METHODS
    """

    def load_artwork(self):
        # Flip artwork
        super().load_artwork()
        self.active_layer.resize(-100, 100, ps.AnchorPosition.MiddleCenter)

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


class NicknameBaseTemplate (BorderlessTemplate):
    """
     * Created by WarpDandy.
     * Fullart Nickname template introduced in the Ikoria: Lair of Behemoths Godzilla promos.
     * Must enter Nickname text manually.
    """
    template_suffix = "Nickname"

    def __init__(self, layout):
        cfg.exit_early = True
        super().__init__(layout)

    """
    TOGGLE
    """

    @property
    def is_land(self) -> bool:
        return False

    """
    LAYERS
    """

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    def enable_crown(self) -> None:
        # No separate border, no hollow, enable pinlines mask
        self.crown_layer.visible = True


class NicknameSmallTemplate(NicknameBaseTemplate):
    """
     * Created by WarpDandy.
     * Nickname template with small textbox.
    """
    template_suffix = "Nickname Small"


class NicknameMediumTemplate(NicknameBaseTemplate):
    """
     * Created by WarpDandy.
     * Nickname template with medium textbox.
    """
    template_suffix = "Nickname Medium"


class NicknameLargeTemplate(NicknameBaseTemplate):
    """
     * Created by WarpDandy.
     * Nickname template with large textbox.
    """
    template_suffix = "Nickname Large"


class NoBorderTemplate (ExtendedTemplate):
    """
     * Created by WarpDandy.
     * A simple template without a border.
    """
    template_suffix = "NB"

    def __init__(self, layout):
        cfg.exit_early = False
        super().__init__(layout)

    """
    TOGGLE
    """

    @property
    def is_nyx(self) -> bool:
        return False
    
    @property
    def is_companion(self) -> bool:
        return False

    """
    LAYERS
    """

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def art_reference(self) -> Optional[ArtLayer]:
        return psd.getLayer(LAYERS.ART_FRAME)


class GoldenAgeTemplate (NormalTemplate):
    """
     * Created by WarpDandy
     * Golden Age template introduced in Streets of New Capenna.
    """
    template_suffix = "Golden Age"

    """
    TOGGLE
    """

    @property
    def is_land(self) -> bool:
        return False

    @property
    def is_nyx(self) -> bool:
        return False

    """
    LAYERS
    """

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def pt_layer(self) -> Optional[ArtLayer]:
        # Not separated by color
        return psd.getLayerSet(LAYERS.PT_BOX)

    @cached_property
    def divider_layer(self) -> Optional[ArtLayer]:
        # Divider is a group
        return psd.getLayerSet(LAYERS.DIVIDER, self.text_group)

    def enable_crown(self) -> None:
        # Legendary border not separate, no hollow crown
        self.crown_layer.visible = True


class GoldenAgeV2Template (GoldenAgeTemplate):
    """
     * Created by WarpDandy
     * Alternate version of the Golden Age template introduced in Streets of New Capenna.
     * Has more color on pinlines and brushed highlights on textures.
    """
    template_suffix = "Golden Age V2"


class GoldenAgeFullArtTemplate (GoldenAgeTemplate):
    """
     * Created by WarpDandy
     * Fullart version of the Golden Age template introduced in Streets of New Capenna.
    """
    template_suffix = "Golden Age Fullart"

    """
    TOGGLE
    """

    @property
    def is_fullart(self) -> bool:
        return True

    """
    LAYERS
    """

    @cached_property
    def text_layer_rules(self) -> Optional[ArtLayer]:
        if not self.is_creature:
            self.text_layer_pt.visible = False
        # No separate text layer for creatures
        return psd.getLayer(LAYERS.RULES_TEXT_NONCREATURE, self.text_group)


class ExpeditionClassicTemplate (NormalTemplate):
    """
     * Created by WarpDandy
     * Original Expedition template introduced in the Battle for Zendikar block.
    """
    template_suffix = "BFZ Expedition"

    """
    TOGGLE
    """

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_legendary(self) -> bool:
        return False

    """
    LAYERS
    """

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class SkyscraperTemplate (NormalTemplate):
    """
     * Created by WarpDandy
     * Skyscraper template introduced in Streets of New Capenna.
    """
    template_suffix = "Skyscraper"

    """
    TOGGLE
    """

    @property
    def is_land(self) -> bool:
        return False

    @property
    def is_legendary(self) -> bool:
        return False

    """
    LAYERS
    """

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class ArtDecoTemplate (NormalTemplate):
    """
     * Created by WarpDandy
     * Art Deco template introduced in Streets of New Capenna.
    """
    template_suffix = "Art Deco"

    """
    TOGGLE
    """

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def is_nyx(self) -> bool:
        return False

    """
    LAYERS
    """

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class DestinyTemplate (NormalTemplate):
    """
     * Created by Meeple, ported to Proxyshop by WarpDandy.
    """
    template_suffix = "Destiny"

    """
    TOGGLE
    """

    @property
    def is_land(self) -> bool:
        return False

    """
    LAYERS
    """

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def pt_layer(self) -> Optional[ArtLayer]:
        # Same for all colors
        return psd.getLayer(LAYERS.PT_BOX)

    @cached_property
    def crown_layer(self) -> Optional[ArtLayer]:
        # Same for all colors
        return psd.getLayer(LAYERS.LEGENDARY_CROWN)

    """
    METHODS
    """

    def enable_crown(self) -> None:
        # No border swap, no hollow crown
        self.crown_layer.visible = True

        
class NeonPinlinesExtendedTemplate (ExtendedTemplate):
    """
     * Created by WarpDandy
     * Extended template with neon pinlines.
    """
    template_suffix = "Neon Extended"

    """
    TOGGLE
    """

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    """
    LAYERS
    """

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def pinlines_layer(self) -> Optional[ArtLayer]:
        # No separate land layers
        return psd.getLayer(self.layout.pinlines, LAYERS.PINLINES_TEXTBOX)

    """
    METHODS
    """

    def enable_crown(self) -> None:
        # No separate border, no hollow, enable pinlines mask
        self.crown_layer.visible = True
        psd.enable_mask(self.pinlines_layer.parent)


class MysticalArchiveTemplate (BorderlessTemplate):
    """
     * Created by WarpDandy
     * Mystical Archive (English) template introduced in Strixhaven: School of Mages.
    """
    template_suffix = "Mystical Archive"

    """
    TOGGLE
    """

    @property
    def is_legendary(self) -> bool:
        # Crowns not supported
        return False

    @property
    def is_land(self) -> bool:
        # No separate pinlines
        return False

    """
    LAYERS
    """

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def pt_layer(self) -> Optional[ArtLayer]:
        # Not separated by color
        return psd.getLayer(LAYERS.PT_BOX)


class FangExtendedTemplate (ExtendedTemplate):
    """
     * Created by WarpDandy
     * Extended version of the Crimson Fang template introduced in Innistrad: Crimson Vow.
    """
    template_suffix = "Fang Extended"

    @property
    def is_nyx(self) -> bool:
        return False

    def enable_crown(self) -> None:
        # No border swap
        self.crown_layer.visible = True


"""
Planeswalker templates
"""


class ClassicPWTemplate (PlaneswalkerTemplate):
    """
     * Created by WarpDandy.
     * Classic version of the Planeswalker template.
    """
    template_suffix = "Classic PW"

    """
    LAYERS
    """

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

    """
    METHODS
    """

    def collector_info_authentic(self) -> None:
        """
        Called to generate realistic collector info.
        """
        # Hide basic layers
        psd.getLayer(LAYERS.ARTIST, self.legal_group).visible = False
        psd.getLayer(LAYERS.SET, self.legal_group).visible = False

        # Get the collector layers
        collector_group = psd.getLayerSet(LAYERS.COLLECTOR, LAYERS.LEGAL)
        artist = psd.getLayer(LAYERS.TOP_LINE, collector_group)
        info = psd.getLayer(LAYERS.BOTTOM_LINE, collector_group)
        collector_group.visible = True

        # Correct color for non-black border
        if self.border_color != 'black':
            artist.textItem.color = psd.rgb_black()
            info.textItem.color = psd.rgb_black()

        # Establish the collector data
        if '/' in self.layout.collector_data:
            number = self.layout.collector_data[:-2]
        else:
            number = self.layout.collector_data[2:]

        # Apply the collector info
        psd.replace_text(info, "NUM", number)
        psd.replace_text(info, "SET", self.layout.set)
        psd.replace_text(artist, "Artist", self.layout.artist)

    def basic_text_layers(self):

        # Iterate through abilities to add text layers
        for i, ability in enumerate(self.abilities):

            # Get the colon index, determine if this is static or activated ability
            colon_index = ability.find(": ")
            if 5 > colon_index > 0:

                # Determine which loyalty group to enable, and set the loyalty symbol's text
                loyalty_graphic = psd.getLayer(LAYERS.COST, self.loyalty_group).duplicate()
                loyalty_graphic.textItem.contents = ability[:int(colon_index)]
                if colon_index > 2:
                    loyalty_graphic.textItem.size = (
                            psd.get_text_scale_factor(loyalty_graphic) * loyalty_graphic.textItem.size
                    ) - 1
                    loyalty_graphic.translate(0, -4)
                ability_layer = psd.getLayer(LAYERS.ABILITY_TEXT, self.loyalty_group).duplicate()

                # Add text layer, shields, and colons to list
                self.ability_layers.append(ability_layer)
                self.shields.append(loyalty_graphic)
                self.colons.append(psd.getLayer(LAYERS.COLON, self.loyalty_group).duplicate())
                ability = ability[colon_index + 2:]

            else:

                # Hide default ability, switch to static
                ability_layer = psd.getLayer(LAYERS.STATIC_TEXT, self.loyalty_group).duplicate()
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
        if self.layout.loyalty:
            self.loyalty_text.textItem.contents = self.layout.loyalty
        else:
            self.loyalty_text.parent.visible = False

        # Add text layers.
        super(PlaneswalkerTemplate, self).basic_text_layers()

    def pw_ability_mask(self):
        # Position a divider between each ability layer
        if self.ability_divider:
            for i in range(len(self.ability_layers) - 1):
                divider = self.ability_divider.duplicate()
                psd.position_between_layers(divider, self.ability_layers[i], self.ability_layers[i+1])
                if self.ability_divider.name != "Divider Block":
                    divider.translate(0, -6)


class ArtDecoPWTemplate (PlaneswalkerTemplate):
    """
     * Created by WarpDandy.
     * Art Deco version of the Planeswalker template.
    """
    template_suffix = "Art Deco"

    @cached_property
    def twins_layer(self) -> Optional[ArtLayer]:
        layer = psd.getLayer(self.pinlines, LAYERS.TWINS)
        layer.move(self.pinlines_layer, ps.ElementPlacement.PlaceBefore)
        return layer

    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def border_group(self) -> Union[None, ArtLayer, LayerSet]:
        return psd.getLayer(LAYERS.BORDER)
