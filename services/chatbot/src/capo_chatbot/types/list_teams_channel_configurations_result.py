"""Generated from Smithy shape ``com.amazonaws.chatbot#ListTeamsChannelConfigurationsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.pagination_token
    import capo_chatbot.types.team_channel_configurations_list


class ListTeamsChannelConfigurationsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_chatbot.types.pagination_token.PaginationToken"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>"""
    team_channel_configurations: NotRequired[
        "capo_chatbot.types.team_channel_configurations_list.TeamChannelConfigurationsList"
    ]
    """<p>A list of AWS Chatbot channel configurations for Microsoft Teams.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTeamsChannelConfigurationsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "team_channel_configurations" in value:
        import capo_chatbot.types.team_channel_configurations_list

        out["TeamChannelConfigurations"] = (
            capo_chatbot.types.team_channel_configurations_list.serialize_json(
                value["team_channel_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListTeamsChannelConfigurationsResult:
    out: ListTeamsChannelConfigurationsResult = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("TeamChannelConfigurations") is not None:
        import capo_chatbot.types.team_channel_configurations_list

        out["team_channel_configurations"] = (
            capo_chatbot.types.team_channel_configurations_list.deserialize_json(
                data["TeamChannelConfigurations"]
            )
        )
    return out


def redact_sensitive(value: ListTeamsChannelConfigurationsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "team_channel_configurations" in value:
        import capo_chatbot.types.team_channel_configurations_list

        out["team_channel_configurations"] = (
            capo_chatbot.types.team_channel_configurations_list.redact_sensitive(
                value["team_channel_configurations"]
            )
        )
    return out
