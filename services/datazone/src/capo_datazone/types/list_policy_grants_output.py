"""Generated from Smithy shape ``com.amazonaws.datazone#ListPolicyGrantsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.pagination_token
    import capo_datazone.types.policy_grant_list


class ListPolicyGrantsOutput(TypedDict, closed=True):
    grant_list: "capo_datazone.types.policy_grant_list.PolicyGrantList"
    """<p>The results of this action - the listed grants.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of grants is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of grants, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListPolicyGrants</code> to list the next set of grants.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyGrantsOutput) -> dict:
    out: dict = {}
    import capo_datazone.types.policy_grant_list

    out["grantList"] = capo_datazone.types.policy_grant_list.serialize_json(
        value["grant_list"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPolicyGrantsOutput:
    out: ListPolicyGrantsOutput = {}  # type: ignore[typeddict-item]
    if data.get("grantList") is not None:
        import capo_datazone.types.policy_grant_list

        out["grant_list"] = capo_datazone.types.policy_grant_list.deserialize_json(
            data["grantList"]
        )
    else:
        out["grant_list"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
