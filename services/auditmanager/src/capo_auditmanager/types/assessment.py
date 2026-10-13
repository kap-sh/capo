"""Generated from Smithy shape ``com.amazonaws.auditmanager#Assessment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_framework
    import capo_auditmanager.types.assessment_metadata
    import capo_auditmanager.types.audit_manager_arn
    import capo_auditmanager.types.aws_account
    import capo_auditmanager.types.tag_map


class Assessment(TypedDict, closed=True):
    arn: NotRequired["capo_auditmanager.types.audit_manager_arn.AuditManagerArn"]
    """<p> The Amazon Resource Name (ARN) of the assessment. </p>"""
    aws_account: NotRequired["capo_auditmanager.types.aws_account.AWSAccount"]
    """<p> The Amazon Web Services account that's associated with the assessment. </p>"""
    metadata: NotRequired[
        "capo_auditmanager.types.assessment_metadata.AssessmentMetadata"
    ]
    """<p> The metadata for the assessment. </p>"""
    framework: NotRequired[
        "capo_auditmanager.types.assessment_framework.AssessmentFramework"
    ]
    """<p> The framework that the assessment was created from. </p>"""
    tags: NotRequired["capo_auditmanager.types.tag_map.TagMap"]
    """<p> The tags that are associated with the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Assessment) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "aws_account" in value:
        import capo_auditmanager.types.aws_account

        out["awsAccount"] = capo_auditmanager.types.aws_account.serialize_json(
            value["aws_account"]
        )
    if "metadata" in value:
        import capo_auditmanager.types.assessment_metadata

        out["metadata"] = capo_auditmanager.types.assessment_metadata.serialize_json(
            value["metadata"]
        )
    if "framework" in value:
        import capo_auditmanager.types.assessment_framework

        out["framework"] = capo_auditmanager.types.assessment_framework.serialize_json(
            value["framework"]
        )
    if "tags" in value:
        import capo_auditmanager.types.tag_map

        out["tags"] = capo_auditmanager.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Assessment:
    out: Assessment = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("awsAccount") is not None:
        import capo_auditmanager.types.aws_account

        out["aws_account"] = capo_auditmanager.types.aws_account.deserialize_json(
            data["awsAccount"]
        )
    if data.get("metadata") is not None:
        import capo_auditmanager.types.assessment_metadata

        out["metadata"] = capo_auditmanager.types.assessment_metadata.deserialize_json(
            data["metadata"]
        )
    if data.get("framework") is not None:
        import capo_auditmanager.types.assessment_framework

        out["framework"] = (
            capo_auditmanager.types.assessment_framework.deserialize_json(
                data["framework"]
            )
        )
    if data.get("tags") is not None:
        import capo_auditmanager.types.tag_map

        out["tags"] = capo_auditmanager.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: Assessment) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "aws_account" in value:
        import capo_auditmanager.types.aws_account

        out["aws_account"] = capo_auditmanager.types.aws_account.redact_sensitive(
            value["aws_account"]
        )
    if "metadata" in value:
        import capo_auditmanager.types.assessment_metadata

        out["metadata"] = capo_auditmanager.types.assessment_metadata.redact_sensitive(
            value["metadata"]
        )
    if "framework" in value:
        out["framework"] = "*** Sensitive Data Redacted ***"
    return out
