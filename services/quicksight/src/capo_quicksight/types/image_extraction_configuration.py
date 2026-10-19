"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageExtractionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.image_extraction_status


class ImageExtractionConfiguration(TypedDict, closed=True):
    image_extraction_status: (
        "capo_quicksight.types.image_extraction_status.ImageExtractionStatus"
    )
    """<p>The status of image extraction. Valid values are ENABLED and DISABLED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageExtractionConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.image_extraction_status

    out["imageExtractionStatus"] = (
        capo_quicksight.types.image_extraction_status.serialize_json(
            value["image_extraction_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> ImageExtractionConfiguration:
    out: ImageExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("imageExtractionStatus") is not None:
        import capo_quicksight.types.image_extraction_status

        out["image_extraction_status"] = (
            capo_quicksight.types.image_extraction_status.deserialize_json(
                data["imageExtractionStatus"]
            )
        )
    else:
        import typing

        out["image_extraction_status"] = typing.cast(
            "capo_quicksight.types.image_extraction_status.ImageExtractionStatus", ""
        )
    return out
