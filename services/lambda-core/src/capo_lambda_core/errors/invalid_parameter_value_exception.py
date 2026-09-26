"""Generated from Smithy shape ``com.amazonaws.lambdacore#InvalidParameterValueException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_core.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda_core.types.string


class InvalidParameterValueException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda_core.types.string.String"]
    """<p>The exception type.</p>"""
    message: NotRequired["capo_lambda_core.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterValueException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidParameterValueException_:
    out: InvalidParameterValueException_ = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidParameterValueException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambdacore#InvalidParameterValueException``."""

    code: str | None = "InvalidParameterValueException"

    def __init__(
        self, data: InvalidParameterValueException_, message: str | None = None
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterValueException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "InvalidParameterValueException":
        return cls(deserialize_json(data), message)
