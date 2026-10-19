"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#LoggingConfiguration``."""

from typing_extensions import TypedDict


class LoggingConfiguration(TypedDict, closed=True):
    log_group_name: "str"
    """<p>The name of the CloudWatch log group where workflow execution logs are stored.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LoggingConfiguration) -> dict:
    out: dict = {}
    out["LogGroupName"] = value["log_group_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LoggingConfiguration:
    out: LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LogGroupName") is not None:
        out["log_group_name"] = data["LogGroupName"]
    else:
        out["log_group_name"] = ""
    return out
