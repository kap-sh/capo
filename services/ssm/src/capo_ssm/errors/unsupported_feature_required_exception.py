"""Generated from Smithy shape ``com.amazonaws.ssm#UnsupportedFeatureRequiredException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class UnsupportedFeatureRequiredException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedFeatureRequiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedFeatureRequiredException_:
    out: UnsupportedFeatureRequiredException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class UnsupportedFeatureRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#UnsupportedFeatureRequiredException``."""

    code: str | None = "UnsupportedFeatureRequiredException"

    def __init__(
        self,
        data: UnsupportedFeatureRequiredException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedFeatureRequiredException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnsupportedFeatureRequiredException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
