"""Generated from Smithy shape ``com.amazonaws.rds#Option``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.db_security_group_membership_list
    import capo_rds.types.integer_optional
    import capo_rds.types.option_setting_configuration_list
    import capo_rds.types.string
    import capo_rds.types.vpc_security_group_membership_list


class Option(TypedDict, closed=True):
    option_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the option.</p>"""
    option_description: NotRequired["capo_rds.types.string.String"]
    """<p>The description of the option.</p>"""
    persistent: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether this option is persistent.</p>"""
    permanent: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether this option is permanent.</p>"""
    port: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>If required, the port configured for this option to use.</p>"""
    option_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version of the option.</p>"""
    option_settings: NotRequired[
        "capo_rds.types.option_setting_configuration_list.OptionSettingConfigurationList"
    ]
    """<p>The option settings for this option.</p>"""
    db_security_group_memberships: NotRequired[
        "capo_rds.types.db_security_group_membership_list.DBSecurityGroupMembershipList"
    ]
    """<p>If the option requires access to a port, then this DB security group allows access to the port.</p>"""
    vpc_security_group_memberships: NotRequired[
        "capo_rds.types.vpc_security_group_membership_list.VpcSecurityGroupMembershipList"
    ]
    """<p>If the option requires access to a port, then this VPC security group allows access to the port.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Option, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "option_name" in value:
        pairs.append((f"{key_prefix}OptionName", str(value["option_name"])))
    if "option_description" in value:
        pairs.append(
            (f"{key_prefix}OptionDescription", str(value["option_description"]))
        )
    if "persistent" in value:
        pairs.append(
            (f"{key_prefix}Persistent", "true" if value["persistent"] else "false")
        )
    if "permanent" in value:
        pairs.append(
            (f"{key_prefix}Permanent", "true" if value["permanent"] else "false")
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "option_version" in value:
        pairs.append((f"{key_prefix}OptionVersion", str(value["option_version"])))
    if "option_settings" in value:
        import capo_rds.types.option_setting_configuration_list

        capo_rds.types.option_setting_configuration_list.serialize_query(
            value["option_settings"], pairs, f"{key_prefix}OptionSettings"
        )
    if "db_security_group_memberships" in value:
        import capo_rds.types.db_security_group_membership_list

        capo_rds.types.db_security_group_membership_list.serialize_query(
            value["db_security_group_memberships"],
            pairs,
            f"{key_prefix}DBSecurityGroupMemberships",
        )
    if "vpc_security_group_memberships" in value:
        import capo_rds.types.vpc_security_group_membership_list

        capo_rds.types.vpc_security_group_membership_list.serialize_query(
            value["vpc_security_group_memberships"],
            pairs,
            f"{key_prefix}VpcSecurityGroupMemberships",
        )


def deserialize_query(el: Element) -> Option:
    out: Option = {}  # type: ignore[typeddict-item]
    child_option_name = el.find("OptionName")
    if child_option_name is not None:
        out["option_name"] = str(child_option_name.text or "")
    child_option_description = el.find("OptionDescription")
    if child_option_description is not None:
        out["option_description"] = str(child_option_description.text or "")
    child_persistent = el.find("Persistent")
    if child_persistent is not None:
        out["persistent"] = (child_persistent.text or "").lower() == "true"
    child_permanent = el.find("Permanent")
    if child_permanent is not None:
        out["permanent"] = (child_permanent.text or "").lower() == "true"
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_option_version = el.find("OptionVersion")
    if child_option_version is not None:
        out["option_version"] = str(child_option_version.text or "")
    child_option_settings = el.find("OptionSettings")
    if child_option_settings is not None:
        import capo_rds.types.option_setting_configuration_list

        out["option_settings"] = (
            capo_rds.types.option_setting_configuration_list.deserialize_query(
                child_option_settings
            )
        )
    child_db_security_group_memberships = el.find("DBSecurityGroupMemberships")
    if child_db_security_group_memberships is not None:
        import capo_rds.types.db_security_group_membership_list

        out["db_security_group_memberships"] = (
            capo_rds.types.db_security_group_membership_list.deserialize_query(
                child_db_security_group_memberships
            )
        )
    child_vpc_security_group_memberships = el.find("VpcSecurityGroupMemberships")
    if child_vpc_security_group_memberships is not None:
        import capo_rds.types.vpc_security_group_membership_list

        out["vpc_security_group_memberships"] = (
            capo_rds.types.vpc_security_group_membership_list.deserialize_query(
                child_vpc_security_group_memberships
            )
        )
    return out


def redact_sensitive(value: Option) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "option_settings" in value:
        import capo_rds.types.option_setting_configuration_list

        out["option_settings"] = (
            capo_rds.types.option_setting_configuration_list.redact_sensitive(
                value["option_settings"]
            )
        )
    return out
