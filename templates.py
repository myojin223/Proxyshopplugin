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
    PlaneswalkerTemplate,
    NormalEssentialsTemplate
)
import src.text_layers as text_classes
import src.helpers as psd
from src.settings import cfg
from src.enums.photoshop import Dimensions
from src.enums.layers import LAYERS


class SamuraiTemplate (NormalEssentialsTemplate):
    """
     * Created by WarpDandy.
     * Samurai frame introduced in Kamigawa Neon Dynasty.
    """
    template_suffix = "Samurai"

    """
    TOGGLE
    """

    @cached_property
    def is_land(self) -> bool:
        return False

    """
    LAYERS
    """

    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    def enable_crown(self) -> None:
        # No separate border, no hollow, enable pinlines mask
        self.crown_layer.visible = True


class NinjaTemplate (NormalEssentialsTemplate):
    """
     * Created by WarpDandy.
     * Ninja frame introduced in Kamigawa Neon Dynasty.
    """
    template_suffix = "Ninja"

    """
    TOGGLE
    """

    @cached_property
    def is_land(self) -> bool:
        return False

    """
    LAYERS
    """

    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
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
    TOGGLE
    """

    @cached_property
    def is_land(self) -> bool:
        return False

    """
    LAYERS
    """

    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
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
    def expansion_symbol_alignments(self) -> list[Dimensions]:
        return [Dimensions.Left, Dimensions.CenterY]

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


class BorderlessIkoria (NormalTemplate):
    """
     * Created by WarpDandy.
     * Ikoria Borderless variant with smokey textbox.
    """
    template_suffix = "Borderless Ikoria"

    @cached_property
    def is_land(self) -> bool:
        return False

    @cached_property
    def is_fullart(self) -> bool:
        return True

    @cached_property
    def is_content_aware_enabled(self) -> bool:
        return True

    """
    LAYERS
    """

    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    """
    CROWN
    """

    def enable_crown(self) -> None:
        """Enable the Legendary crown."""
        self.crown_layer.visible = True

        # Nyx/Companion: Enable the hollow crown shadow and layer mask on crown, pinlines, and shadows
        if self.is_nyx or self.is_companion:
            self.enable_hollow_crown()

            # Enable nyx or companion texture
            if self.is_nyx:
                psd.getLayer(self.background, LAYERS.NYX).visible = True
            elif self.is_companion:
                self.companion_layer.visible = True

    def enable_hollow_crown(self, shadows: Optional[ArtLayer] = None) -> None:
        """Enable the hollow legendary crown."""
        psd.enable_mask(self.crown_layer.parent)
        psd.enable_mask(self.pinlines_layer.parent)
        self.crown_shadow_layer.visible = True


class GoldenAgeTemplate (NormalEssentialsTemplate):
    """
     * Created by WarpDandy
     * Golden Age template introduced in Streets of New Capenna.
    """
    template_suffix = "Golden Age"

    """
    SETTINGS
    """

    @cached_property
    def is_dark_mode(self) -> bool:
        """Whether to use 'Dark Mode' layers."""
        return bool(cfg.get_setting('FRAME', 'Dark.Mode', default=False))

    """
    LAYERS
    """

    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def pt_layer(self) -> Optional[ArtLayer]:
        # Not separated by color
        return psd.getLayerSet(LAYERS.PT_BOX)

    @cached_property
    def pinlines_layer(self) -> Optional[ArtLayer]:
        # Select either normal or dark version
        if self.is_dark_mode:
            return psd.getLayer(self.pinlines, f"{LAYERS.PINLINES_TEXTBOX} Dark")
        return psd.getLayer(self.pinlines, LAYERS.PINLINES_TEXTBOX)

    """
    METHODS
    """

    def enable_crown(self) -> None:
        # Legendary border not separate, no hollow crown
        self.crown_layer.visible = True


class GoldenAgeFullArtTemplate (GoldenAgeTemplate):
    """
     * Created by WarpDandy
     * Fullart version of the Golden Age template introduced in Streets of New Capenna.
    """
    template_suffix = "Golden Age Fullart"

    """
    TOGGLE
    """

    @cached_property
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


class ExpeditionClassicTemplate (NormalEssentialsTemplate):
    """
     * Created by WarpDandy
     * Original Expedition template introduced in the Battle for Zendikar block.
    """
    template_suffix = "BFZ Expedition"

    """
    TOGGLE
    """

    @cached_property
    def is_land(self) -> bool:
        # No separate land Pinlines group
        return False

    @cached_property
    def is_legendary(self) -> bool:
        # No Legendary Crown
        return False

    @cached_property
    def is_fullart(self) -> bool:
        # Prefer vertical art
        return True

    """
    LAYERS
    """

    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        # No Background group
        return

    @cached_property
    def twins_layer(self) -> Optional[ArtLayer]:
        # No Name & Title Boxes group
        return


class SkyscraperTemplate (NormalEssentialsTemplate):
    """
     * Created by WarpDandy
     * Skyscraper template introduced in Streets of New Capenna.
    """
    template_suffix = "Skyscraper"

    """
    TOGGLE
    """

    @cached_property
    def is_land(self) -> bool:
        return False

    @cached_property
    def is_legendary(self) -> bool:
        return False

    """
    LAYERS
    """

    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class ArtDecoTemplate (NormalEssentialsTemplate):
    """
     * Created by WarpDandy
     * Art Deco template introduced in Streets of New Capenna.
    """
    template_suffix = "Art Deco"

    """
    LAYERS
    """

    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class DestinyTemplate (NormalEssentialsTemplate):
    """
     * Created by Meeple, ported to Proxyshop by WarpDandy.
    """
    template_suffix = "Destiny"

    """
    TOGGLE
    """

    @cached_property
    def is_land(self) -> bool:
        return False

    """
    LAYERS
    """

    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
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

    @cached_property
    def is_nyx(self) -> bool:
        return False

    @cached_property
    def is_companion(self) -> bool:
        return False

    """
    LAYERS
    """

    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
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

    @cached_property
    def is_legendary(self) -> bool:
        # Crowns not supported
        return False

    @cached_property
    def is_land(self) -> bool:
        # No separate pinlines
        return False

    """
    LAYERS
    """

    @cached_property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def pt_layer(self) -> Optional[ArtLayer]:
        # Not separated by color
        return psd.getLayer(LAYERS.PT_BOX)


class FangExtendedTemplate (ExtendedTemplate):
    """
     * Created by WarpDandy
     * Extended version of the Crimson Fang template introduced in Innistrad: Crimson Vow.
    """
    template_suffix = "Fang Extended"

    """
    DETAILS
    """

    @cached_property
    def background(self):
        # Use pinlines colors for background
        return self.pinlines

    """
    TOGGLE
    """

    @cached_property
    def is_nyx(self) -> bool:
        return False

    """
    LAYERS
    """

    @cached_property
    def pinlines_layer(self) -> Optional[ArtLayer]:
        # Support backside colors
        if self.is_land:
            return psd.getLayer(self.pinlines, LAYERS.LAND_PINLINES_TEXTBOX)
        if self.is_transform and not self.is_front:
            return psd.getLayer(self.pinlines, "MDFC " + LAYERS.PINLINES_TEXTBOX)
        return psd.getLayer(self.pinlines, LAYERS.PINLINES_TEXTBOX)

    def enable_crown(self) -> None:
        # No border swap
        self.crown_layer.visible = True


class TardisTemplate (NormalEssentialsTemplate):
    """
     * Created by WarpDandy
     * Taris template introduced in WOE.
    """
    template_suffix = "Tardis"

    """
    LAYERS
    """

    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def twins_layer(self) -> Optional[ArtLayer]:
        return



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

    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def ability_divider(self) -> Optional[ArtLayer]:
        div = cfg.get_setting(section="TEXT", key="Ability.Divider", default="Modern", is_bool=False)
        if div == "Modern":
            return psd.getLayer(LAYERS.DIVIDER, self.loyalty_group)
        if div == "Classic":
            return psd.getLayer("Divider Block", self.loyalty_group)
        return

    """
    REFERENCES
    """

    @cached_property
    def top_ref(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def adj_ref(self) -> Optional[ArtLayer]:
        return

    """
    GROUPS
    """

    @cached_property
    def group(self) -> LayerSet:
        return psd.getLayerSet("Planeswalker")

    """
    METHODS
    """

    def collector_info_authentic(self) -> None:
        # Pulled from NormalClassicTemplate.
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
        number = self.layout.collector_data[:-2] if (
            '/' in self.layout.collector_data
        ) else self.layout.collector_data[2:]

        # Apply the collector info
        psd.replace_text(info, "NUM", number)
        psd.replace_text(info, "SET", self.layout.set)
        psd.replace_text(artist, "Artist", self.layout.artist)

    def pw_add_ability(self, ability: dict) -> None:
        """
        Add a Planeswalker ability.
        @param ability: Planeswalker ability data.
        """
        # Create an icon and colon if this isn't a static ability
        static = False if ability.get('icon') and ability.get('cost') else True
        icon = None if static else psd.getLayer(LAYERS.COST, self.loyalty_group).duplicate()
        colon = None if static else self.text_layer_colon.duplicate()

        # Update ability cost if needed
        if not static:
            if len(ability.get('cost')) > 2:
                icon.textItem.size = (psd.get_text_scale_factor(icon) * icon.textItem.size) - 1
                icon.translate(0, -4)
            icon.textItem.contents = ability.get('cost', '0')

        # Add ability, icons, and colons
        self.icons.append(icon)
        self.colons.append(colon)
        self.ability_layers.append(
            self.text_layer_static.duplicate() if static
            else self.text_layer_ability.duplicate())
        self.text.append(
            text_classes.FormattedTextField(
                layer=self.ability_layers[-1],
                contents=ability.get('text', '')
            ))

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
