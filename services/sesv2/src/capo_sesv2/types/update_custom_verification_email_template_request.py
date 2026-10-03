"""Generated from Smithy shape ``com.amazonaws.sesv2#UpdateCustomVerificationEmailTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.email_address
    import capo_sesv2.types.email_template_name
    import capo_sesv2.types.email_template_subject
    import capo_sesv2.types.failure_redirection_url
    import capo_sesv2.types.success_redirection_url
    import capo_sesv2.types.template_content


class UpdateCustomVerificationEmailTemplateRequest(TypedDict, closed=True):
    template_name: "capo_sesv2.types.email_template_name.EmailTemplateName"
    """<p>The name of the custom verification email template that you want to update.</p>"""
    from_email_address: "capo_sesv2.types.email_address.EmailAddress"
    """<p>The email address that the custom verification email is sent from.</p>"""
    template_subject: "capo_sesv2.types.email_template_subject.EmailTemplateSubject"
    """<p>The subject line of the custom verification email.</p>"""
    template_content: "capo_sesv2.types.template_content.TemplateContent"
    """<p>The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom-faq">Custom verification email frequently asked questions</a> in the <i>Amazon SES Developer Guide</i>.</p>"""
    success_redirection_url: (
        "capo_sesv2.types.success_redirection_url.SuccessRedirectionURL"
    )
    """<p>The URL that the recipient of the verification email is sent to if his or her address is successfully verified.</p>"""
    failure_redirection_url: (
        "capo_sesv2.types.failure_redirection_url.FailureRedirectionURL"
    )
    """<p>The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomVerificationEmailTemplateRequest) -> dict:
    out: dict = {}
    out["FromEmailAddress"] = value["from_email_address"]
    out["TemplateSubject"] = value["template_subject"]
    out["TemplateContent"] = value["template_content"]
    out["SuccessRedirectionURL"] = value["success_redirection_url"]
    out["FailureRedirectionURL"] = value["failure_redirection_url"]
    return out


def deserialize_json(data: dict) -> UpdateCustomVerificationEmailTemplateRequest:
    out: UpdateCustomVerificationEmailTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("FromEmailAddress") is not None:
        out["from_email_address"] = data["FromEmailAddress"]
    else:
        raise DeserializationError(
            "UpdateCustomVerificationEmailTemplateRequest.from_email_address required"
        )
    if data.get("TemplateSubject") is not None:
        out["template_subject"] = data["TemplateSubject"]
    else:
        raise DeserializationError(
            "UpdateCustomVerificationEmailTemplateRequest.template_subject required"
        )
    if data.get("TemplateContent") is not None:
        out["template_content"] = data["TemplateContent"]
    else:
        raise DeserializationError(
            "UpdateCustomVerificationEmailTemplateRequest.template_content required"
        )
    if data.get("SuccessRedirectionURL") is not None:
        out["success_redirection_url"] = data["SuccessRedirectionURL"]
    else:
        raise DeserializationError(
            "UpdateCustomVerificationEmailTemplateRequest.success_redirection_url required"
        )
    if data.get("FailureRedirectionURL") is not None:
        out["failure_redirection_url"] = data["FailureRedirectionURL"]
    else:
        raise DeserializationError(
            "UpdateCustomVerificationEmailTemplateRequest.failure_redirection_url required"
        )
    return out
