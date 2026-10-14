"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#UnauthorizedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_meetings.errors import ServiceError

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.string


class UnauthorizedException_(TypedDict, closed=True):
    code: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    message: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    request_id: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The request id associated with the call responsible for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnauthorizedException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UnauthorizedException_:
    out: UnauthorizedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


class UnauthorizedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkmeetings#UnauthorizedException``."""

    code: str | None = "UnauthorizedException"

    def __init__(
        self,
        data: UnauthorizedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnauthorizedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnauthorizedException":
        return cls(deserialize_json(data), message, response=response)
