"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.chat_output_stream


class ChatOutput(TypedDict, closed=True):
    output_stream: NotRequired[
        "capo_qbusiness.types.chat_output_stream.ChatOutputStream"
    ]
    """<p>The streaming output for the <code>Chat</code> API.</p>"""


def redact_sensitive(value: ChatOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "output_stream" in value:
        out["output_stream"] = "*** Streaming Data Redacted ***"
    return out
