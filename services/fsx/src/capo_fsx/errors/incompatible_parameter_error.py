"""Generated from Smithy shape ``com.amazonaws.fsx#IncompatibleParameterError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message
    import capo_fsx.types.parameter


class IncompatibleParameterError_(TypedDict, closed=True):
    parameter: NotRequired["capo_fsx.types.parameter.Parameter"]
    """<p>A parameter that is incompatible with the earlier request.</p>"""
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncompatibleParameterError_) -> dict:
    out: dict = {}
    if "parameter" in value:
        out["Parameter"] = value["parameter"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IncompatibleParameterError_:
    out: IncompatibleParameterError_ = {}  # type: ignore[typeddict-item]
    if data.get("Parameter") is not None:
        out["parameter"] = data["Parameter"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class IncompatibleParameterError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#IncompatibleParameterError``."""

    code: str | None = "IncompatibleParameterError"

    def __init__(
        self,
        data: IncompatibleParameterError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncompatibleParameterError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "IncompatibleParameterError":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
