"""Generated from Smithy shape ``com.amazonaws.codepipeline#ExecutionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.execution_id
    import capo_codepipeline.types.execution_summary
    import capo_codepipeline.types.percentage


class ExecutionDetails(TypedDict, closed=True):
    summary: NotRequired["capo_codepipeline.types.execution_summary.ExecutionSummary"]
    """<p>The summary of the current status of the actions.</p>"""
    external_execution_id: NotRequired[
        "capo_codepipeline.types.execution_id.ExecutionId"
    ]
    """<p>The system-generated unique ID of this action used to identify this job worker in any external systems, such as CodeDeploy.</p>"""
    percent_complete: NotRequired["capo_codepipeline.types.percentage.Percentage"]
    """<p>The percentage of work completed on the action, represented on a scale of 0 to 100 percent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionDetails) -> dict:
    out: dict = {}
    if "summary" in value:
        out["summary"] = value["summary"]
    if "external_execution_id" in value:
        out["externalExecutionId"] = value["external_execution_id"]
    if "percent_complete" in value:
        out["percentComplete"] = value["percent_complete"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionDetails:
    out: ExecutionDetails = {}  # type: ignore[typeddict-item]
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("externalExecutionId") is not None:
        out["external_execution_id"] = data["externalExecutionId"]
    if data.get("percentComplete") is not None:
        out["percent_complete"] = data["percentComplete"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExecutionDetails) -> dict:
    out: dict = {}
    if "summary" in value:
        out["summary"] = value["summary"]
    if "external_execution_id" in value:
        out["externalExecutionId"] = value["external_execution_id"]
    if "percent_complete" in value:
        out["percentComplete"] = value["percent_complete"]
    return out


def deserialize_cbor(data: dict) -> ExecutionDetails:
    out: ExecutionDetails = {}  # type: ignore[typeddict-item]
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("externalExecutionId") is not None:
        out["external_execution_id"] = data["externalExecutionId"]
    if data.get("percentComplete") is not None:
        out["percent_complete"] = data["percentComplete"]
    return out
