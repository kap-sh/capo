"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#ServiceLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_route53_recovery_cluster.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.string


class ServiceLimitExceededException_(TypedDict, closed=True):
    message: "capo_route53_recovery_cluster.types.string.String"
    resource_id: NotRequired["capo_route53_recovery_cluster.types.string.String"]
    """<p>The resource identifier of the limit that was exceeded.</p>"""
    resource_type: NotRequired["capo_route53_recovery_cluster.types.string.String"]
    """<p>The resource type of the limit that was exceeded.</p>"""
    limit_code: "capo_route53_recovery_cluster.types.string.String"
    """<p>The code of the limit that was exceeded.</p>"""
    service_code: "capo_route53_recovery_cluster.types.string.String"
    """<p>The service code of the limit that was exceeded.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceLimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    out["limitCode"] = value["limit_code"]
    out["serviceCode"] = value["service_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceLimitExceededException_:
    out: ServiceLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServiceLimitExceededException_.message required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("limitCode") is not None:
        out["limit_code"] = data["limitCode"]
    else:
        raise DeserializationError("ServiceLimitExceededException_.limit_code required")
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    else:
        raise DeserializationError(
            "ServiceLimitExceededException_.service_code required"
        )
    return out


class ServiceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53recoverycluster#ServiceLimitExceededException``."""

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
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceLimitExceededException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
