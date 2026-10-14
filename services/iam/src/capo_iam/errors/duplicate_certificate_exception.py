"""Generated from Smithy shape ``com.amazonaws.iam#DuplicateCertificateException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import ServiceError

if TYPE_CHECKING:
    import capo_iam.types.duplicate_certificate_message


class DuplicateCertificateException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_iam.types.duplicate_certificate_message.duplicateCertificateMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DuplicateCertificateException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> DuplicateCertificateException_:
    out: DuplicateCertificateException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DuplicateCertificateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#DuplicateCertificateException``."""

    code: str | None = "DuplicateCertificateException"

    def __init__(
        self,
        data: DuplicateCertificateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateCertificateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "DuplicateCertificateException":
        return cls(deserialize_query(el), message, response=response)
