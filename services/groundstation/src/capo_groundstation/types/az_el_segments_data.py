"""Generated from Smithy shape ``com.amazonaws.groundstation#AzElSegmentsData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError
from capo_groundstation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_groundstation.types.az_el_segments
    import capo_groundstation.types.s3_object


class AzElSegmentsDataS3ObjectMember(TypedDict, closed=True):
    s3Object: "capo_groundstation.types.s3_object.S3Object"


class AzElSegmentsDataAzElDataMember(TypedDict, closed=True):
    azElData: "capo_groundstation.types.az_el_segments.AzElSegments"


AzElSegmentsData: TypeAlias = (
    AzElSegmentsDataS3ObjectMember | AzElSegmentsDataAzElDataMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AzElSegmentsData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AzElSegmentsData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3Object" in value:
        import capo_groundstation.types.s3_object

        return {
            "s3Object": capo_groundstation.types.s3_object.serialize_json(
                value["s3Object"]
            )
        }
    elif "azElData" in value:
        import capo_groundstation.types.az_el_segments

        return {
            "azElData": capo_groundstation.types.az_el_segments.serialize_json(
                value["azElData"]
            )
        }
    else:
        raise SerializationError("AzElSegmentsData: no variant present")


def deserialize_json(data: dict) -> AzElSegmentsData:
    if data.get("s3Object") is not None:
        import capo_groundstation.types.s3_object

        return {
            "s3Object": capo_groundstation.types.s3_object.deserialize_json(
                data["s3Object"]
            )
        }
    elif data.get("azElData") is not None:
        import capo_groundstation.types.az_el_segments

        return {
            "azElData": capo_groundstation.types.az_el_segments.deserialize_json(
                data["azElData"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AzElSegmentsData: no recognized variant key")
