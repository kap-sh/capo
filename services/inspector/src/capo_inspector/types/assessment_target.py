"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.assessment_target_name
    import capo_inspector.types.timestamp


class AssessmentTarget(TypedDict, closed=True):
    arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN that specifies the Amazon Inspector assessment target.</p>"""
    name: "capo_inspector.types.assessment_target_name.AssessmentTargetName"
    """<p>The name of the Amazon Inspector assessment target.</p>"""
    resource_group_arn: NotRequired["capo_inspector.types.arn.Arn"]
    """<p>The ARN that specifies the resource group that is associated with the assessment target.</p>"""
    created_at: "capo_inspector.types.timestamp.Timestamp"
    """<p>The time at which the assessment target is created.</p>"""
    updated_at: "capo_inspector.types.timestamp.Timestamp"
    """<p>The time at which <a>UpdateAssessmentTarget</a> is called.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentTarget) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "resource_group_arn" in value:
        out["resourceGroupArn"] = value["resource_group_arn"]
    import capo_inspector.types.timestamp

    out["createdAt"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
        value["created_at"]
    )
    import capo_inspector.types.timestamp

    out["updatedAt"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
        value["updated_at"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentTarget:
    out: AssessmentTarget = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("resourceGroupArn") is not None:
        out["resource_group_arn"] = data["resourceGroupArn"]
    if data.get("createdAt") is not None:
        import capo_inspector.types.timestamp

        out["created_at"] = capo_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_inspector.types.timestamp

        out["updated_at"] = capo_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
