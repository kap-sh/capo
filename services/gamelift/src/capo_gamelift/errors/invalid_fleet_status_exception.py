"""Generated from Smithy shape ``com.amazonaws.gamelift#InvalidFleetStatusException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_gamelift.errors import ServiceError

if TYPE_CHECKING:
    import capo_gamelift.types.non_empty_string


class InvalidFleetStatusException_(TypedDict, closed=True):
    message: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidFleetStatusException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidFleetStatusException_:
    out: InvalidFleetStatusException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidFleetStatusException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.gamelift#InvalidFleetStatusException``."""

    code: str | None = "InvalidFleetStatusException"

    def __init__(
        self,
        data: InvalidFleetStatusException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidFleetStatusException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidFleetStatusException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
