"""Generated from Smithy shape ``com.amazonaws.lambda#S3FilesMountConnectivityException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class S3FilesMountConnectivityException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.string.String"]
    """<p>The exception type.</p>"""
    message: NotRequired["capo_lambda.types.string.String"]
    """<p>The exception message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3FilesMountConnectivityException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> S3FilesMountConnectivityException_:
    out: S3FilesMountConnectivityException_ = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class S3FilesMountConnectivityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#S3FilesMountConnectivityException``."""

    code: str | None = "S3FilesMountConnectivityException"

    def __init__(
        self,
        data: S3FilesMountConnectivityException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="S3FilesMountConnectivityException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "S3FilesMountConnectivityException":
        return cls(deserialize_json(data), message, response=response)
