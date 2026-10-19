"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#NotifyEmailType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.email_notification_body_type
    import capo_cognito_identity_provider.types.email_notification_subject_type


class NotifyEmailType(TypedDict, closed=True):
    subject: "capo_cognito_identity_provider.types.email_notification_subject_type.EmailNotificationSubjectType"
    """<p>The subject of the threat protection email notification.</p>"""
    html_body: NotRequired[
        "capo_cognito_identity_provider.types.email_notification_body_type.EmailNotificationBodyType"
    ]
    """<p>The body of an email notification formatted in HTML. Choose an <code>HtmlBody</code> or a <code>TextBody</code> to send an HTML-formatted or plaintext message, respectively.</p>"""
    text_body: NotRequired[
        "capo_cognito_identity_provider.types.email_notification_body_type.EmailNotificationBodyType"
    ]
    """<p>The body of an email notification formatted in plaintext. Choose an <code>HtmlBody</code> or a <code>TextBody</code> to send an HTML-formatted or plaintext message, respectively.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotifyEmailType) -> dict:
    out: dict = {}
    out["Subject"] = value["subject"]
    if "html_body" in value:
        out["HtmlBody"] = value["html_body"]
    if "text_body" in value:
        out["TextBody"] = value["text_body"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotifyEmailType:
    out: NotifyEmailType = {}  # type: ignore[typeddict-item]
    if data.get("Subject") is not None:
        out["subject"] = data["Subject"]
    else:
        out["subject"] = ""
    if data.get("HtmlBody") is not None:
        out["html_body"] = data["HtmlBody"]
    if data.get("TextBody") is not None:
        out["text_body"] = data["TextBody"]
    return out
