"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceAwsLogsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class ExpressGatewayServiceAwsLogsConfiguration(TypedDict, closed=True):
    log_group: "capo_ecs.types.string.String"
    """<p>The name of the CloudWatch Logs log group to send container logs to.</p>"""
    log_stream_prefix: "capo_ecs.types.string.String"
    """<p>The prefix for the CloudWatch Logs log stream names. The default for an Express service is <code>ecs</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayServiceAwsLogsConfiguration) -> dict:
    out: dict = {}
    out["logGroup"] = value["log_group"]
    out["logStreamPrefix"] = value["log_stream_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpressGatewayServiceAwsLogsConfiguration:
    out: ExpressGatewayServiceAwsLogsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("logGroup") is not None:
        out["log_group"] = data["logGroup"]
    else:
        out["log_group"] = ""
    if data.get("logStreamPrefix") is not None:
        out["log_stream_prefix"] = data["logStreamPrefix"]
    else:
        out["log_stream_prefix"] = ""
    return out
