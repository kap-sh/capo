"""Generated from Smithy shape ``com.amazonaws.budgets#CreateBudgetActionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.action_threshold
    import capo_budgets.types.action_type
    import capo_budgets.types.approval_model
    import capo_budgets.types.budget_name
    import capo_budgets.types.definition
    import capo_budgets.types.notification_type
    import capo_budgets.types.resource_tag_list
    import capo_budgets.types.role_arn
    import capo_budgets.types.subscribers


class CreateBudgetActionRequest(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    budget_name: "capo_budgets.types.budget_name.BudgetName"
    notification_type: "capo_budgets.types.notification_type.NotificationType"
    action_type: "capo_budgets.types.action_type.ActionType"
    """<p> The type of action. This defines the type of tasks that can be carried out by this action. This field also determines the format for definition. </p>"""
    action_threshold: "capo_budgets.types.action_threshold.ActionThreshold"
    definition: "capo_budgets.types.definition.Definition"
    execution_role_arn: "capo_budgets.types.role_arn.RoleArn"
    """<p> The role passed for action execution and reversion. Roles and actions must be in the same account. </p>"""
    approval_model: "capo_budgets.types.approval_model.ApprovalModel"
    """<p> This specifies if the action needs manual or automatic approval. </p>"""
    subscribers: "capo_budgets.types.subscribers.Subscribers"
    resource_tags: NotRequired["capo_budgets.types.resource_tag_list.ResourceTagList"]
    """<p>An optional list of tags to associate with the specified budget action. Each tag consists of a key and a value, and each key must be unique for the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBudgetActionRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import capo_budgets.types.notification_type

    out["NotificationType"] = (
        capo_budgets.types.notification_type.serialize_aws_json_1_1(
            value["notification_type"]
        )
    )
    import capo_budgets.types.action_type

    out["ActionType"] = capo_budgets.types.action_type.serialize_aws_json_1_1(
        value["action_type"]
    )
    import capo_budgets.types.action_threshold

    out["ActionThreshold"] = capo_budgets.types.action_threshold.serialize_aws_json_1_1(
        value["action_threshold"]
    )
    import capo_budgets.types.definition

    out["Definition"] = capo_budgets.types.definition.serialize_aws_json_1_1(
        value["definition"]
    )
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    import capo_budgets.types.approval_model

    out["ApprovalModel"] = capo_budgets.types.approval_model.serialize_aws_json_1_1(
        value["approval_model"]
    )
    import capo_budgets.types.subscribers

    out["Subscribers"] = capo_budgets.types.subscribers.serialize_aws_json_1_1(
        value["subscribers"]
    )
    if "resource_tags" in value:
        import capo_budgets.types.resource_tag_list

        out["ResourceTags"] = (
            capo_budgets.types.resource_tag_list.serialize_aws_json_1_1(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBudgetActionRequest:
    out: CreateBudgetActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("CreateBudgetActionRequest.account_id required")
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("CreateBudgetActionRequest.budget_name required")
    if data.get("NotificationType") is not None:
        import capo_budgets.types.notification_type

        out["notification_type"] = (
            capo_budgets.types.notification_type.deserialize_aws_json_1_1(
                data["NotificationType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBudgetActionRequest.notification_type required"
        )
    if data.get("ActionType") is not None:
        import capo_budgets.types.action_type

        out["action_type"] = capo_budgets.types.action_type.deserialize_aws_json_1_1(
            data["ActionType"]
        )
    else:
        raise DeserializationError("CreateBudgetActionRequest.action_type required")
    if data.get("ActionThreshold") is not None:
        import capo_budgets.types.action_threshold

        out["action_threshold"] = (
            capo_budgets.types.action_threshold.deserialize_aws_json_1_1(
                data["ActionThreshold"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBudgetActionRequest.action_threshold required"
        )
    if data.get("Definition") is not None:
        import capo_budgets.types.definition

        out["definition"] = capo_budgets.types.definition.deserialize_aws_json_1_1(
            data["Definition"]
        )
    else:
        raise DeserializationError("CreateBudgetActionRequest.definition required")
    if data.get("ExecutionRoleArn") is not None:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        raise DeserializationError(
            "CreateBudgetActionRequest.execution_role_arn required"
        )
    if data.get("ApprovalModel") is not None:
        import capo_budgets.types.approval_model

        out["approval_model"] = (
            capo_budgets.types.approval_model.deserialize_aws_json_1_1(
                data["ApprovalModel"]
            )
        )
    else:
        raise DeserializationError("CreateBudgetActionRequest.approval_model required")
    if data.get("Subscribers") is not None:
        import capo_budgets.types.subscribers

        out["subscribers"] = capo_budgets.types.subscribers.deserialize_aws_json_1_1(
            data["Subscribers"]
        )
    else:
        raise DeserializationError("CreateBudgetActionRequest.subscribers required")
    if data.get("ResourceTags") is not None:
        import capo_budgets.types.resource_tag_list

        out["resource_tags"] = (
            capo_budgets.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTags"]
            )
        )
    return out


def redact_sensitive(value: CreateBudgetActionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "subscribers" in value:
        import capo_budgets.types.subscribers

        out["subscribers"] = capo_budgets.types.subscribers.redact_sensitive(
            value["subscribers"]
        )
    return out
