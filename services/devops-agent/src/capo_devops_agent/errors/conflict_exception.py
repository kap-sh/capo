"""Generated from Smithy shape ``com.amazonaws.devopsagent#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import ServiceError

if TYPE_CHECKING:
    import capo_devops_agent.types.conflict_exception_reason


class ConflictException_(TypedDict, closed=True):
    message: "str"
    """<p>Detailed error message describing the conflict.</p>"""
    reason: NotRequired[
        "capo_devops_agent.types.conflict_exception_reason.ConflictExceptionReason"
    ]
    """<p>A machine-readable reason code that explains why the request conflicted with the current state of the resource. For example, <code>CHAT_ARCHIVED</code> indicates that the request acted on a chat that is archived. This field is absent when no specific reason applies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "reason" in value:
        import capo_devops_agent.types.conflict_exception_reason

        out["reason"] = (
            capo_devops_agent.types.conflict_exception_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("reason") is not None:
        import capo_devops_agent.types.conflict_exception_reason

        out["reason"] = (
            capo_devops_agent.types.conflict_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devopsagent#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(
        self,
        data: ConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_json(data), message, response=response)
