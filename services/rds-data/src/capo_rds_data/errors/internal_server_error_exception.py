"""Generated from Smithy shape ``com.amazonaws.rdsdata#InternalServerErrorException``."""

import zapros
from typing_extensions import TypedDict

from capo_rds_data.errors import ServiceError


class InternalServerErrorException_(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerErrorException_) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> InternalServerErrorException_:
    out: InternalServerErrorException_ = {}  # type: ignore[typeddict-item]
    return out


class InternalServerErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#InternalServerErrorException``."""

    code: str | None = "InternalServerErrorException"

    def __init__(
        self,
        data: InternalServerErrorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerErrorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerErrorException":
        return cls(deserialize_json(data), message, response=response)
