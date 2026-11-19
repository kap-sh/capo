"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionConfigurationPropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.action_configuration_property

ActionConfigurationPropertyList: TypeAlias = list[
    "capo_codepipeline.types.action_configuration_property.ActionConfigurationProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionConfigurationPropertyList) -> list:
    import capo_codepipeline.types.action_configuration_property

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.action_configuration_property.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ActionConfigurationPropertyList:
    import capo_codepipeline.types.action_configuration_property

    out: ActionConfigurationPropertyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.action_configuration_property.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionConfigurationPropertyList) -> list:
    import capo_codepipeline.types.action_configuration_property

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.action_configuration_property.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ActionConfigurationPropertyList:
    import capo_codepipeline.types.action_configuration_property

    out: ActionConfigurationPropertyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.action_configuration_property.deserialize_cbor(item)
        )
    return out
