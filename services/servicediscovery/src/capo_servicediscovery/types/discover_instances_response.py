"""Generated from Smithy shape ``com.amazonaws.servicediscovery#DiscoverInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.http_instance_summary_list
    import capo_servicediscovery.types.revision


class DiscoverInstancesResponse(TypedDict, closed=True):
    instances: NotRequired[
        "capo_servicediscovery.types.http_instance_summary_list.HttpInstanceSummaryList"
    ]
    """<p>A complex type that contains one <code>HttpInstanceSummary</code> for each registered instance.</p>"""
    instances_revision: NotRequired["capo_servicediscovery.types.revision.Revision"]
    """<p>The increasing revision associated to the response Instances list. If a new instance is registered or deregistered, the <code>InstancesRevision</code> updates. The health status updates don't update <code>InstancesRevision</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoverInstancesResponse) -> dict:
    out: dict = {}
    if "instances" in value:
        import capo_servicediscovery.types.http_instance_summary_list

        out["Instances"] = (
            capo_servicediscovery.types.http_instance_summary_list.serialize_aws_json_1_1(
                value["instances"]
            )
        )
    if "instances_revision" in value:
        out["InstancesRevision"] = value["instances_revision"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiscoverInstancesResponse:
    out: DiscoverInstancesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Instances") is not None:
        import capo_servicediscovery.types.http_instance_summary_list

        out["instances"] = (
            capo_servicediscovery.types.http_instance_summary_list.deserialize_aws_json_1_1(
                data["Instances"]
            )
        )
    if data.get("InstancesRevision") is not None:
        out["instances_revision"] = data["InstancesRevision"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DiscoverInstancesResponse) -> dict:
    out: dict = {}
    if "instances" in value:
        import capo_servicediscovery.types.http_instance_summary_list

        out["Instances"] = (
            capo_servicediscovery.types.http_instance_summary_list.serialize_cbor(
                value["instances"]
            )
        )
    if "instances_revision" in value:
        out["InstancesRevision"] = value["instances_revision"]
    return out


def deserialize_cbor(data: dict) -> DiscoverInstancesResponse:
    out: DiscoverInstancesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Instances") is not None:
        import capo_servicediscovery.types.http_instance_summary_list

        out["instances"] = (
            capo_servicediscovery.types.http_instance_summary_list.deserialize_cbor(
                data["Instances"]
            )
        )
    if data.get("InstancesRevision") is not None:
        out["instances_revision"] = data["InstancesRevision"]
    return out
