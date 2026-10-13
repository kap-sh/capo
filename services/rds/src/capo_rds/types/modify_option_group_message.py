"""Generated from Smithy shape ``com.amazonaws.rds#ModifyOptionGroupMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.option_configuration_list
    import capo_rds.types.option_names_list
    import capo_rds.types.string


class ModifyOptionGroupMessage(TypedDict, closed=True):
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the option group to be modified.</p> <p>Permanent options, such as the TDE option for Oracle Advanced Security TDE, can't be removed from an option group, and that option group can't be removed from a DB instance once it is associated with a DB instance</p>"""
    options_to_include: NotRequired[
        "capo_rds.types.option_configuration_list.OptionConfigurationList"
    ]
    """<p>Options in this list are added to the option group or, if already present, the specified configuration is used to update the existing configuration.</p>"""
    options_to_remove: NotRequired["capo_rds.types.option_names_list.OptionNamesList"]
    """<p>Options in this list are removed from the option group.</p>"""
    apply_immediately: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether to apply the change immediately or during the next maintenance window for each instance associated with the option group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyOptionGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "option_group_name" in value:
        pairs.append((f"{key_prefix}OptionGroupName", str(value["option_group_name"])))
    if "options_to_include" in value:
        import capo_rds.types.option_configuration_list

        capo_rds.types.option_configuration_list.serialize_query(
            value["options_to_include"], pairs, f"{key_prefix}OptionsToInclude"
        )
    if "options_to_remove" in value:
        import capo_rds.types.option_names_list

        capo_rds.types.option_names_list.serialize_query(
            value["options_to_remove"], pairs, f"{key_prefix}OptionsToRemove"
        )
    if "apply_immediately" in value:
        pairs.append(
            (
                f"{key_prefix}ApplyImmediately",
                "true" if value["apply_immediately"] else "false",
            )
        )


def deserialize_query(el: Element) -> ModifyOptionGroupMessage:
    out: ModifyOptionGroupMessage = {}  # type: ignore[typeddict-item]
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    child_options_to_include = el.find("OptionsToInclude")
    if child_options_to_include is not None:
        import capo_rds.types.option_configuration_list

        out["options_to_include"] = (
            capo_rds.types.option_configuration_list.deserialize_query(
                child_options_to_include
            )
        )
    child_options_to_remove = el.find("OptionsToRemove")
    if child_options_to_remove is not None:
        import capo_rds.types.option_names_list

        out["options_to_remove"] = capo_rds.types.option_names_list.deserialize_query(
            child_options_to_remove
        )
    child_apply_immediately = el.find("ApplyImmediately")
    if child_apply_immediately is not None:
        out["apply_immediately"] = (
            child_apply_immediately.text or ""
        ).lower() == "true"
    return out


def redact_sensitive(value: ModifyOptionGroupMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "options_to_include" in value:
        import capo_rds.types.option_configuration_list

        out["options_to_include"] = (
            capo_rds.types.option_configuration_list.redact_sensitive(
                value["options_to_include"]
            )
        )
    return out
