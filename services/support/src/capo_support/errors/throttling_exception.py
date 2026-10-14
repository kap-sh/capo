"""Generated from Smithy shape ``com.amazonaws.support#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_support.errors import ServiceError

if TYPE_CHECKING:
    import capo_support.types.availability_error_message
    import capo_support.types.throttling_reason_list


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_support.types.availability_error_message.AvailabilityErrorMessage"
    ]
    throttling_reasons: NotRequired[
        "capo_support.types.throttling_reason_list.ThrottlingReasonList"
    ]
    """<p>A list of one or more reasons that the request was throttled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "throttling_reasons" in value:
        import capo_support.types.throttling_reason_list

        out["throttlingReasons"] = (
            capo_support.types.throttling_reason_list.serialize_aws_json_1_1(
                value["throttling_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("throttlingReasons") is not None:
        import capo_support.types.throttling_reason_list

        out["throttling_reasons"] = (
            capo_support.types.throttling_reason_list.deserialize_aws_json_1_1(
                data["throttlingReasons"]
            )
        )
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.support#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
