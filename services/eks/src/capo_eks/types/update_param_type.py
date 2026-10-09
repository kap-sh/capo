"""Generated from Smithy shape ``com.amazonaws.eks#UpdateParamType``."""

from typing import Literal, TypeAlias, cast

UpdateParamType: TypeAlias = Literal[
    "Version",
    "PlatformVersion",
    "EndpointPrivateAccess",
    "EndpointPublicAccess",
    "ClusterLogging",
    "DesiredSize",
    "LabelsToAdd",
    "LabelsToRemove",
    "TaintsToAdd",
    "TaintsToRemove",
    "MaxSize",
    "MinSize",
    "ReleaseVersion",
    "PublicAccessCidrs",
    "LaunchTemplateName",
    "LaunchTemplateVersion",
    "IdentityProviderConfig",
    "EncryptionConfig",
    "AddonVersion",
    "ServiceAccountRoleArn",
    "ResolveConflicts",
    "MaxUnavailable",
    "MaxUnavailablePercentage",
    "NodeRepairEnabled",
    "UpdateStrategy",
    "ConfigurationValues",
    "SecurityGroups",
    "Subnets",
    "AuthenticationMode",
    "PodIdentityAssociations",
    "UpgradePolicy",
    "ZonalShiftConfig",
    "ComputeConfig",
    "StorageConfig",
    "KubernetesNetworkConfig",
    "RemoteNetworkConfig",
    "DeletionProtection",
    "NodeRepairConfig",
    "RoleArn",
    "RoleMappingsToAddOrUpdate",
    "RoleMappingsToRemove",
    "NetworkAccess",
    "VendedLogs",
    "UpdatedTier",
    "PreviousTier",
    "EnableCrossNamespace",
    "DisabledServices",
    "WarmPoolEnabled",
    "WarmPoolMaxGroupPreparedCapacity",
    "WarmPoolMinSize",
    "WarmPoolState",
    "WarmPoolReuseOnScaleIn",
    "ControlPlaneEgressMode",
    "KubeApiServerConfig",
    "KubeSchedulerConfig",
    "KubeControllerManagerConfig",
    "ActiveCertificateAuthority",
    "TrustedCertificateAuthorities",
    "CertificateAuthorityId",
    "SigningStatus",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateParamType) -> str:
    return value


def deserialize_json(data: str) -> UpdateParamType:
    return cast(UpdateParamType, data)
