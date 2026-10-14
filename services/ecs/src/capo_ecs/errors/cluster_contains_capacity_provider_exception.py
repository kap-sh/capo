"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterContainsCapacityProviderException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecs.types.string


class ClusterContainsCapacityProviderException_(TypedDict, closed=True):
    message: NotRequired["capo_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterContainsCapacityProviderException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterContainsCapacityProviderException_:
    out: ClusterContainsCapacityProviderException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ClusterContainsCapacityProviderException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#ClusterContainsCapacityProviderException``."""

    code: str | None = "ClusterContainsCapacityProviderException"

    def __init__(
        self,
        data: ClusterContainsCapacityProviderException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ClusterContainsCapacityProviderException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ClusterContainsCapacityProviderException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
