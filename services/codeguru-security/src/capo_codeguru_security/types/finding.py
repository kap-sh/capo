"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#Finding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_codeguru_security.types.detector_tags
    import capo_codeguru_security.types.remediation
    import capo_codeguru_security.types.resource
    import capo_codeguru_security.types.severity
    import capo_codeguru_security.types.status
    import capo_codeguru_security.types.vulnerability


class Finding(TypedDict, closed=True):
    created_at: NotRequired["datetime.datetime"]
    """<p>The time when the finding was created.</p>"""
    description: NotRequired["str"]
    """<p>A description of the finding.</p>"""
    generator_id: NotRequired["str"]
    """<p>The identifier for the component that generated a finding such as AmazonCodeGuruSecurity.</p>"""
    id: NotRequired["str"]
    """<p>The identifier for a finding.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The time when the finding was last updated. Findings are updated when you remediate them or when the finding code location changes. </p>"""
    type: NotRequired["str"]
    """<p>The type of finding. </p>"""
    status: NotRequired["capo_codeguru_security.types.status.Status"]
    """<p>The status of the finding. A finding status can be open or closed. </p>"""
    resource: NotRequired["capo_codeguru_security.types.resource.Resource"]
    """<p>The resource where Amazon CodeGuru Security detected a finding.</p>"""
    vulnerability: NotRequired[
        "capo_codeguru_security.types.vulnerability.Vulnerability"
    ]
    """<p>An object that describes the detected security vulnerability.</p>"""
    severity: NotRequired["capo_codeguru_security.types.severity.Severity"]
    """<p>The severity of the finding. Severity can be critical, high, medium, low, or informational. For information on severity levels, see <a href="https://docs.aws.amazon.com/codeguru/latest/security-ug/findings-overview.html#severity-distribution">Finding severity</a> in the <i>Amazon CodeGuru Security User Guide</i>.</p>"""
    remediation: NotRequired["capo_codeguru_security.types.remediation.Remediation"]
    """<p>An object that contains the details about how to remediate a finding.</p>"""
    title: NotRequired["str"]
    """<p>The title of the finding.</p>"""
    detector_tags: NotRequired[
        "capo_codeguru_security.types.detector_tags.DetectorTags"
    ]
    """<p>One or more tags or categorizations that are associated with a detector. These tags are defined by type, programming language, or other classification such as maintainability or consistency.</p>"""
    detector_id: NotRequired["str"]
    """<p>The identifier for the detector that detected the finding in your code. A detector is a defined rule based on industry standards and AWS best practices. </p>"""
    detector_name: NotRequired["str"]
    """<p>The name of the detector that identified the security vulnerability in your code. </p>"""
    rule_id: NotRequired["str"]
    """<p>The identifier for the rule that generated the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Finding) -> dict:
    out: dict = {}
    if "created_at" in value:
        import capo_codeguru_security.types._prelude.timestamp

        out["createdAt"] = (
            capo_codeguru_security.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "generator_id" in value:
        out["generatorId"] = value["generator_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "updated_at" in value:
        import capo_codeguru_security.types._prelude.timestamp

        out["updatedAt"] = (
            capo_codeguru_security.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    if "type" in value:
        out["type"] = value["type"]
    if "status" in value:
        import capo_codeguru_security.types.status

        out["status"] = capo_codeguru_security.types.status.serialize_json(
            value["status"]
        )
    if "resource" in value:
        import capo_codeguru_security.types.resource

        out["resource"] = capo_codeguru_security.types.resource.serialize_json(
            value["resource"]
        )
    if "vulnerability" in value:
        import capo_codeguru_security.types.vulnerability

        out["vulnerability"] = (
            capo_codeguru_security.types.vulnerability.serialize_json(
                value["vulnerability"]
            )
        )
    if "severity" in value:
        import capo_codeguru_security.types.severity

        out["severity"] = capo_codeguru_security.types.severity.serialize_json(
            value["severity"]
        )
    if "remediation" in value:
        import capo_codeguru_security.types.remediation

        out["remediation"] = capo_codeguru_security.types.remediation.serialize_json(
            value["remediation"]
        )
    if "title" in value:
        out["title"] = value["title"]
    if "detector_tags" in value:
        import capo_codeguru_security.types.detector_tags

        out["detectorTags"] = capo_codeguru_security.types.detector_tags.serialize_json(
            value["detector_tags"]
        )
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "detector_name" in value:
        out["detectorName"] = value["detector_name"]
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    return out


def deserialize_json(data: dict) -> Finding:
    out: Finding = {}  # type: ignore[typeddict-item]
    if data.get("createdAt") is not None:
        import capo_codeguru_security.types._prelude.timestamp

        out["created_at"] = (
            capo_codeguru_security.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("generatorId") is not None:
        out["generator_id"] = data["generatorId"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("updatedAt") is not None:
        import capo_codeguru_security.types._prelude.timestamp

        out["updated_at"] = (
            capo_codeguru_security.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("status") is not None:
        import capo_codeguru_security.types.status

        out["status"] = capo_codeguru_security.types.status.deserialize_json(
            data["status"]
        )
    if data.get("resource") is not None:
        import capo_codeguru_security.types.resource

        out["resource"] = capo_codeguru_security.types.resource.deserialize_json(
            data["resource"]
        )
    if data.get("vulnerability") is not None:
        import capo_codeguru_security.types.vulnerability

        out["vulnerability"] = (
            capo_codeguru_security.types.vulnerability.deserialize_json(
                data["vulnerability"]
            )
        )
    if data.get("severity") is not None:
        import capo_codeguru_security.types.severity

        out["severity"] = capo_codeguru_security.types.severity.deserialize_json(
            data["severity"]
        )
    if data.get("remediation") is not None:
        import capo_codeguru_security.types.remediation

        out["remediation"] = capo_codeguru_security.types.remediation.deserialize_json(
            data["remediation"]
        )
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("detectorTags") is not None:
        import capo_codeguru_security.types.detector_tags

        out["detector_tags"] = (
            capo_codeguru_security.types.detector_tags.deserialize_json(
                data["detectorTags"]
            )
        )
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    if data.get("detectorName") is not None:
        out["detector_name"] = data["detectorName"]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    return out
