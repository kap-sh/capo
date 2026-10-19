"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_timestream_influxdb.errors import ServiceError

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_timestream_influxdb.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The reason that validation failed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_timestream_influxdb.types.validation_exception_reason

    out["reason"] = (
        capo_timestream_influxdb.types.validation_exception_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("reason") is not None:
        import capo_timestream_influxdb.types.validation_exception_reason

        out["reason"] = (
            capo_timestream_influxdb.types.validation_exception_reason.deserialize_aws_json_1_0(
                data["reason"]
            )
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_timestream_influxdb.types.validation_exception_reason.ValidationExceptionReason",
            "",
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.timestreaminfluxdb#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(
        self,
        data: ValidationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ValidationException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
