"""Generated from Smithy shape ``com.amazonaws.appstream#InvalidRoleException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_appstream.errors import ServiceError

if TYPE_CHECKING:
    import capo_appstream.types.error_message


class InvalidRoleException_(TypedDict, closed=True):
    message: NotRequired["capo_appstream.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidRoleException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidRoleException_:
    out: InvalidRoleException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidRoleException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appstream#InvalidRoleException``."""

    code: str | None = "InvalidRoleException"

    def __init__(
        self,
        data: InvalidRoleException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRoleException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidRoleException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
