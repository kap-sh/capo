"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#DryRunOperation``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_migrationhub_config.errors import ServiceError

if TYPE_CHECKING:
    import capo_migrationhub_config.types.error_message


class DryRunOperation_(TypedDict, closed=True):
    message: NotRequired["capo_migrationhub_config.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DryRunOperation_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DryRunOperation_:
    out: DryRunOperation_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class DryRunOperation(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhubconfig#DryRunOperation``."""

    code: str | None = "DryRunOperation"

    def __init__(
        self,
        data: DryRunOperation_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DryRunOperation",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DryRunOperation":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
