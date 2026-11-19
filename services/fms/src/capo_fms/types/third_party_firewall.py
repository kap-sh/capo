"""Generated from Smithy shape ``com.amazonaws.fms#ThirdPartyFirewall``."""

from typing import Literal, TypeAlias, cast

ThirdPartyFirewall: TypeAlias = Literal[
    "PALO_ALTO_NETWORKS_CLOUD_NGFW",
    "FORTIGATE_CLOUD_NATIVE_FIREWALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThirdPartyFirewall) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThirdPartyFirewall:
    return cast(ThirdPartyFirewall, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThirdPartyFirewall) -> str:
    return value


def deserialize_cbor(data: str) -> ThirdPartyFirewall:
    return cast(ThirdPartyFirewall, data)
