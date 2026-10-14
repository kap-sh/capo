"""Generated from Smithy shape ``com.amazonaws.configservice#IdempotentParameterMismatch``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_config_service.types.string


class IdempotentParameterMismatch_(TypedDict, closed=True):
    message: NotRequired["capo_config_service.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdempotentParameterMismatch_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IdempotentParameterMismatch_:
    out: IdempotentParameterMismatch_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class IdempotentParameterMismatch(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#IdempotentParameterMismatch``."""

    code: str | None = "IdempotentParameterMismatch"

    def __init__(
        self,
        data: IdempotentParameterMismatch_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IdempotentParameterMismatch",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "IdempotentParameterMismatch":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
