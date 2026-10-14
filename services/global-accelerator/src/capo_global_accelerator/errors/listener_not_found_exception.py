"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListenerNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_global_accelerator.errors import ServiceError

if TYPE_CHECKING:
    import capo_global_accelerator.types.error_message


class ListenerNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_global_accelerator.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListenerNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListenerNotFoundException_:
    out: ListenerNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ListenerNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.globalaccelerator#ListenerNotFoundException``."""

    code: str | None = "ListenerNotFoundException"

    def __init__(
        self,
        data: ListenerNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ListenerNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ListenerNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
