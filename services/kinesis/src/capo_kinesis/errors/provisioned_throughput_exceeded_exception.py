"""Generated from Smithy shape ``com.amazonaws.kinesis#ProvisionedThroughputExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis.types.error_message


class ProvisionedThroughputExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_kinesis.types.error_message.ErrorMessage"]
    """<p>A message that provides information about the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedThroughputExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisionedThroughputExceededException_:
    out: ProvisionedThroughputExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ProvisionedThroughputExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesis#ProvisionedThroughputExceededException``."""

    code: str | None = "ProvisionedThroughputExceededException"

    def __init__(
        self,
        data: ProvisionedThroughputExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ProvisionedThroughputExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ProvisionedThroughputExceededException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
