"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#VehicleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.attributes_map
    import capo_iotfleetwise.types.timestamp
    import capo_iotfleetwise.types.vehicle_name


class VehicleSummary(TypedDict, closed=True):
    vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName"
    """<p>The unique ID of the vehicle.</p>"""
    arn: "capo_iotfleetwise.types.arn.arn"
    """<p>The Amazon Resource Name (ARN) of the vehicle.</p>"""
    model_manifest_arn: "capo_iotfleetwise.types.arn.arn"
    """<p>The ARN of a vehicle model (model manifest) associated with the vehicle.</p>"""
    decoder_manifest_arn: "capo_iotfleetwise.types.arn.arn"
    """<p>The ARN of a decoder manifest associated with the vehicle.</p>"""
    creation_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p>The time the vehicle was created in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""
    last_modification_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p>The time the vehicle was last updated in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""
    attributes: NotRequired["capo_iotfleetwise.types.attributes_map.attributesMap"]
    """<p>Static information about a vehicle in a key-value pair. For example:</p> <p> <code>"engineType"</code> : <code>"1.3 L R2"</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VehicleSummary) -> dict:
    out: dict = {}
    out["vehicleName"] = value["vehicle_name"]
    out["arn"] = value["arn"]
    out["modelManifestArn"] = value["model_manifest_arn"]
    out["decoderManifestArn"] = value["decoder_manifest_arn"]
    import capo_iotfleetwise.types.timestamp

    out["creationTime"] = capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
        value["creation_time"]
    )
    import capo_iotfleetwise.types.timestamp

    out["lastModificationTime"] = (
        capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
            value["last_modification_time"]
        )
    )
    if "attributes" in value:
        import capo_iotfleetwise.types.attributes_map

        out["attributes"] = (
            capo_iotfleetwise.types.attributes_map.serialize_aws_json_1_0(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VehicleSummary:
    out: VehicleSummary = {}  # type: ignore[typeddict-item]
    if data.get("vehicleName") is not None:
        out["vehicle_name"] = data["vehicleName"]
    else:
        out["vehicle_name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("modelManifestArn") is not None:
        out["model_manifest_arn"] = data["modelManifestArn"]
    else:
        out["model_manifest_arn"] = ""
    if data.get("decoderManifestArn") is not None:
        out["decoder_manifest_arn"] = data["decoderManifestArn"]
    else:
        out["decoder_manifest_arn"] = ""
    if data.get("creationTime") is not None:
        import capo_iotfleetwise.types.timestamp

        out["creation_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastModificationTime") is not None:
        import capo_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    else:
        import datetime

        out["last_modification_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("attributes") is not None:
        import capo_iotfleetwise.types.attributes_map

        out["attributes"] = (
            capo_iotfleetwise.types.attributes_map.deserialize_aws_json_1_0(
                data["attributes"]
            )
        )
    return out
