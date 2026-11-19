"""Generated from Smithy shape ``com.amazonaws.guardduty#TechniqueCoverage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.finding_type_names
    import capo_guardduty.types.integer
    import capo_guardduty.types.threat_reference


class TechniqueCoverage(TypedDict, closed=True):
    technique: NotRequired["capo_guardduty.types.threat_reference.ThreatReference"]
    """<p>The technique.</p>"""
    finding_count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of findings associated with the technique.</p>"""
    finding_types: NotRequired[
        "capo_guardduty.types.finding_type_names.FindingTypeNames"
    ]
    """<p>The finding types associated with the technique.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TechniqueCoverage) -> dict:
    out: dict = {}
    if "technique" in value:
        import capo_guardduty.types.threat_reference

        out["technique"] = capo_guardduty.types.threat_reference.serialize_json(
            value["technique"]
        )
    if "finding_count" in value:
        out["findingCount"] = value["finding_count"]
    if "finding_types" in value:
        import capo_guardduty.types.finding_type_names

        out["findingTypes"] = capo_guardduty.types.finding_type_names.serialize_json(
            value["finding_types"]
        )
    return out


def deserialize_json(data: dict) -> TechniqueCoverage:
    out: TechniqueCoverage = {}  # type: ignore[typeddict-item]
    if data.get("technique") is not None:
        import capo_guardduty.types.threat_reference

        out["technique"] = capo_guardduty.types.threat_reference.deserialize_json(
            data["technique"]
        )
    if data.get("findingCount") is not None:
        out["finding_count"] = data["findingCount"]
    if data.get("findingTypes") is not None:
        import capo_guardduty.types.finding_type_names

        out["finding_types"] = capo_guardduty.types.finding_type_names.deserialize_json(
            data["findingTypes"]
        )
    return out
