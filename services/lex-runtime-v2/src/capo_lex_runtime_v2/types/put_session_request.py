"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#PutSessionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.bot_alias_identifier
    import capo_lex_runtime_v2.types.bot_identifier
    import capo_lex_runtime_v2.types.locale_id
    import capo_lex_runtime_v2.types.messages
    import capo_lex_runtime_v2.types.non_empty_string
    import capo_lex_runtime_v2.types.session_id
    import capo_lex_runtime_v2.types.session_state
    import capo_lex_runtime_v2.types.string_map


class PutSessionRequest(TypedDict, closed=True):
    bot_id: "capo_lex_runtime_v2.types.bot_identifier.BotIdentifier"
    """<p>The identifier of the bot that receives the session data.</p>"""
    bot_alias_id: "capo_lex_runtime_v2.types.bot_alias_identifier.BotAliasIdentifier"
    """<p>The alias identifier of the bot that receives the session data.</p>"""
    locale_id: "capo_lex_runtime_v2.types.locale_id.LocaleId"
    """<p>The locale where the session is in use.</p>"""
    session_id: "capo_lex_runtime_v2.types.session_id.SessionId"
    """<p>The identifier of the session that receives the session data.</p>"""
    messages: NotRequired["capo_lex_runtime_v2.types.messages.Messages"]
    """<p>A list of messages to send to the user. Messages are sent in the order that they are defined in the list.</p>"""
    session_state: "capo_lex_runtime_v2.types.session_state.SessionState"
    """<p>Sets the state of the session with the user. You can use this to set the current intent, attributes, context, and dialog action. Use the dialog action to determine the next step that Amazon Lex V2 should use in the conversation with the user.</p>"""
    request_attributes: NotRequired["capo_lex_runtime_v2.types.string_map.StringMap"]
    """<p>Request-specific information passed between Amazon Lex V2 and the client application.</p> <p>The namespace <code>x-amz-lex:</code> is reserved for special attributes. Don't create any request attributes with the prefix <code>x-amz-lex:</code>.</p>"""
    response_content_type: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The message that Amazon Lex V2 returns in the response can be either text or speech depending on the value of this parameter. </p> <ul> <li> <p>If the value is <code>text/plain; charset=utf-8</code>, Amazon Lex V2 returns text in the response.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSessionRequest) -> dict:
    out: dict = {}
    if "messages" in value:
        import capo_lex_runtime_v2.types.messages

        out["messages"] = capo_lex_runtime_v2.types.messages.serialize_json(
            value["messages"]
        )
    import capo_lex_runtime_v2.types.session_state

    out["sessionState"] = capo_lex_runtime_v2.types.session_state.serialize_json(
        value["session_state"]
    )
    if "request_attributes" in value:
        import capo_lex_runtime_v2.types.string_map

        out["requestAttributes"] = capo_lex_runtime_v2.types.string_map.serialize_json(
            value["request_attributes"]
        )
    return out


def deserialize_json(data: dict) -> PutSessionRequest:
    out: PutSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_lex_runtime_v2.types.messages

        out["messages"] = capo_lex_runtime_v2.types.messages.deserialize_json(
            data["messages"]
        )
    if data.get("sessionState") is not None:
        import capo_lex_runtime_v2.types.session_state

        out["session_state"] = capo_lex_runtime_v2.types.session_state.deserialize_json(
            data["sessionState"]
        )
    else:
        raise DeserializationError("PutSessionRequest.session_state required")
    if data.get("requestAttributes") is not None:
        import capo_lex_runtime_v2.types.string_map

        out["request_attributes"] = (
            capo_lex_runtime_v2.types.string_map.deserialize_json(
                data["requestAttributes"]
            )
        )
    return out


def redact_sensitive(value: PutSessionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "messages" in value:
        import capo_lex_runtime_v2.types.messages

        out["messages"] = capo_lex_runtime_v2.types.messages.redact_sensitive(
            value["messages"]
        )
    if "session_state" in value:
        import capo_lex_runtime_v2.types.session_state

        out["session_state"] = capo_lex_runtime_v2.types.session_state.redact_sensitive(
            value["session_state"]
        )
    return out
