"""Generated from Smithy shape ``com.amazonaws.codecommit#InvalidSystemTagUsageException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import capo_codecommit.types.message


class InvalidSystemTagUsageException_(TypedDict, closed=True):
    message: NotRequired["capo_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidSystemTagUsageException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidSystemTagUsageException_:
    out: InvalidSystemTagUsageException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidSystemTagUsageException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#InvalidSystemTagUsageException``."""

    code: str | None = "InvalidSystemTagUsageException"

    def __init__(
        self,
        data: InvalidSystemTagUsageException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSystemTagUsageException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidSystemTagUsageException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
