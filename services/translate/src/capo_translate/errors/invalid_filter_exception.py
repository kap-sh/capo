"""Generated from Smithy shape ``com.amazonaws.translate#InvalidFilterException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_translate.errors import ServiceError

if TYPE_CHECKING:
    import capo_translate.types.string


class InvalidFilterException_(TypedDict, closed=True):
    message: NotRequired["capo_translate.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidFilterException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidFilterException_:
    out: InvalidFilterException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidFilterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.translate#InvalidFilterException``."""

    code: str | None = "InvalidFilterException"

    def __init__(
        self,
        data: InvalidFilterException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidFilterException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidFilterException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
