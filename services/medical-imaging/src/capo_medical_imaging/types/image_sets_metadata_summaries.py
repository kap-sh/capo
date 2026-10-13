"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImageSetsMetadataSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_medical_imaging.types.image_sets_metadata_summary

ImageSetsMetadataSummaries: TypeAlias = list[
    "capo_medical_imaging.types.image_sets_metadata_summary.ImageSetsMetadataSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageSetsMetadataSummaries) -> list:
    import capo_medical_imaging.types.image_sets_metadata_summary

    out: list = []
    for item in value:
        out.append(
            capo_medical_imaging.types.image_sets_metadata_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ImageSetsMetadataSummaries:
    import capo_medical_imaging.types.image_sets_metadata_summary

    out: ImageSetsMetadataSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_medical_imaging.types.image_sets_metadata_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ImageSetsMetadataSummaries) -> list[Any]:
    import capo_medical_imaging.types.image_sets_metadata_summary

    return [
        capo_medical_imaging.types.image_sets_metadata_summary.redact_sensitive(item)
        for item in value
    ]
