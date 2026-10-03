"""Generated from Smithy shape ``com.amazonaws.medialive#Scte20SourceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1_max4
    import capo_medialive.types.scte20_convert608_to708


class Scte20SourceSettings(TypedDict, closed=True):
    convert608_to708: NotRequired[
        "capo_medialive.types.scte20_convert608_to708.Scte20Convert608To708"
    ]
    """If upconvert, 608 data is both passed through via the "608 compatibility bytes" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded."""
    source608_channel_number: NotRequired[
        "capo_medialive.types.__integer_min1_max4.__integerMin1Max4"
    ]
    """Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough."""


# --- restJson1 ser/de ---
def serialize_json(value: Scte20SourceSettings) -> dict:
    out: dict = {}
    if "convert608_to708" in value:
        import capo_medialive.types.scte20_convert608_to708

        out["convert608To708"] = (
            capo_medialive.types.scte20_convert608_to708.serialize_json(
                value["convert608_to708"]
            )
        )
    if "source608_channel_number" in value:
        out["source608ChannelNumber"] = value["source608_channel_number"]
    return out


def deserialize_json(data: dict) -> Scte20SourceSettings:
    out: Scte20SourceSettings = {}  # type: ignore[typeddict-item]
    if data.get("convert608To708") is not None:
        import capo_medialive.types.scte20_convert608_to708

        out["convert608_to708"] = (
            capo_medialive.types.scte20_convert608_to708.deserialize_json(
                data["convert608To708"]
            )
        )
    if data.get("source608ChannelNumber") is not None:
        out["source608_channel_number"] = data["source608ChannelNumber"]
    return out
