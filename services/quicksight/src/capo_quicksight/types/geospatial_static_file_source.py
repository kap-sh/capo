"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialStaticFileSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.short_restrictive_resource_id


class GeospatialStaticFileSource(TypedDict, closed=True):
    static_file_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the static file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialStaticFileSource) -> dict:
    out: dict = {}
    out["StaticFileId"] = value["static_file_id"]
    return out


def deserialize_json(data: dict) -> GeospatialStaticFileSource:
    out: GeospatialStaticFileSource = {}  # type: ignore[typeddict-item]
    if data.get("StaticFileId") is not None:
        out["static_file_id"] = data["StaticFileId"]
    else:
        out["static_file_id"] = ""
    return out
