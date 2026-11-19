"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionCoverage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.foundational_data_sources
    import capo_guardduty.types.investigation_text
    import capo_guardduty.types.protection_plans


class DetectionCoverage(TypedDict, closed=True):
    protection_plans: NotRequired[
        "capo_guardduty.types.protection_plans.ProtectionPlans"
    ]
    """<p>The protection plans and their status.</p>"""
    foundational_data_sources: NotRequired[
        "capo_guardduty.types.foundational_data_sources.FoundationalDataSources"
    ]
    """<p>The foundational data sources, such as <code>CLOUD_TRAIL</code>, <code>DNS_LOGS</code>, and <code>FLOW_LOGS</code>.</p>"""
    coverage_gaps: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>A description of the gaps in detection coverage. A record doesn't include both <code>CoverageGaps</code> and <code>KeyObservation</code>.</p>"""
    key_observation: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>A key observation about detection coverage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectionCoverage) -> dict:
    out: dict = {}
    if "protection_plans" in value:
        import capo_guardduty.types.protection_plans

        out["protectionPlans"] = capo_guardduty.types.protection_plans.serialize_json(
            value["protection_plans"]
        )
    if "foundational_data_sources" in value:
        import capo_guardduty.types.foundational_data_sources

        out["foundationalDataSources"] = (
            capo_guardduty.types.foundational_data_sources.serialize_json(
                value["foundational_data_sources"]
            )
        )
    if "coverage_gaps" in value:
        out["coverageGaps"] = value["coverage_gaps"]
    if "key_observation" in value:
        out["keyObservation"] = value["key_observation"]
    return out


def deserialize_json(data: dict) -> DetectionCoverage:
    out: DetectionCoverage = {}  # type: ignore[typeddict-item]
    if data.get("protectionPlans") is not None:
        import capo_guardduty.types.protection_plans

        out["protection_plans"] = (
            capo_guardduty.types.protection_plans.deserialize_json(
                data["protectionPlans"]
            )
        )
    if data.get("foundationalDataSources") is not None:
        import capo_guardduty.types.foundational_data_sources

        out["foundational_data_sources"] = (
            capo_guardduty.types.foundational_data_sources.deserialize_json(
                data["foundationalDataSources"]
            )
        )
    if data.get("coverageGaps") is not None:
        out["coverage_gaps"] = data["coverageGaps"]
    if data.get("keyObservation") is not None:
        out["key_observation"] = data["keyObservation"]
    return out
