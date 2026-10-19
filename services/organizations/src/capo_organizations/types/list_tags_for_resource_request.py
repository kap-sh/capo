"""Generated from Smithy shape ``com.amazonaws.organizations#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.next_token
    import capo_organizations.types.taggable_resource_id


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_id: "capo_organizations.types.taggable_resource_id.TaggableResourceId"
    """<p>The ID of the resource with the tags to list.</p> <p>You can specify any of the following taggable resources.</p> <ul> <li> <p>Amazon Web Services account – specify the account ID number.</p> </li> <li> <p>Organizational unit – specify the OU ID that begins with <code>ou-</code> and looks similar to: <code>ou-<i>1a2b-34uvwxyz</i> </code> </p> </li> <li> <p>Root – specify the root ID that begins with <code>r-</code> and looks similar to: <code>r-<i>1a2b</i> </code> </p> </li> <li> <p>Policy – specify the policy ID that begins with <code>p-</code> andlooks similar to: <code>p-<i>12abcdefg3</i> </code> </p> </li> </ul>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
