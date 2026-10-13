"""Generated from Smithy shape ``com.amazonaws.billingconductor#CreateCustomLineItemInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.account_id
    import capo_billingconductor.types.billing_group_arn
    import capo_billingconductor.types.client_token
    import capo_billingconductor.types.computation_rule_enum
    import capo_billingconductor.types.custom_line_item_billing_period_range
    import capo_billingconductor.types.custom_line_item_charge_details
    import capo_billingconductor.types.custom_line_item_description
    import capo_billingconductor.types.custom_line_item_name
    import capo_billingconductor.types.presentation_object
    import capo_billingconductor.types.tag_map


class CreateCustomLineItemInput(TypedDict, closed=True):
    client_token: NotRequired["capo_billingconductor.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>"""
    name: "capo_billingconductor.types.custom_line_item_name.CustomLineItemName"
    """<p> The name of the custom line item. </p>"""
    description: "capo_billingconductor.types.custom_line_item_description.CustomLineItemDescription"
    """<p> The description of the custom line item. This is shown on the Bills page in association with the charge value. </p>"""
    billing_group_arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn"
    """<p> The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to. </p>"""
    billing_period_range: NotRequired[
        "capo_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
    ]
    """<p> A time range for which the custom line item is effective. </p>"""
    tags: NotRequired["capo_billingconductor.types.tag_map.TagMap"]
    """<p> A map that contains tag keys and tag values that are attached to a custom line item. </p>"""
    charge_details: "capo_billingconductor.types.custom_line_item_charge_details.CustomLineItemChargeDetails"
    """<p> A <code>CustomLineItemChargeDetails</code> that describes the charge details for a custom line item. </p>"""
    account_id: NotRequired["capo_billingconductor.types.account_id.AccountId"]
    """<p>The Amazon Web Services account in which this custom line item will be applied to.</p>"""
    computation_rule: NotRequired[
        "capo_billingconductor.types.computation_rule_enum.ComputationRuleEnum"
    ]
    """<p> Specifies how the custom line item charges are computed. </p>"""
    presentation_details: NotRequired[
        "capo_billingconductor.types.presentation_object.PresentationObject"
    ]
    """<p> Details controlling how the custom line item charges are presented in the bill. Contains specifications for which service the charges will be shown under. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomLineItemInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    out["BillingGroupArn"] = value["billing_group_arn"]
    if "billing_period_range" in value:
        import capo_billingconductor.types.custom_line_item_billing_period_range

        out["BillingPeriodRange"] = (
            capo_billingconductor.types.custom_line_item_billing_period_range.serialize_json(
                value["billing_period_range"]
            )
        )
    if "tags" in value:
        import capo_billingconductor.types.tag_map

        out["Tags"] = capo_billingconductor.types.tag_map.serialize_json(value["tags"])
    import capo_billingconductor.types.custom_line_item_charge_details

    out["ChargeDetails"] = (
        capo_billingconductor.types.custom_line_item_charge_details.serialize_json(
            value["charge_details"]
        )
    )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "computation_rule" in value:
        import capo_billingconductor.types.computation_rule_enum

        out["ComputationRule"] = (
            capo_billingconductor.types.computation_rule_enum.serialize_json(
                value["computation_rule"]
            )
        )
    if "presentation_details" in value:
        import capo_billingconductor.types.presentation_object

        out["PresentationDetails"] = (
            capo_billingconductor.types.presentation_object.serialize_json(
                value["presentation_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateCustomLineItemInput:
    out: CreateCustomLineItemInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateCustomLineItemInput.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("CreateCustomLineItemInput.description required")
    if data.get("BillingGroupArn") is not None:
        out["billing_group_arn"] = data["BillingGroupArn"]
    else:
        raise DeserializationError(
            "CreateCustomLineItemInput.billing_group_arn required"
        )
    if data.get("BillingPeriodRange") is not None:
        import capo_billingconductor.types.custom_line_item_billing_period_range

        out["billing_period_range"] = (
            capo_billingconductor.types.custom_line_item_billing_period_range.deserialize_json(
                data["BillingPeriodRange"]
            )
        )
    if data.get("Tags") is not None:
        import capo_billingconductor.types.tag_map

        out["tags"] = capo_billingconductor.types.tag_map.deserialize_json(data["Tags"])
    if data.get("ChargeDetails") is not None:
        import capo_billingconductor.types.custom_line_item_charge_details

        out["charge_details"] = (
            capo_billingconductor.types.custom_line_item_charge_details.deserialize_json(
                data["ChargeDetails"]
            )
        )
    else:
        raise DeserializationError("CreateCustomLineItemInput.charge_details required")
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("ComputationRule") is not None:
        import capo_billingconductor.types.computation_rule_enum

        out["computation_rule"] = (
            capo_billingconductor.types.computation_rule_enum.deserialize_json(
                data["ComputationRule"]
            )
        )
    if data.get("PresentationDetails") is not None:
        import capo_billingconductor.types.presentation_object

        out["presentation_details"] = (
            capo_billingconductor.types.presentation_object.deserialize_json(
                data["PresentationDetails"]
            )
        )
    return out


def redact_sensitive(value: CreateCustomLineItemInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
