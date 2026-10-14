"""Generated from Smithy shape ``com.amazonaws.lakeformation#GlueEncryptionException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import ServiceError

if TYPE_CHECKING:
    import capo_lakeformation.types.message_string


class GlueEncryptionException_(TypedDict, closed=True):
    message: NotRequired["capo_lakeformation.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueEncryptionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> GlueEncryptionException_:
    out: GlueEncryptionException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class GlueEncryptionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lakeformation#GlueEncryptionException``."""

    code: str | None = "GlueEncryptionException"

    def __init__(
        self,
        data: GlueEncryptionException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GlueEncryptionException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "GlueEncryptionException":
        return cls(deserialize_json(data), message, response=response)
