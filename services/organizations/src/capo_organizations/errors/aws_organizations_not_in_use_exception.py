"""Generated from Smithy shape ``com.amazonaws.organizations#AWSOrganizationsNotInUseException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import ServiceError

if TYPE_CHECKING:
    import capo_organizations.types.exception_message


class AWSOrganizationsNotInUseException_(TypedDict, closed=True):
    message: NotRequired["capo_organizations.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AWSOrganizationsNotInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AWSOrganizationsNotInUseException_:
    out: AWSOrganizationsNotInUseException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class AWSOrganizationsNotInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#AWSOrganizationsNotInUseException``."""

    code: str | None = "AWSOrganizationsNotInUseException"

    def __init__(
        self,
        data: AWSOrganizationsNotInUseException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AWSOrganizationsNotInUseException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AWSOrganizationsNotInUseException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
