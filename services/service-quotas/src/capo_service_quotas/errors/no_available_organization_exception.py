"""Generated from Smithy shape ``com.amazonaws.servicequotas#NoAvailableOrganizationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_service_quotas.errors import ServiceError

if TYPE_CHECKING:
    import capo_service_quotas.types.exception_message


class NoAvailableOrganizationException_(TypedDict, closed=True):
    message: NotRequired["capo_service_quotas.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoAvailableOrganizationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NoAvailableOrganizationException_:
    out: NoAvailableOrganizationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class NoAvailableOrganizationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicequotas#NoAvailableOrganizationException``."""

    code: str | None = "NoAvailableOrganizationException"

    def __init__(
        self,
        data: NoAvailableOrganizationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoAvailableOrganizationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NoAvailableOrganizationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
