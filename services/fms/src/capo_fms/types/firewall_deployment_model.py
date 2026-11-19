"""Generated from Smithy shape ``com.amazonaws.fms#FirewallDeploymentModel``."""

from typing import Literal, TypeAlias, cast

FirewallDeploymentModel: TypeAlias = Literal[
    "CENTRALIZED",
    "DISTRIBUTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallDeploymentModel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallDeploymentModel:
    return cast(FirewallDeploymentModel, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FirewallDeploymentModel) -> str:
    return value


def deserialize_cbor(data: str) -> FirewallDeploymentModel:
    return cast(FirewallDeploymentModel, data)
