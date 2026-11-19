"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointServicePermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.permission_type
    import capo_ec2.types.value_string_list
    import capo_ec2.types.vpc_endpoint_service_id


class ModifyVpcEndpointServicePermissionsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    service_id: NotRequired[
        "capo_ec2.types.vpc_endpoint_service_id.VpcEndpointServiceId"
    ]
    """<p>The ID of the service.</p>"""
    add_allowed_principals: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARN) of the principals. Permissions are granted to the principals in this list. To grant permissions to all principals, specify an asterisk (*).</p>"""
    remove_allowed_principals: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARN) of the principals. Permissions are revoked for principals in this list.</p>"""
    permission_type: NotRequired["capo_ec2.types.permission_type.PermissionType"]
    """<p>The type of permission to add or remove. The permission type applies to all principals in <code>AddAllowedPrincipals</code> and <code>RemoveAllowedPrincipals</code>.</p> <ul> <li> <p> <code>vpc-endpoint</code> - Principals can create VPC endpoints that connect to the endpoint service.</p> </li> <li> <p> <code>transit-gateway-attachment</code> - Principals can create transit gateway attachments that connect to the endpoint service. This permission type is supported only for Gateway Load Balancer endpoint services. You can grant it only to Amazon Web Services accounts (<code>arn:aws:iam::account-id:root</code>). You can't grant it to users, IAM roles, organizations, organizational units, or all principals (*).</p> </li> </ul> <p>Default: <code>vpc-endpoint</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcEndpointServicePermissionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "service_id" in value:
        pairs.append((f"{key_prefix}ServiceId", str(value["service_id"])))
    if "add_allowed_principals" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["add_allowed_principals"], pairs, f"{key_prefix}AddAllowedPrincipals"
        )
    if "remove_allowed_principals" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["remove_allowed_principals"],
            pairs,
            f"{key_prefix}RemoveAllowedPrincipals",
        )
    if "permission_type" in value:
        import capo_ec2.types.permission_type

        capo_ec2.types.permission_type.serialize_ec2_query(
            value["permission_type"], pairs, f"{key_prefix}PermissionType"
        )


def deserialize_ec2_query(el: Element) -> ModifyVpcEndpointServicePermissionsRequest:
    out: ModifyVpcEndpointServicePermissionsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_service_id = el.find("ServiceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    child_add_allowed_principals = el.find("AddAllowedPrincipals")
    if child_add_allowed_principals is not None:
        import capo_ec2.types.value_string_list

        out["add_allowed_principals"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_add_allowed_principals
            )
        )
    child_remove_allowed_principals = el.find("RemoveAllowedPrincipals")
    if child_remove_allowed_principals is not None:
        import capo_ec2.types.value_string_list

        out["remove_allowed_principals"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_remove_allowed_principals
            )
        )
    child_permission_type = el.find("PermissionType")
    if child_permission_type is not None:
        import capo_ec2.types.permission_type

        out["permission_type"] = capo_ec2.types.permission_type.deserialize_ec2_query(
            child_permission_type
        )
    return out
