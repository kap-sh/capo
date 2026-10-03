"""Generated from Smithy shape ``com.amazonaws.dynamodb#RequestLimitExceeded``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import capo_dynamodb.types.error_message
    import capo_dynamodb.types.throttling_reason_list


class RequestLimitExceeded_(TypedDict, closed=True):
    message: NotRequired["capo_dynamodb.types.error_message.ErrorMessage"]
    throttling_reasons: NotRequired[
        "capo_dynamodb.types.throttling_reason_list.ThrottlingReasonList"
    ]
    """<p>A list of <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> that provide detailed diagnostic information about why the request was throttled. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "throttling_reasons" in value:
        import capo_dynamodb.types.throttling_reason_list

        out["ThrottlingReasons"] = (
            capo_dynamodb.types.throttling_reason_list.serialize_aws_json_1_0(
                value["throttling_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RequestLimitExceeded_:
    out: RequestLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("ThrottlingReasons") is not None:
        import capo_dynamodb.types.throttling_reason_list

        out["throttling_reasons"] = (
            capo_dynamodb.types.throttling_reason_list.deserialize_aws_json_1_0(
                data["ThrottlingReasons"]
            )
        )
    return out


class RequestLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#RequestLimitExceeded``."""

    code: str | None = "RequestLimitExceeded"

    def __init__(self, data: RequestLimitExceeded_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestLimitExceeded",
            message=message,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None
    ) -> "RequestLimitExceeded":
        return cls(deserialize_aws_json_1_0(data), message)
