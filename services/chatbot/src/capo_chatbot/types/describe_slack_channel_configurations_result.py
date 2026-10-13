"""Generated from Smithy shape ``com.amazonaws.chatbot#DescribeSlackChannelConfigurationsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.pagination_token
    import capo_chatbot.types.slack_channel_configuration_list


class DescribeSlackChannelConfigurationsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_chatbot.types.pagination_token.PaginationToken"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>"""
    slack_channel_configurations: NotRequired[
        "capo_chatbot.types.slack_channel_configuration_list.SlackChannelConfigurationList"
    ]
    """<p>A list of Slack channel configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSlackChannelConfigurationsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "slack_channel_configurations" in value:
        import capo_chatbot.types.slack_channel_configuration_list

        out["SlackChannelConfigurations"] = (
            capo_chatbot.types.slack_channel_configuration_list.serialize_json(
                value["slack_channel_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeSlackChannelConfigurationsResult:
    out: DescribeSlackChannelConfigurationsResult = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("SlackChannelConfigurations") is not None:
        import capo_chatbot.types.slack_channel_configuration_list

        out["slack_channel_configurations"] = (
            capo_chatbot.types.slack_channel_configuration_list.deserialize_json(
                data["SlackChannelConfigurations"]
            )
        )
    return out


def redact_sensitive(value: DescribeSlackChannelConfigurationsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "slack_channel_configurations" in value:
        import capo_chatbot.types.slack_channel_configuration_list

        out["slack_channel_configurations"] = (
            capo_chatbot.types.slack_channel_configuration_list.redact_sensitive(
                value["slack_channel_configurations"]
            )
        )
    return out
