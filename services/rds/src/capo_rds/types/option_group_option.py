"""Generated from Smithy shape ``com.amazonaws.rds#OptionGroupOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.boolean_optional
    import capo_rds.types.integer_optional
    import capo_rds.types.option_group_option_settings_list
    import capo_rds.types.option_group_option_versions_list
    import capo_rds.types.options_conflicts_with
    import capo_rds.types.options_depended_on
    import capo_rds.types.string


class OptionGroupOption(TypedDict, closed=True):
    name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the option.</p>"""
    description: NotRequired["capo_rds.types.string.String"]
    """<p>The description of the option.</p>"""
    engine_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the engine that this option can be applied to.</p>"""
    major_engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>Indicates the major engine version that the option is available for.</p>"""
    minimum_required_minor_engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The minimum required engine version for the option to be applied.</p>"""
    port_required: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the option requires a port.</p>"""
    default_port: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>If the option requires a port, specifies the default port for the option.</p>"""
    options_depended_on: NotRequired[
        "capo_rds.types.options_depended_on.OptionsDependedOn"
    ]
    """<p>The options that are prerequisites for this option.</p>"""
    options_conflicts_with: NotRequired[
        "capo_rds.types.options_conflicts_with.OptionsConflictsWith"
    ]
    """<p>The options that conflict with this option.</p>"""
    persistent: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Persistent options can't be removed from an option group while DB instances are associated with the option group. If you disassociate all DB instances from the option group, your can remove the persistent option from the option group.</p>"""
    permanent: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Permanent options can never be removed from an option group. An option group containing a permanent option can't be removed from a DB instance.</p>"""
    requires_auto_minor_engine_version_upgrade: NotRequired[
        "capo_rds.types.boolean.Boolean"
    ]
    """<p>If true, you must enable the Auto Minor Version Upgrade setting for your DB instance before you can use this option. You can enable Auto Minor Version Upgrade when you first create your DB instance, or by modifying your DB instance later.</p>"""
    vpc_only: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>If true, you can only use this option with a DB instance that is in a VPC.</p>"""
    supports_option_version_downgrade: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>If true, you can change the option to an earlier version of the option. This only applies to options that have different versions available.</p>"""
    option_group_option_settings: NotRequired[
        "capo_rds.types.option_group_option_settings_list.OptionGroupOptionSettingsList"
    ]
    """<p>The option settings that are available (and the default value) for each option in an option group.</p>"""
    option_group_option_versions: NotRequired[
        "capo_rds.types.option_group_option_versions_list.OptionGroupOptionVersionsList"
    ]
    """<p>The versions that are available for the option.</p>"""
    copyable_cross_account: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the option can be copied across Amazon Web Services accounts.</p>"""
    copyable_cross_region: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the option can be copied across Amazon Web Services Regions.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionGroupOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "engine_name" in value:
        pairs.append((f"{key_prefix}EngineName", str(value["engine_name"])))
    if "major_engine_version" in value:
        pairs.append(
            (f"{key_prefix}MajorEngineVersion", str(value["major_engine_version"]))
        )
    if "minimum_required_minor_engine_version" in value:
        pairs.append(
            (
                f"{key_prefix}MinimumRequiredMinorEngineVersion",
                str(value["minimum_required_minor_engine_version"]),
            )
        )
    if "port_required" in value:
        pairs.append(
            (f"{key_prefix}PortRequired", "true" if value["port_required"] else "false")
        )
    if "default_port" in value:
        pairs.append((f"{key_prefix}DefaultPort", str(value["default_port"])))
    if "options_depended_on" in value:
        import capo_rds.types.options_depended_on

        capo_rds.types.options_depended_on.serialize_query(
            value["options_depended_on"], pairs, f"{key_prefix}OptionsDependedOn"
        )
    if "options_conflicts_with" in value:
        import capo_rds.types.options_conflicts_with

        capo_rds.types.options_conflicts_with.serialize_query(
            value["options_conflicts_with"], pairs, f"{key_prefix}OptionsConflictsWith"
        )
    if "persistent" in value:
        pairs.append(
            (f"{key_prefix}Persistent", "true" if value["persistent"] else "false")
        )
    if "permanent" in value:
        pairs.append(
            (f"{key_prefix}Permanent", "true" if value["permanent"] else "false")
        )
    if "requires_auto_minor_engine_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}RequiresAutoMinorEngineVersionUpgrade",
                "true"
                if value["requires_auto_minor_engine_version_upgrade"]
                else "false",
            )
        )
    if "vpc_only" in value:
        pairs.append((f"{key_prefix}VpcOnly", "true" if value["vpc_only"] else "false"))
    if "supports_option_version_downgrade" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsOptionVersionDowngrade",
                "true" if value["supports_option_version_downgrade"] else "false",
            )
        )
    if "option_group_option_settings" in value:
        import capo_rds.types.option_group_option_settings_list

        capo_rds.types.option_group_option_settings_list.serialize_query(
            value["option_group_option_settings"],
            pairs,
            f"{key_prefix}OptionGroupOptionSettings",
        )
    if "option_group_option_versions" in value:
        import capo_rds.types.option_group_option_versions_list

        capo_rds.types.option_group_option_versions_list.serialize_query(
            value["option_group_option_versions"],
            pairs,
            f"{key_prefix}OptionGroupOptionVersions",
        )
    if "copyable_cross_account" in value:
        pairs.append(
            (
                f"{key_prefix}CopyableCrossAccount",
                "true" if value["copyable_cross_account"] else "false",
            )
        )
    if "copyable_cross_region" in value:
        pairs.append(
            (
                f"{key_prefix}CopyableCrossRegion",
                "true" if value["copyable_cross_region"] else "false",
            )
        )


def deserialize_query(el: Element) -> OptionGroupOption:
    out: OptionGroupOption = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_engine_name = el.find("EngineName")
    if child_engine_name is not None:
        out["engine_name"] = str(child_engine_name.text or "")
    child_major_engine_version = el.find("MajorEngineVersion")
    if child_major_engine_version is not None:
        out["major_engine_version"] = str(child_major_engine_version.text or "")
    child_minimum_required_minor_engine_version = el.find(
        "MinimumRequiredMinorEngineVersion"
    )
    if child_minimum_required_minor_engine_version is not None:
        out["minimum_required_minor_engine_version"] = str(
            child_minimum_required_minor_engine_version.text or ""
        )
    child_port_required = el.find("PortRequired")
    if child_port_required is not None:
        out["port_required"] = (child_port_required.text or "").lower() == "true"
    child_default_port = el.find("DefaultPort")
    if child_default_port is not None:
        out["default_port"] = int(child_default_port.text or "")
    child_options_depended_on = el.find("OptionsDependedOn")
    if child_options_depended_on is not None:
        import capo_rds.types.options_depended_on

        out["options_depended_on"] = (
            capo_rds.types.options_depended_on.deserialize_query(
                child_options_depended_on
            )
        )
    child_options_conflicts_with = el.find("OptionsConflictsWith")
    if child_options_conflicts_with is not None:
        import capo_rds.types.options_conflicts_with

        out["options_conflicts_with"] = (
            capo_rds.types.options_conflicts_with.deserialize_query(
                child_options_conflicts_with
            )
        )
    child_persistent = el.find("Persistent")
    if child_persistent is not None:
        out["persistent"] = (child_persistent.text or "").lower() == "true"
    child_permanent = el.find("Permanent")
    if child_permanent is not None:
        out["permanent"] = (child_permanent.text or "").lower() == "true"
    child_requires_auto_minor_engine_version_upgrade = el.find(
        "RequiresAutoMinorEngineVersionUpgrade"
    )
    if child_requires_auto_minor_engine_version_upgrade is not None:
        out["requires_auto_minor_engine_version_upgrade"] = (
            child_requires_auto_minor_engine_version_upgrade.text or ""
        ).lower() == "true"
    child_vpc_only = el.find("VpcOnly")
    if child_vpc_only is not None:
        out["vpc_only"] = (child_vpc_only.text or "").lower() == "true"
    child_supports_option_version_downgrade = el.find("SupportsOptionVersionDowngrade")
    if child_supports_option_version_downgrade is not None:
        out["supports_option_version_downgrade"] = (
            child_supports_option_version_downgrade.text or ""
        ).lower() == "true"
    child_option_group_option_settings = el.find("OptionGroupOptionSettings")
    if child_option_group_option_settings is not None:
        import capo_rds.types.option_group_option_settings_list

        out["option_group_option_settings"] = (
            capo_rds.types.option_group_option_settings_list.deserialize_query(
                child_option_group_option_settings
            )
        )
    child_option_group_option_versions = el.find("OptionGroupOptionVersions")
    if child_option_group_option_versions is not None:
        import capo_rds.types.option_group_option_versions_list

        out["option_group_option_versions"] = (
            capo_rds.types.option_group_option_versions_list.deserialize_query(
                child_option_group_option_versions
            )
        )
    child_copyable_cross_account = el.find("CopyableCrossAccount")
    if child_copyable_cross_account is not None:
        out["copyable_cross_account"] = (
            child_copyable_cross_account.text or ""
        ).lower() == "true"
    child_copyable_cross_region = el.find("CopyableCrossRegion")
    if child_copyable_cross_region is not None:
        out["copyable_cross_region"] = (
            child_copyable_cross_region.text or ""
        ).lower() == "true"
    return out
