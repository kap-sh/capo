"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterPatternMismatchException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class ParameterPatternMismatchException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]
    """<p>The parameter name isn't valid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterPatternMismatchException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterPatternMismatchException_:
    out: ParameterPatternMismatchException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ParameterPatternMismatchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ParameterPatternMismatchException``."""

    code: str | None = "ParameterPatternMismatchException"

    def __init__(
        self,
        data: ParameterPatternMismatchException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ParameterPatternMismatchException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ParameterPatternMismatchException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
