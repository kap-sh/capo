"""Generated from Smithy shape ``com.amazonaws.lambda#EC2UnexpectedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class EC2UnexpectedException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.string.String"]
    message: NotRequired["capo_lambda.types.string.String"]
    ec2_error_code: NotRequired["capo_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: EC2UnexpectedException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    if "ec2_error_code" in value:
        out["EC2ErrorCode"] = value["ec2_error_code"]
    return out


def deserialize_json(data: dict) -> EC2UnexpectedException_:
    out: EC2UnexpectedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("EC2ErrorCode") is not None:
        out["ec2_error_code"] = data["EC2ErrorCode"]
    return out


class EC2UnexpectedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#EC2UnexpectedException``."""

    code: str | None = "EC2UnexpectedException"

    def __init__(
        self,
        data: EC2UnexpectedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="EC2UnexpectedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "EC2UnexpectedException":
        return cls(deserialize_json(data), message, response=response)
