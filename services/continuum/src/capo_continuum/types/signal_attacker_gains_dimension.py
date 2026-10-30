"""Generated from Smithy shape ``com.amazonaws.continuum#SignalAttackerGainsDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.artifact_text
    import capo_continuum.types.signal_attacker_gains
    import capo_continuum.types.signal_basis


class SignalAttackerGainsDimension(TypedDict, closed=True):
    value: NotRequired["capo_continuum.types.signal_attacker_gains.SignalAttackerGains"]
    """The capability exploitation grants. Absent when the producer reported a value with no mapping yet."""
    basis: NotRequired["capo_continuum.types.signal_basis.SignalBasis"]
    """Where the producer's determination came from."""
    reason: NotRequired["capo_continuum.types.artifact_text.ArtifactText"]
    """The producer's explanation."""
    missing_info: NotRequired["capo_continuum.types.artifact_text.ArtifactText"]
    """What the producer could not determine, when anything was missing."""


# --- restJson1 ser/de ---
def serialize_json(value: SignalAttackerGainsDimension) -> dict:
    out: dict = {}
    if "value" in value:
        import capo_continuum.types.signal_attacker_gains

        out["value"] = capo_continuum.types.signal_attacker_gains.serialize_json(
            value["value"]
        )
    if "basis" in value:
        import capo_continuum.types.signal_basis

        out["basis"] = capo_continuum.types.signal_basis.serialize_json(value["basis"])
    if "reason" in value:
        out["reason"] = value["reason"]
    if "missing_info" in value:
        out["missingInfo"] = value["missing_info"]
    return out


def deserialize_json(data: dict) -> SignalAttackerGainsDimension:
    out: SignalAttackerGainsDimension = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        import capo_continuum.types.signal_attacker_gains

        out["value"] = capo_continuum.types.signal_attacker_gains.deserialize_json(
            data["value"]
        )
    if data.get("basis") is not None:
        import capo_continuum.types.signal_basis

        out["basis"] = capo_continuum.types.signal_basis.deserialize_json(data["basis"])
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("missingInfo") is not None:
        out["missing_info"] = data["missingInfo"]
    return out
