"""Generated from Smithy shape ``com.amazonaws.ssm#ResourcePolicyLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.integer
    import capo_ssm.types.string


class ResourcePolicyLimitExceededException_(TypedDict, closed=True):
    limit: "capo_ssm.types.integer.Integer"
    limit_type: NotRequired["capo_ssm.types.string.String"]
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourcePolicyLimitExceededException_) -> dict:
    out: dict = {}
    out["Limit"] = value.get("limit", 0)
    if "limit_type" in value:
        out["LimitType"] = value["limit_type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourcePolicyLimitExceededException_:
    out: ResourcePolicyLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if data.get("LimitType") is not None:
        out["limit_type"] = data["LimitType"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ResourcePolicyLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ResourcePolicyLimitExceededException``."""

    code: str | None = "ResourcePolicyLimitExceededException"

    def __init__(
        self,
        data: ResourcePolicyLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourcePolicyLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourcePolicyLimitExceededException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
