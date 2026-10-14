"""Generated from Smithy shape ``com.amazonaws.datapipeline#TaskNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_data_pipeline.errors import ServiceError

if TYPE_CHECKING:
    import capo_data_pipeline.types.error_message


class TaskNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_data_pipeline.types.error_message.errorMessage"]
    """<p>Description of the error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskNotFoundException_:
    out: TaskNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class TaskNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.datapipeline#TaskNotFoundException``."""

    code: str | None = "TaskNotFoundException"

    def __init__(
        self,
        data: TaskNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TaskNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TaskNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
