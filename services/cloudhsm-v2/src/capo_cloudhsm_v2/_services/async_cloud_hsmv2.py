"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#BaldrApiService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_cloudhsm_v2._auth._signers
import capo_cloudhsm_v2._auth._sigv4
from capo_cloudhsm_v2._auth._identity import Credentials
from capo_cloudhsm_v2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cloudhsm_v2._auth._zapros_handler import AuthMiddleware
from capo_cloudhsm_v2._pagination import resolve_path as _resolve_path
from capo_cloudhsm_v2._services._aws_config import aaws_config
from capo_cloudhsm_v2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.backup_arn
    import capo_cloudhsm_v2.types.backup_id
    import capo_cloudhsm_v2.types.backup_retention_policy
    import capo_cloudhsm_v2.types.backups_max_size
    import capo_cloudhsm_v2.types.boolean
    import capo_cloudhsm_v2.types.cert
    import capo_cloudhsm_v2.types.cloud_hsm_arn
    import capo_cloudhsm_v2.types.cluster_id
    import capo_cloudhsm_v2.types.cluster_mode
    import capo_cloudhsm_v2.types.clusters_max_size
    import capo_cloudhsm_v2.types.copy_backup_to_region_request
    import capo_cloudhsm_v2.types.copy_backup_to_region_response
    import capo_cloudhsm_v2.types.create_cluster_request
    import capo_cloudhsm_v2.types.create_cluster_response
    import capo_cloudhsm_v2.types.create_hsm_request
    import capo_cloudhsm_v2.types.create_hsm_response
    import capo_cloudhsm_v2.types.delete_backup_request
    import capo_cloudhsm_v2.types.delete_backup_response
    import capo_cloudhsm_v2.types.delete_cluster_request
    import capo_cloudhsm_v2.types.delete_cluster_response
    import capo_cloudhsm_v2.types.delete_hsm_request
    import capo_cloudhsm_v2.types.delete_hsm_response
    import capo_cloudhsm_v2.types.delete_resource_policy_request
    import capo_cloudhsm_v2.types.delete_resource_policy_response
    import capo_cloudhsm_v2.types.describe_backups_request
    import capo_cloudhsm_v2.types.describe_backups_response
    import capo_cloudhsm_v2.types.describe_clusters_request
    import capo_cloudhsm_v2.types.describe_clusters_response
    import capo_cloudhsm_v2.types.eni_id
    import capo_cloudhsm_v2.types.external_az
    import capo_cloudhsm_v2.types.filters
    import capo_cloudhsm_v2.types.get_resource_policy_request
    import capo_cloudhsm_v2.types.get_resource_policy_response
    import capo_cloudhsm_v2.types.hsm_id
    import capo_cloudhsm_v2.types.hsm_type
    import capo_cloudhsm_v2.types.initialize_cluster_request
    import capo_cloudhsm_v2.types.initialize_cluster_response
    import capo_cloudhsm_v2.types.ip_address
    import capo_cloudhsm_v2.types.list_tags_request
    import capo_cloudhsm_v2.types.list_tags_response
    import capo_cloudhsm_v2.types.max_size
    import capo_cloudhsm_v2.types.modify_backup_attributes_request
    import capo_cloudhsm_v2.types.modify_backup_attributes_response
    import capo_cloudhsm_v2.types.modify_cluster_request
    import capo_cloudhsm_v2.types.modify_cluster_response
    import capo_cloudhsm_v2.types.network_type
    import capo_cloudhsm_v2.types.next_token
    import capo_cloudhsm_v2.types.put_resource_policy_request
    import capo_cloudhsm_v2.types.put_resource_policy_response
    import capo_cloudhsm_v2.types.region
    import capo_cloudhsm_v2.types.resource_id
    import capo_cloudhsm_v2.types.resource_policy
    import capo_cloudhsm_v2.types.restore_backup_request
    import capo_cloudhsm_v2.types.restore_backup_response
    import capo_cloudhsm_v2.types.subnet_ids
    import capo_cloudhsm_v2.types.tag_key_list
    import capo_cloudhsm_v2.types.tag_list
    import capo_cloudhsm_v2.types.tag_resource_request
    import capo_cloudhsm_v2.types.tag_resource_response
    import capo_cloudhsm_v2.types.untag_resource_request
    import capo_cloudhsm_v2.types.untag_resource_response


class AsyncCloudHSMV2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncCloudHSMV2Client:
    """A client for the ``CloudHSMV2`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = AsyncCloudHSMV2ClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCloudHSMV2ClientConfig = config_overrides or {}
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
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def copy_backup_to_region(
        self,
        destination_region: "capo_cloudhsm_v2.types.region.Region",
        backup_id: "capo_cloudhsm_v2.types.backup_id.BackupId",
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
        tag_list: Optional["capo_cloudhsm_v2.types.tag_list.TagList"] = None,
    ) -> "capo_cloudhsm_v2.types.copy_backup_to_region_response.CopyBackupToRegionResponse":
        """<p>Copy an CloudHSM cluster backup to a different region.</p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM backup in a different Amazon Web Services account.</p>

        Args:
            destination_region: <p>The AWS region that will contain your copied CloudHSM cluster backup.</p>
            backup_id: <p>The ID of the backup that will be copied to the destination region. </p>
            tag_list: <p>Tags to apply to the destination backup during creation. If you specify tags, only these tags will be applied to the destination backup. If you do not specify tags, the service copies tags from the source backup to the destination backup.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_tag_exception.CloudHsmTagException: <p>The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.copy_backup_to_region_request.CopyBackupToRegionRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.copy_backup_to_region_response.CopyBackupToRegionResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.copy_backup_to_region

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.copy_backup_to_region.async_copy_backup_to_region(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.copy_backup_to_region_request.CopyBackupToRegionRequest = {
            "destination_region": destination_region,
            "backup_id": backup_id,
        }
        if tag_list is not None:
            input_["tag_list"] = tag_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cluster(
        self,
        hsm_type: "capo_cloudhsm_v2.types.hsm_type.HsmType",
        subnet_ids: "capo_cloudhsm_v2.types.subnet_ids.SubnetIds",
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
        backup_retention_policy: Optional[
            "capo_cloudhsm_v2.types.backup_retention_policy.BackupRetentionPolicy"
        ] = None,
        source_backup_id: Optional[
            "capo_cloudhsm_v2.types.backup_arn.BackupArn"
        ] = None,
        network_type: Optional[
            "capo_cloudhsm_v2.types.network_type.NetworkType"
        ] = None,
        tag_list: Optional["capo_cloudhsm_v2.types.tag_list.TagList"] = None,
        mode: Optional["capo_cloudhsm_v2.types.cluster_mode.ClusterMode"] = None,
    ) -> "capo_cloudhsm_v2.types.create_cluster_response.CreateClusterResponse":
        """<p>Creates a new CloudHSM cluster.</p> <p> <b>Cross-account use:</b> Yes. To perform this operation with an CloudHSM backup in a different AWS account, specify the full backup ARN in the value of the SourceBackupId parameter.</p>

        Args:
            backup_retention_policy: <p>A policy that defines how the service retains backups.</p>
            hsm_type: <p>The type of HSM to use in the cluster. The allowed values are <code>hsm1.medium</code> and <code>hsm2m.medium</code>.</p>
            source_backup_id: <p>The identifier (ID) or the Amazon Resource Name (ARN) of the cluster backup to restore. Use this value to restore the cluster from a backup instead of creating a new cluster. To find the backup ID or ARN, use <a>DescribeBackups</a>. <i>If using a backup in another account, the full ARN must be supplied.</i> </p>
            subnet_ids: <p>The identifiers (IDs) of the subnets where you are creating the cluster. You must specify at least one subnet. If you specify multiple subnets, they must meet the following criteria:</p> <ul> <li> <p>All subnets must be in the same virtual private cloud (VPC).</p> </li> <li> <p>You can specify only one subnet per Availability Zone.</p> </li> </ul>
            network_type: <p>The NetworkType to create a cluster with. The allowed values are <code>IPV4</code> and <code>DUALSTACK</code>. </p>
            tag_list: <p>Tags to apply to the CloudHSM cluster during creation.</p>
            mode: <p>The mode to use in the cluster. The allowed values are <code>FIPS</code> and <code>NON_FIPS</code>.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_tag_exception.CloudHsmTagException: <p>The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.create_cluster_request.CreateClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.create_cluster_response.CreateClusterResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.create_cluster

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.create_cluster.async_create_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.create_cluster_request.CreateClusterRequest = {
            "hsm_type": hsm_type,
            "subnet_ids": subnet_ids,
        }
        if backup_retention_policy is not None:
            input_["backup_retention_policy"] = backup_retention_policy
        if source_backup_id is not None:
            input_["source_backup_id"] = source_backup_id
        if network_type is not None:
            input_["network_type"] = network_type
        if tag_list is not None:
            input_["tag_list"] = tag_list
        if mode is not None:
            input_["mode"] = mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_hsm(
        self,
        cluster_id: "capo_cloudhsm_v2.types.cluster_id.ClusterId",
        availability_zone: "capo_cloudhsm_v2.types.external_az.ExternalAz",
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
        ip_address: Optional["capo_cloudhsm_v2.types.ip_address.IpAddress"] = None,
    ) -> "capo_cloudhsm_v2.types.create_hsm_response.CreateHsmResponse":
        """<p>Creates a new hardware security module (HSM) in the specified CloudHSM cluster.</p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM cluster in a different Amazon Web Service account.</p>

        Args:
            cluster_id: <p>The identifier (ID) of the HSM's cluster. To find the cluster ID, use <a>DescribeClusters</a>.</p>
            availability_zone: <p>The Availability Zone where you are creating the HSM. To find the cluster's Availability Zones, use <a>DescribeClusters</a>.</p>
            ip_address: <p>The HSM's IP address. If you specify an IP address, use an available address from the subnet that maps to the Availability Zone where you are creating the HSM. If you don't specify an IP address, one is chosen for you from that subnet.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.create_hsm_request.CreateHsmRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.create_hsm_response.CreateHsmResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.create_hsm

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.create_hsm.async_create_hsm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.create_hsm_request.CreateHsmRequest = {
            "cluster_id": cluster_id,
            "availability_zone": availability_zone,
        }
        if ip_address is not None:
            input_["ip_address"] = ip_address

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_backup(
        self,
        backup_id: "capo_cloudhsm_v2.types.backup_id.BackupId",
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
    ) -> "capo_cloudhsm_v2.types.delete_backup_response.DeleteBackupResponse":
        """<p>Deletes a specified CloudHSM backup. A backup can be restored up to 7 days after the DeleteBackup request is made. For more information on restoring a backup, see <a>RestoreBackup</a>.</p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM backup in a different Amazon Web Services account.</p>

        Args:
            backup_id: <p>The ID of the backup to be deleted. To find the ID of a backup, use the <a>DescribeBackups</a> operation.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.delete_backup_request.DeleteBackupRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.delete_backup_response.DeleteBackupResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.delete_backup

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.delete_backup.async_delete_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.delete_backup_request.DeleteBackupRequest = {
            "backup_id": backup_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cluster(
        self,
        cluster_id: "capo_cloudhsm_v2.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
    ) -> "capo_cloudhsm_v2.types.delete_cluster_response.DeleteClusterResponse":
        """<p>Deletes the specified CloudHSM cluster. Before you can delete a cluster, you must delete all HSMs in the cluster. To see if the cluster contains any HSMs, use <a>DescribeClusters</a>. To delete an HSM, use <a>DeleteHsm</a>.</p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM cluster in a different Amazon Web Services account.</p>

        Args:
            cluster_id: <p>The identifier (ID) of the cluster that you are deleting. To find the cluster ID, use <a>DescribeClusters</a>.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_tag_exception.CloudHsmTagException: <p>The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.delete_cluster

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.delete_cluster.async_delete_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.delete_cluster_request.DeleteClusterRequest = {
            "cluster_id": cluster_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_hsm(
        self,
        cluster_id: "capo_cloudhsm_v2.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
        hsm_id: Optional["capo_cloudhsm_v2.types.hsm_id.HsmId"] = None,
        eni_id: Optional["capo_cloudhsm_v2.types.eni_id.EniId"] = None,
        eni_ip: Optional["capo_cloudhsm_v2.types.ip_address.IpAddress"] = None,
    ) -> "capo_cloudhsm_v2.types.delete_hsm_response.DeleteHsmResponse":
        """<p>Deletes the specified HSM. To specify an HSM, you can use its identifier (ID), the IP address of the HSM's elastic network interface (ENI), or the ID of the HSM's ENI. You need to specify only one of these values. To find these values, use <a>DescribeClusters</a>.</p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM hsm in a different Amazon Web Services account.</p>

        Args:
            cluster_id: <p>The identifier (ID) of the cluster that contains the HSM that you are deleting.</p>
            hsm_id: <p>The identifier (ID) of the HSM that you are deleting.</p>
            eni_id: <p>The identifier (ID) of the elastic network interface (ENI) of the HSM that you are deleting.</p>
            eni_ip: <p>The IP address of the elastic network interface (ENI) of the HSM that you are deleting.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.delete_hsm_request.DeleteHsmRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.delete_hsm_response.DeleteHsmResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.delete_hsm

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.delete_hsm.async_delete_hsm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.delete_hsm_request.DeleteHsmRequest = {
            "cluster_id": cluster_id
        }
        if hsm_id is not None:
            input_["hsm_id"] = hsm_id
        if eni_id is not None:
            input_["eni_id"] = eni_id
        if eni_ip is not None:
            input_["eni_ip"] = eni_ip

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
        resource_arn: Optional[
            "capo_cloudhsm_v2.types.cloud_hsm_arn.CloudHsmArn"
        ] = None,
    ) -> "capo_cloudhsm_v2.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p> Deletes an CloudHSM resource policy. Deleting a resource policy will result in the resource being unshared and removed from any RAM resource shares. Deleting the resource policy attached to a backup will not impact any clusters created from that backup.</p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM resource in a different Amazon Web Services account.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource from which the policy will be removed. </p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_backups(
        self,
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
        next_token: Optional["capo_cloudhsm_v2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudhsm_v2.types.backups_max_size.BackupsMaxSize"
        ] = None,
        filters: Optional["capo_cloudhsm_v2.types.filters.Filters"] = None,
        shared: Optional["capo_cloudhsm_v2.types.boolean.Boolean"] = None,
        sort_ascending: Optional["capo_cloudhsm_v2.types.boolean.Boolean"] = None,
    ) -> "capo_cloudhsm_v2.types.describe_backups_response.DescribeBackupsResponse":
        """<p>Gets information about backups of CloudHSM clusters. Lists either the backups you own or the backups shared with you when the Shared parameter is true.</p> <p>This is a paginated operation, which means that each response might contain only a subset of all the backups. When the response contains only a subset of backups, it includes a <code>NextToken</code> value. Use this value in a subsequent <code>DescribeBackups</code> request to get more backups. When you receive a response with no <code>NextToken</code> (or an empty or null value), that means there are no more backups to get.</p> <p> <b>Cross-account use:</b> Yes. Customers can describe backups in other Amazon Web Services accounts that are shared with them.</p>

        Args:
            next_token: <p>The <code>NextToken</code> value that you received in the previous response. Use this value to get more backups.</p>
            max_results: <p>The maximum number of backups to return in the response. When there are more backups than the number you specify, the response contains a <code>NextToken</code> value.</p>
            filters: <p>One or more filters to limit the items returned in the response.</p> <p>Use the <code>backupIds</code> filter to return only the specified backups. Specify backups by their backup identifier (ID).</p> <p>Use the <code>sourceBackupIds</code> filter to return only the backups created from a source backup. The <code>sourceBackupID</code> of a source backup is returned by the <a>CopyBackupToRegion</a> operation.</p> <p>Use the <code>clusterIds</code> filter to return only the backups for the specified clusters. Specify clusters by their cluster identifier (ID).</p> <p>Use the <code>states</code> filter to return only backups that match the specified state.</p> <p>Use the <code>neverExpires</code> filter to return backups filtered by the value in the <code>neverExpires</code> parameter. <code>True</code> returns all backups exempt from the backup retention policy. <code>False</code> returns all backups with a backup retention policy defined at the cluster.</p>
            shared: <p>Describe backups that are shared with you.</p> <note> <p>By default when using this option, the command returns backups that have been shared using a standard Resource Access Manager resource share. In order for a backup that was shared using the PutResourcePolicy command to be returned, the share must be promoted to a standard resource share using the RAM <a href="https://docs.aws.amazon.com/cli/latest/reference/ram/promote-resource-share-created-from-policy.html">PromoteResourceShareCreatedFromPolicy</a> API operation. For more information about sharing backups, see <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/sharing.html"> Working with shared backups</a> in the CloudHSM User Guide.</p> </note>
            sort_ascending: <p>Designates whether or not to sort the return backups by ascending chronological order of generation.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_tag_exception.CloudHsmTagException: <p>The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.describe_backups_request.DescribeBackupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.describe_backups_response.DescribeBackupsResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.describe_backups

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.describe_backups.async_describe_backups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.describe_backups_request.DescribeBackupsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if shared is not None:
            input_["shared"] = shared
        if sort_ascending is not None:
            input_["sort_ascending"] = sort_ascending

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_backups(
        self,
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
        next_token: Optional["capo_cloudhsm_v2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudhsm_v2.types.backups_max_size.BackupsMaxSize"
        ] = None,
        filters: Optional["capo_cloudhsm_v2.types.filters.Filters"] = None,
        shared: Optional["capo_cloudhsm_v2.types.boolean.Boolean"] = None,
        sort_ascending: Optional["capo_cloudhsm_v2.types.boolean.Boolean"] = None,
    ) -> "AsyncIterator[capo_cloudhsm_v2.types.describe_backups_response.DescribeBackupsResponse]":
        _token = next_token
        while True:
            _response = await self.describe_backups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
                shared=shared,
                sort_ascending=sort_ascending,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_clusters(
        self,
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
        filters: Optional["capo_cloudhsm_v2.types.filters.Filters"] = None,
        next_token: Optional["capo_cloudhsm_v2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudhsm_v2.types.clusters_max_size.ClustersMaxSize"
        ] = None,
    ) -> "capo_cloudhsm_v2.types.describe_clusters_response.DescribeClustersResponse":
        """<p>Gets information about CloudHSM clusters.</p> <p>This is a paginated operation, which means that each response might contain only a subset of all the clusters. When the response contains only a subset of clusters, it includes a <code>NextToken</code> value. Use this value in a subsequent <code>DescribeClusters</code> request to get more clusters. When you receive a response with no <code>NextToken</code> (or an empty or null value), that means there are no more clusters to get.</p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on CloudHSM clusters in a different Amazon Web Services account.</p>

        Args:
            filters: <p>One or more filters to limit the items returned in the response.</p> <p>Use the <code>clusterIds</code> filter to return only the specified clusters. Specify clusters by their cluster identifier (ID).</p> <p>Use the <code>vpcIds</code> filter to return only the clusters in the specified virtual private clouds (VPCs). Specify VPCs by their VPC identifier (ID).</p> <p>Use the <code>states</code> filter to return only clusters that match the specified state.</p>
            next_token: <p>The <code>NextToken</code> value that you received in the previous response. Use this value to get more clusters.</p>
            max_results: <p>The maximum number of clusters to return in the response. When there are more clusters than the number you specify, the response contains a <code>NextToken</code> value.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_tag_exception.CloudHsmTagException: <p>The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.describe_clusters_request.DescribeClustersRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.describe_clusters_response.DescribeClustersResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.describe_clusters

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.describe_clusters.async_describe_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.describe_clusters_request.DescribeClustersRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_clusters(
        self,
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
        filters: Optional["capo_cloudhsm_v2.types.filters.Filters"] = None,
        next_token: Optional["capo_cloudhsm_v2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudhsm_v2.types.clusters_max_size.ClustersMaxSize"
        ] = None,
    ) -> "AsyncIterator[capo_cloudhsm_v2.types.describe_clusters_response.DescribeClustersResponse]":
        _token = next_token
        while True:
            _response = await self.describe_clusters(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_resource_policy(
        self,
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
        resource_arn: Optional[
            "capo_cloudhsm_v2.types.cloud_hsm_arn.CloudHsmArn"
        ] = None,
    ) -> (
        "capo_cloudhsm_v2.types.get_resource_policy_response.GetResourcePolicyResponse"
    ):
        """<p> Retrieves the resource policy document attached to a given resource. </p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM resource in a different Amazon Web Services account.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource to which a policy is attached.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.get_resource_policy_request.GetResourcePolicyRequest = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def initialize_cluster(
        self,
        cluster_id: "capo_cloudhsm_v2.types.cluster_id.ClusterId",
        signed_cert: "capo_cloudhsm_v2.types.cert.Cert",
        trust_anchor: "capo_cloudhsm_v2.types.cert.Cert",
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
    ) -> "capo_cloudhsm_v2.types.initialize_cluster_response.InitializeClusterResponse":
        """<p>Claims an CloudHSM cluster by submitting the cluster certificate issued by your issuing certificate authority (CA) and the CA's root certificate. Before you can claim a cluster, you must sign the cluster's certificate signing request (CSR) with your issuing CA. To get the cluster's CSR, use <a>DescribeClusters</a>.</p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM cluster in a different Amazon Web Services account.</p>

        Args:
            cluster_id: <p>The identifier (ID) of the cluster that you are claiming. To find the cluster ID, use <a>DescribeClusters</a>.</p>
            signed_cert: <p>The cluster certificate issued (signed) by your issuing certificate authority (CA). The certificate must be in PEM format and can contain a maximum of 5000 characters.</p>
            trust_anchor: <p>The issuing certificate of the issuing certificate authority (CA) that issued (signed) the cluster certificate. You must use a self-signed certificate. The certificate used to sign the HSM CSR must be directly available, and thus must be the root certificate. The certificate must be in PEM format and can contain a maximum of 5000 characters.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.initialize_cluster_request.InitializeClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.initialize_cluster_response.InitializeClusterResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.initialize_cluster

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.initialize_cluster.async_initialize_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.initialize_cluster_request.InitializeClusterRequest = {
            "cluster_id": cluster_id,
            "signed_cert": signed_cert,
            "trust_anchor": trust_anchor,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags(
        self,
        resource_id: "capo_cloudhsm_v2.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
        next_token: Optional["capo_cloudhsm_v2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cloudhsm_v2.types.max_size.MaxSize"] = None,
    ) -> "capo_cloudhsm_v2.types.list_tags_response.ListTagsResponse":
        """<p>Gets a list of tags for the specified CloudHSM cluster.</p> <p>This is a paginated operation, which means that each response might contain only a subset of all the tags. When the response contains only a subset of tags, it includes a <code>NextToken</code> value. Use this value in a subsequent <code>ListTags</code> request to get more tags. When you receive a response with no <code>NextToken</code> (or an empty or null value), that means there are no more tags to get.</p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM resource in a different Amazon Web Services account.</p>

        Args:
            resource_id: <p>The cluster identifier (ID) for the cluster whose tags you are getting. To find the cluster ID, use <a>DescribeClusters</a>.</p>
            next_token: <p>The <code>NextToken</code> value that you received in the previous response. Use this value to get more tags.</p>
            max_results: <p>The maximum number of tags to return in the response. When there are more tags than the number you specify, the response contains a <code>NextToken</code> value.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_tag_exception.CloudHsmTagException: <p>The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.list_tags_request.ListTagsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.list_tags_response.ListTagsResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.list_tags

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.list_tags.async_list_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.list_tags_request.ListTagsRequest = {
            "resource_id": resource_id
        }
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

    async def iter_list_tags(
        self,
        resource_id: "capo_cloudhsm_v2.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
        next_token: Optional["capo_cloudhsm_v2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cloudhsm_v2.types.max_size.MaxSize"] = None,
    ) -> "AsyncIterator[capo_cloudhsm_v2.types.list_tags_response.ListTagsResponse]":
        _token = next_token
        while True:
            _response = await self.list_tags(
                resource_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def modify_backup_attributes(
        self,
        backup_id: "capo_cloudhsm_v2.types.backup_id.BackupId",
        never_expires: "capo_cloudhsm_v2.types.boolean.Boolean",
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
    ) -> "capo_cloudhsm_v2.types.modify_backup_attributes_response.ModifyBackupAttributesResponse":
        """<p>Modifies attributes for CloudHSM backup.</p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM backup in a different Amazon Web Services account.</p>

        Args:
            backup_id: <p>The identifier (ID) of the backup to modify. To find the ID of a backup, use the <a>DescribeBackups</a> operation.</p>
            never_expires: <p>Specifies whether the service should exempt a backup from the retention policy for the cluster. <code>True</code> exempts a backup from the retention policy. <code>False</code> means the service applies the backup retention policy defined at the cluster.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.modify_backup_attributes_request.ModifyBackupAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.modify_backup_attributes_response.ModifyBackupAttributesResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.modify_backup_attributes

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.modify_backup_attributes.async_modify_backup_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.modify_backup_attributes_request.ModifyBackupAttributesRequest = {
            "backup_id": backup_id,
            "never_expires": never_expires,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_cluster(
        self,
        cluster_id: "capo_cloudhsm_v2.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
        hsm_type: Optional["capo_cloudhsm_v2.types.hsm_type.HsmType"] = None,
        backup_retention_policy: Optional[
            "capo_cloudhsm_v2.types.backup_retention_policy.BackupRetentionPolicy"
        ] = None,
    ) -> "capo_cloudhsm_v2.types.modify_cluster_response.ModifyClusterResponse":
        """<p>Modifies CloudHSM cluster.</p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM cluster in a different Amazon Web Services account.</p>

        Args:
            hsm_type: <p>The desired HSM type of the cluster.</p>
            backup_retention_policy: <p>A policy that defines how the service retains backups.</p>
            cluster_id: <p>The identifier (ID) of the cluster that you want to modify. To find the cluster ID, use <a>DescribeClusters</a>.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.modify_cluster_request.ModifyClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.modify_cluster_response.ModifyClusterResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.modify_cluster

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.modify_cluster.async_modify_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.modify_cluster_request.ModifyClusterRequest = {
            "cluster_id": cluster_id
        }
        if hsm_type is not None:
            input_["hsm_type"] = hsm_type
        if backup_retention_policy is not None:
            input_["backup_retention_policy"] = backup_retention_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_policy(
        self,
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
        resource_arn: Optional[
            "capo_cloudhsm_v2.types.cloud_hsm_arn.CloudHsmArn"
        ] = None,
        policy: Optional[
            "capo_cloudhsm_v2.types.resource_policy.ResourcePolicy"
        ] = None,
    ) -> (
        "capo_cloudhsm_v2.types.put_resource_policy_response.PutResourcePolicyResponse"
    ):
        """<p>Creates or updates an CloudHSM resource policy. A resource policy helps you to define the IAM entity (for example, an Amazon Web Services account) that can manage your CloudHSM resources. The following resources support CloudHSM resource policies: </p> <ul> <li> <p> Backup - The resource policy allows you to describe the backup and restore a cluster from the backup in another Amazon Web Services account.</p> </li> </ul> <p>In order to share a backup, it must be in a 'READY' state and you must own it.</p> <important> <p>While you can share a backup using the CloudHSM PutResourcePolicy operation, we recommend using Resource Access Manager (RAM) instead. Using RAM provides multiple benefits as it creates the policy for you, allows multiple resources to be shared at one time, and increases the discoverability of shared resources. If you use PutResourcePolicy and want consumers to be able to describe the backups you share with them, you must promote the backup to a standard RAM Resource Share using the RAM PromoteResourceShareCreatedFromPolicy API operation. For more information, see <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/sharing.html"> Working with shared backups</a> in the CloudHSM User Guide</p> </important> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM resource in a different Amazon Web Services account.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource to which you want to attach a policy. </p>
            policy: <p>The policy you want to associate with a resource. </p> <p>For an example policy, see <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/sharing.html"> Working with shared backups</a> in the CloudHSM User Guide</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.put_resource_policy_request.PutResourcePolicyRequest = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if policy is not None:
            input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_backup(
        self,
        backup_id: "capo_cloudhsm_v2.types.backup_id.BackupId",
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
    ) -> "capo_cloudhsm_v2.types.restore_backup_response.RestoreBackupResponse":
        """<p>Restores a specified CloudHSM backup that is in the <code>PENDING_DELETION</code> state. For more information on deleting a backup, see <a>DeleteBackup</a>.</p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM backup in a different Amazon Web Services account.</p>

        Args:
            backup_id: <p>The ID of the backup to be restored. To find the ID of a backup, use the <a>DescribeBackups</a> operation.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.restore_backup_request.RestoreBackupRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.restore_backup_response.RestoreBackupResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.restore_backup

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.restore_backup.async_restore_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.restore_backup_request.RestoreBackupRequest = {
            "backup_id": backup_id
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
        resource_id: "capo_cloudhsm_v2.types.resource_id.ResourceId",
        tag_list: "capo_cloudhsm_v2.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
    ) -> "capo_cloudhsm_v2.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or overwrites one or more tags for the specified CloudHSM cluster.</p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM resource in a different Amazon Web Services account.</p>

        Args:
            resource_id: <p>The cluster identifier (ID) for the cluster that you are tagging. To find the cluster ID, use <a>DescribeClusters</a>.</p>
            tag_list: <p>A list of one or more tags.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_limit_exceeded_exception.CloudHsmResourceLimitExceededException: <p>The request was rejected because it exceeds an CloudHSM limit.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_tag_exception.CloudHsmTagException: <p>The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.tag_resource_request.TagResourceRequest = {
            "resource_id": resource_id,
            "tag_list": tag_list,
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
        resource_id: "capo_cloudhsm_v2.types.resource_id.ResourceId",
        tag_key_list: "capo_cloudhsm_v2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncCloudHSMV2ClientConfig] = None,
    ) -> "capo_cloudhsm_v2.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tag or tags from the specified CloudHSM cluster.</p> <p> <b>Cross-account use:</b> No. You cannot perform this operation on an CloudHSM resource in a different Amazon Web Services account.</p>

        Args:
            resource_id: <p>The cluster identifier (ID) for the cluster whose tags you are removing. To find the cluster ID, use <a>DescribeClusters</a>.</p>
            tag_key_list: <p>A list of one or more tag keys for the tags that you are removing. Specify only the tag keys, not the tag values.</p>

        Raises:
            capo_cloudhsm_v2.errors.cloud_hsm_access_denied_exception.CloudHsmAccessDeniedException: <p>The request was rejected because the requester does not have permission to perform the requested operation.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_internal_failure_exception.CloudHsmInternalFailureException: <p>The request was rejected because of an CloudHSM internal failure. The request can be retried.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_invalid_request_exception.CloudHsmInvalidRequestException: <p>The request was rejected because it is not a valid request.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_resource_not_found_exception.CloudHsmResourceNotFoundException: <p>The request was rejected because it refers to a resource that cannot be found.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>The request was rejected because an error occurred.</p>
            capo_cloudhsm_v2.errors.cloud_hsm_tag_exception.CloudHsmTagException: <p>The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.</p>
            capo_cloudhsm_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudhsm_v2.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_cloudhsm_v2.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_cloudhsm_v2._operations.baldr_api_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_cloudhsm_v2._operations.baldr_api_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm_v2.types.untag_resource_request.UntagResourceRequest = {
            "resource_id": resource_id,
            "tag_key_list": tag_key_list,
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
