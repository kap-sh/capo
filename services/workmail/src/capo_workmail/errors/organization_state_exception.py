"""Generated from Smithy shape ``com.amazonaws.workmail#OrganizationStateException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import ServiceError

if TYPE_CHECKING:
    import capo_workmail.types.string


class OrganizationStateException_(TypedDict, closed=True):
    message: NotRequired["capo_workmail.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationStateException_:
    out: OrganizationStateException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class OrganizationStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workmail#OrganizationStateException``."""

    code: str | None = "OrganizationStateException"

    def __init__(
        self,
        data: OrganizationStateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OrganizationStateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "OrganizationStateException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
