"""Generated from Smithy shape ``com.amazonaws.ecr#LifecyclePolicyNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecr.types.exception_message


class LifecyclePolicyNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_ecr.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecyclePolicyNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LifecyclePolicyNotFoundException_:
    out: LifecyclePolicyNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class LifecyclePolicyNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#LifecyclePolicyNotFoundException``."""

    code: str | None = "LifecyclePolicyNotFoundException"

    def __init__(
        self,
        data: LifecyclePolicyNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LifecyclePolicyNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "LifecyclePolicyNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
