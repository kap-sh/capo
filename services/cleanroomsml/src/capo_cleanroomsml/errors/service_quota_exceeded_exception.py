"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ServiceQuotaExceededException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import ServiceError


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"
    quota_name: NotRequired["str"]
    """The name of the service quota limit that was exceeded"""
    quota_value: NotRequired["float"]
    """The current limit on the service quota that was exceeded"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "quota_name" in value:
        out["quotaName"] = value["quota_name"]
    if "quota_value" in value:
        out["quotaValue"] = (
            "NaN"
            if value["quota_value"] != value["quota_value"]
            else "Infinity"
            if value["quota_value"] == float("inf")
            else "-Infinity"
            if value["quota_value"] == float("-inf")
            else value["quota_value"]
        )
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("quotaName") is not None:
        out["quota_name"] = data["quotaName"]
    if data.get("quotaValue") is not None:
        out["quota_value"] = float(data["quotaValue"])
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cleanroomsml#ServiceQuotaExceededException``."""

    code: str | None = "ServiceQuotaExceededException"

    def __init__(
        self,
        data: ServiceQuotaExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceQuotaExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceQuotaExceededException":
        return cls(deserialize_json(data), message, response=response)
