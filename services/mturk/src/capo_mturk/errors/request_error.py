"""Generated from Smithy shape ``com.amazonaws.mturk#RequestError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mturk.errors import ServiceError

if TYPE_CHECKING:
    import capo_mturk.types.exception_message
    import capo_mturk.types.turk_error_code


class RequestError_(TypedDict, closed=True):
    message: NotRequired["capo_mturk.types.exception_message.ExceptionMessage"]
    turk_error_code: NotRequired["capo_mturk.types.turk_error_code.TurkErrorCode"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "turk_error_code" in value:
        out["TurkErrorCode"] = value["turk_error_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestError_:
    out: RequestError_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("TurkErrorCode") is not None:
        out["turk_error_code"] = data["TurkErrorCode"]
    return out


class RequestError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mturk#RequestError``."""

    code: str | None = "RequestError"

    def __init__(
        self,
        data: RequestError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RequestError":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
