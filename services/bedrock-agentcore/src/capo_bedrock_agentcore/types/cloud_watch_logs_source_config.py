"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchLogsSourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.cloud_watch_logs_source_config_log_group_name_prefixes_list
    import capo_bedrock_agentcore.types.cloud_watch_logs_source_config_log_group_names_list
    import capo_bedrock_agentcore.types.service_name_list


class CloudWatchLogsSourceConfig(TypedDict, closed=True):
    log_group_names: NotRequired[
        "capo_bedrock_agentcore.types.cloud_watch_logs_source_config_log_group_names_list.CloudWatchLogsSourceConfigLogGroupNamesList"
    ]
    """<p>The names of the log groups to read, from 1 to 5. You can't specify this together with <code>logGroupNamePrefixes</code>.</p>"""
    log_group_name_prefixes: NotRequired[
        "capo_bedrock_agentcore.types.cloud_watch_logs_source_config_log_group_name_prefixes_list.CloudWatchLogsSourceConfigLogGroupNamePrefixesList"
    ]
    """<p>Prefixes of the names of the log groups to read, from 1 to 5. You can't specify this together with <code>logGroupNames</code>.</p>"""
    service_names: "capo_bedrock_agentcore.types.service_name_list.ServiceNameList"
    """<p>The service name of the agent, which matches the <code>service.name</code> resource attribute in its traces. Specify exactly one.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start of the time window to read sessions from. The default is 7 days before <code>endTime</code>.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end of the time window to read sessions from. The default is the time the generation starts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsSourceConfig) -> dict:
    out: dict = {}
    if "log_group_names" in value:
        import capo_bedrock_agentcore.types.cloud_watch_logs_source_config_log_group_names_list

        out["logGroupNames"] = (
            capo_bedrock_agentcore.types.cloud_watch_logs_source_config_log_group_names_list.serialize_json(
                value["log_group_names"]
            )
        )
    if "log_group_name_prefixes" in value:
        import capo_bedrock_agentcore.types.cloud_watch_logs_source_config_log_group_name_prefixes_list

        out["logGroupNamePrefixes"] = (
            capo_bedrock_agentcore.types.cloud_watch_logs_source_config_log_group_name_prefixes_list.serialize_json(
                value["log_group_name_prefixes"]
            )
        )
    import capo_bedrock_agentcore.types.service_name_list

    out["serviceNames"] = capo_bedrock_agentcore.types.service_name_list.serialize_json(
        value["service_names"]
    )
    if "start_time" in value:
        import capo_bedrock_agentcore._protocol.serialize

        out["startTime"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_bedrock_agentcore._protocol.serialize

        out["endTime"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> CloudWatchLogsSourceConfig:
    out: CloudWatchLogsSourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("logGroupNames") is not None:
        import capo_bedrock_agentcore.types.cloud_watch_logs_source_config_log_group_names_list

        out["log_group_names"] = (
            capo_bedrock_agentcore.types.cloud_watch_logs_source_config_log_group_names_list.deserialize_json(
                data["logGroupNames"]
            )
        )
    if data.get("logGroupNamePrefixes") is not None:
        import capo_bedrock_agentcore.types.cloud_watch_logs_source_config_log_group_name_prefixes_list

        out["log_group_name_prefixes"] = (
            capo_bedrock_agentcore.types.cloud_watch_logs_source_config_log_group_name_prefixes_list.deserialize_json(
                data["logGroupNamePrefixes"]
            )
        )
    if data.get("serviceNames") is not None:
        import capo_bedrock_agentcore.types.service_name_list

        out["service_names"] = (
            capo_bedrock_agentcore.types.service_name_list.deserialize_json(
                data["serviceNames"]
            )
        )
    else:
        out["service_names"] = []
    if data.get("startTime") is not None:
        import datetime

        out["start_time"] = datetime.datetime.fromisoformat(
            data["startTime"].replace("Z", "+00:00")
        )
    if data.get("endTime") is not None:
        import datetime

        out["end_time"] = datetime.datetime.fromisoformat(
            data["endTime"].replace("Z", "+00:00")
        )
    return out
