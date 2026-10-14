"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterVersionLabelLimitExceeded``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class ParameterVersionLabelLimitExceeded_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterVersionLabelLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterVersionLabelLimitExceeded_:
    out: ParameterVersionLabelLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ParameterVersionLabelLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ParameterVersionLabelLimitExceeded``."""

    code: str | None = "ParameterVersionLabelLimitExceeded"

    def __init__(
        self,
        data: ParameterVersionLabelLimitExceeded_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ParameterVersionLabelLimitExceeded",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ParameterVersionLabelLimitExceeded":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
