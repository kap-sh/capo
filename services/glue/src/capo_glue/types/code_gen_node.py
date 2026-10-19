"""Generated from Smithy shape ``com.amazonaws.glue#CodeGenNode``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.code_gen_identifier
    import capo_glue.types.code_gen_node_args
    import capo_glue.types.code_gen_node_type
    import capo_glue.types.integer


class CodeGenNode(TypedDict, closed=True):
    id: "capo_glue.types.code_gen_identifier.CodeGenIdentifier"
    """<p>A node identifier that is unique within the node's graph.</p>"""
    node_type: "capo_glue.types.code_gen_node_type.CodeGenNodeType"
    """<p>The type of node that this is.</p>"""
    args: "capo_glue.types.code_gen_node_args.CodeGenNodeArgs"
    """<p>Properties of the node, in the form of name-value pairs.</p>"""
    line_number: "capo_glue.types.integer.Integer"
    """<p>The line number of the node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeGenNode) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["NodeType"] = value["node_type"]
    import capo_glue.types.code_gen_node_args

    out["Args"] = capo_glue.types.code_gen_node_args.serialize_aws_json_1_1(
        value["args"]
    )
    out["LineNumber"] = value.get("line_number", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeGenNode:
    out: CodeGenNode = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("NodeType") is not None:
        out["node_type"] = data["NodeType"]
    else:
        out["node_type"] = ""
    if data.get("Args") is not None:
        import capo_glue.types.code_gen_node_args

        out["args"] = capo_glue.types.code_gen_node_args.deserialize_aws_json_1_1(
            data["Args"]
        )
    else:
        out["args"] = []
    if data.get("LineNumber") is not None:
        out["line_number"] = data["LineNumber"]
    else:
        out["line_number"] = 0
    return out
