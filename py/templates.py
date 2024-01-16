"""
* Warpdandy Templates
"""
# Standard Library Imports
from functools import cached_property
from typing import Optional

# Third Party Imports
from photoshop.api._layerSet import LayerSet
from photoshop.api._artlayer import ArtLayer
from photoshop.api import AnchorPosition, ElementPlacement

# Local Imports
from src import CFG
from src.templates import (
    FullartMod,
    M15Template,
    ExtendedMod,
    BorderlessMod,
    NormalTemplate,
    PlaneswalkerTemplate,
    VectorTemplate)
import src.text_layers as text_classes
import src.helpers as psd
from src.enums.adobe import Dimensions
from src.enums.layers import LAYERS


"""
* Template Classes
"""


class SamuraiTemplate (NormalTemplate):
    """
     * Created by WarpDandy.
     * Samurai frame introduced in Kamigawa Neon Dynasty.
    """
    template_suffix = "Samurai"

    # Static Properties
    is_land = False
    background_layer = None
    twins_layer = None

    """
    * Frame Layer Methods
    """

    def enable_crown(self) -> None:
        """No separate border, no hollow, enable pinlines mask."""
        self.crown_layer.visible = True


class NinjaTemplate (NormalTemplate):
    """
     * Created by WarpDandy.
     * Ninja frame introduced in Kamigawa Neon Dynasty.
    """
    template_suffix = "Ninja"

    # Static Properties
    is_land = False
    background_layer = None
    twins_layer = None

    """
    * Frame Layer Methods
    """

    def enable_crown(self) -> None:
        """No separate border, no hollow, enable pinlines mask."""
        self.crown_layer.visible = True

 
class NinjaGlitchTemplate (ExtendedMod, NormalTemplate):
    """
     * Created by WarpDandy.
     * Glitch version of the Ninja extended frame introduced in Kamigawa Neon Dynasty.
    """
    template_suffix = "Glitch Ninja"

    # Static Properties
    is_land = False
    background_layer = None
    twins_layer = None

    """
    * Frame Layer Methods
    """

    def enable_crown(self) -> None:
        """No separate border, no hollow, enable pinlines mask."""
        self.crown_layer.visible = True


class MirroredTemplate (M15Template):
    """
     * Created by WarpDandy.
     * Mirrored frame introduced in the April Fool's Secret Lair reveal.
    """
    template_suffix = "Mirrored"

    """
    * Expansion Symbol
    """

    @cached_property
    def expansion_symbol_alignments(self) -> list[Dimensions]:
        return [Dimensions.Left, Dimensions.CenterY]

    """
    * Art Methods
    """

    def load_artwork(self):
        """Flip artwork."""
        super().load_artwork()
        self.active_layer.resize(-100, 100, AnchorPosition.MiddleCenter)

    """
    * Text Layer Methods
    """

    def basic_text_layers(self):
        """Flip scaling on text layers."""
        self.text.extend([
            text_classes.FormattedTextField(
                layer=self.text_layer_mana,
                contents=self.layout.mana_cost
            ),
            text_classes.ScaledTextFieldLeft(
                layer=self.text_layer_name,
                contents=self.layout.name,
                reference=self.name_reference
            ),
            text_classes.ScaledTextFieldLeft(
                layer=self.text_layer_type,
                contents=self.layout.type_line,
                reference=self.type_reference
            )
        ])


class BorderlessIkoria (BorderlessMod, M15Template):
    """
     * Created by WarpDandy.
     * Ikoria Borderless variant with smokey textbox.
    """
    template_suffix = "Borderless Ikoria"

    # Static Properties
    is_land = False
    twins_layer = None

    """
    * Layer Properties
    """

    @cached_property
    def background_layer(self) -> Optional[ArtLayer]:
        if self.is_legendary and self.is_nyx:
            return psd.getLayer(self.background, LAYERS.NYX)
        return

    """
    * Crown
    """

    def enable_crown(self) -> None:
        """Enable the Legendary crown."""
        self.crown_layer.visible = True

        # Call hollow crown step
        if self.is_hollow_crown:
            self.enable_hollow_crown()


class GoldenAgeTemplate (NormalTemplate):
    """
     * Created by WarpDandy
     * Golden Age template introduced in Streets of New Capenna.
    """
    template_suffix = "Golden Age"

    # Static Properties
    background_layer = None
    twins_layer = None

    """
    * Settings
    """

    @cached_property
    def is_dark_mode(self) -> bool:
        """Whether to use 'Dark Mode' layers."""
        return bool(CFG.get_setting('FRAME', 'Dark.Mode', default=False))

    """
    * Frame Layers
    """

    @cached_property
    def pt_layer(self) -> LayerSet:
        """LayerSet: Not separated by color."""
        return psd.getLayerSet(LAYERS.PT_BOX)

    @cached_property
    def pinlines_layer(self) -> ArtLayer:
        """ArtLayer: Select either normal or dark version."""
        if self.is_dark_mode:
            return psd.getLayer(self.pinlines, f"{LAYERS.PINLINES_TEXTBOX} Dark")
        return psd.getLayer(self.pinlines, LAYERS.PINLINES_TEXTBOX)

    """
    * Frame Layer Methods
    """

    def enable_crown(self) -> None:
        """Legendary border not separate, no hollow crown."""
        self.crown_layer.visible = True


class GoldenAgeFullArtTemplate (FullartMod, GoldenAgeTemplate):
    """
     * Created by WarpDandy
     * Fullart version of the Golden Age template introduced in Streets of New Capenna.
    """
    template_suffix = "Golden Age"

    """
    * Frame Layers
    """

    @cached_property
    def text_layer_rules(self) -> ArtLayer:
        """ArtLayer: No separate text layer for creatures."""
        return psd.getLayer(LAYERS.RULES_TEXT_NONCREATURE, self.text_group)


class ExpeditionClassicTemplate (FullartMod, NormalTemplate):
    """
     * Created by WarpDandy
     * Original Expedition template introduced in the Battle for Zendikar block.
    """
    template_suffix = "BFZ Expedition"

    # Static Properties
    is_land = False
    is_legendary = False
    background_layer = None
    twins_layer = None


class SkyscraperTemplate (NormalTemplate):
    """
     * Created by WarpDandy
     * Skyscraper template introduced in Streets of New Capenna.
    """
    template_suffix = "Skyscraper"

    # Static Properties
    is_land = False
    is_legendary = False
    background_layer = None
    twins_layer = None


class ArtDecoTemplate (NormalTemplate):
    """
     * Created by WarpDandy
     * Art Deco template introduced in Streets of New Capenna.
    """
    template_suffix = "Art Deco"

    # Static Properties
    background_layer = None
    twins_layer = None

    """
    * Frame Layers
    """

    @cached_property
    def pinlines_layer(self) -> ArtLayer:
        """ArtLayer: No delineation for Land cards."""
        return psd.getLayer(self.layout.pinlines, LAYERS.PINLINES_TEXTBOX)


class DestinyTemplate (NormalTemplate):
    """
     * Created by Meeple, ported to Proxyshop by WarpDandy.
    """
    template_suffix = "Destiny"

    # Static Properties
    is_land = False
    background_layer = None
    twins_layer = None

    """
    * Frame Layers
    """

    @cached_property
    def pt_layer(self) -> ArtLayer:
        """ArtLayer: Same for all colors."""
        return psd.getLayer(LAYERS.PT_BOX)

    @cached_property
    def crown_layer(self) -> ArtLayer:
        """ArtLayer: Same for all colors."""
        return psd.getLayer(LAYERS.LEGENDARY_CROWN)

    """
    * Frame Layer Methods
    """

    def enable_crown(self) -> None:
        """No border swap, no hollow crown."""
        self.crown_layer.visible = True

        
class NeonPinlinesExtendedTemplate (ExtendedMod, NormalTemplate):
    """
     * Created by WarpDandy
     * Extended template with neon pinlines.
    """
    template_suffix = "Neon Extended"

    # Static Properties
    background_layer = None
    twins_layer = None

    """
    * Frame Layers
    """

    @cached_property
    def pinlines_layer(self) -> ArtLayer:
        """ArtLayer: No delineation for Land cards."""
        return psd.getLayer(self.layout.pinlines, LAYERS.PINLINES_TEXTBOX)

    """
    * Frame Layer Methods
    """

    def enable_crown(self) -> None:
        """No separate border, no hollow, enable pinlines mask."""
        self.crown_layer.visible = True
        psd.enable_mask(self.pinlines_layer.parent)


class MysticalArchiveTemplate (BorderlessMod, NormalTemplate):
    """
     * Created by WarpDandy
     * Mystical Archive (English) template introduced in Strixhaven: School of Mages.
    """
    template_suffix = "Mystical Archive"

    # Static Properties
    is_legendary = False
    is_land = False
    twins_layer = None

    """
    * Frame Layers
    """

    @cached_property
    def pt_layer(self) -> ArtLayer:
        """ArtLayer: Not differentiated by color."""
        return psd.getLayer(LAYERS.PT_BOX)


class FangExtendedTemplate (ExtendedMod, NormalTemplate):
    """
     * Created by WarpDandy
     * Extended version of the Crimson Fang template introduced in Innistrad: Crimson Vow.
    """
    template_suffix = "Fang Extended"

    """
    * Frame Details
    """

    @cached_property
    def background(self) -> str:
        """Use pinlines colors for background."""
        return self.pinlines

    """
    * Frame Layers
    """

    @cached_property
    def pinlines_layer(self) -> Optional[ArtLayer]:
        """Support backside colors."""
        if self.is_land:
            return psd.getLayer(self.pinlines, LAYERS.LAND_PINLINES_TEXTBOX)
        if self.is_transform and not self.is_front:
            return psd.getLayer(self.pinlines, "MDFC " + LAYERS.PINLINES_TEXTBOX)
        return psd.getLayer(self.pinlines, LAYERS.PINLINES_TEXTBOX)

    """
    * Frame Layer Methods
    """

    def enable_crown(self) -> None:
        """Enable a single layer, no border change."""
        self.crown_layer.visible = True


class TardisTemplate (VectorTemplate):
    """
     * Created by WarpDandy
     * Tardis template introduced in WOE.
    """
    template_suffix = "Tardis"

    """
    * Frame Layers
    """

    @cached_property
    def pt_layer(self) -> ArtLayer:
        """ArtLayer: Not separated by colors."""
        return psd.getLayer(LAYERS.PT_BOX, self.docref)

    """
    * Expansion Symbol
    """

    @property
    def expansion_symbol_alignments(self) -> list[Dimensions]:
        """Alignments used for positioning the expansion symbol"""
        return [Dimensions.CenterX, Dimensions.CenterY]

    def load_expansion_symbol(self) -> None:
        """Imports and positions the expansion symbol SVG image."""

        # Check for expansion symbol disabled
        if not CFG.symbol_enabled or not self.expansion_reference:
            return
        if not self.layout.symbol_svg:
            return self.log("Expansion symbol disabled, SVG file not found.")

        # Try to import the expansion symbol
        try:

            # Import and place the symbol
            svg = psd.import_svg(
                path=str(self.layout.symbol_svg),
                ref=self.expansion_reference,
                placement=ElementPlacement.PlaceBefore,
                docref=self.docref)

            # Frame the symbol
            psd.frame_layer(
                layer=svg,
                ref=self.expansion_reference,
                smallest=True,
                alignments=self.expansion_symbol_alignments)

            # Rename and reset property
            svg.name = 'Expansion Symbol'
            self.expansion_symbol_layer = svg

        except Exception as e:
            return self.log('Expansion symbol disabled due to an error.', e)

    """
    * Frame Layer Methods
    """

    def enable_frame_layers(self) -> None:
        """Enable layers which make-up the frame of the card."""

        # PT Box
        if self.is_creature:
            self.pt_layer.visible = True

        # Pinlines
        self.generate_layer(
            group=self.pinlines_group,
            colors=self.pinlines,
            masks=self.mask_layers)

        # Color Indicator -> Blended solid color layers
        if self.is_type_shifted:
            self.generate_layer(
                group=self.indicator_group,
                colors=self.indicator_colors,
                masks=self.indicator_masks)

        # Legendary crown
        if self.is_legendary:
            self.generate_layer(
                group=self.crown_group,
                colors=self.pinlines,
                masks=self.mask_layers)


"""
Planeswalker templates
"""


class ClassicPWTemplate (PlaneswalkerTemplate):
    """
     * Created by WarpDandy.
     * Classic version of the Planeswalker template.
    """
    template_suffix = "Classic PW"

    # Static Properties
    loyalty_reference = None
    background_layer = None
    twins_layer = None

    @cached_property
    def ability_divider(self) -> Optional[ArtLayer]:
        div = CFG.get_setting(section="TEXT", key="Ability.Divider", default="Modern", is_bool=False)
        if div == 'Modern':
            return psd.getLayer(LAYERS.DIVIDER, self.loyalty_group)
        if div == 'Classic':
            return psd.getLayer("Divider Block", self.loyalty_group)
        return

    """
    * Groups
    """

    @cached_property
    def group(self) -> LayerSet:
        return psd.getLayerSet(LAYERS.PLANESWALKER)

    """
    * Text Layer Methods
    """

    def collector_info_authentic(self) -> None:
        # Pulled from NormalClassicTemplate.
        psd.getLayer(LAYERS.ARTIST, self.legal_group).visible = False
        psd.getLayer(LAYERS.SET, self.legal_group).visible = False

        # Get the collector layers
        collector_group = psd.getLayerSet(LAYERS.COLLECTOR, LAYERS.LEGAL)
        artist = psd.getLayer(LAYERS.TOP, collector_group)
        info = psd.getLayer(LAYERS.BOTTOM, collector_group)
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

    """
    * Planeswalker Frame Layer Methods
    """

    def pw_ability_mask(self):
        """Position a divider between each ability layer."""
        if self.ability_divider:
            for i in range(len(self.ability_layers) - 1):
                divider = self.ability_divider.duplicate()
                psd.position_between_layers(divider, self.ability_layers[i], self.ability_layers[i+1])
                if self.ability_divider.name != "Divider Block":
                    divider.translate(0, -6)

    """
    * Planeswalker Utility Methods
    """

    def pw_add_ability(self, ability: dict) -> None:
        """Add a Planeswalker ability.

        Args:
            ability: Planeswalker ability data.
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


class ArtDecoPWTemplate (PlaneswalkerTemplate):
    """
     * Created by WarpDandy.
     * Art Deco version of the Planeswalker template.
    """
    template_suffix = "Art Deco"

    # Static Properties
    background_layer = None

    """
    * Frame Layers
    """

    @cached_property
    def twins_layer(self) -> Optional[ArtLayer]:
        layer = psd.getLayer(self.pinlines, LAYERS.TWINS)
        layer.move(self.pinlines_layer, ElementPlacement.PlaceBefore)
        return layer

    """
    * Groups
    """

    @cached_property
    def border_group(self) -> ArtLayer:
        """ArtLayer: Single rasterized layer."""
        return psd.getLayer(LAYERS.BORDER)
