"""Generated from Smithy shape ``com.amazonaws.continuum#SignalPrecondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.artifact_text
    import capo_continuum.types.signal_basis


class SignalPrecondition(TypedDict, closed=True):
    value: NotRequired["bool"]
    """The producer's determination. A Boolean rather than an enum, against the Common Terms preference for enums on extensibility grounds. The question each precondition answers is closed — is the code reachable, is configuration required, must a user other than the attacker interact — and the only third state, "not determined", is already expressed by omitting this member, which the projection does whenever the stored value is not a bool. An enum would give two ways to say the same thing, while `basis` and `missingInfo` already qualify how firm the answer is."""
    basis: NotRequired["capo_continuum.types.signal_basis.SignalBasis"]
    """Where the producer's determination came from."""
    reason: NotRequired["capo_continuum.types.artifact_text.ArtifactText"]
    """The producer's explanation."""
    missing_info: NotRequired["capo_continuum.types.artifact_text.ArtifactText"]
    """What the producer could not determine, when anything was missing."""


# --- restJson1 ser/de ---
def serialize_json(value: SignalPrecondition) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "basis" in value:
        import capo_continuum.types.signal_basis

        out["basis"] = capo_continuum.types.signal_basis.serialize_json(value["basis"])
    if "reason" in value:
        out["reason"] = value["reason"]
    if "missing_info" in value:
        out["missingInfo"] = value["missing_info"]
    return out


def deserialize_json(data: dict) -> SignalPrecondition:
    out: SignalPrecondition = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("basis") is not None:
        import capo_continuum.types.signal_basis

        out["basis"] = capo_continuum.types.signal_basis.deserialize_json(data["basis"])
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("missingInfo") is not None:
        out["missing_info"] = data["missingInfo"]
    return out
