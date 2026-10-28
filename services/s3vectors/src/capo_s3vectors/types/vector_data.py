"""Generated from Smithy shape ``com.amazonaws.s3vectors#VectorData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_s3vectors.errors import DeserializationError, SerializationError
from capo_s3vectors.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_s3vectors.types.float32_vector_data


class VectorDataFloat32Member(TypedDict, closed=True):
    float32: "capo_s3vectors.types.float32_vector_data.Float32VectorData"


VectorData: TypeAlias = VectorDataFloat32Member | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: VectorData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"VectorData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "float32" in value:
        import capo_s3vectors.types.float32_vector_data

        return {
            "float32": capo_s3vectors.types.float32_vector_data.serialize_json(
                value["float32"]
            )
        }
    else:
        raise SerializationError("VectorData: no variant present")


def deserialize_json(data: dict) -> VectorData:
    if data.get("float32") is not None:
        import capo_s3vectors.types.float32_vector_data

        return {
            "float32": capo_s3vectors.types.float32_vector_data.deserialize_json(
                data["float32"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("VectorData: no recognized variant key")
