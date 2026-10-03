"""Generated from Smithy shape ``com.amazonaws.cloudformation#TypeConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.is_default_configuration
    import capo_cloudformation.types.timestamp
    import capo_cloudformation.types.type_arn
    import capo_cloudformation.types.type_configuration
    import capo_cloudformation.types.type_configuration_alias
    import capo_cloudformation.types.type_configuration_arn
    import capo_cloudformation.types.type_name


class TypeConfigurationDetails(TypedDict, closed=True):
    arn: NotRequired[
        "capo_cloudformation.types.type_configuration_arn.TypeConfigurationArn"
    ]
    """<p>The ARN for the configuration data, in this account and Region.</p>"""
    alias: NotRequired[
        "capo_cloudformation.types.type_configuration_alias.TypeConfigurationAlias"
    ]
    """<p>The alias specified for this configuration, if one was specified when the configuration was set.</p>"""
    configuration: NotRequired[
        "capo_cloudformation.types.type_configuration.TypeConfiguration"
    ]
    """<p>A JSON string specifying the configuration data for the extension, in this account and Region.</p> <p>If a configuration hasn't been set for a specified extension, CloudFormation returns <code>{}</code>.</p>"""
    last_updated: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>When the configuration data was last updated for this extension.</p> <p>If a configuration hasn't been set for a specified extension, CloudFormation returns <code>null</code>.</p>"""
    type_arn: NotRequired["capo_cloudformation.types.type_arn.TypeArn"]
    """<p>The ARN for the extension, in this account and Region.</p> <p>For public extensions, this will be the ARN assigned when you call the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">ActivateType</a> API operation in this account and Region. For private extensions, this will be the ARN assigned when you call the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a> API operation in this account and Region.</p>"""
    type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>The name of the extension.</p>"""
    is_default_configuration: NotRequired[
        "capo_cloudformation.types.is_default_configuration.IsDefaultConfiguration"
    ]
    """<p>Whether this configuration data is the default configuration for the extension.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TypeConfigurationDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "alias" in value:
        pairs.append((f"{key_prefix}Alias", str(value["alias"])))
    if "configuration" in value:
        pairs.append((f"{key_prefix}Configuration", str(value["configuration"])))
    if "last_updated" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["last_updated"], pairs, f"{key_prefix}LastUpdated"
        )
    if "type_arn" in value:
        pairs.append((f"{key_prefix}TypeArn", str(value["type_arn"])))
    if "type_name" in value:
        pairs.append((f"{key_prefix}TypeName", str(value["type_name"])))
    if "is_default_configuration" in value:
        pairs.append(
            (
                f"{key_prefix}IsDefaultConfiguration",
                "true" if value["is_default_configuration"] else "false",
            )
        )


def deserialize_query(el: Element) -> TypeConfigurationDetails:
    out: TypeConfigurationDetails = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_alias = el.find("Alias")
    if child_alias is not None:
        out["alias"] = str(child_alias.text or "")
    child_configuration = el.find("Configuration")
    if child_configuration is not None:
        out["configuration"] = str(child_configuration.text or "")
    child_last_updated = el.find("LastUpdated")
    if child_last_updated is not None:
        import capo_cloudformation.types.timestamp

        out["last_updated"] = capo_cloudformation.types.timestamp.deserialize_query(
            child_last_updated
        )
    child_type_arn = el.find("TypeArn")
    if child_type_arn is not None:
        out["type_arn"] = str(child_type_arn.text or "")
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_is_default_configuration = el.find("IsDefaultConfiguration")
    if child_is_default_configuration is not None:
        out["is_default_configuration"] = (
            child_is_default_configuration.text or ""
        ).lower() == "true"
    return out
