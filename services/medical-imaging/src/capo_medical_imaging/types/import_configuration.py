"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImportConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_medical_imaging.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.dicom_json_metadata_import_configuration


class _ImportConfiguration_dicomJsonMetadataImportConfiguration(TypedDict, closed=True):
    dicomJsonMetadataImportConfiguration: "capo_medical_imaging.types.dicom_json_metadata_import_configuration.DicomJsonMetadataImportConfiguration"


ImportConfiguration: TypeAlias = (
    _ImportConfiguration_dicomJsonMetadataImportConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ImportConfiguration) -> dict:
    if "dicomJsonMetadataImportConfiguration" in value:
        import capo_medical_imaging.types.dicom_json_metadata_import_configuration

        return {
            "dicomJsonMetadataImportConfiguration": capo_medical_imaging.types.dicom_json_metadata_import_configuration.serialize_json(
                value["dicomJsonMetadataImportConfiguration"]
            )
        }
    else:
        raise SerializationError("ImportConfiguration: no variant present")


def deserialize_json(data: dict) -> ImportConfiguration:
    if data.get("dicomJsonMetadataImportConfiguration") is not None:
        import capo_medical_imaging.types.dicom_json_metadata_import_configuration

        return {
            "dicomJsonMetadataImportConfiguration": capo_medical_imaging.types.dicom_json_metadata_import_configuration.deserialize_json(
                data["dicomJsonMetadataImportConfiguration"]
            )
        }
    else:
        raise DeserializationError("ImportConfiguration: no recognized variant key")


def redact_sensitive(value: ImportConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dicomJsonMetadataImportConfiguration" in value:
        import capo_medical_imaging.types.dicom_json_metadata_import_configuration

        out["dicomJsonMetadataImportConfiguration"] = (
            capo_medical_imaging.types.dicom_json_metadata_import_configuration.redact_sensitive(
                value["dicomJsonMetadataImportConfiguration"]
            )
        )
    return out
