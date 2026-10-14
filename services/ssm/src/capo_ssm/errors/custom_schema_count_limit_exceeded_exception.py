"""Generated from Smithy shape ``com.amazonaws.ssm#CustomSchemaCountLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class CustomSchemaCountLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomSchemaCountLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomSchemaCountLimitExceededException_:
    out: CustomSchemaCountLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class CustomSchemaCountLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#CustomSchemaCountLimitExceededException``."""

    code: str | None = "CustomSchemaCountLimitExceededException"

    def __init__(
        self,
        data: CustomSchemaCountLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomSchemaCountLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CustomSchemaCountLimitExceededException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
