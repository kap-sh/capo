"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineExecutionNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import capo_codepipeline.types.message


class PipelineExecutionNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_codepipeline.types.message.Message"]
    """<p>The message provided to the user in the event of an exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineExecutionNotFoundException_:
    out: PipelineExecutionNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class PipelineExecutionNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#PipelineExecutionNotFoundException``."""

    code: str | None = "PipelineExecutionNotFoundException"

    def __init__(
        self,
        data: PipelineExecutionNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PipelineExecutionNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PipelineExecutionNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
