"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetActionsForBudgetResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.actions
    import capo_budgets.types.generic_string


class DescribeBudgetActionsForBudgetResponse(TypedDict, closed=True):
    actions: "capo_budgets.types.actions.Actions"
    """<p> A list of the budget action resources information. </p>"""
    next_token: NotRequired["capo_budgets.types.generic_string.GenericString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetActionsForBudgetResponse) -> dict:
    out: dict = {}
    import capo_budgets.types.actions

    out["Actions"] = capo_budgets.types.actions.serialize_aws_json_1_1(value["actions"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetActionsForBudgetResponse:
    out: DescribeBudgetActionsForBudgetResponse = {}  # type: ignore[typeddict-item]
    if data.get("Actions") is not None:
        import capo_budgets.types.actions

        out["actions"] = capo_budgets.types.actions.deserialize_aws_json_1_1(
            data["Actions"]
        )
    else:
        raise DeserializationError(
            "DescribeBudgetActionsForBudgetResponse.actions required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeBudgetActionsForBudgetResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "actions" in value:
        import capo_budgets.types.actions

        out["actions"] = capo_budgets.types.actions.redact_sensitive(value["actions"])
    return out
