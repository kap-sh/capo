"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionTypeProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.action_type_property

ActionTypeProperties: TypeAlias = list[
    "capo_codepipeline.types.action_type_property.ActionTypeProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionTypeProperties) -> list:
    import capo_codepipeline.types.action_type_property

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.action_type_property.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ActionTypeProperties:
    import capo_codepipeline.types.action_type_property

    out: ActionTypeProperties = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.action_type_property.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionTypeProperties) -> list:
    import capo_codepipeline.types.action_type_property

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.action_type_property.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ActionTypeProperties:
    import capo_codepipeline.types.action_type_property

    out: ActionTypeProperties = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.action_type_property.deserialize_cbor(item))
    return out
