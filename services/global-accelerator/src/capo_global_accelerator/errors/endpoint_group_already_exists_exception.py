"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#EndpointGroupAlreadyExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_global_accelerator.errors import ServiceError

if TYPE_CHECKING:
    import capo_global_accelerator.types.error_message


class EndpointGroupAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_global_accelerator.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointGroupAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointGroupAlreadyExistsException_:
    out: EndpointGroupAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class EndpointGroupAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.globalaccelerator#EndpointGroupAlreadyExistsException``."""

    code: str | None = "EndpointGroupAlreadyExistsException"

    def __init__(
        self,
        data: EndpointGroupAlreadyExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EndpointGroupAlreadyExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "EndpointGroupAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
