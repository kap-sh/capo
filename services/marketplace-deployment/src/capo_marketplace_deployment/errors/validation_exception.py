"""Generated from Smithy shape ``com.amazonaws.marketplacedeployment#ValidationException``."""

import zapros
from typing_extensions import TypedDict

from capo_marketplace_deployment.errors import ServiceError


class ValidationException_(TypedDict, closed=True):
    message: "str"
    field_name: "str"
    """<p>The field name associated with the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["fieldName"] = value["field_name"]
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("fieldName") is not None:
        out["field_name"] = data["fieldName"]
    else:
        out["field_name"] = ""
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacedeployment#ValidationException``."""

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
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ValidationException":
        return cls(deserialize_json(data), message, response=response)
