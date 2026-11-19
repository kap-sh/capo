"""Generated from Smithy shape ``com.amazonaws.lambda#StateReasonCode``."""

from typing import Literal, TypeAlias, cast

StateReasonCode: TypeAlias = Literal[
    "Idle",
    "Creating",
    "Restoring",
    "EniLimitExceeded",
    "InsufficientRolePermissions",
    "InvalidConfiguration",
    "InternalError",
    "SubnetOutOfIPAddresses",
    "InvalidSubnet",
    "InvalidSecurityGroup",
    "ImageDeleted",
    "ImageAccessDenied",
    "InvalidImage",
    "KMSKeyAccessDenied",
    "KMSKeyNotFound",
    "InvalidStateKMSKey",
    "DisabledKMSKey",
    "EFSIOError",
    "EFSMountConnectivityError",
    "EFSMountFailure",
    "EFSMountTimeout",
    "InvalidRuntime",
    "InvalidZipFileException",
    "FunctionError",
    "ServiceQuotaExceededException",
    "VcpuLimitExceeded",
    "CapacityProviderScalingLimitExceeded",
    "InsufficientCapacity",
    "EC2RequestLimitExceeded",
    "FunctionError.InitTimeout",
    "FunctionError.RuntimeInitError",
    "FunctionError.ExtensionInitError",
    "FunctionError.InvalidEntryPoint",
    "FunctionError.InvalidWorkingDirectory",
    "FunctionError.PermissionDenied",
    "FunctionError.TooManyExtensions",
    "FunctionError.InitResourceExhausted",
    "DisallowedByVpcEncryptionControl",
    "DrainingDurableExecutions",
    "IncompatibleAcceleratorInstanceTypes",
    "DependencyError",
]


# --- restJson1 ser/de ---
def serialize_json(value: StateReasonCode) -> str:
    return value


def deserialize_json(data: str) -> StateReasonCode:
    return cast(StateReasonCode, data)
