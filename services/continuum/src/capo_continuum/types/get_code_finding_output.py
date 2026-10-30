"""Generated from Smithy shape ``com.amazonaws.continuum#GetCodeFindingOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.affected_package_list
    import capo_continuum.types.cve_id
    import capo_continuum.types.cwe_id_list
    import capo_continuum.types.environment_id
    import capo_continuum.types.finding_arn
    import capo_continuum.types.finding_category
    import capo_continuum.types.finding_code_snippet
    import capo_continuum.types.finding_description
    import capo_continuum.types.finding_discard_reason
    import capo_continuum.types.finding_file_path
    import capo_continuum.types.finding_id
    import capo_continuum.types.finding_ocsf_class
    import capo_continuum.types.finding_posture
    import capo_continuum.types.finding_resource_list
    import capo_continuum.types.finding_severity_id
    import capo_continuum.types.finding_source
    import capo_continuum.types.finding_status
    import capo_continuum.types.finding_status_message
    import capo_continuum.types.finding_string_list
    import capo_continuum.types.finding_title
    import capo_continuum.types.finding_type
    import capo_continuum.types.finding_validation
    import capo_continuum.types.finding_vulnerability_list
    import capo_continuum.types.issue_id
    import capo_continuum.types.scan_run_id
    import capo_continuum.types.source_finding_id


class GetCodeFindingOutput(TypedDict, closed=True):
    type: "capo_continuum.types.finding_type.FindingType"
    """What kind of finding this is. Determines which of the type-specific members below are populated."""
    title: "capo_continuum.types.finding_title.FindingTitle"
    """The producer's title for the finding."""
    severity: "capo_continuum.types.finding_severity_id.FindingSeverityId"
    """The finding's severity."""
    summary: NotRequired["capo_continuum.types.finding_description.FindingDescription"]
    """A one-paragraph description."""
    detailed_description: NotRequired[
        "capo_continuum.types.finding_description.FindingDescription"
    ]
    """The full analysis."""
    category: NotRequired["capo_continuum.types.finding_category.FindingCategory"]
    """The producer's vulnerability category. Not a stable filter key across finding types -- see FindingCategory."""
    sub_category: NotRequired["capo_continuum.types.finding_category.FindingCategory"]
    """A more specific classification within `category`."""
    cwe_ids: NotRequired["capo_continuum.types.cwe_id_list.CweIdList"]
    """CWE identifiers classifying the finding."""
    owasp_category: NotRequired["capo_continuum.types.finding_category.FindingCategory"]
    """The OWASP Top 10 category, when the producer supplies one."""
    mitigation: NotRequired[
        "capo_continuum.types.finding_description.FindingDescription"
    ]
    """How to fix the finding."""
    file_path: NotRequired["capo_continuum.types.finding_file_path.FindingFilePath"]
    """The file the finding is about."""
    line_number: NotRequired["int"]
    """The 1-indexed line the finding is about. Bounds are enforced server-side rather than by a constraint trait: a numeric constraint generates a distinct newtype per enclosing structure, so the same concept would not share a type across the create input and the read output."""
    cve_id: NotRequired["capo_continuum.types.cve_id.CveId"]
    """The CVE this finding reports, for software-composition findings. Both code types can carry one: a customer document supplies it under vulnerabilities[].cve, and Continuum's scanner reports CVEs for dependency-manifest findings."""
    cvss_base_score: NotRequired["float"]
    """The CVSS base score accompanying `cveId`, when the producer supplies one, from 0.0 to 10.0. Not computed by Continuum. The range is enforced server-side, not by a @range trait -- the smithy-rs server SDK does not support range constraints on double shapes (smithy-rs#2007)."""
    affected_packages: NotRequired[
        "capo_continuum.types.affected_package_list.AffectedPackageList"
    ]
    """Packages implicated by the finding."""
    vulnerable_code: NotRequired[
        "capo_continuum.types.finding_code_snippet.FindingCodeSnippet"
    ]
    """The vulnerable code fragment."""
    relevant_inputs: NotRequired[
        "capo_continuum.types.finding_string_list.FindingStringList"
    ]
    """User-controlled inputs that reach the vulnerability."""
    steps_to_reproduce: NotRequired[
        "capo_continuum.types.finding_string_list.FindingStringList"
    ]
    """Steps to reproduce or exploit the finding."""
    validation: NotRequired["capo_continuum.types.finding_validation.FindingValidation"]
    """The validator's assessment. Absent when no validation ran."""
    end_line: NotRequired["int"]
    """The last line of the affected range, from the document's affected_code[].end_line."""
    mitre_techniques: NotRequired[
        "capo_continuum.types.finding_string_list.FindingStringList"
    ]
    """MITRE ATT&CK technique identifiers, from the document's finding_info.attacks[].technique.uid."""
    remediation_references: NotRequired[
        "capo_continuum.types.finding_string_list.FindingStringList"
    ]
    """Remediation references, from the document's vulnerabilities[].remediation.references."""
    ocsf_class: NotRequired["capo_continuum.types.finding_ocsf_class.FindingOcsfClass"]
    """The OCSF class the document declared. Determines whether `posture` is populated."""
    ocsf_schema_version: NotRequired[
        "capo_continuum.types.finding_category.FindingCategory"
    ]
    """The OCSF schema version the producer wrote against (metadata.version)."""
    product_name: NotRequired["capo_continuum.types.finding_category.FindingCategory"]
    """The producing product and vendor (metadata.product)."""
    product_vendor_name: NotRequired[
        "capo_continuum.types.finding_category.FindingCategory"
    ]
    product_version: NotRequired[
        "capo_continuum.types.finding_category.FindingCategory"
    ]
    source_status: NotRequired["capo_continuum.types.finding_category.FindingCategory"]
    """The producer's own status for the finding, and the enum value behind it. Distinct from `status`, which is Continuum's lifecycle state -- a producer may call a finding "New" while Continuum has it SUBMITTED."""
    source_status_id: NotRequired["int"]
    """The producer's numeric enum value for `sourceStatus`."""
    first_seen_at: NotRequired["datetime.datetime"]
    """When the producer first observed the finding (finding_info.first_seen_time). The producer's own clock, not Continuum's."""
    finding_types: NotRequired[
        "capo_continuum.types.finding_string_list.FindingStringList"
    ]
    """The producer's own classification of the finding (finding_info.types)."""
    vulnerabilities: NotRequired[
        "capo_continuum.types.finding_vulnerability_list.FindingVulnerabilityList"
    ]
    """Every vulnerability the document reported. A document may report several; the flat `cveId`/`cvssBaseScore`/`filePath`/`lineNumber` members above carry the first one's identity so a caller that only needs "what and where" does not have to walk this list."""
    resources: NotRequired[
        "capo_continuum.types.finding_resource_list.FindingResourceList"
    ]
    """Resources the document named (resources[])."""
    posture: NotRequired["capo_continuum.types.finding_posture.FindingPosture"]
    """The compliance posture, for an Application Security Posture Finding. Absent for a vulnerability finding."""
    finding_id: "capo_continuum.types.finding_id.FindingId"
    """The unique identifier of the finding."""
    finding_arn: "capo_continuum.types.finding_arn.FindingArn"
    """The ARN of the finding."""
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The environment that owns the finding."""
    source: "capo_continuum.types.finding_source.FindingSource"
    """The system that produced the finding."""
    source_finding_id: "capo_continuum.types.source_finding_id.SourceFindingId"
    """The producer's own identifier for the finding."""
    reported_at: "datetime.datetime"
    """When the producer reported the finding -- its own clock, which is not Continuum's ingestion time. `createdAt` is when Continuum accepted it; these are genuinely different instants and a reader usually wants this one. For CreateCodeFinding, this is the submitted OCSF document's own top-level `time`. For findings Continuum's scanner produces, it is the finding's own creation time. Continuum does not validate it for plausibility: a producer's value is echoed as given, so a `timestamp` here asserts the unit and format, not that the instant is genuine."""
    status: "capo_continuum.types.finding_status.FindingStatus"
    """The current lifecycle status of the finding."""
    status_updated_at: "datetime.datetime"
    """The timestamp when the status last transitioned."""
    created_at: "datetime.datetime"
    """The timestamp when the finding was ingested."""
    scan_run_id: NotRequired["capo_continuum.types.scan_run_id.ScanRunId"]
    """The scan that produced the finding, when it came from one. For a finding Continuum's scanner produced, this is the Continuum scan run (see GetCodeScan). For a finding submitted with CreateCodeFinding, it is the OCSF document's `metadata.correlation_uid`, when that value is a valid ScanRunId. Absent when the finding did not come from a scan."""
    status_message: NotRequired[
        "capo_continuum.types.finding_status_message.FindingStatusMessage"
    ]
    """Human-readable context about the current status."""
    discard_reason: NotRequired[
        "capo_continuum.types.finding_discard_reason.FindingDiscardReason"
    ]
    """Why the finding was not escalated. Present only when status is DISCARDED."""
    discard_reasoning: NotRequired[
        "capo_continuum.types.finding_status_message.FindingStatusMessage"
    ]
    """Customer-facing explanation accompanying `discardReason`."""
    duplicate_of_issue_id: NotRequired["capo_continuum.types.issue_id.IssueId"]
    """The existing issue this finding duplicates. Present only for the DUPLICATE_OF_* discard reasons."""
    created_issue_id: NotRequired["capo_continuum.types.issue_id.IssueId"]
    """The issue Continuum created from this finding."""
    completed_at: NotRequired["datetime.datetime"]
    """When processing finished, whether by creating an issue or discarding. Absent while the finding is still in flight."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeFindingOutput) -> dict:
    out: dict = {}
    import capo_continuum.types.finding_type

    out["type"] = capo_continuum.types.finding_type.serialize_json(value["type"])
    out["title"] = value["title"]
    import capo_continuum.types.finding_severity_id

    out["severity"] = capo_continuum.types.finding_severity_id.serialize_json(
        value["severity"]
    )
    if "summary" in value:
        out["summary"] = value["summary"]
    if "detailed_description" in value:
        out["detailedDescription"] = value["detailed_description"]
    if "category" in value:
        out["category"] = value["category"]
    if "sub_category" in value:
        out["subCategory"] = value["sub_category"]
    if "cwe_ids" in value:
        import capo_continuum.types.cwe_id_list

        out["cweIds"] = capo_continuum.types.cwe_id_list.serialize_json(
            value["cwe_ids"]
        )
    if "owasp_category" in value:
        out["owaspCategory"] = value["owasp_category"]
    if "mitigation" in value:
        out["mitigation"] = value["mitigation"]
    if "file_path" in value:
        out["filePath"] = value["file_path"]
    if "line_number" in value:
        out["lineNumber"] = value["line_number"]
    if "cve_id" in value:
        out["cveId"] = value["cve_id"]
    if "cvss_base_score" in value:
        out["cvssBaseScore"] = (
            "NaN"
            if value["cvss_base_score"] != value["cvss_base_score"]
            else "Infinity"
            if value["cvss_base_score"] == float("inf")
            else "-Infinity"
            if value["cvss_base_score"] == float("-inf")
            else value["cvss_base_score"]
        )
    if "affected_packages" in value:
        import capo_continuum.types.affected_package_list

        out["affectedPackages"] = (
            capo_continuum.types.affected_package_list.serialize_json(
                value["affected_packages"]
            )
        )
    if "vulnerable_code" in value:
        out["vulnerableCode"] = value["vulnerable_code"]
    if "relevant_inputs" in value:
        import capo_continuum.types.finding_string_list

        out["relevantInputs"] = capo_continuum.types.finding_string_list.serialize_json(
            value["relevant_inputs"]
        )
    if "steps_to_reproduce" in value:
        import capo_continuum.types.finding_string_list

        out["stepsToReproduce"] = (
            capo_continuum.types.finding_string_list.serialize_json(
                value["steps_to_reproduce"]
            )
        )
    if "validation" in value:
        import capo_continuum.types.finding_validation

        out["validation"] = capo_continuum.types.finding_validation.serialize_json(
            value["validation"]
        )
    if "end_line" in value:
        out["endLine"] = value["end_line"]
    if "mitre_techniques" in value:
        import capo_continuum.types.finding_string_list

        out["mitreTechniques"] = (
            capo_continuum.types.finding_string_list.serialize_json(
                value["mitre_techniques"]
            )
        )
    if "remediation_references" in value:
        import capo_continuum.types.finding_string_list

        out["remediationReferences"] = (
            capo_continuum.types.finding_string_list.serialize_json(
                value["remediation_references"]
            )
        )
    if "ocsf_class" in value:
        import capo_continuum.types.finding_ocsf_class

        out["ocsfClass"] = capo_continuum.types.finding_ocsf_class.serialize_json(
            value["ocsf_class"]
        )
    if "ocsf_schema_version" in value:
        out["ocsfSchemaVersion"] = value["ocsf_schema_version"]
    if "product_name" in value:
        out["productName"] = value["product_name"]
    if "product_vendor_name" in value:
        out["productVendorName"] = value["product_vendor_name"]
    if "product_version" in value:
        out["productVersion"] = value["product_version"]
    if "source_status" in value:
        out["sourceStatus"] = value["source_status"]
    if "source_status_id" in value:
        out["sourceStatusId"] = value["source_status_id"]
    if "first_seen_at" in value:
        import capo_continuum._protocol.serialize

        out["firstSeenAt"] = capo_continuum._protocol.serialize.fmt_date_time(
            value["first_seen_at"]
        )
    if "finding_types" in value:
        import capo_continuum.types.finding_string_list

        out["findingTypes"] = capo_continuum.types.finding_string_list.serialize_json(
            value["finding_types"]
        )
    if "vulnerabilities" in value:
        import capo_continuum.types.finding_vulnerability_list

        out["vulnerabilities"] = (
            capo_continuum.types.finding_vulnerability_list.serialize_json(
                value["vulnerabilities"]
            )
        )
    if "resources" in value:
        import capo_continuum.types.finding_resource_list

        out["resources"] = capo_continuum.types.finding_resource_list.serialize_json(
            value["resources"]
        )
    if "posture" in value:
        import capo_continuum.types.finding_posture

        out["posture"] = capo_continuum.types.finding_posture.serialize_json(
            value["posture"]
        )
    out["findingId"] = value["finding_id"]
    out["findingArn"] = value["finding_arn"]
    out["environmentId"] = value["environment_id"]
    out["source"] = value["source"]
    out["sourceFindingId"] = value["source_finding_id"]
    import capo_continuum._protocol.serialize

    out["reportedAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["reported_at"]
    )
    import capo_continuum.types.finding_status

    out["status"] = capo_continuum.types.finding_status.serialize_json(value["status"])
    import capo_continuum._protocol.serialize

    out["statusUpdatedAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["status_updated_at"]
    )
    import capo_continuum._protocol.serialize

    out["createdAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "scan_run_id" in value:
        out["scanRunId"] = value["scan_run_id"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "discard_reason" in value:
        import capo_continuum.types.finding_discard_reason

        out["discardReason"] = (
            capo_continuum.types.finding_discard_reason.serialize_json(
                value["discard_reason"]
            )
        )
    if "discard_reasoning" in value:
        out["discardReasoning"] = value["discard_reasoning"]
    if "duplicate_of_issue_id" in value:
        out["duplicateOfIssueId"] = value["duplicate_of_issue_id"]
    if "created_issue_id" in value:
        out["createdIssueId"] = value["created_issue_id"]
    if "completed_at" in value:
        import capo_continuum._protocol.serialize

        out["completedAt"] = capo_continuum._protocol.serialize.fmt_date_time(
            value["completed_at"]
        )
    return out


def deserialize_json(data: dict) -> GetCodeFindingOutput:
    out: GetCodeFindingOutput = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_continuum.types.finding_type

        out["type"] = capo_continuum.types.finding_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_continuum.types.finding_type.FindingType", "")
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("severity") is not None:
        import capo_continuum.types.finding_severity_id

        out["severity"] = capo_continuum.types.finding_severity_id.deserialize_json(
            data["severity"]
        )
    else:
        import typing

        out["severity"] = typing.cast(
            "capo_continuum.types.finding_severity_id.FindingSeverityId", ""
        )
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("detailedDescription") is not None:
        out["detailed_description"] = data["detailedDescription"]
    if data.get("category") is not None:
        out["category"] = data["category"]
    if data.get("subCategory") is not None:
        out["sub_category"] = data["subCategory"]
    if data.get("cweIds") is not None:
        import capo_continuum.types.cwe_id_list

        out["cwe_ids"] = capo_continuum.types.cwe_id_list.deserialize_json(
            data["cweIds"]
        )
    if data.get("owaspCategory") is not None:
        out["owasp_category"] = data["owaspCategory"]
    if data.get("mitigation") is not None:
        out["mitigation"] = data["mitigation"]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    if data.get("lineNumber") is not None:
        out["line_number"] = data["lineNumber"]
    if data.get("cveId") is not None:
        out["cve_id"] = data["cveId"]
    if data.get("cvssBaseScore") is not None:
        out["cvss_base_score"] = float(data["cvssBaseScore"])
    if data.get("affectedPackages") is not None:
        import capo_continuum.types.affected_package_list

        out["affected_packages"] = (
            capo_continuum.types.affected_package_list.deserialize_json(
                data["affectedPackages"]
            )
        )
    if data.get("vulnerableCode") is not None:
        out["vulnerable_code"] = data["vulnerableCode"]
    if data.get("relevantInputs") is not None:
        import capo_continuum.types.finding_string_list

        out["relevant_inputs"] = (
            capo_continuum.types.finding_string_list.deserialize_json(
                data["relevantInputs"]
            )
        )
    if data.get("stepsToReproduce") is not None:
        import capo_continuum.types.finding_string_list

        out["steps_to_reproduce"] = (
            capo_continuum.types.finding_string_list.deserialize_json(
                data["stepsToReproduce"]
            )
        )
    if data.get("validation") is not None:
        import capo_continuum.types.finding_validation

        out["validation"] = capo_continuum.types.finding_validation.deserialize_json(
            data["validation"]
        )
    if data.get("endLine") is not None:
        out["end_line"] = data["endLine"]
    if data.get("mitreTechniques") is not None:
        import capo_continuum.types.finding_string_list

        out["mitre_techniques"] = (
            capo_continuum.types.finding_string_list.deserialize_json(
                data["mitreTechniques"]
            )
        )
    if data.get("remediationReferences") is not None:
        import capo_continuum.types.finding_string_list

        out["remediation_references"] = (
            capo_continuum.types.finding_string_list.deserialize_json(
                data["remediationReferences"]
            )
        )
    if data.get("ocsfClass") is not None:
        import capo_continuum.types.finding_ocsf_class

        out["ocsf_class"] = capo_continuum.types.finding_ocsf_class.deserialize_json(
            data["ocsfClass"]
        )
    if data.get("ocsfSchemaVersion") is not None:
        out["ocsf_schema_version"] = data["ocsfSchemaVersion"]
    if data.get("productName") is not None:
        out["product_name"] = data["productName"]
    if data.get("productVendorName") is not None:
        out["product_vendor_name"] = data["productVendorName"]
    if data.get("productVersion") is not None:
        out["product_version"] = data["productVersion"]
    if data.get("sourceStatus") is not None:
        out["source_status"] = data["sourceStatus"]
    if data.get("sourceStatusId") is not None:
        out["source_status_id"] = data["sourceStatusId"]
    if data.get("firstSeenAt") is not None:
        import datetime

        out["first_seen_at"] = datetime.datetime.fromisoformat(
            data["firstSeenAt"].replace("Z", "+00:00")
        )
    if data.get("findingTypes") is not None:
        import capo_continuum.types.finding_string_list

        out["finding_types"] = (
            capo_continuum.types.finding_string_list.deserialize_json(
                data["findingTypes"]
            )
        )
    if data.get("vulnerabilities") is not None:
        import capo_continuum.types.finding_vulnerability_list

        out["vulnerabilities"] = (
            capo_continuum.types.finding_vulnerability_list.deserialize_json(
                data["vulnerabilities"]
            )
        )
    if data.get("resources") is not None:
        import capo_continuum.types.finding_resource_list

        out["resources"] = capo_continuum.types.finding_resource_list.deserialize_json(
            data["resources"]
        )
    if data.get("posture") is not None:
        import capo_continuum.types.finding_posture

        out["posture"] = capo_continuum.types.finding_posture.deserialize_json(
            data["posture"]
        )
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    else:
        out["finding_id"] = ""
    if data.get("findingArn") is not None:
        out["finding_arn"] = data["findingArn"]
    else:
        out["finding_arn"] = ""
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("sourceFindingId") is not None:
        out["source_finding_id"] = data["sourceFindingId"]
    else:
        out["source_finding_id"] = ""
    if data.get("reportedAt") is not None:
        import datetime

        out["reported_at"] = datetime.datetime.fromisoformat(
            data["reportedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["reported_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("status") is not None:
        import capo_continuum.types.finding_status

        out["status"] = capo_continuum.types.finding_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_continuum.types.finding_status.FindingStatus", ""
        )
    if data.get("statusUpdatedAt") is not None:
        import datetime

        out["status_updated_at"] = datetime.datetime.fromisoformat(
            data["statusUpdatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["status_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("scanRunId") is not None:
        out["scan_run_id"] = data["scanRunId"]
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("discardReason") is not None:
        import capo_continuum.types.finding_discard_reason

        out["discard_reason"] = (
            capo_continuum.types.finding_discard_reason.deserialize_json(
                data["discardReason"]
            )
        )
    if data.get("discardReasoning") is not None:
        out["discard_reasoning"] = data["discardReasoning"]
    if data.get("duplicateOfIssueId") is not None:
        out["duplicate_of_issue_id"] = data["duplicateOfIssueId"]
    if data.get("createdIssueId") is not None:
        out["created_issue_id"] = data["createdIssueId"]
    if data.get("completedAt") is not None:
        import datetime

        out["completed_at"] = datetime.datetime.fromisoformat(
            data["completedAt"].replace("Z", "+00:00")
        )
    return out
