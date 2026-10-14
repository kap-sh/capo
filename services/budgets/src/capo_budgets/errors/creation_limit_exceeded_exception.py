"""Generated from Smithy shape ``com.amazonaws.budgets#CreationLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_budgets.errors import ServiceError

if TYPE_CHECKING:
    import capo_budgets.types.error_message


class CreationLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_budgets.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreationLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreationLimitExceededException_:
    out: CreationLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class CreationLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.budgets#CreationLimitExceededException``."""

    code: str | None = "CreationLimitExceededException"

    def __init__(
        self,
        data: CreationLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CreationLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CreationLimitExceededException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
