"""Generated from Smithy shape ``com.amazonaws.codecommit#ApprovalRuleNameRequiredException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import capo_codecommit.types.message


class ApprovalRuleNameRequiredException_(TypedDict, closed=True):
    message: NotRequired["capo_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalRuleNameRequiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApprovalRuleNameRequiredException_:
    out: ApprovalRuleNameRequiredException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ApprovalRuleNameRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#ApprovalRuleNameRequiredException``."""

    code: str | None = "ApprovalRuleNameRequiredException"

    def __init__(
        self,
        data: ApprovalRuleNameRequiredException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ApprovalRuleNameRequiredException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ApprovalRuleNameRequiredException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
