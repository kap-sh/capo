"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchLogsSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.cloud_watch_filter_config
    import capo_bedrock_agentcore.types.evaluation_string_list
    import capo_bedrock_agentcore.types.log_group_name_list
    import capo_bedrock_agentcore.types.log_group_name_prefix_list


class CloudWatchLogsSource(TypedDict, closed=True):
    service_names: (
        "capo_bedrock_agentcore.types.evaluation_string_list.EvaluationStringList"
    )
    """<p>The list of agent service names to filter traces within the specified log groups.</p>"""
    log_group_names: "capo_bedrock_agentcore.types.log_group_name_list.LogGroupNameList"
    """<p>The list of CloudWatch log group names to read agent traces from. Maximum of 10 log groups.</p>"""
    log_group_name_prefixes: NotRequired[
        "capo_bedrock_agentcore.types.log_group_name_prefix_list.LogGroupNamePrefixList"
    ]
    """<p>The list of CloudWatch log group name prefixes to read agent traces from. Specify this instead of <code>logGroupNames</code> to match log groups by prefix. Maximum of 5 prefixes. Specify either <code>logGroupNames</code> or <code>logGroupNamePrefixes</code>, not both. One of the two is required.</p>"""
    filter_config: NotRequired[
        "capo_bedrock_agentcore.types.cloud_watch_filter_config.CloudWatchFilterConfig"
    ]
    """<p>Optional filter configuration to narrow down which sessions to evaluate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsSource) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.evaluation_string_list

    out["serviceNames"] = (
        capo_bedrock_agentcore.types.evaluation_string_list.serialize_json(
            value["service_names"]
        )
    )
    import capo_bedrock_agentcore.types.log_group_name_list

    out["logGroupNames"] = (
        capo_bedrock_agentcore.types.log_group_name_list.serialize_json(
            value.get("log_group_names", [])
        )
    )
    if "log_group_name_prefixes" in value:
        import capo_bedrock_agentcore.types.log_group_name_prefix_list

        out["logGroupNamePrefixes"] = (
            capo_bedrock_agentcore.types.log_group_name_prefix_list.serialize_json(
                value["log_group_name_prefixes"]
            )
        )
    if "filter_config" in value:
        import capo_bedrock_agentcore.types.cloud_watch_filter_config

        out["filterConfig"] = (
            capo_bedrock_agentcore.types.cloud_watch_filter_config.serialize_json(
                value["filter_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CloudWatchLogsSource:
    out: CloudWatchLogsSource = {}  # type: ignore[typeddict-item]
    if data.get("serviceNames") is not None:
        import capo_bedrock_agentcore.types.evaluation_string_list

        out["service_names"] = (
            capo_bedrock_agentcore.types.evaluation_string_list.deserialize_json(
                data["serviceNames"]
            )
        )
    else:
        out["service_names"] = []
    if data.get("logGroupNames") is not None:
        import capo_bedrock_agentcore.types.log_group_name_list

        out["log_group_names"] = (
            capo_bedrock_agentcore.types.log_group_name_list.deserialize_json(
                data["logGroupNames"]
            )
        )
    else:
        out["log_group_names"] = []
    if data.get("logGroupNamePrefixes") is not None:
        import capo_bedrock_agentcore.types.log_group_name_prefix_list

        out["log_group_name_prefixes"] = (
            capo_bedrock_agentcore.types.log_group_name_prefix_list.deserialize_json(
                data["logGroupNamePrefixes"]
            )
        )
    if data.get("filterConfig") is not None:
        import capo_bedrock_agentcore.types.cloud_watch_filter_config

        out["filter_config"] = (
            capo_bedrock_agentcore.types.cloud_watch_filter_config.deserialize_json(
                data["filterConfig"]
            )
        )
    return out
