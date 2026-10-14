"""Generated from Smithy shape ``com.amazonaws.machinelearning#PredictorNotMountedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_machine_learning.errors import ServiceError

if TYPE_CHECKING:
    import capo_machine_learning.types.error_message


class PredictorNotMountedException_(TypedDict, closed=True):
    message: NotRequired["capo_machine_learning.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictorNotMountedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictorNotMountedException_:
    out: PredictorNotMountedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class PredictorNotMountedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.machinelearning#PredictorNotMountedException``."""

    code: str | None = "PredictorNotMountedException"

    def __init__(
        self,
        data: PredictorNotMountedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PredictorNotMountedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PredictorNotMountedException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
