"""Generated from Smithy shape ``com.amazonaws.marketplaceentitlementservice#GetEntitlementFilterName``."""

from typing import Literal, TypeAlias, cast

GetEntitlementFilterName: TypeAlias = Literal[
    "CUSTOMER_IDENTIFIER",
    "DIMENSION",
    "CUSTOMER_AWS_ACCOUNT_ID",
    "LICENSE_ARN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEntitlementFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GetEntitlementFilterName:
    return cast(GetEntitlementFilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetEntitlementFilterName) -> str:
    return value


def deserialize_cbor(data: str) -> GetEntitlementFilterName:
    return cast(GetEntitlementFilterName, data)
