"""Generated from Smithy shape ``com.amazonaws.ecr#StartReplicationBackfillRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.registry_id
    import capo_ecr.types.replication_destination


class StartReplicationBackfillRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry from which to start the replication backfill. If you do not specify a registry, the default registry is assumed.</p>"""
    destination: "capo_ecr.types.replication_destination.ReplicationDestination"
    """<p>The destination Region and registry to which the images are replicated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReplicationBackfillRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    import capo_ecr.types.replication_destination

    out["destination"] = capo_ecr.types.replication_destination.serialize_aws_json_1_1(
        value["destination"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartReplicationBackfillRequest:
    out: StartReplicationBackfillRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("destination") is not None:
        import capo_ecr.types.replication_destination

        out["destination"] = (
            capo_ecr.types.replication_destination.deserialize_aws_json_1_1(
                data["destination"]
            )
        )
    else:
        raise DeserializationError(
            "StartReplicationBackfillRequest.destination required"
        )
    return out
