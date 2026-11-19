"""Generated from Smithy shape ``com.amazonaws.guardduty#TacticCoverage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.attack_phase_name
    import capo_guardduty.types.finding_type_names
    import capo_guardduty.types.integer
    import capo_guardduty.types.technique_coverages


class TacticCoverage(TypedDict, closed=True):
    phase: NotRequired["capo_guardduty.types.attack_phase_name.AttackPhaseName"]
    """<p>The name of the tactic. Possible values are <code>Reconnaissance</code>, <code>Resource Development</code>, <code>Initial Access</code>, <code>Execution</code>, <code>Persistence</code>, <code>Privilege Escalation</code>, <code>Defense Evasion</code>, <code>Credential Access</code>, <code>Discovery</code>, <code>Lateral Movement</code>, <code>Collection</code>, <code>Command and Control</code>, <code>Exfiltration</code>, and <code>Impact</code>.</p>"""
    finding_count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of findings associated with the tactic.</p>"""
    finding_types: NotRequired[
        "capo_guardduty.types.finding_type_names.FindingTypeNames"
    ]
    """<p>The finding types associated with the tactic.</p>"""
    techniques: NotRequired[
        "capo_guardduty.types.technique_coverages.TechniqueCoverages"
    ]
    """<p>The MITRE ATT&amp;CK techniques within the tactic that are associated with findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TacticCoverage) -> dict:
    out: dict = {}
    if "phase" in value:
        import capo_guardduty.types.attack_phase_name

        out["phase"] = capo_guardduty.types.attack_phase_name.serialize_json(
            value["phase"]
        )
    if "finding_count" in value:
        out["findingCount"] = value["finding_count"]
    if "finding_types" in value:
        import capo_guardduty.types.finding_type_names

        out["findingTypes"] = capo_guardduty.types.finding_type_names.serialize_json(
            value["finding_types"]
        )
    if "techniques" in value:
        import capo_guardduty.types.technique_coverages

        out["techniques"] = capo_guardduty.types.technique_coverages.serialize_json(
            value["techniques"]
        )
    return out


def deserialize_json(data: dict) -> TacticCoverage:
    out: TacticCoverage = {}  # type: ignore[typeddict-item]
    if data.get("phase") is not None:
        import capo_guardduty.types.attack_phase_name

        out["phase"] = capo_guardduty.types.attack_phase_name.deserialize_json(
            data["phase"]
        )
    if data.get("findingCount") is not None:
        out["finding_count"] = data["findingCount"]
    if data.get("findingTypes") is not None:
        import capo_guardduty.types.finding_type_names

        out["finding_types"] = capo_guardduty.types.finding_type_names.deserialize_json(
            data["findingTypes"]
        )
    if data.get("techniques") is not None:
        import capo_guardduty.types.technique_coverages

        out["techniques"] = capo_guardduty.types.technique_coverages.deserialize_json(
            data["techniques"]
        )
    return out
