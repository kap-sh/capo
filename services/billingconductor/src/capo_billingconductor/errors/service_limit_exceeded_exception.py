"""Generated from Smithy shape ``com.amazonaws.billingconductor#ServiceLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_billingconductor.errors import ServiceError

if TYPE_CHECKING:
    import capo_billingconductor.types.string


class ServiceLimitExceededException_(TypedDict, closed=True):
    message: "capo_billingconductor.types.string.String"
    resource_id: NotRequired["capo_billingconductor.types.string.String"]
    """<p>Identifier of the resource affected. </p>"""
    resource_type: NotRequired["capo_billingconductor.types.string.String"]
    """<p>Type of the resource affected. </p>"""
    limit_code: "capo_billingconductor.types.string.String"
    """<p>The unique code identifier of the service limit that is being exceeded. </p>"""
    service_code: "capo_billingconductor.types.string.String"
    """<p>The unique code for the service of the limit that is being exceeded. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLimitExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    out["LimitCode"] = value["limit_code"]
    out["ServiceCode"] = value["service_code"]
    return out


def deserialize_json(data: dict) -> ServiceLimitExceededException_:
    out: ServiceLimitExceededException_ = {}  # type: ignore[typeddict-item]
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


class ServiceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.billingconductor#ServiceLimitExceededException``."""

    code: str | None = "ServiceLimitExceededException"

    def __init__(
        self,
        data: ServiceLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceLimitExceededException":
        return cls(deserialize_json(data), message, response=response)
