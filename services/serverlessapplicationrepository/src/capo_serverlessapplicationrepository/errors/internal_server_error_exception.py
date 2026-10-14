"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#InternalServerErrorException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_serverlessapplicationrepository.errors import ServiceError

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__string


class InternalServerErrorException_(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>500</p>"""
    message: NotRequired["capo_serverlessapplicationrepository.types.__string.__string"]
    """<p>The AWS Serverless Application Repository service encountered an internal error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerErrorException_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerErrorException_:
    out: InternalServerErrorException_ = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InternalServerErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.serverlessapplicationrepository#InternalServerErrorException``."""

    code: str | None = "InternalServerErrorException"

    def __init__(
        self,
        data: InternalServerErrorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerErrorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerErrorException":
        return cls(deserialize_json(data), message, response=response)
