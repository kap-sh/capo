"""Generated from Smithy shape ``com.amazonaws.greengrassv2#RequestAlreadyInProgressException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_greengrassv2.errors import ServiceError

if TYPE_CHECKING:
    import capo_greengrassv2.types.string


class RequestAlreadyInProgressException_(TypedDict, closed=True):
    message: "capo_greengrassv2.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: RequestAlreadyInProgressException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RequestAlreadyInProgressException_:
    out: RequestAlreadyInProgressException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class RequestAlreadyInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.greengrassv2#RequestAlreadyInProgressException``."""

    code: str | None = "RequestAlreadyInProgressException"

    def __init__(
        self,
        data: RequestAlreadyInProgressException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestAlreadyInProgressException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RequestAlreadyInProgressException":
        return cls(deserialize_json(data), message, response=response)
