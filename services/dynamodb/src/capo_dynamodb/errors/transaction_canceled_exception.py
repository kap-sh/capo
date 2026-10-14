"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactionCanceledException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import capo_dynamodb.types.cancellation_reason_list
    import capo_dynamodb.types.error_message


class TransactionCanceledException_(TypedDict, closed=True):
    message: NotRequired["capo_dynamodb.types.error_message.ErrorMessage"]
    cancellation_reasons: NotRequired[
        "capo_dynamodb.types.cancellation_reason_list.CancellationReasonList"
    ]
    """<p>A list of cancellation reasons.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransactionCanceledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "cancellation_reasons" in value:
        import capo_dynamodb.types.cancellation_reason_list

        out["CancellationReasons"] = (
            capo_dynamodb.types.cancellation_reason_list.serialize_aws_json_1_0(
                value["cancellation_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TransactionCanceledException_:
    out: TransactionCanceledException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("CancellationReasons") is not None:
        import capo_dynamodb.types.cancellation_reason_list

        out["cancellation_reasons"] = (
            capo_dynamodb.types.cancellation_reason_list.deserialize_aws_json_1_0(
                data["CancellationReasons"]
            )
        )
    return out


class TransactionCanceledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#TransactionCanceledException``."""

    code: str | None = "TransactionCanceledException"

    def __init__(
        self,
        data: TransactionCanceledException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TransactionCanceledException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TransactionCanceledException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
