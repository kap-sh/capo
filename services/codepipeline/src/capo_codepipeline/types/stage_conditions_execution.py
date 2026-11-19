"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageConditionsExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.condition_execution_status
    import capo_codepipeline.types.execution_summary


class StageConditionsExecution(TypedDict, closed=True):
    status: NotRequired[
        "capo_codepipeline.types.condition_execution_status.ConditionExecutionStatus"
    ]
    """<p>The status of a run of a condition for a stage.</p>"""
    summary: NotRequired["capo_codepipeline.types.execution_summary.ExecutionSummary"]
    """<p>A summary of the run of the condition for a stage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageConditionsExecution) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_codepipeline.types.condition_execution_status

        out["status"] = (
            capo_codepipeline.types.condition_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "summary" in value:
        out["summary"] = value["summary"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StageConditionsExecution:
    out: StageConditionsExecution = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_codepipeline.types.condition_execution_status

        out["status"] = (
            capo_codepipeline.types.condition_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StageConditionsExecution) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_codepipeline.types.condition_execution_status

        out["status"] = (
            capo_codepipeline.types.condition_execution_status.serialize_cbor(
                value["status"]
            )
        )
    if "summary" in value:
        out["summary"] = value["summary"]
    return out


def deserialize_cbor(data: dict) -> StageConditionsExecution:
    out: StageConditionsExecution = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_codepipeline.types.condition_execution_status

        out["status"] = (
            capo_codepipeline.types.condition_execution_status.deserialize_cbor(
                data["status"]
            )
        )
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    return out
