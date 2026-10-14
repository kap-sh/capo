"""Generated from Smithy shape ``com.amazonaws.support#CaseIdNotFound``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_support.errors import ServiceError

if TYPE_CHECKING:
    import capo_support.types.error_message


class CaseIdNotFound_(TypedDict, closed=True):
    message: NotRequired["capo_support.types.error_message.ErrorMessage"]
    """<p>The requested <code>CaseId</code> could not be located.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaseIdNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CaseIdNotFound_:
    out: CaseIdNotFound_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class CaseIdNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.support#CaseIdNotFound``."""

    code: str | None = "CaseIdNotFound"

    def __init__(
        self,
        data: CaseIdNotFound_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CaseIdNotFound",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CaseIdNotFound":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
