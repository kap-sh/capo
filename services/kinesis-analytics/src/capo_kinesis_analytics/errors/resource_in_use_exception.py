"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ResourceInUseException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.error_message


class ResourceInUseException_(TypedDict, closed=True):
    message: NotRequired["capo_kinesis_analytics.types.error_message.ErrorMessage"]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceInUseException_:
    out: ResourceInUseException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ResourceInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisanalytics#ResourceInUseException``."""

    code: str | None = "ResourceInUseException"

    def __init__(
        self,
        data: ResourceInUseException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceInUseException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceInUseException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
