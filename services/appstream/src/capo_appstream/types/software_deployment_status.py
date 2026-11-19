"""Generated from Smithy shape ``com.amazonaws.appstream#SoftwareDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

SoftwareDeploymentStatus: TypeAlias = Literal[
    "STAGED_FOR_INSTALLATION",
    "PENDING_INSTALLATION",
    "INSTALLED",
    "STAGED_FOR_UNINSTALLATION",
    "PENDING_UNINSTALLATION",
    "FAILED_TO_INSTALL",
    "FAILED_TO_UNINSTALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SoftwareDeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SoftwareDeploymentStatus:
    return cast(SoftwareDeploymentStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SoftwareDeploymentStatus) -> str:
    return value


def deserialize_cbor(data: str) -> SoftwareDeploymentStatus:
    return cast(SoftwareDeploymentStatus, data)
