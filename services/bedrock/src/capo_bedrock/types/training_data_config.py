"""Generated from Smithy shape ``com.amazonaws.bedrock#TrainingDataConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.invocation_logs_config
    import capo_bedrock.types.s3_uri


class TrainingDataConfig(TypedDict, closed=True):
    s3_uri: NotRequired["capo_bedrock.types.s3_uri.S3Uri"]
    """<p>The S3 URI where the training data is stored.</p>"""
    invocation_logs_config: NotRequired[
        "capo_bedrock.types.invocation_logs_config.InvocationLogsConfig"
    ]
    """<p>Settings for using invocation logs to customize a model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainingDataConfig) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["s3Uri"] = value["s3_uri"]
    if "invocation_logs_config" in value:
        import capo_bedrock.types.invocation_logs_config

        out["invocationLogsConfig"] = (
            capo_bedrock.types.invocation_logs_config.serialize_json(
                value["invocation_logs_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> TrainingDataConfig:
    out: TrainingDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    if data.get("invocationLogsConfig") is not None:
        import capo_bedrock.types.invocation_logs_config

        out["invocation_logs_config"] = (
            capo_bedrock.types.invocation_logs_config.deserialize_json(
                data["invocationLogsConfig"]
            )
        )
    return out


def redact_sensitive(value: TrainingDataConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "invocation_logs_config" in value:
        import capo_bedrock.types.invocation_logs_config

        out["invocation_logs_config"] = (
            capo_bedrock.types.invocation_logs_config.redact_sensitive(
                value["invocation_logs_config"]
            )
        )
    return out
