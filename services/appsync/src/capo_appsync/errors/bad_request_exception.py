"""Generated from Smithy shape ``com.amazonaws.appsync#BadRequestException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_appsync.errors import ServiceError

if TYPE_CHECKING:
    import capo_appsync.types.bad_request_detail
    import capo_appsync.types.bad_request_reason
    import capo_appsync.types.error_message


class BadRequestException_(TypedDict, closed=True):
    message: NotRequired["capo_appsync.types.error_message.ErrorMessage"]
    reason: NotRequired["capo_appsync.types.bad_request_reason.BadRequestReason"]
    detail: NotRequired["capo_appsync.types.bad_request_detail.BadRequestDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        import capo_appsync.types.bad_request_reason

        out["reason"] = capo_appsync.types.bad_request_reason.serialize_json(
            value["reason"]
        )
    if "detail" in value:
        import capo_appsync.types.bad_request_detail

        out["detail"] = capo_appsync.types.bad_request_detail.serialize_json(
            value["detail"]
        )
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("reason") is not None:
        import capo_appsync.types.bad_request_reason

        out["reason"] = capo_appsync.types.bad_request_reason.deserialize_json(
            data["reason"]
        )
    if data.get("detail") is not None:
        import capo_appsync.types.bad_request_detail

        out["detail"] = capo_appsync.types.bad_request_detail.deserialize_json(
            data["detail"]
        )
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appsync#BadRequestException``."""

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
