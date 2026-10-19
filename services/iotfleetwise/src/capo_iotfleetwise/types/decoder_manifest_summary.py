"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DecoderManifestSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.manifest_status
    import capo_iotfleetwise.types.message
    import capo_iotfleetwise.types.string
    import capo_iotfleetwise.types.timestamp


class DecoderManifestSummary(TypedDict, closed=True):
    name: NotRequired["capo_iotfleetwise.types.string.string"]
    """<p>The name of the decoder manifest.</p>"""
    arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p>The ARN of a vehicle model (model manifest) associated with the decoder manifest. </p>"""
    model_manifest_arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p>The ARN of a vehicle model (model manifest) associated with the decoder manifest.</p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p>A brief description of the decoder manifest.</p>"""
    status: NotRequired["capo_iotfleetwise.types.manifest_status.ManifestStatus"]
    """<p>The state of the decoder manifest. If the status is <code>ACTIVE</code>, the decoder manifest can't be edited. If the status is marked <code>DRAFT</code>, you can edit the decoder manifest.</p>"""
    creation_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p>The time the decoder manifest was created in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""
    last_modification_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p>The time the decoder manifest was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""
    message: NotRequired["capo_iotfleetwise.types.message.message"]
    """<p>The detailed message for the decoder manifest. When a decoder manifest is in an <code>INVALID</code> status, the message contains detailed reason and help information.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DecoderManifestSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "model_manifest_arn" in value:
        out["modelManifestArn"] = value["model_manifest_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_iotfleetwise.types.manifest_status

        out["status"] = capo_iotfleetwise.types.manifest_status.serialize_aws_json_1_0(
            value["status"]
        )
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
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DecoderManifestSummary:
    out: DecoderManifestSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("modelManifestArn") is not None:
        out["model_manifest_arn"] = data["modelManifestArn"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_iotfleetwise.types.manifest_status

        out["status"] = (
            capo_iotfleetwise.types.manifest_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
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
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
