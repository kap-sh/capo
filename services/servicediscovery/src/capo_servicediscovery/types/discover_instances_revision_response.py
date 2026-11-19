"""Generated from Smithy shape ``com.amazonaws.servicediscovery#DiscoverInstancesRevisionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.revision


class DiscoverInstancesRevisionResponse(TypedDict, closed=True):
    instances_revision: NotRequired["capo_servicediscovery.types.revision.Revision"]
    """<p>The increasing revision associated to the response Instances list. If a new instance is registered or deregistered, the <code>InstancesRevision</code> updates. The health status updates don't update <code>InstancesRevision</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoverInstancesRevisionResponse) -> dict:
    out: dict = {}
    if "instances_revision" in value:
        out["InstancesRevision"] = value["instances_revision"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiscoverInstancesRevisionResponse:
    out: DiscoverInstancesRevisionResponse = {}  # type: ignore[typeddict-item]
    if data.get("InstancesRevision") is not None:
        out["instances_revision"] = data["InstancesRevision"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DiscoverInstancesRevisionResponse) -> dict:
    out: dict = {}
    if "instances_revision" in value:
        out["InstancesRevision"] = value["instances_revision"]
    return out


def deserialize_cbor(data: dict) -> DiscoverInstancesRevisionResponse:
    out: DiscoverInstancesRevisionResponse = {}  # type: ignore[typeddict-item]
    if data.get("InstancesRevision") is not None:
        out["instances_revision"] = data["InstancesRevision"]
    return out
