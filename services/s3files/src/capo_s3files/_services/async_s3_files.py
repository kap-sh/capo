"""Generated from Smithy shape ``com.amazonaws.s3files#S3Files``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_s3files._auth._signers
import capo_s3files._auth._sigv4
from capo_s3files._auth._identity import Credentials
from capo_s3files._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_s3files._auth._zapros_handler import AuthMiddleware
from capo_s3files._pagination import resolve_path as _resolve_path
from capo_s3files._services._aws_config import aaws_config
from capo_s3files._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_s3files.types.access_point_id
    import capo_s3files.types.bucket_arn
    import capo_s3files.types.client_token
    import capo_s3files.types.create_access_point_request
    import capo_s3files.types.create_access_point_response
    import capo_s3files.types.create_file_system_request
    import capo_s3files.types.create_file_system_response
    import capo_s3files.types.create_mount_target_request
    import capo_s3files.types.create_mount_target_response
    import capo_s3files.types.creation_token
    import capo_s3files.types.delete_access_point_request
    import capo_s3files.types.delete_file_system_policy_request
    import capo_s3files.types.delete_file_system_request
    import capo_s3files.types.delete_mount_target_request
    import capo_s3files.types.expiration_data_rule_list
    import capo_s3files.types.file_system_id
    import capo_s3files.types.get_access_point_request
    import capo_s3files.types.get_access_point_response
    import capo_s3files.types.get_file_system_policy_request
    import capo_s3files.types.get_file_system_policy_response
    import capo_s3files.types.get_file_system_request
    import capo_s3files.types.get_file_system_response
    import capo_s3files.types.get_mount_target_request
    import capo_s3files.types.get_mount_target_response
    import capo_s3files.types.get_synchronization_configuration_request
    import capo_s3files.types.get_synchronization_configuration_response
    import capo_s3files.types.import_data_rule_list
    import capo_s3files.types.ip_address_type
    import capo_s3files.types.ipv4_address
    import capo_s3files.types.ipv6_address
    import capo_s3files.types.kms_key_id
    import capo_s3files.types.list_access_points_description
    import capo_s3files.types.list_access_points_request
    import capo_s3files.types.list_access_points_response
    import capo_s3files.types.list_file_systems_description
    import capo_s3files.types.list_file_systems_request
    import capo_s3files.types.list_file_systems_response
    import capo_s3files.types.list_mount_targets_description
    import capo_s3files.types.list_mount_targets_request
    import capo_s3files.types.list_mount_targets_response
    import capo_s3files.types.list_tags_for_resource_request
    import capo_s3files.types.list_tags_for_resource_response
    import capo_s3files.types.mount_target_id
    import capo_s3files.types.posix_user
    import capo_s3files.types.put_file_system_policy_request
    import capo_s3files.types.put_file_system_policy_response
    import capo_s3files.types.put_synchronization_configuration_request
    import capo_s3files.types.put_synchronization_configuration_response
    import capo_s3files.types.resource_id
    import capo_s3files.types.role_arn
    import capo_s3files.types.root_directory
    import capo_s3files.types.security_groups
    import capo_s3files.types.subnet_id
    import capo_s3files.types.tag
    import capo_s3files.types.tag_keys
    import capo_s3files.types.tag_list
    import capo_s3files.types.tag_resource_request
    import capo_s3files.types.untag_resource_request
    import capo_s3files.types.update_mount_target_request
    import capo_s3files.types.update_mount_target_response


class AsyncS3FilesClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncS3FilesClient:
    """A client for the ``S3Files`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
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
        self._config = AsyncS3FilesClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncS3FilesClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncS3FilesClientConfig = config_overrides or {}
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
        file_system_id: "capo_s3files.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
        client_token: Optional["capo_s3files.types.client_token.ClientToken"] = None,
        tags: Optional["capo_s3files.types.tag_list.TagList"] = None,
        posix_user: Optional["capo_s3files.types.posix_user.PosixUser"] = None,
        root_directory: Optional[
            "capo_s3files.types.root_directory.RootDirectory"
        ] = None,
    ) -> "capo_s3files.types.create_access_point_response.CreateAccessPointResponse":
        """<p>Creates an S3 File System Access Point for application-specific access with POSIX user identity and root directory enforcement. Access points provide a way to manage access to shared datasets in multi-tenant scenarios.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Web Services ignores the request, but does not return an error.</p>
            tags: <p>An array of key-value pairs to apply to the access point for resource tagging.</p>
            file_system_id: <p>The ID or Amazon Resource Name (ARN) of the S3 File System.</p>
            posix_user: <p>The POSIX identity with uid, gid, and secondary group IDs for user enforcement when accessing the file system through this access point.</p>
            root_directory: <p>The root directory path for the access point, with optional creation permissions for newly created directories.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to create a resource that already exists or delete a resource that is in use.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota. Review your service quotas and either delete resources or request a quota increase.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.create_access_point_request.CreateAccessPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.create_access_point_response.CreateAccessPointResponse"
        ]:
            import capo_s3files._operations.s3_files.create_access_point

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.create_access_point.async_create_access_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.create_access_point_request.CreateAccessPointRequest = {
            "file_system_id": file_system_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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
        bucket: "capo_s3files.types.bucket_arn.BucketArn",
        role_arn: "capo_s3files.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
        prefix: Optional[str] = None,
        client_token: Optional[
            "capo_s3files.types.creation_token.CreationToken"
        ] = None,
        kms_key_id: Optional["capo_s3files.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_s3files.types.tag_list.TagList"] = None,
        accept_bucket_warning: Optional[bool] = None,
    ) -> "capo_s3files.types.create_file_system_response.CreateFileSystemResponse":
        """<p>Creates an S3 File System resource scoped to a bucket or prefix within a bucket, enabling file system access to S3 data. To create a file system, you need an S3 bucket and an IAM role that grants the service permission to access the bucket.</p>

        Args:
            bucket: <p>The Amazon Resource Name (ARN) of the S3 bucket that will be accessible through the file system. The bucket must exist and be in the same Amazon Web Services Region as the file system.</p>
            prefix: <p>An optional prefix within the S3 bucket to scope the file system access. If specified, the file system provides access only to objects with keys that begin with this prefix. If not specified, the file system provides access to the entire bucket.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure idempotent creation. Up to 64 ASCII characters are allowed. If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>
            kms_key_id: <p>The ARN, key ID, or alias of the KMS key to use for encryption. If not specified, the service uses a service-owned key for encryption. You can specify a KMS key using the following formats: key ID, ARN, key alias, or key alias ARN. If you use <code>KmsKeyId</code>, the file system will be encrypted.</p>
            role_arn: <p>The ARN of the IAM role that grants the S3 Files service permission to read and write data between the file system and the S3 bucket. This role must have the necessary permissions to access the specified bucket and prefix.</p>
            tags: <p>An array of key-value pairs to apply as tags to the file system resource. Each tag is a user-defined key-value pair. You can use tags to categorize and manage your file systems. Each key must be unique for the resource.</p>
            accept_bucket_warning: <p>Set to true to acknowledge and accept any warnings about the bucket configuration. If not specified, the operation may fail if there are bucket configuration warnings.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to create a resource that already exists or delete a resource that is in use.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota. Review your service quotas and either delete resources or request a quota increase.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.create_file_system_request.CreateFileSystemRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.create_file_system_response.CreateFileSystemResponse"
        ]:
            import capo_s3files._operations.s3_files.create_file_system

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.create_file_system.async_create_file_system(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.create_file_system_request.CreateFileSystemRequest = {
            "bucket": bucket,
            "role_arn": role_arn,
        }
        if prefix is not None:
            input_["prefix"] = prefix
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if accept_bucket_warning is not None:
            input_["accept_bucket_warning"] = accept_bucket_warning

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_mount_target(
        self,
        file_system_id: "capo_s3files.types.file_system_id.FileSystemId",
        subnet_id: "capo_s3files.types.subnet_id.SubnetId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
        ipv4_address: Optional["capo_s3files.types.ipv4_address.Ipv4Address"] = None,
        ipv6_address: Optional["capo_s3files.types.ipv6_address.Ipv6Address"] = None,
        ip_address_type: Optional[
            "capo_s3files.types.ip_address_type.IpAddressType"
        ] = None,
        security_groups: Optional[
            "capo_s3files.types.security_groups.SecurityGroups"
        ] = None,
    ) -> "capo_s3files.types.create_mount_target_response.CreateMountTargetResponse":
        """<p>Creates a mount target resource as an endpoint for mounting the S3 File System from compute resources in a specific Availability Zone and VPC. Mount targets provide network access to the file system.</p>

        Args:
            file_system_id: <p>The ID or Amazon Resource Name (ARN) of the S3 File System to create the mount target for.</p>
            subnet_id: <p>The ID of the subnet where the mount target will be created. The subnet must be in the same Amazon Web Services Region as the file system. For file systems with regional availability, you can create mount targets in any subnet within the Region. The subnet determines the Availability Zone where the mount target will be located.</p>
            ipv4_address: <p>A specific IPv4 address to assign to the mount target. If not specified and the IP address type supports IPv4, an address is automatically assigned from the subnet's available IPv4 address range. The address must be within the subnet's CIDR block and not already in use.</p>
            ipv6_address: <p>A specific IPv6 address to assign to the mount target. If not specified and the IP address type supports IPv6, an address is automatically assigned from the subnet's available IPv6 address range. The address must be within the subnet's IPv6 CIDR block and not already in use.</p>
            ip_address_type: <p>The IP address type for the mount target. If not specified, <code>IPV4_ONLY</code> is used. The IP address type must match the IP configuration of the specified subnet.</p>
            security_groups: <p>An array of VPC security group IDs to associate with the mount target's network interface. These security groups control network access to the mount target. If not specified, the default security group for the subnet's VPC is used. All security groups must belong to the same VPC as the subnet.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to create a resource that already exists or delete a resource that is in use.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota. Review your service quotas and either delete resources or request a quota increase.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.create_mount_target_request.CreateMountTargetRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.create_mount_target_response.CreateMountTargetResponse"
        ]:
            import capo_s3files._operations.s3_files.create_mount_target

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.create_mount_target.async_create_mount_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.create_mount_target_request.CreateMountTargetRequest = {
            "file_system_id": file_system_id,
            "subnet_id": subnet_id,
        }
        if ipv4_address is not None:
            input_["ipv4_address"] = ipv4_address
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

    async def delete_access_point(
        self,
        access_point_id: "capo_s3files.types.access_point_id.AccessPointId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
    ) -> None:
        """<p>Deletes an S3 File System Access Point. This operation is irreversible.</p>

        Args:
            access_point_id: <p>The ID or Amazon Resource Name (ARN) of the access point to delete.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to create a resource that already exists or delete a resource that is in use.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.delete_access_point_request.DeleteAccessPointRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3files._operations.s3_files.delete_access_point

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.delete_access_point.async_delete_access_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.delete_access_point_request.DeleteAccessPointRequest = {
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
        file_system_id: "capo_s3files.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
        force_delete: Optional[bool] = None,
    ) -> None:
        """<p>Deletes an S3 File System. You can optionally force deletion of a file system that has pending export data.</p>

        Args:
            file_system_id: <p>The ID or Amazon Resource Name (ARN) of the S3 File System to delete.</p>
            force_delete: <p>If true, allows deletion of a file system that contains data pending export to S3. If false (the default), the deletion will fail if there is data that has not yet been exported to the S3 bucket. Use this parameter with caution as it may result in data loss.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to create a resource that already exists or delete a resource that is in use.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.delete_file_system_request.DeleteFileSystemRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3files._operations.s3_files.delete_file_system

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.delete_file_system.async_delete_file_system(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.delete_file_system_request.DeleteFileSystemRequest = {
            "file_system_id": file_system_id
        }
        if force_delete is not None:
            input_["force_delete"] = force_delete

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_file_system_policy(
        self,
        file_system_id: "capo_s3files.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
    ) -> None:
        """<p>Deletes the IAM resource policy of an S3 File System.</p>

        Args:
            file_system_id: <p>The ID or Amazon Resource Name (ARN) of the S3 File System whose resource policy to delete.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.delete_file_system_policy_request.DeleteFileSystemPolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3files._operations.s3_files.delete_file_system_policy

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.delete_file_system_policy.async_delete_file_system_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.delete_file_system_policy_request.DeleteFileSystemPolicyRequest = {
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
        mount_target_id: "capo_s3files.types.mount_target_id.MountTargetId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified mount target. This operation is irreversible.</p>

        Args:
            mount_target_id: <p>The ID of the mount target to delete.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to create a resource that already exists or delete a resource that is in use.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.delete_mount_target_request.DeleteMountTargetRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3files._operations.s3_files.delete_mount_target

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.delete_mount_target.async_delete_mount_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.delete_mount_target_request.DeleteMountTargetRequest = {
            "mount_target_id": mount_target_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_point(
        self,
        access_point_id: "capo_s3files.types.access_point_id.AccessPointId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
    ) -> "capo_s3files.types.get_access_point_response.GetAccessPointResponse":
        """<p>Returns resource information for an S3 File System Access Point.</p>

        Args:
            access_point_id: <p>The ID or Amazon Resource Name (ARN) of the access point to retrieve information for.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.get_access_point_request.GetAccessPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.get_access_point_response.GetAccessPointResponse"
        ]:
            import capo_s3files._operations.s3_files.get_access_point

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.get_access_point.async_get_access_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.get_access_point_request.GetAccessPointRequest = {
            "access_point_id": access_point_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_file_system(
        self,
        file_system_id: "capo_s3files.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
    ) -> "capo_s3files.types.get_file_system_response.GetFileSystemResponse":
        """<p>Returns resource information for the specified S3 File System including status, configuration, and metadata.</p>

        Args:
            file_system_id: <p>The ID or Amazon Resource Name (ARN) of the S3 File System to retrieve information for.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.get_file_system_request.GetFileSystemRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.get_file_system_response.GetFileSystemResponse"
        ]:
            import capo_s3files._operations.s3_files.get_file_system

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.get_file_system.async_get_file_system(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.get_file_system_request.GetFileSystemRequest = {
            "file_system_id": file_system_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_file_system_policy(
        self,
        file_system_id: "capo_s3files.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
    ) -> (
        "capo_s3files.types.get_file_system_policy_response.GetFileSystemPolicyResponse"
    ):
        """<p>Returns the IAM resource policy of an S3 File System.</p>

        Args:
            file_system_id: <p>The ID or Amazon Resource Name (ARN) of the S3 File System whose resource policy to retrieve.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.get_file_system_policy_request.GetFileSystemPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.get_file_system_policy_response.GetFileSystemPolicyResponse"
        ]:
            import capo_s3files._operations.s3_files.get_file_system_policy

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.get_file_system_policy.async_get_file_system_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.get_file_system_policy_request.GetFileSystemPolicyRequest = {
            "file_system_id": file_system_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_mount_target(
        self,
        mount_target_id: "capo_s3files.types.mount_target_id.MountTargetId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
    ) -> "capo_s3files.types.get_mount_target_response.GetMountTargetResponse":
        """<p>Returns detailed resource information for the specified mount target including network configuration.</p>

        Args:
            mount_target_id: <p>The ID of the mount target to retrieve information for.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.get_mount_target_request.GetMountTargetRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.get_mount_target_response.GetMountTargetResponse"
        ]:
            import capo_s3files._operations.s3_files.get_mount_target

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.get_mount_target.async_get_mount_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.get_mount_target_request.GetMountTargetRequest = {
            "mount_target_id": mount_target_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_synchronization_configuration(
        self,
        file_system_id: "capo_s3files.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
    ) -> "capo_s3files.types.get_synchronization_configuration_response.GetSynchronizationConfigurationResponse":
        """<p>Returns the synchronization configuration for the specified S3 File System, including import data rules and expiration data rules.</p>

        Args:
            file_system_id: <p>The ID or Amazon Resource Name (ARN) of the S3 File System to retrieve the synchronization configuration for.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.get_synchronization_configuration_request.GetSynchronizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.get_synchronization_configuration_response.GetSynchronizationConfigurationResponse"
        ]:
            import capo_s3files._operations.s3_files.get_synchronization_configuration

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.get_synchronization_configuration.async_get_synchronization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.get_synchronization_configuration_request.GetSynchronizationConfigurationRequest = {
            "file_system_id": file_system_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_access_points(
        self,
        file_system_id: "capo_s3files.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_s3files.types.list_access_points_response.ListAccessPointsResponse":
        """<p>Returns resource information for all S3 File System Access Points associated with the specified S3 File System.</p>

        Args:
            file_system_id: <p>The ID or Amazon Resource Name (ARN) of the S3 File System to list access points for.</p>
            max_results: <p>The maximum number of access points to return in a single response.</p>
            next_token: <p>A pagination token returned from a previous call to continue listing access points.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.list_access_points_request.ListAccessPointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.list_access_points_response.ListAccessPointsResponse"
        ]:
            import capo_s3files._operations.s3_files.list_access_points

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.list_access_points.async_list_access_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.list_access_points_request.ListAccessPointsRequest = {
            "file_system_id": file_system_id
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

    async def iter_list_access_points(
        self,
        file_system_id: "capo_s3files.types.file_system_id.FileSystemId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_s3files.types.list_access_points_description.ListAccessPointsDescription]":
        _token = next_token
        while True:
            _response = await self.list_access_points(
                file_system_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("access_points",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_file_systems(
        self,
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
        bucket: Optional["capo_s3files.types.bucket_arn.BucketArn"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_s3files.types.list_file_systems_response.ListFileSystemsResponse":
        """<p>Returns a list of all S3 File Systems owned by the account with optional filtering by bucket.</p>

        Args:
            bucket: <p>Optional filter to list only file systems associated with the specified S3 bucket Amazon Resource Name (ARN). If provided, only file systems that provide access to this bucket will be returned in the response.</p>
            max_results: <p>The maximum number of file systems to return in a single response. If not specified, up to 100 file systems are returned.</p>
            next_token: <p>A pagination token returned from a previous call to continue listing file systems.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.list_file_systems_request.ListFileSystemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.list_file_systems_response.ListFileSystemsResponse"
        ]:
            import capo_s3files._operations.s3_files.list_file_systems

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.list_file_systems.async_list_file_systems(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.list_file_systems_request.ListFileSystemsRequest = {}
        if bucket is not None:
            input_["bucket"] = bucket
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

    async def iter_list_file_systems(
        self,
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
        bucket: Optional["capo_s3files.types.bucket_arn.BucketArn"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_s3files.types.list_file_systems_description.ListFileSystemsDescription]":
        _token = next_token
        while True:
            _response = await self.list_file_systems(
                config_overrides=config_overrides,
                bucket=bucket,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("file_systems",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_mount_targets(
        self,
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
        file_system_id: Optional[
            "capo_s3files.types.file_system_id.FileSystemId"
        ] = None,
        access_point_id: Optional[
            "capo_s3files.types.access_point_id.AccessPointId"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_s3files.types.list_mount_targets_response.ListMountTargetsResponse":
        """<p>Returns resource information for all mount targets with optional filtering by file system, access point, and VPC.</p>

        Args:
            file_system_id: <p>Optional filter to list only mount targets associated with the specified S3 File System ID or Amazon Resource Name (ARN). If provided, only mount targets for this file system will be returned in the response.</p>
            access_point_id: <p>Optional filter to list only mount targets associated with the specified access point ID or Amazon Resource Name (ARN).</p>
            max_results: <p>The maximum number of mount targets to return in a single response.</p>
            next_token: <p>A pagination token returned from a previous call to continue listing mount targets.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.list_mount_targets_request.ListMountTargetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.list_mount_targets_response.ListMountTargetsResponse"
        ]:
            import capo_s3files._operations.s3_files.list_mount_targets

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.list_mount_targets.async_list_mount_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.list_mount_targets_request.ListMountTargetsRequest = {}
        if file_system_id is not None:
            input_["file_system_id"] = file_system_id
        if access_point_id is not None:
            input_["access_point_id"] = access_point_id
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

    async def iter_list_mount_targets(
        self,
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
        file_system_id: Optional[
            "capo_s3files.types.file_system_id.FileSystemId"
        ] = None,
        access_point_id: Optional[
            "capo_s3files.types.access_point_id.AccessPointId"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_s3files.types.list_mount_targets_description.ListMountTargetsDescription]":
        _token = next_token
        while True:
            _response = await self.list_mount_targets(
                config_overrides=config_overrides,
                file_system_id=file_system_id,
                access_point_id=access_point_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("mount_targets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_id: "capo_s3files.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> (
        "capo_s3files.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Lists all tags for S3 Files resources.</p>

        Args:
            resource_id: <p>The ID or Amazon Resource Name (ARN) of the resource to list tags for.</p>
            max_results: <p>The maximum number of tags to return in a single response.</p>
            next_token: <p>A pagination token returned from a previous call to continue listing tags.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_s3files._operations.s3_files.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_id: "capo_s3files.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_s3files.types.tag.Tag]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                resource_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_file_system_policy(
        self,
        file_system_id: "capo_s3files.types.file_system_id.FileSystemId",
        policy: str,
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
    ) -> (
        "capo_s3files.types.put_file_system_policy_response.PutFileSystemPolicyResponse"
    ):
        """<p>Creates or replaces the IAM resource policy for an S3 File System to control access permissions.</p>

        Args:
            file_system_id: <p>The ID or Amazon Resource Name (ARN) of the S3 File System to apply the resource policy to.</p>
            policy: <p>The JSON-formatted resource policy to apply to the file system. The policy defines the permissions for accessing the file system. The policy must be a valid JSON document that follows IAM policy syntax.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.put_file_system_policy_request.PutFileSystemPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.put_file_system_policy_response.PutFileSystemPolicyResponse"
        ]:
            import capo_s3files._operations.s3_files.put_file_system_policy

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.put_file_system_policy.async_put_file_system_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.put_file_system_policy_request.PutFileSystemPolicyRequest = {
            "file_system_id": file_system_id,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_synchronization_configuration(
        self,
        file_system_id: "capo_s3files.types.file_system_id.FileSystemId",
        import_data_rules: "capo_s3files.types.import_data_rule_list.ImportDataRuleList",
        expiration_data_rules: "capo_s3files.types.expiration_data_rule_list.ExpirationDataRuleList",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
        latest_version_number: Optional[int] = None,
    ) -> "capo_s3files.types.put_synchronization_configuration_response.PutSynchronizationConfigurationResponse":
        """<p>Creates or updates the synchronization configuration for the specified S3 File System, including import data rules and expiration data rules.</p>

        Args:
            file_system_id: <p>The ID or Amazon Resource Name (ARN) of the S3 File System to configure synchronization for.</p>
            latest_version_number: <p>The version number of the current synchronization configuration. Omit this value when creating a synchronization configuration for the first time. For subsequent updates, provide this value for optimistic concurrency control. If the version number does not match the current configuration, the request fails with a <code>ConflictException</code>.</p>
            import_data_rules: <p>An array of import data rules that control how data is imported from S3 into the file system.</p>
            expiration_data_rules: <p>An array of expiration data rules that control when cached data expires from the file system.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to create a resource that already exists or delete a resource that is in use.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.put_synchronization_configuration_request.PutSynchronizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.put_synchronization_configuration_response.PutSynchronizationConfigurationResponse"
        ]:
            import capo_s3files._operations.s3_files.put_synchronization_configuration

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.put_synchronization_configuration.async_put_synchronization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.put_synchronization_configuration_request.PutSynchronizationConfigurationRequest = {
            "file_system_id": file_system_id,
            "import_data_rules": import_data_rules,
            "expiration_data_rules": expiration_data_rules,
        }
        if latest_version_number is not None:
            input_["latest_version_number"] = latest_version_number

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_id: "capo_s3files.types.resource_id.ResourceId",
        tags: "capo_s3files.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
    ) -> None:
        """<p>Creates tags for S3 Files resources using standard Amazon Web Services tagging APIs.</p>

        Args:
            resource_id: <p>The ID or Amazon Resource Name (ARN) of the resource to add tags to.</p>
            tags: <p>An array of key-value pairs to add as tags to the resource.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3files._operations.s3_files.tag_resource

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.tag_resource_request.TagResourceRequest = {
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
        resource_id: "capo_s3files.types.resource_id.ResourceId",
        tag_keys: "capo_s3files.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
    ) -> None:
        """<p>Removes tags from S3 Files resources.</p>

        Args:
            resource_id: <p>The ID or Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>An array of tag keys to remove from the resource.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3files._operations.s3_files.untag_resource

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_mount_target(
        self,
        mount_target_id: "capo_s3files.types.mount_target_id.MountTargetId",
        security_groups: "capo_s3files.types.security_groups.SecurityGroups",
        *,
        config_overrides: Optional[AsyncS3FilesClientConfig] = None,
    ) -> "capo_s3files.types.update_mount_target_response.UpdateMountTargetResponse":
        """<p>Updates the mount target resource, specifically security group configurations.</p>

        Args:
            mount_target_id: <p>The ID of the mount target to update.</p>
            security_groups: <p>An array of VPC security group IDs to associate with the mount target's network interface. This replaces the existing security groups. All security groups must belong to the same VPC as the mount target's subnet.</p>

        Raises:
            capo_s3files.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry your request using exponential backoff.</p>
            capo_s3files.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_s3files.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource exists and that you have permission to access it.</p>
            capo_s3files.errors.validation_exception.ValidationException: <p>The input parameters are not valid. Check the parameter values and try again.</p>
            capo_s3files.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3files.types.update_mount_target_request.UpdateMountTargetRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3files.types.update_mount_target_response.UpdateMountTargetResponse"
        ]:
            import capo_s3files._operations.s3_files.update_mount_target

            (
                output,
                http_response,
            ) = await capo_s3files._operations.s3_files.update_mount_target.async_update_mount_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3files.types.update_mount_target_request.UpdateMountTargetRequest = {
            "mount_target_id": mount_target_id,
            "security_groups": security_groups,
        }

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
