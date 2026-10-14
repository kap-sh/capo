"""Generated from Smithy shape ``com.amazonaws.groundstation#DependencyException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_groundstation.errors import ServiceError


class DependencyException_(TypedDict, closed=True):
    message: NotRequired["str"]
    parameter_name: NotRequired["str"]
    """<p>Name of the parameter that caused the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DependencyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "parameter_name" in value:
        out["parameterName"] = value["parameter_name"]
    return out


def deserialize_json(data: dict) -> DependencyException_:
    out: DependencyException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("parameterName") is not None:
        out["parameter_name"] = data["parameterName"]
    return out


class DependencyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.groundstation#DependencyException``."""

    code: str | None = "DependencyException"

    def __init__(
        self,
        data: DependencyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DependencyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DependencyException":
        return cls(deserialize_json(data), message, response=response)
