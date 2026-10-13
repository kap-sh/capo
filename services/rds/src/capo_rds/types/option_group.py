"""Generated from Smithy shape ``com.amazonaws.rds#OptionGroup``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.options_list
    import capo_rds.types.string
    import capo_rds.types.t_stamp


class OptionGroup(TypedDict, closed=True):
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the name of the option group.</p>"""
    option_group_description: NotRequired["capo_rds.types.string.String"]
    """<p>Provides a description of the option group.</p>"""
    engine_name: NotRequired["capo_rds.types.string.String"]
    """<p>Indicates the name of the engine that this option group can be applied to.</p>"""
    major_engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>Indicates the major engine version associated with this option group.</p>"""
    options: NotRequired["capo_rds.types.options_list.OptionsList"]
    """<p>Indicates what options are available in the option group.</p>"""
    allows_vpc_and_non_vpc_instance_memberships: NotRequired[
        "capo_rds.types.boolean.Boolean"
    ]
    """<p>Indicates whether this option group can be applied to both VPC and non-VPC instances. The value <code>true</code> indicates the option group can be applied to both VPC and non-VPC instances.</p>"""
    vpc_id: NotRequired["capo_rds.types.string.String"]
    """<p>If <b>AllowsVpcAndNonVpcInstanceMemberships</b> is <code>false</code>, this field is blank. If <b>AllowsVpcAndNonVpcInstanceMemberships</b> is <code>true</code> and this field is blank, then this option group can be applied to both VPC and non-VPC instances. If this field contains a value, then this option group can only be applied to instances that are in the VPC indicated by this field.</p>"""
    option_group_arn: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the Amazon Resource Name (ARN) for the option group.</p>"""
    source_option_group: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the name of the option group from which this option group is copied.</p>"""
    source_account_id: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the Amazon Web Services account ID for the option group from which this option group is copied.</p>"""
    copy_timestamp: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>Indicates when the option group was copied.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "option_group_name" in value:
        pairs.append((f"{key_prefix}OptionGroupName", str(value["option_group_name"])))
    if "option_group_description" in value:
        pairs.append(
            (
                f"{key_prefix}OptionGroupDescription",
                str(value["option_group_description"]),
            )
        )
    if "engine_name" in value:
        pairs.append((f"{key_prefix}EngineName", str(value["engine_name"])))
    if "major_engine_version" in value:
        pairs.append(
            (f"{key_prefix}MajorEngineVersion", str(value["major_engine_version"]))
        )
    if "options" in value:
        import capo_rds.types.options_list

        capo_rds.types.options_list.serialize_query(
            value["options"], pairs, f"{key_prefix}Options"
        )
    if "allows_vpc_and_non_vpc_instance_memberships" in value:
        pairs.append(
            (
                f"{key_prefix}AllowsVpcAndNonVpcInstanceMemberships",
                "true"
                if value["allows_vpc_and_non_vpc_instance_memberships"]
                else "false",
            )
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "option_group_arn" in value:
        pairs.append((f"{key_prefix}OptionGroupArn", str(value["option_group_arn"])))
    if "source_option_group" in value:
        pairs.append(
            (f"{key_prefix}SourceOptionGroup", str(value["source_option_group"]))
        )
    if "source_account_id" in value:
        pairs.append((f"{key_prefix}SourceAccountId", str(value["source_account_id"])))
    if "copy_timestamp" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["copy_timestamp"], pairs, f"{key_prefix}CopyTimestamp"
        )


def deserialize_query(el: Element) -> OptionGroup:
    out: OptionGroup = {}  # type: ignore[typeddict-item]
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    child_option_group_description = el.find("OptionGroupDescription")
    if child_option_group_description is not None:
        out["option_group_description"] = str(child_option_group_description.text or "")
    child_engine_name = el.find("EngineName")
    if child_engine_name is not None:
        out["engine_name"] = str(child_engine_name.text or "")
    child_major_engine_version = el.find("MajorEngineVersion")
    if child_major_engine_version is not None:
        out["major_engine_version"] = str(child_major_engine_version.text or "")
    child_options = el.find("Options")
    if child_options is not None:
        import capo_rds.types.options_list

        out["options"] = capo_rds.types.options_list.deserialize_query(child_options)
    child_allows_vpc_and_non_vpc_instance_memberships = el.find(
        "AllowsVpcAndNonVpcInstanceMemberships"
    )
    if child_allows_vpc_and_non_vpc_instance_memberships is not None:
        out["allows_vpc_and_non_vpc_instance_memberships"] = (
            child_allows_vpc_and_non_vpc_instance_memberships.text or ""
        ).lower() == "true"
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_option_group_arn = el.find("OptionGroupArn")
    if child_option_group_arn is not None:
        out["option_group_arn"] = str(child_option_group_arn.text or "")
    child_source_option_group = el.find("SourceOptionGroup")
    if child_source_option_group is not None:
        out["source_option_group"] = str(child_source_option_group.text or "")
    child_source_account_id = el.find("SourceAccountId")
    if child_source_account_id is not None:
        out["source_account_id"] = str(child_source_account_id.text or "")
    child_copy_timestamp = el.find("CopyTimestamp")
    if child_copy_timestamp is not None:
        import capo_rds.types.t_stamp

        out["copy_timestamp"] = capo_rds.types.t_stamp.deserialize_query(
            child_copy_timestamp
        )
    return out


def redact_sensitive(value: OptionGroup) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "options" in value:
        import capo_rds.types.options_list

        out["options"] = capo_rds.types.options_list.redact_sensitive(value["options"])
    return out
