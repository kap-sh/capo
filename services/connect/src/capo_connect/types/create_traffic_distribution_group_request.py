"""Generated from Smithy shape ``com.amazonaws.connect#CreateTrafficDistributionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.acgr_instance_id_or_arn
    import capo_connect.types.client_token
    import capo_connect.types.description250
    import capo_connect.types.name128
    import capo_connect.types.tag_map


class CreateTrafficDistributionGroupRequest(TypedDict, closed=True):
    name: "capo_connect.types.name128.Name128"
    """<p>The name for the traffic distribution group. </p>"""
    description: NotRequired["capo_connect.types.description250.Description250"]
    """<p>A description for the traffic distribution group.</p>"""
    instance_id: "capo_connect.types.acgr_instance_id_or_arn.ACGRInstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance that has been replicated. You can find the <code>instanceId</code> in the ARN of the instance.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTrafficDistributionGroupRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["InstanceId"] = value["instance_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateTrafficDistributionGroupRequest:
    out: CreateTrafficDistributionGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError(
            "CreateTrafficDistributionGroupRequest.name required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "CreateTrafficDistributionGroupRequest.instance_id required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
