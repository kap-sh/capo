"""Generated from Smithy shape ``com.amazonaws.budgets#UpdateBudgetActionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.action
    import capo_budgets.types.budget_name


class UpdateBudgetActionResponse(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    budget_name: "capo_budgets.types.budget_name.BudgetName"
    old_action: "capo_budgets.types.action.Action"
    """<p> The previous action resource information. </p>"""
    new_action: "capo_budgets.types.action.Action"
    """<p> The updated action resource information. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBudgetActionResponse) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import capo_budgets.types.action

    out["OldAction"] = capo_budgets.types.action.serialize_aws_json_1_1(
        value["old_action"]
    )
    import capo_budgets.types.action

    out["NewAction"] = capo_budgets.types.action.serialize_aws_json_1_1(
        value["new_action"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBudgetActionResponse:
    out: UpdateBudgetActionResponse = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    else:
        out["budget_name"] = ""
    if data.get("OldAction") is not None:
        import capo_budgets.types.action

        out["old_action"] = capo_budgets.types.action.deserialize_aws_json_1_1(
            data["OldAction"]
        )
    else:
        raise DeserializationError("UpdateBudgetActionResponse.old_action required")
    if data.get("NewAction") is not None:
        import capo_budgets.types.action

        out["new_action"] = capo_budgets.types.action.deserialize_aws_json_1_1(
            data["NewAction"]
        )
    else:
        raise DeserializationError("UpdateBudgetActionResponse.new_action required")
    return out


def redact_sensitive(value: UpdateBudgetActionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "old_action" in value:
        import capo_budgets.types.action

        out["old_action"] = capo_budgets.types.action.redact_sensitive(
            value["old_action"]
        )
    if "new_action" in value:
        import capo_budgets.types.action

        out["new_action"] = capo_budgets.types.action.redact_sensitive(
            value["new_action"]
        )
    return out
