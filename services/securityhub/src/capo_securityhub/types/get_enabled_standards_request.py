"""Generated from Smithy shape ``com.amazonaws.securityhub#GetEnabledStandardsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.max_results
    import capo_securityhub.types.next_token
    import capo_securityhub.types.standards_providers
    import capo_securityhub.types.standards_subscription_arns


class GetEnabledStandardsRequest(TypedDict, closed=True):
    standards_subscription_arns: NotRequired[
        "capo_securityhub.types.standards_subscription_arns.StandardsSubscriptionArns"
    ]
    """<p>The list of the standards subscription ARNs for the standards to retrieve.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The token that is required for pagination. On your first call to the <code>GetEnabledStandards</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>"""
    max_results: NotRequired["capo_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    providers: NotRequired[
        "capo_securityhub.types.standards_providers.StandardsProviders"
    ]
    """<p>A list of cloud providers to filter the enabled standards by. For example, specify <code>Azure</code> to return only enabled standards that evaluate Azure resources, or <code>GCP</code> to return only enabled standards that evaluate GCP resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnabledStandardsRequest) -> dict:
    out: dict = {}
    if "standards_subscription_arns" in value:
        import capo_securityhub.types.standards_subscription_arns

        out["StandardsSubscriptionArns"] = (
            capo_securityhub.types.standards_subscription_arns.serialize_json(
                value["standards_subscription_arns"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "providers" in value:
        import capo_securityhub.types.standards_providers

        out["Providers"] = capo_securityhub.types.standards_providers.serialize_json(
            value["providers"]
        )
    return out


def deserialize_json(data: dict) -> GetEnabledStandardsRequest:
    out: GetEnabledStandardsRequest = {}  # type: ignore[typeddict-item]
    if data.get("StandardsSubscriptionArns") is not None:
        import capo_securityhub.types.standards_subscription_arns

        out["standards_subscription_arns"] = (
            capo_securityhub.types.standards_subscription_arns.deserialize_json(
                data["StandardsSubscriptionArns"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Providers") is not None:
        import capo_securityhub.types.standards_providers

        out["providers"] = capo_securityhub.types.standards_providers.deserialize_json(
            data["Providers"]
        )
    return out
