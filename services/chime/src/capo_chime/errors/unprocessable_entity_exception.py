"""Generated from Smithy shape ``com.amazonaws.chime#UnprocessableEntityException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_chime.errors import ServiceError

if TYPE_CHECKING:
    import capo_chime.types.error_code
    import capo_chime.types.string


class UnprocessableEntityException_(TypedDict, closed=True):
    code: NotRequired["capo_chime.types.error_code.ErrorCode"]
    message: NotRequired["capo_chime.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessableEntityException_) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_chime.types.error_code

        out["Code"] = capo_chime.types.error_code.serialize_json(value["code"])
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnprocessableEntityException_:
    out: UnprocessableEntityException_ = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_chime.types.error_code

        out["code"] = capo_chime.types.error_code.deserialize_json(data["Code"])
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class UnprocessableEntityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chime#UnprocessableEntityException``."""

    code: str | None = "UnprocessableEntityException"

    def __init__(
        self,
        data: UnprocessableEntityException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnprocessableEntityException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnprocessableEntityException":
        return cls(deserialize_json(data), message, response=response)
