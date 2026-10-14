"""Generated from Smithy shape ``com.amazonaws.ses#CustomVerificationEmailTemplateAlreadyExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import ServiceError

if TYPE_CHECKING:
    import capo_ses.types.error_message
    import capo_ses.types.template_name


class CustomVerificationEmailTemplateAlreadyExistsException_(TypedDict, closed=True):
    custom_verification_email_template_name: NotRequired[
        "capo_ses.types.template_name.TemplateName"
    ]
    """<p>Indicates that the provided custom verification email template with the specified template name already exists.</p>"""
    message: NotRequired["capo_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomVerificationEmailTemplateAlreadyExistsException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "custom_verification_email_template_name" in value:
        pairs.append(
            (
                f"{key_prefix}CustomVerificationEmailTemplateName",
                str(value["custom_verification_email_template_name"]),
            )
        )
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(
    el: Element,
) -> CustomVerificationEmailTemplateAlreadyExistsException_:
    out: CustomVerificationEmailTemplateAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    child_custom_verification_email_template_name = el.find(
        "CustomVerificationEmailTemplateName"
    )
    if child_custom_verification_email_template_name is not None:
        out["custom_verification_email_template_name"] = str(
            child_custom_verification_email_template_name.text or ""
        )
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CustomVerificationEmailTemplateAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#CustomVerificationEmailTemplateAlreadyExistsException``."""

    code: str | None = "CustomVerificationEmailTemplateAlreadyExistsException"

    def __init__(
        self,
        data: CustomVerificationEmailTemplateAlreadyExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomVerificationEmailTemplateAlreadyExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "CustomVerificationEmailTemplateAlreadyExistsException":
        return cls(deserialize_query(el), message, response=response)
