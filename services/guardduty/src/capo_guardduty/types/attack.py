"""Generated from Smithy shape ``com.amazonaws.guardduty#Attack``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.finding_references
    import capo_guardduty.types.string
    import capo_guardduty.types.threat_reference


class Attack(TypedDict, closed=True):
    tactic: NotRequired["capo_guardduty.types.threat_reference.ThreatReference"]
    """<p>The MITRE ATT&amp;CK tactic.</p>"""
    technique: NotRequired["capo_guardduty.types.threat_reference.ThreatReference"]
    """<p>The MITRE ATT&amp;CK technique.</p>"""
    findings: NotRequired["capo_guardduty.types.finding_references.FindingReferences"]
    """<p>The findings associated with the tactic and technique.</p>"""
    version: NotRequired["capo_guardduty.types.string.String"]
    """<p>The version of the attack framework that the tactic and technique classification uses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Attack) -> dict:
    out: dict = {}
    if "tactic" in value:
        import capo_guardduty.types.threat_reference

        out["tactic"] = capo_guardduty.types.threat_reference.serialize_json(
            value["tactic"]
        )
    if "technique" in value:
        import capo_guardduty.types.threat_reference

        out["technique"] = capo_guardduty.types.threat_reference.serialize_json(
            value["technique"]
        )
    if "findings" in value:
        import capo_guardduty.types.finding_references

        out["findings"] = capo_guardduty.types.finding_references.serialize_json(
            value["findings"]
        )
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> Attack:
    out: Attack = {}  # type: ignore[typeddict-item]
    if data.get("tactic") is not None:
        import capo_guardduty.types.threat_reference

        out["tactic"] = capo_guardduty.types.threat_reference.deserialize_json(
            data["tactic"]
        )
    if data.get("technique") is not None:
        import capo_guardduty.types.threat_reference

        out["technique"] = capo_guardduty.types.threat_reference.deserialize_json(
            data["technique"]
        )
    if data.get("findings") is not None:
        import capo_guardduty.types.finding_references

        out["findings"] = capo_guardduty.types.finding_references.deserialize_json(
            data["findings"]
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
