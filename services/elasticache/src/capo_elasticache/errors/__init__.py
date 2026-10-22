from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    ElastiCacheError as ElastiCacheError,
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
from .api_call_rate_for_customer_exceeded_fault import (
    APICallRateForCustomerExceededFault as APICallRateForCustomerExceededFault,
)
from .authorization_already_exists_fault import (
    AuthorizationAlreadyExistsFault as AuthorizationAlreadyExistsFault,
)
from .authorization_not_found_fault import (
    AuthorizationNotFoundFault as AuthorizationNotFoundFault,
)
from .cache_cluster_already_exists_fault import (
    CacheClusterAlreadyExistsFault as CacheClusterAlreadyExistsFault,
)
from .cache_cluster_not_found_fault import (
    CacheClusterNotFoundFault as CacheClusterNotFoundFault,
)
from .cache_parameter_group_already_exists_fault import (
    CacheParameterGroupAlreadyExistsFault as CacheParameterGroupAlreadyExistsFault,
)
from .cache_parameter_group_not_found_fault import (
    CacheParameterGroupNotFoundFault as CacheParameterGroupNotFoundFault,
)
from .cache_parameter_group_quota_exceeded_fault import (
    CacheParameterGroupQuotaExceededFault as CacheParameterGroupQuotaExceededFault,
)
from .cache_security_group_already_exists_fault import (
    CacheSecurityGroupAlreadyExistsFault as CacheSecurityGroupAlreadyExistsFault,
)
from .cache_security_group_not_found_fault import (
    CacheSecurityGroupNotFoundFault as CacheSecurityGroupNotFoundFault,
)
from .cache_security_group_quota_exceeded_fault import (
    CacheSecurityGroupQuotaExceededFault as CacheSecurityGroupQuotaExceededFault,
)
from .cache_subnet_group_already_exists_fault import (
    CacheSubnetGroupAlreadyExistsFault as CacheSubnetGroupAlreadyExistsFault,
)
from .cache_subnet_group_in_use import CacheSubnetGroupInUse as CacheSubnetGroupInUse
from .cache_subnet_group_not_found_fault import (
    CacheSubnetGroupNotFoundFault as CacheSubnetGroupNotFoundFault,
)
from .cache_subnet_group_quota_exceeded_fault import (
    CacheSubnetGroupQuotaExceededFault as CacheSubnetGroupQuotaExceededFault,
)
from .cache_subnet_quota_exceeded_fault import (
    CacheSubnetQuotaExceededFault as CacheSubnetQuotaExceededFault,
)
from .cluster_quota_for_customer_exceeded_fault import (
    ClusterQuotaForCustomerExceededFault as ClusterQuotaForCustomerExceededFault,
)
from .default_user_associated_to_user_group_fault import (
    DefaultUserAssociatedToUserGroupFault as DefaultUserAssociatedToUserGroupFault,
)
from .default_user_required import DefaultUserRequired as DefaultUserRequired
from .duplicate_user_name_fault import DuplicateUserNameFault as DuplicateUserNameFault
from .global_replication_group_already_exists_fault import (
    GlobalReplicationGroupAlreadyExistsFault as GlobalReplicationGroupAlreadyExistsFault,
)
from .global_replication_group_not_found_fault import (
    GlobalReplicationGroupNotFoundFault as GlobalReplicationGroupNotFoundFault,
)
from .insufficient_cache_cluster_capacity_fault import (
    InsufficientCacheClusterCapacityFault as InsufficientCacheClusterCapacityFault,
)
from .invalid_arn_fault import InvalidARNFault as InvalidARNFault
from .invalid_cache_cluster_state_fault import (
    InvalidCacheClusterStateFault as InvalidCacheClusterStateFault,
)
from .invalid_cache_parameter_group_state_fault import (
    InvalidCacheParameterGroupStateFault as InvalidCacheParameterGroupStateFault,
)
from .invalid_cache_security_group_state_fault import (
    InvalidCacheSecurityGroupStateFault as InvalidCacheSecurityGroupStateFault,
)
from .invalid_credentials_exception import (
    InvalidCredentialsException as InvalidCredentialsException,
)
from .invalid_global_replication_group_state_fault import (
    InvalidGlobalReplicationGroupStateFault as InvalidGlobalReplicationGroupStateFault,
)
from .invalid_kms_key_fault import InvalidKMSKeyFault as InvalidKMSKeyFault
from .invalid_parameter_combination_exception import (
    InvalidParameterCombinationException as InvalidParameterCombinationException,
)
from .invalid_parameter_value_exception import (
    InvalidParameterValueException as InvalidParameterValueException,
)
from .invalid_replication_group_state_fault import (
    InvalidReplicationGroupStateFault as InvalidReplicationGroupStateFault,
)
from .invalid_serverless_cache_snapshot_state_fault import (
    InvalidServerlessCacheSnapshotStateFault as InvalidServerlessCacheSnapshotStateFault,
)
from .invalid_serverless_cache_state_fault import (
    InvalidServerlessCacheStateFault as InvalidServerlessCacheStateFault,
)
from .invalid_snapshot_state_fault import (
    InvalidSnapshotStateFault as InvalidSnapshotStateFault,
)
from .invalid_subnet import InvalidSubnet as InvalidSubnet
from .invalid_user_group_state_fault import (
    InvalidUserGroupStateFault as InvalidUserGroupStateFault,
)
from .invalid_user_state_fault import InvalidUserStateFault as InvalidUserStateFault
from .invalid_vpc_network_state_fault import (
    InvalidVPCNetworkStateFault as InvalidVPCNetworkStateFault,
)
from .migration_health_fault import MigrationHealthFault as MigrationHealthFault
from .no_operation_fault import NoOperationFault as NoOperationFault
from .node_group_not_found_fault import NodeGroupNotFoundFault as NodeGroupNotFoundFault
from .node_groups_per_replication_group_quota_exceeded_fault import (
    NodeGroupsPerReplicationGroupQuotaExceededFault as NodeGroupsPerReplicationGroupQuotaExceededFault,
)
from .node_quota_for_cluster_exceeded_fault import (
    NodeQuotaForClusterExceededFault as NodeQuotaForClusterExceededFault,
)
from .node_quota_for_customer_exceeded_fault import (
    NodeQuotaForCustomerExceededFault as NodeQuotaForCustomerExceededFault,
)
from .replication_group_already_exists_fault import (
    ReplicationGroupAlreadyExistsFault as ReplicationGroupAlreadyExistsFault,
)
from .replication_group_already_under_migration_fault import (
    ReplicationGroupAlreadyUnderMigrationFault as ReplicationGroupAlreadyUnderMigrationFault,
)
from .replication_group_not_found_fault import (
    ReplicationGroupNotFoundFault as ReplicationGroupNotFoundFault,
)
from .replication_group_not_under_migration_fault import (
    ReplicationGroupNotUnderMigrationFault as ReplicationGroupNotUnderMigrationFault,
)
from .reserved_cache_node_already_exists_fault import (
    ReservedCacheNodeAlreadyExistsFault as ReservedCacheNodeAlreadyExistsFault,
)
from .reserved_cache_node_not_found_fault import (
    ReservedCacheNodeNotFoundFault as ReservedCacheNodeNotFoundFault,
)
from .reserved_cache_node_quota_exceeded_fault import (
    ReservedCacheNodeQuotaExceededFault as ReservedCacheNodeQuotaExceededFault,
)
from .reserved_cache_nodes_offering_not_found_fault import (
    ReservedCacheNodesOfferingNotFoundFault as ReservedCacheNodesOfferingNotFoundFault,
)
from .serverless_cache_already_exists_fault import (
    ServerlessCacheAlreadyExistsFault as ServerlessCacheAlreadyExistsFault,
)
from .serverless_cache_already_under_migration_fault import (
    ServerlessCacheAlreadyUnderMigrationFault as ServerlessCacheAlreadyUnderMigrationFault,
)
from .serverless_cache_not_found_fault import (
    ServerlessCacheNotFoundFault as ServerlessCacheNotFoundFault,
)
from .serverless_cache_not_under_migration_fault import (
    ServerlessCacheNotUnderMigrationFault as ServerlessCacheNotUnderMigrationFault,
)
from .serverless_cache_quota_for_customer_exceeded_fault import (
    ServerlessCacheQuotaForCustomerExceededFault as ServerlessCacheQuotaForCustomerExceededFault,
)
from .serverless_cache_snapshot_already_exists_fault import (
    ServerlessCacheSnapshotAlreadyExistsFault as ServerlessCacheSnapshotAlreadyExistsFault,
)
from .serverless_cache_snapshot_not_found_fault import (
    ServerlessCacheSnapshotNotFoundFault as ServerlessCacheSnapshotNotFoundFault,
)
from .serverless_cache_snapshot_quota_exceeded_fault import (
    ServerlessCacheSnapshotQuotaExceededFault as ServerlessCacheSnapshotQuotaExceededFault,
)
from .service_linked_role_not_found_fault import (
    ServiceLinkedRoleNotFoundFault as ServiceLinkedRoleNotFoundFault,
)
from .service_update_not_found_fault import (
    ServiceUpdateNotFoundFault as ServiceUpdateNotFoundFault,
)
from .snapshot_already_exists_fault import (
    SnapshotAlreadyExistsFault as SnapshotAlreadyExistsFault,
)
from .snapshot_feature_not_supported_fault import (
    SnapshotFeatureNotSupportedFault as SnapshotFeatureNotSupportedFault,
)
from .snapshot_not_found_fault import SnapshotNotFoundFault as SnapshotNotFoundFault
from .snapshot_quota_exceeded_fault import (
    SnapshotQuotaExceededFault as SnapshotQuotaExceededFault,
)
from .subnet_in_use import SubnetInUse as SubnetInUse
from .subnet_not_allowed_fault import SubnetNotAllowedFault as SubnetNotAllowedFault
from .tag_not_found_fault import TagNotFoundFault as TagNotFoundFault
from .tag_quota_per_resource_exceeded import (
    TagQuotaPerResourceExceeded as TagQuotaPerResourceExceeded,
)
from .test_failover_not_available_fault import (
    TestFailoverNotAvailableFault as TestFailoverNotAvailableFault,
)
from .user_already_exists_fault import UserAlreadyExistsFault as UserAlreadyExistsFault
from .user_group_already_exists_fault import (
    UserGroupAlreadyExistsFault as UserGroupAlreadyExistsFault,
)
from .user_group_not_found_fault import UserGroupNotFoundFault as UserGroupNotFoundFault
from .user_group_quota_exceeded_fault import (
    UserGroupQuotaExceededFault as UserGroupQuotaExceededFault,
)
from .user_not_found_fault import UserNotFoundFault as UserNotFoundFault
from .user_quota_exceeded_fault import UserQuotaExceededFault as UserQuotaExceededFault
