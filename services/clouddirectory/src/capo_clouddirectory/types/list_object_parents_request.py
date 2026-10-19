"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListObjectParentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.bool
    import capo_clouddirectory.types.consistency_level
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.number_results
    import capo_clouddirectory.types.object_reference


class ListObjectParentsRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.</p>"""
    object_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>The reference that identifies the object for which parent objects are being listed.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired["capo_clouddirectory.types.number_results.NumberResults"]
    """<p>The maximum number of items to be retrieved in a single call. This is an approximate number.</p>"""
    consistency_level: NotRequired[
        "capo_clouddirectory.types.consistency_level.ConsistencyLevel"
    ]
    """<p>Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.</p>"""
    include_all_links_to_each_parent: NotRequired["capo_clouddirectory.types.bool.Bool"]
    """<p>When set to True, returns all <a>ListObjectParentsResponse$ParentLinks</a>. There could be multiple links between a parent-child pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectParentsRequest) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.object_reference

    out["ObjectReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["object_reference"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "include_all_links_to_each_parent" in value:
        out["IncludeAllLinksToEachParent"] = value["include_all_links_to_each_parent"]
    return out


def deserialize_json(data: dict) -> ListObjectParentsRequest:
    out: ListObjectParentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ObjectReference") is not None:
        import capo_clouddirectory.types.object_reference

        out["object_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError("ListObjectParentsRequest.object_reference required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("IncludeAllLinksToEachParent") is not None:
        out["include_all_links_to_each_parent"] = data["IncludeAllLinksToEachParent"]
    return out
