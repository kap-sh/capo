"""Generated from Smithy shape ``com.amazonaws.efs#DescribeTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_efs.types.marker
    import capo_efs.types.tags


class DescribeTagsResponse(TypedDict, closed=True):
    marker: NotRequired["capo_efs.types.marker.Marker"]
    """<p>If the request included a <code>Marker</code>, the response returns that value in this field.</p>"""
    tags: "capo_efs.types.tags.Tags"
    """<p>Returns tags associated with the file system as an array of <code>Tag</code> objects. </p>"""
    next_marker: NotRequired["capo_efs.types.marker.Marker"]
    """<p>If a value is present, there are more tags to return. In a subsequent request, you can provide the value of <code>NextMarker</code> as the value of the <code>Marker</code> parameter in your next request to retrieve the next set of tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTagsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    import capo_efs.types.tags

    out["Tags"] = capo_efs.types.tags.serialize_json(value["tags"])
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> DescribeTagsResponse:
    out: DescribeTagsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("Tags") is not None:
        import capo_efs.types.tags

        out["tags"] = capo_efs.types.tags.deserialize_json(data["Tags"])
    else:
        out["tags"] = []
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
