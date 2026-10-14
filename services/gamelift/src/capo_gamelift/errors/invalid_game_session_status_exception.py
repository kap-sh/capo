"""Generated from Smithy shape ``com.amazonaws.gamelift#InvalidGameSessionStatusException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_gamelift.errors import ServiceError

if TYPE_CHECKING:
    import capo_gamelift.types.non_empty_string


class InvalidGameSessionStatusException_(TypedDict, closed=True):
    message: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidGameSessionStatusException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidGameSessionStatusException_:
    out: InvalidGameSessionStatusException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidGameSessionStatusException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.gamelift#InvalidGameSessionStatusException``."""

    code: str | None = "InvalidGameSessionStatusException"

    def __init__(
        self,
        data: InvalidGameSessionStatusException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidGameSessionStatusException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidGameSessionStatusException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
