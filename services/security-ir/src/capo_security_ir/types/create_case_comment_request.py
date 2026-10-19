"""Generated from Smithy shape ``com.amazonaws.securityir#CreateCaseCommentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.case_id
    import capo_security_ir.types.comment_body


class CreateCaseCommentRequest(TypedDict, closed=True):
    case_id: "capo_security_ir.types.case_id.CaseId"
    """<p>Required element used in combination with CreateCaseComment to specify a case ID.</p>"""
    client_token: NotRequired["str"]
    """<note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>"""
    body: "capo_security_ir.types.comment_body.CommentBody"
    """<p>Required element used in combination with CreateCaseComment to add content for the new comment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseCommentRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["body"] = value["body"]
    return out


def deserialize_json(data: dict) -> CreateCaseCommentRequest:
    out: CreateCaseCommentRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("body") is not None:
        out["body"] = data["body"]
    else:
        out["body"] = ""
    return out


def redact_sensitive(value: CreateCaseCommentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out
