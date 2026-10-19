"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetModelManifestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.manifest_status
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.timestamp


class GetModelManifestResponse(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the vehicle model. </p>"""
    arn: "capo_iotfleetwise.types.arn.arn"
    """<p> The Amazon Resource Name (ARN) of the vehicle model. </p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p> A brief description of the vehicle model. </p>"""
    signal_catalog_arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p> The ARN of the signal catalog associated with the vehicle model. </p>"""
    status: NotRequired["capo_iotfleetwise.types.manifest_status.ManifestStatus"]
    """<p> The state of the vehicle model. If the status is <code>ACTIVE</code>, the vehicle model can't be edited. You can edit the vehicle model if the status is marked <code>DRAFT</code>.</p>"""
    creation_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p>The time the vehicle model was created, in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""
    last_modification_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p>The last time the vehicle model was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetModelManifestResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "signal_catalog_arn" in value:
        out["signalCatalogArn"] = value["signal_catalog_arn"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> GetModelManifestResponse:
    out: GetModelManifestResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("signalCatalogArn") is not None:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
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
    return out
