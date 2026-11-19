"""Generated from Smithy shape ``com.amazonaws.codepipeline#RetryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.stage_retry_mode


class RetryConfiguration(TypedDict, closed=True):
    retry_mode: NotRequired["capo_codepipeline.types.stage_retry_mode.StageRetryMode"]
    """<p>The method that you want to configure for automatic stage retry on stage failure. You can specify to retry only failed action in the stage or all actions in the stage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryConfiguration) -> dict:
    out: dict = {}
    if "retry_mode" in value:
        import capo_codepipeline.types.stage_retry_mode

        out["retryMode"] = (
            capo_codepipeline.types.stage_retry_mode.serialize_aws_json_1_1(
                value["retry_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RetryConfiguration:
    out: RetryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("retryMode") is not None:
        import capo_codepipeline.types.stage_retry_mode

        out["retry_mode"] = (
            capo_codepipeline.types.stage_retry_mode.deserialize_aws_json_1_1(
                data["retryMode"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RetryConfiguration) -> dict:
    out: dict = {}
    if "retry_mode" in value:
        import capo_codepipeline.types.stage_retry_mode

        out["retryMode"] = capo_codepipeline.types.stage_retry_mode.serialize_cbor(
            value["retry_mode"]
        )
    return out


def deserialize_cbor(data: dict) -> RetryConfiguration:
    out: RetryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("retryMode") is not None:
        import capo_codepipeline.types.stage_retry_mode

        out["retry_mode"] = capo_codepipeline.types.stage_retry_mode.deserialize_cbor(
            data["retryMode"]
        )
    return out
