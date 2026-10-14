"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InactiveEventDataStoreException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudtrail.types.error_message


class InactiveEventDataStoreException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InactiveEventDataStoreException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InactiveEventDataStoreException_:
    out: InactiveEventDataStoreException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InactiveEventDataStoreException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#InactiveEventDataStoreException``."""

    code: str | None = "InactiveEventDataStoreException"

    def __init__(
        self,
        data: InactiveEventDataStoreException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InactiveEventDataStoreException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InactiveEventDataStoreException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
