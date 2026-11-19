"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchLogsSourceConfigLogGroupNamePrefixesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.log_group_name_prefix

CloudWatchLogsSourceConfigLogGroupNamePrefixesList: TypeAlias = list[
    "capo_bedrock_agentcore.types.log_group_name_prefix.LogGroupNamePrefix"
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsSourceConfigLogGroupNamePrefixesList) -> list:
    return list(value)


def deserialize_json(data: list) -> CloudWatchLogsSourceConfigLogGroupNamePrefixesList:
    return [item for item in data if item is not None]
