"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.region
    import capo_ecr.types.registry_id


class ReplicationDestination(TypedDict, closed=True):
    region: "capo_ecr.types.region.Region"
    """<p>The Region to replicate to.</p>"""
    registry_id: "capo_ecr.types.registry_id.RegistryId"
    """<p>The Amazon Web Services account ID of the Amazon ECR private registry to replicate to. When configuring cross-Region replication within your own registry, specify your own account ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationDestination) -> dict:
    out: dict = {}
    out["region"] = value["region"]
    out["registryId"] = value["registry_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationDestination:
    out: ReplicationDestination = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    else:
        out["registry_id"] = ""
    return out
