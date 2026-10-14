"""Generated from Smithy shape ``com.amazonaws.codepipeline#InvalidActionDeclarationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import capo_codepipeline.types.message


class InvalidActionDeclarationException_(TypedDict, closed=True):
    message: NotRequired["capo_codepipeline.types.message.Message"]
    """<p>The message provided to the user in the event of an exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidActionDeclarationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidActionDeclarationException_:
    out: InvalidActionDeclarationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidActionDeclarationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#InvalidActionDeclarationException``."""

    code: str | None = "InvalidActionDeclarationException"

    def __init__(
        self,
        data: InvalidActionDeclarationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidActionDeclarationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidActionDeclarationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
