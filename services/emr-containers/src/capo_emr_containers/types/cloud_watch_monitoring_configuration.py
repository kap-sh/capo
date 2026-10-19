"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CloudWatchMonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.log_group_name
    import capo_emr_containers.types.string256


class CloudWatchMonitoringConfiguration(TypedDict, closed=True):
    log_group_name: "capo_emr_containers.types.log_group_name.LogGroupName"
    """<p>The name of the log group for log publishing.</p>"""
    log_stream_name_prefix: NotRequired["capo_emr_containers.types.string256.String256"]
    """<p>The specified name prefix for log streams.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchMonitoringConfiguration) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    if "log_stream_name_prefix" in value:
        out["logStreamNamePrefix"] = value["log_stream_name_prefix"]
    return out


def deserialize_json(data: dict) -> CloudWatchMonitoringConfiguration:
    out: CloudWatchMonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        out["log_group_name"] = ""
    if data.get("logStreamNamePrefix") is not None:
        out["log_stream_name_prefix"] = data["logStreamNamePrefix"]
    return out
