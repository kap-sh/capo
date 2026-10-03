"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer
    import capo_medialive.types.__integer_min0
    import capo_medialive.types.__integer_min0_max10
    import capo_medialive.types.__integer_min0_max255
    import capo_medialive.types.__integer_min96_max600
    import capo_medialive.types.__string
    import capo_medialive.types.burn_in_alignment
    import capo_medialive.types.burn_in_background_color
    import capo_medialive.types.burn_in_destination_subtitle_rows
    import capo_medialive.types.burn_in_font_color
    import capo_medialive.types.burn_in_outline_color
    import capo_medialive.types.burn_in_shadow_color
    import capo_medialive.types.burn_in_teletext_grid_control
    import capo_medialive.types.input_location


class BurnInDestinationSettings(TypedDict, closed=True):
    alignment: NotRequired["capo_medialive.types.burn_in_alignment.BurnInAlignment"]
    """If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting "smart" justification will left-justify live subtitles and center-justify pre-recorded subtitles. All burn-in and DVB-Sub font settings must match."""
    background_color: NotRequired[
        "capo_medialive.types.burn_in_background_color.BurnInBackgroundColor"
    ]
    """Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match."""
    background_opacity: NotRequired[
        "capo_medialive.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match."""
    font: NotRequired["capo_medialive.types.input_location.InputLocation"]
    """External font file used for caption burn-in. File extension must be 'ttf' or 'tte'. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match."""
    font_color: NotRequired["capo_medialive.types.burn_in_font_color.BurnInFontColor"]
    """Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match."""
    font_opacity: NotRequired[
        "capo_medialive.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match."""
    font_resolution: NotRequired[
        "capo_medialive.types.__integer_min96_max600.__integerMin96Max600"
    ]
    """Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match."""
    font_size: NotRequired["capo_medialive.types.__string.__string"]
    """When set to 'auto' fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match."""
    outline_color: NotRequired[
        "capo_medialive.types.burn_in_outline_color.BurnInOutlineColor"
    ]
    """Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match."""
    outline_size: NotRequired[
        "capo_medialive.types.__integer_min0_max10.__integerMin0Max10"
    ]
    """Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match."""
    shadow_color: NotRequired[
        "capo_medialive.types.burn_in_shadow_color.BurnInShadowColor"
    ]
    """Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match."""
    shadow_opacity: NotRequired[
        "capo_medialive.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match."""
    shadow_x_offset: NotRequired["capo_medialive.types.__integer.__integer"]
    """Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match."""
    shadow_y_offset: NotRequired["capo_medialive.types.__integer.__integer"]
    """Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match."""
    teletext_grid_control: NotRequired[
        "capo_medialive.types.burn_in_teletext_grid_control.BurnInTeletextGridControl"
    ]
    """Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs."""
    x_position: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. All burn-in and DVB-Sub font settings must match."""
    y_position: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. All burn-in and DVB-Sub font settings must match."""
    subtitle_rows: NotRequired[
        "capo_medialive.types.burn_in_destination_subtitle_rows.BurnInDestinationSubtitleRows"
    ]
    """Applies only when the input captions are Teletext and the output captions are DVB-Sub or Burn-In. Choose the number of lines for the captions bitmap. The captions bitmap is 700 wide × 576 high and will be laid over the video. For example, a value of 16 divides the bitmap into 16 lines, with each line 36 pixels high (16 × 36 = 576). The default is 24 (24 pixels high). Enter the same number in every encode in every output that converts the same Teletext source to DVB-Sub or Burn-in."""


# --- restJson1 ser/de ---
def serialize_json(value: BurnInDestinationSettings) -> dict:
    out: dict = {}
    if "alignment" in value:
        import capo_medialive.types.burn_in_alignment

        out["alignment"] = capo_medialive.types.burn_in_alignment.serialize_json(
            value["alignment"]
        )
    if "background_color" in value:
        import capo_medialive.types.burn_in_background_color

        out["backgroundColor"] = (
            capo_medialive.types.burn_in_background_color.serialize_json(
                value["background_color"]
            )
        )
    if "background_opacity" in value:
        out["backgroundOpacity"] = value["background_opacity"]
    if "font" in value:
        import capo_medialive.types.input_location

        out["font"] = capo_medialive.types.input_location.serialize_json(value["font"])
    if "font_color" in value:
        import capo_medialive.types.burn_in_font_color

        out["fontColor"] = capo_medialive.types.burn_in_font_color.serialize_json(
            value["font_color"]
        )
    if "font_opacity" in value:
        out["fontOpacity"] = value["font_opacity"]
    if "font_resolution" in value:
        out["fontResolution"] = value["font_resolution"]
    if "font_size" in value:
        out["fontSize"] = value["font_size"]
    if "outline_color" in value:
        import capo_medialive.types.burn_in_outline_color

        out["outlineColor"] = capo_medialive.types.burn_in_outline_color.serialize_json(
            value["outline_color"]
        )
    if "outline_size" in value:
        out["outlineSize"] = value["outline_size"]
    if "shadow_color" in value:
        import capo_medialive.types.burn_in_shadow_color

        out["shadowColor"] = capo_medialive.types.burn_in_shadow_color.serialize_json(
            value["shadow_color"]
        )
    if "shadow_opacity" in value:
        out["shadowOpacity"] = value["shadow_opacity"]
    if "shadow_x_offset" in value:
        out["shadowXOffset"] = value["shadow_x_offset"]
    if "shadow_y_offset" in value:
        out["shadowYOffset"] = value["shadow_y_offset"]
    if "teletext_grid_control" in value:
        import capo_medialive.types.burn_in_teletext_grid_control

        out["teletextGridControl"] = (
            capo_medialive.types.burn_in_teletext_grid_control.serialize_json(
                value["teletext_grid_control"]
            )
        )
    if "x_position" in value:
        out["xPosition"] = value["x_position"]
    if "y_position" in value:
        out["yPosition"] = value["y_position"]
    if "subtitle_rows" in value:
        import capo_medialive.types.burn_in_destination_subtitle_rows

        out["subtitleRows"] = (
            capo_medialive.types.burn_in_destination_subtitle_rows.serialize_json(
                value["subtitle_rows"]
            )
        )
    return out


def deserialize_json(data: dict) -> BurnInDestinationSettings:
    out: BurnInDestinationSettings = {}  # type: ignore[typeddict-item]
    if data.get("alignment") is not None:
        import capo_medialive.types.burn_in_alignment

        out["alignment"] = capo_medialive.types.burn_in_alignment.deserialize_json(
            data["alignment"]
        )
    if data.get("backgroundColor") is not None:
        import capo_medialive.types.burn_in_background_color

        out["background_color"] = (
            capo_medialive.types.burn_in_background_color.deserialize_json(
                data["backgroundColor"]
            )
        )
    if data.get("backgroundOpacity") is not None:
        out["background_opacity"] = data["backgroundOpacity"]
    if data.get("font") is not None:
        import capo_medialive.types.input_location

        out["font"] = capo_medialive.types.input_location.deserialize_json(data["font"])
    if data.get("fontColor") is not None:
        import capo_medialive.types.burn_in_font_color

        out["font_color"] = capo_medialive.types.burn_in_font_color.deserialize_json(
            data["fontColor"]
        )
    if data.get("fontOpacity") is not None:
        out["font_opacity"] = data["fontOpacity"]
    if data.get("fontResolution") is not None:
        out["font_resolution"] = data["fontResolution"]
    if data.get("fontSize") is not None:
        out["font_size"] = data["fontSize"]
    if data.get("outlineColor") is not None:
        import capo_medialive.types.burn_in_outline_color

        out["outline_color"] = (
            capo_medialive.types.burn_in_outline_color.deserialize_json(
                data["outlineColor"]
            )
        )
    if data.get("outlineSize") is not None:
        out["outline_size"] = data["outlineSize"]
    if data.get("shadowColor") is not None:
        import capo_medialive.types.burn_in_shadow_color

        out["shadow_color"] = (
            capo_medialive.types.burn_in_shadow_color.deserialize_json(
                data["shadowColor"]
            )
        )
    if data.get("shadowOpacity") is not None:
        out["shadow_opacity"] = data["shadowOpacity"]
    if data.get("shadowXOffset") is not None:
        out["shadow_x_offset"] = data["shadowXOffset"]
    if data.get("shadowYOffset") is not None:
        out["shadow_y_offset"] = data["shadowYOffset"]
    if data.get("teletextGridControl") is not None:
        import capo_medialive.types.burn_in_teletext_grid_control

        out["teletext_grid_control"] = (
            capo_medialive.types.burn_in_teletext_grid_control.deserialize_json(
                data["teletextGridControl"]
            )
        )
    if data.get("xPosition") is not None:
        out["x_position"] = data["xPosition"]
    if data.get("yPosition") is not None:
        out["y_position"] = data["yPosition"]
    if data.get("subtitleRows") is not None:
        import capo_medialive.types.burn_in_destination_subtitle_rows

        out["subtitle_rows"] = (
            capo_medialive.types.burn_in_destination_subtitle_rows.deserialize_json(
                data["subtitleRows"]
            )
        )
    return out
