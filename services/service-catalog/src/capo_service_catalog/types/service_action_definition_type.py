"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ServiceActionDefinitionType``."""

from typing import Literal, TypeAlias, cast

ServiceActionDefinitionType: TypeAlias = Literal["SSM_AUTOMATION",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceActionDefinitionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceActionDefinitionType:
    return cast(ServiceActionDefinitionType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceActionDefinitionType) -> str:
    return value


def deserialize_cbor(data: str) -> ServiceActionDefinitionType:
    return cast(ServiceActionDefinitionType, data)
