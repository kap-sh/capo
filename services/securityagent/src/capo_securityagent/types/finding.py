"""Generated from Smithy shape ``com.amazonaws.securityagent#Finding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.code_location_list
    import capo_securityagent.types.code_remediation_task
    import capo_securityagent.types.confidence_level
    import capo_securityagent.types.finding_status
    import capo_securityagent.types.risk_level
    import capo_securityagent.types.string_list
    import capo_securityagent.types.validation_status
    import capo_securityagent.types.verification_script


class Finding(TypedDict, closed=True):
    finding_id: "str"
    """<p>The unique identifier of the finding.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space associated with the finding.</p>"""
    pentest_id: NotRequired["str"]
    """<p>The unique identifier of the pentest associated with the finding.</p>"""
    pentest_job_id: NotRequired["str"]
    """<p>The unique identifier of the pentest job that produced the finding.</p>"""
    code_review_id: NotRequired["str"]
    """<p>The unique identifier of the code review associated with the finding.</p>"""
    code_review_job_id: NotRequired["str"]
    """<p>The unique identifier of the code review job that produced the finding.</p>"""
    task_id: NotRequired["str"]
    """<p>The unique identifier of the task that produced the finding.</p>"""
    name: NotRequired["str"]
    """<p>The name of the finding.</p>"""
    description: NotRequired["str"]
    """<p>A description of the finding.</p>"""
    status: NotRequired["capo_securityagent.types.finding_status.FindingStatus"]
    """<p>The current status of the finding. Valid values include ACTIVE, RESOLVED, ACCEPTED, and FALSE_POSITIVE.</p>"""
    risk_type: NotRequired["str"]
    """<p>The type of security risk identified by the finding.</p>"""
    risk_level: NotRequired["capo_securityagent.types.risk_level.RiskLevel"]
    """<p>The risk level of the finding. Valid values include UNKNOWN, INFORMATIONAL, LOW, MEDIUM, HIGH, and CRITICAL.</p>"""
    risk_score: NotRequired["str"]
    """<p>The numerical risk score of the finding.</p>"""
    reasoning: NotRequired["str"]
    """<p>The reasoning behind the finding, explaining why it was identified as a vulnerability.</p>"""
    confidence: NotRequired["capo_securityagent.types.confidence_level.ConfidenceLevel"]
    """<p>The confidence level of the finding. Valid values include FALSE_POSITIVE, UNCONFIRMED, LOW, MEDIUM, and HIGH.</p>"""
    validation_status: NotRequired[
        "capo_securityagent.types.validation_status.ValidationStatus"
    ]
    """<p>The simulated validation status of the finding. Valid values are NOT_VALIDATED, VALIDATING, CONFIRMED, NOT_REPRODUCED, and VALIDATION_FAILED.</p>"""
    attack_script: NotRequired["str"]
    """<p>The attack script used to reproduce the finding.</p>"""
    remediation_code: NotRequired["str"]
    """<p>The suggested fix for the finding, describing the changes recommended to remediate the vulnerability, with example code or configuration.</p>"""
    code_remediation_task: NotRequired[
        "capo_securityagent.types.code_remediation_task.CodeRemediationTask"
    ]
    """<p>The code remediation task associated with the finding, if code remediation was initiated.</p>"""
    last_updated_by: NotRequired["str"]
    """<p>The identifier of the entity that last updated the finding.</p>"""
    customer_note: NotRequired["str"]
    """<p>A customer-provided note on the finding.</p>"""
    code_locations: NotRequired[
        "capo_securityagent.types.code_location_list.CodeLocationList"
    ]
    """<p>The file locations involved in the vulnerability, as reported by the code scanner.</p>"""
    verification_script: NotRequired[
        "capo_securityagent.types.verification_script.VerificationScript"
    ]
    """<p>The verification script metadata for reproducing the finding, including download URL, instructions, and required environment variables.</p>"""
    alignment_rationale: NotRequired["str"]
    """<p>The rationale provided by the alignment agent explaining how the finding was adjusted based on customer preferences.</p>"""
    revalidation_job_ids: NotRequired["capo_securityagent.types.string_list.StringList"]
    """<p>The list of pentest job identifiers for revalidation jobs that retested this finding.</p>"""
    original_finding_id: NotRequired["str"]
    """<p>The identifier of the original finding that this revalidation finding was produced from.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the finding was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the finding was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Finding) -> dict:
    out: dict = {}
    out["findingId"] = value["finding_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "pentest_id" in value:
        out["pentestId"] = value["pentest_id"]
    if "pentest_job_id" in value:
        out["pentestJobId"] = value["pentest_job_id"]
    if "code_review_id" in value:
        out["codeReviewId"] = value["code_review_id"]
    if "code_review_job_id" in value:
        out["codeReviewJobId"] = value["code_review_job_id"]
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_securityagent.types.finding_status

        out["status"] = capo_securityagent.types.finding_status.serialize_json(
            value["status"]
        )
    if "risk_type" in value:
        out["riskType"] = value["risk_type"]
    if "risk_level" in value:
        import capo_securityagent.types.risk_level

        out["riskLevel"] = capo_securityagent.types.risk_level.serialize_json(
            value["risk_level"]
        )
    if "risk_score" in value:
        out["riskScore"] = value["risk_score"]
    if "reasoning" in value:
        out["reasoning"] = value["reasoning"]
    if "confidence" in value:
        import capo_securityagent.types.confidence_level

        out["confidence"] = capo_securityagent.types.confidence_level.serialize_json(
            value["confidence"]
        )
    if "validation_status" in value:
        import capo_securityagent.types.validation_status

        out["validationStatus"] = (
            capo_securityagent.types.validation_status.serialize_json(
                value["validation_status"]
            )
        )
    if "attack_script" in value:
        out["attackScript"] = value["attack_script"]
    if "remediation_code" in value:
        out["remediationCode"] = value["remediation_code"]
    if "code_remediation_task" in value:
        import capo_securityagent.types.code_remediation_task

        out["codeRemediationTask"] = (
            capo_securityagent.types.code_remediation_task.serialize_json(
                value["code_remediation_task"]
            )
        )
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    if "customer_note" in value:
        out["customerNote"] = value["customer_note"]
    if "code_locations" in value:
        import capo_securityagent.types.code_location_list

        out["codeLocations"] = (
            capo_securityagent.types.code_location_list.serialize_json(
                value["code_locations"]
            )
        )
    if "verification_script" in value:
        import capo_securityagent.types.verification_script

        out["verificationScript"] = (
            capo_securityagent.types.verification_script.serialize_json(
                value["verification_script"]
            )
        )
    if "alignment_rationale" in value:
        out["alignmentRationale"] = value["alignment_rationale"]
    if "revalidation_job_ids" in value:
        import capo_securityagent.types.string_list

        out["revalidationJobIds"] = capo_securityagent.types.string_list.serialize_json(
            value["revalidation_job_ids"]
        )
    if "original_finding_id" in value:
        out["originalFindingId"] = value["original_finding_id"]
    if "created_at" in value:
        import capo_securityagent._protocol.serialize

        out["createdAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent._protocol.serialize

        out["updatedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> Finding:
    out: Finding = {}  # type: ignore[typeddict-item]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    else:
        raise DeserializationError("Finding.finding_id required")
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("Finding.agent_space_id required")
    if data.get("pentestId") is not None:
        out["pentest_id"] = data["pentestId"]
    if data.get("pentestJobId") is not None:
        out["pentest_job_id"] = data["pentestJobId"]
    if data.get("codeReviewId") is not None:
        out["code_review_id"] = data["codeReviewId"]
    if data.get("codeReviewJobId") is not None:
        out["code_review_job_id"] = data["codeReviewJobId"]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_securityagent.types.finding_status

        out["status"] = capo_securityagent.types.finding_status.deserialize_json(
            data["status"]
        )
    if data.get("riskType") is not None:
        out["risk_type"] = data["riskType"]
    if data.get("riskLevel") is not None:
        import capo_securityagent.types.risk_level

        out["risk_level"] = capo_securityagent.types.risk_level.deserialize_json(
            data["riskLevel"]
        )
    if data.get("riskScore") is not None:
        out["risk_score"] = data["riskScore"]
    if data.get("reasoning") is not None:
        out["reasoning"] = data["reasoning"]
    if data.get("confidence") is not None:
        import capo_securityagent.types.confidence_level

        out["confidence"] = capo_securityagent.types.confidence_level.deserialize_json(
            data["confidence"]
        )
    if data.get("validationStatus") is not None:
        import capo_securityagent.types.validation_status

        out["validation_status"] = (
            capo_securityagent.types.validation_status.deserialize_json(
                data["validationStatus"]
            )
        )
    if data.get("attackScript") is not None:
        out["attack_script"] = data["attackScript"]
    if data.get("remediationCode") is not None:
        out["remediation_code"] = data["remediationCode"]
    if data.get("codeRemediationTask") is not None:
        import capo_securityagent.types.code_remediation_task

        out["code_remediation_task"] = (
            capo_securityagent.types.code_remediation_task.deserialize_json(
                data["codeRemediationTask"]
            )
        )
    if data.get("lastUpdatedBy") is not None:
        out["last_updated_by"] = data["lastUpdatedBy"]
    if data.get("customerNote") is not None:
        out["customer_note"] = data["customerNote"]
    if data.get("codeLocations") is not None:
        import capo_securityagent.types.code_location_list

        out["code_locations"] = (
            capo_securityagent.types.code_location_list.deserialize_json(
                data["codeLocations"]
            )
        )
    if data.get("verificationScript") is not None:
        import capo_securityagent.types.verification_script

        out["verification_script"] = (
            capo_securityagent.types.verification_script.deserialize_json(
                data["verificationScript"]
            )
        )
    if data.get("alignmentRationale") is not None:
        out["alignment_rationale"] = data["alignmentRationale"]
    if data.get("revalidationJobIds") is not None:
        import capo_securityagent.types.string_list

        out["revalidation_job_ids"] = (
            capo_securityagent.types.string_list.deserialize_json(
                data["revalidationJobIds"]
            )
        )
    if data.get("originalFindingId") is not None:
        out["original_finding_id"] = data["originalFindingId"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    return out
