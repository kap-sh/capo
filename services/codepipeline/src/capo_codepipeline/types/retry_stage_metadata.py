"""Generated from Smithy shape ``com.amazonaws.codepipeline#RetryStageMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.retry_attempt
    import capo_codepipeline.types.retry_trigger


class RetryStageMetadata(TypedDict, closed=True):
    auto_stage_retry_attempt: NotRequired[
        "capo_codepipeline.types.retry_attempt.RetryAttempt"
    ]
    """<p>The number of attempts for a specific stage with automatic retry on stage failure. One attempt is allowed for automatic stage retry on failure.</p>"""
    manual_stage_retry_attempt: NotRequired[
        "capo_codepipeline.types.retry_attempt.RetryAttempt"
    ]
    """<p>The number of attempts for a specific stage where manual retries have been made upon stage failure.</p>"""
    latest_retry_trigger: NotRequired[
        "capo_codepipeline.types.retry_trigger.RetryTrigger"
    ]
    """<p>The latest trigger for a specific stage where manual or automatic retries have been made upon stage failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryStageMetadata) -> dict:
    out: dict = {}
    if "auto_stage_retry_attempt" in value:
        out["autoStageRetryAttempt"] = value["auto_stage_retry_attempt"]
    if "manual_stage_retry_attempt" in value:
        out["manualStageRetryAttempt"] = value["manual_stage_retry_attempt"]
    if "latest_retry_trigger" in value:
        import capo_codepipeline.types.retry_trigger

        out["latestRetryTrigger"] = (
            capo_codepipeline.types.retry_trigger.serialize_aws_json_1_1(
                value["latest_retry_trigger"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RetryStageMetadata:
    out: RetryStageMetadata = {}  # type: ignore[typeddict-item]
    if data.get("autoStageRetryAttempt") is not None:
        out["auto_stage_retry_attempt"] = data["autoStageRetryAttempt"]
    if data.get("manualStageRetryAttempt") is not None:
        out["manual_stage_retry_attempt"] = data["manualStageRetryAttempt"]
    if data.get("latestRetryTrigger") is not None:
        import capo_codepipeline.types.retry_trigger

        out["latest_retry_trigger"] = (
            capo_codepipeline.types.retry_trigger.deserialize_aws_json_1_1(
                data["latestRetryTrigger"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RetryStageMetadata) -> dict:
    out: dict = {}
    if "auto_stage_retry_attempt" in value:
        out["autoStageRetryAttempt"] = value["auto_stage_retry_attempt"]
    if "manual_stage_retry_attempt" in value:
        out["manualStageRetryAttempt"] = value["manual_stage_retry_attempt"]
    if "latest_retry_trigger" in value:
        import capo_codepipeline.types.retry_trigger

        out["latestRetryTrigger"] = (
            capo_codepipeline.types.retry_trigger.serialize_cbor(
                value["latest_retry_trigger"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RetryStageMetadata:
    out: RetryStageMetadata = {}  # type: ignore[typeddict-item]
    if data.get("autoStageRetryAttempt") is not None:
        out["auto_stage_retry_attempt"] = data["autoStageRetryAttempt"]
    if data.get("manualStageRetryAttempt") is not None:
        out["manual_stage_retry_attempt"] = data["manualStageRetryAttempt"]
    if data.get("latestRetryTrigger") is not None:
        import capo_codepipeline.types.retry_trigger

        out["latest_retry_trigger"] = (
            capo_codepipeline.types.retry_trigger.deserialize_cbor(
                data["latestRetryTrigger"]
            )
        )
    return out
