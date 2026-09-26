"""Generated from Smithy shape ``com.amazonaws.accountaccess#AlreadyCreatedException``."""

from typing_extensions import NotRequired, TypedDict

from capo_account_access.errors import ServiceError


class AlreadyCreatedException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: AlreadyCreatedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AlreadyCreatedException_:
    out: AlreadyCreatedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class AlreadyCreatedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.accountaccess#AlreadyCreatedException``."""

    code: str | None = "AlreadyCreatedException"

    def __init__(self, data: AlreadyCreatedException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AlreadyCreatedException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "AlreadyCreatedException":
        return cls(deserialize_json(data), message)
