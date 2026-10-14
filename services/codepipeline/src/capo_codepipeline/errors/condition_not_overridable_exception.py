"""Generated from Smithy shape ``com.amazonaws.codepipeline#ConditionNotOverridableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import capo_codepipeline.types.string


class ConditionNotOverridableException_(TypedDict, closed=True):
    message: NotRequired["capo_codepipeline.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionNotOverridableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConditionNotOverridableException_:
    out: ConditionNotOverridableException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ConditionNotOverridableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#ConditionNotOverridableException``."""

    code: str | None = "ConditionNotOverridableException"

    def __init__(
        self,
        data: ConditionNotOverridableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConditionNotOverridableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConditionNotOverridableException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
