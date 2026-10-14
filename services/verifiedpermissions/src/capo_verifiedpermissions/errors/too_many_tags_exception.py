"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#TooManyTagsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import ServiceError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.amazon_resource_name


class TooManyTagsException_(TypedDict, closed=True):
    message: NotRequired["str"]
    resource_name: NotRequired[
        "capo_verifiedpermissions.types.amazon_resource_name.AmazonResourceName"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TooManyTagsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TooManyTagsException_:
    out: TooManyTagsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    return out


class TooManyTagsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.verifiedpermissions#TooManyTagsException``."""

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
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyTagsException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
