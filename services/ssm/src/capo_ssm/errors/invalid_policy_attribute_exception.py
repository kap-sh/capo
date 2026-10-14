"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidPolicyAttributeException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class InvalidPolicyAttributeException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPolicyAttributeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPolicyAttributeException_:
    out: InvalidPolicyAttributeException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidPolicyAttributeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidPolicyAttributeException``."""

    code: str | None = "InvalidPolicyAttributeException"

    def __init__(
        self,
        data: InvalidPolicyAttributeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPolicyAttributeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidPolicyAttributeException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
