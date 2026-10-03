"""Generated from Smithy shape ``com.amazonaws.medialive#EmbeddedDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.embedded_caption_position_settings
    import capo_medialive.types.embedded_destination_style_control


class EmbeddedDestinationSettings(TypedDict, closed=True):
    position: NotRequired[
        "capo_medialive.types.embedded_caption_position_settings.EmbeddedCaptionPositionSettings"
    ]
    """Specifies the position of the output captions. Applies only when styleControl is set to manual."""
    style_control: NotRequired[
        "capo_medialive.types.embedded_destination_style_control.EmbeddedDestinationStyleControl"
    ]
    """Controls the source of position and style information for the output captions. - "passthrough": Carry the caption position and style from the source captions. When the source captions are embedded, SCTE-20, or ancillary, the position and style are preserved exactly. When the source captions are another format, the position and any supported style are carried over. - "manual": Applies the specified styling and positioning. All other styling and positioning is given default values."""


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddedDestinationSettings) -> dict:
    out: dict = {}
    if "position" in value:
        import capo_medialive.types.embedded_caption_position_settings

        out["position"] = (
            capo_medialive.types.embedded_caption_position_settings.serialize_json(
                value["position"]
            )
        )
    if "style_control" in value:
        import capo_medialive.types.embedded_destination_style_control

        out["styleControl"] = (
            capo_medialive.types.embedded_destination_style_control.serialize_json(
                value["style_control"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmbeddedDestinationSettings:
    out: EmbeddedDestinationSettings = {}  # type: ignore[typeddict-item]
    if data.get("position") is not None:
        import capo_medialive.types.embedded_caption_position_settings

        out["position"] = (
            capo_medialive.types.embedded_caption_position_settings.deserialize_json(
                data["position"]
            )
        )
    if data.get("styleControl") is not None:
        import capo_medialive.types.embedded_destination_style_control

        out["style_control"] = (
            capo_medialive.types.embedded_destination_style_control.deserialize_json(
                data["styleControl"]
            )
        )
    return out
