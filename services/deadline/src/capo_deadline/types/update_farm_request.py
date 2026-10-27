"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateFarmRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.cost_scale_factor
    import capo_deadline.types.description
    import capo_deadline.types.farm_id
    import capo_deadline.types.resource_name


class UpdateFarmRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID to update."""
    display_name: NotRequired["capo_deadline.types.resource_name.ResourceName"]
    """<p>The display name of the farm to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    description: NotRequired["capo_deadline.types.description.Description"]
    """<p>The description of the farm to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    cost_scale_factor: NotRequired[
        "capo_deadline.types.cost_scale_factor.CostScaleFactor"
    ]
    """A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFarmRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "cost_scale_factor" in value:
        out["costScaleFactor"] = (
            "NaN"
            if value["cost_scale_factor"] != value["cost_scale_factor"]
            else "Infinity"
            if value["cost_scale_factor"] == float("inf")
            else "-Infinity"
            if value["cost_scale_factor"] == float("-inf")
            else value["cost_scale_factor"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFarmRequest:
    out: UpdateFarmRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("costScaleFactor") is not None:
        out["cost_scale_factor"] = float(data["costScaleFactor"])
    return out


def redact_sensitive(value: UpdateFarmRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
