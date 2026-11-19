"""Generated from Smithy shape ``com.amazonaws.codepipeline#ExecutionTrigger``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.trigger_detail
    import capo_codepipeline.types.trigger_type


class ExecutionTrigger(TypedDict, closed=True):
    trigger_type: NotRequired["capo_codepipeline.types.trigger_type.TriggerType"]
    """<p>The type of change-detection method, command, or user interaction that started a pipeline execution.</p>"""
    trigger_detail: NotRequired["capo_codepipeline.types.trigger_detail.TriggerDetail"]
    """<p>Detail related to the event that started a pipeline execution, such as the webhook ARN of the webhook that triggered the pipeline execution or the user ARN for a user-initiated <code>start-pipeline-execution</code> CLI command.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionTrigger) -> dict:
    out: dict = {}
    if "trigger_type" in value:
        import capo_codepipeline.types.trigger_type

        out["triggerType"] = (
            capo_codepipeline.types.trigger_type.serialize_aws_json_1_1(
                value["trigger_type"]
            )
        )
    if "trigger_detail" in value:
        out["triggerDetail"] = value["trigger_detail"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionTrigger:
    out: ExecutionTrigger = {}  # type: ignore[typeddict-item]
    if data.get("triggerType") is not None:
        import capo_codepipeline.types.trigger_type

        out["trigger_type"] = (
            capo_codepipeline.types.trigger_type.deserialize_aws_json_1_1(
                data["triggerType"]
            )
        )
    if data.get("triggerDetail") is not None:
        out["trigger_detail"] = data["triggerDetail"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExecutionTrigger) -> dict:
    out: dict = {}
    if "trigger_type" in value:
        import capo_codepipeline.types.trigger_type

        out["triggerType"] = capo_codepipeline.types.trigger_type.serialize_cbor(
            value["trigger_type"]
        )
    if "trigger_detail" in value:
        out["triggerDetail"] = value["trigger_detail"]
    return out


def deserialize_cbor(data: dict) -> ExecutionTrigger:
    out: ExecutionTrigger = {}  # type: ignore[typeddict-item]
    if data.get("triggerType") is not None:
        import capo_codepipeline.types.trigger_type

        out["trigger_type"] = capo_codepipeline.types.trigger_type.deserialize_cbor(
            data["triggerType"]
        )
    if data.get("triggerDetail") is not None:
        out["trigger_detail"] = data["triggerDetail"]
    return out
