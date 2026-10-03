"""Generated from Smithy shape ``com.amazonaws.connect#Instance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.directory_alias
    import capo_connect.types.directory_type
    import capo_connect.types.inbound_calls_enabled
    import capo_connect.types.instance_id
    import capo_connect.types.instance_status
    import capo_connect.types.instance_status_reason
    import capo_connect.types.outbound_calls_enabled
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp
    import capo_connect.types.url


class Instance(TypedDict, closed=True):
    id: NotRequired["capo_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the instance.</p>"""
    identity_management_type: NotRequired[
        "capo_connect.types.directory_type.DirectoryType"
    ]
    """<p>The identity management type.</p>"""
    instance_alias: NotRequired["capo_connect.types.directory_alias.DirectoryAlias"]
    """<p>The alias of instance.</p>"""
    created_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>When the instance was created.</p>"""
    service_role: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The service role of the instance.</p>"""
    instance_status: NotRequired["capo_connect.types.instance_status.InstanceStatus"]
    """<p>The state of the instance.</p>"""
    status_reason: NotRequired[
        "capo_connect.types.instance_status_reason.InstanceStatusReason"
    ]
    """<p>Relevant details why the instance was not successfully created. </p>"""
    inbound_calls_enabled: NotRequired[
        "capo_connect.types.inbound_calls_enabled.InboundCallsEnabled"
    ]
    """<p>Whether inbound calls are enabled.</p>"""
    outbound_calls_enabled: NotRequired[
        "capo_connect.types.outbound_calls_enabled.OutboundCallsEnabled"
    ]
    """<p>Whether outbound calls are enabled.</p>"""
    instance_access_url: NotRequired["capo_connect.types.url.Url"]
    """<p>This URL allows contact center users to access the Connect Customer admin website.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags of an instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Instance) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "identity_management_type" in value:
        import capo_connect.types.directory_type

        out["IdentityManagementType"] = (
            capo_connect.types.directory_type.serialize_json(
                value["identity_management_type"]
            )
        )
    if "instance_alias" in value:
        out["InstanceAlias"] = value["instance_alias"]
    if "created_time" in value:
        import capo_connect.types.timestamp

        out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "instance_status" in value:
        import capo_connect.types.instance_status

        out["InstanceStatus"] = capo_connect.types.instance_status.serialize_json(
            value["instance_status"]
        )
    if "status_reason" in value:
        import capo_connect.types.instance_status_reason

        out["StatusReason"] = capo_connect.types.instance_status_reason.serialize_json(
            value["status_reason"]
        )
    if "inbound_calls_enabled" in value:
        out["InboundCallsEnabled"] = value["inbound_calls_enabled"]
    if "outbound_calls_enabled" in value:
        out["OutboundCallsEnabled"] = value["outbound_calls_enabled"]
    if "instance_access_url" in value:
        out["InstanceAccessUrl"] = value["instance_access_url"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("IdentityManagementType") is not None:
        import capo_connect.types.directory_type

        out["identity_management_type"] = (
            capo_connect.types.directory_type.deserialize_json(
                data["IdentityManagementType"]
            )
        )
    if data.get("InstanceAlias") is not None:
        out["instance_alias"] = data["InstanceAlias"]
    if data.get("CreatedTime") is not None:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("ServiceRole") is not None:
        out["service_role"] = data["ServiceRole"]
    if data.get("InstanceStatus") is not None:
        import capo_connect.types.instance_status

        out["instance_status"] = capo_connect.types.instance_status.deserialize_json(
            data["InstanceStatus"]
        )
    if data.get("StatusReason") is not None:
        import capo_connect.types.instance_status_reason

        out["status_reason"] = (
            capo_connect.types.instance_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if data.get("InboundCallsEnabled") is not None:
        out["inbound_calls_enabled"] = data["InboundCallsEnabled"]
    if data.get("OutboundCallsEnabled") is not None:
        out["outbound_calls_enabled"] = data["OutboundCallsEnabled"]
    if data.get("InstanceAccessUrl") is not None:
        out["instance_access_url"] = data["InstanceAccessUrl"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
