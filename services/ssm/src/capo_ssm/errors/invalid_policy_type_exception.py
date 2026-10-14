"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidPolicyTypeException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class InvalidPolicyTypeException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPolicyTypeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPolicyTypeException_:
    out: InvalidPolicyTypeException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidPolicyTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidPolicyTypeException``."""

    code: str | None = "InvalidPolicyTypeException"

    def __init__(
        self,
        data: InvalidPolicyTypeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPolicyTypeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidPolicyTypeException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
