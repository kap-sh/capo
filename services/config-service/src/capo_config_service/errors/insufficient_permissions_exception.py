"""Generated from Smithy shape ``com.amazonaws.configservice#InsufficientPermissionsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_config_service.types.error_message


class InsufficientPermissionsException_(TypedDict, closed=True):
    message: NotRequired["capo_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsufficientPermissionsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InsufficientPermissionsException_:
    out: InsufficientPermissionsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InsufficientPermissionsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#InsufficientPermissionsException``."""

    code: str | None = "InsufficientPermissionsException"

    def __init__(
        self,
        data: InsufficientPermissionsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InsufficientPermissionsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InsufficientPermissionsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
