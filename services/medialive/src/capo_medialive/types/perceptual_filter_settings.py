"""Generated from Smithy shape ``com.amazonaws.medialive#PerceptualFilterSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.perceptual_filter_strength


class PerceptualFilterSettings(TypedDict, closed=True):
    strength: NotRequired[
        "capo_medialive.types.perceptual_filter_strength.PerceptualFilterStrength"
    ]
    """Selects the perceptual noise filter strength. Strength 1 (perceptual lite) is the recommended default and adds approximately 30% of an AVC encode of compute on the highest rendition. Strength 2 adds approximately 60% of an AVC encode of compute and can introduce slight softening on noisy content."""


# --- restJson1 ser/de ---
def serialize_json(value: PerceptualFilterSettings) -> dict:
    out: dict = {}
    if "strength" in value:
        import capo_medialive.types.perceptual_filter_strength

        out["strength"] = (
            capo_medialive.types.perceptual_filter_strength.serialize_json(
                value["strength"]
            )
        )
    return out


def deserialize_json(data: dict) -> PerceptualFilterSettings:
    out: PerceptualFilterSettings = {}  # type: ignore[typeddict-item]
    if data.get("strength") is not None:
        import capo_medialive.types.perceptual_filter_strength

        out["strength"] = (
            capo_medialive.types.perceptual_filter_strength.deserialize_json(
                data["strength"]
            )
        )
    return out
