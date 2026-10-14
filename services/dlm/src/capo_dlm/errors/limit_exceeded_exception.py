"""Generated from Smithy shape ``com.amazonaws.dlm#LimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_dlm.errors import ServiceError

if TYPE_CHECKING:
    import capo_dlm.types.error_code
    import capo_dlm.types.error_message
    import capo_dlm.types.string


class LimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_dlm.types.error_message.ErrorMessage"]
    code: NotRequired["capo_dlm.types.error_code.ErrorCode"]
    resource_type: NotRequired["capo_dlm.types.string.String"]
    """<p>Value is the type of resource for which a limit was exceeded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dlm#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(
        self,
        data: LimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "LimitExceededException":
        return cls(deserialize_json(data), message, response=response)
