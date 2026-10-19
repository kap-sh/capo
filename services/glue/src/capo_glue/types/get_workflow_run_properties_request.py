"""Generated from Smithy shape ``com.amazonaws.glue#GetWorkflowRunPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.id_string
    import capo_glue.types.name_string


class GetWorkflowRunPropertiesRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>Name of the workflow which was run.</p>"""
    run_id: "capo_glue.types.id_string.IdString"
    """<p>The ID of the workflow run whose run properties should be returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkflowRunPropertiesRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkflowRunPropertiesRequest:
    out: GetWorkflowRunPropertiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        out["run_id"] = ""
    return out
