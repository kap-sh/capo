"""Generated from Smithy shape ``com.amazonaws.glue#CodeGenEdge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.code_gen_arg_name
    import capo_glue.types.code_gen_identifier


class CodeGenEdge(TypedDict, closed=True):
    source: "capo_glue.types.code_gen_identifier.CodeGenIdentifier"
    """<p>The ID of the node at which the edge starts.</p>"""
    target: "capo_glue.types.code_gen_identifier.CodeGenIdentifier"
    """<p>The ID of the node at which the edge ends.</p>"""
    target_parameter: NotRequired["capo_glue.types.code_gen_arg_name.CodeGenArgName"]
    """<p>The target of the edge.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeGenEdge) -> dict:
    out: dict = {}
    out["Source"] = value["source"]
    out["Target"] = value["target"]
    if "target_parameter" in value:
        out["TargetParameter"] = value["target_parameter"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeGenEdge:
    out: CodeGenEdge = {}  # type: ignore[typeddict-item]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    else:
        out["source"] = ""
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    else:
        out["target"] = ""
    if data.get("TargetParameter") is not None:
        out["target_parameter"] = data["TargetParameter"]
    return out
