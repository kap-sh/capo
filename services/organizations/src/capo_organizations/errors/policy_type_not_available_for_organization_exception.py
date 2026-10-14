"""Generated from Smithy shape ``com.amazonaws.organizations#PolicyTypeNotAvailableForOrganizationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import ServiceError

if TYPE_CHECKING:
    import capo_organizations.types.exception_message


class PolicyTypeNotAvailableForOrganizationException_(TypedDict, closed=True):
    message: NotRequired["capo_organizations.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: PolicyTypeNotAvailableForOrganizationException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> PolicyTypeNotAvailableForOrganizationException_:
    out: PolicyTypeNotAvailableForOrganizationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class PolicyTypeNotAvailableForOrganizationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#PolicyTypeNotAvailableForOrganizationException``."""

    code: str | None = "PolicyTypeNotAvailableForOrganizationException"

    def __init__(
        self,
        data: PolicyTypeNotAvailableForOrganizationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyTypeNotAvailableForOrganizationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PolicyTypeNotAvailableForOrganizationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
