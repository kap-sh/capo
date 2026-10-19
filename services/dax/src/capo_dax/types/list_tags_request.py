"""Generated from Smithy shape ``com.amazonaws.dax#ListTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.string


class ListTagsRequest(TypedDict, closed=True):
    resource_name: "capo_dax.types.string.String"
    """<p>The name of the DAX resource to which the tags belong.</p>"""
    next_token: NotRequired["capo_dax.types.string.String"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsRequest) -> dict:
    out: dict = {}
    out["ResourceName"] = value["resource_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsRequest:
    out: ListTagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    else:
        out["resource_name"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
