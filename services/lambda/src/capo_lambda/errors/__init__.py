from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    LambdaError as LambdaError,
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
from .alias_limit_exceeded_exception import (
    AliasLimitExceededException as AliasLimitExceededException,
)
from .callback_timeout_exception import (
    CallbackTimeoutException as CallbackTimeoutException,
)
from .capacity_provider_limit_exceeded_exception import (
    CapacityProviderLimitExceededException as CapacityProviderLimitExceededException,
)
from .code_artifact_user_deleted_exception import (
    CodeArtifactUserDeletedException as CodeArtifactUserDeletedException,
)
from .code_artifact_user_failed_exception import (
    CodeArtifactUserFailedException as CodeArtifactUserFailedException,
)
from .code_artifact_user_pending_exception import (
    CodeArtifactUserPendingException as CodeArtifactUserPendingException,
)
from .code_signing_config_not_found_exception import (
    CodeSigningConfigNotFoundException as CodeSigningConfigNotFoundException,
)
from .code_storage_exceeded_exception import (
    CodeStorageExceededException as CodeStorageExceededException,
)
from .code_verification_failed_exception import (
    CodeVerificationFailedException as CodeVerificationFailedException,
)
from .durable_execution_already_started_exception import (
    DurableExecutionAlreadyStartedException as DurableExecutionAlreadyStartedException,
)
from .ec2_access_denied_exception import (
    EC2AccessDeniedException as EC2AccessDeniedException,
)
from .ec2_throttled_exception import EC2ThrottledException as EC2ThrottledException
from .ec2_unexpected_exception import EC2UnexpectedException as EC2UnexpectedException
from .efs_mount_connectivity_exception import (
    EFSMountConnectivityException as EFSMountConnectivityException,
)
from .efs_mount_failure_exception import (
    EFSMountFailureException as EFSMountFailureException,
)
from .efs_mount_timeout_exception import (
    EFSMountTimeoutException as EFSMountTimeoutException,
)
from .efsio_exception import EFSIOException as EFSIOException
from .eni_limit_reached_exception import (
    ENILimitReachedException as ENILimitReachedException,
)
from .eni_not_ready_exception import ENINotReadyException as ENINotReadyException
from .function_versions_per_capacity_provider_limit_exceeded_exception import (
    FunctionVersionsPerCapacityProviderLimitExceededException as FunctionVersionsPerCapacityProviderLimitExceededException,
)
from .invalid_code_signature_exception import (
    InvalidCodeSignatureException as InvalidCodeSignatureException,
)
from .invalid_parameter_value_exception import (
    InvalidParameterValueException as InvalidParameterValueException,
)
from .invalid_request_content_exception import (
    InvalidRequestContentException as InvalidRequestContentException,
)
from .invalid_runtime_exception import (
    InvalidRuntimeException as InvalidRuntimeException,
)
from .invalid_security_group_id_exception import (
    InvalidSecurityGroupIDException as InvalidSecurityGroupIDException,
)
from .invalid_subnet_id_exception import (
    InvalidSubnetIDException as InvalidSubnetIDException,
)
from .invalid_zip_file_exception import (
    InvalidZipFileException as InvalidZipFileException,
)
from .kms_access_denied_exception import (
    KMSAccessDeniedException as KMSAccessDeniedException,
)
from .kms_disabled_exception import KMSDisabledException as KMSDisabledException
from .kms_invalid_state_exception import (
    KMSInvalidStateException as KMSInvalidStateException,
)
from .kms_not_found_exception import KMSNotFoundException as KMSNotFoundException
from .mode_not_supported_exception import (
    ModeNotSupportedException as ModeNotSupportedException,
)
from .no_published_version_exception import (
    NoPublishedVersionException as NoPublishedVersionException,
)
from .policy_length_exceeded_exception import (
    PolicyLengthExceededException as PolicyLengthExceededException,
)
from .precondition_failed_exception import (
    PreconditionFailedException as PreconditionFailedException,
)
from .provisioned_concurrency_config_not_found_exception import (
    ProvisionedConcurrencyConfigNotFoundException as ProvisionedConcurrencyConfigNotFoundException,
)
from .public_policy_exception import PublicPolicyException as PublicPolicyException
from .recursive_invocation_exception import (
    RecursiveInvocationException as RecursiveInvocationException,
)
from .request_too_large_exception import (
    RequestTooLargeException as RequestTooLargeException,
)
from .resource_conflict_exception import (
    ResourceConflictException as ResourceConflictException,
)
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .resource_not_ready_exception import (
    ResourceNotReadyException as ResourceNotReadyException,
)
from .runtime_alias_deleted_exception import (
    RuntimeAliasDeletedException as RuntimeAliasDeletedException,
)
from .runtime_version_deleted_exception import (
    RuntimeVersionDeletedException as RuntimeVersionDeletedException,
)
from .s3_files_mount_connectivity_exception import (
    S3FilesMountConnectivityException as S3FilesMountConnectivityException,
)
from .s3_files_mount_failure_exception import (
    S3FilesMountFailureException as S3FilesMountFailureException,
)
from .s3_files_mount_timeout_exception import (
    S3FilesMountTimeoutException as S3FilesMountTimeoutException,
)
from .serialized_request_entity_too_large_exception import (
    SerializedRequestEntityTooLargeException as SerializedRequestEntityTooLargeException,
)
from .service_exception import ServiceException as ServiceException
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .snap_start_exception import SnapStartException as SnapStartException
from .snap_start_not_ready_exception import (
    SnapStartNotReadyException as SnapStartNotReadyException,
)
from .snap_start_regeneration_failure_exception import (
    SnapStartRegenerationFailureException as SnapStartRegenerationFailureException,
)
from .snap_start_timeout_exception import (
    SnapStartTimeoutException as SnapStartTimeoutException,
)
from .subnet_ip_address_limit_reached_exception import (
    SubnetIPAddressLimitReachedException as SubnetIPAddressLimitReachedException,
)
from .too_many_requests_exception import (
    TooManyRequestsException as TooManyRequestsException,
)
from .unsupported_media_type_exception import (
    UnsupportedMediaTypeException as UnsupportedMediaTypeException,
)
