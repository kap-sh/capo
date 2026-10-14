"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#PublicPolicyException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography.errors import ServiceError


class PublicPolicyException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PublicPolicyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PublicPolicyException_:
    out: PublicPolicyException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class PublicPolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.paymentcryptography#PublicPolicyException``."""

    code: str | None = "PublicPolicyException"

    def __init__(
        self,
        data: PublicPolicyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PublicPolicyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PublicPolicyException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
