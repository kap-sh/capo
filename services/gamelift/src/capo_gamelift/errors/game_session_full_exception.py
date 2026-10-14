"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionFullException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_gamelift.errors import ServiceError

if TYPE_CHECKING:
    import capo_gamelift.types.non_empty_string


class GameSessionFullException_(TypedDict, closed=True):
    message: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionFullException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GameSessionFullException_:
    out: GameSessionFullException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class GameSessionFullException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.gamelift#GameSessionFullException``."""

    code: str | None = "GameSessionFullException"

    def __init__(
        self,
        data: GameSessionFullException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GameSessionFullException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "GameSessionFullException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
