"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidFilterOption``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class InvalidFilterOption_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]
    """<p>The specified filter option isn't valid. Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidFilterOption_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidFilterOption_:
    out: InvalidFilterOption_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidFilterOption(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidFilterOption``."""

    code: str | None = "InvalidFilterOption"

    def __init__(
        self,
        data: InvalidFilterOption_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidFilterOption",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidFilterOption":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
