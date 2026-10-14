"""Generated from Smithy shape ``com.amazonaws.ses#InvalidTemplateException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import ServiceError

if TYPE_CHECKING:
    import capo_ses.types.error_message
    import capo_ses.types.template_name


class InvalidTemplateException_(TypedDict, closed=True):
    template_name: NotRequired["capo_ses.types.template_name.TemplateName"]
    message: NotRequired["capo_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidTemplateException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "template_name" in value:
        pairs.append((f"{key_prefix}TemplateName", str(value["template_name"])))
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidTemplateException_:
    out: InvalidTemplateException_ = {}  # type: ignore[typeddict-item]
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidTemplateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#InvalidTemplateException``."""

    code: str | None = "InvalidTemplateException"

    def __init__(
        self,
        data: InvalidTemplateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidTemplateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidTemplateException":
        return cls(deserialize_query(el), message, response=response)
