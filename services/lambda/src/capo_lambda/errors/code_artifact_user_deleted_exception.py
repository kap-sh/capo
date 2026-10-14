"""Generated from Smithy shape ``com.amazonaws.lambda#CodeArtifactUserDeletedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class CodeArtifactUserDeletedException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.string.String"]
    """<p>The exception type.</p>"""
    message: NotRequired["capo_lambda.types.string.String"]
    """<p>The exception message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeArtifactUserDeletedException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CodeArtifactUserDeletedException_:
    out: CodeArtifactUserDeletedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class CodeArtifactUserDeletedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#CodeArtifactUserDeletedException``."""

    code: str | None = "CodeArtifactUserDeletedException"

    def __init__(
        self,
        data: CodeArtifactUserDeletedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CodeArtifactUserDeletedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CodeArtifactUserDeletedException":
        return cls(deserialize_json(data), message, response=response)
