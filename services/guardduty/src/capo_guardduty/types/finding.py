"""Generated from Smithy shape ``com.amazonaws.guardduty#Finding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.double
    import capo_guardduty.types.finding_type
    import capo_guardduty.types.resource
    import capo_guardduty.types.service
    import capo_guardduty.types.string


class Finding(TypedDict, closed=True):
    account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the account in which the finding was generated.</p>"""
    arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ARN of the finding.</p>"""
    confidence: NotRequired["capo_guardduty.types.double.Double"]
    """<p>The confidence score for the finding.</p>"""
    created_at: NotRequired["capo_guardduty.types.string.String"]
    """<p>The time and date when the finding was created.</p>"""
    description: NotRequired["capo_guardduty.types.string.String"]
    """<p>The description of the finding.</p>"""
    id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the finding.</p>"""
    partition: NotRequired["capo_guardduty.types.string.String"]
    """<p>The partition associated with the finding.</p>"""
    region: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Region where the finding was generated. For findings generated from <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-global-service-events">Global Service Events</a>, the Region value in the finding might differ from the Region where GuardDuty identifies the potential threat. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html#cloudtrail_global">How GuardDuty handles Amazon Web Services CloudTrail global events</a> in the <i>Amazon GuardDuty User Guide</i>.</p>"""
    resource: NotRequired["capo_guardduty.types.resource.Resource"]
    schema_version: NotRequired["capo_guardduty.types.string.String"]
    """<p>The version of the schema used for the finding.</p>"""
    service: NotRequired["capo_guardduty.types.service.Service"]
    severity: NotRequired["capo_guardduty.types.double.Double"]
    """<p>The severity of the finding.</p>"""
    title: NotRequired["capo_guardduty.types.string.String"]
    """<p>The title of the finding.</p>"""
    type: NotRequired["capo_guardduty.types.finding_type.FindingType"]
    """<p>The type of finding.</p>"""
    updated_at: NotRequired["capo_guardduty.types.string.String"]
    """<p>The time and date when the finding was last updated.</p>"""
    associated_attack_sequence_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>Amazon Resource Name (ARN) associated with the attack sequence finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Finding) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "confidence" in value:
        out["confidence"] = (
            "NaN"
            if value["confidence"] != value["confidence"]
            else "Infinity"
            if value["confidence"] == float("inf")
            else "-Infinity"
            if value["confidence"] == float("-inf")
            else value["confidence"]
        )
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "description" in value:
        out["description"] = value["description"]
    if "id" in value:
        out["id"] = value["id"]
    if "partition" in value:
        out["partition"] = value["partition"]
    if "region" in value:
        out["region"] = value["region"]
    if "resource" in value:
        import capo_guardduty.types.resource

        out["resource"] = capo_guardduty.types.resource.serialize_json(
            value["resource"]
        )
    if "schema_version" in value:
        out["schemaVersion"] = value["schema_version"]
    if "service" in value:
        import capo_guardduty.types.service

        out["service"] = capo_guardduty.types.service.serialize_json(value["service"])
    if "severity" in value:
        out["severity"] = (
            "NaN"
            if value["severity"] != value["severity"]
            else "Infinity"
            if value["severity"] == float("inf")
            else "-Infinity"
            if value["severity"] == float("-inf")
            else value["severity"]
        )
    if "title" in value:
        out["title"] = value["title"]
    if "type" in value:
        out["type"] = value["type"]
    if "updated_at" in value:
        out["updatedAt"] = value["updated_at"]
    if "associated_attack_sequence_arn" in value:
        out["associatedAttackSequenceArn"] = value["associated_attack_sequence_arn"]
    return out


def deserialize_json(data: dict) -> Finding:
    out: Finding = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("confidence") is not None:
        out["confidence"] = float(data["confidence"])
    if data.get("createdAt") is not None:
        out["created_at"] = data["createdAt"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("partition") is not None:
        out["partition"] = data["partition"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("resource") is not None:
        import capo_guardduty.types.resource

        out["resource"] = capo_guardduty.types.resource.deserialize_json(
            data["resource"]
        )
    if data.get("schemaVersion") is not None:
        out["schema_version"] = data["schemaVersion"]
    if data.get("service") is not None:
        import capo_guardduty.types.service

        out["service"] = capo_guardduty.types.service.deserialize_json(data["service"])
    if data.get("severity") is not None:
        out["severity"] = float(data["severity"])
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("updatedAt") is not None:
        out["updated_at"] = data["updatedAt"]
    if data.get("associatedAttackSequenceArn") is not None:
        out["associated_attack_sequence_arn"] = data["associatedAttackSequenceArn"]
    return out
