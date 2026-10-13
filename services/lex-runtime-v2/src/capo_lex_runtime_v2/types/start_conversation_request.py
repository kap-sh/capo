"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#StartConversationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.bot_alias_identifier
    import capo_lex_runtime_v2.types.bot_identifier
    import capo_lex_runtime_v2.types.conversation_mode
    import capo_lex_runtime_v2.types.locale_id
    import capo_lex_runtime_v2.types.session_id
    import capo_lex_runtime_v2.types.start_conversation_request_event_stream


class StartConversationRequest(TypedDict, closed=True):
    bot_id: "capo_lex_runtime_v2.types.bot_identifier.BotIdentifier"
    """<p>The identifier of the bot to process the request.</p>"""
    bot_alias_id: "capo_lex_runtime_v2.types.bot_alias_identifier.BotAliasIdentifier"
    """<p>The alias identifier in use for the bot that processes the request.</p>"""
    locale_id: "capo_lex_runtime_v2.types.locale_id.LocaleId"
    """<p>The locale where the session is in use.</p>"""
    session_id: "capo_lex_runtime_v2.types.session_id.SessionId"
    """<p>The identifier of the user session that is having the conversation.</p>"""
    conversation_mode: NotRequired[
        "capo_lex_runtime_v2.types.conversation_mode.ConversationMode"
    ]
    """<p>The conversation type that you are using the Amazon Lex V2. If the conversation mode is <code>AUDIO</code> you can send both audio and DTMF information. If the mode is <code>TEXT</code> you can only send text.</p>"""
    request_event_stream: "capo_lex_runtime_v2.types.start_conversation_request_event_stream.StartConversationRequestEventStream"
    """<p>Represents the stream of events to Amazon Lex V2 from your application. The events are encoded as HTTP/2 data frames.</p>"""


def redact_sensitive(value: StartConversationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "request_event_stream" in value:
        out["request_event_stream"] = "*** Streaming Data Redacted ***"
    return out
