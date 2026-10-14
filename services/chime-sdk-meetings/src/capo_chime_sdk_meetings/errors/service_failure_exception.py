"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#ServiceFailureException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_meetings.errors import ServiceError

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.string


class ServiceFailureException_(TypedDict, closed=True):
    code: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    message: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    request_id: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The ID of the failed request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceFailureException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ServiceFailureException_:
    out: ServiceFailureException_ = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


class ServiceFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkmeetings#ServiceFailureException``."""

    code: str | None = "ServiceFailureException"

    def __init__(
        self,
        data: ServiceFailureException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceFailureException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceFailureException":
        return cls(deserialize_json(data), message, response=response)
