"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#StartConversationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.start_conversation_response_event_stream


class StartConversationResponse(TypedDict, closed=True):
    response_event_stream: NotRequired[
        "capo_lex_runtime_v2.types.start_conversation_response_event_stream.StartConversationResponseEventStream"
    ]
    """<p>Represents the stream of events from Amazon Lex V2 to your application. The events are encoded as HTTP/2 data frames.</p>"""


def redact_sensitive(value: StartConversationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "response_event_stream" in value:
        out["response_event_stream"] = "*** Streaming Data Redacted ***"
    return out
