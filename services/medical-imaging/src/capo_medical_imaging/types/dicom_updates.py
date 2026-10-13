"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DICOMUpdates``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.dicom_attribute


class DICOMUpdates(TypedDict, closed=True):
    removable_attributes: NotRequired[
        "capo_medical_imaging.types.dicom_attribute.DICOMAttribute"
    ]
    """<p>The DICOM tags to be removed from <code>ImageSetMetadata</code>.</p>"""
    updatable_attributes: NotRequired[
        "capo_medical_imaging.types.dicom_attribute.DICOMAttribute"
    ]
    """<p>The DICOM tags that need to be updated in <code>ImageSetMetadata</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DICOMUpdates) -> dict:
    out: dict = {}
    if "removable_attributes" in value:
        import capo_medical_imaging.types.dicom_attribute

        out["removableAttributes"] = (
            capo_medical_imaging.types.dicom_attribute.serialize_json(
                value["removable_attributes"]
            )
        )
    if "updatable_attributes" in value:
        import capo_medical_imaging.types.dicom_attribute

        out["updatableAttributes"] = (
            capo_medical_imaging.types.dicom_attribute.serialize_json(
                value["updatable_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> DICOMUpdates:
    out: DICOMUpdates = {}  # type: ignore[typeddict-item]
    if data.get("removableAttributes") is not None:
        import capo_medical_imaging.types.dicom_attribute

        out["removable_attributes"] = (
            capo_medical_imaging.types.dicom_attribute.deserialize_json(
                data["removableAttributes"]
            )
        )
    if data.get("updatableAttributes") is not None:
        import capo_medical_imaging.types.dicom_attribute

        out["updatable_attributes"] = (
            capo_medical_imaging.types.dicom_attribute.deserialize_json(
                data["updatableAttributes"]
            )
        )
    return out


def redact_sensitive(value: DICOMUpdates) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "removable_attributes" in value:
        out["removable_attributes"] = "*** Sensitive Data Redacted ***"
    if "updatable_attributes" in value:
        out["updatable_attributes"] = "*** Sensitive Data Redacted ***"
    return out
