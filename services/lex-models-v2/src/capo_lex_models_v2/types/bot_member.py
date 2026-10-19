"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotMember``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_alias_id
    import capo_lex_models_v2.types.bot_alias_name
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.name


class BotMember(TypedDict, closed=True):
    bot_member_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique ID of a bot that is a member of this network of bots.</p>"""
    bot_member_name: "capo_lex_models_v2.types.name.Name"
    """<p>The unique name of a bot that is a member of this network of bots.</p>"""
    bot_member_alias_id: "capo_lex_models_v2.types.bot_alias_id.BotAliasId"
    """<p>The alias ID of a bot that is a member of this network of bots.</p>"""
    bot_member_alias_name: "capo_lex_models_v2.types.bot_alias_name.BotAliasName"
    """<p>The alias name of a bot that is a member of this network of bots.</p>"""
    bot_member_version: "capo_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of a bot that is a member of this network of bots.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotMember) -> dict:
    out: dict = {}
    out["botMemberId"] = value["bot_member_id"]
    out["botMemberName"] = value["bot_member_name"]
    out["botMemberAliasId"] = value["bot_member_alias_id"]
    out["botMemberAliasName"] = value["bot_member_alias_name"]
    out["botMemberVersion"] = value["bot_member_version"]
    return out


def deserialize_json(data: dict) -> BotMember:
    out: BotMember = {}  # type: ignore[typeddict-item]
    if data.get("botMemberId") is not None:
        out["bot_member_id"] = data["botMemberId"]
    else:
        out["bot_member_id"] = ""
    if data.get("botMemberName") is not None:
        out["bot_member_name"] = data["botMemberName"]
    else:
        out["bot_member_name"] = ""
    if data.get("botMemberAliasId") is not None:
        out["bot_member_alias_id"] = data["botMemberAliasId"]
    else:
        out["bot_member_alias_id"] = ""
    if data.get("botMemberAliasName") is not None:
        out["bot_member_alias_name"] = data["botMemberAliasName"]
    else:
        out["bot_member_alias_name"] = ""
    if data.get("botMemberVersion") is not None:
        out["bot_member_version"] = data["botMemberVersion"]
    else:
        out["bot_member_version"] = ""
    return out
