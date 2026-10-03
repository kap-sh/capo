"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_reports_destination
    import capo_auditmanager.types.boolean
    import capo_auditmanager.types.default_export_destination
    import capo_auditmanager.types.deregistration_policy
    import capo_auditmanager.types.kms_key
    import capo_auditmanager.types.roles
    import capo_auditmanager.types.sns_arn


class UpdateSettingsRequest(TypedDict, closed=True):
    sns_topic: NotRequired["capo_auditmanager.types.sns_arn.SnsArn"]
    """<p> The Amazon Simple Notification Service (Amazon SNS) topic that Audit Manager sends notifications to. </p>"""
    default_assessment_reports_destination: NotRequired[
        "capo_auditmanager.types.assessment_reports_destination.AssessmentReportsDestination"
    ]
    """<p> The default S3 destination bucket for storing assessment reports. </p>"""
    default_process_owners: NotRequired["capo_auditmanager.types.roles.Roles"]
    """<p> A list of the default audit owners. </p>"""
    kms_key: NotRequired["capo_auditmanager.types.kms_key.KmsKey"]
    """<p> The KMS key details. </p>"""
    evidence_finder_enabled: NotRequired["capo_auditmanager.types.boolean.Boolean"]
    """<p>Specifies whether the evidence finder feature is enabled. Change this attribute to enable or disable evidence finder.</p> <important> <p>When you use this attribute to disable evidence finder, Audit Manager deletes the event data store that’s used to query your evidence data. As a result, you can’t re-enable evidence finder and use the feature again. Your only alternative is to <a href="https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeregisterAccount.html">deregister</a> and then <a href="https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterAccount.html">re-register</a> Audit Manager. </p> </important>"""
    deregistration_policy: NotRequired[
        "capo_auditmanager.types.deregistration_policy.DeregistrationPolicy"
    ]
    """<p>The deregistration policy for your Audit Manager data. You can use this attribute to determine how your data is handled when you deregister Audit Manager.</p>"""
    default_export_destination: NotRequired[
        "capo_auditmanager.types.default_export_destination.DefaultExportDestination"
    ]
    """<p> The default S3 destination bucket for storing evidence finder exports. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSettingsRequest) -> dict:
    out: dict = {}
    if "sns_topic" in value:
        out["snsTopic"] = value["sns_topic"]
    if "default_assessment_reports_destination" in value:
        import capo_auditmanager.types.assessment_reports_destination

        out["defaultAssessmentReportsDestination"] = (
            capo_auditmanager.types.assessment_reports_destination.serialize_json(
                value["default_assessment_reports_destination"]
            )
        )
    if "default_process_owners" in value:
        import capo_auditmanager.types.roles

        out["defaultProcessOwners"] = capo_auditmanager.types.roles.serialize_json(
            value["default_process_owners"]
        )
    if "kms_key" in value:
        out["kmsKey"] = value["kms_key"]
    if "evidence_finder_enabled" in value:
        out["evidenceFinderEnabled"] = value["evidence_finder_enabled"]
    if "deregistration_policy" in value:
        import capo_auditmanager.types.deregistration_policy

        out["deregistrationPolicy"] = (
            capo_auditmanager.types.deregistration_policy.serialize_json(
                value["deregistration_policy"]
            )
        )
    if "default_export_destination" in value:
        import capo_auditmanager.types.default_export_destination

        out["defaultExportDestination"] = (
            capo_auditmanager.types.default_export_destination.serialize_json(
                value["default_export_destination"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSettingsRequest:
    out: UpdateSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("snsTopic") is not None:
        out["sns_topic"] = data["snsTopic"]
    if data.get("defaultAssessmentReportsDestination") is not None:
        import capo_auditmanager.types.assessment_reports_destination

        out["default_assessment_reports_destination"] = (
            capo_auditmanager.types.assessment_reports_destination.deserialize_json(
                data["defaultAssessmentReportsDestination"]
            )
        )
    if data.get("defaultProcessOwners") is not None:
        import capo_auditmanager.types.roles

        out["default_process_owners"] = capo_auditmanager.types.roles.deserialize_json(
            data["defaultProcessOwners"]
        )
    if data.get("kmsKey") is not None:
        out["kms_key"] = data["kmsKey"]
    if data.get("evidenceFinderEnabled") is not None:
        out["evidence_finder_enabled"] = data["evidenceFinderEnabled"]
    if data.get("deregistrationPolicy") is not None:
        import capo_auditmanager.types.deregistration_policy

        out["deregistration_policy"] = (
            capo_auditmanager.types.deregistration_policy.deserialize_json(
                data["deregistrationPolicy"]
            )
        )
    if data.get("defaultExportDestination") is not None:
        import capo_auditmanager.types.default_export_destination

        out["default_export_destination"] = (
            capo_auditmanager.types.default_export_destination.deserialize_json(
                data["defaultExportDestination"]
            )
        )
    return out
