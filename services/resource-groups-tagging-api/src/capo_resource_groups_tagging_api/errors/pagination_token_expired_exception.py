"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#PaginationTokenExpiredException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_resource_groups_tagging_api.errors import ServiceError

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.exception_message


class PaginationTokenExpiredException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_resource_groups_tagging_api.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PaginationTokenExpiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PaginationTokenExpiredException_:
    out: PaginationTokenExpiredException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class PaginationTokenExpiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.resourcegroupstaggingapi#PaginationTokenExpiredException``."""

    code: str | None = "PaginationTokenExpiredException"

    def __init__(
        self,
        data: PaginationTokenExpiredException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PaginationTokenExpiredException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PaginationTokenExpiredException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
