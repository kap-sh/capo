"""Generated from Smithy shape ``com.amazonaws.glue#GetBlueprintRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.id_string
    import capo_glue.types.orchestration_name_string


class GetBlueprintRunRequest(TypedDict, closed=True):
    blueprint_name: "capo_glue.types.orchestration_name_string.OrchestrationNameString"
    """<p>The name of the blueprint.</p>"""
    run_id: "capo_glue.types.id_string.IdString"
    """<p>The run ID for the blueprint run you want to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlueprintRunRequest) -> dict:
    out: dict = {}
    out["BlueprintName"] = value["blueprint_name"]
    out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlueprintRunRequest:
    out: GetBlueprintRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("BlueprintName") is not None:
        out["blueprint_name"] = data["BlueprintName"]
    else:
        out["blueprint_name"] = ""
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        out["run_id"] = ""
    return out
