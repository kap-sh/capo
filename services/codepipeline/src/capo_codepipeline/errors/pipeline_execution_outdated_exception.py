"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineExecutionOutdatedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import capo_codepipeline.types.message


class PipelineExecutionOutdatedException_(TypedDict, closed=True):
    message: NotRequired["capo_codepipeline.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionOutdatedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineExecutionOutdatedException_:
    out: PipelineExecutionOutdatedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class PipelineExecutionOutdatedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#PipelineExecutionOutdatedException``."""

    code: str | None = "PipelineExecutionOutdatedException"

    def __init__(
        self,
        data: PipelineExecutionOutdatedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PipelineExecutionOutdatedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PipelineExecutionOutdatedException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
