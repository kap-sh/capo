"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_identity.errors import ServiceError

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.error_code
    import capo_chime_sdk_identity.types.string


class ConflictException_(TypedDict, closed=True):
    code: NotRequired["capo_chime_sdk_identity.types.error_code.ErrorCode"]
    message: NotRequired["capo_chime_sdk_identity.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_chime_sdk_identity.types.error_code

        out["Code"] = capo_chime_sdk_identity.types.error_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_chime_sdk_identity.types.error_code

        out["code"] = capo_chime_sdk_identity.types.error_code.deserialize_json(
            data["Code"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkidentity#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(
        self,
        data: ConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_json(data), message, response=response)
