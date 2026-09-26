"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#TagPolicyViolationException``."""

from typing_extensions import TypedDict

from capo_network_security_manager.errors import DeserializationError, ServiceError


class TagPolicyViolationException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: TagPolicyViolationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TagPolicyViolationException_:
    out: TagPolicyViolationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("TagPolicyViolationException_.message required")
    return out


class TagPolicyViolationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networksecuritymanager#TagPolicyViolationException``."""

    code: str | None = "TagPolicyViolationException"

    def __init__(self, data: TagPolicyViolationException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TagPolicyViolationException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "TagPolicyViolationException":
        return cls(deserialize_json(data), message)
