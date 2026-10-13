"""Generated from Smithy shape ``com.amazonaws.deadline#GetFarmResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.cost_scale_factor
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.description
    import capo_deadline.types.farm_id
    import capo_deadline.types.kms_key_arn
    import capo_deadline.types.resource_name
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class GetFarmResponse(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm to get.</p>"""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The display name of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    kms_key_arn: NotRequired["capo_deadline.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key used on the farm.</p>"""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    description: NotRequired["capo_deadline.types.description.Description"]
    """<p>The description of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    cost_scale_factor: "capo_deadline.types.cost_scale_factor.CostScaleFactor"
    """<p>A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFarmResponse) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["displayName"] = value["display_name"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
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
    if "description" in value:
        out["description"] = value["description"]
    out["costScaleFactor"] = (
        "NaN"
        if value.get("cost_scale_factor", 1) != value.get("cost_scale_factor", 1)
        else "Infinity"
        if value.get("cost_scale_factor", 1) == float("inf")
        else "-Infinity"
        if value.get("cost_scale_factor", 1) == float("-inf")
        else value.get("cost_scale_factor", 1)
    )
    return out


def deserialize_json(data: dict) -> GetFarmResponse:
    out: GetFarmResponse = {}  # type: ignore[typeddict-item]
    if data.get("farmId") is not None:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("GetFarmResponse.farm_id required")
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("GetFarmResponse.display_name required")
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("createdAt") is not None:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetFarmResponse.created_at required")
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetFarmResponse.created_by required")
    if data.get("updatedAt") is not None:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("costScaleFactor") is not None:
        out["cost_scale_factor"] = float(data["costScaleFactor"])
    else:
        out["cost_scale_factor"] = 1
    return out


def redact_sensitive(value: GetFarmResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
