"""Generated from Smithy shape ``com.amazonaws.workspaces#AssociationState``."""

from typing import Literal, TypeAlias, cast

AssociationState: TypeAlias = Literal[
    "PENDING_INSTALL",
    "PENDING_INSTALL_DEPLOYMENT",
    "PENDING_UNINSTALL",
    "PENDING_UNINSTALL_DEPLOYMENT",
    "INSTALLING",
    "UNINSTALLING",
    "ERROR",
    "COMPLETED",
    "REMOVED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationState:
    return cast(AssociationState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociationState) -> str:
    return value


def deserialize_cbor(data: str) -> AssociationState:
    return cast(AssociationState, data)
