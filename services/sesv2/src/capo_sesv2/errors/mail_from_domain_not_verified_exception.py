"""Generated from Smithy shape ``com.amazonaws.sesv2#MailFromDomainNotVerifiedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import ServiceError

if TYPE_CHECKING:
    import capo_sesv2.types.error_message


class MailFromDomainNotVerifiedException_(TypedDict, closed=True):
    message: NotRequired["capo_sesv2.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: MailFromDomainNotVerifiedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MailFromDomainNotVerifiedException_:
    out: MailFromDomainNotVerifiedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class MailFromDomainNotVerifiedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sesv2#MailFromDomainNotVerifiedException``."""

    code: str | None = "MailFromDomainNotVerifiedException"

    def __init__(
        self,
        data: MailFromDomainNotVerifiedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MailFromDomainNotVerifiedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MailFromDomainNotVerifiedException":
        return cls(deserialize_json(data), message, response=response)
