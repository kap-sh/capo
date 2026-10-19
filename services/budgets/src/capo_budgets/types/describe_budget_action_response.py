"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetActionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.action
    import capo_budgets.types.budget_name


class DescribeBudgetActionResponse(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    budget_name: "capo_budgets.types.budget_name.BudgetName"
    action: "capo_budgets.types.action.Action"
    """<p> A budget action resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetActionResponse) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import capo_budgets.types.action

    out["Action"] = capo_budgets.types.action.serialize_aws_json_1_1(value["action"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetActionResponse:
    out: DescribeBudgetActionResponse = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    else:
        out["budget_name"] = ""
    if data.get("Action") is not None:
        import capo_budgets.types.action

        out["action"] = capo_budgets.types.action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        raise DeserializationError("DescribeBudgetActionResponse.action required")
    return out


def redact_sensitive(value: DescribeBudgetActionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "action" in value:
        import capo_budgets.types.action

        out["action"] = capo_budgets.types.action.redact_sensitive(value["action"])
    return out
