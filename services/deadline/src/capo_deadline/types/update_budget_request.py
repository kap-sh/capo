"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateBudgetRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.budget_actions_to_add
    import capo_deadline.types.budget_actions_to_remove
    import capo_deadline.types.budget_id
    import capo_deadline.types.budget_schedule
    import capo_deadline.types.budget_status
    import capo_deadline.types.client_token
    import capo_deadline.types.consumed_usage_limit
    import capo_deadline.types.description
    import capo_deadline.types.farm_id
    import capo_deadline.types.resource_name


class UpdateBudgetRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the budget to update."""
    budget_id: "capo_deadline.types.budget_id.BudgetId"
    """The budget ID to update."""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """The unique token which the server uses to recognize retries of the same request."""
    display_name: NotRequired["capo_deadline.types.resource_name.ResourceName"]
    """<p>The display name of the budget to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    description: NotRequired["capo_deadline.types.description.Description"]
    """<p>The description of the budget to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    status: NotRequired["capo_deadline.types.budget_status.BudgetStatus"]
    """<p>Updates the status of the budget.</p> <ul> <li> <p> <code>ACTIVE</code>–The budget is being evaluated.</p> </li> <li> <p> <code>INACTIVE</code>–The budget is inactive. This can include Expired, Canceled, or deleted Deleted statuses.</p> </li> </ul>"""
    approximate_dollar_limit: NotRequired[
        "capo_deadline.types.consumed_usage_limit.ConsumedUsageLimit"
    ]
    """The dollar limit to update on the budget. Based on consumed usage."""
    actions_to_add: NotRequired[
        "capo_deadline.types.budget_actions_to_add.BudgetActionsToAdd"
    ]
    """The budget actions to add. Budget actions specify what happens when the budget runs out."""
    actions_to_remove: NotRequired[
        "capo_deadline.types.budget_actions_to_remove.BudgetActionsToRemove"
    ]
    """The budget actions to remove from the budget."""
    schedule: NotRequired["capo_deadline.types.budget_schedule.BudgetSchedule"]
    """The schedule to update."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBudgetRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_deadline.types.budget_status

        out["status"] = capo_deadline.types.budget_status.serialize_json(
            value["status"]
        )
    if "approximate_dollar_limit" in value:
        out["approximateDollarLimit"] = (
            "NaN"
            if value["approximate_dollar_limit"] != value["approximate_dollar_limit"]
            else "Infinity"
            if value["approximate_dollar_limit"] == float("inf")
            else "-Infinity"
            if value["approximate_dollar_limit"] == float("-inf")
            else value["approximate_dollar_limit"]
        )
    if "actions_to_add" in value:
        import capo_deadline.types.budget_actions_to_add

        out["actionsToAdd"] = capo_deadline.types.budget_actions_to_add.serialize_json(
            value["actions_to_add"]
        )
    if "actions_to_remove" in value:
        import capo_deadline.types.budget_actions_to_remove

        out["actionsToRemove"] = (
            capo_deadline.types.budget_actions_to_remove.serialize_json(
                value["actions_to_remove"]
            )
        )
    if "schedule" in value:
        import capo_deadline.types.budget_schedule

        out["schedule"] = capo_deadline.types.budget_schedule.serialize_json(
            value["schedule"]
        )
    return out


def deserialize_json(data: dict) -> UpdateBudgetRequest:
    out: UpdateBudgetRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_deadline.types.budget_status

        out["status"] = capo_deadline.types.budget_status.deserialize_json(
            data["status"]
        )
    if data.get("approximateDollarLimit") is not None:
        out["approximate_dollar_limit"] = float(data["approximateDollarLimit"])
    if data.get("actionsToAdd") is not None:
        import capo_deadline.types.budget_actions_to_add

        out["actions_to_add"] = (
            capo_deadline.types.budget_actions_to_add.deserialize_json(
                data["actionsToAdd"]
            )
        )
    if data.get("actionsToRemove") is not None:
        import capo_deadline.types.budget_actions_to_remove

        out["actions_to_remove"] = (
            capo_deadline.types.budget_actions_to_remove.deserialize_json(
                data["actionsToRemove"]
            )
        )
    if data.get("schedule") is not None:
        import capo_deadline.types.budget_schedule

        out["schedule"] = capo_deadline.types.budget_schedule.deserialize_json(
            data["schedule"]
        )
    return out


def redact_sensitive(value: UpdateBudgetRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "actions_to_add" in value:
        import capo_deadline.types.budget_actions_to_add

        out["actions_to_add"] = (
            capo_deadline.types.budget_actions_to_add.redact_sensitive(
                value["actions_to_add"]
            )
        )
    return out
