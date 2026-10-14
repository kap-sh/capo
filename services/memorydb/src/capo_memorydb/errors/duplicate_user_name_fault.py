"""Generated from Smithy shape ``com.amazonaws.memorydb#DuplicateUserNameFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import capo_memorydb.types.exception_message


class DuplicateUserNameFault_(TypedDict, closed=True):
    message: NotRequired["capo_memorydb.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicateUserNameFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicateUserNameFault_:
    out: DuplicateUserNameFault_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class DuplicateUserNameFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#DuplicateUserNameFault``."""

    code: str | None = "DuplicateUserNameFault"

    def __init__(
        self,
        data: DuplicateUserNameFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateUserNameFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DuplicateUserNameFault":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
