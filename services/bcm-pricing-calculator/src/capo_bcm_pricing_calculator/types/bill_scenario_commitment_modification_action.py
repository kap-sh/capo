"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillScenarioCommitmentModificationAction``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError, SerializationError
from capo_bcm_pricing_calculator.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.add_reserved_instance_action
    import capo_bcm_pricing_calculator.types.add_savings_plan_action
    import capo_bcm_pricing_calculator.types.negate_reserved_instance_action
    import capo_bcm_pricing_calculator.types.negate_savings_plan_action


class _BillScenarioCommitmentModificationAction_addReservedInstanceAction(
    TypedDict, closed=True
):
    addReservedInstanceAction: "capo_bcm_pricing_calculator.types.add_reserved_instance_action.AddReservedInstanceAction"


class _BillScenarioCommitmentModificationAction_addSavingsPlanAction(
    TypedDict, closed=True
):
    addSavingsPlanAction: (
        "capo_bcm_pricing_calculator.types.add_savings_plan_action.AddSavingsPlanAction"
    )


class _BillScenarioCommitmentModificationAction_negateReservedInstanceAction(
    TypedDict, closed=True
):
    negateReservedInstanceAction: "capo_bcm_pricing_calculator.types.negate_reserved_instance_action.NegateReservedInstanceAction"


class _BillScenarioCommitmentModificationAction_negateSavingsPlanAction(
    TypedDict, closed=True
):
    negateSavingsPlanAction: "capo_bcm_pricing_calculator.types.negate_savings_plan_action.NegateSavingsPlanAction"


BillScenarioCommitmentModificationAction: TypeAlias = (
    _BillScenarioCommitmentModificationAction_addReservedInstanceAction
    | _BillScenarioCommitmentModificationAction_addSavingsPlanAction
    | _BillScenarioCommitmentModificationAction_negateReservedInstanceAction
    | _BillScenarioCommitmentModificationAction_negateSavingsPlanAction
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillScenarioCommitmentModificationAction) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"BillScenarioCommitmentModificationAction: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "addReservedInstanceAction" in value:
        import capo_bcm_pricing_calculator.types.add_reserved_instance_action

        return {
            "addReservedInstanceAction": capo_bcm_pricing_calculator.types.add_reserved_instance_action.serialize_aws_json_1_0(
                value["addReservedInstanceAction"]
            )
        }
    elif "addSavingsPlanAction" in value:
        import capo_bcm_pricing_calculator.types.add_savings_plan_action

        return {
            "addSavingsPlanAction": capo_bcm_pricing_calculator.types.add_savings_plan_action.serialize_aws_json_1_0(
                value["addSavingsPlanAction"]
            )
        }
    elif "negateReservedInstanceAction" in value:
        import capo_bcm_pricing_calculator.types.negate_reserved_instance_action

        return {
            "negateReservedInstanceAction": capo_bcm_pricing_calculator.types.negate_reserved_instance_action.serialize_aws_json_1_0(
                value["negateReservedInstanceAction"]
            )
        }
    elif "negateSavingsPlanAction" in value:
        import capo_bcm_pricing_calculator.types.negate_savings_plan_action

        return {
            "negateSavingsPlanAction": capo_bcm_pricing_calculator.types.negate_savings_plan_action.serialize_aws_json_1_0(
                value["negateSavingsPlanAction"]
            )
        }
    else:
        raise SerializationError(
            "BillScenarioCommitmentModificationAction: no variant present"
        )


def deserialize_aws_json_1_0(data: dict) -> BillScenarioCommitmentModificationAction:
    if data.get("addReservedInstanceAction") is not None:
        import capo_bcm_pricing_calculator.types.add_reserved_instance_action

        return {
            "addReservedInstanceAction": capo_bcm_pricing_calculator.types.add_reserved_instance_action.deserialize_aws_json_1_0(
                data["addReservedInstanceAction"]
            )
        }
    elif data.get("addSavingsPlanAction") is not None:
        import capo_bcm_pricing_calculator.types.add_savings_plan_action

        return {
            "addSavingsPlanAction": capo_bcm_pricing_calculator.types.add_savings_plan_action.deserialize_aws_json_1_0(
                data["addSavingsPlanAction"]
            )
        }
    elif data.get("negateReservedInstanceAction") is not None:
        import capo_bcm_pricing_calculator.types.negate_reserved_instance_action

        return {
            "negateReservedInstanceAction": capo_bcm_pricing_calculator.types.negate_reserved_instance_action.deserialize_aws_json_1_0(
                data["negateReservedInstanceAction"]
            )
        }
    elif data.get("negateSavingsPlanAction") is not None:
        import capo_bcm_pricing_calculator.types.negate_savings_plan_action

        return {
            "negateSavingsPlanAction": capo_bcm_pricing_calculator.types.negate_savings_plan_action.deserialize_aws_json_1_0(
                data["negateSavingsPlanAction"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "BillScenarioCommitmentModificationAction: no recognized variant key"
        )
