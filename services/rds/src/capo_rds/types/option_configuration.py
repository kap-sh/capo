"""Generated from Smithy shape ``com.amazonaws.rds#OptionConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_security_group_name_list
    import capo_rds.types.integer_optional
    import capo_rds.types.option_settings_list
    import capo_rds.types.string
    import capo_rds.types.vpc_security_group_id_list


class OptionConfiguration(TypedDict, closed=True):
    option_name: NotRequired["capo_rds.types.string.String"]
    """<p>The configuration of options to include in a group.</p>"""
    port: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The optional port for the option.</p>"""
    option_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version for the option.</p>"""
    db_security_group_memberships: NotRequired[
        "capo_rds.types.db_security_group_name_list.DBSecurityGroupNameList"
    ]
    """<p>A list of DB security groups used for this option.</p>"""
    vpc_security_group_memberships: NotRequired[
        "capo_rds.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of VPC security group names used for this option.</p>"""
    option_settings: NotRequired[
        "capo_rds.types.option_settings_list.OptionSettingsList"
    ]
    """<p>The option settings to include in an option group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "option_name" in value:
        pairs.append((f"{key_prefix}OptionName", str(value["option_name"])))
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "option_version" in value:
        pairs.append((f"{key_prefix}OptionVersion", str(value["option_version"])))
    if "db_security_group_memberships" in value:
        import capo_rds.types.db_security_group_name_list

        capo_rds.types.db_security_group_name_list.serialize_query(
            value["db_security_group_memberships"],
            pairs,
            f"{key_prefix}DBSecurityGroupMemberships",
        )
    if "vpc_security_group_memberships" in value:
        import capo_rds.types.vpc_security_group_id_list

        capo_rds.types.vpc_security_group_id_list.serialize_query(
            value["vpc_security_group_memberships"],
            pairs,
            f"{key_prefix}VpcSecurityGroupMemberships",
        )
    if "option_settings" in value:
        import capo_rds.types.option_settings_list

        capo_rds.types.option_settings_list.serialize_query(
            value["option_settings"], pairs, f"{key_prefix}OptionSettings"
        )


def deserialize_query(el: Element) -> OptionConfiguration:
    out: OptionConfiguration = {}  # type: ignore[typeddict-item]
    child_option_name = el.find("OptionName")
    if child_option_name is not None:
        out["option_name"] = str(child_option_name.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_option_version = el.find("OptionVersion")
    if child_option_version is not None:
        out["option_version"] = str(child_option_version.text or "")
    child_db_security_group_memberships = el.find("DBSecurityGroupMemberships")
    if child_db_security_group_memberships is not None:
        import capo_rds.types.db_security_group_name_list

        out["db_security_group_memberships"] = (
            capo_rds.types.db_security_group_name_list.deserialize_query(
                child_db_security_group_memberships
            )
        )
    child_vpc_security_group_memberships = el.find("VpcSecurityGroupMemberships")
    if child_vpc_security_group_memberships is not None:
        import capo_rds.types.vpc_security_group_id_list

        out["vpc_security_group_memberships"] = (
            capo_rds.types.vpc_security_group_id_list.deserialize_query(
                child_vpc_security_group_memberships
            )
        )
    child_option_settings = el.find("OptionSettings")
    if child_option_settings is not None:
        import capo_rds.types.option_settings_list

        out["option_settings"] = capo_rds.types.option_settings_list.deserialize_query(
            child_option_settings
        )
    return out


def redact_sensitive(value: OptionConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "option_settings" in value:
        import capo_rds.types.option_settings_list

        out["option_settings"] = capo_rds.types.option_settings_list.redact_sensitive(
            value["option_settings"]
        )
    return out
