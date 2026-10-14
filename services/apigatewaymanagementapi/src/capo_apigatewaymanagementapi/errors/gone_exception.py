"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#GoneException``."""

import zapros
from typing_extensions import TypedDict

from capo_apigatewaymanagementapi.errors import ServiceError


class GoneException_(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GoneException_) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GoneException_:
    out: GoneException_ = {}  # type: ignore[typeddict-item]
    return out


class GoneException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.apigatewaymanagementapi#GoneException``."""

    code: str | None = "GoneException"

    def __init__(
        self,
        data: GoneException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GoneException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "GoneException":
        return cls(deserialize_json(data), message, response=response)
