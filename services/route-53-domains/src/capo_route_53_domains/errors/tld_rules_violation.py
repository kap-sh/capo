"""Generated from Smithy shape ``com.amazonaws.route53domains#TLDRulesViolation``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_route_53_domains.errors import ServiceError

if TYPE_CHECKING:
    import capo_route_53_domains.types.error_message


class TLDRulesViolation_(TypedDict, closed=True):
    message: NotRequired["capo_route_53_domains.types.error_message.ErrorMessage"]
    """<p>The top-level domain does not support this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TLDRulesViolation_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TLDRulesViolation_:
    out: TLDRulesViolation_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class TLDRulesViolation(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53domains#TLDRulesViolation``."""

    code: str | None = "TLDRulesViolation"

    def __init__(
        self,
        data: TLDRulesViolation_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TLDRulesViolation",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TLDRulesViolation":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
