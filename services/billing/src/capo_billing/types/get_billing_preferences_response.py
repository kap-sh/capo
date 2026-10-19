"""Generated from Smithy shape ``com.amazonaws.billing#GetBillingPreferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.billing_preferences
    import capo_billing.types.page_token


class GetBillingPreferencesResponse(TypedDict, closed=True):
    billing_preferences: "capo_billing.types.billing_preferences.BillingPreferences"
    """<p>The list of preference entries matching the request.</p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>Pagination token. Present when more pages are available; <code>null</code> when there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBillingPreferencesResponse) -> dict:
    out: dict = {}
    import capo_billing.types.billing_preferences

    out["billingPreferences"] = (
        capo_billing.types.billing_preferences.serialize_aws_json_1_0(
            value["billing_preferences"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBillingPreferencesResponse:
    out: GetBillingPreferencesResponse = {}  # type: ignore[typeddict-item]
    if data.get("billingPreferences") is not None:
        import capo_billing.types.billing_preferences

        out["billing_preferences"] = (
            capo_billing.types.billing_preferences.deserialize_aws_json_1_0(
                data["billingPreferences"]
            )
        )
    else:
        out["billing_preferences"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
