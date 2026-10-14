"""Generated from Smithy shape ``com.amazonaws.backup#AlreadyExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import ServiceError

if TYPE_CHECKING:
    import capo_backup.types.string


class AlreadyExistsException_(TypedDict, closed=True):
    code: NotRequired["capo_backup.types.string.string"]
    message: NotRequired["capo_backup.types.string.string"]
    creator_request_id: NotRequired["capo_backup.types.string.string"]
    """<p></p>"""
    arn: NotRequired["capo_backup.types.string.string"]
    """<p></p>"""
    type: NotRequired["capo_backup.types.string.string"]
    """<p></p>"""
    context: NotRequired["capo_backup.types.string.string"]
    """<p></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlreadyExistsException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        out["Type"] = value["type"]
    if "context" in value:
        out["Context"] = value["context"]
    return out


def deserialize_json(data: dict) -> AlreadyExistsException_:
    out: AlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Context") is not None:
        out["context"] = data["Context"]
    return out


class AlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.backup#AlreadyExistsException``."""

    code: str | None = "AlreadyExistsException"

    def __init__(
        self,
        data: AlreadyExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AlreadyExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AlreadyExistsException":
        return cls(deserialize_json(data), message, response=response)
