"""Generated from Smithy shape ``com.amazonaws.support#CaseCreationLimitExceeded``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_support.errors import ServiceError

if TYPE_CHECKING:
    import capo_support.types.error_message


class CaseCreationLimitExceeded_(TypedDict, closed=True):
    message: NotRequired["capo_support.types.error_message.ErrorMessage"]
    """<p>An error message that indicates that you have exceeded the number of cases you can have open.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaseCreationLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CaseCreationLimitExceeded_:
    out: CaseCreationLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class CaseCreationLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.support#CaseCreationLimitExceeded``."""

    code: str | None = "CaseCreationLimitExceeded"

    def __init__(
        self,
        data: CaseCreationLimitExceeded_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CaseCreationLimitExceeded",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CaseCreationLimitExceeded":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
