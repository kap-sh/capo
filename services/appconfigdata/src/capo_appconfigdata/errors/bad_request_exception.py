"""Generated from Smithy shape ``com.amazonaws.appconfigdata#BadRequestException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_appconfigdata.errors import ServiceError

if TYPE_CHECKING:
    import capo_appconfigdata.types.bad_request_details
    import capo_appconfigdata.types.bad_request_reason
    import capo_appconfigdata.types.string


class BadRequestException_(TypedDict, closed=True):
    message: NotRequired["capo_appconfigdata.types.string.String"]
    reason: NotRequired["capo_appconfigdata.types.bad_request_reason.BadRequestReason"]
    """<p>Code indicating the reason the request was invalid.</p>"""
    details: NotRequired[
        "capo_appconfigdata.types.bad_request_details.BadRequestDetails"
    ]
    """<p>Details describing why the request was invalid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "details" in value:
        import capo_appconfigdata.types.bad_request_details

        out["Details"] = capo_appconfigdata.types.bad_request_details.serialize_json(
            value["details"]
        )
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    if data.get("Details") is not None:
        import capo_appconfigdata.types.bad_request_details

        out["details"] = capo_appconfigdata.types.bad_request_details.deserialize_json(
            data["Details"]
        )
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appconfigdata#BadRequestException``."""

    code: str | None = "BadRequestException"

    def __init__(
        self,
        data: BadRequestException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadRequestException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "BadRequestException":
        return cls(deserialize_json(data), message, response=response)
