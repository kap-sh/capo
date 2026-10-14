"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ConstraintViolationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_resource_groups_tagging_api.errors import ServiceError

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.exception_message


class ConstraintViolationException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_resource_groups_tagging_api.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConstraintViolationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConstraintViolationException_:
    out: ConstraintViolationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ConstraintViolationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ConstraintViolationException``."""

    code: str | None = "ConstraintViolationException"

    def __init__(
        self,
        data: ConstraintViolationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConstraintViolationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConstraintViolationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
