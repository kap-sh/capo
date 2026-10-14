"""Generated from Smithy shape ``com.amazonaws.servicequotas#InvalidResourceStateException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_service_quotas.errors import ServiceError

if TYPE_CHECKING:
    import capo_service_quotas.types.exception_message


class InvalidResourceStateException_(TypedDict, closed=True):
    message: NotRequired["capo_service_quotas.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidResourceStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidResourceStateException_:
    out: InvalidResourceStateException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidResourceStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicequotas#InvalidResourceStateException``."""

    code: str | None = "InvalidResourceStateException"

    def __init__(
        self,
        data: InvalidResourceStateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourceStateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidResourceStateException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
