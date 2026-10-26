"""Generated from Smithy shape ``com.amazonaws.groundstation#ConfigDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError
from capo_groundstation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_groundstation.types.antenna_demod_decode_details
    import capo_groundstation.types.endpoint_details
    import capo_groundstation.types.s3_recording_details


class _ConfigDetails_endpointDetails(TypedDict, closed=True):
    endpointDetails: "capo_groundstation.types.endpoint_details.EndpointDetails"


class _ConfigDetails_antennaDemodDecodeDetails(TypedDict, closed=True):
    antennaDemodDecodeDetails: "capo_groundstation.types.antenna_demod_decode_details.AntennaDemodDecodeDetails"


class _ConfigDetails_s3RecordingDetails(TypedDict, closed=True):
    s3RecordingDetails: (
        "capo_groundstation.types.s3_recording_details.S3RecordingDetails"
    )


ConfigDetails: TypeAlias = (
    _ConfigDetails_endpointDetails
    | _ConfigDetails_antennaDemodDecodeDetails
    | _ConfigDetails_s3RecordingDetails
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ConfigDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ConfigDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "endpointDetails" in value:
        import capo_groundstation.types.endpoint_details

        return {
            "endpointDetails": capo_groundstation.types.endpoint_details.serialize_json(
                value["endpointDetails"]
            )
        }
    elif "antennaDemodDecodeDetails" in value:
        import capo_groundstation.types.antenna_demod_decode_details

        return {
            "antennaDemodDecodeDetails": capo_groundstation.types.antenna_demod_decode_details.serialize_json(
                value["antennaDemodDecodeDetails"]
            )
        }
    elif "s3RecordingDetails" in value:
        import capo_groundstation.types.s3_recording_details

        return {
            "s3RecordingDetails": capo_groundstation.types.s3_recording_details.serialize_json(
                value["s3RecordingDetails"]
            )
        }
    else:
        raise SerializationError("ConfigDetails: no variant present")


def deserialize_json(data: dict) -> ConfigDetails:
    if data.get("endpointDetails") is not None:
        import capo_groundstation.types.endpoint_details

        return {
            "endpointDetails": capo_groundstation.types.endpoint_details.deserialize_json(
                data["endpointDetails"]
            )
        }
    elif data.get("antennaDemodDecodeDetails") is not None:
        import capo_groundstation.types.antenna_demod_decode_details

        return {
            "antennaDemodDecodeDetails": capo_groundstation.types.antenna_demod_decode_details.deserialize_json(
                data["antennaDemodDecodeDetails"]
            )
        }
    elif data.get("s3RecordingDetails") is not None:
        import capo_groundstation.types.s3_recording_details

        return {
            "s3RecordingDetails": capo_groundstation.types.s3_recording_details.deserialize_json(
                data["s3RecordingDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ConfigDetails: no recognized variant key")
