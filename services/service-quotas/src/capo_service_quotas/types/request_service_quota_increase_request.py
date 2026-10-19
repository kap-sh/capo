"""Generated from Smithy shape ``com.amazonaws.servicequotas#RequestServiceQuotaIncreaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_quotas.types.quota_code
    import capo_service_quotas.types.quota_context_id
    import capo_service_quotas.types.quota_value
    import capo_service_quotas.types.service_code
    import capo_service_quotas.types.support_case_allowed


class RequestServiceQuotaIncreaseRequest(TypedDict, closed=True):
    service_code: "capo_service_quotas.types.service_code.ServiceCode"
    """<p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>"""
    quota_code: "capo_service_quotas.types.quota_code.QuotaCode"
    """<p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>"""
    desired_value: "capo_service_quotas.types.quota_value.QuotaValue"
    """<p>Specifies the new, increased value for the quota.</p>"""
    context_id: NotRequired["capo_service_quotas.types.quota_context_id.QuotaContextId"]
    """<p>Specifies the resource with an Amazon Resource Name (ARN).</p>"""
    support_case_allowed: NotRequired[
        "capo_service_quotas.types.support_case_allowed.SupportCaseAllowed"
    ]
    """<p>Specifies if an Amazon Web Services Support case can be opened for the quota increase request. This parameter is optional. </p> <p>By default, this flag is set to <code>True</code> and Amazon Web Services may create a support case for some quota increase requests. You can set this flag to <code>False</code> if you do not want a support case created when you request a quota increase. If you set the flag to <code>False</code>, Amazon Web Services does not open a support case and updates the request status to <code>Not approved</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestServiceQuotaIncreaseRequest) -> dict:
    out: dict = {}
    out["ServiceCode"] = value["service_code"]
    out["QuotaCode"] = value["quota_code"]
    out["DesiredValue"] = (
        "NaN"
        if value["desired_value"] != value["desired_value"]
        else "Infinity"
        if value["desired_value"] == float("inf")
        else "-Infinity"
        if value["desired_value"] == float("-inf")
        else value["desired_value"]
    )
    if "context_id" in value:
        out["ContextId"] = value["context_id"]
    if "support_case_allowed" in value:
        out["SupportCaseAllowed"] = value["support_case_allowed"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestServiceQuotaIncreaseRequest:
    out: RequestServiceQuotaIncreaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    else:
        out["service_code"] = ""
    if data.get("QuotaCode") is not None:
        out["quota_code"] = data["QuotaCode"]
    else:
        out["quota_code"] = ""
    if data.get("DesiredValue") is not None:
        out["desired_value"] = float(data["DesiredValue"])
    else:
        out["desired_value"] = 0.0
    if data.get("ContextId") is not None:
        out["context_id"] = data["ContextId"]
    if data.get("SupportCaseAllowed") is not None:
        out["support_case_allowed"] = data["SupportCaseAllowed"]
    return out
