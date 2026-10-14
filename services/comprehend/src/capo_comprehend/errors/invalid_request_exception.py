"""Generated from Smithy shape ``com.amazonaws.comprehend#InvalidRequestException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import ServiceError

if TYPE_CHECKING:
    import capo_comprehend.types.invalid_request_detail
    import capo_comprehend.types.invalid_request_reason
    import capo_comprehend.types.string


class InvalidRequestException_(TypedDict, closed=True):
    message: NotRequired["capo_comprehend.types.string.String"]
    reason: NotRequired[
        "capo_comprehend.types.invalid_request_reason.InvalidRequestReason"
    ]
    detail: NotRequired[
        "capo_comprehend.types.invalid_request_detail.InvalidRequestDetail"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import capo_comprehend.types.invalid_request_reason

        out["Reason"] = (
            capo_comprehend.types.invalid_request_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    if "detail" in value:
        import capo_comprehend.types.invalid_request_detail

        out["Detail"] = (
            capo_comprehend.types.invalid_request_detail.serialize_aws_json_1_1(
                value["detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        import capo_comprehend.types.invalid_request_reason

        out["reason"] = (
            capo_comprehend.types.invalid_request_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    if data.get("Detail") is not None:
        import capo_comprehend.types.invalid_request_detail

        out["detail"] = (
            capo_comprehend.types.invalid_request_detail.deserialize_aws_json_1_1(
                data["Detail"]
            )
        )
    return out


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.comprehend#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(
        self,
        data: InvalidRequestException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidRequestException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
