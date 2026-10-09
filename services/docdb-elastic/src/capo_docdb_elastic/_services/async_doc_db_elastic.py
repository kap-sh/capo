"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ChimeraDbLionfishServiceLambda``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_docdb_elastic._auth._signers
import capo_docdb_elastic._auth._sigv4
from capo_docdb_elastic._auth._identity import Credentials
from capo_docdb_elastic._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_docdb_elastic._auth._zapros_handler import AuthMiddleware
from capo_docdb_elastic._pagination import resolve_path as _resolve_path
from capo_docdb_elastic._services._aws_config import aaws_config
from capo_docdb_elastic._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_docdb_elastic.types.apply_pending_maintenance_action_input
    import capo_docdb_elastic.types.apply_pending_maintenance_action_output
    import capo_docdb_elastic.types.arn
    import capo_docdb_elastic.types.auth
    import capo_docdb_elastic.types.cluster_in_list
    import capo_docdb_elastic.types.cluster_snapshot_in_list
    import capo_docdb_elastic.types.copy_cluster_snapshot_input
    import capo_docdb_elastic.types.copy_cluster_snapshot_output
    import capo_docdb_elastic.types.create_cluster_input
    import capo_docdb_elastic.types.create_cluster_output
    import capo_docdb_elastic.types.create_cluster_snapshot_input
    import capo_docdb_elastic.types.create_cluster_snapshot_output
    import capo_docdb_elastic.types.delete_cluster_input
    import capo_docdb_elastic.types.delete_cluster_output
    import capo_docdb_elastic.types.delete_cluster_snapshot_input
    import capo_docdb_elastic.types.delete_cluster_snapshot_output
    import capo_docdb_elastic.types.get_cluster_input
    import capo_docdb_elastic.types.get_cluster_output
    import capo_docdb_elastic.types.get_cluster_snapshot_input
    import capo_docdb_elastic.types.get_cluster_snapshot_output
    import capo_docdb_elastic.types.get_pending_maintenance_action_input
    import capo_docdb_elastic.types.get_pending_maintenance_action_output
    import capo_docdb_elastic.types.input_string
    import capo_docdb_elastic.types.list_cluster_snapshots_input
    import capo_docdb_elastic.types.list_cluster_snapshots_output
    import capo_docdb_elastic.types.list_clusters_input
    import capo_docdb_elastic.types.list_clusters_output
    import capo_docdb_elastic.types.list_pending_maintenance_actions_input
    import capo_docdb_elastic.types.list_pending_maintenance_actions_output
    import capo_docdb_elastic.types.list_tags_for_resource_request
    import capo_docdb_elastic.types.list_tags_for_resource_response
    import capo_docdb_elastic.types.opt_in_type
    import capo_docdb_elastic.types.pagination_token
    import capo_docdb_elastic.types.password
    import capo_docdb_elastic.types.resource_pending_maintenance_action
    import capo_docdb_elastic.types.restore_cluster_from_snapshot_input
    import capo_docdb_elastic.types.restore_cluster_from_snapshot_output
    import capo_docdb_elastic.types.start_cluster_input
    import capo_docdb_elastic.types.start_cluster_output
    import capo_docdb_elastic.types.stop_cluster_input
    import capo_docdb_elastic.types.stop_cluster_output
    import capo_docdb_elastic.types.string_list
    import capo_docdb_elastic.types.tag_key_list
    import capo_docdb_elastic.types.tag_map
    import capo_docdb_elastic.types.tag_resource_request
    import capo_docdb_elastic.types.tag_resource_response
    import capo_docdb_elastic.types.untag_resource_request
    import capo_docdb_elastic.types.untag_resource_response
    import capo_docdb_elastic.types.update_cluster_input
    import capo_docdb_elastic.types.update_cluster_output


class AsyncDocDBElasticClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncDocDBElasticClient:
    """A client for the ``DocDBElastic`` service.

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
        self._config = AsyncDocDBElasticClientConfig(
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
        self, config_overrides: Optional[AsyncDocDBElasticClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDocDBElasticClientConfig = config_overrides or {}
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

    async def apply_pending_maintenance_action(
        self,
        resource_arn: "capo_docdb_elastic.types.input_string.InputString",
        apply_action: "capo_docdb_elastic.types.input_string.InputString",
        opt_in_type: "capo_docdb_elastic.types.opt_in_type.OptInType",
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
        apply_on: Optional["capo_docdb_elastic.types.input_string.InputString"] = None,
    ) -> "capo_docdb_elastic.types.apply_pending_maintenance_action_output.ApplyPendingMaintenanceActionOutput":
        """<p>The type of pending maintenance action to be applied to the resource.</p>

        Args:
            resource_arn: <p>The Amazon DocumentDB Amazon Resource Name (ARN) of the resource to which the pending maintenance action applies.</p>
            apply_action: <p>The pending maintenance action to apply to the resource.</p> <p>Valid actions are:</p> <ul> <li> <p> <code>ENGINE_UPDATE<i/> </code> </p> </li> <li> <p> <code>ENGINE_UPGRADE</code> </p> </li> <li> <p> <code>SECURITY_UPDATE</code> </p> </li> <li> <p> <code>OS_UPDATE</code> </p> </li> <li> <p> <code>MASTER_USER_PASSWORD_UPDATE</code> </p> </li> </ul>
            opt_in_type: <p>A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type <code>IMMEDIATE</code> can't be undone.</p>
            apply_on: <p>A specific date to apply the pending maintenance action. Required if opt-in-type is <code>APPLY_ON</code>. Format: <code>yyyy/MM/dd HH:mm-yyyy/MM/dd HH:mm</code> </p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.conflict_exception.ConflictException: <p>There was an access conflict.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.apply_pending_maintenance_action_input.ApplyPendingMaintenanceActionInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.apply_pending_maintenance_action_output.ApplyPendingMaintenanceActionOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.apply_pending_maintenance_action

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.apply_pending_maintenance_action.async_apply_pending_maintenance_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.apply_pending_maintenance_action_input.ApplyPendingMaintenanceActionInput = {
            "resource_arn": resource_arn,
            "apply_action": apply_action,
            "opt_in_type": opt_in_type,
        }
        if apply_on is not None:
            input_["apply_on"] = apply_on

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def copy_cluster_snapshot(
        self,
        snapshot_arn: str,
        target_snapshot_name: str,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
        kms_key_id: Optional[str] = None,
        copy_tags: Optional[bool] = None,
        tags: Optional["capo_docdb_elastic.types.tag_map.TagMap"] = None,
    ) -> "capo_docdb_elastic.types.copy_cluster_snapshot_output.CopyClusterSnapshotOutput":
        """<p>Copies a snapshot of an elastic cluster.</p>

        Args:
            snapshot_arn: <p>The Amazon Resource Name (ARN) identifier of the elastic cluster snapshot.</p>
            target_snapshot_name: <p>The identifier of the new elastic cluster snapshot to create from the source cluster snapshot. This parameter is not case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>elastic-cluster-snapshot-5</code> </p>
            kms_key_id: <p>The Amazon Web Services KMS key ID for an encrypted elastic cluster snapshot. The Amazon Web Services KMS key ID is the Amazon Resource Name (ARN), Amazon Web Services KMS key identifier, or the Amazon Web Services KMS key alias for the Amazon Web Services KMS encryption key.</p> <p>If you copy an encrypted elastic cluster snapshot from your Amazon Web Services account, you can specify a value for <code>KmsKeyId</code> to encrypt the copy with a new Amazon Web ServicesS KMS encryption key. If you don't specify a value for <code>KmsKeyId</code>, then the copy of the elastic cluster snapshot is encrypted with the same <code>AWS</code> KMS key as the source elastic cluster snapshot.</p> <p>To copy an encrypted elastic cluster snapshot to another Amazon Web Services region, set <code>KmsKeyId</code> to the Amazon Web Services KMS key ID that you want to use to encrypt the copy of the elastic cluster snapshot in the destination region. Amazon Web Services KMS encryption keys are specific to the Amazon Web Services region that they are created in, and you can't use encryption keys from one Amazon Web Services region in another Amazon Web Services region.</p> <p>If you copy an unencrypted elastic cluster snapshot and specify a value for the <code>KmsKeyId</code> parameter, an error is returned.</p>
            copy_tags: <p>Set to <code>true</code> to copy all tags from the source cluster snapshot to the target elastic cluster snapshot. The default is <code>false</code>.</p>
            tags: <p>The tags to be assigned to the elastic cluster snapshot.</p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.conflict_exception.ConflictException: <p>There was an access conflict.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota for the action was exceeded.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Basic Copy Cluster Snapshot Example
            update applied

            >>> await client.copy_cluster_snapshot(snapshot_arn='arn:aws:docdb-elastic:us-east-1:$AWS_ACCOUNT_ID:cluster-snapshot/$SOURCE_SNAPSHOT_ID', target_snapshot_name='sampleSnapshotName')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.copy_cluster_snapshot_input.CopyClusterSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.copy_cluster_snapshot_output.CopyClusterSnapshotOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.copy_cluster_snapshot

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.copy_cluster_snapshot.async_copy_cluster_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.copy_cluster_snapshot_input.CopyClusterSnapshotInput = {
            "snapshot_arn": snapshot_arn,
            "target_snapshot_name": target_snapshot_name,
        }
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cluster(
        self,
        cluster_name: str,
        auth_type: "capo_docdb_elastic.types.auth.Auth",
        admin_user_name: str,
        admin_user_password: "capo_docdb_elastic.types.password.Password",
        shard_capacity: int,
        shard_count: int,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
        vpc_security_group_ids: Optional[
            "capo_docdb_elastic.types.string_list.StringList"
        ] = None,
        subnet_ids: Optional["capo_docdb_elastic.types.string_list.StringList"] = None,
        kms_key_id: Optional[str] = None,
        client_token: Optional[str] = None,
        preferred_maintenance_window: Optional[str] = None,
        tags: Optional["capo_docdb_elastic.types.tag_map.TagMap"] = None,
        backup_retention_period: Optional[int] = None,
        preferred_backup_window: Optional[str] = None,
        shard_instance_count: Optional[int] = None,
    ) -> "capo_docdb_elastic.types.create_cluster_output.CreateClusterOutput":
        """<p>Creates a new Amazon DocumentDB elastic cluster and returns its cluster structure.</p>

        Args:
            cluster_name: <p>The name of the new elastic cluster. This parameter is stored as a lowercase string.</p> <p> <i>Constraints</i>:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p> <i>Example</i>: <code>my-cluster</code> </p>
            auth_type: <p>The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are <code>PLAIN_TEXT</code> or <code>SECRET_ARN</code>.</p>
            admin_user_name: <p>The name of the Amazon DocumentDB elastic clusters administrator.</p> <p> <i>Constraints</i>:</p> <ul> <li> <p>Must be from 1 to 63 letters or numbers.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot be a reserved word.</p> </li> </ul>
            admin_user_password: <p>The password for the Amazon DocumentDB elastic clusters administrator. The password can contain any printable ASCII characters.</p> <p> <i>Constraints</i>:</p> <ul> <li> <p>Must contain from 8 to 100 characters.</p> </li> <li> <p>Cannot contain a forward slash (/), double quote ("), or the "at" symbol (@).</p> </li> </ul>
            shard_capacity: <p>The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.</p>
            shard_count: <p>The number of shards assigned to the elastic cluster. Maximum is 32.</p>
            vpc_security_group_ids: <p>A list of EC2 VPC security groups to associate with the new elastic cluster.</p>
            subnet_ids: <p>The Amazon EC2 subnet IDs for the new elastic cluster.</p>
            kms_key_id: <p>The KMS key identifier to use to encrypt the new elastic cluster.</p> <p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.</p> <p>If an encryption key is not specified, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.</p>
            client_token: <p>The client token for the elastic cluster.</p>
            preferred_maintenance_window: <p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p> <i>Format</i>: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p> <i>Default</i>: a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week.</p> <p> <i>Valid days</i>: Mon, Tue, Wed, Thu, Fri, Sat, Sun</p> <p> <i>Constraints</i>: Minimum 30-minute window.</p>
            tags: <p>The tags to be assigned to the new elastic cluster.</p>
            backup_retention_period: <p>The number of days for which automatic snapshots are retained.</p>
            preferred_backup_window: <p>The daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>backupRetentionPeriod</code>.</p>
            shard_instance_count: <p>The number of replica instances applying to all shards in the elastic cluster. A <code>shardInstanceCount</code> value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.</p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.conflict_exception.ConflictException: <p>There was an access conflict.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota for the action was exceeded.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.create_cluster_input.CreateClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.create_cluster_output.CreateClusterOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.create_cluster

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.create_cluster.async_create_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.create_cluster_input.CreateClusterInput = {
            "cluster_name": cluster_name,
            "auth_type": auth_type,
            "admin_user_name": admin_user_name,
            "admin_user_password": admin_user_password,
            "shard_capacity": shard_capacity,
            "shard_count": shard_count,
        }
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if tags is not None:
            input_["tags"] = tags
        if backup_retention_period is not None:
            input_["backup_retention_period"] = backup_retention_period
        if preferred_backup_window is not None:
            input_["preferred_backup_window"] = preferred_backup_window
        if shard_instance_count is not None:
            input_["shard_instance_count"] = shard_instance_count

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cluster_snapshot(
        self,
        cluster_arn: str,
        snapshot_name: str,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
        tags: Optional["capo_docdb_elastic.types.tag_map.TagMap"] = None,
    ) -> "capo_docdb_elastic.types.create_cluster_snapshot_output.CreateClusterSnapshotOutput":
        """<p>Creates a snapshot of an elastic cluster.</p>

        Args:
            cluster_arn: <p>The ARN identifier of the elastic cluster of which you want to create a snapshot.</p>
            snapshot_name: <p>The name of the new elastic cluster snapshot.</p>
            tags: <p>The tags to be assigned to the new elastic cluster snapshot.</p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.conflict_exception.ConflictException: <p>There was an access conflict.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota for the action was exceeded.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.create_cluster_snapshot_input.CreateClusterSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.create_cluster_snapshot_output.CreateClusterSnapshotOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.create_cluster_snapshot

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.create_cluster_snapshot.async_create_cluster_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.create_cluster_snapshot_input.CreateClusterSnapshotInput = {
            "cluster_arn": cluster_arn,
            "snapshot_name": snapshot_name,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cluster(
        self,
        cluster_arn: str,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
    ) -> "capo_docdb_elastic.types.delete_cluster_output.DeleteClusterOutput":
        """<p>Delete an elastic cluster.</p>

        Args:
            cluster_arn: <p>The ARN identifier of the elastic cluster that is to be deleted.</p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.conflict_exception.ConflictException: <p>There was an access conflict.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.delete_cluster_input.DeleteClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.delete_cluster_output.DeleteClusterOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.delete_cluster

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.delete_cluster.async_delete_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.delete_cluster_input.DeleteClusterInput = {
            "cluster_arn": cluster_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cluster_snapshot(
        self,
        snapshot_arn: str,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
    ) -> "capo_docdb_elastic.types.delete_cluster_snapshot_output.DeleteClusterSnapshotOutput":
        """<p>Delete an elastic cluster snapshot.</p>

        Args:
            snapshot_arn: <p>The ARN identifier of the elastic cluster snapshot that is to be deleted.</p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.conflict_exception.ConflictException: <p>There was an access conflict.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.delete_cluster_snapshot_input.DeleteClusterSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.delete_cluster_snapshot_output.DeleteClusterSnapshotOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.delete_cluster_snapshot

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.delete_cluster_snapshot.async_delete_cluster_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.delete_cluster_snapshot_input.DeleteClusterSnapshotInput = {
            "snapshot_arn": snapshot_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_cluster(
        self,
        cluster_arn: str,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
    ) -> "capo_docdb_elastic.types.get_cluster_output.GetClusterOutput":
        """<p>Returns information about a specific elastic cluster.</p>

        Args:
            cluster_arn: <p>The ARN identifier of the elastic cluster.</p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.get_cluster_input.GetClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.get_cluster_output.GetClusterOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.get_cluster

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.get_cluster.async_get_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.get_cluster_input.GetClusterInput = {
            "cluster_arn": cluster_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_cluster_snapshot(
        self,
        snapshot_arn: str,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
    ) -> (
        "capo_docdb_elastic.types.get_cluster_snapshot_output.GetClusterSnapshotOutput"
    ):
        """<p>Returns information about a specific elastic cluster snapshot</p>

        Args:
            snapshot_arn: <p>The ARN identifier of the elastic cluster snapshot.</p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.get_cluster_snapshot_input.GetClusterSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.get_cluster_snapshot_output.GetClusterSnapshotOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.get_cluster_snapshot

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.get_cluster_snapshot.async_get_cluster_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.get_cluster_snapshot_input.GetClusterSnapshotInput = {
            "snapshot_arn": snapshot_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_pending_maintenance_action(
        self,
        resource_arn: "capo_docdb_elastic.types.input_string.InputString",
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
    ) -> "capo_docdb_elastic.types.get_pending_maintenance_action_output.GetPendingMaintenanceActionOutput":
        """<p>Retrieves all maintenance actions that are pending.</p>

        Args:
            resource_arn: <p>Retrieves pending maintenance actions for a specific Amazon Resource Name (ARN).</p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.conflict_exception.ConflictException: <p>There was an access conflict.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.get_pending_maintenance_action_input.GetPendingMaintenanceActionInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.get_pending_maintenance_action_output.GetPendingMaintenanceActionOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.get_pending_maintenance_action

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.get_pending_maintenance_action.async_get_pending_maintenance_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.get_pending_maintenance_action_input.GetPendingMaintenanceActionInput = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_clusters(
        self,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
        next_token: Optional[
            "capo_docdb_elastic.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_docdb_elastic.types.list_clusters_output.ListClustersOutput":
        """<p>Returns information about provisioned Amazon DocumentDB elastic clusters.</p>

        Args:
            next_token: <p>A pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond this token, up to the value specified by <code>max-results</code>.</p> <p>If there is no more data in the responce, the <code>nextToken</code> will not be returned.</p>
            max_results: <p>The maximum number of elastic cluster snapshot results to receive in the response.</p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.list_clusters_input.ListClustersInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.list_clusters_output.ListClustersOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.list_clusters

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.list_clusters.async_list_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.list_clusters_input.ListClustersInput = {}
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

    async def iter_list_clusters(
        self,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
        next_token: Optional[
            "capo_docdb_elastic.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_docdb_elastic.types.cluster_in_list.ClusterInList]":
        _token = next_token
        while True:
            _response = await self.list_clusters(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_cluster_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
        cluster_arn: Optional[str] = None,
        next_token: Optional[
            "capo_docdb_elastic.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
        snapshot_type: Optional[str] = None,
    ) -> "capo_docdb_elastic.types.list_cluster_snapshots_output.ListClusterSnapshotsOutput":
        """<p>Returns information about snapshots for a specified elastic cluster.</p>

        Args:
            cluster_arn: <p>The ARN identifier of the elastic cluster.</p>
            next_token: <p>A pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond this token, up to the value specified by <code>max-results</code>.</p> <p>If there is no more data in the responce, the <code>nextToken</code> will not be returned.</p>
            max_results: <p>The maximum number of elastic cluster snapshot results to receive in the response.</p>
            snapshot_type: <p>The type of cluster snapshots to be returned. You can specify one of the following values:</p> <ul> <li> <p> <code>automated</code> - Return all cluster snapshots that Amazon DocumentDB has automatically created for your Amazon Web Services account.</p> </li> <li> <p> <code>manual</code> - Return all cluster snapshots that you have manually created for your Amazon Web Services account.</p> </li> </ul>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.list_cluster_snapshots_input.ListClusterSnapshotsInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.list_cluster_snapshots_output.ListClusterSnapshotsOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.list_cluster_snapshots

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.list_cluster_snapshots.async_list_cluster_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.list_cluster_snapshots_input.ListClusterSnapshotsInput = {}
        if cluster_arn is not None:
            input_["cluster_arn"] = cluster_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if snapshot_type is not None:
            input_["snapshot_type"] = snapshot_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_cluster_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
        cluster_arn: Optional[str] = None,
        next_token: Optional[
            "capo_docdb_elastic.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
        snapshot_type: Optional[str] = None,
    ) -> "AsyncIterator[capo_docdb_elastic.types.cluster_snapshot_in_list.ClusterSnapshotInList]":
        _token = next_token
        while True:
            _response = await self.list_cluster_snapshots(
                config_overrides=config_overrides,
                cluster_arn=cluster_arn,
                next_token=_token,
                max_results=max_results,
                snapshot_type=snapshot_type,
            )
            _page = _resolve_path(_response, ("snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pending_maintenance_actions(
        self,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
        next_token: Optional[
            "capo_docdb_elastic.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_docdb_elastic.types.list_pending_maintenance_actions_output.ListPendingMaintenanceActionsOutput":
        """<p>Retrieves a list of all maintenance actions that are pending.</p>

        Args:
            next_token: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>maxResults</code>.</p>
            max_results: <p>The maximum number of results to include in the response. If more records exist than the specified <code>maxResults</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.list_pending_maintenance_actions_input.ListPendingMaintenanceActionsInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.list_pending_maintenance_actions_output.ListPendingMaintenanceActionsOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.list_pending_maintenance_actions

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.list_pending_maintenance_actions.async_list_pending_maintenance_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.list_pending_maintenance_actions_input.ListPendingMaintenanceActionsInput = {}
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

    async def iter_list_pending_maintenance_actions(
        self,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
        next_token: Optional[
            "capo_docdb_elastic.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_docdb_elastic.types.resource_pending_maintenance_action.ResourcePendingMaintenanceAction]":
        _token = next_token
        while True:
            _response = await self.list_pending_maintenance_actions(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("resource_pending_maintenance_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_docdb_elastic.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
    ) -> "capo_docdb_elastic.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags on a elastic cluster resource</p>

        Args:
            resource_arn: <p>The ARN identifier of the elastic cluster resource.</p>

        Raises:
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_cluster_from_snapshot(
        self,
        cluster_name: str,
        snapshot_arn: str,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
        vpc_security_group_ids: Optional[
            "capo_docdb_elastic.types.string_list.StringList"
        ] = None,
        subnet_ids: Optional["capo_docdb_elastic.types.string_list.StringList"] = None,
        kms_key_id: Optional[str] = None,
        tags: Optional["capo_docdb_elastic.types.tag_map.TagMap"] = None,
        shard_capacity: Optional[int] = None,
        shard_instance_count: Optional[int] = None,
    ) -> "capo_docdb_elastic.types.restore_cluster_from_snapshot_output.RestoreClusterFromSnapshotOutput":
        """<p>Restores an elastic cluster from a snapshot.</p>

        Args:
            cluster_name: <p>The name of the elastic cluster.</p>
            snapshot_arn: <p>The ARN identifier of the elastic cluster snapshot.</p>
            vpc_security_group_ids: <p>A list of EC2 VPC security groups to associate with the elastic cluster.</p>
            subnet_ids: <p>The Amazon EC2 subnet IDs for the elastic cluster.</p>
            kms_key_id: <p>The KMS key identifier to use to encrypt the new Amazon DocumentDB elastic clusters cluster.</p> <p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.</p> <p>If an encryption key is not specified here, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.</p>
            tags: <p>A list of the tag names to be assigned to the restored elastic cluster, in the form of an array of key-value pairs in which the key is the tag name and the value is the key value.</p>
            shard_capacity: <p>The capacity of each shard in the new restored elastic cluster.</p>
            shard_instance_count: <p>The number of replica instances applying to all shards in the elastic cluster. A <code>shardInstanceCount</code> value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.</p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.conflict_exception.ConflictException: <p>There was an access conflict.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota for the action was exceeded.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.restore_cluster_from_snapshot_input.RestoreClusterFromSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.restore_cluster_from_snapshot_output.RestoreClusterFromSnapshotOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.restore_cluster_from_snapshot

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.restore_cluster_from_snapshot.async_restore_cluster_from_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.restore_cluster_from_snapshot_input.RestoreClusterFromSnapshotInput = {
            "cluster_name": cluster_name,
            "snapshot_arn": snapshot_arn,
        }
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if shard_capacity is not None:
            input_["shard_capacity"] = shard_capacity
        if shard_instance_count is not None:
            input_["shard_instance_count"] = shard_instance_count

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_cluster(
        self,
        cluster_arn: str,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
    ) -> "capo_docdb_elastic.types.start_cluster_output.StartClusterOutput":
        """<p>Restarts the stopped elastic cluster that is specified by <code>clusterARN</code>.</p>

        Args:
            cluster_arn: <p>The ARN identifier of the elastic cluster.</p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Basic Start Cluster Example
            update applied

            >>> await client.start_cluster(cluster_arn='arn:aws:docdb-elastic:us-east-1:$AWS_ACCOUNT_ID:cluster/$CLUSTER_ID')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.start_cluster_input.StartClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.start_cluster_output.StartClusterOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.start_cluster

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.start_cluster.async_start_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.start_cluster_input.StartClusterInput = {
            "cluster_arn": cluster_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_cluster(
        self,
        cluster_arn: str,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
    ) -> "capo_docdb_elastic.types.stop_cluster_output.StopClusterOutput":
        """<p>Stops the running elastic cluster that is specified by <code>clusterArn</code>. The elastic cluster must be in the <i>available</i> state. </p>

        Args:
            cluster_arn: <p>The ARN identifier of the elastic cluster.</p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Basic Stop Cluster Example
            update applied

            >>> await client.stop_cluster(cluster_arn='arn:aws:docdb-elastic:us-east-1:$AWS_ACCOUNT_ID:cluster/$CLUSTER_ID')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.stop_cluster_input.StopClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.stop_cluster_output.StopClusterOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.stop_cluster

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.stop_cluster.async_stop_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.stop_cluster_input.StopClusterInput = {
            "cluster_arn": cluster_arn
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
        resource_arn: "capo_docdb_elastic.types.arn.Arn",
        tags: "capo_docdb_elastic.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
    ) -> "capo_docdb_elastic.types.tag_resource_response.TagResourceResponse":
        """<p>Adds metadata tags to an elastic cluster resource</p>

        Args:
            resource_arn: <p>The ARN identifier of the elastic cluster resource.</p>
            tags: <p>The tags that are assigned to the elastic cluster resource.</p>

        Raises:
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.tag_resource

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_docdb_elastic.types.arn.Arn",
        tag_keys: "capo_docdb_elastic.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
    ) -> "capo_docdb_elastic.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes metadata tags from an elastic cluster resource</p>

        Args:
            resource_arn: <p>The ARN identifier of the elastic cluster resource.</p>
            tag_keys: <p>The tag keys to be removed from the elastic cluster resource.</p>

        Raises:
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.untag_resource

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_cluster(
        self,
        cluster_arn: str,
        *,
        config_overrides: Optional[AsyncDocDBElasticClientConfig] = None,
        auth_type: Optional["capo_docdb_elastic.types.auth.Auth"] = None,
        shard_capacity: Optional[int] = None,
        shard_count: Optional[int] = None,
        vpc_security_group_ids: Optional[
            "capo_docdb_elastic.types.string_list.StringList"
        ] = None,
        subnet_ids: Optional["capo_docdb_elastic.types.string_list.StringList"] = None,
        admin_user_password: Optional[
            "capo_docdb_elastic.types.password.Password"
        ] = None,
        client_token: Optional[str] = None,
        preferred_maintenance_window: Optional[str] = None,
        backup_retention_period: Optional[int] = None,
        preferred_backup_window: Optional[str] = None,
        shard_instance_count: Optional[int] = None,
    ) -> "capo_docdb_elastic.types.update_cluster_output.UpdateClusterOutput":
        """<p>Modifies an elastic cluster. This includes updating admin-username/password, upgrading the API version, and setting up a backup window and maintenance window</p>

        Args:
            cluster_arn: <p>The ARN identifier of the elastic cluster.</p>
            auth_type: <p>The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are <code>PLAIN_TEXT</code> or <code>SECRET_ARN</code>.</p>
            shard_capacity: <p>The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.</p>
            shard_count: <p>The number of shards assigned to the elastic cluster. Maximum is 32.</p>
            vpc_security_group_ids: <p>A list of EC2 VPC security groups to associate with the elastic cluster.</p>
            subnet_ids: <p>The Amazon EC2 subnet IDs for the elastic cluster.</p>
            admin_user_password: <p>The password associated with the elastic cluster administrator. This password can contain any printable ASCII character except forward slash (/), double quote ("), or the "at" symbol (@).</p> <p> <i>Constraints</i>: Must contain from 8 to 100 characters.</p>
            client_token: <p>The client token for the elastic cluster.</p>
            preferred_maintenance_window: <p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p> <i>Format</i>: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p> <i>Default</i>: a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week.</p> <p> <i>Valid days</i>: Mon, Tue, Wed, Thu, Fri, Sat, Sun</p> <p> <i>Constraints</i>: Minimum 30-minute window.</p>
            backup_retention_period: <p>The number of days for which automatic snapshots are retained.</p>
            preferred_backup_window: <p>The daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>backupRetentionPeriod</code>.</p>
            shard_instance_count: <p>The number of replica instances applying to all shards in the elastic cluster. A <code>shardInstanceCount</code> value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.</p>

        Raises:
            capo_docdb_elastic.errors.access_denied_exception.AccessDeniedException: <p>An exception that occurs when there are not sufficient permissions to perform an action.</p>
            capo_docdb_elastic.errors.conflict_exception.ConflictException: <p>There was an access conflict.</p>
            capo_docdb_elastic.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_docdb_elastic.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be located.</p>
            capo_docdb_elastic.errors.throttling_exception.ThrottlingException: <p>ThrottlingException will be thrown when request was denied due to request throttling.</p>
            capo_docdb_elastic.errors.validation_exception.ValidationException: <p>A structure defining a validation exception.</p>
            capo_docdb_elastic.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_docdb_elastic.types.update_cluster_input.UpdateClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_docdb_elastic.types.update_cluster_output.UpdateClusterOutput"
        ]:
            import capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.update_cluster

            (
                output,
                http_response,
            ) = await capo_docdb_elastic._operations.chimera_db_lionfish_service_lambda.update_cluster.async_update_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb_elastic.types.update_cluster_input.UpdateClusterInput = {
            "cluster_arn": cluster_arn
        }
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if shard_capacity is not None:
            input_["shard_capacity"] = shard_capacity
        if shard_count is not None:
            input_["shard_count"] = shard_count
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if admin_user_password is not None:
            input_["admin_user_password"] = admin_user_password
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if backup_retention_period is not None:
            input_["backup_retention_period"] = backup_retention_period
        if preferred_backup_window is not None:
            input_["preferred_backup_window"] = preferred_backup_window
        if shard_instance_count is not None:
            input_["shard_instance_count"] = shard_instance_count

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
