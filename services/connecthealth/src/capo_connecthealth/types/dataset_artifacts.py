"""Generated from Smithy shape ``com.amazonaws.connecthealth#DatasetArtifacts``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connecthealth.errors import DeserializationError, SerializationError
from capo_connecthealth.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connecthealth.types.medical_coding_dataset_artifacts


class DatasetArtifactsMedicalCodingMember(TypedDict, closed=True):
    medicalCoding: "capo_connecthealth.types.medical_coding_dataset_artifacts.MedicalCodingDatasetArtifacts"


DatasetArtifacts: TypeAlias = DatasetArtifactsMedicalCodingMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: DatasetArtifacts) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DatasetArtifacts: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "medicalCoding" in value:
        import capo_connecthealth.types.medical_coding_dataset_artifacts

        return {
            "medicalCoding": capo_connecthealth.types.medical_coding_dataset_artifacts.serialize_json(
                value["medicalCoding"]
            )
        }
    else:
        raise SerializationError("DatasetArtifacts: no variant present")


def deserialize_json(data: dict) -> DatasetArtifacts:
    if data.get("medicalCoding") is not None:
        import capo_connecthealth.types.medical_coding_dataset_artifacts

        return {
            "medicalCoding": capo_connecthealth.types.medical_coding_dataset_artifacts.deserialize_json(
                data["medicalCoding"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DatasetArtifacts: no recognized variant key")
