"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.attack_phases
    import capo_guardduty.types.string


class ThreatAssessment(TypedDict, closed=True):
    attack_progression: NotRequired["capo_guardduty.types.attack_phases.AttackPhases"]
    """<p>The phases of the attack, in terms of MITRE ATT&amp;CK tactics.</p>"""
    threat_actor_profile: NotRequired["capo_guardduty.types.string.String"]
    """<p>A description of the likely threat actor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatAssessment) -> dict:
    out: dict = {}
    if "attack_progression" in value:
        import capo_guardduty.types.attack_phases

        out["attackProgression"] = capo_guardduty.types.attack_phases.serialize_json(
            value["attack_progression"]
        )
    if "threat_actor_profile" in value:
        out["threatActorProfile"] = value["threat_actor_profile"]
    return out


def deserialize_json(data: dict) -> ThreatAssessment:
    out: ThreatAssessment = {}  # type: ignore[typeddict-item]
    if data.get("attackProgression") is not None:
        import capo_guardduty.types.attack_phases

        out["attack_progression"] = capo_guardduty.types.attack_phases.deserialize_json(
            data["attackProgression"]
        )
    if data.get("threatActorProfile") is not None:
        out["threat_actor_profile"] = data["threatActorProfile"]
    return out
