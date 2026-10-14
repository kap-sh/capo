"""Generated from Smithy shape ``com.amazonaws.signer#NotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_signer.errors import ServiceError

if TYPE_CHECKING:
    import capo_signer.types.error_code
    import capo_signer.types.error_message


class NotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_signer.types.error_message.ErrorMessage"]
    code: NotRequired["capo_signer.types.error_code.ErrorCode"]


# --- restJson1 ser/de ---
def serialize_json(value: NotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> NotFoundException_:
    out: NotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    return out


class NotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.signer#NotFoundException``."""

    code: str | None = "NotFoundException"

    def __init__(
        self,
        data: NotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NotFoundException":
        return cls(deserialize_json(data), message, response=response)
