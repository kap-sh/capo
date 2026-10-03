"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyImageAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attribute_value
    import capo_ec2.types.boolean
    import capo_ec2.types.image_id
    import capo_ec2.types.launch_permission_modifications
    import capo_ec2.types.operation_type
    import capo_ec2.types.organization_arn_string_list
    import capo_ec2.types.organizational_unit_arn_string_list
    import capo_ec2.types.product_code_string_list
    import capo_ec2.types.string
    import capo_ec2.types.user_group_string_list
    import capo_ec2.types.user_id_string_list


class ModifyImageAttributeRequest(TypedDict, closed=True):
    attribute: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the attribute to modify.</p> <p>Valid values: <code>description</code> | <code>imdsSupport</code> | <code>launchPermission</code> </p>"""
    description: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>A new description for the AMI.</p>"""
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    launch_permission: NotRequired[
        "capo_ec2.types.launch_permission_modifications.LaunchPermissionModifications"
    ]
    """<p>A new launch permission for the AMI.</p>"""
    operation_type: NotRequired["capo_ec2.types.operation_type.OperationType"]
    """<p>The operation type. This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    product_codes: NotRequired[
        "capo_ec2.types.product_code_string_list.ProductCodeStringList"
    ]
    """<p>Not supported.</p>"""
    user_groups: NotRequired[
        "capo_ec2.types.user_group_string_list.UserGroupStringList"
    ]
    """<p>The user groups. This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    user_ids: NotRequired["capo_ec2.types.user_id_string_list.UserIdStringList"]
    """<p>The Amazon Web Services account IDs. This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    value: NotRequired["capo_ec2.types.string.String"]
    """<p>The value of the attribute being modified. This parameter can be used only when the <code>Attribute</code> parameter is <code>description</code> or <code>imdsSupport</code>.</p>"""
    organization_arns: NotRequired[
        "capo_ec2.types.organization_arn_string_list.OrganizationArnStringList"
    ]
    """<p>The Amazon Resource Name (ARN) of an organization. This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    organizational_unit_arns: NotRequired[
        "capo_ec2.types.organizational_unit_arn_string_list.OrganizationalUnitArnStringList"
    ]
    """<p>The Amazon Resource Name (ARN) of an organizational unit (OU). This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    imds_support: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>Set to <code>v2.0</code> to indicate that IMDSv2 is specified in the AMI. Instances launched from this AMI will have <code>HttpTokens</code> automatically set to <code>required</code> so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, <code>HttpPutResponseHopLimit</code> is set to <code>2</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration">Configure the AMI</a> in the <i>Amazon EC2 User Guide</i>.</p> <important> <p>Do not use this parameter unless your AMI software supports IMDSv2. After you set the value to <code>v2.0</code>, you can't undo it. The only way to “reset” your AMI is to create a new AMI from the underlying snapshot.</p> </important>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyImageAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attribute" in value:
        pairs.append((f"{key_prefix}Attribute", str(value["attribute"])))
    if "description" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["description"], pairs, f"{key_prefix}Description"
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "launch_permission" in value:
        import capo_ec2.types.launch_permission_modifications

        capo_ec2.types.launch_permission_modifications.serialize_ec2_query(
            value["launch_permission"], pairs, f"{key_prefix}LaunchPermission"
        )
    if "operation_type" in value:
        import capo_ec2.types.operation_type

        capo_ec2.types.operation_type.serialize_ec2_query(
            value["operation_type"], pairs, f"{key_prefix}OperationType"
        )
    if "product_codes" in value:
        import capo_ec2.types.product_code_string_list

        capo_ec2.types.product_code_string_list.serialize_ec2_query(
            value["product_codes"], pairs, f"{key_prefix}ProductCode"
        )
    if "user_groups" in value:
        import capo_ec2.types.user_group_string_list

        capo_ec2.types.user_group_string_list.serialize_ec2_query(
            value["user_groups"], pairs, f"{key_prefix}UserGroup"
        )
    if "user_ids" in value:
        import capo_ec2.types.user_id_string_list

        capo_ec2.types.user_id_string_list.serialize_ec2_query(
            value["user_ids"], pairs, f"{key_prefix}UserId"
        )
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))
    if "organization_arns" in value:
        import capo_ec2.types.organization_arn_string_list

        capo_ec2.types.organization_arn_string_list.serialize_ec2_query(
            value["organization_arns"], pairs, f"{key_prefix}OrganizationArn"
        )
    if "organizational_unit_arns" in value:
        import capo_ec2.types.organizational_unit_arn_string_list

        capo_ec2.types.organizational_unit_arn_string_list.serialize_ec2_query(
            value["organizational_unit_arns"],
            pairs,
            f"{key_prefix}OrganizationalUnitArn",
        )
    if "imds_support" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["imds_support"], pairs, f"{key_prefix}ImdsSupport"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyImageAttributeRequest:
    out: ModifyImageAttributeRequest = {}  # type: ignore[typeddict-item]
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        out["attribute"] = str(child_attribute.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        import capo_ec2.types.attribute_value

        out["description"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_description
        )
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_launch_permission = el.find("LaunchPermission")
    if child_launch_permission is not None:
        import capo_ec2.types.launch_permission_modifications

        out["launch_permission"] = (
            capo_ec2.types.launch_permission_modifications.deserialize_ec2_query(
                child_launch_permission
            )
        )
    child_operation_type = el.find("OperationType")
    if child_operation_type is not None:
        import capo_ec2.types.operation_type

        out["operation_type"] = capo_ec2.types.operation_type.deserialize_ec2_query(
            child_operation_type
        )
    child_product_codes = el.find("ProductCode")
    if child_product_codes is not None:
        import capo_ec2.types.product_code_string_list

        out["product_codes"] = (
            capo_ec2.types.product_code_string_list.deserialize_ec2_query(
                child_product_codes
            )
        )
    child_user_groups = el.find("UserGroup")
    if child_user_groups is not None:
        import capo_ec2.types.user_group_string_list

        out["user_groups"] = (
            capo_ec2.types.user_group_string_list.deserialize_ec2_query(
                child_user_groups
            )
        )
    child_user_ids = el.find("UserId")
    if child_user_ids is not None:
        import capo_ec2.types.user_id_string_list

        out["user_ids"] = capo_ec2.types.user_id_string_list.deserialize_ec2_query(
            child_user_ids
        )
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    child_organization_arns = el.find("OrganizationArn")
    if child_organization_arns is not None:
        import capo_ec2.types.organization_arn_string_list

        out["organization_arns"] = (
            capo_ec2.types.organization_arn_string_list.deserialize_ec2_query(
                child_organization_arns
            )
        )
    child_organizational_unit_arns = el.find("OrganizationalUnitArn")
    if child_organizational_unit_arns is not None:
        import capo_ec2.types.organizational_unit_arn_string_list

        out["organizational_unit_arns"] = (
            capo_ec2.types.organizational_unit_arn_string_list.deserialize_ec2_query(
                child_organizational_unit_arns
            )
        )
    child_imds_support = el.find("ImdsSupport")
    if child_imds_support is not None:
        import capo_ec2.types.attribute_value

        out["imds_support"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_imds_support
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
