"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyHostsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.auto_placement
    import capo_ec2.types.host_maintenance
    import capo_ec2.types.host_recovery
    import capo_ec2.types.request_host_id_list
    import capo_ec2.types.string


class ModifyHostsRequest(TypedDict, closed=True):
    host_recovery: NotRequired["capo_ec2.types.host_recovery.HostRecovery"]
    """<p>Indicates whether to enable or disable host recovery for the Dedicated Host. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-recovery.html">Host recovery</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p>Specifies the instance type to be supported by the Dedicated Host. Specify this parameter to modify a Dedicated Host to support only a specific instance type.</p> <p>If you want to modify a Dedicated Host to support multiple instance types in its current instance family, omit this parameter and specify <b>InstanceFamily</b> instead. You cannot specify <b>InstanceType</b> and <b>InstanceFamily</b> in the same request.</p>"""
    instance_family: NotRequired["capo_ec2.types.string.String"]
    """<p>Specifies the instance family to be supported by the Dedicated Host. Specify this parameter to modify a Dedicated Host to support multiple instance types within its current instance family.</p> <p>If you want to modify a Dedicated Host to support a specific instance type only, omit this parameter and specify <b>InstanceType</b> instead. You cannot specify <b>InstanceFamily</b> and <b>InstanceType</b> in the same request.</p>"""
    host_maintenance: NotRequired["capo_ec2.types.host_maintenance.HostMaintenance"]
    """<p>Indicates whether to enable or disable host maintenance for the Dedicated Host. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-maintenance.html">Host maintenance</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    host_ids: NotRequired["capo_ec2.types.request_host_id_list.RequestHostIdList"]
    """<p>The IDs of the Dedicated Hosts to modify.</p>"""
    auto_placement: NotRequired["capo_ec2.types.auto_placement.AutoPlacement"]
    """<p>Specify whether to enable or disable auto-placement.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyHostsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "host_recovery" in value:
        import capo_ec2.types.host_recovery

        capo_ec2.types.host_recovery.serialize_ec2_query(
            value["host_recovery"], pairs, f"{key_prefix}HostRecovery"
        )
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "instance_family" in value:
        pairs.append((f"{key_prefix}InstanceFamily", str(value["instance_family"])))
    if "host_maintenance" in value:
        import capo_ec2.types.host_maintenance

        capo_ec2.types.host_maintenance.serialize_ec2_query(
            value["host_maintenance"], pairs, f"{key_prefix}HostMaintenance"
        )
    if "host_ids" in value:
        import capo_ec2.types.request_host_id_list

        capo_ec2.types.request_host_id_list.serialize_ec2_query(
            value["host_ids"], pairs, f"{key_prefix}HostId"
        )
    if "auto_placement" in value:
        import capo_ec2.types.auto_placement

        capo_ec2.types.auto_placement.serialize_ec2_query(
            value["auto_placement"], pairs, f"{key_prefix}AutoPlacement"
        )


def deserialize_ec2_query(el: Element) -> ModifyHostsRequest:
    out: ModifyHostsRequest = {}  # type: ignore[typeddict-item]
    child_host_recovery = el.find("HostRecovery")
    if child_host_recovery is not None:
        import capo_ec2.types.host_recovery

        out["host_recovery"] = capo_ec2.types.host_recovery.deserialize_ec2_query(
            child_host_recovery
        )
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_instance_family = el.find("InstanceFamily")
    if child_instance_family is not None:
        out["instance_family"] = str(child_instance_family.text or "")
    child_host_maintenance = el.find("HostMaintenance")
    if child_host_maintenance is not None:
        import capo_ec2.types.host_maintenance

        out["host_maintenance"] = capo_ec2.types.host_maintenance.deserialize_ec2_query(
            child_host_maintenance
        )
    child_host_ids = el.find("hostId")
    if child_host_ids is not None:
        import capo_ec2.types.request_host_id_list

        out["host_ids"] = capo_ec2.types.request_host_id_list.deserialize_ec2_query(
            child_host_ids
        )
    child_auto_placement = el.find("autoPlacement")
    if child_auto_placement is not None:
        import capo_ec2.types.auto_placement

        out["auto_placement"] = capo_ec2.types.auto_placement.deserialize_ec2_query(
            child_auto_placement
        )
    return out
