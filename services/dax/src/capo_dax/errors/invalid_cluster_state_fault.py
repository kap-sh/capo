"""Generated from Smithy shape ``com.amazonaws.dax#InvalidClusterStateFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_dax.errors import ServiceError

if TYPE_CHECKING:
    import capo_dax.types.exception_message


class InvalidClusterStateFault_(TypedDict, closed=True):
    message: NotRequired["capo_dax.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidClusterStateFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidClusterStateFault_:
    out: InvalidClusterStateFault_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidClusterStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dax#InvalidClusterStateFault``."""

    code: str | None = "InvalidClusterStateFault"

    def __init__(
        self,
        data: InvalidClusterStateFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidClusterStateFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidClusterStateFault":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
