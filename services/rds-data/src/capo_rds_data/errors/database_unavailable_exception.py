"""Generated from Smithy shape ``com.amazonaws.rdsdata#DatabaseUnavailableException``."""

import zapros
from typing_extensions import TypedDict

from capo_rds_data.errors import ServiceError


class DatabaseUnavailableException_(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseUnavailableException_) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DatabaseUnavailableException_:
    out: DatabaseUnavailableException_ = {}  # type: ignore[typeddict-item]
    return out


class DatabaseUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#DatabaseUnavailableException``."""

    code: str | None = "DatabaseUnavailableException"

    def __init__(
        self,
        data: DatabaseUnavailableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DatabaseUnavailableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DatabaseUnavailableException":
        return cls(deserialize_json(data), message, response=response)
