"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidDocument``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class InvalidDocument_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]
    """<p>The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidDocument_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidDocument_:
    out: InvalidDocument_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidDocument(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidDocument``."""

    code: str | None = "InvalidDocument"

    def __init__(
        self,
        data: InvalidDocument_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDocument",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidDocument":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
