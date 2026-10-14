"""Generated from Smithy shape ``com.amazonaws.rdsdata#UnsupportedResultException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_rds_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_rds_data.types.error_message


class UnsupportedResultException_(TypedDict, closed=True):
    message: NotRequired["capo_rds_data.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedResultException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnsupportedResultException_:
    out: UnsupportedResultException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class UnsupportedResultException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#UnsupportedResultException``."""

    code: str | None = "UnsupportedResultException"

    def __init__(
        self,
        data: UnsupportedResultException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedResultException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnsupportedResultException":
        return cls(deserialize_json(data), message, response=response)
