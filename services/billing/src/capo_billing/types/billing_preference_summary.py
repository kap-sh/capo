"""Generated from Smithy shape ``com.amazonaws.billing#BillingPreferenceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.account_id
    import capo_billing.types.account_name
    import capo_billing.types.billing_feature
    import capo_billing.types.billing_period
    import capo_billing.types.preference_key
    import capo_billing.types.preference_value


class BillingPreferenceSummary(TypedDict, closed=True):
    feature: "capo_billing.types.billing_feature.BillingFeature"
    """<p>The feature this preference belongs to.</p>"""
    key: "capo_billing.types.preference_key.PreferenceKey"
    """<p>The preference key. Format depends on the feature.</p>"""
    value: "capo_billing.types.preference_value.PreferenceValue"
    """<p>The preference value. Valid values: <code>ENABLED</code> or <code>DISABLED</code>.</p>"""
    account_name: NotRequired["capo_billing.types.account_name.AccountName"]
    """<p>The display name of the account. Populated together with <code>accountId</code>; <code>null</code> otherwise.</p>"""
    account_id: NotRequired["capo_billing.types.account_id.AccountId"]
    """<p>The associated Amazon Web Services account ID. Populated for account-list keys; <code>null</code> otherwise.</p>"""
    billing_period: NotRequired["capo_billing.types.billing_period.BillingPeriod"]
    """<p>The billing period associated with the preference change. Populated only for the history features <code>RI_SHARING_HISTORY</code> and <code>CREDIT_SHARING_HISTORY</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingPreferenceSummary) -> dict:
    out: dict = {}
    import capo_billing.types.billing_feature

    out["feature"] = capo_billing.types.billing_feature.serialize_aws_json_1_0(
        value["feature"]
    )
    out["key"] = value["key"]
    import capo_billing.types.preference_value

    out["value"] = capo_billing.types.preference_value.serialize_aws_json_1_0(
        value["value"]
    )
    if "account_name" in value:
        out["accountName"] = value["account_name"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "billing_period" in value:
        import capo_billing.types.billing_period

        out["billingPeriod"] = capo_billing.types.billing_period.serialize_aws_json_1_0(
            value["billing_period"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingPreferenceSummary:
    out: BillingPreferenceSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        import capo_billing.types.preference_value

        out["value"] = capo_billing.types.preference_value.deserialize_aws_json_1_0(
            data["value"]
        )
    else:
        import typing

        out["value"] = typing.cast(
            "capo_billing.types.preference_value.PreferenceValue", ""
        )
    if data.get("accountName") is not None:
        out["account_name"] = data["accountName"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("billingPeriod") is not None:
        import capo_billing.types.billing_period

        out["billing_period"] = (
            capo_billing.types.billing_period.deserialize_aws_json_1_0(
                data["billingPeriod"]
            )
        )
    return out
