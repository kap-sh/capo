"""Generated from Smithy shape ``com.amazonaws.swf#TypeNotDeprecatedFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import ServiceError

if TYPE_CHECKING:
    import capo_swf.types.error_message


class TypeNotDeprecatedFault_(TypedDict, closed=True):
    message: NotRequired["capo_swf.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TypeNotDeprecatedFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TypeNotDeprecatedFault_:
    out: TypeNotDeprecatedFault_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class TypeNotDeprecatedFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.swf#TypeNotDeprecatedFault``."""

    code: str | None = "TypeNotDeprecatedFault"

    def __init__(
        self,
        data: TypeNotDeprecatedFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TypeNotDeprecatedFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TypeNotDeprecatedFault":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
