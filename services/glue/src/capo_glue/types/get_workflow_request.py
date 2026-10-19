"""Generated from Smithy shape ``com.amazonaws.glue#GetWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string
    import capo_glue.types.nullable_boolean


class GetWorkflowRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the workflow to retrieve.</p>"""
    include_graph: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether to include a graph when returning the workflow resource metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkflowRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "include_graph" in value:
        out["IncludeGraph"] = value["include_graph"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkflowRequest:
    out: GetWorkflowRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("IncludeGraph") is not None:
        out["include_graph"] = data["IncludeGraph"]
    return out
