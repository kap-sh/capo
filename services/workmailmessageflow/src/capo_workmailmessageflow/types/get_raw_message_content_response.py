"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#GetRawMessageContentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmailmessageflow.types.message_content_blob


class GetRawMessageContentResponse(TypedDict, closed=True):
    message_content: (
        "capo_workmailmessageflow.types.message_content_blob.messageContentBlob"
    )
    """<p>The raw content of the email message, in MIME format.</p>"""


def redact_sensitive(value: GetRawMessageContentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message_content" in value:
        out["message_content"] = "*** Streaming Data Redacted ***"
    return out
