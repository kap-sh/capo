"""Generated from Smithy shape ``com.amazonaws.deadline#CreateBudgetRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.budget_actions_to_add
    import capo_deadline.types.budget_schedule
    import capo_deadline.types.client_token
    import capo_deadline.types.consumed_usage_limit
    import capo_deadline.types.description
    import capo_deadline.types.farm_id
    import capo_deadline.types.resource_name
    import capo_deadline.types.tags
    import capo_deadline.types.usage_tracking_resource


class CreateBudgetRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID to include in this budget.</p>"""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The display name of the budget.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    description: NotRequired["capo_deadline.types.description.Description"]
    """<p>The description of the budget.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    usage_tracking_resource: (
        "capo_deadline.types.usage_tracking_resource.UsageTrackingResource"
    )
    """<p>The queue ID provided to this budget to track usage.</p>"""
    approximate_dollar_limit: (
        "capo_deadline.types.consumed_usage_limit.ConsumedUsageLimit"
    )
    """<p>The dollar limit based on consumed usage.</p>"""
    actions: "capo_deadline.types.budget_actions_to_add.BudgetActionsToAdd"
    """<p>The budget actions to specify what happens when the budget runs out.</p>"""
    schedule: "capo_deadline.types.budget_schedule.BudgetSchedule"
    """<p>The schedule to associate with this budget.</p>"""
    tags: NotRequired["capo_deadline.types.tags.Tags"]
    """<p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBudgetRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_deadline.types.usage_tracking_resource

    out["usageTrackingResource"] = (
        capo_deadline.types.usage_tracking_resource.serialize_json(
            value["usage_tracking_resource"]
        )
    )
    out["approximateDollarLimit"] = (
        "NaN"
        if value["approximate_dollar_limit"] != value["approximate_dollar_limit"]
        else "Infinity"
        if value["approximate_dollar_limit"] == float("inf")
        else "-Infinity"
        if value["approximate_dollar_limit"] == float("-inf")
        else value["approximate_dollar_limit"]
    )
    import capo_deadline.types.budget_actions_to_add

    out["actions"] = capo_deadline.types.budget_actions_to_add.serialize_json(
        value["actions"]
    )
    import capo_deadline.types.budget_schedule

    out["schedule"] = capo_deadline.types.budget_schedule.serialize_json(
        value["schedule"]
    )
    if "tags" in value:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateBudgetRequest:
    out: CreateBudgetRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("usageTrackingResource") is not None:
        import capo_deadline.types.usage_tracking_resource

        out["usage_tracking_resource"] = (
            capo_deadline.types.usage_tracking_resource.deserialize_json(
                data["usageTrackingResource"]
            )
        )
    else:
        import capo_deadline.types._unknown

        out["usage_tracking_resource"] = (
            capo_deadline.types._unknown.UnknownUnionMember("")
        )
    if data.get("approximateDollarLimit") is not None:
        out["approximate_dollar_limit"] = float(data["approximateDollarLimit"])
    else:
        out["approximate_dollar_limit"] = 0.0
    if data.get("actions") is not None:
        import capo_deadline.types.budget_actions_to_add

        out["actions"] = capo_deadline.types.budget_actions_to_add.deserialize_json(
            data["actions"]
        )
    else:
        out["actions"] = []
    if data.get("schedule") is not None:
        import capo_deadline.types.budget_schedule

        out["schedule"] = capo_deadline.types.budget_schedule.deserialize_json(
            data["schedule"]
        )
    else:
        import capo_deadline.types._unknown

        out["schedule"] = capo_deadline.types._unknown.UnknownUnionMember("")
    if data.get("tags") is not None:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateBudgetRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "actions" in value:
        import capo_deadline.types.budget_actions_to_add

        out["actions"] = capo_deadline.types.budget_actions_to_add.redact_sensitive(
            value["actions"]
        )
    return out
