"""Generated from Smithy shape ``com.amazonaws.ram#MalformedPolicyTemplateException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ram.errors import ServiceError

if TYPE_CHECKING:
    import capo_ram.types.string


class MalformedPolicyTemplateException_(TypedDict, closed=True):
    message: "capo_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: MalformedPolicyTemplateException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MalformedPolicyTemplateException_:
    out: MalformedPolicyTemplateException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class MalformedPolicyTemplateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#MalformedPolicyTemplateException``."""

    code: str | None = "MalformedPolicyTemplateException"

    def __init__(
        self,
        data: MalformedPolicyTemplateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MalformedPolicyTemplateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MalformedPolicyTemplateException":
        return cls(deserialize_json(data), message, response=response)
