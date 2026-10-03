"""Generated from Smithy shape ``com.amazonaws.ec2#AllocateHostsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.asset_id_list
    import capo_ec2.types.auto_placement
    import capo_ec2.types.availability_zone_id
    import capo_ec2.types.availability_zone_name
    import capo_ec2.types.host_cpu_options_request
    import capo_ec2.types.host_maintenance
    import capo_ec2.types.host_recovery
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class AllocateHostsRequest(TypedDict, closed=True):
    instance_family: NotRequired["capo_ec2.types.string.String"]
    """<p>Specifies the instance family to be supported by the Dedicated Hosts. If you specify an instance family, the Dedicated Hosts support multiple instance types within that instance family.</p> <p>If you want the Dedicated Hosts to support a specific instance type only, omit this parameter and specify <b>InstanceType</b> instead. You cannot specify <b>InstanceFamily</b> and <b>InstanceType</b> in the same request.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the Dedicated Host during creation.</p>"""
    host_recovery: NotRequired["capo_ec2.types.host_recovery.HostRecovery"]
    """<p>Indicates whether to enable or disable host recovery for the Dedicated Host. Host recovery is disabled by default. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-recovery.html"> Host recovery</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: <code>off</code> </p>"""
    outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Outpost on which to allocate the Dedicated Host. If you specify <b>OutpostArn</b>, you can optionally specify <b>AssetIds</b>.</p> <p>If you are allocating the Dedicated Host in a Region, omit this parameter.</p>"""
    host_maintenance: NotRequired["capo_ec2.types.host_maintenance.HostMaintenance"]
    """<p>Indicates whether to enable or disable host maintenance for the Dedicated Host. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-maintenance.html">Host maintenance</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    asset_ids: NotRequired["capo_ec2.types.asset_id_list.AssetIdList"]
    """<p>The IDs of the Outpost hardware assets on which to allocate the Dedicated Hosts. Targeting specific hardware assets on an Outpost can help to minimize latency between your workloads. This parameter is supported only if you specify <b>OutpostArn</b>. If you are allocating the Dedicated Hosts in a Region, omit this parameter.</p> <ul> <li> <p>If you specify this parameter, you can omit <b>Quantity</b>. In this case, Amazon EC2 allocates a Dedicated Host on each specified hardware asset.</p> </li> <li> <p>If you specify both <b>AssetIds</b> and <b>Quantity</b>, then the value for <b>Quantity</b> must be equal to the number of asset IDs specified.</p> </li> </ul>"""
    availability_zone_id: NotRequired[
        "capo_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone.</p>"""
    cpu_options: NotRequired[
        "capo_ec2.types.host_cpu_options_request.HostCpuOptionsRequest"
    ]
    """<p>The CPU configuration options to apply to the Dedicated Host.</p>"""
    auto_placement: NotRequired["capo_ec2.types.auto_placement.AutoPlacement"]
    """<p>Indicates whether the host accepts any untargeted instance launches that match its instance type configuration, or if it only accepts Host tenancy instance launches that specify its unique host ID. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-dedicated-hosts-work.html#dedicated-hosts-understanding"> Understanding auto-placement and affinity</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: <code>off</code> </p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring Idempotency</a>.</p>"""
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p>Specifies the instance type to be supported by the Dedicated Hosts. If you specify an instance type, the Dedicated Hosts support instances of the specified instance type only.</p> <p>If you want the Dedicated Hosts to support multiple instance types in a specific instance family, omit this parameter and specify <b>InstanceFamily</b> instead. You cannot specify <b>InstanceType</b> and <b>InstanceFamily</b> in the same request.</p>"""
    quantity: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of Dedicated Hosts to allocate to your account with these parameters. If you are allocating the Dedicated Hosts on an Outpost, and you specify <b>AssetIds</b>, you can omit this parameter. In this case, Amazon EC2 allocates a Dedicated Host on each specified hardware asset. If you specify both <b>AssetIds</b> and <b>Quantity</b>, then the value that you specify for <b>Quantity</b> must be equal to the number of asset IDs specified.</p>"""
    availability_zone: NotRequired[
        "capo_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone in which to allocate the Dedicated Host.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AllocateHostsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_family" in value:
        pairs.append((f"{key_prefix}InstanceFamily", str(value["instance_family"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "host_recovery" in value:
        import capo_ec2.types.host_recovery

        capo_ec2.types.host_recovery.serialize_ec2_query(
            value["host_recovery"], pairs, f"{key_prefix}HostRecovery"
        )
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "host_maintenance" in value:
        import capo_ec2.types.host_maintenance

        capo_ec2.types.host_maintenance.serialize_ec2_query(
            value["host_maintenance"], pairs, f"{key_prefix}HostMaintenance"
        )
    if "asset_ids" in value:
        import capo_ec2.types.asset_id_list

        capo_ec2.types.asset_id_list.serialize_ec2_query(
            value["asset_ids"], pairs, f"{key_prefix}AssetId"
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "cpu_options" in value:
        import capo_ec2.types.host_cpu_options_request

        capo_ec2.types.host_cpu_options_request.serialize_ec2_query(
            value["cpu_options"], pairs, f"{key_prefix}CpuOptions"
        )
    if "auto_placement" in value:
        import capo_ec2.types.auto_placement

        capo_ec2.types.auto_placement.serialize_ec2_query(
            value["auto_placement"], pairs, f"{key_prefix}AutoPlacement"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "quantity" in value:
        pairs.append((f"{key_prefix}Quantity", str(value["quantity"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))


def deserialize_ec2_query(el: Element) -> AllocateHostsRequest:
    out: AllocateHostsRequest = {}  # type: ignore[typeddict-item]
    child_instance_family = el.find("InstanceFamily")
    if child_instance_family is not None:
        out["instance_family"] = str(child_instance_family.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_host_recovery = el.find("HostRecovery")
    if child_host_recovery is not None:
        import capo_ec2.types.host_recovery

        out["host_recovery"] = capo_ec2.types.host_recovery.deserialize_ec2_query(
            child_host_recovery
        )
    child_outpost_arn = el.find("OutpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_host_maintenance = el.find("HostMaintenance")
    if child_host_maintenance is not None:
        import capo_ec2.types.host_maintenance

        out["host_maintenance"] = capo_ec2.types.host_maintenance.deserialize_ec2_query(
            child_host_maintenance
        )
    child_asset_ids = el.find("AssetId")
    if child_asset_ids is not None:
        import capo_ec2.types.asset_id_list

        out["asset_ids"] = capo_ec2.types.asset_id_list.deserialize_ec2_query(
            child_asset_ids
        )
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_cpu_options = el.find("CpuOptions")
    if child_cpu_options is not None:
        import capo_ec2.types.host_cpu_options_request

        out["cpu_options"] = (
            capo_ec2.types.host_cpu_options_request.deserialize_ec2_query(
                child_cpu_options
            )
        )
    child_auto_placement = el.find("autoPlacement")
    if child_auto_placement is not None:
        import capo_ec2.types.auto_placement

        out["auto_placement"] = capo_ec2.types.auto_placement.deserialize_ec2_query(
            child_auto_placement
        )
    child_client_token = el.find("clientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_quantity = el.find("quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    return out
