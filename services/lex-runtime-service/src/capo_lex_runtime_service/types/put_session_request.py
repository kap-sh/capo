"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#PutSessionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.accept
    import capo_lex_runtime_service.types.active_contexts_list
    import capo_lex_runtime_service.types.bot_alias
    import capo_lex_runtime_service.types.bot_name
    import capo_lex_runtime_service.types.dialog_action
    import capo_lex_runtime_service.types.intent_summary_list
    import capo_lex_runtime_service.types.string_map
    import capo_lex_runtime_service.types.user_id


class PutSessionRequest(TypedDict, closed=True):
    bot_name: "capo_lex_runtime_service.types.bot_name.BotName"
    """<p>The name of the bot that contains the session data.</p>"""
    bot_alias: "capo_lex_runtime_service.types.bot_alias.BotAlias"
    """<p>The alias in use for the bot that contains the session data.</p>"""
    user_id: "capo_lex_runtime_service.types.user_id.UserId"
    """<p>The ID of the client application user. Amazon Lex uses this to identify a user's conversation with your bot. </p>"""
    session_attributes: NotRequired[
        "capo_lex_runtime_service.types.string_map.StringMap"
    ]
    """<p>Map of key/value pairs representing the session-specific context information. It contains application information passed between Amazon Lex and a client application.</p>"""
    dialog_action: NotRequired[
        "capo_lex_runtime_service.types.dialog_action.DialogAction"
    ]
    """<p>Sets the next action that the bot should take to fulfill the conversation.</p>"""
    recent_intent_summary_view: NotRequired[
        "capo_lex_runtime_service.types.intent_summary_list.IntentSummaryList"
    ]
    """<p>A summary of the recent intents for the bot. You can use the intent summary view to set a checkpoint label on an intent and modify attributes of intents. You can also use it to remove or add intent summary objects to the list.</p> <p>An intent that you modify or add to the list must make sense for the bot. For example, the intent name must be valid for the bot. You must provide valid values for:</p> <ul> <li> <p> <code>intentName</code> </p> </li> <li> <p>slot names</p> </li> <li> <p> <code>slotToElict</code> </p> </li> </ul> <p>If you send the <code>recentIntentSummaryView</code> parameter in a <code>PutSession</code> request, the contents of the new summary view replaces the old summary view. For example, if a <code>GetSession</code> request returns three intents in the summary view and you call <code>PutSession</code> with one intent in the summary view, the next call to <code>GetSession</code> will only return one intent.</p>"""
    accept: NotRequired["capo_lex_runtime_service.types.accept.Accept"]
    """<p>The message that Amazon Lex returns in the response can be either text or speech based depending on the value of this field.</p> <ul> <li> <p>If the value is <code>text/plain; charset=utf-8</code>, Amazon Lex returns text in the response.</p> </li> <li> <p>If the value begins with <code>audio/</code>, Amazon Lex returns speech in the response. Amazon Lex uses Amazon Polly to generate the speech in the configuration that you specify. For example, if you specify <code>audio/mpeg</code> as the value, Amazon Lex returns speech in the MPEG format.</p> </li> <li> <p>If the value is <code>audio/pcm</code>, the speech is returned as <code>audio/pcm</code> in 16-bit, little endian format.</p> </li> <li> <p>The following are the accepted values:</p> <ul> <li> <p> <code>audio/mpeg</code> </p> </li> <li> <p> <code>audio/ogg</code> </p> </li> <li> <p> <code>audio/pcm</code> </p> </li> <li> <p> <code>audio/*</code> (defaults to mpeg)</p> </li> <li> <p> <code>text/plain; charset=utf-8</code> </p> </li> </ul> </li> </ul>"""
    active_contexts: NotRequired[
        "capo_lex_runtime_service.types.active_contexts_list.ActiveContextsList"
    ]
    """<p>A list of contexts active for the request. A context can be activated when a previous intent is fulfilled, or by including the context in the request,</p> <p>If you don't specify a list of contexts, Amazon Lex will use the current list of contexts for the session. If you specify an empty list, all contexts for the session are cleared.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSessionRequest) -> dict:
    out: dict = {}
    if "session_attributes" in value:
        import capo_lex_runtime_service.types.string_map

        out["sessionAttributes"] = (
            capo_lex_runtime_service.types.string_map.serialize_json(
                value["session_attributes"]
            )
        )
    if "dialog_action" in value:
        import capo_lex_runtime_service.types.dialog_action

        out["dialogAction"] = (
            capo_lex_runtime_service.types.dialog_action.serialize_json(
                value["dialog_action"]
            )
        )
    if "recent_intent_summary_view" in value:
        import capo_lex_runtime_service.types.intent_summary_list

        out["recentIntentSummaryView"] = (
            capo_lex_runtime_service.types.intent_summary_list.serialize_json(
                value["recent_intent_summary_view"]
            )
        )
    if "active_contexts" in value:
        import capo_lex_runtime_service.types.active_contexts_list

        out["activeContexts"] = (
            capo_lex_runtime_service.types.active_contexts_list.serialize_json(
                value["active_contexts"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutSessionRequest:
    out: PutSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("sessionAttributes") is not None:
        import capo_lex_runtime_service.types.string_map

        out["session_attributes"] = (
            capo_lex_runtime_service.types.string_map.deserialize_json(
                data["sessionAttributes"]
            )
        )
    if data.get("dialogAction") is not None:
        import capo_lex_runtime_service.types.dialog_action

        out["dialog_action"] = (
            capo_lex_runtime_service.types.dialog_action.deserialize_json(
                data["dialogAction"]
            )
        )
    if data.get("recentIntentSummaryView") is not None:
        import capo_lex_runtime_service.types.intent_summary_list

        out["recent_intent_summary_view"] = (
            capo_lex_runtime_service.types.intent_summary_list.deserialize_json(
                data["recentIntentSummaryView"]
            )
        )
    if data.get("activeContexts") is not None:
        import capo_lex_runtime_service.types.active_contexts_list

        out["active_contexts"] = (
            capo_lex_runtime_service.types.active_contexts_list.deserialize_json(
                data["activeContexts"]
            )
        )
    return out


def redact_sensitive(value: PutSessionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "session_attributes" in value:
        out["session_attributes"] = "*** Sensitive Data Redacted ***"
    if "dialog_action" in value:
        import capo_lex_runtime_service.types.dialog_action

        out["dialog_action"] = (
            capo_lex_runtime_service.types.dialog_action.redact_sensitive(
                value["dialog_action"]
            )
        )
    if "recent_intent_summary_view" in value:
        import capo_lex_runtime_service.types.intent_summary_list

        out["recent_intent_summary_view"] = (
            capo_lex_runtime_service.types.intent_summary_list.redact_sensitive(
                value["recent_intent_summary_view"]
            )
        )
    if "active_contexts" in value:
        out["active_contexts"] = "*** Sensitive Data Redacted ***"
    return out
