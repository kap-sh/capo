"""Generated from Smithy shape ``com.amazonaws.codecommit#ParentCommitIdOutdatedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import capo_codecommit.types.message


class ParentCommitIdOutdatedException_(TypedDict, closed=True):
    message: NotRequired["capo_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParentCommitIdOutdatedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParentCommitIdOutdatedException_:
    out: ParentCommitIdOutdatedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ParentCommitIdOutdatedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#ParentCommitIdOutdatedException``."""

    code: str | None = "ParentCommitIdOutdatedException"

    def __init__(
        self,
        data: ParentCommitIdOutdatedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ParentCommitIdOutdatedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ParentCommitIdOutdatedException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
