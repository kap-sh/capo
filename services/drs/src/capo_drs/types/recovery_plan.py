"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlan``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.iso8601_datetime_string
    import capo_drs.types.recovery_plan_description
    import capo_drs.types.recovery_plan_name
    import capo_drs.types.recovery_plan_status
    import capo_drs.types.strict_drsarn
    import capo_drs.types.tags_map


class RecoveryPlan(TypedDict, closed=True):
    recovery_plan_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan.</p>"""
    name: "capo_drs.types.recovery_plan_name.RecoveryPlanName"
    description: NotRequired[
        "capo_drs.types.recovery_plan_description.RecoveryPlanDescription"
    ]
    status: "capo_drs.types.recovery_plan_status.RecoveryPlanStatus"
    """<p>The status of the Recovery Plan.</p>"""
    created_at: "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    """<p>The timestamp when the Recovery Plan was created.</p>"""
    updated_at: "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    """<p>The timestamp when the Recovery Plan was last updated.</p>"""
    tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>The tags associated with the Recovery Plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlan) -> dict:
    out: dict = {}
    out["recoveryPlanArn"] = value["recovery_plan_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["status"] = value["status"]
    out["createdAt"] = value["created_at"]
    out["updatedAt"] = value["updated_at"]
    if "tags" in value:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RecoveryPlan:
    out: RecoveryPlan = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanArn") is not None:
        out["recovery_plan_arn"] = data["recoveryPlanArn"]
    else:
        out["recovery_plan_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("createdAt") is not None:
        out["created_at"] = data["createdAt"]
    else:
        out["created_at"] = ""
    if data.get("updatedAt") is not None:
        out["updated_at"] = data["updatedAt"]
    else:
        out["updated_at"] = ""
    if data.get("tags") is not None:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: RecoveryPlan) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
