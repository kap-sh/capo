"""Generated from Smithy shape ``com.amazonaws.codepipeline#ConcurrentPipelineExecutionsLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import capo_codepipeline.types.message


class ConcurrentPipelineExecutionsLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_codepipeline.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ConcurrentPipelineExecutionsLimitExceededException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ConcurrentPipelineExecutionsLimitExceededException_:
    out: ConcurrentPipelineExecutionsLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ConcurrentPipelineExecutionsLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#ConcurrentPipelineExecutionsLimitExceededException``."""

    code: str | None = "ConcurrentPipelineExecutionsLimitExceededException"

    def __init__(
        self,
        data: ConcurrentPipelineExecutionsLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConcurrentPipelineExecutionsLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConcurrentPipelineExecutionsLimitExceededException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
