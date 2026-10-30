"""Generated from Smithy shape ``com.amazonaws.continuum#SignalAccessPrecondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.artifact_text
    import capo_continuum.types.signal_access_level
    import capo_continuum.types.signal_basis


class SignalAccessPrecondition(TypedDict, closed=True):
    value: NotRequired["capo_continuum.types.signal_access_level.SignalAccessLevel"]
    """The level of access exploitation requires. Absent when the producer reported a level with no mapping yet."""
    basis: NotRequired["capo_continuum.types.signal_basis.SignalBasis"]
    """Where the producer's determination came from."""
    reason: NotRequired["capo_continuum.types.artifact_text.ArtifactText"]
    """The producer's explanation."""
    missing_info: NotRequired["capo_continuum.types.artifact_text.ArtifactText"]
    """What the producer could not determine, when anything was missing."""


# --- restJson1 ser/de ---
def serialize_json(value: SignalAccessPrecondition) -> dict:
    out: dict = {}
    if "value" in value:
        import capo_continuum.types.signal_access_level

        out["value"] = capo_continuum.types.signal_access_level.serialize_json(
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


def deserialize_json(data: dict) -> SignalAccessPrecondition:
    out: SignalAccessPrecondition = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        import capo_continuum.types.signal_access_level

        out["value"] = capo_continuum.types.signal_access_level.deserialize_json(
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
