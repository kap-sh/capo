"""Generated from Smithy shape ``com.amazonaws.rdsdata#ForbiddenException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_rds_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_rds_data.types.error_message


class ForbiddenException_(TypedDict, closed=True):
    message: NotRequired["capo_rds_data.types.error_message.ErrorMessage"]
    """<p>The error message returned by this <code>ForbiddenException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForbiddenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ForbiddenException_:
    out: ForbiddenException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ForbiddenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#ForbiddenException``."""

    code: str | None = "ForbiddenException"

    def __init__(
        self,
        data: ForbiddenException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ForbiddenException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ForbiddenException":
        return cls(deserialize_json(data), message, response=response)
