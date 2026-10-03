"""Generated from Smithy shape ``com.amazonaws.connect#UpdateInstanceStorageConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.association_id
    import capo_connect.types.client_token
    import capo_connect.types.instance_id
    import capo_connect.types.instance_storage_config
    import capo_connect.types.instance_storage_resource_type


class UpdateInstanceStorageConfigRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    association_id: "capo_connect.types.association_id.AssociationId"
    """<p>The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.</p>"""
    resource_type: (
        "capo_connect.types.instance_storage_resource_type.InstanceStorageResourceType"
    )
    """<p>A valid resource type.</p>"""
    storage_config: "capo_connect.types.instance_storage_config.InstanceStorageConfig"
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInstanceStorageConfigRequest) -> dict:
    out: dict = {}
    import capo_connect.types.instance_storage_config

    out["StorageConfig"] = capo_connect.types.instance_storage_config.serialize_json(
        value["storage_config"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateInstanceStorageConfigRequest:
    out: UpdateInstanceStorageConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("StorageConfig") is not None:
        import capo_connect.types.instance_storage_config

        out["storage_config"] = (
            capo_connect.types.instance_storage_config.deserialize_json(
                data["StorageConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateInstanceStorageConfigRequest.storage_config required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
