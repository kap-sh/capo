"""Generated from Smithy shape ``com.amazonaws.snowball#KMSRequestFailedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_snowball.errors import ServiceError

if TYPE_CHECKING:
    import capo_snowball.types.string


class KMSRequestFailedException_(TypedDict, closed=True):
    message: NotRequired["capo_snowball.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSRequestFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSRequestFailedException_:
    out: KMSRequestFailedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class KMSRequestFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.snowball#KMSRequestFailedException``."""

    code: str | None = "KMSRequestFailedException"

    def __init__(
        self,
        data: KMSRequestFailedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSRequestFailedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "KMSRequestFailedException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
