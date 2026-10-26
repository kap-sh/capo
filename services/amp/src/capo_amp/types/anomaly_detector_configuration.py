"""Generated from Smithy shape ``com.amazonaws.amp#AnomalyDetectorConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError, SerializationError
from capo_amp.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_amp.types.random_cut_forest_configuration


class _AnomalyDetectorConfiguration_randomCutForest(TypedDict, closed=True):
    randomCutForest: (
        "capo_amp.types.random_cut_forest_configuration.RandomCutForestConfiguration"
    )


AnomalyDetectorConfiguration: TypeAlias = (
    _AnomalyDetectorConfiguration_randomCutForest | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyDetectorConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AnomalyDetectorConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "randomCutForest" in value:
        import capo_amp.types.random_cut_forest_configuration

        return {
            "randomCutForest": capo_amp.types.random_cut_forest_configuration.serialize_json(
                value["randomCutForest"]
            )
        }
    else:
        raise SerializationError("AnomalyDetectorConfiguration: no variant present")


def deserialize_json(data: dict) -> AnomalyDetectorConfiguration:
    if data.get("randomCutForest") is not None:
        import capo_amp.types.random_cut_forest_configuration

        return {
            "randomCutForest": capo_amp.types.random_cut_forest_configuration.deserialize_json(
                data["randomCutForest"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AnomalyDetectorConfiguration: no recognized variant key"
        )
