"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#GetSessionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.active_contexts_list
    import capo_lex_runtime_service.types.dialog_action
    import capo_lex_runtime_service.types.intent_summary_list
    import capo_lex_runtime_service.types.string
    import capo_lex_runtime_service.types.string_map


class GetSessionResponse(TypedDict, closed=True):
    recent_intent_summary_view: NotRequired[
        "capo_lex_runtime_service.types.intent_summary_list.IntentSummaryList"
    ]
    """<p>An array of information about the intents used in the session. The array can contain a maximum of three summaries. If more than three intents are used in the session, the <code>recentIntentSummaryView</code> operation contains information about the last three intents used.</p> <p>If you set the <code>checkpointLabelFilter</code> parameter in the request, the array contains only the intents with the specified label.</p>"""
    session_attributes: NotRequired[
        "capo_lex_runtime_service.types.string_map.StringMap"
    ]
    """<p>Map of key/value pairs representing the session-specific context information. It contains application information passed between Amazon Lex and a client application.</p>"""
    session_id: NotRequired["capo_lex_runtime_service.types.string.String"]
    """<p>A unique identifier for the session.</p>"""
    dialog_action: NotRequired[
        "capo_lex_runtime_service.types.dialog_action.DialogAction"
    ]
    """<p>Describes the current state of the bot.</p>"""
    active_contexts: NotRequired[
        "capo_lex_runtime_service.types.active_contexts_list.ActiveContextsList"
    ]
    """<p>A list of active contexts for the session. A context can be set when an intent is fulfilled or by calling the <code>PostContent</code>, <code>PostText</code>, or <code>PutSession</code> operation.</p> <p>You can use a context to control the intents that can follow up an intent, or to modify the operation of your application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionResponse) -> dict:
    out: dict = {}
    if "recent_intent_summary_view" in value:
        import capo_lex_runtime_service.types.intent_summary_list

        out["recentIntentSummaryView"] = (
            capo_lex_runtime_service.types.intent_summary_list.serialize_json(
                value["recent_intent_summary_view"]
            )
        )
    if "session_attributes" in value:
        import capo_lex_runtime_service.types.string_map

        out["sessionAttributes"] = (
            capo_lex_runtime_service.types.string_map.serialize_json(
                value["session_attributes"]
            )
        )
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "dialog_action" in value:
        import capo_lex_runtime_service.types.dialog_action

        out["dialogAction"] = (
            capo_lex_runtime_service.types.dialog_action.serialize_json(
                value["dialog_action"]
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


def deserialize_json(data: dict) -> GetSessionResponse:
    out: GetSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("recentIntentSummaryView") is not None:
        import capo_lex_runtime_service.types.intent_summary_list

        out["recent_intent_summary_view"] = (
            capo_lex_runtime_service.types.intent_summary_list.deserialize_json(
                data["recentIntentSummaryView"]
            )
        )
    if data.get("sessionAttributes") is not None:
        import capo_lex_runtime_service.types.string_map

        out["session_attributes"] = (
            capo_lex_runtime_service.types.string_map.deserialize_json(
                data["sessionAttributes"]
            )
        )
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("dialogAction") is not None:
        import capo_lex_runtime_service.types.dialog_action

        out["dialog_action"] = (
            capo_lex_runtime_service.types.dialog_action.deserialize_json(
                data["dialogAction"]
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


def redact_sensitive(value: GetSessionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recent_intent_summary_view" in value:
        import capo_lex_runtime_service.types.intent_summary_list

        out["recent_intent_summary_view"] = (
            capo_lex_runtime_service.types.intent_summary_list.redact_sensitive(
                value["recent_intent_summary_view"]
            )
        )
    if "session_attributes" in value:
        out["session_attributes"] = "*** Sensitive Data Redacted ***"
    if "dialog_action" in value:
        import capo_lex_runtime_service.types.dialog_action

        out["dialog_action"] = (
            capo_lex_runtime_service.types.dialog_action.redact_sensitive(
                value["dialog_action"]
            )
        )
    if "active_contexts" in value:
        out["active_contexts"] = "*** Sensitive Data Redacted ***"
    return out
