"""Generated from Smithy shape ``com.amazonaws.detective#DeleteMembersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.account_id_list
    import capo_detective.types.graph_arn


class DeleteMembersRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph to remove members from.</p>"""
    account_ids: "capo_detective.types.account_id_list.AccountIdList"
    """<p>The list of Amazon Web Services account identifiers for the member accounts to remove from the behavior graph. You can remove up to 50 member accounts at a time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMembersRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    import capo_detective.types.account_id_list

    out["AccountIds"] = capo_detective.types.account_id_list.serialize_json(
        value["account_ids"]
    )
    return out


def deserialize_json(data: dict) -> DeleteMembersRequest:
    out: DeleteMembersRequest = {}  # type: ignore[typeddict-item]
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
