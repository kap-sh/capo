"""Generated from Smithy shape ``com.amazonaws.billing#UpdateBillingPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.billing_feature
    import capo_billing.types.billing_preferences_per_key


class UpdateBillingPreferencesRequest(TypedDict, closed=True):
    feature: "capo_billing.types.billing_feature.BillingFeature"
    """<p>The feature to update. Valid values: <code>BILLING_ALERTS</code>, <code>RI_SHARING</code>, <code>CREDIT_SHARING</code>, <code>CREDIT_LEVEL_SHARING</code>, <code>CREDIT_PREFERENCE_OPTIONS</code>, <code>BENEFIT_LEVEL_SHARING</code>. The history features (<code>RI_SHARING_HISTORY</code> and <code>CREDIT_SHARING_HISTORY</code>) are read-only and cannot be updated.</p>"""
    billing_preferences_per_key: (
        "capo_billing.types.billing_preferences_per_key.BillingPreferencesPerKey"
    )
    """<p>Key/value pairs to apply. All keys in a single request must be valid for the specified <code>feature</code> and must not be duplicated. For <code>CREDIT_PREFERENCE_OPTIONS</code>, all keys must reference the same <code>creditId</code>.</p> <p>For <code>BENEFIT_LEVEL_SHARING</code>, all keys must reference the same Reserved Instance or Savings Plan. To share it with the accounts in one Cost Category rule, send these three keys with the value <code>ENABLED</code>:</p> <ul> <li> <p> <code>benefit/{ri|sp}/{benefitId}/sharing/costCategoryArn/{costCategoryArn}</code> </p> </li> <li> <p> <code>benefit/{ri|sp}/{benefitId}/sharing/ruleName/{ruleName}</code> </p> </li> <li> <p> <code>benefit/{ri|sp}/{benefitId}/sharing/mode/{prioritized|restricted}</code> </p> </li> </ul> <p>With <code>prioritized</code>, any benefit that the rule's accounts don't use goes to the rest of your consolidated billing family, following your family sharing settings. With <code>restricted</code>, only the owner and the rule's accounts receive it. The Cost Category must belong to your account. To stop sharing, send the same three keys with the value <code>DISABLED</code>.</p> <p>For <code>RI_SHARING</code> and <code>CREDIT_SHARING</code>, you can share benefits by account group. Each rule in a Cost Category is one group. Send exactly one of these group keys with the value <code>ENABLED</code>:</p> <ul> <li> <p> <code>open-sharing</code> - Share across the whole consolidated billing family, with no groups.</p> </li> <li> <p> <code>costcategory-prioritized/{costCategoryArn}</code> - Share within each group first, then with the rest of the family.</p> </li> <li> <p> <code>costcategory-restricted/{costCategoryArn}</code> - An account in a group shares only with accounts in the same group.</p> </li> </ul> <p>For <code>RI_SHARING</code>, the <code>costcategory-</code> keys use a Cost Category that supports the <code>billing:rispgroupsharing</code> resource type. To use a Cost Category that supports the <code>billing:benefitgroupsharing</code> resource type, use the <code>benefitgroup-prioritized/</code> or <code>benefitgroup-restricted/</code> prefix instead. For <code>CREDIT_SHARING</code>, the Cost Category must support the <code>billing:benefitgroupsharing</code> resource type. The Cost Category must belong to your account. <code>GetBillingPreferences</code> returns the group key that is in effect.</p>"""


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
