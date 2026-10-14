"""Generated from Smithy shape ``com.amazonaws.migrationhub#UnauthorizedOperation``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_migration_hub.errors import ServiceError

if TYPE_CHECKING:
    import capo_migration_hub.types.error_message


class UnauthorizedOperation_(TypedDict, closed=True):
    message: NotRequired["capo_migration_hub.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnauthorizedOperation_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnauthorizedOperation_:
    out: UnauthorizedOperation_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class UnauthorizedOperation(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhub#UnauthorizedOperation``."""

    code: str | None = "UnauthorizedOperation"

    def __init__(
        self,
        data: UnauthorizedOperation_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnauthorizedOperation",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnauthorizedOperation":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
