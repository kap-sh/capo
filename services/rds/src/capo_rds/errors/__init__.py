from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    RDSError as RDSError,
)
from ._base import (
    SerializationError as SerializationError,
)
from ._base import (
    ServiceError as ServiceError,
)
from ._base import (
    UnknownServiceError as UnknownServiceError,
)
from ._base import (
    WaiterFailedError as WaiterFailedError,
)
from ._base import (
    WaiterTimeoutError as WaiterTimeoutError,
)
from .authorization_already_exists_fault import (
    AuthorizationAlreadyExistsFault as AuthorizationAlreadyExistsFault,
)
from .authorization_not_found_fault import (
    AuthorizationNotFoundFault as AuthorizationNotFoundFault,
)
from .authorization_quota_exceeded_fault import (
    AuthorizationQuotaExceededFault as AuthorizationQuotaExceededFault,
)
from .backup_policy_not_found_fault import (
    BackupPolicyNotFoundFault as BackupPolicyNotFoundFault,
)
from .blue_green_deployment_already_exists_fault import (
    BlueGreenDeploymentAlreadyExistsFault as BlueGreenDeploymentAlreadyExistsFault,
)
from .blue_green_deployment_not_found_fault import (
    BlueGreenDeploymentNotFoundFault as BlueGreenDeploymentNotFoundFault,
)
from .certificate_not_found_fault import (
    CertificateNotFoundFault as CertificateNotFoundFault,
)
from .create_custom_db_engine_version_fault import (
    CreateCustomDBEngineVersionFault as CreateCustomDBEngineVersionFault,
)
from .custom_availability_zone_not_found_fault import (
    CustomAvailabilityZoneNotFoundFault as CustomAvailabilityZoneNotFoundFault,
)
from .custom_db_engine_version_already_exists_fault import (
    CustomDBEngineVersionAlreadyExistsFault as CustomDBEngineVersionAlreadyExistsFault,
)
from .custom_db_engine_version_not_found_fault import (
    CustomDBEngineVersionNotFoundFault as CustomDBEngineVersionNotFoundFault,
)
from .custom_db_engine_version_quota_exceeded_fault import (
    CustomDBEngineVersionQuotaExceededFault as CustomDBEngineVersionQuotaExceededFault,
)
from .db_capacity_reservation_already_exists_fault import (
    DBCapacityReservationAlreadyExistsFault as DBCapacityReservationAlreadyExistsFault,
)
from .db_capacity_reservation_not_found_fault import (
    DBCapacityReservationNotFoundFault as DBCapacityReservationNotFoundFault,
)
from .db_capacity_reservation_unsupported_fault import (
    DBCapacityReservationUnsupportedFault as DBCapacityReservationUnsupportedFault,
)
from .db_cluster_already_exists_fault import (
    DBClusterAlreadyExistsFault as DBClusterAlreadyExistsFault,
)
from .db_cluster_automated_backup_not_found_fault import (
    DBClusterAutomatedBackupNotFoundFault as DBClusterAutomatedBackupNotFoundFault,
)
from .db_cluster_automated_backup_quota_exceeded_fault import (
    DBClusterAutomatedBackupQuotaExceededFault as DBClusterAutomatedBackupQuotaExceededFault,
)
from .db_cluster_backtrack_not_found_fault import (
    DBClusterBacktrackNotFoundFault as DBClusterBacktrackNotFoundFault,
)
from .db_cluster_endpoint_already_exists_fault import (
    DBClusterEndpointAlreadyExistsFault as DBClusterEndpointAlreadyExistsFault,
)
from .db_cluster_endpoint_not_found_fault import (
    DBClusterEndpointNotFoundFault as DBClusterEndpointNotFoundFault,
)
from .db_cluster_endpoint_quota_exceeded_fault import (
    DBClusterEndpointQuotaExceededFault as DBClusterEndpointQuotaExceededFault,
)
from .db_cluster_not_found_fault import DBClusterNotFoundFault as DBClusterNotFoundFault
from .db_cluster_parameter_group_not_found_fault import (
    DBClusterParameterGroupNotFoundFault as DBClusterParameterGroupNotFoundFault,
)
from .db_cluster_quota_exceeded_fault import (
    DBClusterQuotaExceededFault as DBClusterQuotaExceededFault,
)
from .db_cluster_role_already_exists_fault import (
    DBClusterRoleAlreadyExistsFault as DBClusterRoleAlreadyExistsFault,
)
from .db_cluster_role_not_found_fault import (
    DBClusterRoleNotFoundFault as DBClusterRoleNotFoundFault,
)
from .db_cluster_role_quota_exceeded_fault import (
    DBClusterRoleQuotaExceededFault as DBClusterRoleQuotaExceededFault,
)
from .db_cluster_snapshot_already_exists_fault import (
    DBClusterSnapshotAlreadyExistsFault as DBClusterSnapshotAlreadyExistsFault,
)
from .db_cluster_snapshot_not_found_fault import (
    DBClusterSnapshotNotFoundFault as DBClusterSnapshotNotFoundFault,
)
from .db_instance_already_exists_fault import (
    DBInstanceAlreadyExistsFault as DBInstanceAlreadyExistsFault,
)
from .db_instance_automated_backup_not_found_fault import (
    DBInstanceAutomatedBackupNotFoundFault as DBInstanceAutomatedBackupNotFoundFault,
)
from .db_instance_automated_backup_quota_exceeded_fault import (
    DBInstanceAutomatedBackupQuotaExceededFault as DBInstanceAutomatedBackupQuotaExceededFault,
)
from .db_instance_not_found_fault import (
    DBInstanceNotFoundFault as DBInstanceNotFoundFault,
)
from .db_instance_not_ready_fault import (
    DBInstanceNotReadyFault as DBInstanceNotReadyFault,
)
from .db_instance_role_already_exists_fault import (
    DBInstanceRoleAlreadyExistsFault as DBInstanceRoleAlreadyExistsFault,
)
from .db_instance_role_not_found_fault import (
    DBInstanceRoleNotFoundFault as DBInstanceRoleNotFoundFault,
)
from .db_instance_role_quota_exceeded_fault import (
    DBInstanceRoleQuotaExceededFault as DBInstanceRoleQuotaExceededFault,
)
from .db_log_file_not_found_fault import (
    DBLogFileNotFoundFault as DBLogFileNotFoundFault,
)
from .db_parameter_group_already_exists_fault import (
    DBParameterGroupAlreadyExistsFault as DBParameterGroupAlreadyExistsFault,
)
from .db_parameter_group_not_found_fault import (
    DBParameterGroupNotFoundFault as DBParameterGroupNotFoundFault,
)
from .db_parameter_group_quota_exceeded_fault import (
    DBParameterGroupQuotaExceededFault as DBParameterGroupQuotaExceededFault,
)
from .db_proxy_already_exists_fault import (
    DBProxyAlreadyExistsFault as DBProxyAlreadyExistsFault,
)
from .db_proxy_endpoint_already_exists_fault import (
    DBProxyEndpointAlreadyExistsFault as DBProxyEndpointAlreadyExistsFault,
)
from .db_proxy_endpoint_not_found_fault import (
    DBProxyEndpointNotFoundFault as DBProxyEndpointNotFoundFault,
)
from .db_proxy_endpoint_quota_exceeded_fault import (
    DBProxyEndpointQuotaExceededFault as DBProxyEndpointQuotaExceededFault,
)
from .db_proxy_not_found_fault import DBProxyNotFoundFault as DBProxyNotFoundFault
from .db_proxy_quota_exceeded_fault import (
    DBProxyQuotaExceededFault as DBProxyQuotaExceededFault,
)
from .db_proxy_target_already_registered_fault import (
    DBProxyTargetAlreadyRegisteredFault as DBProxyTargetAlreadyRegisteredFault,
)
from .db_proxy_target_group_not_found_fault import (
    DBProxyTargetGroupNotFoundFault as DBProxyTargetGroupNotFoundFault,
)
from .db_proxy_target_not_found_fault import (
    DBProxyTargetNotFoundFault as DBProxyTargetNotFoundFault,
)
from .db_security_group_already_exists_fault import (
    DBSecurityGroupAlreadyExistsFault as DBSecurityGroupAlreadyExistsFault,
)
from .db_security_group_not_found_fault import (
    DBSecurityGroupNotFoundFault as DBSecurityGroupNotFoundFault,
)
from .db_security_group_not_supported_fault import (
    DBSecurityGroupNotSupportedFault as DBSecurityGroupNotSupportedFault,
)
from .db_security_group_quota_exceeded_fault import (
    DBSecurityGroupQuotaExceededFault as DBSecurityGroupQuotaExceededFault,
)
from .db_shard_group_already_exists_fault import (
    DBShardGroupAlreadyExistsFault as DBShardGroupAlreadyExistsFault,
)
from .db_shard_group_not_found_fault import (
    DBShardGroupNotFoundFault as DBShardGroupNotFoundFault,
)
from .db_snapshot_already_exists_fault import (
    DBSnapshotAlreadyExistsFault as DBSnapshotAlreadyExistsFault,
)
from .db_snapshot_not_found_fault import (
    DBSnapshotNotFoundFault as DBSnapshotNotFoundFault,
)
from .db_snapshot_tenant_database_not_found_fault import (
    DBSnapshotTenantDatabaseNotFoundFault as DBSnapshotTenantDatabaseNotFoundFault,
)
from .db_subnet_group_already_exists_fault import (
    DBSubnetGroupAlreadyExistsFault as DBSubnetGroupAlreadyExistsFault,
)
from .db_subnet_group_does_not_cover_enough_a_zs import (
    DBSubnetGroupDoesNotCoverEnoughAZs as DBSubnetGroupDoesNotCoverEnoughAZs,
)
from .db_subnet_group_not_allowed_fault import (
    DBSubnetGroupNotAllowedFault as DBSubnetGroupNotAllowedFault,
)
from .db_subnet_group_not_found_fault import (
    DBSubnetGroupNotFoundFault as DBSubnetGroupNotFoundFault,
)
from .db_subnet_group_quota_exceeded_fault import (
    DBSubnetGroupQuotaExceededFault as DBSubnetGroupQuotaExceededFault,
)
from .db_subnet_quota_exceeded_fault import (
    DBSubnetQuotaExceededFault as DBSubnetQuotaExceededFault,
)
from .db_upgrade_dependency_failure_fault import (
    DBUpgradeDependencyFailureFault as DBUpgradeDependencyFailureFault,
)
from .domain_not_found_fault import DomainNotFoundFault as DomainNotFoundFault
from .ec2_image_properties_not_supported_fault import (
    Ec2ImagePropertiesNotSupportedFault as Ec2ImagePropertiesNotSupportedFault,
)
from .event_subscription_quota_exceeded_fault import (
    EventSubscriptionQuotaExceededFault as EventSubscriptionQuotaExceededFault,
)
from .export_task_already_exists_fault import (
    ExportTaskAlreadyExistsFault as ExportTaskAlreadyExistsFault,
)
from .export_task_not_found_fault import (
    ExportTaskNotFoundFault as ExportTaskNotFoundFault,
)
from .global_cluster_already_exists_fault import (
    GlobalClusterAlreadyExistsFault as GlobalClusterAlreadyExistsFault,
)
from .global_cluster_not_found_fault import (
    GlobalClusterNotFoundFault as GlobalClusterNotFoundFault,
)
from .global_cluster_quota_exceeded_fault import (
    GlobalClusterQuotaExceededFault as GlobalClusterQuotaExceededFault,
)
from .iam_role_missing_permissions_fault import (
    IamRoleMissingPermissionsFault as IamRoleMissingPermissionsFault,
)
from .iam_role_not_found_fault import IamRoleNotFoundFault as IamRoleNotFoundFault
from .instance_quota_exceeded_fault import (
    InstanceQuotaExceededFault as InstanceQuotaExceededFault,
)
from .insufficient_available_i_ps_in_subnet_fault import (
    InsufficientAvailableIPsInSubnetFault as InsufficientAvailableIPsInSubnetFault,
)
from .insufficient_db_cluster_capacity_fault import (
    InsufficientDBClusterCapacityFault as InsufficientDBClusterCapacityFault,
)
from .insufficient_db_instance_capacity_fault import (
    InsufficientDBInstanceCapacityFault as InsufficientDBInstanceCapacityFault,
)
from .insufficient_storage_cluster_capacity_fault import (
    InsufficientStorageClusterCapacityFault as InsufficientStorageClusterCapacityFault,
)
from .integration_already_exists_fault import (
    IntegrationAlreadyExistsFault as IntegrationAlreadyExistsFault,
)
from .integration_conflict_operation_fault import (
    IntegrationConflictOperationFault as IntegrationConflictOperationFault,
)
from .integration_not_found_fault import (
    IntegrationNotFoundFault as IntegrationNotFoundFault,
)
from .integration_quota_exceeded_fault import (
    IntegrationQuotaExceededFault as IntegrationQuotaExceededFault,
)
from .invalid_blue_green_deployment_state_fault import (
    InvalidBlueGreenDeploymentStateFault as InvalidBlueGreenDeploymentStateFault,
)
from .invalid_custom_db_engine_version_state_fault import (
    InvalidCustomDBEngineVersionStateFault as InvalidCustomDBEngineVersionStateFault,
)
from .invalid_db_capacity_reservation_state_fault import (
    InvalidDBCapacityReservationStateFault as InvalidDBCapacityReservationStateFault,
)
from .invalid_db_cluster_automated_backup_state_fault import (
    InvalidDBClusterAutomatedBackupStateFault as InvalidDBClusterAutomatedBackupStateFault,
)
from .invalid_db_cluster_capacity_fault import (
    InvalidDBClusterCapacityFault as InvalidDBClusterCapacityFault,
)
from .invalid_db_cluster_endpoint_state_fault import (
    InvalidDBClusterEndpointStateFault as InvalidDBClusterEndpointStateFault,
)
from .invalid_db_cluster_snapshot_state_fault import (
    InvalidDBClusterSnapshotStateFault as InvalidDBClusterSnapshotStateFault,
)
from .invalid_db_cluster_state_fault import (
    InvalidDBClusterStateFault as InvalidDBClusterStateFault,
)
from .invalid_db_instance_automated_backup_state_fault import (
    InvalidDBInstanceAutomatedBackupStateFault as InvalidDBInstanceAutomatedBackupStateFault,
)
from .invalid_db_instance_state_fault import (
    InvalidDBInstanceStateFault as InvalidDBInstanceStateFault,
)
from .invalid_db_parameter_group_state_fault import (
    InvalidDBParameterGroupStateFault as InvalidDBParameterGroupStateFault,
)
from .invalid_db_proxy_endpoint_state_fault import (
    InvalidDBProxyEndpointStateFault as InvalidDBProxyEndpointStateFault,
)
from .invalid_db_proxy_state_fault import (
    InvalidDBProxyStateFault as InvalidDBProxyStateFault,
)
from .invalid_db_security_group_state_fault import (
    InvalidDBSecurityGroupStateFault as InvalidDBSecurityGroupStateFault,
)
from .invalid_db_shard_group_state_fault import (
    InvalidDBShardGroupStateFault as InvalidDBShardGroupStateFault,
)
from .invalid_db_snapshot_state_fault import (
    InvalidDBSnapshotStateFault as InvalidDBSnapshotStateFault,
)
from .invalid_db_subnet_group_fault import (
    InvalidDBSubnetGroupFault as InvalidDBSubnetGroupFault,
)
from .invalid_db_subnet_group_state_fault import (
    InvalidDBSubnetGroupStateFault as InvalidDBSubnetGroupStateFault,
)
from .invalid_db_subnet_state_fault import (
    InvalidDBSubnetStateFault as InvalidDBSubnetStateFault,
)
from .invalid_event_subscription_state_fault import (
    InvalidEventSubscriptionStateFault as InvalidEventSubscriptionStateFault,
)
from .invalid_export_only_fault import InvalidExportOnlyFault as InvalidExportOnlyFault
from .invalid_export_source_state_fault import (
    InvalidExportSourceStateFault as InvalidExportSourceStateFault,
)
from .invalid_export_task_state_fault import (
    InvalidExportTaskStateFault as InvalidExportTaskStateFault,
)
from .invalid_global_cluster_state_fault import (
    InvalidGlobalClusterStateFault as InvalidGlobalClusterStateFault,
)
from .invalid_integration_state_fault import (
    InvalidIntegrationStateFault as InvalidIntegrationStateFault,
)
from .invalid_option_group_state_fault import (
    InvalidOptionGroupStateFault as InvalidOptionGroupStateFault,
)
from .invalid_resource_state_fault import (
    InvalidResourceStateFault as InvalidResourceStateFault,
)
from .invalid_restore_fault import InvalidRestoreFault as InvalidRestoreFault
from .invalid_s3_bucket_fault import InvalidS3BucketFault as InvalidS3BucketFault
from .invalid_subnet import InvalidSubnet as InvalidSubnet
from .invalid_vpc_network_state_fault import (
    InvalidVPCNetworkStateFault as InvalidVPCNetworkStateFault,
)
from .kms_key_not_accessible_fault import (
    KMSKeyNotAccessibleFault as KMSKeyNotAccessibleFault,
)
from .max_db_shard_group_limit_reached import (
    MaxDBShardGroupLimitReached as MaxDBShardGroupLimitReached,
)
from .network_type_not_supported import (
    NetworkTypeNotSupported as NetworkTypeNotSupported,
)
from .option_group_already_exists_fault import (
    OptionGroupAlreadyExistsFault as OptionGroupAlreadyExistsFault,
)
from .option_group_not_found_fault import (
    OptionGroupNotFoundFault as OptionGroupNotFoundFault,
)
from .option_group_quota_exceeded_fault import (
    OptionGroupQuotaExceededFault as OptionGroupQuotaExceededFault,
)
from .point_in_time_restore_not_enabled_fault import (
    PointInTimeRestoreNotEnabledFault as PointInTimeRestoreNotEnabledFault,
)
from .provisioned_iops_not_available_in_az_fault import (
    ProvisionedIopsNotAvailableInAZFault as ProvisionedIopsNotAvailableInAZFault,
)
from .reserved_db_instance_already_exists_fault import (
    ReservedDBInstanceAlreadyExistsFault as ReservedDBInstanceAlreadyExistsFault,
)
from .reserved_db_instance_not_found_fault import (
    ReservedDBInstanceNotFoundFault as ReservedDBInstanceNotFoundFault,
)
from .reserved_db_instance_quota_exceeded_fault import (
    ReservedDBInstanceQuotaExceededFault as ReservedDBInstanceQuotaExceededFault,
)
from .reserved_db_instances_offering_not_found_fault import (
    ReservedDBInstancesOfferingNotFoundFault as ReservedDBInstancesOfferingNotFoundFault,
)
from .resource_not_found_fault import ResourceNotFoundFault as ResourceNotFoundFault
from .shared_snapshot_quota_exceeded_fault import (
    SharedSnapshotQuotaExceededFault as SharedSnapshotQuotaExceededFault,
)
from .snapshot_quota_exceeded_fault import (
    SnapshotQuotaExceededFault as SnapshotQuotaExceededFault,
)
from .sns_invalid_topic_fault import SNSInvalidTopicFault as SNSInvalidTopicFault
from .sns_no_authorization_fault import (
    SNSNoAuthorizationFault as SNSNoAuthorizationFault,
)
from .sns_topic_arn_not_found_fault import (
    SNSTopicArnNotFoundFault as SNSTopicArnNotFoundFault,
)
from .source_cluster_not_supported_fault import (
    SourceClusterNotSupportedFault as SourceClusterNotSupportedFault,
)
from .source_database_not_supported_fault import (
    SourceDatabaseNotSupportedFault as SourceDatabaseNotSupportedFault,
)
from .source_not_found_fault import SourceNotFoundFault as SourceNotFoundFault
from .storage_quota_exceeded_fault import (
    StorageQuotaExceededFault as StorageQuotaExceededFault,
)
from .storage_type_not_available_fault import (
    StorageTypeNotAvailableFault as StorageTypeNotAvailableFault,
)
from .storage_type_not_supported_fault import (
    StorageTypeNotSupportedFault as StorageTypeNotSupportedFault,
)
from .subnet_already_in_use import SubnetAlreadyInUse as SubnetAlreadyInUse
from .subscription_already_exist_fault import (
    SubscriptionAlreadyExistFault as SubscriptionAlreadyExistFault,
)
from .subscription_category_not_found_fault import (
    SubscriptionCategoryNotFoundFault as SubscriptionCategoryNotFoundFault,
)
from .subscription_not_found_fault import (
    SubscriptionNotFoundFault as SubscriptionNotFoundFault,
)
from .tenant_database_already_exists_fault import (
    TenantDatabaseAlreadyExistsFault as TenantDatabaseAlreadyExistsFault,
)
from .tenant_database_not_found_fault import (
    TenantDatabaseNotFoundFault as TenantDatabaseNotFoundFault,
)
from .tenant_database_quota_exceeded_fault import (
    TenantDatabaseQuotaExceededFault as TenantDatabaseQuotaExceededFault,
)
from .unsupported_db_engine_version_fault import (
    UnsupportedDBEngineVersionFault as UnsupportedDBEngineVersionFault,
)
from .vpc_encryption_control_violation_exception import (
    VpcEncryptionControlViolationException as VpcEncryptionControlViolationException,
)
