"""Generated from Smithy shape ``com.amazonaws.cloudformation#SetTypeConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.third_party_type
    import capo_cloudformation.types.type_arn
    import capo_cloudformation.types.type_configuration
    import capo_cloudformation.types.type_configuration_alias
    import capo_cloudformation.types.type_name


class SetTypeConfigurationInput(TypedDict, closed=True):
    type_arn: NotRequired["capo_cloudformation.types.type_arn.TypeArn"]
    """<p>The Amazon Resource Name (ARN) for the extension in this account and Region.</p> <p>For public extensions, this will be the ARN assigned when you call the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">ActivateType</a> API operation in this account and Region. For private extensions, this will be the ARN assigned when you call the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a> API operation in this account and Region.</p> <p>Do not include the extension versions suffix at the end of the ARN. You can set the configuration for an extension, but not for a specific extension version.</p>"""
    configuration: NotRequired[
        "capo_cloudformation.types.type_configuration.TypeConfiguration"
    ]
    """<p>The configuration data for the extension in this account and Region.</p> <p>The configuration data must be formatted as JSON and validate against the extension's schema returned in the <code>Schema</code> response element of <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>.</p>"""
    configuration_alias: NotRequired[
        "capo_cloudformation.types.type_configuration_alias.TypeConfigurationAlias"
    ]
    """<p>An alias by which to refer to this extension configuration data.</p> <p>Conditional: Specifying a configuration alias is required when setting a configuration for a resource type extension.</p>"""
    type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>The name of the extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>"""
    type: NotRequired["capo_cloudformation.types.third_party_type.ThirdPartyType"]
    """<p>The type of extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetTypeConfigurationInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type_arn" in value:
        pairs.append((f"{key_prefix}TypeArn", str(value["type_arn"])))
    if "configuration" in value:
        pairs.append((f"{key_prefix}Configuration", str(value["configuration"])))
    if "configuration_alias" in value:
        pairs.append(
            (f"{key_prefix}ConfigurationAlias", str(value["configuration_alias"]))
        )
    if "type_name" in value:
        pairs.append((f"{key_prefix}TypeName", str(value["type_name"])))
    if "type" in value:
        import capo_cloudformation.types.third_party_type

        capo_cloudformation.types.third_party_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )


def deserialize_query(el: Element) -> SetTypeConfigurationInput:
    out: SetTypeConfigurationInput = {}  # type: ignore[typeddict-item]
    child_type_arn = el.find("TypeArn")
    if child_type_arn is not None:
        out["type_arn"] = str(child_type_arn.text or "")
    child_configuration = el.find("Configuration")
    if child_configuration is not None:
        out["configuration"] = str(child_configuration.text or "")
    child_configuration_alias = el.find("ConfigurationAlias")
    if child_configuration_alias is not None:
        out["configuration_alias"] = str(child_configuration_alias.text or "")
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudformation.types.third_party_type

        out["type"] = capo_cloudformation.types.third_party_type.deserialize_query(
            child_type
        )
    return out
