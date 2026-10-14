"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterContainsTasksException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecs.types.string


class ClusterContainsTasksException_(TypedDict, closed=True):
    message: NotRequired["capo_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterContainsTasksException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterContainsTasksException_:
    out: ClusterContainsTasksException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ClusterContainsTasksException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#ClusterContainsTasksException``."""

    code: str | None = "ClusterContainsTasksException"

    def __init__(
        self,
        data: ClusterContainsTasksException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ClusterContainsTasksException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ClusterContainsTasksException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
