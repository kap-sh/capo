"""Generated from Smithy shape ``com.amazonaws.billing#UpdateBillingPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.billing_feature
    import capo_billing.types.billing_preferences_per_key


class UpdateBillingPreferencesRequest(TypedDict, closed=True):
    feature: "capo_billing.types.billing_feature.BillingFeature"
    """<p>The feature to update. Valid values: <code>BILLING_ALERTS</code>, <code>RI_SHARING</code>, <code>CREDIT_SHARING</code>, <code>CREDIT_LEVEL_SHARING</code>, <code>CREDIT_PREFERENCE_OPTIONS</code>. The history features (<code>RI_SHARING_HISTORY</code> and <code>CREDIT_SHARING_HISTORY</code>) are read-only and cannot be updated.</p>"""
    billing_preferences_per_key: (
        "capo_billing.types.billing_preferences_per_key.BillingPreferencesPerKey"
    )
    """<p>Key/value pairs to apply. All keys in a single request must be valid for the specified <code>feature</code> and must not be duplicated. For <code>CREDIT_PREFERENCE_OPTIONS</code>, all keys must reference the same <code>creditId</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateBillingPreferencesRequest) -> dict:
    out: dict = {}
    import capo_billing.types.billing_feature

    out["feature"] = capo_billing.types.billing_feature.serialize_aws_json_1_0(
        value["feature"]
    )
    import capo_billing.types.billing_preferences_per_key

    out["billingPreferencesPerKey"] = (
        capo_billing.types.billing_preferences_per_key.serialize_aws_json_1_0(
            value["billing_preferences_per_key"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateBillingPreferencesRequest:
    out: UpdateBillingPreferencesRequest = {}  # type: ignore[typeddict-item]
    if data.get("feature") is not None:
        import capo_billing.types.billing_feature

        out["feature"] = capo_billing.types.billing_feature.deserialize_aws_json_1_0(
            data["feature"]
        )
    else:
        import typing

        out["feature"] = typing.cast(
            "capo_billing.types.billing_feature.BillingFeature", ""
        )
    if data.get("billingPreferencesPerKey") is not None:
        import capo_billing.types.billing_preferences_per_key

        out["billing_preferences_per_key"] = (
            capo_billing.types.billing_preferences_per_key.deserialize_aws_json_1_0(
                data["billingPreferencesPerKey"]
            )
        )
    else:
        out["billing_preferences_per_key"] = []
    return out
