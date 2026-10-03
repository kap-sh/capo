"""Generated from Smithy shape ``com.amazonaws.organizations#ListChildrenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.child_type
    import capo_organizations.types.max_results
    import capo_organizations.types.next_token
    import capo_organizations.types.parent_id


class ListChildrenRequest(TypedDict, closed=True):
    parent_id: "capo_organizations.types.parent_id.ParentId"
    """<p>The unique identifier (ID) for the parent root or OU whose children you want to list.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for a parent ID string requires one of the following:</p> <ul> <li> <p> <b>Root</b> - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits.</p> </li> <li> <p> <b>Organizational unit (OU)</b> - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.</p> </li> </ul>"""
    child_type: "capo_organizations.types.child_type.ChildType"
    """<p>Filters the output to include only the specified child type.</p>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>"""
    max_results: NotRequired["capo_organizations.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListChildrenRequest) -> dict:
    out: dict = {}
    out["ParentId"] = value["parent_id"]
    import capo_organizations.types.child_type

    out["ChildType"] = capo_organizations.types.child_type.serialize_aws_json_1_1(
        value["child_type"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListChildrenRequest:
    out: ListChildrenRequest = {}  # type: ignore[typeddict-item]
    if data.get("ParentId") is not None:
        out["parent_id"] = data["ParentId"]
    else:
        raise DeserializationError("ListChildrenRequest.parent_id required")
    if data.get("ChildType") is not None:
        import capo_organizations.types.child_type

        out["child_type"] = (
            capo_organizations.types.child_type.deserialize_aws_json_1_1(
                data["ChildType"]
            )
        )
    else:
        raise DeserializationError("ListChildrenRequest.child_type required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
