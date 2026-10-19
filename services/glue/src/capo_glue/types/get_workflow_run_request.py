"""Generated from Smithy shape ``com.amazonaws.glue#GetWorkflowRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.id_string
    import capo_glue.types.name_string
    import capo_glue.types.nullable_boolean


class GetWorkflowRunRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>Name of the workflow being run.</p>"""
    run_id: "capo_glue.types.id_string.IdString"
    """<p>The ID of the workflow run.</p>"""
    include_graph: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether to include the workflow graph in response or not.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkflowRunRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RunId"] = value["run_id"]
    if "include_graph" in value:
        out["IncludeGraph"] = value["include_graph"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkflowRunRequest:
    out: GetWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        out["run_id"] = ""
    if data.get("IncludeGraph") is not None:
        out["include_graph"] = data["IncludeGraph"]
    return out
