"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateMessageTemplateAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.attachment_file_name
    import capo_qconnect.types.client_token
    import capo_qconnect.types.content_disposition
    import capo_qconnect.types.non_empty_unlimited_string
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier


class CreateMessageTemplateAttachmentRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>"""
    content_disposition: "capo_qconnect.types.content_disposition.ContentDisposition"
    """<p>The presentation information for the attachment file.</p>"""
    name: "capo_qconnect.types.attachment_file_name.AttachmentFileName"
    """<p>The name of the attachment file being uploaded. The name should include the file extension.</p>"""
    body: "capo_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    """<p>The body of the attachment file being uploaded. It should be encoded using base64 encoding.</p>"""
    client_token: NotRequired["capo_qconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMessageTemplateAttachmentRequest) -> dict:
    out: dict = {}
    out["contentDisposition"] = value["content_disposition"]
    out["name"] = value["name"]
    out["body"] = value["body"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateMessageTemplateAttachmentRequest:
    out: CreateMessageTemplateAttachmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("contentDisposition") is not None:
        out["content_disposition"] = data["contentDisposition"]
    else:
        raise DeserializationError(
            "CreateMessageTemplateAttachmentRequest.content_disposition required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateMessageTemplateAttachmentRequest.name required"
        )
    if data.get("body") is not None:
        out["body"] = data["body"]
    else:
        raise DeserializationError(
            "CreateMessageTemplateAttachmentRequest.body required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
