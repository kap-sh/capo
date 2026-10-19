"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdateBillingTransferPreferenceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.auto_transfer_billing_group_creation_preference
    import capo_billingconductor.types.client_token
    import capo_billingconductor.types.responsibility_transfer_arn


class UpdateBillingTransferPreferenceInput(TypedDict, closed=True):
    client_token: NotRequired["capo_billingconductor.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>"""
    responsibility_transfer_arn: "capo_billingconductor.types.responsibility_transfer_arn.ResponsibilityTransferArn"
    """<p>The Amazon Resource Name (ARN) of the billing transfer whose preference you want to set.</p>"""
    auto_billing_transfer_billing_group_creation: "capo_billingconductor.types.auto_transfer_billing_group_creation_preference.AutoTransferBillingGroupCreationPreference"
    """<p>The auto billing group creation preference to set for the billing transfer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBillingTransferPreferenceInput) -> dict:
    out: dict = {}
    out["ResponsibilityTransferArn"] = value["responsibility_transfer_arn"]
    import capo_billingconductor.types.auto_transfer_billing_group_creation_preference

    out["AutoBillingTransferBillingGroupCreation"] = (
        capo_billingconductor.types.auto_transfer_billing_group_creation_preference.serialize_json(
            value["auto_billing_transfer_billing_group_creation"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateBillingTransferPreferenceInput:
    out: UpdateBillingTransferPreferenceInput = {}  # type: ignore[typeddict-item]
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
            "UpdateBillingTransferPreferenceInput.auto_billing_transfer_billing_group_creation required"
        )
    return out
