"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#SessionState``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.active_contexts_list
    import capo_lex_runtime_v2.types.dialog_action
    import capo_lex_runtime_v2.types.intent
    import capo_lex_runtime_v2.types.non_empty_string
    import capo_lex_runtime_v2.types.runtime_hints
    import capo_lex_runtime_v2.types.string_map


class SessionState(TypedDict, closed=True):
    dialog_action: NotRequired["capo_lex_runtime_v2.types.dialog_action.DialogAction"]
    """<p>The next step that Amazon Lex V2 should take in the conversation with a user.</p>"""
    intent: NotRequired["capo_lex_runtime_v2.types.intent.Intent"]
    """<p>The active intent that Amazon Lex V2 is processing.</p>"""
    active_contexts: NotRequired[
        "capo_lex_runtime_v2.types.active_contexts_list.ActiveContextsList"
    ]
    """<p>One or more contexts that indicate to Amazon Lex V2 the context of a request. When a context is active, Amazon Lex V2 considers intents with the matching context as a trigger as the next intent in a session.</p>"""
    session_attributes: NotRequired["capo_lex_runtime_v2.types.string_map.StringMap"]
    """<p>Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex V2 and a client application.</p>"""
    originating_request_id: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>A unique identifier for a specific request.</p>"""
    runtime_hints: NotRequired["capo_lex_runtime_v2.types.runtime_hints.RuntimeHints"]
    """<p>Hints for phrases that a customer is likely to use for a slot. Amazon Lex V2 uses the hints to help determine the correct value of a slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionState) -> dict:
    out: dict = {}
    if "dialog_action" in value:
        import capo_lex_runtime_v2.types.dialog_action

        out["dialogAction"] = capo_lex_runtime_v2.types.dialog_action.serialize_json(
            value["dialog_action"]
        )
    if "intent" in value:
        import capo_lex_runtime_v2.types.intent

        out["intent"] = capo_lex_runtime_v2.types.intent.serialize_json(value["intent"])
    if "active_contexts" in value:
        import capo_lex_runtime_v2.types.active_contexts_list

        out["activeContexts"] = (
            capo_lex_runtime_v2.types.active_contexts_list.serialize_json(
                value["active_contexts"]
            )
        )
    if "session_attributes" in value:
        import capo_lex_runtime_v2.types.string_map

        out["sessionAttributes"] = capo_lex_runtime_v2.types.string_map.serialize_json(
            value["session_attributes"]
        )
    if "originating_request_id" in value:
        out["originatingRequestId"] = value["originating_request_id"]
    if "runtime_hints" in value:
        import capo_lex_runtime_v2.types.runtime_hints

        out["runtimeHints"] = capo_lex_runtime_v2.types.runtime_hints.serialize_json(
            value["runtime_hints"]
        )
    return out


def deserialize_json(data: dict) -> SessionState:
    out: SessionState = {}  # type: ignore[typeddict-item]
    if data.get("dialogAction") is not None:
        import capo_lex_runtime_v2.types.dialog_action

        out["dialog_action"] = capo_lex_runtime_v2.types.dialog_action.deserialize_json(
            data["dialogAction"]
        )
    if data.get("intent") is not None:
        import capo_lex_runtime_v2.types.intent

        out["intent"] = capo_lex_runtime_v2.types.intent.deserialize_json(
            data["intent"]
        )
    if data.get("activeContexts") is not None:
        import capo_lex_runtime_v2.types.active_contexts_list

        out["active_contexts"] = (
            capo_lex_runtime_v2.types.active_contexts_list.deserialize_json(
                data["activeContexts"]
            )
        )
    if data.get("sessionAttributes") is not None:
        import capo_lex_runtime_v2.types.string_map

        out["session_attributes"] = (
            capo_lex_runtime_v2.types.string_map.deserialize_json(
                data["sessionAttributes"]
            )
        )
    if data.get("originatingRequestId") is not None:
        out["originating_request_id"] = data["originatingRequestId"]
    if data.get("runtimeHints") is not None:
        import capo_lex_runtime_v2.types.runtime_hints

        out["runtime_hints"] = capo_lex_runtime_v2.types.runtime_hints.deserialize_json(
            data["runtimeHints"]
        )
    return out


def redact_sensitive(value: SessionState) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "active_contexts" in value:
        import capo_lex_runtime_v2.types.active_contexts_list

        out["active_contexts"] = (
            capo_lex_runtime_v2.types.active_contexts_list.redact_sensitive(
                value["active_contexts"]
            )
        )
    return out
