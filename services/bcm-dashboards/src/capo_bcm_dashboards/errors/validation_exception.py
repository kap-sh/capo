"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_bcm_dashboards.errors import ServiceError

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.generic_string


class ValidationException_(TypedDict, closed=True):
    message: "capo_bcm_dashboards.types.generic_string.GenericString"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bcmdashboards#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(
        self,
        data: ValidationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ValidationException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
