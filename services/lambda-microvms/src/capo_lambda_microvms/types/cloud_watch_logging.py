"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#CloudWatchLogging``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.string


class CloudWatchLogging(TypedDict, closed=True):
    log_group: NotRequired["capo_lambda_microvms.types.string.String"]
    """<p>The name of the CloudWatch Logs log group to send logs to.</p>"""
    log_stream: NotRequired["capo_lambda_microvms.types.string.String"]
    """<p>The name of the CloudWatch Logs log stream within the log group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogging) -> dict:
    out: dict = {}
    if "log_group" in value:
        out["logGroup"] = value["log_group"]
    if "log_stream" in value:
        out["logStream"] = value["log_stream"]
    return out


def deserialize_json(data: dict) -> CloudWatchLogging:
    out: CloudWatchLogging = {}  # type: ignore[typeddict-item]
    if data.get("logGroup") is not None:
        out["log_group"] = data["logGroup"]
    if data.get("logStream") is not None:
        out["log_stream"] = data["logStream"]
    return out
