"""Generated from Smithy shape ``com.amazonaws.deadline#LimitSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.amount_requirement_name
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.farm_id
    import capo_deadline.types.limit_id
    import capo_deadline.types.max_count
    import capo_deadline.types.min_zero_max_integer
    import capo_deadline.types.resource_name
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class LimitSummary(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The unique identifier of the farm that contains the limit."""
    limit_id: "capo_deadline.types.limit_id.LimitId"
    """The unique identifier of the limit."""
    current_count: "capo_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    """The number of resources from the limit that are being used by jobs. The result is delayed and may not be the count at the time that you called the operation."""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """The Unix timestamp of the date and time that the limit was created."""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """The user identifier of the person that created the limit."""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """The Unix timestamp of the date and time that the limit was last updated."""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """The user identifier of the person that last updated the limit."""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The name of the limit used in lists to identify the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    amount_requirement_name: (
        "capo_deadline.types.amount_requirement_name.AmountRequirementName"
    )
    """The value that you specify as the <code>name</code> in the <code>amounts</code> field of the <code>hostRequirements</code> in a step of a job template to declare the limit requirement."""
    max_count: "capo_deadline.types.max_count.MaxCount"
    """The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available. The <code>maxValue</code> must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit."""


# --- restJson1 ser/de ---
def serialize_json(value: LimitSummary) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["limitId"] = value["limit_id"]
    out["currentCount"] = value["current_count"]
    import capo_deadline.types.created_at

    out["createdAt"] = capo_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["displayName"] = value["display_name"]
    out["amountRequirementName"] = value["amount_requirement_name"]
    out["maxCount"] = value["max_count"]
    return out


def deserialize_json(data: dict) -> LimitSummary:
    out: LimitSummary = {}  # type: ignore[typeddict-item]
    if data.get("farmId") is not None:
        out["farm_id"] = data["farmId"]
    else:
        out["farm_id"] = ""
    if data.get("limitId") is not None:
        out["limit_id"] = data["limitId"]
    else:
        out["limit_id"] = ""
    if data.get("currentCount") is not None:
        out["current_count"] = data["currentCount"]
    else:
        out["current_count"] = 0
    if data.get("createdAt") is not None:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("updatedAt") is not None:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("amountRequirementName") is not None:
        out["amount_requirement_name"] = data["amountRequirementName"]
    else:
        out["amount_requirement_name"] = ""
    if data.get("maxCount") is not None:
        out["max_count"] = data["maxCount"]
    else:
        out["max_count"] = 0
    return out
