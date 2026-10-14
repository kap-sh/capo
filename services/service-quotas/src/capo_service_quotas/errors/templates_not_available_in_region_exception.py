"""Generated from Smithy shape ``com.amazonaws.servicequotas#TemplatesNotAvailableInRegionException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_service_quotas.errors import ServiceError

if TYPE_CHECKING:
    import capo_service_quotas.types.exception_message


class TemplatesNotAvailableInRegionException_(TypedDict, closed=True):
    message: NotRequired["capo_service_quotas.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TemplatesNotAvailableInRegionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TemplatesNotAvailableInRegionException_:
    out: TemplatesNotAvailableInRegionException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class TemplatesNotAvailableInRegionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicequotas#TemplatesNotAvailableInRegionException``."""

    code: str | None = "TemplatesNotAvailableInRegionException"

    def __init__(
        self,
        data: TemplatesNotAvailableInRegionException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TemplatesNotAvailableInRegionException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TemplatesNotAvailableInRegionException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
