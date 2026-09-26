"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#InsufficientCapacityException``."""

from typing_extensions import TypedDict

from capo_lambda_microvms.errors import DeserializationError, ServiceError


class InsufficientCapacityException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: InsufficientCapacityException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InsufficientCapacityException_:
    out: InsufficientCapacityException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InsufficientCapacityException_.message required")
    return out


class InsufficientCapacityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambdamicrovms#InsufficientCapacityException``."""

    code: str | None = "InsufficientCapacityException"

    def __init__(
        self, data: InsufficientCapacityException_, message: str | None = None
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InsufficientCapacityException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "InsufficientCapacityException":
        return cls(deserialize_json(data), message)
