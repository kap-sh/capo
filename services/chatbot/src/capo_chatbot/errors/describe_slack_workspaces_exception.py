"""Generated from Smithy shape ``com.amazonaws.chatbot#DescribeSlackWorkspacesException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import capo_chatbot.types.error_message


class DescribeSlackWorkspacesException_(TypedDict, closed=True):
    message: NotRequired["capo_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSlackWorkspacesException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DescribeSlackWorkspacesException_:
    out: DescribeSlackWorkspacesException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class DescribeSlackWorkspacesException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#DescribeSlackWorkspacesException``."""

    code: str | None = "DescribeSlackWorkspacesException"

    def __init__(
        self,
        data: DescribeSlackWorkspacesException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DescribeSlackWorkspacesException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DescribeSlackWorkspacesException":
        return cls(deserialize_json(data), message, response=response)
