"""Generated from Smithy shape ``com.amazonaws.ses#CustomVerificationEmailInvalidContentException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import ServiceError

if TYPE_CHECKING:
    import capo_ses.types.error_message


class CustomVerificationEmailInvalidContentException_(TypedDict, closed=True):
    message: NotRequired["capo_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomVerificationEmailInvalidContentException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> CustomVerificationEmailInvalidContentException_:
    out: CustomVerificationEmailInvalidContentException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CustomVerificationEmailInvalidContentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#CustomVerificationEmailInvalidContentException``."""

    code: str | None = "CustomVerificationEmailInvalidContentException"

    def __init__(
        self,
        data: CustomVerificationEmailInvalidContentException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomVerificationEmailInvalidContentException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "CustomVerificationEmailInvalidContentException":
        return cls(deserialize_query(el), message, response=response)
