"""Generated from Smithy shape ``com.amazonaws.budgets#DeleteBudgetActionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.action
    import capo_budgets.types.budget_name


class DeleteBudgetActionResponse(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    budget_name: "capo_budgets.types.budget_name.BudgetName"
    action: "capo_budgets.types.action.Action"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBudgetActionResponse) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import capo_budgets.types.action

    out["Action"] = capo_budgets.types.action.serialize_aws_json_1_1(value["action"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBudgetActionResponse:
    out: DeleteBudgetActionResponse = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("DeleteBudgetActionResponse.account_id required")
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("DeleteBudgetActionResponse.budget_name required")
    if data.get("Action") is not None:
        import capo_budgets.types.action

        out["action"] = capo_budgets.types.action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        raise DeserializationError("DeleteBudgetActionResponse.action required")
    return out


def redact_sensitive(value: DeleteBudgetActionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "action" in value:
        import capo_budgets.types.action

        out["action"] = capo_budgets.types.action.redact_sensitive(value["action"])
    return out
