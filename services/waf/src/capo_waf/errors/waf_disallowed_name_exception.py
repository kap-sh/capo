"""Generated from Smithy shape ``com.amazonaws.waf#WAFDisallowedNameException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_waf.errors import ServiceError

if TYPE_CHECKING:
    import capo_waf.types.error_message


class WAFDisallowedNameException_(TypedDict, closed=True):
    message: NotRequired["capo_waf.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFDisallowedNameException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFDisallowedNameException_:
    out: WAFDisallowedNameException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class WAFDisallowedNameException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.waf#WAFDisallowedNameException``."""

    code: str | None = "WAFDisallowedNameException"

    def __init__(
        self,
        data: WAFDisallowedNameException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFDisallowedNameException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "WAFDisallowedNameException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
