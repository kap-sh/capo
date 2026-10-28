"""Generated from Smithy shape ``com.amazonaws.medicalimaging#MetadataUpdates``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_medical_imaging.errors import DeserializationError, SerializationError
from capo_medical_imaging.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_medical_imaging.types.dicom_updates
    import capo_medical_imaging.types.image_set_external_version_id


class MetadataUpdatesDICOMUpdatesMember(TypedDict, closed=True):
    DICOMUpdates: "capo_medical_imaging.types.dicom_updates.DICOMUpdates"


class MetadataUpdatesRevertToVersionIdMember(TypedDict, closed=True):
    revertToVersionId: "capo_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"


MetadataUpdates: TypeAlias = (
    MetadataUpdatesDICOMUpdatesMember
    | MetadataUpdatesRevertToVersionIdMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MetadataUpdates) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MetadataUpdates: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "DICOMUpdates" in value:
        import capo_medical_imaging.types.dicom_updates

        return {
            "DICOMUpdates": capo_medical_imaging.types.dicom_updates.serialize_json(
                value["DICOMUpdates"]
            )
        }
    elif "revertToVersionId" in value:
        return {"revertToVersionId": value["revertToVersionId"]}
    else:
        raise SerializationError("MetadataUpdates: no variant present")


def deserialize_json(data: dict) -> MetadataUpdates:
    if data.get("DICOMUpdates") is not None:
        import capo_medical_imaging.types.dicom_updates

        return {
            "DICOMUpdates": capo_medical_imaging.types.dicom_updates.deserialize_json(
                data["DICOMUpdates"]
            )
        }
    elif data.get("revertToVersionId") is not None:
        return {"revertToVersionId": data["revertToVersionId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("MetadataUpdates: no recognized variant key")


def redact_sensitive(value: MetadataUpdates) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "DICOMUpdates" in value:
        import capo_medical_imaging.types.dicom_updates

        out["DICOMUpdates"] = capo_medical_imaging.types.dicom_updates.redact_sensitive(
            value["DICOMUpdates"]
        )
    return out
