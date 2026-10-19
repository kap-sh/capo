"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdateBillingTransferPreferenceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.auto_transfer_billing_group_creation_preference
    import capo_billingconductor.types.instant
    import capo_billingconductor.types.responsibility_transfer_arn


class UpdateBillingTransferPreferenceOutput(TypedDict, closed=True):
    responsibility_transfer_arn: "capo_billingconductor.types.responsibility_transfer_arn.ResponsibilityTransferArn"
    """<p>The Amazon Resource Name (ARN) of the billing transfer that the preference applies to.</p>"""
    auto_billing_transfer_billing_group_creation: "capo_billingconductor.types.auto_transfer_billing_group_creation_preference.AutoTransferBillingGroupCreationPreference"
    """<p>The updated auto billing group creation preference for the billing transfer.</p>"""
    last_modified_time: "capo_billingconductor.types.instant.Instant"
    """<p>The most recent time when the preference was modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBillingTransferPreferenceOutput) -> dict:
    out: dict = {}
    out["ResponsibilityTransferArn"] = value["responsibility_transfer_arn"]
    import capo_billingconductor.types.auto_transfer_billing_group_creation_preference

    out["AutoBillingTransferBillingGroupCreation"] = (
        capo_billingconductor.types.auto_transfer_billing_group_creation_preference.serialize_json(
            value["auto_billing_transfer_billing_group_creation"]
        )
    )
    out["LastModifiedTime"] = value.get("last_modified_time", 0)
    return out


def deserialize_json(data: dict) -> UpdateBillingTransferPreferenceOutput:
    out: UpdateBillingTransferPreferenceOutput = {}  # type: ignore[typeddict-item]
    if data.get("ResponsibilityTransferArn") is not None:
        out["responsibility_transfer_arn"] = data["ResponsibilityTransferArn"]
    else:
        out["responsibility_transfer_arn"] = ""
    if data.get("AutoBillingTransferBillingGroupCreation") is not None:
        import capo_billingconductor.types.auto_transfer_billing_group_creation_preference

        out["auto_billing_transfer_billing_group_creation"] = (
            capo_billingconductor.types.auto_transfer_billing_group_creation_preference.deserialize_json(
                data["AutoBillingTransferBillingGroupCreation"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateBillingTransferPreferenceOutput.auto_billing_transfer_billing_group_creation required"
        )
    if data.get("LastModifiedTime") is not None:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    return out
