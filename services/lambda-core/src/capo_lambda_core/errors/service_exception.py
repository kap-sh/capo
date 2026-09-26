"""Generated from Smithy shape ``com.amazonaws.lambdacore#ServiceException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_core.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda_core.types.string


class ServiceException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda_core.types.string.String"]
    """<p>The exception type.</p>"""
    message: NotRequired["capo_lambda_core.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceException_:
    out: ServiceException_ = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambdacore#ServiceException``."""

    code: str | None = "ServiceException"

    def __init__(self, data: ServiceException_, message: str | None = None):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict, message: str | None = None) -> "ServiceException":
        return cls(deserialize_json(data), message)
