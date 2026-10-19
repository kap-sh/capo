"""Generated from Smithy shape ``com.amazonaws.glue#CodeGenNodeArg``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boolean
    import capo_glue.types.code_gen_arg_name
    import capo_glue.types.code_gen_arg_value


class CodeGenNodeArg(TypedDict, closed=True):
    name: "capo_glue.types.code_gen_arg_name.CodeGenArgName"
    """<p>The name of the argument or property.</p>"""
    value: "capo_glue.types.code_gen_arg_value.CodeGenArgValue"
    """<p>The value of the argument or property.</p>"""
    param: "capo_glue.types.boolean.Boolean"
    """<p>True if the value is used as a parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeGenNodeArg) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    out["Param"] = value.get("param", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeGenNodeArg:
    out: CodeGenNodeArg = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    if data.get("Param") is not None:
        out["param"] = data["Param"]
    else:
        out["param"] = False
    return out
