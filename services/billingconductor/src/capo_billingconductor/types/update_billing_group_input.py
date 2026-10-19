"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdateBillingGroupInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_group_arn
    import capo_billingconductor.types.billing_group_description
    import capo_billingconductor.types.billing_group_name
    import capo_billingconductor.types.billing_group_status
    import capo_billingconductor.types.computation_preference
    import capo_billingconductor.types.update_billing_group_account_grouping


class UpdateBillingGroupInput(TypedDict, closed=True):
    arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn"
    """<p>The Amazon Resource Name (ARN) of the billing group being updated. </p>"""
    name: NotRequired["capo_billingconductor.types.billing_group_name.BillingGroupName"]
    """<p>The name of the billing group. The names must be unique to each billing group. </p>"""
    status: NotRequired[
        "capo_billingconductor.types.billing_group_status.BillingGroupStatus"
    ]
    """<p>The status of the billing group. Only one of the valid values can be used. </p>"""
    computation_preference: NotRequired[
        "capo_billingconductor.types.computation_preference.ComputationPreference"
    ]
    """<p> The preferences and settings that will be used to compute the Amazon Web Services charges for a billing group. </p>"""
    description: NotRequired[
        "capo_billingconductor.types.billing_group_description.BillingGroupDescription"
    ]
    """<p>A description of the billing group. </p>"""
    account_grouping: NotRequired[
        "capo_billingconductor.types.update_billing_group_account_grouping.UpdateBillingGroupAccountGrouping"
    ]
    """<p>Specifies if the billing group has automatic account association (<code>AutoAssociate</code>) enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBillingGroupInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_billingconductor.types.billing_group_status

        out["Status"] = capo_billingconductor.types.billing_group_status.serialize_json(
            value["status"]
        )
    if "computation_preference" in value:
        import capo_billingconductor.types.computation_preference

        out["ComputationPreference"] = (
            capo_billingconductor.types.computation_preference.serialize_json(
                value["computation_preference"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "account_grouping" in value:
        import capo_billingconductor.types.update_billing_group_account_grouping

        out["AccountGrouping"] = (
            capo_billingconductor.types.update_billing_group_account_grouping.serialize_json(
                value["account_grouping"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBillingGroupInput:
    out: UpdateBillingGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_billingconductor.types.billing_group_status

        out["status"] = (
            capo_billingconductor.types.billing_group_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("ComputationPreference") is not None:
        import capo_billingconductor.types.computation_preference

        out["computation_preference"] = (
            capo_billingconductor.types.computation_preference.deserialize_json(
                data["ComputationPreference"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AccountGrouping") is not None:
        import capo_billingconductor.types.update_billing_group_account_grouping

        out["account_grouping"] = (
            capo_billingconductor.types.update_billing_group_account_grouping.deserialize_json(
                data["AccountGrouping"]
            )
        )
    return out


def redact_sensitive(value: UpdateBillingGroupInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
