"""Generated from Smithy shape ``com.amazonaws.athena#CloudWatchLoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.boxed_boolean
    import capo_athena.types.log_group_name
    import capo_athena.types.log_stream_name_prefix
    import capo_athena.types.log_types_map


class CloudWatchLoggingConfiguration(TypedDict, closed=True):
    enabled: "capo_athena.types.boxed_boolean.BoxedBoolean"
    """<p>Enables CloudWatch logging.</p>"""
    log_group: NotRequired["capo_athena.types.log_group_name.LogGroupName"]
    """<p>The name of the log group in Amazon CloudWatch Logs where you want to publish your logs.</p>"""
    log_stream_name_prefix: NotRequired[
        "capo_athena.types.log_stream_name_prefix.LogStreamNamePrefix"
    ]
    """<p>Prefix for the CloudWatch log stream name.</p>"""
    log_types: NotRequired["capo_athena.types.log_types_map.LogTypesMap"]
    """<p>The types of logs that you want to publish to CloudWatch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "log_group" in value:
        out["LogGroup"] = value["log_group"]
    if "log_stream_name_prefix" in value:
        out["LogStreamNamePrefix"] = value["log_stream_name_prefix"]
    if "log_types" in value:
        import capo_athena.types.log_types_map

        out["LogTypes"] = capo_athena.types.log_types_map.serialize_aws_json_1_1(
            value["log_types"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLoggingConfiguration:
    out: CloudWatchLoggingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("LogGroup") is not None:
        out["log_group"] = data["LogGroup"]
    if data.get("LogStreamNamePrefix") is not None:
        out["log_stream_name_prefix"] = data["LogStreamNamePrefix"]
    if data.get("LogTypes") is not None:
        import capo_athena.types.log_types_map

        out["log_types"] = capo_athena.types.log_types_map.deserialize_aws_json_1_1(
            data["LogTypes"]
        )
    return out
