"""Generated from Smithy shape ``com.amazonaws.iam#CredentialReportNotPresentException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import ServiceError

if TYPE_CHECKING:
    import capo_iam.types.credential_report_not_present_exception_message


class CredentialReportNotPresentException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_iam.types.credential_report_not_present_exception_message.credentialReportNotPresentExceptionMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CredentialReportNotPresentException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> CredentialReportNotPresentException_:
    out: CredentialReportNotPresentException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CredentialReportNotPresentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#CredentialReportNotPresentException``."""

    code: str | None = "CredentialReportNotPresentException"

    def __init__(
        self,
        data: CredentialReportNotPresentException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CredentialReportNotPresentException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "CredentialReportNotPresentException":
        return cls(deserialize_query(el), message, response=response)
