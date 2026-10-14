"""Generated from Smithy shape ``com.amazonaws.directconnect#DuplicateTagKeysException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_direct_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_direct_connect.types.error_message


class DuplicateTagKeysException_(TypedDict, closed=True):
    message: NotRequired["capo_direct_connect.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicateTagKeysException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicateTagKeysException_:
    out: DuplicateTagKeysException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class DuplicateTagKeysException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directconnect#DuplicateTagKeysException``."""

    code: str | None = "DuplicateTagKeysException"

    def __init__(
        self,
        data: DuplicateTagKeysException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateTagKeysException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DuplicateTagKeysException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
