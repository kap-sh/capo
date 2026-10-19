"""Generated from Smithy shape ``com.amazonaws.securityir#SecurityIncidentResponseNotActiveException``."""

import zapros
from typing_extensions import TypedDict

from capo_security_ir.errors import ServiceError


class SecurityIncidentResponseNotActiveException_(TypedDict, closed=True):
    message: "str"
    """<p>The exception message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityIncidentResponseNotActiveException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SecurityIncidentResponseNotActiveException_:
    out: SecurityIncidentResponseNotActiveException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class SecurityIncidentResponseNotActiveException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.securityir#SecurityIncidentResponseNotActiveException``."""

    code: str | None = "SecurityIncidentResponseNotActiveException"

    def __init__(
        self,
        data: SecurityIncidentResponseNotActiveException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SecurityIncidentResponseNotActiveException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SecurityIncidentResponseNotActiveException":
        return cls(deserialize_json(data), message, response=response)
