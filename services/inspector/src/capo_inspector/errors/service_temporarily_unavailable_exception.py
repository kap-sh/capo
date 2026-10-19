"""Generated from Smithy shape ``com.amazonaws.inspector#ServiceTemporarilyUnavailableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_inspector.errors import ServiceError

if TYPE_CHECKING:
    import capo_inspector.types.bool
    import capo_inspector.types.error_message


class ServiceTemporarilyUnavailableException_(TypedDict, closed=True):
    message: "capo_inspector.types.error_message.ErrorMessage"
    """<p>Details of the exception error.</p>"""
    can_retry: "capo_inspector.types.bool.Bool"
    """<p>You can wait and then retry your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceTemporarilyUnavailableException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["canRetry"] = value["can_retry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceTemporarilyUnavailableException_:
    out: ServiceTemporarilyUnavailableException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("canRetry") is not None:
        out["can_retry"] = data["canRetry"]
    else:
        out["can_retry"] = False
    return out


class ServiceTemporarilyUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.inspector#ServiceTemporarilyUnavailableException``."""

    code: str | None = "ServiceTemporarilyUnavailableException"

    def __init__(
        self,
        data: ServiceTemporarilyUnavailableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceTemporarilyUnavailableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceTemporarilyUnavailableException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
