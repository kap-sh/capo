"""Generated from Smithy shape ``com.amazonaws.codebuild#AccountSuspendedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codebuild.errors import ServiceError

if TYPE_CHECKING:
    import capo_codebuild.types.string


class AccountSuspendedException_(TypedDict, closed=True):
    message: NotRequired["capo_codebuild.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountSuspendedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountSuspendedException_:
    out: AccountSuspendedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class AccountSuspendedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codebuild#AccountSuspendedException``."""

    code: str | None = "AccountSuspendedException"

    def __init__(
        self,
        data: AccountSuspendedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccountSuspendedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AccountSuspendedException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
