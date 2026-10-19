"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.budget_id
    import capo_deadline.types.budget_status
    import capo_deadline.types.consumed_usage_limit
    import capo_deadline.types.consumed_usages
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.description
    import capo_deadline.types.resource_name
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by
    import capo_deadline.types.usage_tracking_resource


class BudgetSummary(TypedDict, closed=True):
    budget_id: "capo_deadline.types.budget_id.BudgetId"
    """<p>The budget ID.</p>"""
    usage_tracking_resource: (
        "capo_deadline.types.usage_tracking_resource.UsageTrackingResource"
    )
    """<p>The resource used to track expenditure in the budget.</p>"""
    status: "capo_deadline.types.budget_status.BudgetStatus"
    """<p>The status of the budget.</p> <ul> <li> <p> <code>ACTIVE</code>–The budget is being evaluated.</p> </li> <li> <p> <code>INACTIVE</code>–The budget is inactive. This can include Expired, Canceled, or deleted Deleted statuses.</p> </li> </ul>"""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The display name of the budget summary to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    approximate_dollar_limit: (
        "capo_deadline.types.consumed_usage_limit.ConsumedUsageLimit"
    )
    """<p>The approximate dollar limit of the budget.</p>"""
    usages: "capo_deadline.types.consumed_usages.ConsumedUsages"
    """<p>The consumed usage for the budget.</p>"""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    description: NotRequired["capo_deadline.types.description.Description"]
    """<p>The description of the budget summary.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: BudgetSummary) -> dict:
    out: dict = {}
    out["budgetId"] = value["budget_id"]
    import capo_deadline.types.usage_tracking_resource

    out["usageTrackingResource"] = (
        capo_deadline.types.usage_tracking_resource.serialize_json(
            value["usage_tracking_resource"]
        )
    )
    import capo_deadline.types.budget_status

    out["status"] = capo_deadline.types.budget_status.serialize_json(value["status"])
    out["displayName"] = value["display_name"]
    out["approximateDollarLimit"] = (
        "NaN"
        if value["approximate_dollar_limit"] != value["approximate_dollar_limit"]
        else "Infinity"
        if value["approximate_dollar_limit"] == float("inf")
        else "-Infinity"
        if value["approximate_dollar_limit"] == float("-inf")
        else value["approximate_dollar_limit"]
    )
    import capo_deadline.types.consumed_usages

    out["usages"] = capo_deadline.types.consumed_usages.serialize_json(value["usages"])
    out["createdBy"] = value["created_by"]
    import capo_deadline.types.created_at

    out["createdAt"] = capo_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> BudgetSummary:
    out: BudgetSummary = {}  # type: ignore[typeddict-item]
    if data.get("budgetId") is not None:
        out["budget_id"] = data["budgetId"]
    else:
        out["budget_id"] = ""
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
    if data.get("status") is not None:
        import capo_deadline.types.budget_status

        out["status"] = capo_deadline.types.budget_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_deadline.types.budget_status.BudgetStatus", ""
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("approximateDollarLimit") is not None:
        out["approximate_dollar_limit"] = float(data["approximateDollarLimit"])
    else:
        out["approximate_dollar_limit"] = 0.0
    if data.get("usages") is not None:
        import capo_deadline.types.consumed_usages

        out["usages"] = capo_deadline.types.consumed_usages.deserialize_json(
            data["usages"]
        )
    else:
        raise DeserializationError("BudgetSummary.usages required")
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("createdAt") is not None:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("updatedAt") is not None:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: BudgetSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
