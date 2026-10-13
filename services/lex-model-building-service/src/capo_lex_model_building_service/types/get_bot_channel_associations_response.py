"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBotChannelAssociationsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.bot_channel_association_list
    import capo_lex_model_building_service.types.next_token


class GetBotChannelAssociationsResponse(TypedDict, closed=True):
    bot_channel_associations: NotRequired[
        "capo_lex_model_building_service.types.bot_channel_association_list.BotChannelAssociationList"
    ]
    """<p>An array of objects, one for each association, that provides information about the Amazon Lex bot and its association with the channel. </p>"""
    next_token: NotRequired[
        "capo_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token that fetches the next page of associations. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of associations, specify the pagination token in the next request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotChannelAssociationsResponse) -> dict:
    out: dict = {}
    if "bot_channel_associations" in value:
        import capo_lex_model_building_service.types.bot_channel_association_list

        out["botChannelAssociations"] = (
            capo_lex_model_building_service.types.bot_channel_association_list.serialize_json(
                value["bot_channel_associations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetBotChannelAssociationsResponse:
    out: GetBotChannelAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("botChannelAssociations") is not None:
        import capo_lex_model_building_service.types.bot_channel_association_list

        out["bot_channel_associations"] = (
            capo_lex_model_building_service.types.bot_channel_association_list.deserialize_json(
                data["botChannelAssociations"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: GetBotChannelAssociationsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bot_channel_associations" in value:
        import capo_lex_model_building_service.types.bot_channel_association_list

        out["bot_channel_associations"] = (
            capo_lex_model_building_service.types.bot_channel_association_list.redact_sensitive(
                value["bot_channel_associations"]
            )
        )
    return out
