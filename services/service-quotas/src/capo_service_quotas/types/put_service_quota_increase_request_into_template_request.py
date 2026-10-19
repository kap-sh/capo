"""Generated from Smithy shape ``com.amazonaws.servicequotas#PutServiceQuotaIncreaseRequestIntoTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_service_quotas.types.aws_region
    import capo_service_quotas.types.quota_code
    import capo_service_quotas.types.quota_value
    import capo_service_quotas.types.service_code


class PutServiceQuotaIncreaseRequestIntoTemplateRequest(TypedDict, closed=True):
    quota_code: "capo_service_quotas.types.quota_code.QuotaCode"
    """<p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>"""
    service_code: "capo_service_quotas.types.service_code.ServiceCode"
    """<p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>"""
    aws_region: "capo_service_quotas.types.aws_region.AwsRegion"
    """<p>Specifies the Amazon Web Services Region to which the template applies.</p>"""
    desired_value: "capo_service_quotas.types.quota_value.QuotaValue"
    """<p>Specifies the new, increased value for the quota.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: PutServiceQuotaIncreaseRequestIntoTemplateRequest,
) -> dict:
    out: dict = {}
    out["QuotaCode"] = value["quota_code"]
    out["ServiceCode"] = value["service_code"]
    out["AwsRegion"] = value["aws_region"]
    out["DesiredValue"] = (
        "NaN"
        if value["desired_value"] != value["desired_value"]
        else "Infinity"
        if value["desired_value"] == float("inf")
        else "-Infinity"
        if value["desired_value"] == float("-inf")
        else value["desired_value"]
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> PutServiceQuotaIncreaseRequestIntoTemplateRequest:
    out: PutServiceQuotaIncreaseRequestIntoTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("QuotaCode") is not None:
        out["quota_code"] = data["QuotaCode"]
    else:
        out["quota_code"] = ""
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    else:
        out["service_code"] = ""
    if data.get("AwsRegion") is not None:
        out["aws_region"] = data["AwsRegion"]
    else:
        out["aws_region"] = ""
    if data.get("DesiredValue") is not None:
        out["desired_value"] = float(data["DesiredValue"])
    else:
        out["desired_value"] = 0.0
    return out
