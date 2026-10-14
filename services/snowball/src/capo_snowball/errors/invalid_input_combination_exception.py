"""Generated from Smithy shape ``com.amazonaws.snowball#InvalidInputCombinationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_snowball.errors import ServiceError

if TYPE_CHECKING:
    import capo_snowball.types.string


class InvalidInputCombinationException_(TypedDict, closed=True):
    message: NotRequired["capo_snowball.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidInputCombinationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidInputCombinationException_:
    out: InvalidInputCombinationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidInputCombinationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.snowball#InvalidInputCombinationException``."""

    code: str | None = "InvalidInputCombinationException"

    def __init__(
        self,
        data: InvalidInputCombinationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInputCombinationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidInputCombinationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
