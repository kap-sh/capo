"""Generated from Smithy shape ``com.amazonaws.cloudformation#TypeConfigurationIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.third_party_type
    import capo_cloudformation.types.type_arn
    import capo_cloudformation.types.type_configuration_alias
    import capo_cloudformation.types.type_configuration_arn
    import capo_cloudformation.types.type_name


class TypeConfigurationIdentifier(TypedDict, closed=True):
    type_arn: NotRequired["capo_cloudformation.types.type_arn.TypeArn"]
    """<p>The ARN for the extension, in this account and Region.</p> <p>For public extensions, this will be the ARN assigned when you call the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">ActivateType</a> API operation in this account and Region. For private extensions, this will be the ARN assigned when you call the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a> API operation in this account and Region.</p>"""
    type_configuration_alias: NotRequired[
        "capo_cloudformation.types.type_configuration_alias.TypeConfigurationAlias"
    ]
    """<p>The alias specified for this configuration, if one was specified when the configuration was set.</p>"""
    type_configuration_arn: NotRequired[
        "capo_cloudformation.types.type_configuration_arn.TypeConfigurationArn"
    ]
    """<p>The ARN for the configuration, in this account and Region.</p>"""
    type: NotRequired["capo_cloudformation.types.third_party_type.ThirdPartyType"]
    """<p>The type of extension.</p>"""
    type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>The name of the extension type to which this configuration applies.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TypeConfigurationIdentifier, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type_arn" in value:
        pairs.append((f"{key_prefix}TypeArn", str(value["type_arn"])))
    if "type_configuration_alias" in value:
        pairs.append(
            (
                f"{key_prefix}TypeConfigurationAlias",
                str(value["type_configuration_alias"]),
            )
        )
    if "type_configuration_arn" in value:
        pairs.append(
            (f"{key_prefix}TypeConfigurationArn", str(value["type_configuration_arn"]))
        )
    if "type" in value:
        import capo_cloudformation.types.third_party_type

        capo_cloudformation.types.third_party_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "type_name" in value:
        pairs.append((f"{key_prefix}TypeName", str(value["type_name"])))


def deserialize_query(el: Element) -> TypeConfigurationIdentifier:
    out: TypeConfigurationIdentifier = {}  # type: ignore[typeddict-item]
    child_type_arn = el.find("TypeArn")
    if child_type_arn is not None:
        out["type_arn"] = str(child_type_arn.text or "")
    child_type_configuration_alias = el.find("TypeConfigurationAlias")
    if child_type_configuration_alias is not None:
        out["type_configuration_alias"] = str(child_type_configuration_alias.text or "")
    child_type_configuration_arn = el.find("TypeConfigurationArn")
    if child_type_configuration_arn is not None:
        out["type_configuration_arn"] = str(child_type_configuration_arn.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudformation.types.third_party_type

        out["type"] = capo_cloudformation.types.third_party_type.deserialize_query(
            child_type
        )
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    return out
