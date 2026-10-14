"""Generated from Smithy shape ``com.amazonaws.servicequotas#NoSuchResourceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_service_quotas.errors import ServiceError

if TYPE_CHECKING:
    import capo_service_quotas.types.exception_message


class NoSuchResourceException_(TypedDict, closed=True):
    message: NotRequired["capo_service_quotas.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoSuchResourceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NoSuchResourceException_:
    out: NoSuchResourceException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class NoSuchResourceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicequotas#NoSuchResourceException``."""

    code: str | None = "NoSuchResourceException"

    def __init__(
        self,
        data: NoSuchResourceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchResourceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NoSuchResourceException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
