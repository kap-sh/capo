"""Generated from Smithy shape ``com.amazonaws.continuum#SignalComputation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.signal_band


class SignalComputation(TypedDict, closed=True):
    likelihood_band: NotRequired["capo_continuum.types.signal_band.SignalBand"]
    """Computed likelihood band, on a likelihood signal."""
    impact_band: NotRequired["capo_continuum.types.signal_band.SignalBand"]
    """Computed impact band, on an impact signal."""
    barriers: NotRequired["int"]
    """How many of the four exploit preconditions act as barriers (0-4)."""


# --- restJson1 ser/de ---
def serialize_json(value: SignalComputation) -> dict:
    out: dict = {}
    if "likelihood_band" in value:
        import capo_continuum.types.signal_band

        out["likelihoodBand"] = capo_continuum.types.signal_band.serialize_json(
            value["likelihood_band"]
        )
    if "impact_band" in value:
        import capo_continuum.types.signal_band

        out["impactBand"] = capo_continuum.types.signal_band.serialize_json(
            value["impact_band"]
        )
    if "barriers" in value:
        out["barriers"] = value["barriers"]
    return out


def deserialize_json(data: dict) -> SignalComputation:
    out: SignalComputation = {}  # type: ignore[typeddict-item]
    if data.get("likelihoodBand") is not None:
        import capo_continuum.types.signal_band

        out["likelihood_band"] = capo_continuum.types.signal_band.deserialize_json(
            data["likelihoodBand"]
        )
    if data.get("impactBand") is not None:
        import capo_continuum.types.signal_band

        out["impact_band"] = capo_continuum.types.signal_band.deserialize_json(
            data["impactBand"]
        )
    if data.get("barriers") is not None:
        out["barriers"] = data["barriers"]
    return out
