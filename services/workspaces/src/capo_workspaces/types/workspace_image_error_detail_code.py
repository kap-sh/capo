"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceImageErrorDetailCode``."""

from typing import Literal, TypeAlias, cast

WorkspaceImageErrorDetailCode: TypeAlias = Literal[
    "OutdatedPowershellVersion",
    "OfficeInstalled",
    "PCoIPAgentInstalled",
    "WindowsUpdatesEnabled",
    "AutoMountDisabled",
    "WorkspacesBYOLAccountNotFound",
    "WorkspacesBYOLAccountDisabled",
    "DHCPDisabled",
    "DiskFreeSpace",
    "AdditionalDrivesAttached",
    "OSNotSupported",
    "DomainJoined",
    "AzureDomainJoined",
    "FirewallEnabled",
    "VMWareToolsInstalled",
    "DiskSizeExceeded",
    "IncompatiblePartitioning",
    "PendingReboot",
    "AutoLogonEnabled",
    "RealTimeUniversalDisabled",
    "MultipleBootPartition",
    "Requires64BitOS",
    "ZeroRearmCount",
    "InPlaceUpgrade",
    "AntiVirusInstalled",
    "UEFINotSupported",
    "UnknownError",
    "AppXPackagesInstalled",
    "ReservedStorageInUse",
    "AdditionalDrivesPresent",
    "WindowsUpdatesRequired",
    "SysPrepFileMissing",
    "UserProfileMissing",
    "InsufficientDiskSpace",
    "EnvironmentVariablesPathMissingEntries",
    "DomainAccountServicesFound",
    "InvalidIp",
    "RemoteDesktopServicesDisabled",
    "WindowsModulesInstallerDisabled",
    "AmazonSsmAgentEnabled",
    "UnsupportedSecurityProtocol",
    "MultipleUserProfiles",
    "StagedAppxPackage",
    "UnsupportedOsUpgrade",
    "InsufficientRearmCount",
    "ProtocolOSIncompatibility",
    "MemoryIntegrityIncompatibility",
    "RestrictedDriveLetterInUse",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceImageErrorDetailCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceImageErrorDetailCode:
    return cast(WorkspaceImageErrorDetailCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceImageErrorDetailCode) -> str:
    return value


def deserialize_cbor(data: str) -> WorkspaceImageErrorDetailCode:
    return cast(WorkspaceImageErrorDetailCode, data)
