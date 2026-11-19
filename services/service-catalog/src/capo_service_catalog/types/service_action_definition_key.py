"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ServiceActionDefinitionKey``."""

from typing import Literal, TypeAlias, cast

ServiceActionDefinitionKey: TypeAlias = Literal[
    "Name",
    "Version",
    "AssumeRole",
    "Parameters",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceActionDefinitionKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceActionDefinitionKey:
    return cast(ServiceActionDefinitionKey, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceActionDefinitionKey) -> str:
    return value


def deserialize_cbor(data: str) -> ServiceActionDefinitionKey:
    return cast(ServiceActionDefinitionKey, data)
