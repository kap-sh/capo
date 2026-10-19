"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageStaticFile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.static_file_source


class ImageStaticFile(TypedDict, closed=True):
    static_file_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the static file that contains an image.</p>"""
    source: NotRequired["capo_quicksight.types.static_file_source.StaticFileSource"]
    """<p>The source of the image static file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageStaticFile) -> dict:
    out: dict = {}
    out["StaticFileId"] = value["static_file_id"]
    if "source" in value:
        import capo_quicksight.types.static_file_source

        out["Source"] = capo_quicksight.types.static_file_source.serialize_json(
            value["source"]
        )
    return out


def deserialize_json(data: dict) -> ImageStaticFile:
    out: ImageStaticFile = {}  # type: ignore[typeddict-item]
    if data.get("StaticFileId") is not None:
        out["static_file_id"] = data["StaticFileId"]
    else:
        out["static_file_id"] = ""
    if data.get("Source") is not None:
        import capo_quicksight.types.static_file_source

        out["source"] = capo_quicksight.types.static_file_source.deserialize_json(
            data["Source"]
        )
    return out
