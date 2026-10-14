"""Generated from Smithy shape ``com.amazonaws.rdsdata#DatabaseNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_rds_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_rds_data.types.error_message


class DatabaseNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_rds_data.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DatabaseNotFoundException_:
    out: DatabaseNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class DatabaseNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#DatabaseNotFoundException``."""

    code: str | None = "DatabaseNotFoundException"

    def __init__(
        self,
        data: DatabaseNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DatabaseNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DatabaseNotFoundException":
        return cls(deserialize_json(data), message, response=response)
