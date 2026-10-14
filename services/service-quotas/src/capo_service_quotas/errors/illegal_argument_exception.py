"""Generated from Smithy shape ``com.amazonaws.servicequotas#IllegalArgumentException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_service_quotas.errors import ServiceError

if TYPE_CHECKING:
    import capo_service_quotas.types.exception_message


class IllegalArgumentException_(TypedDict, closed=True):
    message: NotRequired["capo_service_quotas.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IllegalArgumentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IllegalArgumentException_:
    out: IllegalArgumentException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class IllegalArgumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicequotas#IllegalArgumentException``."""

    code: str | None = "IllegalArgumentException"

    def __init__(
        self,
        data: IllegalArgumentException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IllegalArgumentException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "IllegalArgumentException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
