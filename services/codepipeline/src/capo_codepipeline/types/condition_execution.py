"""Generated from Smithy shape ``com.amazonaws.codepipeline#ConditionExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.condition_execution_status
    import capo_codepipeline.types.execution_summary
    import capo_codepipeline.types.timestamp


class ConditionExecution(TypedDict, closed=True):
    status: NotRequired[
        "capo_codepipeline.types.condition_execution_status.ConditionExecutionStatus"
    ]
    """<p>The status of the run for a condition.</p>"""
    summary: NotRequired["capo_codepipeline.types.execution_summary.ExecutionSummary"]
    """<p>The summary of information about a run for a condition.</p>"""
    last_status_change: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The last status change of the condition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionExecution) -> dict:
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
    if "last_status_change" in value:
        import capo_codepipeline.types.timestamp

        out["lastStatusChange"] = (
            capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
                value["last_status_change"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConditionExecution:
    out: ConditionExecution = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_codepipeline.types.condition_execution_status

        out["status"] = (
            capo_codepipeline.types.condition_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("lastStatusChange") is not None:
        import capo_codepipeline.types.timestamp

        out["last_status_change"] = (
            capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
                data["lastStatusChange"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConditionExecution) -> dict:
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
    if "last_status_change" in value:
        import capo_codepipeline.types.timestamp

        out["lastStatusChange"] = capo_codepipeline.types.timestamp.serialize_cbor(
            value["last_status_change"]
        )
    return out


def deserialize_cbor(data: dict) -> ConditionExecution:
    out: ConditionExecution = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_codepipeline.types.condition_execution_status

        out["status"] = (
            capo_codepipeline.types.condition_execution_status.deserialize_cbor(
                data["status"]
            )
        )
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("lastStatusChange") is not None:
        import capo_codepipeline.types.timestamp

        out["last_status_change"] = capo_codepipeline.types.timestamp.deserialize_cbor(
            data["lastStatusChange"]
        )
    return out
