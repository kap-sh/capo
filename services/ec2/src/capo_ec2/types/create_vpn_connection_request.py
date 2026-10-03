"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpnConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.customer_gateway_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.transit_gateway_id
    import capo_ec2.types.vpn_concentrator_id
    import capo_ec2.types.vpn_connection_options_specification
    import capo_ec2.types.vpn_gateway_id


class CreateVpnConnectionRequest(TypedDict, closed=True):
    customer_gateway_id: NotRequired[
        "capo_ec2.types.customer_gateway_id.CustomerGatewayId"
    ]
    """<p>The ID of the customer gateway.</p>"""
    type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of VPN connection (<code>ipsec.1</code>).</p>"""
    vpn_gateway_id: NotRequired["capo_ec2.types.vpn_gateway_id.VpnGatewayId"]
    """<p>The ID of the virtual private gateway. If you specify a virtual private gateway, you cannot specify a transit gateway.</p>"""
    transit_gateway_id: NotRequired[
        "capo_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway. If you specify a transit gateway, you cannot specify a virtual private gateway.</p>"""
    vpn_concentrator_id: NotRequired[
        "capo_ec2.types.vpn_concentrator_id.VpnConcentratorId"
    ]
    """<p>The ID of the VPN concentrator to associate with the VPN connection.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the VPN connection.</p>"""
    pre_shared_key_storage: NotRequired["capo_ec2.types.string.String"]
    """<p>Specifies the storage mode for the pre-shared key (PSK). Valid values are <code>Standard</code>" (stored in the Site-to-Site VPN service) or <code>SecretsManager</code> (stored in Amazon Web Services Secrets Manager).</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    options: NotRequired[
        "capo_ec2.types.vpn_connection_options_specification.VpnConnectionOptionsSpecification"
    ]
    """<p>The options for the VPN connection.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpnConnectionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "customer_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}CustomerGatewayId", str(value["customer_gateway_id"]))
        )
    if "type" in value:
        pairs.append((f"{key_prefix}Type", str(value["type"])))
    if "vpn_gateway_id" in value:
        pairs.append((f"{key_prefix}VpnGatewayId", str(value["vpn_gateway_id"])))
    if "transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}TransitGatewayId", str(value["transit_gateway_id"]))
        )
    if "vpn_concentrator_id" in value:
        pairs.append(
            (f"{key_prefix}VpnConcentratorId", str(value["vpn_concentrator_id"]))
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "pre_shared_key_storage" in value:
        pairs.append(
            (f"{key_prefix}PreSharedKeyStorage", str(value["pre_shared_key_storage"]))
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "options" in value:
        import capo_ec2.types.vpn_connection_options_specification

        capo_ec2.types.vpn_connection_options_specification.serialize_ec2_query(
            value["options"], pairs, f"{key_prefix}Options"
        )


def deserialize_ec2_query(el: Element) -> CreateVpnConnectionRequest:
    out: CreateVpnConnectionRequest = {}  # type: ignore[typeddict-item]
    child_customer_gateway_id = el.find("CustomerGatewayId")
    if child_customer_gateway_id is not None:
        out["customer_gateway_id"] = str(child_customer_gateway_id.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    child_vpn_gateway_id = el.find("VpnGatewayId")
    if child_vpn_gateway_id is not None:
        out["vpn_gateway_id"] = str(child_vpn_gateway_id.text or "")
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_vpn_concentrator_id = el.find("VpnConcentratorId")
    if child_vpn_concentrator_id is not None:
        out["vpn_concentrator_id"] = str(child_vpn_concentrator_id.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_pre_shared_key_storage = el.find("PreSharedKeyStorage")
    if child_pre_shared_key_storage is not None:
        out["pre_shared_key_storage"] = str(child_pre_shared_key_storage.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_options = el.find("options")
    if child_options is not None:
        import capo_ec2.types.vpn_connection_options_specification

        out["options"] = (
            capo_ec2.types.vpn_connection_options_specification.deserialize_ec2_query(
                child_options
            )
        )
    return out
