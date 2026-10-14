"""Generated from Smithy shape ``com.amazonaws.codecommit#TargetRequiredException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import capo_codecommit.types.message


class TargetRequiredException_(TypedDict, closed=True):
    message: NotRequired["capo_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetRequiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetRequiredException_:
    out: TargetRequiredException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class TargetRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#TargetRequiredException``."""

    code: str | None = "TargetRequiredException"

    def __init__(
        self,
        data: TargetRequiredException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TargetRequiredException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TargetRequiredException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
