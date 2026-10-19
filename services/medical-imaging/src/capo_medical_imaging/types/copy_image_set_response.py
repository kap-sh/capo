"""Generated from Smithy shape ``com.amazonaws.medicalimaging#CopyImageSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.copy_destination_image_set_properties
    import capo_medical_imaging.types.copy_source_image_set_properties
    import capo_medical_imaging.types.datastore_id


class CopyImageSetResponse(TypedDict, closed=True):
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    source_image_set_properties: "capo_medical_imaging.types.copy_source_image_set_properties.CopySourceImageSetProperties"
    """<p>The properties of the source image set.</p>"""
    destination_image_set_properties: "capo_medical_imaging.types.copy_destination_image_set_properties.CopyDestinationImageSetProperties"
    """<p>The properties of the destination image set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyImageSetResponse) -> dict:
    out: dict = {}
    out["datastoreId"] = value["datastore_id"]
    import capo_medical_imaging.types.copy_source_image_set_properties

    out["sourceImageSetProperties"] = (
        capo_medical_imaging.types.copy_source_image_set_properties.serialize_json(
            value["source_image_set_properties"]
        )
    )
    import capo_medical_imaging.types.copy_destination_image_set_properties

    out["destinationImageSetProperties"] = (
        capo_medical_imaging.types.copy_destination_image_set_properties.serialize_json(
            value["destination_image_set_properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> CopyImageSetResponse:
    out: CopyImageSetResponse = {}  # type: ignore[typeddict-item]
    if data.get("datastoreId") is not None:
        out["datastore_id"] = data["datastoreId"]
    else:
        out["datastore_id"] = ""
    if data.get("sourceImageSetProperties") is not None:
        import capo_medical_imaging.types.copy_source_image_set_properties

        out["source_image_set_properties"] = (
            capo_medical_imaging.types.copy_source_image_set_properties.deserialize_json(
                data["sourceImageSetProperties"]
            )
        )
    else:
        raise DeserializationError(
            "CopyImageSetResponse.source_image_set_properties required"
        )
    if data.get("destinationImageSetProperties") is not None:
        import capo_medical_imaging.types.copy_destination_image_set_properties

        out["destination_image_set_properties"] = (
            capo_medical_imaging.types.copy_destination_image_set_properties.deserialize_json(
                data["destinationImageSetProperties"]
            )
        )
    else:
        raise DeserializationError(
            "CopyImageSetResponse.destination_image_set_properties required"
        )
    return out
