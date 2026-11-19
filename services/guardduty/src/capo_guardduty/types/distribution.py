"""Generated from Smithy shape ``com.amazonaws.guardduty#Distribution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.archive_distribution
    import capo_guardduty.types.count
    import capo_guardduty.types.distribution_dimension
    import capo_guardduty.types.finding_type_counts
    import capo_guardduty.types.resource_distributions
    import capo_guardduty.types.severity_breakdown
    import capo_guardduty.types.tactic_coverages
    import capo_guardduty.types.type_distributions


class Distribution(TypedDict, closed=True):
    dimension: NotRequired[
        "capo_guardduty.types.distribution_dimension.DistributionDimension"
    ]
    """<p>The dimension of the breakdown. The value identifies the breakdown that the record describes: <code>SEVERITY</code> (<code>SeverityBreakdown</code>), <code>TYPE</code> (<code>FindingTypes</code> or <code>TopFindingTypes</code>), <code>RESOURCE</code> (<code>Resources</code>), <code>ATTACK_VECTOR</code> (<code>AttackVectors</code>), and <code>ARCHIVE</code> (<code>Archive</code>).</p>"""
    total_findings: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The total number of findings in the breakdown.</p>"""
    severity_breakdown: NotRequired[
        "capo_guardduty.types.severity_breakdown.SeverityBreakdown"
    ]
    """<p>The number of findings at each severity level.</p>"""
    finding_types: NotRequired[
        "capo_guardduty.types.type_distributions.TypeDistributions"
    ]
    """<p>The findings broken down by finding type, with counts and percentages.</p>"""
    top_finding_types: NotRequired[
        "capo_guardduty.types.finding_type_counts.FindingTypeCounts"
    ]
    """<p>The finding types that have the most findings, with counts.</p>"""
    resources: NotRequired[
        "capo_guardduty.types.resource_distributions.ResourceDistributions"
    ]
    """<p>The findings broken down by affected resource.</p>"""
    attack_vectors: NotRequired["capo_guardduty.types.tactic_coverages.TacticCoverages"]
    """<p>The findings broken down by MITRE ATT&amp;CK tactic.</p>"""
    archive: NotRequired[
        "capo_guardduty.types.archive_distribution.ArchiveDistribution"
    ]
    """<p>The number and percentage of archived and unarchived findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Distribution) -> dict:
    out: dict = {}
    if "dimension" in value:
        import capo_guardduty.types.distribution_dimension

        out["dimension"] = capo_guardduty.types.distribution_dimension.serialize_json(
            value["dimension"]
        )
    if "total_findings" in value:
        out["totalFindings"] = value["total_findings"]
    if "severity_breakdown" in value:
        import capo_guardduty.types.severity_breakdown

        out["severityBreakdown"] = (
            capo_guardduty.types.severity_breakdown.serialize_json(
                value["severity_breakdown"]
            )
        )
    if "finding_types" in value:
        import capo_guardduty.types.type_distributions

        out["findingTypes"] = capo_guardduty.types.type_distributions.serialize_json(
            value["finding_types"]
        )
    if "top_finding_types" in value:
        import capo_guardduty.types.finding_type_counts

        out["topFindingTypes"] = (
            capo_guardduty.types.finding_type_counts.serialize_json(
                value["top_finding_types"]
            )
        )
    if "resources" in value:
        import capo_guardduty.types.resource_distributions

        out["resources"] = capo_guardduty.types.resource_distributions.serialize_json(
            value["resources"]
        )
    if "attack_vectors" in value:
        import capo_guardduty.types.tactic_coverages

        out["attackVectors"] = capo_guardduty.types.tactic_coverages.serialize_json(
            value["attack_vectors"]
        )
    if "archive" in value:
        import capo_guardduty.types.archive_distribution

        out["archive"] = capo_guardduty.types.archive_distribution.serialize_json(
            value["archive"]
        )
    return out


def deserialize_json(data: dict) -> Distribution:
    out: Distribution = {}  # type: ignore[typeddict-item]
    if data.get("dimension") is not None:
        import capo_guardduty.types.distribution_dimension

        out["dimension"] = capo_guardduty.types.distribution_dimension.deserialize_json(
            data["dimension"]
        )
    if data.get("totalFindings") is not None:
        out["total_findings"] = data["totalFindings"]
    if data.get("severityBreakdown") is not None:
        import capo_guardduty.types.severity_breakdown

        out["severity_breakdown"] = (
            capo_guardduty.types.severity_breakdown.deserialize_json(
                data["severityBreakdown"]
            )
        )
    if data.get("findingTypes") is not None:
        import capo_guardduty.types.type_distributions

        out["finding_types"] = capo_guardduty.types.type_distributions.deserialize_json(
            data["findingTypes"]
        )
    if data.get("topFindingTypes") is not None:
        import capo_guardduty.types.finding_type_counts

        out["top_finding_types"] = (
            capo_guardduty.types.finding_type_counts.deserialize_json(
                data["topFindingTypes"]
            )
        )
    if data.get("resources") is not None:
        import capo_guardduty.types.resource_distributions

        out["resources"] = capo_guardduty.types.resource_distributions.deserialize_json(
            data["resources"]
        )
    if data.get("attackVectors") is not None:
        import capo_guardduty.types.tactic_coverages

        out["attack_vectors"] = capo_guardduty.types.tactic_coverages.deserialize_json(
            data["attackVectors"]
        )
    if data.get("archive") is not None:
        import capo_guardduty.types.archive_distribution

        out["archive"] = capo_guardduty.types.archive_distribution.deserialize_json(
            data["archive"]
        )
    return out
