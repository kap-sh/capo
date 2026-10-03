"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBotChannelAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.alias_name_or_list_all
    import capo_lex_model_building_service.types.bot_channel_name
    import capo_lex_model_building_service.types.bot_name
    import capo_lex_model_building_service.types.max_results
    import capo_lex_model_building_service.types.next_token


class GetBotChannelAssociationsRequest(TypedDict, closed=True):
    bot_name: "capo_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the Amazon Lex bot in the association.</p>"""
    bot_alias: "capo_lex_model_building_service.types.alias_name_or_list_all.AliasNameOrListAll"
    """<p>An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.</p>"""
    next_token: NotRequired[
        "capo_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token for fetching the next page of associations. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of associations, specify the pagination token in the next request. </p>"""
    max_results: NotRequired[
        "capo_lex_model_building_service.types.max_results.MaxResults"
    ]
    """<p>The maximum number of associations to return in the response. The default is 50. </p>"""
    name_contains: NotRequired[
        "capo_lex_model_building_service.types.bot_channel_name.BotChannelName"
    ]
    """<p>Substring to match in channel association names. An association will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz." To return all bot channel associations, use a hyphen ("-") as the <code>nameContains</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotChannelAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBotChannelAssociationsRequest:
    out: GetBotChannelAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
