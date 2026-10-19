"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImageSetsMetadataSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.date
    import capo_medical_imaging.types.dicom_tags
    import capo_medical_imaging.types.image_set_id
    import capo_medical_imaging.types.storage_tier


class ImageSetsMetadataSummary(TypedDict, closed=True):
    image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier.</p>"""
    version: NotRequired["int"]
    """<p>The image set version.</p>"""
    created_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The time an image set is created. Sample creation date is provided in <code>1985-04-12T23:20:50.52Z</code> format.</p>"""
    updated_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The time an image set was last updated.</p>"""
    last_accessed_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>When the image set was last accessed.</p>"""
    storage_tier: NotRequired["capo_medical_imaging.types.storage_tier.StorageTier"]
    """<p>The image set's storage tier.</p>"""
    dicom_tags: NotRequired["capo_medical_imaging.types.dicom_tags.DICOMTags"]
    """<p>The DICOM tags associated with the image set.</p>"""
    is_primary: NotRequired["bool"]
    """<p>The flag to determine whether the image set is primary or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageSetsMetadataSummary) -> dict:
    out: dict = {}
    out["imageSetId"] = value["image_set_id"]
    if "version" in value:
        out["version"] = value["version"]
    if "created_at" in value:
        import capo_medical_imaging.types.date

        out["createdAt"] = capo_medical_imaging.types.date.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_medical_imaging.types.date

        out["updatedAt"] = capo_medical_imaging.types.date.serialize_json(
            value["updated_at"]
        )
    if "last_accessed_at" in value:
        import capo_medical_imaging.types.date

        out["lastAccessedAt"] = capo_medical_imaging.types.date.serialize_json(
            value["last_accessed_at"]
        )
    if "storage_tier" in value:
        import capo_medical_imaging.types.storage_tier

        out["storageTier"] = capo_medical_imaging.types.storage_tier.serialize_json(
            value["storage_tier"]
        )
    if "dicom_tags" in value:
        import capo_medical_imaging.types.dicom_tags

        out["DICOMTags"] = capo_medical_imaging.types.dicom_tags.serialize_json(
            value["dicom_tags"]
        )
    if "is_primary" in value:
        out["isPrimary"] = value["is_primary"]
    return out


def deserialize_json(data: dict) -> ImageSetsMetadataSummary:
    out: ImageSetsMetadataSummary = {}  # type: ignore[typeddict-item]
    if data.get("imageSetId") is not None:
        out["image_set_id"] = data["imageSetId"]
    else:
        out["image_set_id"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("createdAt") is not None:
        import capo_medical_imaging.types.date

        out["created_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_medical_imaging.types.date

        out["updated_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["updatedAt"]
        )
    if data.get("lastAccessedAt") is not None:
        import capo_medical_imaging.types.date

        out["last_accessed_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["lastAccessedAt"]
        )
    if data.get("storageTier") is not None:
        import capo_medical_imaging.types.storage_tier

        out["storage_tier"] = capo_medical_imaging.types.storage_tier.deserialize_json(
            data["storageTier"]
        )
    if data.get("DICOMTags") is not None:
        import capo_medical_imaging.types.dicom_tags

        out["dicom_tags"] = capo_medical_imaging.types.dicom_tags.deserialize_json(
            data["DICOMTags"]
        )
    if data.get("isPrimary") is not None:
        out["is_primary"] = data["isPrimary"]
    return out


def redact_sensitive(value: ImageSetsMetadataSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dicom_tags" in value:
        import capo_medical_imaging.types.dicom_tags

        out["dicom_tags"] = capo_medical_imaging.types.dicom_tags.redact_sensitive(
            value["dicom_tags"]
        )
    return out
