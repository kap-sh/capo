"""Generated from Smithy shape ``com.amazonaws.billing#GetBillingPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.billing_feature_filters
    import capo_billing.types.billing_features
    import capo_billing.types.page_token


class GetBillingPreferencesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>Pagination token from a previous response. Pass the value returned in <code>nextToken</code> to retrieve the next page of results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of records to return per page. Range: 1 to 50. Default: 50.</p>"""
    features: "capo_billing.types.billing_features.BillingFeatures"
    """<p>The feature to retrieve. Specify exactly one value. Valid values: <code>BILLING_ALERTS</code>, <code>RI_SHARING</code>, <code>RI_SHARING_HISTORY</code>, <code>CREDIT_SHARING</code>, <code>CREDIT_SHARING_HISTORY</code>, <code>CREDIT_LEVEL_SHARING</code>, <code>CREDIT_PREFERENCE_OPTIONS</code>.</p>"""
    filters: NotRequired[
        "capo_billing.types.billing_feature_filters.BillingFeatureFilters"
    ]
    """<p>Filters to narrow results. Specify exactly one filter when supplied. The supported filter name is <code>PREFERENCE_KEY</code>, which accepts 1 to 10 values to match preference keys.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBillingPreferencesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    import capo_billing.types.billing_features

    out["features"] = capo_billing.types.billing_features.serialize_aws_json_1_0(
        value["features"]
    )
    if "filters" in value:
        import capo_billing.types.billing_feature_filters

        out["filters"] = (
            capo_billing.types.billing_feature_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBillingPreferencesRequest:
    out: GetBillingPreferencesRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("features") is not None:
        import capo_billing.types.billing_features

        out["features"] = capo_billing.types.billing_features.deserialize_aws_json_1_0(
            data["features"]
        )
    else:
        out["features"] = []
    if data.get("filters") is not None:
        import capo_billing.types.billing_feature_filters

        out["filters"] = (
            capo_billing.types.billing_feature_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    return out
