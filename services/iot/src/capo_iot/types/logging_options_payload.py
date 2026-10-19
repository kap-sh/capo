"""Generated from Smithy shape ``com.amazonaws.iot#LoggingOptionsPayload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.log_level


class LoggingOptionsPayload(TypedDict, closed=True):
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the IAM role that grants access.</p>"""
    log_level: NotRequired["capo_iot.types.log_level.LogLevel"]
    """<p>The log level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingOptionsPayload) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    if "log_level" in value:
        import capo_iot.types.log_level

        out["logLevel"] = capo_iot.types.log_level.serialize_json(value["log_level"])
    return out


def deserialize_json(data: dict) -> LoggingOptionsPayload:
    out: LoggingOptionsPayload = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("logLevel") is not None:
        import capo_iot.types.log_level

        out["log_level"] = capo_iot.types.log_level.deserialize_json(data["logLevel"])
    return out
