"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#ServiceUnavailable``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_featurestore_runtime.errors import ServiceError

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.message


class ServiceUnavailable_(TypedDict, closed=True):
    message: NotRequired["capo_sagemaker_featurestore_runtime.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceUnavailable_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceUnavailable_:
    out: ServiceUnavailable_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ServiceUnavailable(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#ServiceUnavailable``."""

    code: str | None = "ServiceUnavailable"

    def __init__(
        self,
        data: ServiceUnavailable_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceUnavailable",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceUnavailable":
        return cls(deserialize_json(data), message, response=response)
