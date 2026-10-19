"""Generated from Smithy shape ``com.amazonaws.directoryservice#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.limit
    import capo_directory_service.types.next_token
    import capo_directory_service.types.resource_id


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_id: "capo_directory_service.types.resource_id.ResourceId"
    """<p>Identifier (ID) of the directory for which you want to retrieve tags.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>Reserved for future use.</p>"""
    limit: NotRequired["capo_directory_service.types.limit.Limit"]
    """<p>Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
