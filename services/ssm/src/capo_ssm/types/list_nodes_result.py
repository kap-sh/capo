"""Generated from Smithy shape ``com.amazonaws.ssm#ListNodesResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.node_list


class ListNodesResult(TypedDict, closed=True):
    nodes: NotRequired["capo_ssm.types.node_list.NodeList"]
    """<p>A list of managed nodes that match the specified filter criteria.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNodesResult) -> dict:
    out: dict = {}
    if "nodes" in value:
        import capo_ssm.types.node_list

        out["Nodes"] = capo_ssm.types.node_list.serialize_aws_json_1_1(value["nodes"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNodesResult:
    out: ListNodesResult = {}  # type: ignore[typeddict-item]
    if data.get("Nodes") is not None:
        import capo_ssm.types.node_list

        out["nodes"] = capo_ssm.types.node_list.deserialize_aws_json_1_1(data["Nodes"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListNodesResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "nodes" in value:
        import capo_ssm.types.node_list

        out["nodes"] = capo_ssm.types.node_list.redact_sensitive(value["nodes"])
    return out
