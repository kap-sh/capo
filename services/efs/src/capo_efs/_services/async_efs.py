"""Generated from Smithy shape ``com.amazonaws.efs#MagnolioAPIService_v20150201``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_efs._auth._signers
import capo_efs._auth._sigv4
from capo_efs._auth._identity import Credentials
from capo_efs._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_efs._auth._zapros_handler import AuthMiddleware
from capo_efs._pagination import resolve_path as _resolve_path
from capo_efs._services._aws_config import aaws_config
from capo_efs._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_efs.types.access_point_description
    import capo_efs.types.access_point_id
    import capo_efs.types.availability_zone_name
    import capo_efs.types.backup
    import capo_efs.types.backup_policy
    import capo_efs.types.backup_policy_description
    import capo_efs.types.bypass_policy_lockout_safety_check
    import capo_efs.types.client_token
    import capo_efs.types.create_access_point_request
    import capo_efs.types.create_file_system_request
    import capo_efs.types.create_mount_target_request
    import capo_efs.types.create_replication_configuration_request
    import capo_efs.types.create_tags_request
    import capo_efs.types.creation_token
    import capo_efs.types.delete_access_point_request
    import capo_efs.types.delete_file_system_policy_request
    import capo_efs.types.delete_file_system_request
    import capo_efs.types.delete_mount_target_request
    import capo_efs.types.delete_replication_configuration_request
    import capo_efs.types.delete_tags_request
    import capo_efs.types.deletion_mode
    import capo_efs.types.describe_access_points_request
    import capo_efs.types.describe_access_points_response
    import capo_efs.types.describe_account_preferences_request
    import capo_efs.types.describe_account_preferences_response
    import capo_efs.types.describe_backup_policy_request
    import capo_efs.types.describe_file_system_policy_request
    import capo_efs.types.describe_file_systems_request
    import capo_efs.types.describe_file_systems_response
    import capo_efs.types.describe_lifecycle_configuration_request
    import capo_efs.types.describe_mount_target_security_groups_request
    import capo_efs.types.describe_mount_target_security_groups_response
    import capo_efs.types.describe_mount_targets_request
    import capo_efs.types.describe_mount_targets_response
    import capo_efs.types.describe_replication_configurations_request
    import capo_efs.types.describe_replication_configurations_response
    import capo_efs.types.describe_tags_request
    import capo_efs.types.describe_tags_response
    import capo_efs.types.destinations_to_create
    import capo_efs.types.encrypted
    import capo_efs.types.file_system_description
    import capo_efs.types.file_system_id
    import capo_efs.types.file_system_policy_description
    import capo_efs.types.file_system_protection_description
    import capo_efs.types.ip_address
    import capo_efs.types.ip_address_type
    import capo_efs.types.ipv6_address
    import capo_efs.types.kms_key_id
    import capo_efs.types.lifecycle_configuration_description
    import capo_efs.types.lifecycle_policies
    import capo_efs.types.list_tags_for_resource_request
    import capo_efs.types.list_tags_for_resource_response
    import capo_efs.types.marker
    import capo_efs.types.max_items
    import capo_efs.types.max_results
    import capo_efs.types.modify_mount_target_security_groups_request
    import capo_efs.types.mount_target_description
    import capo_efs.types.mount_target_id
    import capo_efs.types.performance_mode
    import capo_efs.types.policy
    import capo_efs.types.posix_user
    import capo_efs.types.provisioned_throughput_in_mibps
    import capo_efs.types.put_account_preferences_request
    import capo_efs.types.put_account_preferences_response
    import capo_efs.types.put_backup_policy_request
    import capo_efs.types.put_file_system_policy_request
    import capo_efs.types.put_lifecycle_configuration_request
    import capo_efs.types.replication_configuration_description
    import capo_efs.types.replication_overwrite_protection
    import capo_efs.types.resource_id
    import capo_efs.types.resource_id_type
    import capo_efs.types.root_directory
    import capo_efs.types.security_groups
    import capo_efs.types.subnet_id
    import capo_efs.types.tag
    import capo_efs.types.tag_keys
    import capo_efs.types.tag_resource_request
    import capo_efs.types.tags
    import capo_efs.types.throughput_mode
    import capo_efs.types.token
    import capo_efs.types.untag_resource_request
    import capo_efs.types.update_file_system_protection_request
    import capo_efs.types.update_file_system_request


class AsyncEFSClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncEFSClient:
    """A client for the ``EFS`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncEFSClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncEFSClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncEFSClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def create_access_point(
        self,
        client_token: "capo_efs.types.client_token.ClientToken",
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        tags: Optional["capo_efs.types.tags.Tags"] = None,
        posix_user: Optional["capo_efs.types.posix_user.PosixUser"] = None,
        root_directory: Optional["capo_efs.types.root_directory.RootDirectory"] = None,
    ) -> "capo_efs.types.access_point_description.AccessPointDescription":
        """<p>Creates an EFS access point. An access point is an application-specific view into an EFS file system that applies an operating system user and group, and a file system path, to any file system request made through the access point. The operating system user and group override any identity information provided by the NFS client. The file system path is exposed as the access point's root directory. Applications using the access point can only access data in the application's own directory and any subdirectories. A file system can have a maximum of 10,000 access points unless you request an increase. To learn more, see <a href="https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html">Mounting a file system using EFS access points</a>.</p> <note> <p>If multiple requests to create access points on the same file system are sent in quick succession, and the file system is near the limit of access points, you may experience a throttling response for these requests. This is to ensure that the file system does not exceed the stated access point limit.</p> </note> <p>This operation requires permissions for the <code>elasticfilesystem:CreateAccessPoint</code> action.</p> <p>Access points can be tagged on creation. If tags are specified in the creation action, IAM performs additional authorization on the <code>elasticfilesystem:TagResource</code> action to verify if users have permissions to create tags. Therefore, you must grant explicit permissions to use the <code>elasticfilesystem:TagResource</code> action. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/using-tags-efs.html#supported-iam-actions-tagging.html">Granting permissions to tag resources during creation</a>.</p>

        Args:
            client_token: <p>A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.</p>
            tags: <p>Creates tags associated with the access point. Each tag is a key-value pair, each key must be unique. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>
            file_system_id: <p>The ID of the EFS file system that the access point provides access to.</p>
            posix_user: <p>The operating system user and group applied to all file system requests made using the access point.</p>
            root_directory: <p>Specifies the directory on the EFS file system that the access point exposes as the root directory of your file system to NFS clients using the access point. The clients using the access point can only access the root directory and below. If the <code>RootDirectory</code> > <code>Path</code> specified does not exist, Amazon EFS creates it and applies the <code>CreationInfo</code> settings when a client connects to an access point. When specifying a <code>RootDirectory</code>, you must provide the <code>Path</code>, and the <code>CreationInfo</code>.</p> <p>Amazon EFS creates a root directory only if you have provided the CreationInfo: OwnUid, OwnGID, and permissions for the directory. If you do not provide this information, Amazon EFS does not create the root directory. If the root directory does not exist, attempts to mount using the access point will fail.</p>

        Raises:
            capo_efs.errors.access_point_already_exists.AccessPointAlreadyExists: <p>Returned if the access point that you are trying to create already exists, with the creation token you provided in the request.</p>
            capo_efs.errors.access_point_limit_exceeded.AccessPointLimitExceeded: <p>Returned if the Amazon Web Services account has already created the maximum number of access points allowed per file system. For more informaton, see <a href="https://docs.aws.amazon.com/efs/latest/ug/limits.html#limits-efs-resources-per-account-per-region">https://docs.aws.amazon.com/efs/latest/ug/limits.html#limits-efs-resources-per-account-per-region</a>.</p>
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.incorrect_file_system_life_cycle_state.IncorrectFileSystemLifeCycleState: <p>Returned if the file system's lifecycle state is not "available".</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.throttling_exception.ThrottlingException: <p>Returned when the <code>CreateAccessPoint</code> API action is called too quickly and the number of Access Points on the file system is nearing the <a href="https://docs.aws.amazon.com/efs/latest/ug/limits.html#limits-efs-resources-per-account-per-region">limit of 120</a>.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.create_access_point_request.CreateAccessPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.access_point_description.AccessPointDescription"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.create_access_point

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.create_access_point.async_create_access_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.create_access_point_request.CreateAccessPointRequest = {
            "client_token": client_token,
            "file_system_id": file_system_id,
        }
        if tags is not None:
            input_["tags"] = tags
        if posix_user is not None:
            input_["posix_user"] = posix_user
        if root_directory is not None:
            input_["root_directory"] = root_directory

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_file_system(
        self,
        creation_token: "capo_efs.types.creation_token.CreationToken",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        performance_mode: Optional[
            "capo_efs.types.performance_mode.PerformanceMode"
        ] = None,
        encrypted: Optional["capo_efs.types.encrypted.Encrypted"] = None,
        kms_key_id: Optional["capo_efs.types.kms_key_id.KmsKeyId"] = None,
        throughput_mode: Optional[
            "capo_efs.types.throughput_mode.ThroughputMode"
        ] = None,
        provisioned_throughput_in_mibps: Optional[
            "capo_efs.types.provisioned_throughput_in_mibps.ProvisionedThroughputInMibps"
        ] = None,
        availability_zone_name: Optional[
            "capo_efs.types.availability_zone_name.AvailabilityZoneName"
        ] = None,
        backup: Optional["capo_efs.types.backup.Backup"] = None,
        tags: Optional["capo_efs.types.tags.Tags"] = None,
    ) -> "capo_efs.types.file_system_description.FileSystemDescription":
        """<p>Creates a new, empty file system. The operation requires a creation token in the request that Amazon EFS uses to ensure idempotent creation (calling the operation with same creation token has no effect). If a file system does not currently exist that is owned by the caller's Amazon Web Services account with the specified creation token, this operation does the following:</p> <ul> <li> <p>Creates a new, empty file system. The file system will have an Amazon EFS assigned ID, and an initial lifecycle state <code>creating</code>.</p> </li> <li> <p>Returns with the description of the created file system.</p> </li> </ul> <p>Otherwise, this operation returns a <code>FileSystemAlreadyExists</code> error with the ID of the existing file system.</p> <note> <p>For basic use cases, you can use a randomly generated UUID for the creation token.</p> </note> <p>The idempotent operation allows you to retry a <code>CreateFileSystem</code> call without risk of creating an extra file system. This can happen when an initial call fails in a way that leaves it uncertain whether or not a file system was actually created. An example might be that a transport level timeout occurred or your connection was reset. As long as you use the same creation token, if the initial call had succeeded in creating a file system, the client can learn of its existence from the <code>FileSystemAlreadyExists</code> error.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html#creating-using-create-fs-part1">Creating a file system</a> in the <i>Amazon EFS User Guide</i>.</p> <note> <p>The <code>CreateFileSystem</code> call returns while the file system's lifecycle state is still <code>creating</code>. You can check the file system creation status by calling the <a>DescribeFileSystems</a> operation, which among other things returns the file system state.</p> </note> <p>This operation accepts an optional <code>PerformanceMode</code> parameter that you choose for your file system. We recommend <code>generalPurpose</code> <code>PerformanceMode</code> for all file systems. The <code>maxIO</code> mode is a previous generation performance type that is designed for highly parallelized workloads that can tolerate higher latencies than the <code>generalPurpose</code> mode. <code>MaxIO</code> mode is not supported for One Zone file systems or file systems that use Elastic throughput.</p> <p>The <code>PerformanceMode</code> can't be changed after the file system has been created. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/performance.html#performancemodes.html">Amazon EFS performance modes</a>.</p> <p>You can set the throughput mode for the file system using the <code>ThroughputMode</code> parameter.</p> <p>After the file system is fully created, Amazon EFS sets its lifecycle state to <code>available</code>, at which point you can create one or more mount targets for the file system in your VPC. For more information, see <a>CreateMountTarget</a>. You mount your Amazon EFS file system on an EC2 instances in your VPC by using the mount target. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html">Amazon EFS: How it Works</a>. </p> <p>This operation requires permissions for the <code>elasticfilesystem:CreateFileSystem</code> action. </p> <p>File systems can be tagged on creation. If tags are specified in the creation action, IAM performs additional authorization on the <code>elasticfilesystem:TagResource</code> action to verify if users have permissions to create tags. Therefore, you must grant explicit permissions to use the <code>elasticfilesystem:TagResource</code> action. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/using-tags-efs.html#supported-iam-actions-tagging.html">Granting permissions to tag resources during creation</a>.</p>

        Args:
            creation_token: <p>A string of up to 64 ASCII characters. Amazon EFS uses this to ensure idempotent creation.</p>
            performance_mode: <p>The performance mode of the file system. We recommend <code>generalPurpose</code> performance mode for all file systems. File systems using the <code>maxIO</code> performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. The performance mode can't be changed after the file system has been created. The <code>maxIO</code> mode is not supported on One Zone file systems.</p> <important> <p>Due to the higher per-operation latencies with Max I/O, we recommend using General Purpose performance mode for all file systems.</p> </important> <p>Default is <code>generalPurpose</code>.</p>
            encrypted: <p>A Boolean value that, if true, creates an encrypted file system. When creating an encrypted file system, you have the option of specifying an existing Key Management Service key (KMS key). If you don't specify a KMS key, then the default KMS key for Amazon EFS, <code>/aws/elasticfilesystem</code>, is used to protect the encrypted file system. </p>
            kms_key_id: <p>The ID of the KMS key that you want to use to protect the encrypted file system. This parameter is required only if you want to use a non-default KMS key. If this parameter is not specified, the default KMS key for Amazon EFS is used. You can specify a KMS key ID using the following formats:</p> <ul> <li> <p>Key ID - A unique identifier of the key, for example <code>1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p> </li> <li> <p>ARN - An Amazon Resource Name (ARN) for the key, for example <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p> </li> <li> <p>Key alias - A previously created display name for a key, for example <code>alias/projectKey1</code>.</p> </li> <li> <p>Key alias ARN - An ARN for a key alias, for example <code>arn:aws:kms:us-west-2:444455556666:alias/projectKey1</code>.</p> </li> </ul> <p>If you use <code>KmsKeyId</code>, you must set the <a>CreateFileSystemRequest$Encrypted</a> parameter to true.</p> <important> <p>EFS accepts only symmetric KMS keys. You cannot use asymmetric KMS keys with Amazon EFS file systems.</p> </important>
            throughput_mode: <p>Specifies the throughput mode for the file system. The mode can be <code>bursting</code>, <code>provisioned</code>, or <code>elastic</code>. If you set <code>ThroughputMode</code> to <code>provisioned</code>, you must also set a value for <code>ProvisionedThroughputInMibps</code>. After you create the file system, you can decrease your file system's Provisioned throughput or change between the throughput modes, with certain time restrictions. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/performance.html#provisioned-throughput">Specifying throughput with provisioned mode</a> in the <i>Amazon EFS User Guide</i>. </p> <p>Default is <code>bursting</code>.</p>
            provisioned_throughput_in_mibps: <p>The throughput, measured in mebibytes per second (MiBps), that you want to provision for a file system that you're creating. Required if <code>ThroughputMode</code> is set to <code>provisioned</code>. Valid values are 1-3414 MiBps, with the upper limit depending on Region. To increase this limit, contact Amazon Web Services Support. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits">Amazon EFS quotas that you can increase</a> in the <i>Amazon EFS User Guide</i>.</p>
            availability_zone_name: <p>For One Zone file systems, specify the Amazon Web Services Availability Zone in which to create the file system. Use the format <code>us-east-1a</code> to specify the Availability Zone. For more information about One Zone file systems, see <a href="https://docs.aws.amazon.com/efs/latest/ug/availability-durability.html#file-system-type">EFS file system types</a> in the <i>Amazon EFS User Guide</i>.</p> <note> <p>One Zone file systems are not available in all Availability Zones in Amazon Web Services Regions where Amazon EFS is available.</p> </note>
            backup: <p>Specifies whether automatic backups are enabled on the file system that you are creating. Set the value to <code>true</code> to enable automatic backups. If you are creating a One Zone file system, automatic backups are enabled by default. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html#automatic-backups">Automatic backups</a> in the <i>Amazon EFS User Guide</i>.</p> <p>Default is <code>false</code>. However, if you specify an <code>AvailabilityZoneName</code>, the default is <code>true</code>.</p> <note> <p>Backup is not available in all Amazon Web Services Regions where Amazon EFS is available.</p> </note>
            tags: <p>Use to create one or more tags associated with the file system. Each tag is a user-defined key-value pair. Name your file system on creation by including a <code>"Key":"Name","Value":"{value}"</code> key-value pair. Each key must be unique. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_already_exists.FileSystemAlreadyExists: <p>Returned if the file system you are trying to create already exists, with the creation token you provided.</p>
            capo_efs.errors.file_system_limit_exceeded.FileSystemLimitExceeded: <p>Returned if the Amazon Web Services account has already created the maximum number of file systems allowed per account.</p>
            capo_efs.errors.insufficient_throughput_capacity.InsufficientThroughputCapacity: <p>Returned if there's not enough capacity to provision additional throughput. This value might be returned when you try to create a file system in provisioned throughput mode, when you attempt to increase the provisioned throughput of an existing file system, or when you attempt to change an existing file system from Bursting Throughput to Provisioned Throughput mode. Try again later.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.throughput_limit_exceeded.ThroughputLimitExceeded: <p>Returned if the throughput mode or amount of provisioned throughput can't be changed because the throughput limit of 1024 MiB/s has been reached.</p>
            capo_efs.errors.unsupported_availability_zone.UnsupportedAvailabilityZone: <p>Returned if the requested Amazon EFS functionality is not available in the specified Availability Zone.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.create_file_system_request.CreateFileSystemRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.file_system_description.FileSystemDescription"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.create_file_system

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.create_file_system.async_create_file_system(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.create_file_system_request.CreateFileSystemRequest = {
            "creation_token": creation_token
        }
        if performance_mode is not None:
            input_["performance_mode"] = performance_mode
        if encrypted is not None:
            input_["encrypted"] = encrypted
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if throughput_mode is not None:
            input_["throughput_mode"] = throughput_mode
        if provisioned_throughput_in_mibps is not None:
            input_["provisioned_throughput_in_mibps"] = provisioned_throughput_in_mibps
        if availability_zone_name is not None:
            input_["availability_zone_name"] = availability_zone_name
        if backup is not None:
            input_["backup"] = backup
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_mount_target(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        subnet_id: "capo_efs.types.subnet_id.SubnetId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        ip_address: Optional["capo_efs.types.ip_address.IpAddress"] = None,
        ipv6_address: Optional["capo_efs.types.ipv6_address.Ipv6Address"] = None,
        ip_address_type: Optional[
            "capo_efs.types.ip_address_type.IpAddressType"
        ] = None,
        security_groups: Optional[
            "capo_efs.types.security_groups.SecurityGroups"
        ] = None,
    ) -> "capo_efs.types.mount_target_description.MountTargetDescription":
        """<p>Creates a mount target for a file system. You can then mount the file system on EC2 instances by using the mount target.</p> <p>You can create one mount target in each Availability Zone in your VPC. All EC2 instances in a VPC within a given Availability Zone share a single mount target for a given file system. If you have multiple subnets in an Availability Zone, you create a mount target in one of the subnets. EC2 instances do not need to be in the same subnet as the mount target in order to access their file system.</p> <p>You can create only one mount target for a One Zone file system. You must create that mount target in the same Availability Zone in which the file system is located. Use the <code>AvailabilityZoneName</code> and <code>AvailabiltyZoneId</code> properties in the <a>DescribeFileSystems</a> response object to get this information. Use the <code>subnetId</code> associated with the file system's Availability Zone when creating the mount target.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html">Amazon EFS: How it Works</a>. </p> <p>To create a mount target for a file system, the file system's lifecycle state must be <code>available</code>. For more information, see <a>DescribeFileSystems</a>.</p> <p>In the request, provide the following:</p> <ul> <li> <p>The file system ID for which you are creating the mount target.</p> </li> <li> <p>A subnet ID, which determines the following:</p> <ul> <li> <p>The VPC in which Amazon EFS creates the mount target</p> </li> <li> <p>The Availability Zone in which Amazon EFS creates the mount target</p> </li> <li> <p>The IP address range from which Amazon EFS selects the IP address of the mount target (if you don't specify an IP address in the request)</p> </li> </ul> </li> </ul> <p>After creating the mount target, Amazon EFS returns a response that includes, a <code>MountTargetId</code> and an <code>IpAddress</code>. You use this IP address when mounting the file system in an EC2 instance. You can also use the mount target's DNS name when mounting the file system. The EC2 instance on which you mount the file system by using the mount target can resolve the mount target's DNS name to its IP address. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html#how-it-works-implementation">How it Works: Implementation Overview</a>. </p> <p>Note that you can create mount targets for a file system in only one VPC, and there can be only one mount target per Availability Zone. That is, if the file system already has one or more mount targets created for it, the subnet specified in the request to add another mount target must meet the following requirements:</p> <ul> <li> <p>Must belong to the same VPC as the subnets of the existing mount targets</p> </li> <li> <p>Must not be in the same Availability Zone as any of the subnets of the existing mount targets</p> </li> </ul> <p>If the request satisfies the requirements, Amazon EFS does the following:</p> <ul> <li> <p>Creates a new mount target in the specified subnet.</p> </li> <li> <p>Also creates a new network interface in the subnet as follows:</p> <ul> <li> <p>If the request provides an <code>IpAddress</code>, Amazon EFS assigns that IP address to the network interface. Otherwise, Amazon EFS assigns a free address in the subnet (in the same way that the Amazon EC2 <code>CreateNetworkInterface</code> call does when a request does not specify a primary private IP address).</p> </li> <li> <p>If the request provides <code>SecurityGroups</code>, this network interface is associated with those security groups. Otherwise, it belongs to the default security group for the subnet's VPC.</p> </li> <li> <p>Assigns the description <code>Mount target <i>fsmt-id</i> for file system <i>fs-id</i> </code> where <code> <i>fsmt-id</i> </code> is the mount target ID, and <code> <i>fs-id</i> </code> is the <code>FileSystemId</code>.</p> </li> <li> <p>Sets the <code>requesterManaged</code> property of the network interface to <code>true</code>, and the <code>requesterId</code> value to <code>EFS</code>.</p> </li> </ul> <p>Each Amazon EFS mount target has one corresponding requester-managed EC2 network interface. After the network interface is created, Amazon EFS sets the <code>NetworkInterfaceId</code> field in the mount target's description to the network interface ID, and the <code>IpAddress</code> field to its address. If network interface creation fails, the entire <code>CreateMountTarget</code> operation fails.</p> </li> </ul> <note> <p>The <code>CreateMountTarget</code> call returns only after creating the network interface, but while the mount target state is still <code>creating</code>, you can check the mount target creation status by calling the <a>DescribeMountTargets</a> operation, which among other things returns the mount target state.</p> </note> <p>We recommend that you create a mount target in each of the Availability Zones. There are cost considerations for using a file system in an Availability Zone through a mount target created in another Availability Zone. For more information, see <a href="http://aws.amazon.com/efs/pricing/">Amazon EFS pricing</a>. In addition, by always using a mount target local to the instance's Availability Zone, you eliminate a partial failure scenario. If the Availability Zone in which your mount target is created goes down, then you can't access your file system through that mount target. </p> <p>This operation requires permissions for the following action on the file system:</p> <ul> <li> <p> <code>elasticfilesystem:CreateMountTarget</code> </p> </li> </ul> <p>This operation also requires permissions for the following Amazon EC2 actions:</p> <ul> <li> <p> <code>ec2:DescribeSubnets</code> </p> </li> <li> <p> <code>ec2:DescribeNetworkInterfaces</code> </p> </li> <li> <p> <code>ec2:CreateNetworkInterface</code> </p> </li> </ul>

        Args:
            file_system_id: <p>The ID of the file system for which to create the mount target.</p>
            subnet_id: <p>The ID of the subnet to add the mount target in. For One Zone file systems, use the subnet that is associated with the file system's Availability Zone.</p>
            ip_address: <p>If the IP address type for the mount target is IPv4, then specify the IPv4 address within the address range of the specified subnet.</p>
            ipv6_address: <p>If the IP address type for the mount target is IPv6, then specify the IPv6 address within the address range of the specified subnet.</p>
            ip_address_type: <p>Specify the type of IP address of the mount target you are creating. Options are IPv4, dual stack, or IPv6. If you don’t specify an IpAddressType, then IPv4 is used.</p> <ul> <li> <p>IPV4_ONLY – Create mount target with IPv4 only subnet or dual-stack subnet.</p> </li> <li> <p>DUAL_STACK – Create mount target with dual-stack subnet.</p> </li> <li> <p>IPV6_ONLY – Create mount target with IPv6 only subnet.</p> </li> </ul> <note> <p>Creating IPv6 mount target only ENI in dual-stack subnet is not supported.</p> </note>
            security_groups: <p>VPC security group IDs, of the form <code>sg-xxxxxxxx</code>. These must be for the same VPC as the subnet specified. The maximum number of security groups depends on account quota. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html">Amazon VPC Quotas</a> in the <i>Amazon VPC User Guide</i> (see the <b>Security Groups</b> table). </p>

        Raises:
            capo_efs.errors.availability_zones_mismatch.AvailabilityZonesMismatch: <p>Returned if the Availability Zone that was specified for a mount target is different from the Availability Zone that was specified for One Zone storage. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/availability-durability.html">Regional and One Zone storage redundancy</a>.</p>
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.incorrect_file_system_life_cycle_state.IncorrectFileSystemLifeCycleState: <p>Returned if the file system's lifecycle state is not "available".</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.ip_address_in_use.IpAddressInUse: <p>Returned if the request specified an <code>IpAddress</code> that is already in use in the subnet.</p>
            capo_efs.errors.mount_target_conflict.MountTargetConflict: <p>Returned if the mount target would violate one of the specified restrictions based on the file system's existing mount targets.</p>
            capo_efs.errors.network_interface_limit_exceeded.NetworkInterfaceLimitExceeded: <p>The calling account has reached the limit for elastic network interfaces for the specific Amazon Web Services Region. Either delete some network interfaces or request that the account quota be raised. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html">Amazon VPC Quotas</a> in the <i>Amazon VPC User Guide</i> (see the <b>Network interfaces per Region</b> entry in the <b>Network interfaces</b> table). </p>
            capo_efs.errors.no_free_addresses_in_subnet.NoFreeAddressesInSubnet: <p>Returned if <code>IpAddress</code> was not specified in the request and there are no free IP addresses in the subnet.</p>
            capo_efs.errors.security_group_limit_exceeded.SecurityGroupLimitExceeded: <p>Returned if the number of <code>SecurityGroups</code> specified in the request is greater than the limit, which is based on account quota. Either delete some security groups or request that the account quota be raised. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html">Amazon VPC Quotas</a> in the <i>Amazon VPC User Guide</i> (see the <b>Security Groups</b> table). </p>
            capo_efs.errors.security_group_not_found.SecurityGroupNotFound: <p>Returned if one of the specified security groups doesn't exist in the subnet's virtual private cloud (VPC).</p>
            capo_efs.errors.subnet_not_found.SubnetNotFound: <p>Returned if there is no subnet with ID <code>SubnetId</code> provided in the request.</p>
            capo_efs.errors.unsupported_availability_zone.UnsupportedAvailabilityZone: <p>Returned if the requested Amazon EFS functionality is not available in the specified Availability Zone.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new mount target
            This operation creates a new mount target for an EFS file system.

            >>> await client.create_mount_target(file_system_id='fs-01234567', subnet_id='subnet-1234abcd')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.create_mount_target_request.CreateMountTargetRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.mount_target_description.MountTargetDescription"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.create_mount_target

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.create_mount_target.async_create_mount_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.create_mount_target_request.CreateMountTargetRequest = {
            "file_system_id": file_system_id,
            "subnet_id": subnet_id,
        }
        if ip_address is not None:
            input_["ip_address"] = ip_address
        if ipv6_address is not None:
            input_["ipv6_address"] = ipv6_address
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if security_groups is not None:
            input_["security_groups"] = security_groups

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_replication_configuration(
        self,
        source_file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        destinations: "capo_efs.types.destinations_to_create.DestinationsToCreate",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> "capo_efs.types.replication_configuration_description.ReplicationConfigurationDescription":
        """<p>Creates a replication conﬁguration to either a new or existing EFS file system. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/efs-replication.html">Amazon EFS replication</a> in the <i>Amazon EFS User Guide</i>. The replication configuration specifies the following:</p> <ul> <li> <p> <b>Source file system</b> – The EFS file system that you want to replicate. </p> </li> <li> <p> <b>Destination file system</b> – The destination file system to which the source file system is replicated. There can only be one destination file system in a replication configuration. </p> <note> <p>A file system can be part of only one replication configuration. </p> </note> <p>The destination parameters for the replication configuration depend on whether you are replicating to a new file system or to an existing file system, and if you are replicating across Amazon Web Services accounts. See <a>DestinationToCreate</a> for more information.</p> </li> </ul> <p>This operation requires permissions for the <code>elasticfilesystem:CreateReplicationConfiguration</code> action. Additionally, other permissions are required depending on how you are replicating file systems. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/efs-replication.html#efs-replication-permissions">Required permissions for replication</a> in the <i>Amazon EFS User Guide</i>.</p>

        Args:
            source_file_system_id: <p>Specifies the Amazon EFS file system that you want to replicate. This file system cannot already be a source or destination file system in another replication configuration.</p>
            destinations: <p>An array of destination configuration objects. Only one destination configuration object is supported.</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.conflict_exception.ConflictException: <p>Returned if the source file system in a replication is encrypted but the destination file system is unencrypted.</p>
            capo_efs.errors.file_system_limit_exceeded.FileSystemLimitExceeded: <p>Returned if the Amazon Web Services account has already created the maximum number of file systems allowed per account.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.incorrect_file_system_life_cycle_state.IncorrectFileSystemLifeCycleState: <p>Returned if the file system's lifecycle state is not "available".</p>
            capo_efs.errors.insufficient_throughput_capacity.InsufficientThroughputCapacity: <p>Returned if there's not enough capacity to provision additional throughput. This value might be returned when you try to create a file system in provisioned throughput mode, when you attempt to increase the provisioned throughput of an existing file system, or when you attempt to change an existing file system from Bursting Throughput to Provisioned Throughput mode. Try again later.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.replication_not_found.ReplicationNotFound: <p>Returned if the specified file system does not have a replication configuration.</p>
            capo_efs.errors.throughput_limit_exceeded.ThroughputLimitExceeded: <p>Returned if the throughput mode or amount of provisioned throughput can't be changed because the throughput limit of 1024 MiB/s has been reached.</p>
            capo_efs.errors.unsupported_availability_zone.UnsupportedAvailabilityZone: <p>Returned if the requested Amazon EFS functionality is not available in the specified Availability Zone.</p>
            capo_efs.errors.validation_exception.ValidationException: <p>Returned if the Backup service is not available in the Amazon Web Services Region in which the request was made.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.create_replication_configuration_request.CreateReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.replication_configuration_description.ReplicationConfigurationDescription"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.create_replication_configuration

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.create_replication_configuration.async_create_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.create_replication_configuration_request.CreateReplicationConfigurationRequest = {
            "source_file_system_id": source_file_system_id,
            "destinations": destinations,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_tags(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        tags: "capo_efs.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> None:
        """<note> <p>DEPRECATED - <code>CreateTags</code> is deprecated and not maintained. To create tags for EFS resources, use the API action.</p> </note> <p>Creates or overwrites tags associated with a file system. Each tag is a key-value pair. If a tag key specified in the request already exists on the file system, this operation overwrites its value with the value provided in the request. If you add the <code>Name</code> tag to your file system, Amazon EFS returns it in the response to the <a>DescribeFileSystems</a> operation. </p> <p>This operation requires permission for the <code>elasticfilesystem:CreateTags</code> action.</p>

        Args:
            file_system_id: <p>The ID of the file system whose tags you want to modify (String). This operation modifies the tags only, not the file system.</p>
            tags: <p>An array of <code>Tag</code> objects to add. Each <code>Tag</code> object is a key-value pair. </p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new tag
            This operation creates a new tag for an EFS file system.

            >>> await client.create_tags(file_system_id='fs-01234567', tags=[{'Key': 'Name', 'Value': 'MyFileSystem'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.create_tags_request.CreateTagsRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_efs._operations.magnolio_api_service_v20150201.create_tags

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.create_tags.async_create_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.create_tags_request.CreateTagsRequest = {
            "file_system_id": file_system_id,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_access_point(
        self,
        access_point_id: "capo_efs.types.access_point_id.AccessPointId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified access point. After deletion is complete, new clients can no longer connect to the access points. Clients connected to the access point at the time of deletion will continue to function until they terminate their connection.</p> <p>This operation requires permissions for the <code>elasticfilesystem:DeleteAccessPoint</code> action.</p>

        Args:
            access_point_id: <p>The ID of the access point that you want to delete.</p>

        Raises:
            capo_efs.errors.access_point_not_found.AccessPointNotFound: <p>Returned if the specified <code>AccessPointId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.delete_access_point_request.DeleteAccessPointRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_efs._operations.magnolio_api_service_v20150201.delete_access_point

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.delete_access_point.async_delete_access_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.delete_access_point_request.DeleteAccessPointRequest = {
            "access_point_id": access_point_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_file_system(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> None:
        """<p>Deletes a file system, permanently severing access to its contents. Upon return, the file system no longer exists and you can't access any contents of the deleted file system.</p> <p>You need to manually delete mount targets attached to a file system before you can delete an EFS file system. This step is performed for you when you use the Amazon Web Services console to delete a file system.</p> <note> <p>You cannot delete a file system that is part of an EFS replication configuration. You need to delete the replication configuration first.</p> </note> <p> You can't delete a file system that is in use. That is, if the file system has any mount targets, you must first delete them. For more information, see <a>DescribeMountTargets</a> and <a>DeleteMountTarget</a>. </p> <note> <p>The <code>DeleteFileSystem</code> call returns while the file system state is still <code>deleting</code>. You can check the file system deletion status by calling the <a>DescribeFileSystems</a> operation, which returns a list of file systems in your account. If you pass file system ID or creation token for the deleted file system, the <a>DescribeFileSystems</a> returns a <code>404 FileSystemNotFound</code> error.</p> </note> <p>This operation requires permissions for the <code>elasticfilesystem:DeleteFileSystem</code> action.</p>

        Args:
            file_system_id: <p>The ID of the file system you want to delete.</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_in_use.FileSystemInUse: <p>Returned if a file system has mount targets.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a file system
            This operation deletes an EFS file system.

            >>> await client.delete_file_system(file_system_id='fs-01234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.delete_file_system_request.DeleteFileSystemRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_efs._operations.magnolio_api_service_v20150201.delete_file_system

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.delete_file_system.async_delete_file_system(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.delete_file_system_request.DeleteFileSystemRequest = {
            "file_system_id": file_system_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_file_system_policy(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> None:
        """<p>Deletes the <code>FileSystemPolicy</code> for the specified file system. The default <code>FileSystemPolicy</code> goes into effect once the existing policy is deleted. For more information about the default file system policy, see <a href="https://docs.aws.amazon.com/efs/latest/ug/res-based-policies-efs.html">Using Resource-based Policies with EFS</a>.</p> <p>This operation requires permissions for the <code>elasticfilesystem:DeleteFileSystemPolicy</code> action.</p>

        Args:
            file_system_id: <p>Specifies the EFS file system for which to delete the <code>FileSystemPolicy</code>.</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.incorrect_file_system_life_cycle_state.IncorrectFileSystemLifeCycleState: <p>Returned if the file system's lifecycle state is not "available".</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.delete_file_system_policy_request.DeleteFileSystemPolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_efs._operations.magnolio_api_service_v20150201.delete_file_system_policy

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.delete_file_system_policy.async_delete_file_system_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.delete_file_system_policy_request.DeleteFileSystemPolicyRequest = {
            "file_system_id": file_system_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_mount_target(
        self,
        mount_target_id: "capo_efs.types.mount_target_id.MountTargetId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified mount target.</p> <p>This operation forcibly breaks any mounts of the file system by using the mount target that is being deleted, which might disrupt instances or applications using those mounts. To avoid applications getting cut off abruptly, you might consider unmounting any mounts of the mount target, if feasible. The operation also deletes the associated network interface. Uncommitted writes might be lost, but breaking a mount target using this operation does not corrupt the file system itself. The file system you created remains. You can mount an EC2 instance in your VPC by using another mount target.</p> <p>This operation requires permissions for the following action on the file system:</p> <ul> <li> <p> <code>elasticfilesystem:DeleteMountTarget</code> </p> </li> </ul> <note> <p>The <code>DeleteMountTarget</code> call returns while the mount target state is still <code>deleting</code>. You can check the mount target deletion by calling the <a>DescribeMountTargets</a> operation, which returns a list of mount target descriptions for the given file system. </p> </note> <p>The operation also requires permissions for the following Amazon EC2 action on the mount target's network interface:</p> <ul> <li> <p> <code>ec2:DeleteNetworkInterface</code> </p> </li> </ul>

        Args:
            mount_target_id: <p>The ID of the mount target to delete (String).</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.dependency_timeout.DependencyTimeout: <p>The service timed out trying to fulfill the request, and the client should try the call again.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.mount_target_not_found.MountTargetNotFound: <p>Returned if there is no mount target with the specified ID found in the caller's Amazon Web Services account.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a mount target
            This operation deletes a mount target.

            >>> await client.delete_mount_target(mount_target_id='fsmt-12340abc')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.delete_mount_target_request.DeleteMountTargetRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_efs._operations.magnolio_api_service_v20150201.delete_mount_target

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.delete_mount_target.async_delete_mount_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.delete_mount_target_request.DeleteMountTargetRequest = {
            "mount_target_id": mount_target_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_replication_configuration(
        self,
        source_file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        deletion_mode: Optional["capo_efs.types.deletion_mode.DeletionMode"] = None,
    ) -> None:
        """<p>Deletes a replication configuration. Deleting a replication configuration ends the replication process. After a replication configuration is deleted, the destination file system becomes <code>Writeable</code> and its replication overwrite protection is re-enabled. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/delete-replications.html">Delete a replication configuration</a>.</p> <p>This operation requires permissions for the <code>elasticfilesystem:DeleteReplicationConfiguration</code> action. </p>

        Args:
            source_file_system_id: <p>The ID of the source file system in the replication configuration.</p>
            deletion_mode: <p>When replicating across Amazon Web Services accounts or across Amazon Web Services Regions, Amazon EFS deletes the replication configuration from both the source and destination account or Region (<code>ALL_CONFIGURATIONS</code>) by default. If there's a configuration or permissions issue that prevents Amazon EFS from deleting the replication configuration from both sides, you can use the <code>LOCAL_CONFIGURATION_ONLY</code> mode to delete the replication configuration from only the local side (the account or Region from which the delete is performed). </p> <note> <p>Only use the <code>LOCAL_CONFIGURATION_ONLY</code> mode in the case that Amazon EFS is unable to delete the replication configuration in both the source and destination account or Region. Deleting the local configuration leaves the configuration in the other account or Region unrecoverable.</p> <p>Additionally, do not use this mode for same-account, same-region replication as doing so results in a BadRequest exception error.</p> </note>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.replication_not_found.ReplicationNotFound: <p>Returned if the specified file system does not have a replication configuration.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.delete_replication_configuration_request.DeleteReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_efs._operations.magnolio_api_service_v20150201.delete_replication_configuration

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.delete_replication_configuration.async_delete_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.delete_replication_configuration_request.DeleteReplicationConfigurationRequest = {
            "source_file_system_id": source_file_system_id
        }
        if deletion_mode is not None:
            input_["deletion_mode"] = deletion_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_tags(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        tag_keys: "capo_efs.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> None:
        """<note> <p>DEPRECATED - <code>DeleteTags</code> is deprecated and not maintained. To remove tags from EFS resources, use the API action.</p> </note> <p>Deletes the specified tags from a file system. If the <code>DeleteTags</code> request includes a tag key that doesn't exist, Amazon EFS ignores it and doesn't cause an error. For more information about tags and related restrictions, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html">Tag restrictions</a> in the <i>Billing and Cost Management User Guide</i>.</p> <p>This operation requires permissions for the <code>elasticfilesystem:DeleteTags</code> action.</p>

        Args:
            file_system_id: <p>The ID of the file system whose tags you want to delete (String).</p>
            tag_keys: <p>A list of tag keys to delete.</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete tags for an EFS file system
            This operation deletes tags for an EFS file system.

            >>> await client.delete_tags(file_system_id='fs-01234567', tag_keys=['Name'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.delete_tags_request.DeleteTagsRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_efs._operations.magnolio_api_service_v20150201.delete_tags

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.delete_tags.async_delete_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.delete_tags_request.DeleteTagsRequest = {
            "file_system_id": file_system_id,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_access_points(
        self,
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        max_results: Optional["capo_efs.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_efs.types.token.Token"] = None,
        access_point_id: Optional[
            "capo_efs.types.access_point_id.AccessPointId"
        ] = None,
        file_system_id: Optional["capo_efs.types.file_system_id.FileSystemId"] = None,
    ) -> "capo_efs.types.describe_access_points_response.DescribeAccessPointsResponse":
        """<p>Returns the description of a specific Amazon EFS access point if the <code>AccessPointId</code> is provided. If you provide an EFS <code>FileSystemId</code>, it returns descriptions of all access points for that file system. You can provide either an <code>AccessPointId</code> or a <code>FileSystemId</code> in the request, but not both. </p> <p>This operation requires permissions for the <code>elasticfilesystem:DescribeAccessPoints</code> action.</p>

        Args:
            max_results: <p>(Optional) When retrieving all access points for a file system, you can optionally specify the <code>MaxItems</code> parameter to limit the number of objects returned in a response. The default value is 100. </p>
            next_token: <p> <code>NextToken</code> is present if the response is paginated. You can use <code>NextMarker</code> in the subsequent request to fetch the next page of access point descriptions.</p>
            access_point_id: <p>(Optional) Specifies an EFS access point to describe in the response; mutually exclusive with <code>FileSystemId</code>.</p>
            file_system_id: <p>(Optional) If you provide a <code>FileSystemId</code>, EFS returns all access points for that file system; mutually exclusive with <code>AccessPointId</code>.</p>

        Raises:
            capo_efs.errors.access_point_not_found.AccessPointNotFound: <p>Returned if the specified <code>AccessPointId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.describe_access_points_request.DescribeAccessPointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.describe_access_points_response.DescribeAccessPointsResponse"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.describe_access_points

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.describe_access_points.async_describe_access_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.describe_access_points_request.DescribeAccessPointsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if access_point_id is not None:
            input_["access_point_id"] = access_point_id
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_access_points(
        self,
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        max_results: Optional["capo_efs.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_efs.types.token.Token"] = None,
        access_point_id: Optional[
            "capo_efs.types.access_point_id.AccessPointId"
        ] = None,
        file_system_id: Optional["capo_efs.types.file_system_id.FileSystemId"] = None,
    ) -> (
        "AsyncIterator[capo_efs.types.access_point_description.AccessPointDescription]"
    ):
        _token = next_token
        while True:
            _response = await self.describe_access_points(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                access_point_id=access_point_id,
                file_system_id=file_system_id,
            )
            _page = _resolve_path(_response, ("access_points",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_account_preferences(
        self,
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        next_token: Optional["capo_efs.types.token.Token"] = None,
        max_results: Optional["capo_efs.types.max_results.MaxResults"] = None,
    ) -> "capo_efs.types.describe_account_preferences_response.DescribeAccountPreferencesResponse":
        """<p>Returns the account preferences settings for the Amazon Web Services account associated with the user making the request, in the current Amazon Web Services Region.</p>

        Args:
            next_token: <p>(Optional) You can use <code>NextToken</code> in a subsequent request to fetch the next page of Amazon Web Services account preferences if the response payload was paginated.</p>
            max_results: <p>(Optional) When retrieving account preferences, you can optionally specify the <code>MaxItems</code> parameter to limit the number of objects returned in a response. The default value is 100. </p>

        Raises:
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.describe_account_preferences_request.DescribeAccountPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.describe_account_preferences_response.DescribeAccountPreferencesResponse"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.describe_account_preferences

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.describe_account_preferences.async_describe_account_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.describe_account_preferences_request.DescribeAccountPreferencesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_backup_policy(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> "capo_efs.types.backup_policy_description.BackupPolicyDescription":
        """<p>Returns the backup policy for the specified EFS file system.</p>

        Args:
            file_system_id: <p>Specifies which EFS file system for which to retrieve the <code>BackupPolicy</code>.</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.policy_not_found.PolicyNotFound: <p>Returned if <code>no backup</code> is specified for a One Zone EFS file system.</p>
            capo_efs.errors.validation_exception.ValidationException: <p>Returned if the Backup service is not available in the Amazon Web Services Region in which the request was made.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.describe_backup_policy_request.DescribeBackupPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.backup_policy_description.BackupPolicyDescription"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.describe_backup_policy

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.describe_backup_policy.async_describe_backup_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.describe_backup_policy_request.DescribeBackupPolicyRequest = {
            "file_system_id": file_system_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_file_system_policy(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> "capo_efs.types.file_system_policy_description.FileSystemPolicyDescription":
        """<p>Returns the <code>FileSystemPolicy</code> for the specified EFS file system.</p> <p>This operation requires permissions for the <code>elasticfilesystem:DescribeFileSystemPolicy</code> action.</p>

        Args:
            file_system_id: <p>Specifies which EFS file system to retrieve the <code>FileSystemPolicy</code> for.</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.policy_not_found.PolicyNotFound: <p>Returned if <code>no backup</code> is specified for a One Zone EFS file system.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.describe_file_system_policy_request.DescribeFileSystemPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.file_system_policy_description.FileSystemPolicyDescription"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.describe_file_system_policy

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.describe_file_system_policy.async_describe_file_system_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.describe_file_system_policy_request.DescribeFileSystemPolicyRequest = {
            "file_system_id": file_system_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_file_systems(
        self,
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        max_items: Optional["capo_efs.types.max_items.MaxItems"] = None,
        marker: Optional["capo_efs.types.marker.Marker"] = None,
        creation_token: Optional["capo_efs.types.creation_token.CreationToken"] = None,
        file_system_id: Optional["capo_efs.types.file_system_id.FileSystemId"] = None,
    ) -> "capo_efs.types.describe_file_systems_response.DescribeFileSystemsResponse":
        """<p>Returns the description of a specific Amazon EFS file system if either the file system <code>CreationToken</code> or the <code>FileSystemId</code> is provided. Otherwise, it returns descriptions of all file systems owned by the caller's Amazon Web Services account in the Amazon Web Services Region of the endpoint that you're calling.</p> <p>When retrieving all file system descriptions, you can optionally specify the <code>MaxItems</code> parameter to limit the number of descriptions in a response. This number is automatically set to 100. If more file system descriptions remain, Amazon EFS returns a <code>NextMarker</code>, an opaque token, in the response. In this case, you should send a subsequent request with the <code>Marker</code> request parameter set to the value of <code>NextMarker</code>. </p> <p>To retrieve a list of your file system descriptions, this operation is used in an iterative process, where <code>DescribeFileSystems</code> is called first without the <code>Marker</code> and then the operation continues to call it with the <code>Marker</code> parameter set to the value of the <code>NextMarker</code> from the previous response until the response has no <code>NextMarker</code>. </p> <p> The order of file systems returned in the response of one <code>DescribeFileSystems</code> call and the order of file systems returned across the responses of a multi-call iteration is unspecified. </p> <p> This operation requires permissions for the <code>elasticfilesystem:DescribeFileSystems</code> action. </p>

        Args:
            max_items: <p>(Optional) Specifies the maximum number of file systems to return in the response (integer). This number is automatically set to 100. The response is paginated at 100 per page if you have more than 100 file systems. </p>
            marker: <p>(Optional) Opaque pagination token returned from a previous <code>DescribeFileSystems</code> operation (String). If present, specifies to continue the list from where the returning call had left off. </p>
            creation_token: <p>(Optional) Restricts the list to the file system with this creation token (String). You specify a creation token when you create an Amazon EFS file system.</p>
            file_system_id: <p>(Optional) ID of the file system whose description you want to retrieve (String).</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.describe_file_systems_request.DescribeFileSystemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.describe_file_systems_response.DescribeFileSystemsResponse"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.describe_file_systems

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.describe_file_systems.async_describe_file_systems(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.describe_file_systems_request.DescribeFileSystemsRequest = {}
        if max_items is not None:
            input_["max_items"] = max_items
        if marker is not None:
            input_["marker"] = marker
        if creation_token is not None:
            input_["creation_token"] = creation_token
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_file_systems(
        self,
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        max_items: Optional["capo_efs.types.max_items.MaxItems"] = None,
        marker: Optional["capo_efs.types.marker.Marker"] = None,
        creation_token: Optional["capo_efs.types.creation_token.CreationToken"] = None,
        file_system_id: Optional["capo_efs.types.file_system_id.FileSystemId"] = None,
    ) -> "AsyncIterator[capo_efs.types.file_system_description.FileSystemDescription]":
        _token = marker
        while True:
            _response = await self.describe_file_systems(
                config_overrides=config_overrides,
                max_items=max_items,
                marker=_token,
                creation_token=creation_token,
                file_system_id=file_system_id,
            )
            _page = _resolve_path(_response, ("file_systems",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    async def describe_lifecycle_configuration(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> "capo_efs.types.lifecycle_configuration_description.LifecycleConfigurationDescription":
        """<p>Returns the current <code>LifecycleConfiguration</code> object for the specified EFS file system. Lifecycle management uses the <code>LifecycleConfiguration</code> object to identify when to move files between storage classes. For a file system without a <code>LifecycleConfiguration</code> object, the call returns an empty array in the response.</p> <p>This operation requires permissions for the <code>elasticfilesystem:DescribeLifecycleConfiguration</code> operation.</p>

        Args:
            file_system_id: <p>The ID of the file system whose <code>LifecycleConfiguration</code> object you want to retrieve (String).</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the lifecycle configuration for a file system
            This operation describes a file system's LifecycleConfiguration. EFS lifecycle management uses the LifecycleConfiguration object to identify which files to move to the EFS Infrequent Access (IA) storage class.

            >>> await client.describe_lifecycle_configuration(file_system_id='fs-01234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.describe_lifecycle_configuration_request.DescribeLifecycleConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.lifecycle_configuration_description.LifecycleConfigurationDescription"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.describe_lifecycle_configuration

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.describe_lifecycle_configuration.async_describe_lifecycle_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.describe_lifecycle_configuration_request.DescribeLifecycleConfigurationRequest = {
            "file_system_id": file_system_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_mount_targets(
        self,
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        max_items: Optional["capo_efs.types.max_items.MaxItems"] = None,
        marker: Optional["capo_efs.types.marker.Marker"] = None,
        file_system_id: Optional["capo_efs.types.file_system_id.FileSystemId"] = None,
        mount_target_id: Optional[
            "capo_efs.types.mount_target_id.MountTargetId"
        ] = None,
        access_point_id: Optional[
            "capo_efs.types.access_point_id.AccessPointId"
        ] = None,
    ) -> "capo_efs.types.describe_mount_targets_response.DescribeMountTargetsResponse":
        """<p>Returns the descriptions of all the current mount targets, or a specific mount target, for a file system. When requesting all of the current mount targets, the order of mount targets returned in the response is unspecified.</p> <p>This operation requires permissions for the <code>elasticfilesystem:DescribeMountTargets</code> action, on either the file system ID that you specify in <code>FileSystemId</code>, or on the file system of the mount target that you specify in <code>MountTargetId</code>.</p>

        Args:
            max_items: <p>(Optional) Maximum number of mount targets to return in the response. Currently, this number is automatically set to 10, and other values are ignored. The response is paginated at 100 per page if you have more than 100 mount targets.</p>
            marker: <p>(Optional) Opaque pagination token returned from a previous <code>DescribeMountTargets</code> operation (String). If present, it specifies to continue the list from where the previous returning call left off.</p>
            file_system_id: <p>(Optional) ID of the file system whose mount targets you want to list (String). It must be included in your request if an <code>AccessPointId</code> or <code>MountTargetId</code> is not included. Accepts either a file system ID or ARN as input.</p>
            mount_target_id: <p>(Optional) ID of the mount target that you want to have described (String). It must be included in your request if <code>FileSystemId</code> is not included. Accepts either a mount target ID or ARN as input.</p>
            access_point_id: <p>(Optional) The ID of the access point whose mount targets that you want to list. It must be included in your request if a <code>FileSystemId</code> or <code>MountTargetId</code> is not included in your request. Accepts either an access point ID or ARN as input.</p>

        Raises:
            capo_efs.errors.access_point_not_found.AccessPointNotFound: <p>Returned if the specified <code>AccessPointId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.mount_target_not_found.MountTargetNotFound: <p>Returned if there is no mount target with the specified ID found in the caller's Amazon Web Services account.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the mount targets for a file system
            This operation describes all of a file system's mount targets.

            >>> await client.describe_mount_targets(file_system_id='fs-01234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.describe_mount_targets_request.DescribeMountTargetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.describe_mount_targets_response.DescribeMountTargetsResponse"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.describe_mount_targets

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.describe_mount_targets.async_describe_mount_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.describe_mount_targets_request.DescribeMountTargetsRequest = {}
        if max_items is not None:
            input_["max_items"] = max_items
        if marker is not None:
            input_["marker"] = marker
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id
        if mount_target_id is not None:
            input_["mount_target_id"] = mount_target_id
        if access_point_id is not None:
            input_["access_point_id"] = access_point_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_mount_targets(
        self,
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        max_items: Optional["capo_efs.types.max_items.MaxItems"] = None,
        marker: Optional["capo_efs.types.marker.Marker"] = None,
        file_system_id: Optional["capo_efs.types.file_system_id.FileSystemId"] = None,
        mount_target_id: Optional[
            "capo_efs.types.mount_target_id.MountTargetId"
        ] = None,
        access_point_id: Optional[
            "capo_efs.types.access_point_id.AccessPointId"
        ] = None,
    ) -> (
        "AsyncIterator[capo_efs.types.mount_target_description.MountTargetDescription]"
    ):
        _token = marker
        while True:
            _response = await self.describe_mount_targets(
                config_overrides=config_overrides,
                max_items=max_items,
                marker=_token,
                file_system_id=file_system_id,
                mount_target_id=mount_target_id,
                access_point_id=access_point_id,
            )
            _page = _resolve_path(_response, ("mount_targets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    async def describe_mount_target_security_groups(
        self,
        mount_target_id: "capo_efs.types.mount_target_id.MountTargetId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> "capo_efs.types.describe_mount_target_security_groups_response.DescribeMountTargetSecurityGroupsResponse":
        """<p>Returns the security groups currently in effect for a mount target. This operation requires that the network interface of the mount target has been created and the lifecycle state of the mount target is not <code>deleted</code>.</p> <p>This operation requires permissions for the following actions:</p> <ul> <li> <p> <code>elasticfilesystem:DescribeMountTargetSecurityGroups</code> action on the mount target's file system. </p> </li> <li> <p> <code>ec2:DescribeNetworkInterfaceAttribute</code> action on the mount target's network interface. </p> </li> </ul>

        Args:
            mount_target_id: <p>The ID of the mount target whose security groups you want to retrieve.</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.incorrect_mount_target_state.IncorrectMountTargetState: <p>Returned if the mount target is not in the correct state for the operation.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.mount_target_not_found.MountTargetNotFound: <p>Returned if there is no mount target with the specified ID found in the caller's Amazon Web Services account.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the security groups for a mount target
            This operation describes all of the security groups for a file system's mount target.

            >>> await client.describe_mount_target_security_groups(mount_target_id='fsmt-12340abc')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.describe_mount_target_security_groups_request.DescribeMountTargetSecurityGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.describe_mount_target_security_groups_response.DescribeMountTargetSecurityGroupsResponse"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.describe_mount_target_security_groups

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.describe_mount_target_security_groups.async_describe_mount_target_security_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.describe_mount_target_security_groups_request.DescribeMountTargetSecurityGroupsRequest = {
            "mount_target_id": mount_target_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_replication_configurations(
        self,
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        file_system_id: Optional["capo_efs.types.file_system_id.FileSystemId"] = None,
        next_token: Optional["capo_efs.types.token.Token"] = None,
        max_results: Optional["capo_efs.types.max_results.MaxResults"] = None,
    ) -> "capo_efs.types.describe_replication_configurations_response.DescribeReplicationConfigurationsResponse":
        """<p>Retrieves the replication configuration for a specific file system. If a file system is not specified, all of the replication configurations for the Amazon Web Services account in an Amazon Web Services Region are retrieved.</p>

        Args:
            file_system_id: <p>You can retrieve the replication configuration for a specific file system by providing its file system ID. For cross-account,cross-region replication, an account can only describe the replication configuration for a file system in its own Region.</p>
            next_token: <p> <code>NextToken</code> is present if the response is paginated. You can use <code>NextToken</code> in a subsequent request to fetch the next page of output.</p>
            max_results: <p>(Optional) To limit the number of objects returned in a response, you can specify the <code>MaxItems</code> parameter. The default value is 100. </p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.replication_not_found.ReplicationNotFound: <p>Returned if the specified file system does not have a replication configuration.</p>
            capo_efs.errors.validation_exception.ValidationException: <p>Returned if the Backup service is not available in the Amazon Web Services Region in which the request was made.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.describe_replication_configurations_request.DescribeReplicationConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.describe_replication_configurations_response.DescribeReplicationConfigurationsResponse"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.describe_replication_configurations

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.describe_replication_configurations.async_describe_replication_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.describe_replication_configurations_request.DescribeReplicationConfigurationsRequest = {}
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_replication_configurations(
        self,
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        file_system_id: Optional["capo_efs.types.file_system_id.FileSystemId"] = None,
        next_token: Optional["capo_efs.types.token.Token"] = None,
        max_results: Optional["capo_efs.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_efs.types.replication_configuration_description.ReplicationConfigurationDescription]":
        _token = next_token
        while True:
            _response = await self.describe_replication_configurations(
                config_overrides=config_overrides,
                file_system_id=file_system_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("replications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_tags(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        max_items: Optional["capo_efs.types.max_items.MaxItems"] = None,
        marker: Optional["capo_efs.types.marker.Marker"] = None,
    ) -> "capo_efs.types.describe_tags_response.DescribeTagsResponse":
        """<note> <p>DEPRECATED - The <code>DescribeTags</code> action is deprecated and not maintained. To view tags associated with EFS resources, use the <code>ListTagsForResource</code> API action.</p> </note> <p>Returns the tags associated with a file system. The order of tags returned in the response of one <code>DescribeTags</code> call and the order of tags returned across the responses of a multiple-call iteration (when using pagination) is unspecified. </p> <p> This operation requires permissions for the <code>elasticfilesystem:DescribeTags</code> action. </p>

        Args:
            max_items: <p>(Optional) The maximum number of file system tags to return in the response. Currently, this number is automatically set to 100, and other values are ignored. The response is paginated at 100 per page if you have more than 100 tags.</p>
            marker: <p>(Optional) An opaque pagination token returned from a previous <code>DescribeTags</code> operation (String). If present, it specifies to continue the list from where the previous call left off.</p>
            file_system_id: <p>The ID of the file system whose tag set you want to retrieve.</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the tags for a file system
            This operation describes all of a file system's tags.

            >>> await client.describe_tags(file_system_id='fs-01234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.describe_tags_request.DescribeTagsRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.describe_tags_response.DescribeTagsResponse"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.describe_tags

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.describe_tags.async_describe_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.describe_tags_request.DescribeTagsRequest = {
            "file_system_id": file_system_id
        }
        if max_items is not None:
            input_["max_items"] = max_items
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_tags(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        max_items: Optional["capo_efs.types.max_items.MaxItems"] = None,
        marker: Optional["capo_efs.types.marker.Marker"] = None,
    ) -> "AsyncIterator[capo_efs.types.tag.Tag]":
        _token = marker
        while True:
            _response = await self.describe_tags(
                file_system_id,
                config_overrides=config_overrides,
                max_items=max_items,
                marker=_token,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_id: "capo_efs.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        max_results: Optional["capo_efs.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_efs.types.token.Token"] = None,
    ) -> "capo_efs.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags for a top-level EFS resource. You must provide the ID of the resource that you want to retrieve the tags for.</p> <p>This operation requires permissions for the <code>elasticfilesystem:DescribeAccessPoints</code> action.</p>

        Args:
            resource_id: <p>Specifies the EFS resource you want to retrieve tags for. You can retrieve tags for EFS file systems and access points using this API endpoint.</p>
            max_results: <p>(Optional) Specifies the maximum number of tag objects to return in the response. The default value is 100.</p>
            next_token: <p>(Optional) You can use <code>NextToken</code> in a subsequent request to fetch the next page of access point descriptions if the response payload was paginated.</p>

        Raises:
            capo_efs.errors.access_point_not_found.AccessPointNotFound: <p>Returned if the specified <code>AccessPointId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_id": resource_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_tags_for_resource(
        self,
        resource_id: "capo_efs.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        max_results: Optional["capo_efs.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_efs.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_efs.types.list_tags_for_resource_response.ListTagsForResourceResponse]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                resource_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def modify_mount_target_security_groups(
        self,
        mount_target_id: "capo_efs.types.mount_target_id.MountTargetId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        security_groups: Optional[
            "capo_efs.types.security_groups.SecurityGroups"
        ] = None,
    ) -> None:
        """<p>Modifies the set of security groups in effect for a mount target.</p> <p>When you create a mount target, Amazon EFS also creates a new network interface. For more information, see <a>CreateMountTarget</a>. This operation replaces the security groups in effect for the network interface associated with a mount target, with the <code>SecurityGroups</code> provided in the request. This operation requires that the network interface of the mount target has been created and the lifecycle state of the mount target is not <code>deleted</code>. </p> <p>The operation requires permissions for the following actions:</p> <ul> <li> <p> <code>elasticfilesystem:ModifyMountTargetSecurityGroups</code> action on the mount target's file system. </p> </li> <li> <p> <code>ec2:ModifyNetworkInterfaceAttribute</code> action on the mount target's network interface. </p> </li> </ul>

        Args:
            mount_target_id: <p>The ID of the mount target whose security groups you want to modify.</p>
            security_groups: <p>An array of VPC security group IDs. </p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.incorrect_mount_target_state.IncorrectMountTargetState: <p>Returned if the mount target is not in the correct state for the operation.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.mount_target_not_found.MountTargetNotFound: <p>Returned if there is no mount target with the specified ID found in the caller's Amazon Web Services account.</p>
            capo_efs.errors.security_group_limit_exceeded.SecurityGroupLimitExceeded: <p>Returned if the number of <code>SecurityGroups</code> specified in the request is greater than the limit, which is based on account quota. Either delete some security groups or request that the account quota be raised. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html">Amazon VPC Quotas</a> in the <i>Amazon VPC User Guide</i> (see the <b>Security Groups</b> table). </p>
            capo_efs.errors.security_group_not_found.SecurityGroupNotFound: <p>Returned if one of the specified security groups doesn't exist in the subnet's virtual private cloud (VPC).</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To modify the security groups associated with a mount target for a file system
            This operation modifies the security groups associated with a mount target for a file system.

            >>> await client.modify_mount_target_security_groups(mount_target_id='fsmt-12340abc', security_groups=['sg-abcd1234'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.modify_mount_target_security_groups_request.ModifyMountTargetSecurityGroupsRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_efs._operations.magnolio_api_service_v20150201.modify_mount_target_security_groups

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.modify_mount_target_security_groups.async_modify_mount_target_security_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.modify_mount_target_security_groups_request.ModifyMountTargetSecurityGroupsRequest = {
            "mount_target_id": mount_target_id
        }
        if security_groups is not None:
            input_["security_groups"] = security_groups

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_account_preferences(
        self,
        resource_id_type: "capo_efs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> (
        "capo_efs.types.put_account_preferences_response.PutAccountPreferencesResponse"
    ):
        """<p>Use this operation to set the account preference in the current Amazon Web Services Region to use long 17 character (63 bit) or short 8 character (32 bit) resource IDs for new EFS file system and mount target resources. All existing resource IDs are not affected by any changes you make. You can set the ID preference during the opt-in period as EFS transitions to long resource IDs. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/manage-efs-resource-ids.html">Managing Amazon EFS resource IDs</a>.</p> <note> <p>Starting in October, 2021, you will receive an error if you try to set the account preference to use the short 8 character format resource ID. Contact Amazon Web Services support if you receive an error and must use short IDs for file system and mount target resources.</p> </note>

        Args:
            resource_id_type: <p>Specifies the EFS resource ID preference to set for the user's Amazon Web Services account, in the current Amazon Web Services Region, either <code>LONG_ID</code> (17 characters), or <code>SHORT_ID</code> (8 characters).</p> <note> <p>Starting in October, 2021, you will receive an error when setting the account preference to <code>SHORT_ID</code>. Contact Amazon Web Services support if you receive an error and must use short IDs for file system and mount target resources.</p> </note>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.put_account_preferences_request.PutAccountPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.put_account_preferences_response.PutAccountPreferencesResponse"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.put_account_preferences

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.put_account_preferences.async_put_account_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.put_account_preferences_request.PutAccountPreferencesRequest = {
            "resource_id_type": resource_id_type
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_backup_policy(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        backup_policy: "capo_efs.types.backup_policy.BackupPolicy",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> "capo_efs.types.backup_policy_description.BackupPolicyDescription":
        """<p>Updates the file system's backup policy. Use this action to start or stop automatic backups of the file system. </p>

        Args:
            file_system_id: <p>Specifies which EFS file system to update the backup policy for.</p>
            backup_policy: <p>The backup policy included in the <code>PutBackupPolicy</code> request.</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.incorrect_file_system_life_cycle_state.IncorrectFileSystemLifeCycleState: <p>Returned if the file system's lifecycle state is not "available".</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.validation_exception.ValidationException: <p>Returned if the Backup service is not available in the Amazon Web Services Region in which the request was made.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.put_backup_policy_request.PutBackupPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.backup_policy_description.BackupPolicyDescription"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.put_backup_policy

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.put_backup_policy.async_put_backup_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.put_backup_policy_request.PutBackupPolicyRequest = {
            "file_system_id": file_system_id,
            "backup_policy": backup_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_file_system_policy(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        policy: "capo_efs.types.policy.Policy",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        bypass_policy_lockout_safety_check: Optional[
            "capo_efs.types.bypass_policy_lockout_safety_check.BypassPolicyLockoutSafetyCheck"
        ] = None,
    ) -> "capo_efs.types.file_system_policy_description.FileSystemPolicyDescription":
        """<p>Applies an Amazon EFS <code>FileSystemPolicy</code> to an Amazon EFS file system. A file system policy is an IAM resource-based policy and can contain multiple policy statements. A file system always has exactly one file system policy, which can be the default policy or an explicit policy set or updated using this API operation. EFS file system policies have a 20,000 character limit. When an explicit policy is set, it overrides the default policy. For more information about the default file system policy, see <a href="https://docs.aws.amazon.com/efs/latest/ug/iam-access-control-nfs-efs.html#default-filesystempolicy"> Default EFS file system policy</a>. </p> <note> <p>EFS file system policies have a 20,000 character limit.</p> </note> <p>This operation requires permissions for the <code>elasticfilesystem:PutFileSystemPolicy</code> action.</p>

        Args:
            file_system_id: <p>The ID of the EFS file system that you want to create or update the <code>FileSystemPolicy</code> for.</p>
            policy: <p>The <code>FileSystemPolicy</code> that you're creating. Accepts a JSON formatted policy definition. EFS file system policies have a 20,000 character limit. To find out more about the elements that make up a file system policy, see <a href="https://docs.aws.amazon.com/efs/latest/ug/security_iam_service-with-iam.html#security_iam_service-with-iam-resource-based-policies">Resource-based policies within Amazon EFS</a>. </p>
            bypass_policy_lockout_safety_check: <p>(Optional) A boolean that specifies whether or not to bypass the <code>FileSystemPolicy</code> lockout safety check. The lockout safety check determines whether the policy in the request will lock out, or prevent, the IAM principal that is making the request from making future <code>PutFileSystemPolicy</code> requests on this file system. Set <code>BypassPolicyLockoutSafetyCheck</code> to <code>True</code> only when you intend to prevent the IAM principal that is making the request from making subsequent <code>PutFileSystemPolicy</code> requests on this file system. The default value is <code>False</code>. </p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.incorrect_file_system_life_cycle_state.IncorrectFileSystemLifeCycleState: <p>Returned if the file system's lifecycle state is not "available".</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.invalid_policy_exception.InvalidPolicyException: <p>Returned if the <code>FileSystemPolicy</code> is malformed or contains an error such as a parameter value that is not valid or a missing required parameter. Returned in the case of a policy lockout safety check error.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.put_file_system_policy_request.PutFileSystemPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.file_system_policy_description.FileSystemPolicyDescription"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.put_file_system_policy

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.put_file_system_policy.async_put_file_system_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.put_file_system_policy_request.PutFileSystemPolicyRequest = {
            "file_system_id": file_system_id,
            "policy": policy,
        }
        if bypass_policy_lockout_safety_check is not None:
            input_["bypass_policy_lockout_safety_check"] = (
                bypass_policy_lockout_safety_check
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_lifecycle_configuration(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        lifecycle_policies: "capo_efs.types.lifecycle_policies.LifecyclePolicies",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> "capo_efs.types.lifecycle_configuration_description.LifecycleConfigurationDescription":
        """<p>Use this action to manage storage for your file system. A <code>LifecycleConfiguration</code> consists of one or more <code>LifecyclePolicy</code> objects that define the following:</p> <ul> <li> <p> <b> <code>TransitionToIA</code> </b> – When to move files in the file system from primary storage (Standard storage class) into the Infrequent Access (IA) storage.</p> </li> <li> <p> <b> <code>TransitionToArchive</code> </b> – When to move files in the file system from their current storage class (either IA or Standard storage) into the Archive storage.</p> <p>File systems cannot transition into Archive storage before transitioning into IA storage. Therefore, TransitionToArchive must either not be set or must be later than TransitionToIA.</p> <note> <p> The Archive storage class is available only for file systems that use the Elastic throughput mode and the General Purpose performance mode. </p> </note> </li> </ul> <ul> <li> <p> <b> <code>TransitionToPrimaryStorageClass</code> </b> – Whether to move files in the file system back to primary storage (Standard storage class) after they are accessed in IA or Archive storage.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html"> Managing file system storage</a>.</p> <p>Each Amazon EFS file system supports one lifecycle configuration, which applies to all files in the file system. If a <code>LifecycleConfiguration</code> object already exists for the specified file system, a <code>PutLifecycleConfiguration</code> call modifies the existing configuration. A <code>PutLifecycleConfiguration</code> call with an empty <code>LifecyclePolicies</code> array in the request body deletes any existing <code>LifecycleConfiguration</code>. In the request, specify the following: </p> <ul> <li> <p>The ID for the file system for which you are enabling, disabling, or modifying lifecycle management.</p> </li> <li> <p>A <code>LifecyclePolicies</code> array of <code>LifecyclePolicy</code> objects that define when to move files to IA storage, to Archive storage, and back to primary storage.</p> <note> <p>Amazon EFS requires that each <code>LifecyclePolicy</code> object have only have a single transition, so the <code>LifecyclePolicies</code> array needs to be structured with separate <code>LifecyclePolicy</code> objects. See the example requests in the following section for more information.</p> </note> </li> </ul> <p>This operation requires permissions for the <code>elasticfilesystem:PutLifecycleConfiguration</code> operation.</p> <p>To apply a <code>LifecycleConfiguration</code> object to an encrypted file system, you need the same Key Management Service permissions as when you created the encrypted file system.</p>

        Args:
            file_system_id: <p>The ID of the file system for which you are creating the <code>LifecycleConfiguration</code> object (String).</p>
            lifecycle_policies: <p>An array of <code>LifecyclePolicy</code> objects that define the file system's <code>LifecycleConfiguration</code> object. A <code>LifecycleConfiguration</code> object informs lifecycle management of the following:</p> <ul> <li> <p> <b> <code>TransitionToIA</code> </b> – When to move files in the file system from primary storage (Standard storage class) into the Infrequent Access (IA) storage.</p> </li> <li> <p> <b> <code>TransitionToArchive</code> </b> – When to move files in the file system from their current storage class (either IA or Standard storage) into the Archive storage.</p> <p>File systems cannot transition into Archive storage before transitioning into IA storage. Therefore, TransitionToArchive must either not be set or must be later than TransitionToIA.</p> <note> <p>The Archive storage class is available only for file systems that use the Elastic throughput mode and the General Purpose performance mode. </p> </note> </li> <li> <p> <b> <code>TransitionToPrimaryStorageClass</code> </b> – Whether to move files in the file system back to primary storage (Standard storage class) after they are accessed in IA or Archive storage.</p> </li> </ul> <note> <p>When using the <code>put-lifecycle-configuration</code> CLI command or the <code>PutLifecycleConfiguration</code> API action, Amazon EFS requires that each <code>LifecyclePolicy</code> object have only a single transition. This means that in a request body, <code>LifecyclePolicies</code> must be structured as an array of <code>LifecyclePolicy</code> objects, one object for each storage transition. See the example requests in the following section for more information.</p> </note>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.incorrect_file_system_life_cycle_state.IncorrectFileSystemLifeCycleState: <p>Returned if the file system's lifecycle state is not "available".</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Creates a new lifecycleconfiguration object for a file system
            This operation enables lifecycle management on a file system by creating a new LifecycleConfiguration object. A LifecycleConfiguration object defines when files in an Amazon EFS file system are automatically transitioned to the lower-cost EFS Infrequent Access (IA) storage class. A LifecycleConfiguration applies to all files in a file system.

            >>> await client.put_lifecycle_configuration(file_system_id='fs-01234567', lifecycle_policies=[{'TransitionToIA': 'AFTER_30_DAYS'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.put_lifecycle_configuration_request.PutLifecycleConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.lifecycle_configuration_description.LifecycleConfigurationDescription"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.put_lifecycle_configuration

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.put_lifecycle_configuration.async_put_lifecycle_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.put_lifecycle_configuration_request.PutLifecycleConfigurationRequest = {
            "file_system_id": file_system_id,
            "lifecycle_policies": lifecycle_policies,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_id: "capo_efs.types.resource_id.ResourceId",
        tags: "capo_efs.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> None:
        """<p>Creates a tag for an EFS resource. You can create tags for EFS file systems and access points using this API operation.</p> <p>This operation requires permissions for the <code>elasticfilesystem:TagResource</code> action.</p>

        Args:
            resource_id: <p>The ID specifying the EFS resource that you want to create a tag for.</p>
            tags: <p>An array of <code>Tag</code> objects to add. Each <code>Tag</code> object is a key-value pair.</p>

        Raises:
            capo_efs.errors.access_point_not_found.AccessPointNotFound: <p>Returned if the specified <code>AccessPointId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_efs._operations.magnolio_api_service_v20150201.tag_resource

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.tag_resource_request.TagResourceRequest = {
            "resource_id": resource_id,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_id: "capo_efs.types.resource_id.ResourceId",
        tag_keys: "capo_efs.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
    ) -> None:
        """<p>Removes tags from an EFS resource. You can remove tags from EFS file systems and access points using this API operation.</p> <p>This operation requires permissions for the <code>elasticfilesystem:UntagResource</code> action.</p>

        Args:
            resource_id: <p>Specifies the EFS resource that you want to remove tags from.</p>
            tag_keys: <p>The keys of the key-value tag pairs that you want to remove from the specified EFS resource.</p>

        Raises:
            capo_efs.errors.access_point_not_found.AccessPointNotFound: <p>Returned if the specified <code>AccessPointId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_efs._operations.magnolio_api_service_v20150201.untag_resource

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.untag_resource_request.UntagResourceRequest = {
            "resource_id": resource_id,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_file_system(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        throughput_mode: Optional[
            "capo_efs.types.throughput_mode.ThroughputMode"
        ] = None,
        provisioned_throughput_in_mibps: Optional[
            "capo_efs.types.provisioned_throughput_in_mibps.ProvisionedThroughputInMibps"
        ] = None,
    ) -> "capo_efs.types.file_system_description.FileSystemDescription":
        """<p>Updates the throughput mode or the amount of provisioned throughput of an existing file system.</p>

        Args:
            file_system_id: <p>The ID of the file system that you want to update.</p>
            throughput_mode: <p>(Optional) Updates the file system's throughput mode. If you're not updating your throughput mode, you don't need to provide this value in your request. If you are changing the <code>ThroughputMode</code> to <code>provisioned</code>, you must also set a value for <code>ProvisionedThroughputInMibps</code>.</p>
            provisioned_throughput_in_mibps: <p>(Optional) The throughput, measured in mebibytes per second (MiBps), that you want to provision for a file system that you're creating. Required if <code>ThroughputMode</code> is set to <code>provisioned</code>. Valid values are 1-3414 MiBps, with the upper limit depending on Region. To increase this limit, contact Amazon Web Services Support. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits">Amazon EFS quotas that you can increase</a> in the <i>Amazon EFS User Guide</i>.</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.incorrect_file_system_life_cycle_state.IncorrectFileSystemLifeCycleState: <p>Returned if the file system's lifecycle state is not "available".</p>
            capo_efs.errors.insufficient_throughput_capacity.InsufficientThroughputCapacity: <p>Returned if there's not enough capacity to provision additional throughput. This value might be returned when you try to create a file system in provisioned throughput mode, when you attempt to increase the provisioned throughput of an existing file system, or when you attempt to change an existing file system from Bursting Throughput to Provisioned Throughput mode. Try again later.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.throughput_limit_exceeded.ThroughputLimitExceeded: <p>Returned if the throughput mode or amount of provisioned throughput can't be changed because the throughput limit of 1024 MiB/s has been reached.</p>
            capo_efs.errors.too_many_requests.TooManyRequests: <p>Returned if you don’t wait at least 24 hours before either changing the throughput mode, or decreasing the Provisioned Throughput value.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.update_file_system_request.UpdateFileSystemRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.file_system_description.FileSystemDescription"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.update_file_system

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.update_file_system.async_update_file_system(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.update_file_system_request.UpdateFileSystemRequest = {
            "file_system_id": file_system_id
        }
        if throughput_mode is not None:
            input_["throughput_mode"] = throughput_mode
        if provisioned_throughput_in_mibps is not None:
            input_["provisioned_throughput_in_mibps"] = provisioned_throughput_in_mibps

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_file_system_protection(
        self,
        file_system_id: "capo_efs.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncEFSClientConfig] = None,
        replication_overwrite_protection: Optional[
            "capo_efs.types.replication_overwrite_protection.ReplicationOverwriteProtection"
        ] = None,
    ) -> "capo_efs.types.file_system_protection_description.FileSystemProtectionDescription":
        """<p>Updates protection on the file system.</p> <p>This operation requires permissions for the <code>elasticfilesystem:UpdateFileSystemProtection</code> action. </p>

        Args:
            file_system_id: <p>The ID of the file system to update. </p>
            replication_overwrite_protection: <p>The status of the file system's replication overwrite protection.</p> <ul> <li> <p> <code>ENABLED</code> – The file system cannot be used as the destination file system in a replication configuration. The file system is writeable. Replication overwrite protection is <code>ENABLED</code> by default. </p> </li> <li> <p> <code>DISABLED</code> – The file system can be used as the destination file system in a replication configuration. The file system is read-only and can only be modified by EFS replication.</p> </li> <li> <p> <code>REPLICATING</code> – The file system is being used as the destination file system in a replication configuration. The file system is read-only and is only modified only by EFS replication.</p> </li> </ul> <p>If the replication configuration is deleted, the file system's replication overwrite protection is re-enabled and the file system becomes writeable.</p>

        Raises:
            capo_efs.errors.bad_request.BadRequest: <p>Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_efs.errors.file_system_not_found.FileSystemNotFound: <p>Returned if the specified <code>FileSystemId</code> value doesn't exist in the requester's Amazon Web Services account.</p>
            capo_efs.errors.incorrect_file_system_life_cycle_state.IncorrectFileSystemLifeCycleState: <p>Returned if the file system's lifecycle state is not "available".</p>
            capo_efs.errors.insufficient_throughput_capacity.InsufficientThroughputCapacity: <p>Returned if there's not enough capacity to provision additional throughput. This value might be returned when you try to create a file system in provisioned throughput mode, when you attempt to increase the provisioned throughput of an existing file system, or when you attempt to change an existing file system from Bursting Throughput to Provisioned Throughput mode. Try again later.</p>
            capo_efs.errors.internal_server_error.InternalServerError: <p>Returned if an error occurred on the server side.</p>
            capo_efs.errors.replication_already_exists.ReplicationAlreadyExists: <p>Returned if the file system is already included in a replication configuration.></p>
            capo_efs.errors.throughput_limit_exceeded.ThroughputLimitExceeded: <p>Returned if the throughput mode or amount of provisioned throughput can't be changed because the throughput limit of 1024 MiB/s has been reached.</p>
            capo_efs.errors.too_many_requests.TooManyRequests: <p>Returned if you don’t wait at least 24 hours before either changing the throughput mode, or decreasing the Provisioned Throughput value.</p>
            capo_efs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_efs.types.update_file_system_protection_request.UpdateFileSystemProtectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_efs.types.file_system_protection_description.FileSystemProtectionDescription"
        ]:
            import capo_efs._operations.magnolio_api_service_v20150201.update_file_system_protection

            (
                output,
                http_response,
            ) = await capo_efs._operations.magnolio_api_service_v20150201.update_file_system_protection.async_update_file_system_protection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_efs.types.update_file_system_protection_request.UpdateFileSystemProtectionRequest = {
            "file_system_id": file_system_id
        }
        if replication_overwrite_protection is not None:
            input_["replication_overwrite_protection"] = (
                replication_overwrite_protection
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
