"""Generated from Smithy shape ``com.amazonaws.dynamodb#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import capo_dynamodb.types.availability_error_message
    import capo_dynamodb.types.throttling_reason_list


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_dynamodb.types.availability_error_message.AvailabilityErrorMessage"
    ]
    throttling_reasons: NotRequired[
        "capo_dynamodb.types.throttling_reason_list.ThrottlingReasonList"
    ]
    """<p>A list of <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> that provide detailed diagnostic information about why the request was throttled. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "throttling_reasons" in value:
        import capo_dynamodb.types.throttling_reason_list

        out["throttlingReasons"] = (
            capo_dynamodb.types.throttling_reason_list.serialize_aws_json_1_0(
                value["throttling_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("throttlingReasons") is not None:
        import capo_dynamodb.types.throttling_reason_list

        out["throttling_reasons"] = (
            capo_dynamodb.types.throttling_reason_list.deserialize_aws_json_1_0(
                data["throttlingReasons"]
            )
        )
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None
    ) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_0(data), message)
