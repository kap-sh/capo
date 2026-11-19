"""Generated from Smithy shape ``com.amazonaws.fms#RemediationAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.create_network_acl_action
    import capo_fms.types.create_network_acl_entries_action
    import capo_fms.types.delete_network_acl_entries_action
    import capo_fms.types.ec2_associate_route_table_action
    import capo_fms.types.ec2_copy_route_table_action
    import capo_fms.types.ec2_create_route_action
    import capo_fms.types.ec2_create_route_table_action
    import capo_fms.types.ec2_delete_route_action
    import capo_fms.types.ec2_replace_route_action
    import capo_fms.types.ec2_replace_route_table_association_action
    import capo_fms.types.fms_policy_update_firewall_creation_config_action
    import capo_fms.types.length_bounded_string
    import capo_fms.types.replace_network_acl_association_action


class RemediationAction(TypedDict, closed=True):
    description: NotRequired["capo_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>A description of a remediation action.</p>"""
    ec2_create_route_action: NotRequired[
        "capo_fms.types.ec2_create_route_action.EC2CreateRouteAction"
    ]
    """<p>Information about the CreateRoute action in the Amazon EC2 API.</p>"""
    ec2_replace_route_action: NotRequired[
        "capo_fms.types.ec2_replace_route_action.EC2ReplaceRouteAction"
    ]
    """<p>Information about the ReplaceRoute action in the Amazon EC2 API.</p>"""
    ec2_delete_route_action: NotRequired[
        "capo_fms.types.ec2_delete_route_action.EC2DeleteRouteAction"
    ]
    """<p>Information about the DeleteRoute action in the Amazon EC2 API.</p>"""
    ec2_copy_route_table_action: NotRequired[
        "capo_fms.types.ec2_copy_route_table_action.EC2CopyRouteTableAction"
    ]
    """<p>Information about the CopyRouteTable action in the Amazon EC2 API.</p>"""
    ec2_replace_route_table_association_action: NotRequired[
        "capo_fms.types.ec2_replace_route_table_association_action.EC2ReplaceRouteTableAssociationAction"
    ]
    """<p>Information about the ReplaceRouteTableAssociation action in the Amazon EC2 API.</p>"""
    ec2_associate_route_table_action: NotRequired[
        "capo_fms.types.ec2_associate_route_table_action.EC2AssociateRouteTableAction"
    ]
    """<p>Information about the AssociateRouteTable action in the Amazon EC2 API.</p>"""
    ec2_create_route_table_action: NotRequired[
        "capo_fms.types.ec2_create_route_table_action.EC2CreateRouteTableAction"
    ]
    """<p>Information about the CreateRouteTable action in the Amazon EC2 API.</p>"""
    fms_policy_update_firewall_creation_config_action: NotRequired[
        "capo_fms.types.fms_policy_update_firewall_creation_config_action.FMSPolicyUpdateFirewallCreationConfigAction"
    ]
    """<p>The remedial action to take when updating a firewall configuration.</p>"""
    create_network_acl_action: NotRequired[
        "capo_fms.types.create_network_acl_action.CreateNetworkAclAction"
    ]
    """<p>Information about the <code>CreateNetworkAcl</code> action in Amazon EC2.</p>"""
    replace_network_acl_association_action: NotRequired[
        "capo_fms.types.replace_network_acl_association_action.ReplaceNetworkAclAssociationAction"
    ]
    """<p>Information about the <code>ReplaceNetworkAclAssociation</code> action in Amazon EC2. </p>"""
    create_network_acl_entries_action: NotRequired[
        "capo_fms.types.create_network_acl_entries_action.CreateNetworkAclEntriesAction"
    ]
    """<p>Information about the <code>CreateNetworkAclEntries</code> action in Amazon EC2.</p>"""
    delete_network_acl_entries_action: NotRequired[
        "capo_fms.types.delete_network_acl_entries_action.DeleteNetworkAclEntriesAction"
    ]
    """<p>Information about the <code>DeleteNetworkAclEntries</code> action in Amazon EC2.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "ec2_create_route_action" in value:
        import capo_fms.types.ec2_create_route_action

        out["EC2CreateRouteAction"] = (
            capo_fms.types.ec2_create_route_action.serialize_aws_json_1_1(
                value["ec2_create_route_action"]
            )
        )
    if "ec2_replace_route_action" in value:
        import capo_fms.types.ec2_replace_route_action

        out["EC2ReplaceRouteAction"] = (
            capo_fms.types.ec2_replace_route_action.serialize_aws_json_1_1(
                value["ec2_replace_route_action"]
            )
        )
    if "ec2_delete_route_action" in value:
        import capo_fms.types.ec2_delete_route_action

        out["EC2DeleteRouteAction"] = (
            capo_fms.types.ec2_delete_route_action.serialize_aws_json_1_1(
                value["ec2_delete_route_action"]
            )
        )
    if "ec2_copy_route_table_action" in value:
        import capo_fms.types.ec2_copy_route_table_action

        out["EC2CopyRouteTableAction"] = (
            capo_fms.types.ec2_copy_route_table_action.serialize_aws_json_1_1(
                value["ec2_copy_route_table_action"]
            )
        )
    if "ec2_replace_route_table_association_action" in value:
        import capo_fms.types.ec2_replace_route_table_association_action

        out["EC2ReplaceRouteTableAssociationAction"] = (
            capo_fms.types.ec2_replace_route_table_association_action.serialize_aws_json_1_1(
                value["ec2_replace_route_table_association_action"]
            )
        )
    if "ec2_associate_route_table_action" in value:
        import capo_fms.types.ec2_associate_route_table_action

        out["EC2AssociateRouteTableAction"] = (
            capo_fms.types.ec2_associate_route_table_action.serialize_aws_json_1_1(
                value["ec2_associate_route_table_action"]
            )
        )
    if "ec2_create_route_table_action" in value:
        import capo_fms.types.ec2_create_route_table_action

        out["EC2CreateRouteTableAction"] = (
            capo_fms.types.ec2_create_route_table_action.serialize_aws_json_1_1(
                value["ec2_create_route_table_action"]
            )
        )
    if "fms_policy_update_firewall_creation_config_action" in value:
        import capo_fms.types.fms_policy_update_firewall_creation_config_action

        out["FMSPolicyUpdateFirewallCreationConfigAction"] = (
            capo_fms.types.fms_policy_update_firewall_creation_config_action.serialize_aws_json_1_1(
                value["fms_policy_update_firewall_creation_config_action"]
            )
        )
    if "create_network_acl_action" in value:
        import capo_fms.types.create_network_acl_action

        out["CreateNetworkAclAction"] = (
            capo_fms.types.create_network_acl_action.serialize_aws_json_1_1(
                value["create_network_acl_action"]
            )
        )
    if "replace_network_acl_association_action" in value:
        import capo_fms.types.replace_network_acl_association_action

        out["ReplaceNetworkAclAssociationAction"] = (
            capo_fms.types.replace_network_acl_association_action.serialize_aws_json_1_1(
                value["replace_network_acl_association_action"]
            )
        )
    if "create_network_acl_entries_action" in value:
        import capo_fms.types.create_network_acl_entries_action

        out["CreateNetworkAclEntriesAction"] = (
            capo_fms.types.create_network_acl_entries_action.serialize_aws_json_1_1(
                value["create_network_acl_entries_action"]
            )
        )
    if "delete_network_acl_entries_action" in value:
        import capo_fms.types.delete_network_acl_entries_action

        out["DeleteNetworkAclEntriesAction"] = (
            capo_fms.types.delete_network_acl_entries_action.serialize_aws_json_1_1(
                value["delete_network_acl_entries_action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemediationAction:
    out: RemediationAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EC2CreateRouteAction") is not None:
        import capo_fms.types.ec2_create_route_action

        out["ec2_create_route_action"] = (
            capo_fms.types.ec2_create_route_action.deserialize_aws_json_1_1(
                data["EC2CreateRouteAction"]
            )
        )
    if data.get("EC2ReplaceRouteAction") is not None:
        import capo_fms.types.ec2_replace_route_action

        out["ec2_replace_route_action"] = (
            capo_fms.types.ec2_replace_route_action.deserialize_aws_json_1_1(
                data["EC2ReplaceRouteAction"]
            )
        )
    if data.get("EC2DeleteRouteAction") is not None:
        import capo_fms.types.ec2_delete_route_action

        out["ec2_delete_route_action"] = (
            capo_fms.types.ec2_delete_route_action.deserialize_aws_json_1_1(
                data["EC2DeleteRouteAction"]
            )
        )
    if data.get("EC2CopyRouteTableAction") is not None:
        import capo_fms.types.ec2_copy_route_table_action

        out["ec2_copy_route_table_action"] = (
            capo_fms.types.ec2_copy_route_table_action.deserialize_aws_json_1_1(
                data["EC2CopyRouteTableAction"]
            )
        )
    if data.get("EC2ReplaceRouteTableAssociationAction") is not None:
        import capo_fms.types.ec2_replace_route_table_association_action

        out["ec2_replace_route_table_association_action"] = (
            capo_fms.types.ec2_replace_route_table_association_action.deserialize_aws_json_1_1(
                data["EC2ReplaceRouteTableAssociationAction"]
            )
        )
    if data.get("EC2AssociateRouteTableAction") is not None:
        import capo_fms.types.ec2_associate_route_table_action

        out["ec2_associate_route_table_action"] = (
            capo_fms.types.ec2_associate_route_table_action.deserialize_aws_json_1_1(
                data["EC2AssociateRouteTableAction"]
            )
        )
    if data.get("EC2CreateRouteTableAction") is not None:
        import capo_fms.types.ec2_create_route_table_action

        out["ec2_create_route_table_action"] = (
            capo_fms.types.ec2_create_route_table_action.deserialize_aws_json_1_1(
                data["EC2CreateRouteTableAction"]
            )
        )
    if data.get("FMSPolicyUpdateFirewallCreationConfigAction") is not None:
        import capo_fms.types.fms_policy_update_firewall_creation_config_action

        out["fms_policy_update_firewall_creation_config_action"] = (
            capo_fms.types.fms_policy_update_firewall_creation_config_action.deserialize_aws_json_1_1(
                data["FMSPolicyUpdateFirewallCreationConfigAction"]
            )
        )
    if data.get("CreateNetworkAclAction") is not None:
        import capo_fms.types.create_network_acl_action

        out["create_network_acl_action"] = (
            capo_fms.types.create_network_acl_action.deserialize_aws_json_1_1(
                data["CreateNetworkAclAction"]
            )
        )
    if data.get("ReplaceNetworkAclAssociationAction") is not None:
        import capo_fms.types.replace_network_acl_association_action

        out["replace_network_acl_association_action"] = (
            capo_fms.types.replace_network_acl_association_action.deserialize_aws_json_1_1(
                data["ReplaceNetworkAclAssociationAction"]
            )
        )
    if data.get("CreateNetworkAclEntriesAction") is not None:
        import capo_fms.types.create_network_acl_entries_action

        out["create_network_acl_entries_action"] = (
            capo_fms.types.create_network_acl_entries_action.deserialize_aws_json_1_1(
                data["CreateNetworkAclEntriesAction"]
            )
        )
    if data.get("DeleteNetworkAclEntriesAction") is not None:
        import capo_fms.types.delete_network_acl_entries_action

        out["delete_network_acl_entries_action"] = (
            capo_fms.types.delete_network_acl_entries_action.deserialize_aws_json_1_1(
                data["DeleteNetworkAclEntriesAction"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RemediationAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "ec2_create_route_action" in value:
        import capo_fms.types.ec2_create_route_action

        out["EC2CreateRouteAction"] = (
            capo_fms.types.ec2_create_route_action.serialize_cbor(
                value["ec2_create_route_action"]
            )
        )
    if "ec2_replace_route_action" in value:
        import capo_fms.types.ec2_replace_route_action

        out["EC2ReplaceRouteAction"] = (
            capo_fms.types.ec2_replace_route_action.serialize_cbor(
                value["ec2_replace_route_action"]
            )
        )
    if "ec2_delete_route_action" in value:
        import capo_fms.types.ec2_delete_route_action

        out["EC2DeleteRouteAction"] = (
            capo_fms.types.ec2_delete_route_action.serialize_cbor(
                value["ec2_delete_route_action"]
            )
        )
    if "ec2_copy_route_table_action" in value:
        import capo_fms.types.ec2_copy_route_table_action

        out["EC2CopyRouteTableAction"] = (
            capo_fms.types.ec2_copy_route_table_action.serialize_cbor(
                value["ec2_copy_route_table_action"]
            )
        )
    if "ec2_replace_route_table_association_action" in value:
        import capo_fms.types.ec2_replace_route_table_association_action

        out["EC2ReplaceRouteTableAssociationAction"] = (
            capo_fms.types.ec2_replace_route_table_association_action.serialize_cbor(
                value["ec2_replace_route_table_association_action"]
            )
        )
    if "ec2_associate_route_table_action" in value:
        import capo_fms.types.ec2_associate_route_table_action

        out["EC2AssociateRouteTableAction"] = (
            capo_fms.types.ec2_associate_route_table_action.serialize_cbor(
                value["ec2_associate_route_table_action"]
            )
        )
    if "ec2_create_route_table_action" in value:
        import capo_fms.types.ec2_create_route_table_action

        out["EC2CreateRouteTableAction"] = (
            capo_fms.types.ec2_create_route_table_action.serialize_cbor(
                value["ec2_create_route_table_action"]
            )
        )
    if "fms_policy_update_firewall_creation_config_action" in value:
        import capo_fms.types.fms_policy_update_firewall_creation_config_action

        out["FMSPolicyUpdateFirewallCreationConfigAction"] = (
            capo_fms.types.fms_policy_update_firewall_creation_config_action.serialize_cbor(
                value["fms_policy_update_firewall_creation_config_action"]
            )
        )
    if "create_network_acl_action" in value:
        import capo_fms.types.create_network_acl_action

        out["CreateNetworkAclAction"] = (
            capo_fms.types.create_network_acl_action.serialize_cbor(
                value["create_network_acl_action"]
            )
        )
    if "replace_network_acl_association_action" in value:
        import capo_fms.types.replace_network_acl_association_action

        out["ReplaceNetworkAclAssociationAction"] = (
            capo_fms.types.replace_network_acl_association_action.serialize_cbor(
                value["replace_network_acl_association_action"]
            )
        )
    if "create_network_acl_entries_action" in value:
        import capo_fms.types.create_network_acl_entries_action

        out["CreateNetworkAclEntriesAction"] = (
            capo_fms.types.create_network_acl_entries_action.serialize_cbor(
                value["create_network_acl_entries_action"]
            )
        )
    if "delete_network_acl_entries_action" in value:
        import capo_fms.types.delete_network_acl_entries_action

        out["DeleteNetworkAclEntriesAction"] = (
            capo_fms.types.delete_network_acl_entries_action.serialize_cbor(
                value["delete_network_acl_entries_action"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RemediationAction:
    out: RemediationAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EC2CreateRouteAction") is not None:
        import capo_fms.types.ec2_create_route_action

        out["ec2_create_route_action"] = (
            capo_fms.types.ec2_create_route_action.deserialize_cbor(
                data["EC2CreateRouteAction"]
            )
        )
    if data.get("EC2ReplaceRouteAction") is not None:
        import capo_fms.types.ec2_replace_route_action

        out["ec2_replace_route_action"] = (
            capo_fms.types.ec2_replace_route_action.deserialize_cbor(
                data["EC2ReplaceRouteAction"]
            )
        )
    if data.get("EC2DeleteRouteAction") is not None:
        import capo_fms.types.ec2_delete_route_action

        out["ec2_delete_route_action"] = (
            capo_fms.types.ec2_delete_route_action.deserialize_cbor(
                data["EC2DeleteRouteAction"]
            )
        )
    if data.get("EC2CopyRouteTableAction") is not None:
        import capo_fms.types.ec2_copy_route_table_action

        out["ec2_copy_route_table_action"] = (
            capo_fms.types.ec2_copy_route_table_action.deserialize_cbor(
                data["EC2CopyRouteTableAction"]
            )
        )
    if data.get("EC2ReplaceRouteTableAssociationAction") is not None:
        import capo_fms.types.ec2_replace_route_table_association_action

        out["ec2_replace_route_table_association_action"] = (
            capo_fms.types.ec2_replace_route_table_association_action.deserialize_cbor(
                data["EC2ReplaceRouteTableAssociationAction"]
            )
        )
    if data.get("EC2AssociateRouteTableAction") is not None:
        import capo_fms.types.ec2_associate_route_table_action

        out["ec2_associate_route_table_action"] = (
            capo_fms.types.ec2_associate_route_table_action.deserialize_cbor(
                data["EC2AssociateRouteTableAction"]
            )
        )
    if data.get("EC2CreateRouteTableAction") is not None:
        import capo_fms.types.ec2_create_route_table_action

        out["ec2_create_route_table_action"] = (
            capo_fms.types.ec2_create_route_table_action.deserialize_cbor(
                data["EC2CreateRouteTableAction"]
            )
        )
    if data.get("FMSPolicyUpdateFirewallCreationConfigAction") is not None:
        import capo_fms.types.fms_policy_update_firewall_creation_config_action

        out["fms_policy_update_firewall_creation_config_action"] = (
            capo_fms.types.fms_policy_update_firewall_creation_config_action.deserialize_cbor(
                data["FMSPolicyUpdateFirewallCreationConfigAction"]
            )
        )
    if data.get("CreateNetworkAclAction") is not None:
        import capo_fms.types.create_network_acl_action

        out["create_network_acl_action"] = (
            capo_fms.types.create_network_acl_action.deserialize_cbor(
                data["CreateNetworkAclAction"]
            )
        )
    if data.get("ReplaceNetworkAclAssociationAction") is not None:
        import capo_fms.types.replace_network_acl_association_action

        out["replace_network_acl_association_action"] = (
            capo_fms.types.replace_network_acl_association_action.deserialize_cbor(
                data["ReplaceNetworkAclAssociationAction"]
            )
        )
    if data.get("CreateNetworkAclEntriesAction") is not None:
        import capo_fms.types.create_network_acl_entries_action

        out["create_network_acl_entries_action"] = (
            capo_fms.types.create_network_acl_entries_action.deserialize_cbor(
                data["CreateNetworkAclEntriesAction"]
            )
        )
    if data.get("DeleteNetworkAclEntriesAction") is not None:
        import capo_fms.types.delete_network_acl_entries_action

        out["delete_network_acl_entries_action"] = (
            capo_fms.types.delete_network_acl_entries_action.deserialize_cbor(
                data["DeleteNetworkAclEntriesAction"]
            )
        )
    return out
