"""Generated from Smithy shape ``com.amazonaws.connect#DescribeInstanceStorageConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.association_id
    import capo_connect.types.instance_id
    import capo_connect.types.instance_storage_resource_type


class DescribeInstanceStorageConfigRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    association_id: "capo_connect.types.association_id.AssociationId"
    """<p>The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.</p>"""
    resource_type: (
        "capo_connect.types.instance_storage_resource_type.InstanceStorageResourceType"
    )
    """<p>A valid resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInstanceStorageConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeInstanceStorageConfigRequest:
    out: DescribeInstanceStorageConfigRequest = {}  # type: ignore[typeddict-item]
    return out
