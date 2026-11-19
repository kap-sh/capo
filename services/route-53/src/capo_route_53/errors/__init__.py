from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    Route53Error as Route53Error,
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
from .cidr_block_in_use_exception import (
    CidrBlockInUseException as CidrBlockInUseException,
)
from .cidr_collection_already_exists_exception import (
    CidrCollectionAlreadyExistsException as CidrCollectionAlreadyExistsException,
)
from .cidr_collection_in_use_exception import (
    CidrCollectionInUseException as CidrCollectionInUseException,
)
from .cidr_collection_version_mismatch_exception import (
    CidrCollectionVersionMismatchException as CidrCollectionVersionMismatchException,
)
from .concurrent_modification import ConcurrentModification as ConcurrentModification
from .conflicting_domain_exists import (
    ConflictingDomainExists as ConflictingDomainExists,
)
from .conflicting_types import ConflictingTypes as ConflictingTypes
from .delegation_set_already_created import (
    DelegationSetAlreadyCreated as DelegationSetAlreadyCreated,
)
from .delegation_set_already_reusable import (
    DelegationSetAlreadyReusable as DelegationSetAlreadyReusable,
)
from .delegation_set_in_use import DelegationSetInUse as DelegationSetInUse
from .delegation_set_not_available import (
    DelegationSetNotAvailable as DelegationSetNotAvailable,
)
from .delegation_set_not_reusable import (
    DelegationSetNotReusable as DelegationSetNotReusable,
)
from .dnssec_not_found import DNSSECNotFound as DNSSECNotFound
from .health_check_already_exists import (
    HealthCheckAlreadyExists as HealthCheckAlreadyExists,
)
from .health_check_in_use import HealthCheckInUse as HealthCheckInUse
from .health_check_version_mismatch import (
    HealthCheckVersionMismatch as HealthCheckVersionMismatch,
)
from .hosted_zone_already_exists import (
    HostedZoneAlreadyExists as HostedZoneAlreadyExists,
)
from .hosted_zone_not_empty import HostedZoneNotEmpty as HostedZoneNotEmpty
from .hosted_zone_not_found import HostedZoneNotFound as HostedZoneNotFound
from .hosted_zone_not_private import HostedZoneNotPrivate as HostedZoneNotPrivate
from .hosted_zone_partially_delegated import (
    HostedZonePartiallyDelegated as HostedZonePartiallyDelegated,
)
from .incompatible_version import IncompatibleVersion as IncompatibleVersion
from .insufficient_cloud_watch_logs_resource_policy import (
    InsufficientCloudWatchLogsResourcePolicy as InsufficientCloudWatchLogsResourcePolicy,
)
from .invalid_argument import InvalidArgument as InvalidArgument
from .invalid_change_batch import InvalidChangeBatch as InvalidChangeBatch
from .invalid_domain_name import InvalidDomainName as InvalidDomainName
from .invalid_input import InvalidInput as InvalidInput
from .invalid_key_signing_key_name import (
    InvalidKeySigningKeyName as InvalidKeySigningKeyName,
)
from .invalid_key_signing_key_status import (
    InvalidKeySigningKeyStatus as InvalidKeySigningKeyStatus,
)
from .invalid_kms_arn import InvalidKMSArn as InvalidKMSArn
from .invalid_pagination_token import InvalidPaginationToken as InvalidPaginationToken
from .invalid_resource_record_set_protection_batch import (
    InvalidResourceRecordSetProtectionBatch as InvalidResourceRecordSetProtectionBatch,
)
from .invalid_signing_status import InvalidSigningStatus as InvalidSigningStatus
from .invalid_traffic_policy_document import (
    InvalidTrafficPolicyDocument as InvalidTrafficPolicyDocument,
)
from .invalid_vpc_id import InvalidVPCId as InvalidVPCId
from .key_signing_key_already_exists import (
    KeySigningKeyAlreadyExists as KeySigningKeyAlreadyExists,
)
from .key_signing_key_in_parent_ds_record import (
    KeySigningKeyInParentDSRecord as KeySigningKeyInParentDSRecord,
)
from .key_signing_key_in_use import KeySigningKeyInUse as KeySigningKeyInUse
from .key_signing_key_with_active_status_not_found import (
    KeySigningKeyWithActiveStatusNotFound as KeySigningKeyWithActiveStatusNotFound,
)
from .last_vpc_association import LastVPCAssociation as LastVPCAssociation
from .limits_exceeded import LimitsExceeded as LimitsExceeded
from .no_such_change import NoSuchChange as NoSuchChange
from .no_such_cidr_collection_exception import (
    NoSuchCidrCollectionException as NoSuchCidrCollectionException,
)
from .no_such_cidr_location_exception import (
    NoSuchCidrLocationException as NoSuchCidrLocationException,
)
from .no_such_cloud_watch_logs_log_group import (
    NoSuchCloudWatchLogsLogGroup as NoSuchCloudWatchLogsLogGroup,
)
from .no_such_delegation_set import NoSuchDelegationSet as NoSuchDelegationSet
from .no_such_geo_location import NoSuchGeoLocation as NoSuchGeoLocation
from .no_such_health_check import NoSuchHealthCheck as NoSuchHealthCheck
from .no_such_hosted_zone import NoSuchHostedZone as NoSuchHostedZone
from .no_such_key_signing_key import NoSuchKeySigningKey as NoSuchKeySigningKey
from .no_such_query_logging_config import (
    NoSuchQueryLoggingConfig as NoSuchQueryLoggingConfig,
)
from .no_such_traffic_policy import NoSuchTrafficPolicy as NoSuchTrafficPolicy
from .no_such_traffic_policy_instance import (
    NoSuchTrafficPolicyInstance as NoSuchTrafficPolicyInstance,
)
from .not_authorized_exception import NotAuthorizedException as NotAuthorizedException
from .prior_request_not_complete import (
    PriorRequestNotComplete as PriorRequestNotComplete,
)
from .protection_already_exists import (
    ProtectionAlreadyExists as ProtectionAlreadyExists,
)
from .public_zone_vpc_association import (
    PublicZoneVPCAssociation as PublicZoneVPCAssociation,
)
from .query_logging_config_already_exists import (
    QueryLoggingConfigAlreadyExists as QueryLoggingConfigAlreadyExists,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .too_many_health_checks import TooManyHealthChecks as TooManyHealthChecks
from .too_many_hosted_zones import TooManyHostedZones as TooManyHostedZones
from .too_many_key_signing_keys import TooManyKeySigningKeys as TooManyKeySigningKeys
from .too_many_traffic_policies import TooManyTrafficPolicies as TooManyTrafficPolicies
from .too_many_traffic_policy_instances import (
    TooManyTrafficPolicyInstances as TooManyTrafficPolicyInstances,
)
from .too_many_traffic_policy_versions_for_current_policy import (
    TooManyTrafficPolicyVersionsForCurrentPolicy as TooManyTrafficPolicyVersionsForCurrentPolicy,
)
from .too_many_vpc_association_authorizations import (
    TooManyVPCAssociationAuthorizations as TooManyVPCAssociationAuthorizations,
)
from .traffic_policy_already_exists import (
    TrafficPolicyAlreadyExists as TrafficPolicyAlreadyExists,
)
from .traffic_policy_in_use import TrafficPolicyInUse as TrafficPolicyInUse
from .traffic_policy_instance_already_exists import (
    TrafficPolicyInstanceAlreadyExists as TrafficPolicyInstanceAlreadyExists,
)
from .vpc_association_authorization_not_found import (
    VPCAssociationAuthorizationNotFound as VPCAssociationAuthorizationNotFound,
)
from .vpc_association_not_found import VPCAssociationNotFound as VPCAssociationNotFound
