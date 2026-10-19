"""Generated from Smithy shape ``com.amazonaws.supportapp#ListSlackChannelConfigurationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support_app.types.pagination_token
    import capo_support_app.types.slack_channel_configuration_list


class ListSlackChannelConfigurationsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_support_app.types.pagination_token.paginationToken"]
    """<p>The point where pagination should resume when the response returns only partial results.</p>"""
    slack_channel_configurations: "capo_support_app.types.slack_channel_configuration_list.slackChannelConfigurationList"
    """<p>The configurations for a Slack channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSlackChannelConfigurationsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_support_app.types.slack_channel_configuration_list

    out["slackChannelConfigurations"] = (
        capo_support_app.types.slack_channel_configuration_list.serialize_json(
            value["slack_channel_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListSlackChannelConfigurationsResult:
    out: ListSlackChannelConfigurationsResult = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("slackChannelConfigurations") is not None:
        import capo_support_app.types.slack_channel_configuration_list

        out["slack_channel_configurations"] = (
            capo_support_app.types.slack_channel_configuration_list.deserialize_json(
                data["slackChannelConfigurations"]
            )
        )
    else:
        out["slack_channel_configurations"] = []
    return out
