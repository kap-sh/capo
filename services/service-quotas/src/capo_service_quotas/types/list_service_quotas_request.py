"""Generated from Smithy shape ``com.amazonaws.servicequotas#ListServiceQuotasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_quotas.types.applied_level_enum
    import capo_service_quotas.types.max_results
    import capo_service_quotas.types.next_token
    import capo_service_quotas.types.quota_code
    import capo_service_quotas.types.service_code


class ListServiceQuotasRequest(TypedDict, closed=True):
    service_code: "capo_service_quotas.types.service_code.ServiceCode"
    """<p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>"""
    next_token: NotRequired["capo_service_quotas.types.next_token.NextToken"]
    """<p>Specifies a value for receiving additional results after you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>"""
    max_results: NotRequired["capo_service_quotas.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>"""
    quota_code: NotRequired["capo_service_quotas.types.quota_code.QuotaCode"]
    """<p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>"""
    quota_applied_at_level: NotRequired[
        "capo_service_quotas.types.applied_level_enum.AppliedLevelEnum"
    ]
    """<p>Filters the response to return applied quota values for the <code>ACCOUNT</code>, <code>RESOURCE</code>, or <code>ALL</code> levels. <code>ACCOUNT</code> is the default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServiceQuotasRequest) -> dict:
    out: dict = {}
    out["ServiceCode"] = value["service_code"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "quota_applied_at_level" in value:
        import capo_service_quotas.types.applied_level_enum

        out["QuotaAppliedAtLevel"] = (
            capo_service_quotas.types.applied_level_enum.serialize_aws_json_1_1(
                value["quota_applied_at_level"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServiceQuotasRequest:
    out: ListServiceQuotasRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    else:
        out["service_code"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("QuotaCode") is not None:
        out["quota_code"] = data["QuotaCode"]
    if data.get("QuotaAppliedAtLevel") is not None:
        import capo_service_quotas.types.applied_level_enum

        out["quota_applied_at_level"] = (
            capo_service_quotas.types.applied_level_enum.deserialize_aws_json_1_1(
                data["QuotaAppliedAtLevel"]
            )
        )
    return out
