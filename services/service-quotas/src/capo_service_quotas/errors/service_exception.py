"""Generated from Smithy shape ``com.amazonaws.servicequotas#ServiceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_service_quotas.errors import ServiceError

if TYPE_CHECKING:
    import capo_service_quotas.types.exception_message


class ServiceException_(TypedDict, closed=True):
    message: NotRequired["capo_service_quotas.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceException_:
    out: ServiceException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicequotas#ServiceException``."""

    code: str | None = "ServiceException"

    def __init__(
        self,
        data: ServiceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
