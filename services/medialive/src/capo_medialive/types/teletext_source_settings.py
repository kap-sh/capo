"""Generated from Smithy shape ``com.amazonaws.medialive#TeletextSourceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.caption_rectangle


class TeletextSourceSettings(TypedDict, closed=True):
    output_rectangle: NotRequired[
        "capo_medialive.types.caption_rectangle.CaptionRectangle"
    ]
    """Optionally defines a region where TTML style captions will be displayed"""
    page_number: NotRequired["capo_medialive.types.__string.__string"]
    """Specifies the teletext page number within the data stream from which to extract captions. Range of 0x100 (256) to 0x8FF (2303). Unused for passthrough. Should be specified as a hexadecimal string with no "0x" prefix."""


# --- restJson1 ser/de ---
def serialize_json(value: TeletextSourceSettings) -> dict:
    out: dict = {}
    if "output_rectangle" in value:
        import capo_medialive.types.caption_rectangle

        out["outputRectangle"] = capo_medialive.types.caption_rectangle.serialize_json(
            value["output_rectangle"]
        )
    if "page_number" in value:
        out["pageNumber"] = value["page_number"]
    return out


def deserialize_json(data: dict) -> TeletextSourceSettings:
    out: TeletextSourceSettings = {}  # type: ignore[typeddict-item]
    if data.get("outputRectangle") is not None:
        import capo_medialive.types.caption_rectangle

        out["output_rectangle"] = (
            capo_medialive.types.caption_rectangle.deserialize_json(
                data["outputRectangle"]
            )
        )
    if data.get("pageNumber") is not None:
        out["page_number"] = data["pageNumber"]
    return out
