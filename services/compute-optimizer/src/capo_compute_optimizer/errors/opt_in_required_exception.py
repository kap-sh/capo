"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#OptInRequiredException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_compute_optimizer.errors import ServiceError

if TYPE_CHECKING:
    import capo_compute_optimizer.types.error_message


class OptInRequiredException_(TypedDict, closed=True):
    message: NotRequired["capo_compute_optimizer.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OptInRequiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OptInRequiredException_:
    out: OptInRequiredException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class OptInRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.computeoptimizer#OptInRequiredException``."""

    code: str | None = "OptInRequiredException"

    def __init__(
        self,
        data: OptInRequiredException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OptInRequiredException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "OptInRequiredException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
