"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ServiceLinkedRoleLockClientException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_migrationhubstrategy.errors import ServiceError

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.error_message


class ServiceLinkedRoleLockClientException_(TypedDict, closed=True):
    message: NotRequired["capo_migrationhubstrategy.types.error_message.errorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLinkedRoleLockClientException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceLinkedRoleLockClientException_:
    out: ServiceLinkedRoleLockClientException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ServiceLinkedRoleLockClientException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhubstrategy#ServiceLinkedRoleLockClientException``."""

    code: str | None = "ServiceLinkedRoleLockClientException"

    def __init__(
        self,
        data: ServiceLinkedRoleLockClientException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceLinkedRoleLockClientException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceLinkedRoleLockClientException":
        return cls(deserialize_json(data), message, response=response)
