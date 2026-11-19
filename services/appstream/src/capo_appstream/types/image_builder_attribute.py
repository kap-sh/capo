"""Generated from Smithy shape ``com.amazonaws.appstream#ImageBuilderAttribute``."""

from typing import Literal, TypeAlias, cast

"""<p>An image builder attribute that you can delete by using the AttributesToDelete parameter of UpdateImageBuilder.</p> <ul> <li> <p>AGENT_ACCESS_CONFIG - Removes the stored agent access configuration from the image builder.</p> </li> </ul>"""
ImageBuilderAttribute: TypeAlias = Literal["AGENT_ACCESS_CONFIG",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageBuilderAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageBuilderAttribute:
    return cast(ImageBuilderAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageBuilderAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> ImageBuilderAttribute:
    return cast(ImageBuilderAttribute, data)
