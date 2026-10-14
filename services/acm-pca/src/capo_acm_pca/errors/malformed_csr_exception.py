"""Generated from Smithy shape ``com.amazonaws.acmpca#MalformedCSRException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import ServiceError

if TYPE_CHECKING:
    import capo_acm_pca.types.string


class MalformedCSRException_(TypedDict, closed=True):
    message: NotRequired["capo_acm_pca.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MalformedCSRException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MalformedCSRException_:
    out: MalformedCSRException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class MalformedCSRException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.acmpca#MalformedCSRException``."""

    code: str | None = "MalformedCSRException"

    def __init__(
        self,
        data: MalformedCSRException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MalformedCSRException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MalformedCSRException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
