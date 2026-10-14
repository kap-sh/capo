"""Generated from Smithy shape ``com.amazonaws.ses#FromEmailAddressNotVerifiedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import ServiceError

if TYPE_CHECKING:
    import capo_ses.types.error_message
    import capo_ses.types.from_address


class FromEmailAddressNotVerifiedException_(TypedDict, closed=True):
    from_email_address: NotRequired["capo_ses.types.from_address.FromAddress"]
    """<p>Indicates that the from email address associated with the custom verification email template is not verified.</p>"""
    message: NotRequired["capo_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: FromEmailAddressNotVerifiedException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "from_email_address" in value:
        pairs.append(
            (f"{key_prefix}FromEmailAddress", str(value["from_email_address"]))
        )
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> FromEmailAddressNotVerifiedException_:
    out: FromEmailAddressNotVerifiedException_ = {}  # type: ignore[typeddict-item]
    child_from_email_address = el.find("FromEmailAddress")
    if child_from_email_address is not None:
        out["from_email_address"] = str(child_from_email_address.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class FromEmailAddressNotVerifiedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#FromEmailAddressNotVerifiedException``."""

    code: str | None = "FromEmailAddressNotVerifiedException"

    def __init__(
        self,
        data: FromEmailAddressNotVerifiedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FromEmailAddressNotVerifiedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "FromEmailAddressNotVerifiedException":
        return cls(deserialize_query(el), message, response=response)
