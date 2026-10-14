"""Generated from Smithy shape ``com.amazonaws.rdsdata#StatementTimeoutException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_rds_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_rds_data.types.error_message
    import capo_rds_data.types.long


class StatementTimeoutException_(TypedDict, closed=True):
    message: NotRequired["capo_rds_data.types.error_message.ErrorMessage"]
    """<p>The error message returned by this <code>StatementTimeoutException</code> error.</p>"""
    db_connection_id: "capo_rds_data.types.long.Long"
    """<p>The database connection ID that executed the SQL statement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatementTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    out["dbConnectionId"] = value.get("db_connection_id", 0)
    return out


def deserialize_json(data: dict) -> StatementTimeoutException_:
    out: StatementTimeoutException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("dbConnectionId") is not None:
        out["db_connection_id"] = data["dbConnectionId"]
    else:
        out["db_connection_id"] = 0
    return out


class StatementTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#StatementTimeoutException``."""

    code: str | None = "StatementTimeoutException"

    def __init__(
        self,
        data: StatementTimeoutException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="StatementTimeoutException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "StatementTimeoutException":
        return cls(deserialize_json(data), message, response=response)
