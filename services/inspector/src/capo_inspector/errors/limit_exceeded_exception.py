"""Generated from Smithy shape ``com.amazonaws.inspector#LimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_inspector.errors import ServiceError

if TYPE_CHECKING:
    import capo_inspector.types.bool
    import capo_inspector.types.error_message
    import capo_inspector.types.limit_exceeded_error_code


class LimitExceededException_(TypedDict, closed=True):
    message: "capo_inspector.types.error_message.ErrorMessage"
    """<p>Details of the exception error.</p>"""
    error_code: "capo_inspector.types.limit_exceeded_error_code.LimitExceededErrorCode"
    """<p>Code that indicates the type of error that is generated.</p>"""
    can_retry: "capo_inspector.types.bool.Bool"
    """<p>You can immediately retry your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_inspector.types.limit_exceeded_error_code

    out["errorCode"] = (
        capo_inspector.types.limit_exceeded_error_code.serialize_aws_json_1_1(
            value["error_code"]
        )
    )
    out["canRetry"] = value["can_retry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("errorCode") is not None:
        import capo_inspector.types.limit_exceeded_error_code

        out["error_code"] = (
            capo_inspector.types.limit_exceeded_error_code.deserialize_aws_json_1_1(
                data["errorCode"]
            )
        )
    else:
        import typing

        out["error_code"] = typing.cast(
            "capo_inspector.types.limit_exceeded_error_code.LimitExceededErrorCode", ""
        )
    if data.get("canRetry") is not None:
        out["can_retry"] = data["canRetry"]
    else:
        out["can_retry"] = False
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.inspector#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(
        self,
        data: LimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "LimitExceededException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
