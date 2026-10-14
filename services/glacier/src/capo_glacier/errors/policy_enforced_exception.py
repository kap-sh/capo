"""Generated from Smithy shape ``com.amazonaws.glacier#PolicyEnforcedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_glacier.errors import ServiceError

if TYPE_CHECKING:
    import capo_glacier.types.string


class PolicyEnforcedException_(TypedDict, closed=True):
    type: NotRequired["capo_glacier.types.string.string"]
    """<p>Client</p>"""
    code: NotRequired["capo_glacier.types.string.string"]
    """<p>PolicyEnforcedException</p>"""
    message: NotRequired["capo_glacier.types.string.string"]
    """<p>InitiateJob request denied by current data retrieval policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyEnforcedException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PolicyEnforcedException_:
    out: PolicyEnforcedException_ = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class PolicyEnforcedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glacier#PolicyEnforcedException``."""

    code: str | None = "PolicyEnforcedException"

    def __init__(
        self,
        data: PolicyEnforcedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyEnforcedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PolicyEnforcedException":
        return cls(deserialize_json(data), message, response=response)
