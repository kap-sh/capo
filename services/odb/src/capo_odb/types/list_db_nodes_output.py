"""Generated from Smithy shape ``com.amazonaws.odb#ListDbNodesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.db_node_list


class ListDbNodesOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    db_nodes: "capo_odb.types.db_node_list.DbNodeList"
    """<p>The list of DB nodes along with their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDbNodesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.db_node_list

    out["dbNodes"] = capo_odb.types.db_node_list.serialize_aws_json_1_0(
        value["db_nodes"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDbNodesOutput:
    out: ListDbNodesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("dbNodes") is not None:
        import capo_odb.types.db_node_list

        out["db_nodes"] = capo_odb.types.db_node_list.deserialize_aws_json_1_0(
            data["dbNodes"]
        )
    else:
        out["db_nodes"] = []
    return out
