"""Generated from Smithy shape ``com.amazonaws.billing#Investment``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError, SerializationError
from capo_billing.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_billing.types.milestone_based_investment
    import capo_billing.types.outcome_based_investment


class _Investment_milestoneBasedInvestment(TypedDict, closed=True):
    milestoneBasedInvestment: (
        "capo_billing.types.milestone_based_investment.MilestoneBasedInvestment"
    )


class _Investment_outcomeBasedInvestment(TypedDict, closed=True):
    outcomeBasedInvestment: (
        "capo_billing.types.outcome_based_investment.OutcomeBasedInvestment"
    )


Investment: TypeAlias = (
    _Investment_milestoneBasedInvestment
    | _Investment_outcomeBasedInvestment
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Investment) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Investment: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "milestoneBasedInvestment" in value:
        import capo_billing.types.milestone_based_investment

        return {
            "milestoneBasedInvestment": capo_billing.types.milestone_based_investment.serialize_aws_json_1_0(
                value["milestoneBasedInvestment"]
            )
        }
    elif "outcomeBasedInvestment" in value:
        import capo_billing.types.outcome_based_investment

        return {
            "outcomeBasedInvestment": capo_billing.types.outcome_based_investment.serialize_aws_json_1_0(
                value["outcomeBasedInvestment"]
            )
        }
    else:
        raise SerializationError("Investment: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Investment:
    if data.get("milestoneBasedInvestment") is not None:
        import capo_billing.types.milestone_based_investment

        return {
            "milestoneBasedInvestment": capo_billing.types.milestone_based_investment.deserialize_aws_json_1_0(
                data["milestoneBasedInvestment"]
            )
        }
    elif data.get("outcomeBasedInvestment") is not None:
        import capo_billing.types.outcome_based_investment

        return {
            "outcomeBasedInvestment": capo_billing.types.outcome_based_investment.deserialize_aws_json_1_0(
                data["outcomeBasedInvestment"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Investment: no recognized variant key")
