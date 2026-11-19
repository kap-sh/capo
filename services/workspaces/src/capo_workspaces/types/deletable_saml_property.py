"""Generated from Smithy shape ``com.amazonaws.workspaces#DeletableSamlProperty``."""

from typing import Literal, TypeAlias, cast

DeletableSamlProperty: TypeAlias = Literal[
    "SAML_PROPERTIES_USER_ACCESS_URL",
    "SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletableSamlProperty) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeletableSamlProperty:
    return cast(DeletableSamlProperty, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeletableSamlProperty) -> str:
    return value


def deserialize_cbor(data: str) -> DeletableSamlProperty:
    return cast(DeletableSamlProperty, data)
