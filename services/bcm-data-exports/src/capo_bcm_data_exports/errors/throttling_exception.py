"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_bcm_data_exports.errors import ServiceError

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.generic_string


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_bcm_data_exports.types.generic_string.GenericString"
    quota_code: NotRequired["capo_bcm_data_exports.types.generic_string.GenericString"]
    """<p>The quota code that exceeded the throttling limit.</p>"""
    service_code: NotRequired[
        "capo_bcm_data_exports.types.generic_string.GenericString"
    ]
    """<p>The service code that exceeded the throttling limit. It will always be “AWSBillingAndCostManagementDataExports”.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("QuotaCode") is not None:
        out["quota_code"] = data["QuotaCode"]
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bcmdataexports#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
