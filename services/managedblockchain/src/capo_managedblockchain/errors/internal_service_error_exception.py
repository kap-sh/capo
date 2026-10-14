"""Generated from Smithy shape ``com.amazonaws.managedblockchain#InternalServiceErrorException``."""

import zapros
from typing_extensions import TypedDict

from capo_managedblockchain.errors import ServiceError


class InternalServiceErrorException_(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: InternalServiceErrorException_) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> InternalServiceErrorException_:
    out: InternalServiceErrorException_ = {}  # type: ignore[typeddict-item]
    return out


class InternalServiceErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.managedblockchain#InternalServiceErrorException``."""

    code: str | None = "InternalServiceErrorException"

    def __init__(
        self,
        data: InternalServiceErrorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceErrorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServiceErrorException":
        return cls(deserialize_json(data), message, response=response)
