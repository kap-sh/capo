"""Generated from Smithy shape ``com.amazonaws.quicksight#InvalidDataSetParameterValueException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import ServiceError

if TYPE_CHECKING:
    import capo_quicksight.types.string


class InvalidDataSetParameterValueException_(TypedDict, closed=True):
    message: NotRequired["capo_quicksight.types.string.String"]
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidDataSetParameterValueException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> InvalidDataSetParameterValueException_:
    out: InvalidDataSetParameterValueException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


class InvalidDataSetParameterValueException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.quicksight#InvalidDataSetParameterValueException``."""

    code: str | None = "InvalidDataSetParameterValueException"

    def __init__(
        self,
        data: InvalidDataSetParameterValueException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDataSetParameterValueException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidDataSetParameterValueException":
        return cls(deserialize_json(data), message, response=response)
