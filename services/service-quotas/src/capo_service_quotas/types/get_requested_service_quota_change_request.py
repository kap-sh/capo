"""Generated from Smithy shape ``com.amazonaws.servicequotas#GetRequestedServiceQuotaChangeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_service_quotas.types.request_id


class GetRequestedServiceQuotaChangeRequest(TypedDict, closed=True):
    request_id: "capo_service_quotas.types.request_id.RequestId"
    """<p>Specifies the ID of the quota increase request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRequestedServiceQuotaChangeRequest) -> dict:
    out: dict = {}
    out["RequestId"] = value["request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRequestedServiceQuotaChangeRequest:
    out: GetRequestedServiceQuotaChangeRequest = {}  # type: ignore[typeddict-item]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    else:
        out["request_id"] = ""
    return out
