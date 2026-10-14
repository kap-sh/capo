"""Generated from Smithy shape ``com.amazonaws.devicefarm#NotEligibleException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_device_farm.errors import ServiceError

if TYPE_CHECKING:
    import capo_device_farm.types.message


class NotEligibleException_(TypedDict, closed=True):
    message: NotRequired["capo_device_farm.types.message.Message"]
    """<p>The HTTP response code of a Not Eligible exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotEligibleException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotEligibleException_:
    out: NotEligibleException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class NotEligibleException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devicefarm#NotEligibleException``."""

    code: str | None = "NotEligibleException"

    def __init__(
        self,
        data: NotEligibleException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotEligibleException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NotEligibleException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
