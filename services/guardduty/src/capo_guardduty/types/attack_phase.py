"""Generated from Smithy shape ``com.amazonaws.guardduty#AttackPhase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.attack_phase_name
    import capo_guardduty.types.attacks
    import capo_guardduty.types.string


class AttackPhase(TypedDict, closed=True):
    phase: NotRequired["capo_guardduty.types.attack_phase_name.AttackPhaseName"]
    """<p>The MITRE ATT&amp;CK tactic of the phase. Possible values are <code>Reconnaissance</code>, <code>Resource Development</code>, <code>Initial Access</code>, <code>Execution</code>, <code>Persistence</code>, <code>Privilege Escalation</code>, <code>Defense Evasion</code>, <code>Credential Access</code>, <code>Discovery</code>, <code>Lateral Movement</code>, <code>Collection</code>, <code>Command and Control</code>, <code>Exfiltration</code>, and <code>Impact</code>.</p>"""
    description: NotRequired["capo_guardduty.types.string.String"]
    """<p>A description of the activity in this phase.</p>"""
    attacks: NotRequired["capo_guardduty.types.attacks.Attacks"]
    """<p>The MITRE ATT&amp;CK tactics and techniques observed in this phase, with the findings that are associated with them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttackPhase) -> dict:
    out: dict = {}
    if "phase" in value:
        import capo_guardduty.types.attack_phase_name

        out["phase"] = capo_guardduty.types.attack_phase_name.serialize_json(
            value["phase"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "attacks" in value:
        import capo_guardduty.types.attacks

        out["attacks"] = capo_guardduty.types.attacks.serialize_json(value["attacks"])
    return out


def deserialize_json(data: dict) -> AttackPhase:
    out: AttackPhase = {}  # type: ignore[typeddict-item]
    if data.get("phase") is not None:
        import capo_guardduty.types.attack_phase_name

        out["phase"] = capo_guardduty.types.attack_phase_name.deserialize_json(
            data["phase"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("attacks") is not None:
        import capo_guardduty.types.attacks

        out["attacks"] = capo_guardduty.types.attacks.deserialize_json(data["attacks"])
    return out
