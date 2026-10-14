"""Generated from Smithy shape ``com.amazonaws.budgets#DuplicateRecordException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_budgets.errors import ServiceError

if TYPE_CHECKING:
    import capo_budgets.types.error_message


class DuplicateRecordException_(TypedDict, closed=True):
    message: NotRequired["capo_budgets.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicateRecordException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicateRecordException_:
    out: DuplicateRecordException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class DuplicateRecordException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.budgets#DuplicateRecordException``."""

    code: str | None = "DuplicateRecordException"

    def __init__(
        self,
        data: DuplicateRecordException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateRecordException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DuplicateRecordException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
