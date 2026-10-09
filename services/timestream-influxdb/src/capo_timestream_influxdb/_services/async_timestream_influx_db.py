"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#AmazonTimestreamInfluxDB``."""

import datetime
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_timestream_influxdb._auth._signers
import capo_timestream_influxdb._auth._sigv4
from capo_timestream_influxdb._auth._identity import Credentials
from capo_timestream_influxdb._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_timestream_influxdb._auth._zapros_handler import AuthMiddleware
from capo_timestream_influxdb._pagination import resolve_path as _resolve_path
from capo_timestream_influxdb._resources.amazon_timestream_influx_db.db_backup_resource import (
    AsyncDbBackupResource,
)
from capo_timestream_influxdb._resources.amazon_timestream_influx_db.db_cluster_resource import (
    AsyncDbClusterResource,
)
from capo_timestream_influxdb._resources.amazon_timestream_influx_db.db_instance_resource import (
    AsyncDbInstanceResource,
)
from capo_timestream_influxdb._resources.amazon_timestream_influx_db.db_parameter_group_resource import (
    AsyncDbParameterGroupResource,
)
from capo_timestream_influxdb._services._aws_config import aaws_config
from capo_timestream_influxdb._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.allocated_storage
    import capo_timestream_influxdb.types.arn
    import capo_timestream_influxdb.types.bucket
    import capo_timestream_influxdb.types.cluster_deployment_type
    import capo_timestream_influxdb.types.create_db_backup_input
    import capo_timestream_influxdb.types.create_db_backup_output
    import capo_timestream_influxdb.types.create_db_cluster_input
    import capo_timestream_influxdb.types.create_db_cluster_output
    import capo_timestream_influxdb.types.create_db_instance_input
    import capo_timestream_influxdb.types.create_db_instance_output
    import capo_timestream_influxdb.types.create_db_parameter_group_input
    import capo_timestream_influxdb.types.create_db_parameter_group_output
    import capo_timestream_influxdb.types.db_backup_configuration_input_list
    import capo_timestream_influxdb.types.db_backup_id
    import capo_timestream_influxdb.types.db_backup_name
    import capo_timestream_influxdb.types.db_backup_summary
    import capo_timestream_influxdb.types.db_cluster_id
    import capo_timestream_influxdb.types.db_cluster_name
    import capo_timestream_influxdb.types.db_cluster_summary
    import capo_timestream_influxdb.types.db_instance_for_cluster_summary
    import capo_timestream_influxdb.types.db_instance_id_list
    import capo_timestream_influxdb.types.db_instance_identifier
    import capo_timestream_influxdb.types.db_instance_name
    import capo_timestream_influxdb.types.db_instance_summary
    import capo_timestream_influxdb.types.db_instance_type
    import capo_timestream_influxdb.types.db_parameter_group_identifier
    import capo_timestream_influxdb.types.db_parameter_group_name
    import capo_timestream_influxdb.types.db_parameter_group_summary
    import capo_timestream_influxdb.types.db_resource_id
    import capo_timestream_influxdb.types.db_resource_name
    import capo_timestream_influxdb.types.db_storage_type
    import capo_timestream_influxdb.types.delete_db_backup_input
    import capo_timestream_influxdb.types.delete_db_backup_output
    import capo_timestream_influxdb.types.delete_db_cluster_input
    import capo_timestream_influxdb.types.delete_db_cluster_output
    import capo_timestream_influxdb.types.delete_db_instance_input
    import capo_timestream_influxdb.types.delete_db_instance_output
    import capo_timestream_influxdb.types.deployment_type
    import capo_timestream_influxdb.types.failover_mode
    import capo_timestream_influxdb.types.get_db_backup_input
    import capo_timestream_influxdb.types.get_db_backup_output
    import capo_timestream_influxdb.types.get_db_cluster_input
    import capo_timestream_influxdb.types.get_db_cluster_output
    import capo_timestream_influxdb.types.get_db_instance_input
    import capo_timestream_influxdb.types.get_db_instance_output
    import capo_timestream_influxdb.types.get_db_parameter_group_input
    import capo_timestream_influxdb.types.get_db_parameter_group_output
    import capo_timestream_influxdb.types.kms_key_id
    import capo_timestream_influxdb.types.list_db_backups_input
    import capo_timestream_influxdb.types.list_db_backups_output
    import capo_timestream_influxdb.types.list_db_clusters_input
    import capo_timestream_influxdb.types.list_db_clusters_output
    import capo_timestream_influxdb.types.list_db_instances_for_cluster_input
    import capo_timestream_influxdb.types.list_db_instances_for_cluster_output
    import capo_timestream_influxdb.types.list_db_instances_input
    import capo_timestream_influxdb.types.list_db_instances_output
    import capo_timestream_influxdb.types.list_db_parameter_groups_input
    import capo_timestream_influxdb.types.list_db_parameter_groups_output
    import capo_timestream_influxdb.types.list_tags_for_resource_request
    import capo_timestream_influxdb.types.list_tags_for_resource_response
    import capo_timestream_influxdb.types.log_delivery_configuration
    import capo_timestream_influxdb.types.maintenance_schedule
    import capo_timestream_influxdb.types.max_results
    import capo_timestream_influxdb.types.network_type
    import capo_timestream_influxdb.types.next_token
    import capo_timestream_influxdb.types.organization
    import capo_timestream_influxdb.types.parameters
    import capo_timestream_influxdb.types.password
    import capo_timestream_influxdb.types.port
    import capo_timestream_influxdb.types.reboot_db_cluster_input
    import capo_timestream_influxdb.types.reboot_db_cluster_output
    import capo_timestream_influxdb.types.reboot_db_instance_input
    import capo_timestream_influxdb.types.reboot_db_instance_output
    import capo_timestream_influxdb.types.request_tag_map
    import capo_timestream_influxdb.types.resource_deployment_type
    import capo_timestream_influxdb.types.restore_from_db_backup_input
    import capo_timestream_influxdb.types.restore_from_db_backup_output
    import capo_timestream_influxdb.types.restore_mode
    import capo_timestream_influxdb.types.retention_days
    import capo_timestream_influxdb.types.tag_keys
    import capo_timestream_influxdb.types.tag_resource_request
    import capo_timestream_influxdb.types.untag_resource_request
    import capo_timestream_influxdb.types.update_db_cluster_input
    import capo_timestream_influxdb.types.update_db_cluster_output
    import capo_timestream_influxdb.types.update_db_instance_input
    import capo_timestream_influxdb.types.update_db_instance_output
    import capo_timestream_influxdb.types.username
    import capo_timestream_influxdb.types.vpc_security_group_id_list
    import capo_timestream_influxdb.types.vpc_subnet_id_list


class AsyncTimestreamInfluxDBClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncTimestreamInfluxDBClient:
    """A client for the ``TimestreamInfluxDB`` service.

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
        self._config = AsyncTimestreamInfluxDBClientConfig(
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

        # resources
        self.db_backup_resource = AsyncDbBackupResource(self)
        self.db_cluster_resource = AsyncDbClusterResource(self)
        self.db_instance_resource = AsyncDbInstanceResource(self)
        self.db_parameter_group_resource = AsyncDbParameterGroupResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncTimestreamInfluxDBClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_timestream_influxdb.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>A list of tags applied to the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the tagged resource.</p>

        Raises:
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        resource_arn: "capo_timestream_influxdb.types.arn.Arn",
        tags: "capo_timestream_influxdb.types.request_tag_map.RequestTagMap",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
    ) -> None:
        """<p>Tags are composed of a Key/Value pairs. You can use tags to categorize and track your Timestream for InfluxDB resources.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the tagged resource.</p>
            tags: <p>A list of tags used to categorize and track resources.</p>

        Raises:
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.tag_resource

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
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
        resource_arn: "capo_timestream_influxdb.types.arn.Arn",
        tag_keys: "capo_timestream_influxdb.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
    ) -> None:
        """<p>Removes the tag from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the tagged resource.</p>
            tag_keys: <p>The keys used to identify the tags.</p>

        Raises:
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.untag_resource

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_db_backup(
        self,
        name: "capo_timestream_influxdb.types.db_backup_name.DbBackupName",
        db_resource_id: "capo_timestream_influxdb.types.db_resource_id.DbResourceId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        retention_days: Optional[
            "capo_timestream_influxdb.types.retention_days.RetentionDays"
        ] = None,
        tags: Optional[
            "capo_timestream_influxdb.types.request_tag_map.RequestTagMap"
        ] = None,
    ) -> "capo_timestream_influxdb.types.create_db_backup_output.CreateDbBackupOutput":
        """<p>Creates a new on-demand backup of a Timestream for InfluxDB resource.</p>

        Args:
            name: <p>The name of the backup. Must be unique within the account and region.</p>
            db_resource_id: <p>The id of the DB instance or DB cluster to back up.</p>
            retention_days: <p>The number of days to retain the backup. Valid values are 1 to 3650.</p>
            tags: <p>A list of key-value pairs to associate with the backup.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.create_db_backup_input.CreateDbBackupInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.create_db_backup_output.CreateDbBackupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_backup

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_backup.async_create_db_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.create_db_backup_input.CreateDbBackupInput = {
            "name": name,
            "db_resource_id": db_resource_id,
        }
        if retention_days is not None:
            input_["retention_days"] = retention_days
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_db_backup(
        self,
        identifier: "capo_timestream_influxdb.types.db_backup_id.DbBackupId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.get_db_backup_output.GetDbBackupOutput":
        """<p>Returns information about a specific Timestream for InfluxDB backup.</p>

        Args:
            identifier: <p>The identifier of the backup to retrieve information for.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.get_db_backup_input.GetDbBackupInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.get_db_backup_output.GetDbBackupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_backup

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_backup.async_get_db_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.get_db_backup_input.GetDbBackupInput = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_db_backup(
        self,
        identifier: "capo_timestream_influxdb.types.db_backup_id.DbBackupId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.delete_db_backup_output.DeleteDbBackupOutput":
        """<p>Deletes a Timestream for InfluxDB backup.</p>

        Args:
            identifier: <p>The identifier of the backup to delete.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.delete_db_backup_input.DeleteDbBackupInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.delete_db_backup_output.DeleteDbBackupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.delete_db_backup

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.delete_db_backup.async_delete_db_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.delete_db_backup_input.DeleteDbBackupInput = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_db_backups(
        self,
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        db_resource_id: Optional[
            "capo_timestream_influxdb.types.db_resource_id.DbResourceId"
        ] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_timestream_influxdb.types.list_db_backups_output.ListDbBackupsOutput":
        """<p>Returns a list of Timestream for InfluxDB backups.</p>

        Args:
            db_resource_id: <p>The identifier of the DB instance or DB cluster to list backups for. If not specified, returns all backups in the account and region.</p>
            next_token: <p>The pagination token. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>
            max_results: <p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a nextToken is provided in the output. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.list_db_backups_input.ListDbBackupsInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.list_db_backups_output.ListDbBackupsOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_backups

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_backups.async_list_db_backups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.list_db_backups_input.ListDbBackupsInput = {}
        if db_resource_id is not None:
            input_["db_resource_id"] = db_resource_id
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

    async def iter_list_db_backups(
        self,
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        db_resource_id: Optional[
            "capo_timestream_influxdb.types.db_resource_id.DbResourceId"
        ] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_timestream_influxdb.types.db_backup_summary.DbBackupSummary]":
        _token = next_token
        while True:
            _response = await self.list_db_backups(
                config_overrides=config_overrides,
                db_resource_id=db_resource_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def restore_from_db_backup(
        self,
        name: "capo_timestream_influxdb.types.db_resource_name.DbResourceName",
        db_backup_id: "capo_timestream_influxdb.types.db_backup_id.DbBackupId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        restore_to_time: Optional[datetime.datetime] = None,
        restore_mode: Optional[
            "capo_timestream_influxdb.types.restore_mode.RestoreMode"
        ] = None,
        vpc_subnet_ids: Optional[
            "capo_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList"
        ] = None,
        vpc_security_group_ids: Optional[
            "capo_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        publicly_accessible: Optional[bool] = None,
        log_delivery_configuration: Optional[
            "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
        ] = None,
        maintenance_schedule: Optional[
            "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
        ] = None,
        tags: Optional[
            "capo_timestream_influxdb.types.request_tag_map.RequestTagMap"
        ] = None,
        port: Optional["capo_timestream_influxdb.types.port.Port"] = None,
        network_type: Optional[
            "capo_timestream_influxdb.types.network_type.NetworkType"
        ] = None,
        deployment_type: Optional[
            "capo_timestream_influxdb.types.resource_deployment_type.ResourceDeploymentType"
        ] = None,
        db_backup_configurations: Optional[
            "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
        ] = None,
        kms_key_id: Optional[
            "capo_timestream_influxdb.types.kms_key_id.KmsKeyId"
        ] = None,
    ) -> "capo_timestream_influxdb.types.restore_from_db_backup_output.RestoreFromDbBackupOutput":
        """<p>Restores a Timestream for InfluxDB resource from a backup. By default, a new resource is created. You can optionally restore to the same resource using the REPLACE_EXISTING restore mode.</p>

        Args:
            name: <p>The name of the new resource to create from the restore. If restoring to an existing resource, the name must match the existing resource name.</p>
            db_backup_id: <p>The identifier of the backup to restore from.</p>
            restore_to_time: <p>The point in time to restore to, for continuous backups. Must be within the backup's retention window.</p>
            restore_mode: <p>Specifies whether to restore to a new resource or replace the existing resource. Valid values are NEW_RESOURCE (default) and REPLACE_EXISTING.</p>
            vpc_subnet_ids: <p>A list of VPC subnet IDs for the restored resource. If not specified, the restored resource uses the same subnets as the backup.</p>
            vpc_security_group_ids: <p>A list of VPC security group IDs for the restored resource. If not specified, the restored resource uses the same security groups as the backup.</p>
            publicly_accessible: <p>Specifies whether the restored resource is publicly accessible.</p>
            log_delivery_configuration: <p>Configuration for sending InfluxDB engine logs to the specified S3 bucket for the restored resource.</p>
            maintenance_schedule: <p>The maintenance schedule for the restored resource.</p>
            tags: <p>A list of key-value pairs to associate with the restored resource.</p>
            port: <p>The port number on which the restored InfluxDB resource accepts connections.</p>
            network_type: <p>Specifies the network type of the restored resource. Valid values are IPV4 and DUAL.</p>
            deployment_type: <p>Specifies the deployment type of the restored resource. Valid values are SINGLE_AZ, WITH_MULTIAZ_STANDBY, and MULTI_NODE_READ_REPLICAS.</p>
            db_backup_configurations: <p>A list of backup configurations to apply to the restored resource.</p>
            kms_key_id: <p>The Amazon Web Services KMS key identifier to use for encryption of the restored resource. Can be a key ID, key ARN, alias name, or alias ARN.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.restore_from_db_backup_input.RestoreFromDbBackupInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.restore_from_db_backup_output.RestoreFromDbBackupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.restore_from_db_backup

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.restore_from_db_backup.async_restore_from_db_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.restore_from_db_backup_input.RestoreFromDbBackupInput = {
            "name": name,
            "db_backup_id": db_backup_id,
        }
        if restore_to_time is not None:
            input_["restore_to_time"] = restore_to_time
        if restore_mode is not None:
            input_["restore_mode"] = restore_mode
        if vpc_subnet_ids is not None:
            input_["vpc_subnet_ids"] = vpc_subnet_ids
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if log_delivery_configuration is not None:
            input_["log_delivery_configuration"] = log_delivery_configuration
        if maintenance_schedule is not None:
            input_["maintenance_schedule"] = maintenance_schedule
        if tags is not None:
            input_["tags"] = tags
        if port is not None:
            input_["port"] = port
        if network_type is not None:
            input_["network_type"] = network_type
        if deployment_type is not None:
            input_["deployment_type"] = deployment_type
        if db_backup_configurations is not None:
            input_["db_backup_configurations"] = db_backup_configurations
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_db_cluster(
        self,
        name: "capo_timestream_influxdb.types.db_cluster_name.DbClusterName",
        db_instance_type: "capo_timestream_influxdb.types.db_instance_type.DbInstanceType",
        vpc_subnet_ids: "capo_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList",
        vpc_security_group_ids: "capo_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        username: Optional["capo_timestream_influxdb.types.username.Username"] = None,
        password: Optional["capo_timestream_influxdb.types.password.Password"] = None,
        organization: Optional[
            "capo_timestream_influxdb.types.organization.Organization"
        ] = None,
        bucket: Optional["capo_timestream_influxdb.types.bucket.Bucket"] = None,
        port: Optional["capo_timestream_influxdb.types.port.Port"] = None,
        db_parameter_group_identifier: Optional[
            "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
        ] = None,
        db_storage_type: Optional[
            "capo_timestream_influxdb.types.db_storage_type.DbStorageType"
        ] = None,
        allocated_storage: Optional[
            "capo_timestream_influxdb.types.allocated_storage.AllocatedStorage"
        ] = None,
        network_type: Optional[
            "capo_timestream_influxdb.types.network_type.NetworkType"
        ] = None,
        publicly_accessible: Optional[bool] = None,
        deployment_type: Optional[
            "capo_timestream_influxdb.types.cluster_deployment_type.ClusterDeploymentType"
        ] = None,
        failover_mode: Optional[
            "capo_timestream_influxdb.types.failover_mode.FailoverMode"
        ] = None,
        log_delivery_configuration: Optional[
            "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
        ] = None,
        maintenance_schedule: Optional[
            "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
        ] = None,
        db_backup_configurations: Optional[
            "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
        ] = None,
        kms_key_id: Optional[
            "capo_timestream_influxdb.types.kms_key_id.KmsKeyId"
        ] = None,
        tags: Optional[
            "capo_timestream_influxdb.types.request_tag_map.RequestTagMap"
        ] = None,
    ) -> (
        "capo_timestream_influxdb.types.create_db_cluster_output.CreateDbClusterOutput"
    ):
        """<p>Creates a new Timestream for InfluxDB cluster.</p>

        Args:
            name: <p>The name that uniquely identifies the DB cluster when interacting with the Amazon Timestream for InfluxDB API and CLI commands. This name will also be a prefix included in the endpoint. DB cluster names must be unique per customer and per region.</p>
            username: <p>The username of the initial admin user created in InfluxDB. Must start with a letter and can't end with a hyphen or contain two consecutive hyphens. For example, my-user1. This username will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a secret created in Secrets Manager in your account.</p>
            password: <p>The password of the initial admin user created in InfluxDB. This password will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a secret created in Secrets Manager in your account.</p>
            organization: <p>The name of the initial organization for the initial admin user in InfluxDB. An InfluxDB organization is a workspace for a group of users.</p>
            bucket: <p>The name of the initial InfluxDB bucket. All InfluxDB data is stored in a bucket. A bucket combines the concept of a database and a retention period (the duration of time that each data point persists). A bucket belongs to an organization.</p>
            port: <p>The port number on which InfluxDB accepts connections.</p> <p>Valid Values: 1024-65535</p> <p>Default: 8086 for InfluxDB v2, 8181 for InfluxDB v3</p> <p>Constraints: The value can't be 2375-2376, 7788-7799, 8090, or 51678-51680</p>
            db_parameter_group_identifier: <p>The ID of the DB parameter group to assign to your DB cluster. DB parameter groups specify how the database is configured. For example, DB parameter groups can specify the limit for query concurrency.</p>
            db_instance_type: <p>The Timestream for InfluxDB DB instance type to run InfluxDB on.</p>
            db_storage_type: <p>The Timestream for InfluxDB DB storage type to read and write InfluxDB data.</p> <p>You can choose between three different types of provisioned Influx IOPS Included storage according to your workload requirements:</p> <ul> <li> <p>Influx I/O Included 3000 IOPS</p> </li> <li> <p>Influx I/O Included 12000 IOPS</p> </li> <li> <p>Influx I/O Included 16000 IOPS</p> </li> </ul>
            allocated_storage: <p>The amount of storage to allocate for your DB storage type in GiB (gibibytes).</p>
            network_type: <p>Specifies whether the network type of the Timestream for InfluxDB cluster is IPv4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.</p>
            publicly_accessible: <p>Configures the Timestream for InfluxDB cluster with a public IP to facilitate access from outside the VPC.</p>
            vpc_subnet_ids: <p>A list of VPC subnet IDs to associate with the DB cluster. Provide at least two VPC subnet IDs in different Availability Zones when deploying with a Multi-AZ standby.</p>
            vpc_security_group_ids: <p>A list of VPC security group IDs to associate with the Timestream for InfluxDB cluster.</p>
            deployment_type: <p>Specifies the type of cluster to create.</p>
            failover_mode: <p>Specifies the behavior of failure recovery when the primary node of the cluster fails.</p>
            log_delivery_configuration: <p>Configuration for sending InfluxDB engine logs to a specified S3 bucket.</p>
            maintenance_schedule: <p>Specifies the maintenance schedule for the DB cluster, including the preferred maintenance window and timezone.</p>
            db_backup_configurations: <p>A list of backup configurations to enable automated backups for the DB cluster.</p>
            kms_key_id: <p>The Amazon Web Services KMS key identifier to use for encryption of the DB cluster. Can be a key ID, key ARN, alias name, or alias ARN.</p>
            tags: <p>A list of key-value pairs to associate with the DB instance.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.create_db_cluster_input.CreateDbClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.create_db_cluster_output.CreateDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_cluster

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_cluster.async_create_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.create_db_cluster_input.CreateDbClusterInput = {
            "name": name,
            "db_instance_type": db_instance_type,
            "vpc_subnet_ids": vpc_subnet_ids,
            "vpc_security_group_ids": vpc_security_group_ids,
        }
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if organization is not None:
            input_["organization"] = organization
        if bucket is not None:
            input_["bucket"] = bucket
        if port is not None:
            input_["port"] = port
        if db_parameter_group_identifier is not None:
            input_["db_parameter_group_identifier"] = db_parameter_group_identifier
        if db_storage_type is not None:
            input_["db_storage_type"] = db_storage_type
        if allocated_storage is not None:
            input_["allocated_storage"] = allocated_storage
        if network_type is not None:
            input_["network_type"] = network_type
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if deployment_type is not None:
            input_["deployment_type"] = deployment_type
        if failover_mode is not None:
            input_["failover_mode"] = failover_mode
        if log_delivery_configuration is not None:
            input_["log_delivery_configuration"] = log_delivery_configuration
        if maintenance_schedule is not None:
            input_["maintenance_schedule"] = maintenance_schedule
        if db_backup_configurations is not None:
            input_["db_backup_configurations"] = db_backup_configurations
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_db_cluster(
        self,
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.get_db_cluster_output.GetDbClusterOutput":
        """<p>Retrieves information about a Timestream for InfluxDB cluster.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster to retrieve.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.get_db_cluster_input.GetDbClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.get_db_cluster_output.GetDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_cluster

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_cluster.async_get_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.get_db_cluster_input.GetDbClusterInput = {
            "db_cluster_id": db_cluster_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_db_cluster(
        self,
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        log_delivery_configuration: Optional[
            "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
        ] = None,
        db_parameter_group_identifier: Optional[
            "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
        ] = None,
        port: Optional["capo_timestream_influxdb.types.port.Port"] = None,
        db_instance_type: Optional[
            "capo_timestream_influxdb.types.db_instance_type.DbInstanceType"
        ] = None,
        failover_mode: Optional[
            "capo_timestream_influxdb.types.failover_mode.FailoverMode"
        ] = None,
        maintenance_schedule: Optional[
            "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
        ] = None,
        db_backup_configurations: Optional[
            "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
        ] = None,
    ) -> (
        "capo_timestream_influxdb.types.update_db_cluster_output.UpdateDbClusterOutput"
    ):
        """<p>Updates a Timestream for InfluxDB cluster.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster to update.</p>
            log_delivery_configuration: <p>The log delivery configuration to apply to the DB cluster.</p>
            db_parameter_group_identifier: <p>Update the DB cluster to use the specified DB parameter group.</p>
            port: <p>Update the DB cluster to use the specified port.</p>
            db_instance_type: <p>Update the DB cluster to use the specified DB instance Type.</p>
            failover_mode: <p>Update the DB cluster's failover behavior.</p>
            maintenance_schedule: <p>Specifies the maintenance schedule for the DB cluster, including the preferred maintenance window and timezone.</p>
            db_backup_configurations: <p>A list of backup configurations to update for the DB cluster.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.update_db_cluster_input.UpdateDbClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.update_db_cluster_output.UpdateDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.update_db_cluster

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.update_db_cluster.async_update_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.update_db_cluster_input.UpdateDbClusterInput = {
            "db_cluster_id": db_cluster_id
        }
        if log_delivery_configuration is not None:
            input_["log_delivery_configuration"] = log_delivery_configuration
        if db_parameter_group_identifier is not None:
            input_["db_parameter_group_identifier"] = db_parameter_group_identifier
        if port is not None:
            input_["port"] = port
        if db_instance_type is not None:
            input_["db_instance_type"] = db_instance_type
        if failover_mode is not None:
            input_["failover_mode"] = failover_mode
        if maintenance_schedule is not None:
            input_["maintenance_schedule"] = maintenance_schedule
        if db_backup_configurations is not None:
            input_["db_backup_configurations"] = db_backup_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_db_cluster(
        self,
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        retain_automated_backups: Optional[bool] = None,
    ) -> (
        "capo_timestream_influxdb.types.delete_db_cluster_output.DeleteDbClusterOutput"
    ):
        """<p>Deletes a Timestream for InfluxDB cluster.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster.</p>
            retain_automated_backups: <p>Specifies whether to retain automated backups after the DB cluster is deleted. If set to true, automated backups are not deleted and can be restored later.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.delete_db_cluster_input.DeleteDbClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.delete_db_cluster_output.DeleteDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.delete_db_cluster

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.delete_db_cluster.async_delete_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.delete_db_cluster_input.DeleteDbClusterInput = {
            "db_cluster_id": db_cluster_id
        }
        if retain_automated_backups is not None:
            input_["retain_automated_backups"] = retain_automated_backups

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_db_clusters(
        self,
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_timestream_influxdb.types.list_db_clusters_output.ListDbClustersOutput":
        """<p>Returns a list of Timestream for InfluxDB DB clusters.</p>

        Args:
            next_token: <p>The pagination token. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>
            max_results: <p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a nextToken is provided in the output. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.list_db_clusters_input.ListDbClustersInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.list_db_clusters_output.ListDbClustersOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_clusters

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_clusters.async_list_db_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.list_db_clusters_input.ListDbClustersInput = {}
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

    async def iter_list_db_clusters(
        self,
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_timestream_influxdb.types.db_cluster_summary.DbClusterSummary]":
        _token = next_token
        while True:
            _response = await self.list_db_clusters(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_db_instances_for_cluster(
        self,
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_timestream_influxdb.types.list_db_instances_for_cluster_output.ListDbInstancesForClusterOutput":
        """<p>Returns a list of Timestream for InfluxDB clusters.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster.</p>
            next_token: <p>The pagination token. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>
            max_results: <p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a nextToken is provided in the output. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.list_db_instances_for_cluster_input.ListDbInstancesForClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.list_db_instances_for_cluster_output.ListDbInstancesForClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_instances_for_cluster

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_instances_for_cluster.async_list_db_instances_for_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.list_db_instances_for_cluster_input.ListDbInstancesForClusterInput = {
            "db_cluster_id": db_cluster_id
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

    async def iter_list_db_instances_for_cluster(
        self,
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_timestream_influxdb.types.db_instance_for_cluster_summary.DbInstanceForClusterSummary]":
        _token = next_token
        while True:
            _response = await self.list_db_instances_for_cluster(
                db_cluster_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def reboot_db_cluster(
        self,
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        instance_ids: Optional[
            "capo_timestream_influxdb.types.db_instance_id_list.DbInstanceIdList"
        ] = None,
    ) -> (
        "capo_timestream_influxdb.types.reboot_db_cluster_output.RebootDbClusterOutput"
    ):
        """<p>Reboots a Timestream for InfluxDB cluster.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster to reboot.</p>
            instance_ids: <p>A list of service-generated unique DB Instance Ids belonging to the DB Cluster to reboot.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.reboot_db_cluster_input.RebootDbClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.reboot_db_cluster_output.RebootDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.reboot_db_cluster

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.reboot_db_cluster.async_reboot_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.reboot_db_cluster_input.RebootDbClusterInput = {
            "db_cluster_id": db_cluster_id
        }
        if instance_ids is not None:
            input_["instance_ids"] = instance_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_db_instance(
        self,
        name: "capo_timestream_influxdb.types.db_instance_name.DbInstanceName",
        password: "capo_timestream_influxdb.types.password.Password",
        db_instance_type: "capo_timestream_influxdb.types.db_instance_type.DbInstanceType",
        vpc_subnet_ids: "capo_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList",
        vpc_security_group_ids: "capo_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList",
        allocated_storage: "capo_timestream_influxdb.types.allocated_storage.AllocatedStorage",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        username: Optional["capo_timestream_influxdb.types.username.Username"] = None,
        organization: Optional[
            "capo_timestream_influxdb.types.organization.Organization"
        ] = None,
        bucket: Optional["capo_timestream_influxdb.types.bucket.Bucket"] = None,
        publicly_accessible: Optional[bool] = None,
        db_storage_type: Optional[
            "capo_timestream_influxdb.types.db_storage_type.DbStorageType"
        ] = None,
        db_parameter_group_identifier: Optional[
            "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
        ] = None,
        deployment_type: Optional[
            "capo_timestream_influxdb.types.deployment_type.DeploymentType"
        ] = None,
        log_delivery_configuration: Optional[
            "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
        ] = None,
        maintenance_schedule: Optional[
            "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
        ] = None,
        tags: Optional[
            "capo_timestream_influxdb.types.request_tag_map.RequestTagMap"
        ] = None,
        port: Optional["capo_timestream_influxdb.types.port.Port"] = None,
        network_type: Optional[
            "capo_timestream_influxdb.types.network_type.NetworkType"
        ] = None,
        db_backup_configurations: Optional[
            "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
        ] = None,
        kms_key_id: Optional[
            "capo_timestream_influxdb.types.kms_key_id.KmsKeyId"
        ] = None,
    ) -> "capo_timestream_influxdb.types.create_db_instance_output.CreateDbInstanceOutput":
        """<p>Creates a new Timestream for InfluxDB DB instance.</p>

        Args:
            name: <p>The name that uniquely identifies the DB instance when interacting with the Amazon Timestream for InfluxDB API and CLI commands. This name will also be a prefix included in the endpoint. DB instance names must be unique per customer and per region.</p>
            username: <p>The username of the initial admin user created in InfluxDB. Must start with a letter and can't end with a hyphen or contain two consecutive hyphens. For example, my-user1. This username will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a Secret created in Amazon Secrets Manager in your account.</p>
            password: <p>The password of the initial admin user created in InfluxDB v2. This password will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a Secret created in Secrets Manager in your account.</p>
            organization: <p>The name of the initial organization for the initial admin user in InfluxDB. An InfluxDB organization is a workspace for a group of users.</p>
            bucket: <p>The name of the initial InfluxDB bucket. All InfluxDB data is stored in a bucket. A bucket combines the concept of a database and a retention period (the duration of time that each data point persists). A bucket belongs to an organization.</p>
            db_instance_type: <p>The Timestream for InfluxDB DB instance type to run InfluxDB on.</p>
            vpc_subnet_ids: <p>A list of VPC subnet IDs to associate with the DB instance. Provide at least two VPC subnet IDs in different availability zones when deploying with a Multi-AZ standby.</p>
            vpc_security_group_ids: <p>A list of VPC security group IDs to associate with the DB instance.</p>
            publicly_accessible: <p>Configures the DB instance with a public IP to facilitate access.</p>
            db_storage_type: <p>The Timestream for InfluxDB DB storage type to read and write InfluxDB data.</p> <p>You can choose between 3 different types of provisioned Influx IOPS included storage according to your workloads requirements:</p> <ul> <li> <p>Influx IO Included 3000 IOPS</p> </li> <li> <p>Influx IO Included 12000 IOPS</p> </li> <li> <p>Influx IO Included 16000 IOPS</p> </li> </ul>
            allocated_storage: <p>The amount of storage to allocate for your DB storage type in GiB (gibibytes).</p>
            db_parameter_group_identifier: <p>The id of the DB parameter group to assign to your DB instance. DB parameter groups specify how the database is configured. For example, DB parameter groups can specify the limit for query concurrency.</p>
            deployment_type: <p>Specifies whether the DB instance will be deployed as a standalone instance or with a Multi-AZ standby for high availability.</p>
            log_delivery_configuration: <p>Configuration for sending InfluxDB engine logs to a specified S3 bucket.</p>
            maintenance_schedule: <p>Specifies the maintenance schedule for the DB instance, including the preferred maintenance window and timezone.</p>
            tags: <p>A list of key-value pairs to associate with the DB instance.</p>
            port: <p>The port number on which InfluxDB accepts connections.</p> <p>Valid Values: 1024-65535</p> <p>Default: 8086</p> <p>Constraints: The value can't be 2375-2376, 7788-7799, 8090, or 51678-51680</p>
            network_type: <p>Specifies whether the networkType of the Timestream for InfluxDB instance is IPV4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.</p>
            db_backup_configurations: <p>A list of backup configurations to enable automated backups for the DB instance.</p>
            kms_key_id: <p>The Amazon Web Services KMS key identifier to use for encryption of the DB instance. Can be a key ID, key ARN, alias name, or alias ARN.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.create_db_instance_input.CreateDbInstanceInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.create_db_instance_output.CreateDbInstanceOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_instance

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_instance.async_create_db_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.create_db_instance_input.CreateDbInstanceInput = {
            "name": name,
            "password": password,
            "db_instance_type": db_instance_type,
            "vpc_subnet_ids": vpc_subnet_ids,
            "vpc_security_group_ids": vpc_security_group_ids,
            "allocated_storage": allocated_storage,
        }
        if username is not None:
            input_["username"] = username
        if organization is not None:
            input_["organization"] = organization
        if bucket is not None:
            input_["bucket"] = bucket
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if db_storage_type is not None:
            input_["db_storage_type"] = db_storage_type
        if db_parameter_group_identifier is not None:
            input_["db_parameter_group_identifier"] = db_parameter_group_identifier
        if deployment_type is not None:
            input_["deployment_type"] = deployment_type
        if log_delivery_configuration is not None:
            input_["log_delivery_configuration"] = log_delivery_configuration
        if maintenance_schedule is not None:
            input_["maintenance_schedule"] = maintenance_schedule
        if tags is not None:
            input_["tags"] = tags
        if port is not None:
            input_["port"] = port
        if network_type is not None:
            input_["network_type"] = network_type
        if db_backup_configurations is not None:
            input_["db_backup_configurations"] = db_backup_configurations
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_db_instance(
        self,
        identifier: "capo_timestream_influxdb.types.db_instance_identifier.DbInstanceIdentifier",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.get_db_instance_output.GetDbInstanceOutput":
        """<p>Returns a Timestream for InfluxDB DB instance.</p>

        Args:
            identifier: <p>The id of the DB instance.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.get_db_instance_input.GetDbInstanceInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.get_db_instance_output.GetDbInstanceOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_instance

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_instance.async_get_db_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.get_db_instance_input.GetDbInstanceInput = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_db_instance(
        self,
        identifier: "capo_timestream_influxdb.types.db_instance_identifier.DbInstanceIdentifier",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        log_delivery_configuration: Optional[
            "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
        ] = None,
        db_parameter_group_identifier: Optional[
            "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
        ] = None,
        port: Optional["capo_timestream_influxdb.types.port.Port"] = None,
        db_instance_type: Optional[
            "capo_timestream_influxdb.types.db_instance_type.DbInstanceType"
        ] = None,
        deployment_type: Optional[
            "capo_timestream_influxdb.types.deployment_type.DeploymentType"
        ] = None,
        db_storage_type: Optional[
            "capo_timestream_influxdb.types.db_storage_type.DbStorageType"
        ] = None,
        allocated_storage: Optional[
            "capo_timestream_influxdb.types.allocated_storage.AllocatedStorage"
        ] = None,
        maintenance_schedule: Optional[
            "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
        ] = None,
        db_backup_configurations: Optional[
            "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
        ] = None,
    ) -> "capo_timestream_influxdb.types.update_db_instance_output.UpdateDbInstanceOutput":
        """<p>Updates a Timestream for InfluxDB DB instance.</p>

        Args:
            identifier: <p>The id of the DB instance.</p>
            log_delivery_configuration: <p>Configuration for sending InfluxDB engine logs to send to specified S3 bucket.</p>
            db_parameter_group_identifier: <p>The id of the DB parameter group to assign to your DB instance. DB parameter groups specify how the database is configured. For example, DB parameter groups can specify the limit for query concurrency.</p>
            port: <p>The port number on which InfluxDB accepts connections.</p> <p>If you change the Port value, your database restarts immediately.</p> <p>Valid Values: 1024-65535</p> <p>Default: 8086</p> <p>Constraints: The value can't be 2375-2376, 7788-7799, 8090, or 51678-51680</p>
            db_instance_type: <p>The Timestream for InfluxDB DB instance type to run InfluxDB on.</p>
            deployment_type: <p>Specifies whether the DB instance will be deployed as a standalone instance or with a Multi-AZ standby for high availability.</p>
            db_storage_type: <p>The Timestream for InfluxDB DB storage type that InfluxDB stores data on.</p>
            allocated_storage: <p>The amount of storage to allocate for your DB storage type (in gibibytes).</p>
            maintenance_schedule: <p>Specifies the maintenance schedule for the DB instance, including the preferred maintenance window and timezone.</p>
            db_backup_configurations: <p>A list of backup configurations to update for the DB instance.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.update_db_instance_input.UpdateDbInstanceInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.update_db_instance_output.UpdateDbInstanceOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.update_db_instance

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.update_db_instance.async_update_db_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.update_db_instance_input.UpdateDbInstanceInput = {
            "identifier": identifier
        }
        if log_delivery_configuration is not None:
            input_["log_delivery_configuration"] = log_delivery_configuration
        if db_parameter_group_identifier is not None:
            input_["db_parameter_group_identifier"] = db_parameter_group_identifier
        if port is not None:
            input_["port"] = port
        if db_instance_type is not None:
            input_["db_instance_type"] = db_instance_type
        if deployment_type is not None:
            input_["deployment_type"] = deployment_type
        if db_storage_type is not None:
            input_["db_storage_type"] = db_storage_type
        if allocated_storage is not None:
            input_["allocated_storage"] = allocated_storage
        if maintenance_schedule is not None:
            input_["maintenance_schedule"] = maintenance_schedule
        if db_backup_configurations is not None:
            input_["db_backup_configurations"] = db_backup_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_db_instance(
        self,
        identifier: "capo_timestream_influxdb.types.db_instance_identifier.DbInstanceIdentifier",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        retain_automated_backups: Optional[bool] = None,
    ) -> "capo_timestream_influxdb.types.delete_db_instance_output.DeleteDbInstanceOutput":
        """<p>Deletes a Timestream for InfluxDB DB instance.</p>

        Args:
            identifier: <p>The id of the DB instance.</p>
            retain_automated_backups: <p>Specifies whether to retain automated backups after the DB instance is deleted. If set to true, automated backups are not deleted and can be restored later.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.delete_db_instance_input.DeleteDbInstanceInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.delete_db_instance_output.DeleteDbInstanceOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.delete_db_instance

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.delete_db_instance.async_delete_db_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.delete_db_instance_input.DeleteDbInstanceInput = {
            "identifier": identifier
        }
        if retain_automated_backups is not None:
            input_["retain_automated_backups"] = retain_automated_backups

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_db_instances(
        self,
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "capo_timestream_influxdb.types.list_db_instances_output.ListDbInstancesOutput"
    ):
        """<p>Returns a list of Timestream for InfluxDB DB instances.</p>

        Args:
            next_token: <p>The pagination token. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>
            max_results: <p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.list_db_instances_input.ListDbInstancesInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.list_db_instances_output.ListDbInstancesOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_instances

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_instances.async_list_db_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.list_db_instances_input.ListDbInstancesInput = {}
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

    async def iter_list_db_instances(
        self,
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_timestream_influxdb.types.db_instance_summary.DbInstanceSummary]":
        _token = next_token
        while True:
            _response = await self.list_db_instances(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def reboot_db_instance(
        self,
        identifier: "capo_timestream_influxdb.types.db_instance_identifier.DbInstanceIdentifier",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.reboot_db_instance_output.RebootDbInstanceOutput":
        """<p>Reboots a Timestream for InfluxDB instance.</p>

        Args:
            identifier: <p>The id of the DB instance to reboot.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.reboot_db_instance_input.RebootDbInstanceInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.reboot_db_instance_output.RebootDbInstanceOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.reboot_db_instance

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.reboot_db_instance.async_reboot_db_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.reboot_db_instance_input.RebootDbInstanceInput = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_db_parameter_group(
        self,
        name: "capo_timestream_influxdb.types.db_parameter_group_name.DbParameterGroupName",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        description: Optional[str] = None,
        parameters: Optional[
            "capo_timestream_influxdb.types.parameters.Parameters"
        ] = None,
        tags: Optional[
            "capo_timestream_influxdb.types.request_tag_map.RequestTagMap"
        ] = None,
    ) -> "capo_timestream_influxdb.types.create_db_parameter_group_output.CreateDbParameterGroupOutput":
        """<p>Creates a new Timestream for InfluxDB DB parameter group to associate with DB instances.</p>

        Args:
            name: <p>The name of the DB parameter group. The name must be unique per customer and per region.</p>
            description: <p>A description of the DB parameter group.</p>
            parameters: <p>A list of the parameters that comprise the DB parameter group.</p>
            tags: <p>A list of key-value pairs to associate with the DB parameter group.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.create_db_parameter_group_input.CreateDbParameterGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.create_db_parameter_group_output.CreateDbParameterGroupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_parameter_group

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_parameter_group.async_create_db_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.create_db_parameter_group_input.CreateDbParameterGroupInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if parameters is not None:
            input_["parameters"] = parameters
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_db_parameter_group(
        self,
        identifier: "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.get_db_parameter_group_output.GetDbParameterGroupOutput":
        """<p>Returns a Timestream for InfluxDB DB parameter group.</p>

        Args:
            identifier: <p>The id of the DB parameter group.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.get_db_parameter_group_input.GetDbParameterGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.get_db_parameter_group_output.GetDbParameterGroupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_parameter_group

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_parameter_group.async_get_db_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.get_db_parameter_group_input.GetDbParameterGroupInput = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_db_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_timestream_influxdb.types.list_db_parameter_groups_output.ListDbParameterGroupsOutput":
        """<p>Returns a list of Timestream for InfluxDB DB parameter groups.</p>

        Args:
            next_token: <p>The pagination token. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>
            max_results: <p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.list_db_parameter_groups_input.ListDbParameterGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.list_db_parameter_groups_output.ListDbParameterGroupsOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_parameter_groups

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_parameter_groups.async_list_db_parameter_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_influxdb.types.list_db_parameter_groups_input.ListDbParameterGroupsInput = {}
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

    async def iter_list_db_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_timestream_influxdb.types.db_parameter_group_summary.DbParameterGroupSummary]":
        _token = next_token
        while True:
            _response = await self.list_db_parameter_groups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
