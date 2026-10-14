"""Generated from Smithy shape ``com.amazonaws.iotwireless#TooManyTagsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iot_wireless.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot_wireless.types.amazon_resource_name
    import capo_iot_wireless.types.message


class TooManyTagsException_(TypedDict, closed=True):
    message: NotRequired["capo_iot_wireless.types.message.Message"]
    resource_name: NotRequired[
        "capo_iot_wireless.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>Name of the resource that exceeds maximum number of tags allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TooManyTagsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> TooManyTagsException_:
    out: TooManyTagsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    return out


class TooManyTagsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotwireless#TooManyTagsException``."""

    code: str | None = "TooManyTagsException"

    def __init__(
        self,
        data: TooManyTagsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyTagsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyTagsException":
        return cls(deserialize_json(data), message, response=response)
