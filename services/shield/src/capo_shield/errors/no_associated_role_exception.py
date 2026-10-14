"""Generated from Smithy shape ``com.amazonaws.shield#NoAssociatedRoleException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_shield.errors import ServiceError

if TYPE_CHECKING:
    import capo_shield.types.error_message


class NoAssociatedRoleException_(TypedDict, closed=True):
    message: NotRequired["capo_shield.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoAssociatedRoleException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NoAssociatedRoleException_:
    out: NoAssociatedRoleException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class NoAssociatedRoleException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.shield#NoAssociatedRoleException``."""

    code: str | None = "NoAssociatedRoleException"

    def __init__(
        self,
        data: NoAssociatedRoleException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoAssociatedRoleException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NoAssociatedRoleException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
