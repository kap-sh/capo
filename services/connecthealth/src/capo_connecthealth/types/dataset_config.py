"""Generated from Smithy shape ``com.amazonaws.connecthealth#DatasetConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connecthealth.errors import DeserializationError, SerializationError
from capo_connecthealth.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connecthealth.types.medical_coding_dataset_config


class DatasetConfigMedicalCodingMember(TypedDict, closed=True):
    medicalCoding: "capo_connecthealth.types.medical_coding_dataset_config.MedicalCodingDatasetConfig"


DatasetConfig: TypeAlias = DatasetConfigMedicalCodingMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: DatasetConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DatasetConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "medicalCoding" in value:
        import capo_connecthealth.types.medical_coding_dataset_config

        return {
            "medicalCoding": capo_connecthealth.types.medical_coding_dataset_config.serialize_json(
                value["medicalCoding"]
            )
        }
    else:
        raise SerializationError("DatasetConfig: no variant present")


def deserialize_json(data: dict) -> DatasetConfig:
    if data.get("medicalCoding") is not None:
        import capo_connecthealth.types.medical_coding_dataset_config

        return {
            "medicalCoding": capo_connecthealth.types.medical_coding_dataset_config.deserialize_json(
                data["medicalCoding"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DatasetConfig: no recognized variant key")
