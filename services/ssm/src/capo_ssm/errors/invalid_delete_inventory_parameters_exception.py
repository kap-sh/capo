"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidDeleteInventoryParametersException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class InvalidDeleteInventoryParametersException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidDeleteInventoryParametersException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidDeleteInventoryParametersException_:
    out: InvalidDeleteInventoryParametersException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidDeleteInventoryParametersException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidDeleteInventoryParametersException``."""

    code: str | None = "InvalidDeleteInventoryParametersException"

    def __init__(
        self,
        data: InvalidDeleteInventoryParametersException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDeleteInventoryParametersException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidDeleteInventoryParametersException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
