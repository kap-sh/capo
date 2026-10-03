"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlDomainInsights``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control_domain_id
    import capo_auditmanager.types.evidence_insights
    import capo_auditmanager.types.nullable_integer
    import capo_auditmanager.types.string
    import capo_auditmanager.types.timestamp


class ControlDomainInsights(TypedDict, closed=True):
    name: NotRequired["capo_auditmanager.types.string.String"]
    """<p>The name of the control domain. </p>"""
    id: NotRequired["capo_auditmanager.types.control_domain_id.ControlDomainId"]
    """<p>The unique identifier for the control domain. Audit Manager supports the control domains that are provided by Amazon Web Services Control Catalog. For information about how to find a list of available control domains, see <a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html"> <code>ListDomains</code> </a> in the Amazon Web Services Control Catalog API Reference.</p>"""
    controls_count_by_noncompliant_evidence: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of controls in the control domain that collected non-compliant evidence on the <code>lastUpdated</code> date. </p>"""
    total_controls_count: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The total number of controls in the control domain. </p>"""
    evidence_insights: NotRequired[
        "capo_auditmanager.types.evidence_insights.EvidenceInsights"
    ]
    """<p>A breakdown of the compliance check status for the evidence that’s associated with the control domain. </p>"""
    last_updated: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p>The time when the control domain insights were last updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlDomainInsights) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "controls_count_by_noncompliant_evidence" in value:
        out["controlsCountByNoncompliantEvidence"] = value[
            "controls_count_by_noncompliant_evidence"
        ]
    if "total_controls_count" in value:
        out["totalControlsCount"] = value["total_controls_count"]
    if "evidence_insights" in value:
        import capo_auditmanager.types.evidence_insights

        out["evidenceInsights"] = (
            capo_auditmanager.types.evidence_insights.serialize_json(
                value["evidence_insights"]
            )
        )
    if "last_updated" in value:
        import capo_auditmanager.types.timestamp

        out["lastUpdated"] = capo_auditmanager.types.timestamp.serialize_json(
            value["last_updated"]
        )
    return out


def deserialize_json(data: dict) -> ControlDomainInsights:
    out: ControlDomainInsights = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("controlsCountByNoncompliantEvidence") is not None:
        out["controls_count_by_noncompliant_evidence"] = data[
            "controlsCountByNoncompliantEvidence"
        ]
    if data.get("totalControlsCount") is not None:
        out["total_controls_count"] = data["totalControlsCount"]
    if data.get("evidenceInsights") is not None:
        import capo_auditmanager.types.evidence_insights

        out["evidence_insights"] = (
            capo_auditmanager.types.evidence_insights.deserialize_json(
                data["evidenceInsights"]
            )
        )
    if data.get("lastUpdated") is not None:
        import capo_auditmanager.types.timestamp

        out["last_updated"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["lastUpdated"]
        )
    return out
