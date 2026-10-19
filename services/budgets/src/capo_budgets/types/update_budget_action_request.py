"""Generated from Smithy shape ``com.amazonaws.budgets#UpdateBudgetActionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.action_id
    import capo_budgets.types.action_threshold
    import capo_budgets.types.approval_model
    import capo_budgets.types.budget_name
    import capo_budgets.types.definition
    import capo_budgets.types.notification_type
    import capo_budgets.types.role_arn
    import capo_budgets.types.subscribers


class UpdateBudgetActionRequest(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    budget_name: "capo_budgets.types.budget_name.BudgetName"
    action_id: "capo_budgets.types.action_id.ActionId"
    """<p> A system-generated universally unique identifier (UUID) for the action. </p>"""
    notification_type: NotRequired[
        "capo_budgets.types.notification_type.NotificationType"
    ]
    action_threshold: NotRequired["capo_budgets.types.action_threshold.ActionThreshold"]
    definition: NotRequired["capo_budgets.types.definition.Definition"]
    execution_role_arn: NotRequired["capo_budgets.types.role_arn.RoleArn"]
    """<p> The role passed for action execution and reversion. Roles and actions must be in the same account. </p>"""
    approval_model: NotRequired["capo_budgets.types.approval_model.ApprovalModel"]
    """<p> This specifies if the action needs manual or automatic approval. </p>"""
    subscribers: NotRequired["capo_budgets.types.subscribers.Subscribers"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBudgetActionRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    out["ActionId"] = value["action_id"]
    if "notification_type" in value:
        import capo_budgets.types.notification_type

        out["NotificationType"] = (
            capo_budgets.types.notification_type.serialize_aws_json_1_1(
                value["notification_type"]
            )
        )
    if "action_threshold" in value:
        import capo_budgets.types.action_threshold

        out["ActionThreshold"] = (
            capo_budgets.types.action_threshold.serialize_aws_json_1_1(
                value["action_threshold"]
            )
        )
    if "definition" in value:
        import capo_budgets.types.definition

        out["Definition"] = capo_budgets.types.definition.serialize_aws_json_1_1(
            value["definition"]
        )
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "approval_model" in value:
        import capo_budgets.types.approval_model

        out["ApprovalModel"] = capo_budgets.types.approval_model.serialize_aws_json_1_1(
            value["approval_model"]
        )
    if "subscribers" in value:
        import capo_budgets.types.subscribers

        out["Subscribers"] = capo_budgets.types.subscribers.serialize_aws_json_1_1(
            value["subscribers"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBudgetActionRequest:
    out: UpdateBudgetActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    else:
        out["budget_name"] = ""
    if data.get("ActionId") is not None:
        out["action_id"] = data["ActionId"]
    else:
        out["action_id"] = ""
    if data.get("NotificationType") is not None:
        import capo_budgets.types.notification_type

        out["notification_type"] = (
            capo_budgets.types.notification_type.deserialize_aws_json_1_1(
                data["NotificationType"]
            )
        )
    if data.get("ActionThreshold") is not None:
        import capo_budgets.types.action_threshold

        out["action_threshold"] = (
            capo_budgets.types.action_threshold.deserialize_aws_json_1_1(
                data["ActionThreshold"]
            )
        )
    if data.get("Definition") is not None:
        import capo_budgets.types.definition

        out["definition"] = capo_budgets.types.definition.deserialize_aws_json_1_1(
            data["Definition"]
        )
    if data.get("ExecutionRoleArn") is not None:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if data.get("ApprovalModel") is not None:
        import capo_budgets.types.approval_model

        out["approval_model"] = (
            capo_budgets.types.approval_model.deserialize_aws_json_1_1(
                data["ApprovalModel"]
            )
        )
    if data.get("Subscribers") is not None:
        import capo_budgets.types.subscribers

        out["subscribers"] = capo_budgets.types.subscribers.deserialize_aws_json_1_1(
            data["Subscribers"]
        )
    return out


def redact_sensitive(value: UpdateBudgetActionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "subscribers" in value:
        import capo_budgets.types.subscribers

        out["subscribers"] = capo_budgets.types.subscribers.redact_sensitive(
            value["subscribers"]
        )
    return out
