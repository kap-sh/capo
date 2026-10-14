"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidInventoryItemContextException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class InvalidInventoryItemContextException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidInventoryItemContextException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidInventoryItemContextException_:
    out: InvalidInventoryItemContextException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidInventoryItemContextException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidInventoryItemContextException``."""

    code: str | None = "InvalidInventoryItemContextException"

    def __init__(
        self,
        data: InvalidInventoryItemContextException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInventoryItemContextException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidInventoryItemContextException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
