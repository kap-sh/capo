"""Generated from Smithy shape ``com.amazonaws.continuum#SignalImpactDimensions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.signal_attacker_gains_dimension
    import capo_continuum.types.signal_blast_radius_dimension
    import capo_continuum.types.signal_target_value_dimension


class SignalImpactDimensions(TypedDict, closed=True):
    attacker_gains: NotRequired[
        "capo_continuum.types.signal_attacker_gains_dimension.SignalAttackerGainsDimension"
    ]
    """What the attacker gains from exploitation."""
    blast_radius: NotRequired[
        "capo_continuum.types.signal_blast_radius_dimension.SignalBlastRadiusDimension"
    ]
    """How far the consequences reach."""
    target_value: NotRequired[
        "capo_continuum.types.signal_target_value_dimension.SignalTargetValueDimension"
    ]
    """How valuable the target is, which can shift the band off its base value."""


# --- restJson1 ser/de ---
def serialize_json(value: SignalImpactDimensions) -> dict:
    out: dict = {}
    if "attacker_gains" in value:
        import capo_continuum.types.signal_attacker_gains_dimension

        out["attackerGains"] = (
            capo_continuum.types.signal_attacker_gains_dimension.serialize_json(
                value["attacker_gains"]
            )
        )
    if "blast_radius" in value:
        import capo_continuum.types.signal_blast_radius_dimension

        out["blastRadius"] = (
            capo_continuum.types.signal_blast_radius_dimension.serialize_json(
                value["blast_radius"]
            )
        )
    if "target_value" in value:
        import capo_continuum.types.signal_target_value_dimension

        out["targetValue"] = (
            capo_continuum.types.signal_target_value_dimension.serialize_json(
                value["target_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> SignalImpactDimensions:
    out: SignalImpactDimensions = {}  # type: ignore[typeddict-item]
    if data.get("attackerGains") is not None:
        import capo_continuum.types.signal_attacker_gains_dimension

        out["attacker_gains"] = (
            capo_continuum.types.signal_attacker_gains_dimension.deserialize_json(
                data["attackerGains"]
            )
        )
    if data.get("blastRadius") is not None:
        import capo_continuum.types.signal_blast_radius_dimension

        out["blast_radius"] = (
            capo_continuum.types.signal_blast_radius_dimension.deserialize_json(
                data["blastRadius"]
            )
        )
    if data.get("targetValue") is not None:
        import capo_continuum.types.signal_target_value_dimension

        out["target_value"] = (
            capo_continuum.types.signal_target_value_dimension.deserialize_json(
                data["targetValue"]
            )
        )
    return out
