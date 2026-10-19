"""Generated from Smithy shape ``com.amazonaws.detective#GetMembersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.account_id_list
    import capo_detective.types.graph_arn


class GetMembersRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph for which to request the member details.</p>"""
    account_ids: "capo_detective.types.account_id_list.AccountIdList"
    """<p>The list of Amazon Web Services account identifiers for the member account for which to return member details. You can request details for up to 50 member accounts at a time.</p> <p>You cannot use <code>GetMembers</code> to retrieve information about member accounts that were removed from the behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMembersRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    import capo_detective.types.account_id_list

    out["AccountIds"] = capo_detective.types.account_id_list.serialize_json(
        value["account_ids"]
    )
    return out


def deserialize_json(data: dict) -> GetMembersRequest:
    out: GetMembersRequest = {}  # type: ignore[typeddict-item]
    if data.get("GraphArn") is not None:
        out["graph_arn"] = data["GraphArn"]
    else:
        out["graph_arn"] = ""
    if data.get("AccountIds") is not None:
        import capo_detective.types.account_id_list

        out["account_ids"] = capo_detective.types.account_id_list.deserialize_json(
            data["AccountIds"]
        )
    else:
        out["account_ids"] = []
    return out
