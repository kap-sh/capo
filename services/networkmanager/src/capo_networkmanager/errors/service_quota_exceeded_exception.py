"""Generated from Smithy shape ``com.amazonaws.networkmanager#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_networkmanager.errors import ServiceError

if TYPE_CHECKING:
    import capo_networkmanager.types.server_side_string


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_networkmanager.types.server_side_string.ServerSideString"
    """<p>The error message.</p>"""
    resource_id: NotRequired[
        "capo_networkmanager.types.server_side_string.ServerSideString"
    ]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired[
        "capo_networkmanager.types.server_side_string.ServerSideString"
    ]
    """<p>The resource type.</p>"""
    limit_code: "capo_networkmanager.types.server_side_string.ServerSideString"
    """<p>The limit code.</p>"""
    service_code: "capo_networkmanager.types.server_side_string.ServerSideString"
    """<p>The service code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    out["LimitCode"] = value["limit_code"]
    out["ServiceCode"] = value["service_code"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("LimitCode") is not None:
        out["limit_code"] = data["LimitCode"]
    else:
        out["limit_code"] = ""
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    else:
        out["service_code"] = ""
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networkmanager#ServiceQuotaExceededException``."""

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
