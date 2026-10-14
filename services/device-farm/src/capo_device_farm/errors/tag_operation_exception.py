"""Generated from Smithy shape ``com.amazonaws.devicefarm#TagOperationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_device_farm.errors import ServiceError

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.exception_message


class TagOperationException_(TypedDict, closed=True):
    message: NotRequired["capo_device_farm.types.exception_message.ExceptionMessage"]
    resource_name: NotRequired[
        "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagOperationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TagOperationException_:
    out: TagOperationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    return out


class TagOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devicefarm#TagOperationException``."""

    code: str | None = "TagOperationException"

    def __init__(
        self,
        data: TagOperationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TagOperationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TagOperationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
