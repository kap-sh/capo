"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SyntheticDataParameters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.ml_synthetic_data_parameters


class _SyntheticDataParameters_mlSyntheticDataParameters(TypedDict, closed=True):
    mlSyntheticDataParameters: (
        "capo_cleanrooms.types.ml_synthetic_data_parameters.MLSyntheticDataParameters"
    )


SyntheticDataParameters: TypeAlias = (
    _SyntheticDataParameters_mlSyntheticDataParameters | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SyntheticDataParameters) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SyntheticDataParameters: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "mlSyntheticDataParameters" in value:
        import capo_cleanrooms.types.ml_synthetic_data_parameters

        return {
            "mlSyntheticDataParameters": capo_cleanrooms.types.ml_synthetic_data_parameters.serialize_json(
                value["mlSyntheticDataParameters"]
            )
        }
    else:
        raise SerializationError("SyntheticDataParameters: no variant present")


def deserialize_json(data: dict) -> SyntheticDataParameters:
    if data.get("mlSyntheticDataParameters") is not None:
        import capo_cleanrooms.types.ml_synthetic_data_parameters

        return {
            "mlSyntheticDataParameters": capo_cleanrooms.types.ml_synthetic_data_parameters.deserialize_json(
                data["mlSyntheticDataParameters"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SyntheticDataParameters: no recognized variant key")
