"""Generated from Smithy shape ``com.amazonaws.detective#BatchGetGraphMemberDatasourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.account_id_extended_list
    import capo_detective.types.graph_arn


class BatchGetGraphMemberDatasourcesRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph.</p>"""
    account_ids: "capo_detective.types.account_id_extended_list.AccountIdExtendedList"
    """<p>The list of Amazon Web Services accounts to get data source package information on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetGraphMemberDatasourcesRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    import capo_detective.types.account_id_extended_list

    out["AccountIds"] = capo_detective.types.account_id_extended_list.serialize_json(
        value["account_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetGraphMemberDatasourcesRequest:
    out: BatchGetGraphMemberDatasourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("GraphArn") is not None:
        out["graph_arn"] = data["GraphArn"]
    else:
        out["graph_arn"] = ""
    if data.get("AccountIds") is not None:
        import capo_detective.types.account_id_extended_list

        out["account_ids"] = (
            capo_detective.types.account_id_extended_list.deserialize_json(
                data["AccountIds"]
            )
        )
    else:
        out["account_ids"] = []
    return out
