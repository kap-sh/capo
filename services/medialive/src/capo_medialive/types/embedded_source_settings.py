"""Generated from Smithy shape ``com.amazonaws.medialive#EmbeddedSourceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1_max4
    import capo_medialive.types.__integer_min1_max5
    import capo_medialive.types.embedded_convert608_to708
    import capo_medialive.types.embedded_scte20_detection


class EmbeddedSourceSettings(TypedDict, closed=True):
    convert608_to708: NotRequired[
        "capo_medialive.types.embedded_convert608_to708.EmbeddedConvert608To708"
    ]
    """If upconvert, 608 data is both passed through via the "608 compatibility bytes" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded."""
    scte20_detection: NotRequired[
        "capo_medialive.types.embedded_scte20_detection.EmbeddedScte20Detection"
    ]
    """Set to "auto" to handle streams with intermittent and/or non-aligned SCTE-20 and Embedded captions."""
    source608_channel_number: NotRequired[
        "capo_medialive.types.__integer_min1_max4.__integerMin1Max4"
    ]
    """Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough."""
    source608_track_number: NotRequired[
        "capo_medialive.types.__integer_min1_max5.__integerMin1Max5"
    ]
    """This field is unused and deprecated."""


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddedSourceSettings) -> dict:
    out: dict = {}
    if "convert608_to708" in value:
        import capo_medialive.types.embedded_convert608_to708

        out["convert608To708"] = (
            capo_medialive.types.embedded_convert608_to708.serialize_json(
                value["convert608_to708"]
            )
        )
    if "scte20_detection" in value:
        import capo_medialive.types.embedded_scte20_detection

        out["scte20Detection"] = (
            capo_medialive.types.embedded_scte20_detection.serialize_json(
                value["scte20_detection"]
            )
        )
    if "source608_channel_number" in value:
        out["source608ChannelNumber"] = value["source608_channel_number"]
    if "source608_track_number" in value:
        out["source608TrackNumber"] = value["source608_track_number"]
    return out


def deserialize_json(data: dict) -> EmbeddedSourceSettings:
    out: EmbeddedSourceSettings = {}  # type: ignore[typeddict-item]
    if data.get("convert608To708") is not None:
        import capo_medialive.types.embedded_convert608_to708

        out["convert608_to708"] = (
            capo_medialive.types.embedded_convert608_to708.deserialize_json(
                data["convert608To708"]
            )
        )
    if data.get("scte20Detection") is not None:
        import capo_medialive.types.embedded_scte20_detection

        out["scte20_detection"] = (
            capo_medialive.types.embedded_scte20_detection.deserialize_json(
                data["scte20Detection"]
            )
        )
    if data.get("source608ChannelNumber") is not None:
        out["source608_channel_number"] = data["source608ChannelNumber"]
    if data.get("source608TrackNumber") is not None:
        out["source608_track_number"] = data["source608TrackNumber"]
    return out
