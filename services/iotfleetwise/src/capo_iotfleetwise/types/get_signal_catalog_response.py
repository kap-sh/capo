"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetSignalCatalogResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.node_counts
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.timestamp


class GetSignalCatalogResponse(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the signal catalog. </p>"""
    arn: "capo_iotfleetwise.types.arn.arn"
    """<p> The Amazon Resource Name (ARN) of the signal catalog. </p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p> A brief description of the signal catalog. </p>"""
    node_counts: NotRequired["capo_iotfleetwise.types.node_counts.NodeCounts"]
    """<p> The total number of network nodes specified in a signal catalog. </p>"""
    creation_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p> The time the signal catalog was created in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""
    last_modification_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p>The last time the signal catalog was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSignalCatalogResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "node_counts" in value:
        import capo_iotfleetwise.types.node_counts

        out["nodeCounts"] = capo_iotfleetwise.types.node_counts.serialize_aws_json_1_0(
            value["node_counts"]
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


def deserialize_aws_json_1_0(data: dict) -> GetSignalCatalogResponse:
    out: GetSignalCatalogResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("nodeCounts") is not None:
        import capo_iotfleetwise.types.node_counts

        out["node_counts"] = (
            capo_iotfleetwise.types.node_counts.deserialize_aws_json_1_0(
                data["nodeCounts"]
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
