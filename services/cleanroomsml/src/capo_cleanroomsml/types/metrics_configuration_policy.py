"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MetricsConfigurationPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.noise_level_type


class MetricsConfigurationPolicy(TypedDict, closed=True):
    noise_level: "capo_cleanroomsml.types.noise_level_type.NoiseLevelType"
    """<p>The noise level for the generated metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricsConfigurationPolicy) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.noise_level_type

    out["noiseLevel"] = capo_cleanroomsml.types.noise_level_type.serialize_json(
        value["noise_level"]
    )
    return out


def deserialize_json(data: dict) -> MetricsConfigurationPolicy:
    out: MetricsConfigurationPolicy = {}  # type: ignore[typeddict-item]
    if data.get("noiseLevel") is not None:
        import capo_cleanroomsml.types.noise_level_type

        out["noise_level"] = capo_cleanroomsml.types.noise_level_type.deserialize_json(
            data["noiseLevel"]
        )
    else:
        import typing

        out["noise_level"] = typing.cast(
            "capo_cleanroomsml.types.noise_level_type.NoiseLevelType", ""
        )
    return out
