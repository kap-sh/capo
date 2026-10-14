"""Generated from Smithy shape ``com.amazonaws.rekognition#HumanLoopQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import ServiceError

if TYPE_CHECKING:
    import capo_rekognition.types.string


class HumanLoopQuotaExceededException_(TypedDict, closed=True):
    resource_type: NotRequired["capo_rekognition.types.string.String"]
    """<p>The resource type.</p>"""
    quota_code: NotRequired["capo_rekognition.types.string.String"]
    """<p>The quota code.</p>"""
    service_code: NotRequired["capo_rekognition.types.string.String"]
    """<p>The service code.</p>"""
    message: NotRequired["capo_rekognition.types.string.String"]
    code: NotRequired["capo_rekognition.types.string.String"]
    logref: NotRequired["capo_rekognition.types.string.String"]
    """<p>A universally unique identifier (UUID) for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanLoopQuotaExceededException_) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    if "logref" in value:
        out["Logref"] = value["logref"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HumanLoopQuotaExceededException_:
    out: HumanLoopQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("QuotaCode") is not None:
        out["quota_code"] = data["QuotaCode"]
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Logref") is not None:
        out["logref"] = data["Logref"]
    return out


class HumanLoopQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rekognition#HumanLoopQuotaExceededException``."""

    code: str | None = "HumanLoopQuotaExceededException"

    def __init__(
        self,
        data: HumanLoopQuotaExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="HumanLoopQuotaExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "HumanLoopQuotaExceededException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
