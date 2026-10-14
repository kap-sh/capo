"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateMismatchException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import ServiceError

if TYPE_CHECKING:
    import capo_acm_pca.types.string


class CertificateMismatchException_(TypedDict, closed=True):
    message: NotRequired["capo_acm_pca.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateMismatchException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateMismatchException_:
    out: CertificateMismatchException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class CertificateMismatchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.acmpca#CertificateMismatchException``."""

    code: str | None = "CertificateMismatchException"

    def __init__(
        self,
        data: CertificateMismatchException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CertificateMismatchException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CertificateMismatchException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
