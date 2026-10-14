"""Generated from Smithy shape ``com.amazonaws.efs#AccessPointAlreadyExists``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_efs.types.access_point_id
    import capo_efs.types.error_code
    import capo_efs.types.error_message


class AccessPointAlreadyExists_(TypedDict, closed=True):
    error_code: "capo_efs.types.error_code.ErrorCode"
    message: NotRequired["capo_efs.types.error_message.ErrorMessage"]
    access_point_id: "capo_efs.types.access_point_id.AccessPointId"


# --- restJson1 ser/de ---
def serialize_json(value: AccessPointAlreadyExists_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    out["AccessPointId"] = value["access_point_id"]
    return out


def deserialize_json(data: dict) -> AccessPointAlreadyExists_:
    out: AccessPointAlreadyExists_ = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("AccessPointAlreadyExists_.error_code required")
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("AccessPointId") is not None:
        out["access_point_id"] = data["AccessPointId"]
    else:
        raise DeserializationError("AccessPointAlreadyExists_.access_point_id required")
    return out


class AccessPointAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#AccessPointAlreadyExists``."""

    code: str | None = "AccessPointAlreadyExists"

    def __init__(
        self,
        data: AccessPointAlreadyExists_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessPointAlreadyExists",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AccessPointAlreadyExists":
        return cls(deserialize_json(data), message, response=response)
