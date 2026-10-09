"""Generated from Smithy shape ``com.amazonaws.keyspaces#KeyspacesService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_keyspaces._auth._signers
import capo_keyspaces._auth._sigv4
from capo_keyspaces._auth._identity import Credentials
from capo_keyspaces._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_keyspaces._auth._zapros_handler import AuthMiddleware
from capo_keyspaces._pagination import resolve_path as _resolve_path
from capo_keyspaces._services._aws_config import aaws_config
from capo_keyspaces._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_keyspaces.types.arn
    import capo_keyspaces.types.auto_scaling_specification
    import capo_keyspaces.types.capacity_specification
    import capo_keyspaces.types.cdc_specification
    import capo_keyspaces.types.client_side_timestamps
    import capo_keyspaces.types.column_definition_list
    import capo_keyspaces.types.comment
    import capo_keyspaces.types.create_keyspace_request
    import capo_keyspaces.types.create_keyspace_response
    import capo_keyspaces.types.create_table_request
    import capo_keyspaces.types.create_table_response
    import capo_keyspaces.types.create_type_request
    import capo_keyspaces.types.create_type_response
    import capo_keyspaces.types.default_time_to_live
    import capo_keyspaces.types.delete_keyspace_request
    import capo_keyspaces.types.delete_keyspace_response
    import capo_keyspaces.types.delete_table_request
    import capo_keyspaces.types.delete_table_response
    import capo_keyspaces.types.delete_type_request
    import capo_keyspaces.types.delete_type_response
    import capo_keyspaces.types.encryption_specification
    import capo_keyspaces.types.field_list
    import capo_keyspaces.types.get_keyspace_request
    import capo_keyspaces.types.get_keyspace_response
    import capo_keyspaces.types.get_table_auto_scaling_settings_request
    import capo_keyspaces.types.get_table_auto_scaling_settings_response
    import capo_keyspaces.types.get_table_request
    import capo_keyspaces.types.get_table_response
    import capo_keyspaces.types.get_type_request
    import capo_keyspaces.types.get_type_response
    import capo_keyspaces.types.keyspace_name
    import capo_keyspaces.types.keyspace_summary
    import capo_keyspaces.types.list_keyspaces_request
    import capo_keyspaces.types.list_keyspaces_response
    import capo_keyspaces.types.list_tables_request
    import capo_keyspaces.types.list_tables_response
    import capo_keyspaces.types.list_tags_for_resource_request
    import capo_keyspaces.types.list_tags_for_resource_response
    import capo_keyspaces.types.list_types_request
    import capo_keyspaces.types.list_types_response
    import capo_keyspaces.types.max_results
    import capo_keyspaces.types.next_token
    import capo_keyspaces.types.point_in_time_recovery
    import capo_keyspaces.types.replica_specification_list
    import capo_keyspaces.types.replication_specification
    import capo_keyspaces.types.restore_table_request
    import capo_keyspaces.types.restore_table_response
    import capo_keyspaces.types.schema_definition
    import capo_keyspaces.types.table_name
    import capo_keyspaces.types.table_summary
    import capo_keyspaces.types.tag
    import capo_keyspaces.types.tag_list
    import capo_keyspaces.types.tag_resource_request
    import capo_keyspaces.types.tag_resource_response
    import capo_keyspaces.types.time_to_live
    import capo_keyspaces.types.timestamp
    import capo_keyspaces.types.type_name
    import capo_keyspaces.types.untag_resource_request
    import capo_keyspaces.types.untag_resource_response
    import capo_keyspaces.types.update_keyspace_request
    import capo_keyspaces.types.update_keyspace_response
    import capo_keyspaces.types.update_table_request
    import capo_keyspaces.types.update_table_response
    import capo_keyspaces.types.warm_throughput_specification


class AsyncKeyspacesClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncKeyspacesClient:
    """A client for the ``Keyspaces`` service.

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
        self._config = AsyncKeyspacesClientConfig(
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
        self, config_overrides: Optional[AsyncKeyspacesClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncKeyspacesClientConfig = config_overrides or {}
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

    async def create_keyspace(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
        tags: Optional["capo_keyspaces.types.tag_list.TagList"] = None,
        replication_specification: Optional[
            "capo_keyspaces.types.replication_specification.ReplicationSpecification"
        ] = None,
    ) -> "capo_keyspaces.types.create_keyspace_response.CreateKeyspaceResponse":
        """<p>The <code>CreateKeyspace</code> operation adds a new keyspace to your account. In an Amazon Web Services account, keyspace names must be unique within each Region.</p> <p> <code>CreateKeyspace</code> is an asynchronous operation. You can monitor the creation status of the new keyspace by using the <code>GetKeyspace</code> operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.keyspaces.html">Create a keyspace</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>

        Args:
            keyspace_name: <p>The name of the keyspace to be created.</p>
            tags: <p>A list of key-value pair tags to be attached to the keyspace.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html">Adding tags and labels to Amazon Keyspaces resources</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            replication_specification: <p> The replication specification of the keyspace includes:</p> <ul> <li> <p> <code>replicationStrategy</code> - the required value is <code>SINGLE_REGION</code> or <code>MULTI_REGION</code>.</p> </li> <li> <p> <code>regionList</code> - if the <code>replicationStrategy</code> is <code>MULTI_REGION</code>, the <code>regionList</code> requires the current Region and at least one additional Amazon Web Services Region where the keyspace is going to be replicated in.</p> </li> </ul>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.conflict_exception.ConflictException: <p>Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.create_keyspace_request.CreateKeyspaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.create_keyspace_response.CreateKeyspaceResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.create_keyspace

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.create_keyspace.async_create_keyspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.create_keyspace_request.CreateKeyspaceRequest = {
            "keyspace_name": keyspace_name
        }
        if tags is not None:
            input_["tags"] = tags
        if replication_specification is not None:
            input_["replication_specification"] = replication_specification

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_table(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        table_name: "capo_keyspaces.types.table_name.TableName",
        schema_definition: "capo_keyspaces.types.schema_definition.SchemaDefinition",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
        comment: Optional["capo_keyspaces.types.comment.Comment"] = None,
        capacity_specification: Optional[
            "capo_keyspaces.types.capacity_specification.CapacitySpecification"
        ] = None,
        encryption_specification: Optional[
            "capo_keyspaces.types.encryption_specification.EncryptionSpecification"
        ] = None,
        point_in_time_recovery: Optional[
            "capo_keyspaces.types.point_in_time_recovery.PointInTimeRecovery"
        ] = None,
        ttl: Optional["capo_keyspaces.types.time_to_live.TimeToLive"] = None,
        default_time_to_live: Optional[
            "capo_keyspaces.types.default_time_to_live.DefaultTimeToLive"
        ] = None,
        tags: Optional["capo_keyspaces.types.tag_list.TagList"] = None,
        client_side_timestamps: Optional[
            "capo_keyspaces.types.client_side_timestamps.ClientSideTimestamps"
        ] = None,
        auto_scaling_specification: Optional[
            "capo_keyspaces.types.auto_scaling_specification.AutoScalingSpecification"
        ] = None,
        replica_specifications: Optional[
            "capo_keyspaces.types.replica_specification_list.ReplicaSpecificationList"
        ] = None,
        cdc_specification: Optional[
            "capo_keyspaces.types.cdc_specification.CdcSpecification"
        ] = None,
        warm_throughput_specification: Optional[
            "capo_keyspaces.types.warm_throughput_specification.WarmThroughputSpecification"
        ] = None,
    ) -> "capo_keyspaces.types.create_table_response.CreateTableResponse":
        """<p>The <code>CreateTable</code> operation adds a new table to the specified keyspace. Within a keyspace, table names must be unique.</p> <p> <code>CreateTable</code> is an asynchronous operation. When the request is received, the status of the table is set to <code>CREATING</code>. You can monitor the creation status of the new table by using the <code>GetTable</code> operation, which returns the current <code>status</code> of the table. You can start using a table when the status is <code>ACTIVE</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.tables.html">Create a table</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>

        Args:
            keyspace_name: <p>The name of the keyspace that the table is going to be created in.</p>
            table_name: <p>The name of the table.</p>
            schema_definition: <p>The <code>schemaDefinition</code> consists of the following parameters.</p> <p>For each column to be created:</p> <ul> <li> <p> <code>name</code> - The name of the column.</p> </li> <li> <p> <code>type</code> - An Amazon Keyspaces data type. For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.data-types">Data types</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p> </li> </ul> <p>The primary key of the table consists of the following columns:</p> <ul> <li> <p> <code>partitionKeys</code> - The partition key can be a single column, or it can be a compound value composed of two or more columns. The partition key portion of the primary key is required and determines how Amazon Keyspaces stores your data.</p> </li> <li> <p> <code>name</code> - The name of each partition key column.</p> </li> <li> <p> <code>clusteringKeys</code> - The optional clustering column portion of your primary key determines how the data is clustered and sorted within each partition.</p> </li> <li> <p> <code>name</code> - The name of the clustering column. </p> </li> <li> <p> <code>orderBy</code> - Sets the ascendant (<code>ASC</code>) or descendant (<code>DESC</code>) order modifier.</p> <p>To define a column as static use <code>staticColumns</code> - Static columns store values that are shared by all rows in the same partition:</p> </li> <li> <p> <code>name</code> - The name of the column.</p> </li> <li> <p> <code>type</code> - An Amazon Keyspaces data type.</p> </li> </ul>
            comment: <p>This parameter allows to enter a description of the table.</p>
            capacity_specification: <p>Specifies the read/write throughput capacity mode for the table. The options are:</p> <ul> <li> <p> <code>throughputMode:PAY_PER_REQUEST</code> and </p> </li> <li> <p> <code>throughputMode:PROVISIONED</code> - Provisioned capacity mode requires <code>readCapacityUnits</code> and <code>writeCapacityUnits</code> as input.</p> </li> </ul> <p>The default is <code>throughput_mode:PAY_PER_REQUEST</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html">Read/write capacity modes</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            encryption_specification: <p>Specifies how the encryption key for encryption at rest is managed for the table. You can choose one of the following KMS key (KMS key):</p> <ul> <li> <p> <code>type:AWS_OWNED_KMS_KEY</code> - This key is owned by Amazon Keyspaces. </p> </li> <li> <p> <code>type:CUSTOMER_MANAGED_KMS_KEY</code> - This key is stored in your account and is created, owned, and managed by you. This option requires the <code>kms_key_identifier</code> of the KMS key in Amazon Resource Name (ARN) format as input.</p> </li> </ul> <p>The default is <code>type:AWS_OWNED_KMS_KEY</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html">Encryption at rest</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            point_in_time_recovery: <p>Specifies if <code>pointInTimeRecovery</code> is enabled or disabled for the table. The options are:</p> <ul> <li> <p> <code>status=ENABLED</code> </p> </li> <li> <p> <code>status=DISABLED</code> </p> </li> </ul> <p>If it's not specified, the default is <code>status=DISABLED</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery.html">Point-in-time recovery</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            ttl: <p>Enables Time to Live custom settings for the table. The options are:</p> <ul> <li> <p> <code>status:enabled</code> </p> </li> <li> <p> <code>status:disabled</code> </p> </li> </ul> <p>The default is <code>status:disabled</code>. After <code>ttl</code> is enabled, you can't disable it for the table.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL.html">Expiring data by using Amazon Keyspaces Time to Live (TTL)</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            default_time_to_live: <p>The default Time to Live setting in seconds for the table.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-it-works.html#ttl-howitworks_default_ttl">Setting the default TTL value for a table</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            tags: <p>A list of key-value pair tags to be attached to the resource. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html">Adding tags and labels to Amazon Keyspaces resources</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            client_side_timestamps: <p> Enables client-side timestamps for the table. By default, the setting is disabled. You can enable client-side timestamps with the following option:</p> <ul> <li> <p> <code>status: "enabled"</code> </p> </li> </ul> <p>Once client-side timestamps are enabled for a table, this setting cannot be disabled.</p>
            auto_scaling_specification: <p>The optional auto scaling settings for a table in provisioned capacity mode. Specifies if the service can manage throughput capacity automatically on your behalf.</p> <p>Auto scaling helps you provision throughput capacity for variable workloads efficiently by increasing and decreasing your table's read and write capacity automatically in response to application traffic. For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html">Managing throughput capacity automatically with Amazon Keyspaces auto scaling</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p> <p>By default, auto scaling is disabled for a table. </p>
            replica_specifications: <p>The optional Amazon Web Services Region specific settings of a multi-Region table. These settings overwrite the general settings of the table for the specified Region. </p> <p>For a multi-Region table in provisioned capacity mode, you can configure the table's read capacity differently for each Region's replica. The write capacity, however, remains synchronized between all replicas to ensure that there's enough capacity to replicate writes across all Regions. To define the read capacity for a table replica in a specific Region, you can do so by configuring the following parameters.</p> <ul> <li> <p> <code>region</code>: The Region where these settings are applied. (Required)</p> </li> <li> <p> <code>readCapacityUnits</code>: The provisioned read capacity units. (Optional)</p> </li> <li> <p> <code>readCapacityAutoScaling</code>: The read capacity auto scaling settings for the table. (Optional) </p> </li> </ul>
            cdc_specification: <p>The CDC stream settings of the table.</p>
            warm_throughput_specification: <p>Specifies the warm throughput settings for the table. Pre-warming a table helps you avoid capacity exceeded exceptions by pre-provisioning read and write capacity units to reduce cold start latency when your table receives traffic.</p> <p>For more information about pre-warming in Amazon Keyspaces, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/warm-throughput.html">Pre-warm a table in Amazon Keyspaces</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.conflict_exception.ConflictException: <p>Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.create_table_request.CreateTableRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.create_table_response.CreateTableResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.create_table

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.create_table.async_create_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.create_table_request.CreateTableRequest = {
            "keyspace_name": keyspace_name,
            "table_name": table_name,
            "schema_definition": schema_definition,
        }
        if comment is not None:
            input_["comment"] = comment
        if capacity_specification is not None:
            input_["capacity_specification"] = capacity_specification
        if encryption_specification is not None:
            input_["encryption_specification"] = encryption_specification
        if point_in_time_recovery is not None:
            input_["point_in_time_recovery"] = point_in_time_recovery
        if ttl is not None:
            input_["ttl"] = ttl
        if default_time_to_live is not None:
            input_["default_time_to_live"] = default_time_to_live
        if tags is not None:
            input_["tags"] = tags
        if client_side_timestamps is not None:
            input_["client_side_timestamps"] = client_side_timestamps
        if auto_scaling_specification is not None:
            input_["auto_scaling_specification"] = auto_scaling_specification
        if replica_specifications is not None:
            input_["replica_specifications"] = replica_specifications
        if cdc_specification is not None:
            input_["cdc_specification"] = cdc_specification
        if warm_throughput_specification is not None:
            input_["warm_throughput_specification"] = warm_throughput_specification

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_type(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        type_name: "capo_keyspaces.types.type_name.TypeName",
        field_definitions: "capo_keyspaces.types.field_list.FieldList",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
    ) -> "capo_keyspaces.types.create_type_response.CreateTypeResponse":
        """<p> The <code>CreateType</code> operation creates a new user-defined type in the specified keyspace. </p> <p>To configure the required permissions, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/configure-udt-permissions.html#udt-permissions-create">Permissions to create a UDT</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/udts.html">User-defined types (UDTs)</a> in the <i>Amazon Keyspaces Developer Guide</i>. </p>

        Args:
            keyspace_name: <p> The name of the keyspace. </p>
            type_name: <p> The name of the user-defined type. </p> <p>UDT names must contain 48 characters or less, must begin with an alphabetic character, and can only contain alpha-numeric characters and underscores. Amazon Keyspaces converts upper case characters automatically into lower case characters. </p> <p>Alternatively, you can declare a UDT name in double quotes. When declaring a UDT name inside double quotes, Amazon Keyspaces preserves upper casing and allows special characters.</p> <p>You can also use double quotes as part of the name when you create the UDT, but you must escape each double quote character with an additional double quote character.</p>
            field_definitions: <p> The field definitions, consisting of names and types, that define this type. </p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.conflict_exception.ConflictException: <p>Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.create_type_request.CreateTypeRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.create_type_response.CreateTypeResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.create_type

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.create_type.async_create_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.create_type_request.CreateTypeRequest = {
            "keyspace_name": keyspace_name,
            "type_name": type_name,
            "field_definitions": field_definitions,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_keyspace(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
    ) -> "capo_keyspaces.types.delete_keyspace_response.DeleteKeyspaceResponse":
        """<p>The <code>DeleteKeyspace</code> operation deletes a keyspace and all of its tables. </p>

        Args:
            keyspace_name: <p>The name of the keyspace to be deleted.</p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.conflict_exception.ConflictException: <p>Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.delete_keyspace_request.DeleteKeyspaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.delete_keyspace_response.DeleteKeyspaceResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.delete_keyspace

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.delete_keyspace.async_delete_keyspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.delete_keyspace_request.DeleteKeyspaceRequest = {
            "keyspace_name": keyspace_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_table(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        table_name: "capo_keyspaces.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
    ) -> "capo_keyspaces.types.delete_table_response.DeleteTableResponse":
        """<p>The <code>DeleteTable</code> operation deletes a table and all of its data. After a <code>DeleteTable</code> request is received, the specified table is in the <code>DELETING</code> state until Amazon Keyspaces completes the deletion. If the table is in the <code>ACTIVE</code> state, you can delete it. If a table is either in the <code>CREATING</code> or <code>UPDATING</code> states, then Amazon Keyspaces returns a <code>ResourceInUseException</code>. If the specified table does not exist, Amazon Keyspaces returns a <code>ResourceNotFoundException</code>. If the table is already in the <code>DELETING</code> state, no error is returned.</p>

        Args:
            keyspace_name: <p>The name of the keyspace of the to be deleted table.</p>
            table_name: <p>The name of the table to be deleted.</p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.conflict_exception.ConflictException: <p>Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.delete_table_request.DeleteTableRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.delete_table_response.DeleteTableResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.delete_table

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.delete_table.async_delete_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.delete_table_request.DeleteTableRequest = {
            "keyspace_name": keyspace_name,
            "table_name": table_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_type(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        type_name: "capo_keyspaces.types.type_name.TypeName",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
    ) -> "capo_keyspaces.types.delete_type_response.DeleteTypeResponse":
        """<p> The <code>DeleteType</code> operation deletes a user-defined type (UDT). You can only delete a type that is not used in a table or another UDT. </p> <p>To configure the required permissions, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/configure-udt-permissions.html#udt-permissions-drop">Permissions to delete a UDT</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>

        Args:
            keyspace_name: <p> The name of the keyspace of the to be deleted type. </p>
            type_name: <p> The name of the type to be deleted. </p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.conflict_exception.ConflictException: <p>Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.delete_type_request.DeleteTypeRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.delete_type_response.DeleteTypeResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.delete_type

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.delete_type.async_delete_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.delete_type_request.DeleteTypeRequest = {
            "keyspace_name": keyspace_name,
            "type_name": type_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_keyspace(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
    ) -> "capo_keyspaces.types.get_keyspace_response.GetKeyspaceResponse":
        """<p>Returns the name of the specified keyspace, the Amazon Resource Name (ARN), the replication strategy, the Amazon Web Services Regions of a multi-Region keyspace, and the status of newly added Regions after an <code>UpdateKeyspace</code> operation.</p>

        Args:
            keyspace_name: <p>The name of the keyspace.</p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.get_keyspace_request.GetKeyspaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.get_keyspace_response.GetKeyspaceResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.get_keyspace

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.get_keyspace.async_get_keyspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.get_keyspace_request.GetKeyspaceRequest = {
            "keyspace_name": keyspace_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        table_name: "capo_keyspaces.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
    ) -> "capo_keyspaces.types.get_table_response.GetTableResponse":
        """<p>Returns information about the table, including the table's name and current status, the keyspace name, configuration settings, and metadata.</p> <p>To read table metadata using <code>GetTable</code>, the IAM principal needs <code>Select</code> action permissions for the table and the system keyspace.</p>

        Args:
            keyspace_name: <p>The name of the keyspace that the table is stored in.</p>
            table_name: <p>The name of the table.</p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.get_table_request.GetTableRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.get_table_response.GetTableResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.get_table

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.get_table.async_get_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.get_table_request.GetTableRequest = {
            "keyspace_name": keyspace_name,
            "table_name": table_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table_auto_scaling_settings(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        table_name: "capo_keyspaces.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
    ) -> "capo_keyspaces.types.get_table_auto_scaling_settings_response.GetTableAutoScalingSettingsResponse":
        """<p>Returns auto scaling related settings of the specified table in JSON format. If the table is a multi-Region table, the Amazon Web Services Region specific auto scaling settings of the table are included.</p> <p>Amazon Keyspaces auto scaling helps you provision throughput capacity for variable workloads efficiently by increasing and decreasing your table's read and write capacity automatically in response to application traffic. For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html">Managing throughput capacity automatically with Amazon Keyspaces auto scaling</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p> <important> <p> <code>GetTableAutoScalingSettings</code> can't be used as an action in an IAM policy.</p> </important> <p>To define permissions for <code>GetTableAutoScalingSettings</code>, you must allow the following two actions in the IAM policy statement's <code>Action</code> element:</p> <ul> <li> <p> <code>application-autoscaling:DescribeScalableTargets</code> </p> </li> <li> <p> <code>application-autoscaling:DescribeScalingPolicies</code> </p> </li> </ul>

        Args:
            keyspace_name: <p>The name of the keyspace.</p>
            table_name: <p>The name of the table.</p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.get_table_auto_scaling_settings_request.GetTableAutoScalingSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.get_table_auto_scaling_settings_response.GetTableAutoScalingSettingsResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.get_table_auto_scaling_settings

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.get_table_auto_scaling_settings.async_get_table_auto_scaling_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.get_table_auto_scaling_settings_request.GetTableAutoScalingSettingsRequest = {
            "keyspace_name": keyspace_name,
            "table_name": table_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_type(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        type_name: "capo_keyspaces.types.type_name.TypeName",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
    ) -> "capo_keyspaces.types.get_type_response.GetTypeResponse":
        """<p> The <code>GetType</code> operation returns information about the type, for example the field definitions, the timestamp when the type was last modified, the level of nesting, the status, and details about if the type is used in other types and tables. </p> <p>To read keyspace metadata using <code>GetType</code>, the IAM principal needs <code>Select</code> action permissions for the system keyspace. To configure the required permissions, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/configure-udt-permissions.html#udt-permissions-view">Permissions to view a UDT</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>

        Args:
            keyspace_name: <p> The name of the keyspace that contains this type. </p>
            type_name: <p>The formatted name of the type. For example, if the name of the type was created without double quotes, Amazon Keyspaces saved the name in lower-case characters. If the name was created in double quotes, you must use double quotes to specify the type name. </p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.get_type_request.GetTypeRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.get_type_response.GetTypeResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.get_type

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.get_type.async_get_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.get_type_request.GetTypeRequest = {
            "keyspace_name": keyspace_name,
            "type_name": type_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_keyspaces(
        self,
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
        next_token: Optional["capo_keyspaces.types.next_token.NextToken"] = None,
        max_results: Optional["capo_keyspaces.types.max_results.MaxResults"] = None,
    ) -> "capo_keyspaces.types.list_keyspaces_response.ListKeyspacesResponse":
        """<p>The <code>ListKeyspaces</code> operation returns a list of keyspaces.</p>

        Args:
            next_token: <p>The pagination token. To resume pagination, provide the <code>NextToken</code> value as argument of a subsequent API invocation.</p>
            max_results: <p>The total number of keyspaces to return in the output. If the total number of keyspaces available is more than the value specified, a <code>NextToken</code> is provided in the output. To resume pagination, provide the <code>NextToken</code> value as an argument of a subsequent API invocation.</p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.list_keyspaces_request.ListKeyspacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.list_keyspaces_response.ListKeyspacesResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.list_keyspaces

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.list_keyspaces.async_list_keyspaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.list_keyspaces_request.ListKeyspacesRequest = {}
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

    async def iter_list_keyspaces(
        self,
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
        next_token: Optional["capo_keyspaces.types.next_token.NextToken"] = None,
        max_results: Optional["capo_keyspaces.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_keyspaces.types.keyspace_summary.KeyspaceSummary]":
        _token = next_token
        while True:
            _response = await self.list_keyspaces(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("keyspaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tables(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
        next_token: Optional["capo_keyspaces.types.next_token.NextToken"] = None,
        max_results: Optional["capo_keyspaces.types.max_results.MaxResults"] = None,
    ) -> "capo_keyspaces.types.list_tables_response.ListTablesResponse":
        """<p>The <code>ListTables</code> operation returns a list of tables for a specified keyspace.</p> <p>To read keyspace metadata using <code>ListTables</code>, the IAM principal needs <code>Select</code> action permissions for the system keyspace.</p>

        Args:
            next_token: <p>The pagination token. To resume pagination, provide the <code>NextToken</code> value as an argument of a subsequent API invocation.</p>
            max_results: <p>The total number of tables to return in the output. If the total number of tables available is more than the value specified, a <code>NextToken</code> is provided in the output. To resume pagination, provide the <code>NextToken</code> value as an argument of a subsequent API invocation.</p>
            keyspace_name: <p>The name of the keyspace.</p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.list_tables_request.ListTablesRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.list_tables_response.ListTablesResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.list_tables

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.list_tables.async_list_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.list_tables_request.ListTablesRequest = {
            "keyspace_name": keyspace_name
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

    async def iter_list_tables(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
        next_token: Optional["capo_keyspaces.types.next_token.NextToken"] = None,
        max_results: Optional["capo_keyspaces.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_keyspaces.types.table_summary.TableSummary]":
        _token = next_token
        while True:
            _response = await self.list_tables(
                keyspace_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tables",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_keyspaces.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
        next_token: Optional["capo_keyspaces.types.next_token.NextToken"] = None,
        max_results: Optional["capo_keyspaces.types.max_results.MaxResults"] = None,
    ) -> "capo_keyspaces.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of all tags associated with the specified Amazon Keyspaces resource.</p> <p>To read keyspace metadata using <code>ListTagsForResource</code>, the IAM principal needs <code>Select</code> action permissions for the specified resource and the system keyspace.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Keyspaces resource.</p>
            next_token: <p>The pagination token. To resume pagination, provide the <code>NextToken</code> value as argument of a subsequent API invocation.</p>
            max_results: <p>The total number of tags to return in the output. If the total number of tags available is more than the value specified, a <code>NextToken</code> is provided in the output. To resume pagination, provide the <code>NextToken</code> value as an argument of a subsequent API invocation.</p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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

    async def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_keyspaces.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
        next_token: Optional["capo_keyspaces.types.next_token.NextToken"] = None,
        max_results: Optional["capo_keyspaces.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_keyspaces.types.tag.Tag]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_types(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
        next_token: Optional["capo_keyspaces.types.next_token.NextToken"] = None,
        max_results: Optional["capo_keyspaces.types.max_results.MaxResults"] = None,
    ) -> "capo_keyspaces.types.list_types_response.ListTypesResponse":
        """<p> The <code>ListTypes</code> operation returns a list of types for a specified keyspace. </p> <p>To read keyspace metadata using <code>ListTypes</code>, the IAM principal needs <code>Select</code> action permissions for the system keyspace. To configure the required permissions, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/configure-udt-permissions.html#udt-permissions-view">Permissions to view a UDT</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>

        Args:
            next_token: <p> The pagination token. To resume pagination, provide the <code>NextToken</code> value as an argument of a subsequent API invocation. </p>
            max_results: <p> The total number of types to return in the output. If the total number of types available is more than the value specified, a <code>NextToken</code> is provided in the output. To resume pagination, provide the <code>NextToken</code> value as an argument of a subsequent API invocation. </p>
            keyspace_name: <p> The name of the keyspace that contains the listed types. </p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.list_types_request.ListTypesRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.list_types_response.ListTypesResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.list_types

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.list_types.async_list_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.list_types_request.ListTypesRequest = {
            "keyspace_name": keyspace_name
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

    async def iter_list_types(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
        next_token: Optional["capo_keyspaces.types.next_token.NextToken"] = None,
        max_results: Optional["capo_keyspaces.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_keyspaces.types.type_name.TypeName]":
        _token = next_token
        while True:
            _response = await self.list_types(
                keyspace_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def restore_table(
        self,
        source_keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        source_table_name: "capo_keyspaces.types.table_name.TableName",
        target_keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        target_table_name: "capo_keyspaces.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
        restore_timestamp: Optional["capo_keyspaces.types.timestamp.Timestamp"] = None,
        capacity_specification_override: Optional[
            "capo_keyspaces.types.capacity_specification.CapacitySpecification"
        ] = None,
        encryption_specification_override: Optional[
            "capo_keyspaces.types.encryption_specification.EncryptionSpecification"
        ] = None,
        point_in_time_recovery_override: Optional[
            "capo_keyspaces.types.point_in_time_recovery.PointInTimeRecovery"
        ] = None,
        tags_override: Optional["capo_keyspaces.types.tag_list.TagList"] = None,
        auto_scaling_specification: Optional[
            "capo_keyspaces.types.auto_scaling_specification.AutoScalingSpecification"
        ] = None,
        replica_specifications: Optional[
            "capo_keyspaces.types.replica_specification_list.ReplicaSpecificationList"
        ] = None,
    ) -> "capo_keyspaces.types.restore_table_response.RestoreTableResponse":
        """<p>Restores the table to the specified point in time within the <code>earliest_restorable_timestamp</code> and the current time. For more information about restore points, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery_HowItWorks.html#howitworks_backup_window"> Time window for PITR continuous backups</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p> <p>Any number of users can execute up to 4 concurrent restores (any type of restore) in a given account.</p> <p>When you restore using point in time recovery, Amazon Keyspaces restores your source table's schema and data to the state based on the selected timestamp <code>(day:hour:minute:second)</code> to a new table. The Time to Live (TTL) settings are also restored to the state based on the selected timestamp.</p> <p>In addition to the table's schema, data, and TTL settings, <code>RestoreTable</code> restores the capacity mode, auto scaling settings, encryption settings, and point-in-time recovery settings from the source table. Unlike the table's schema data and TTL settings, which are restored based on the selected timestamp, these settings are always restored based on the table's settings as of the current time or when the table was deleted.</p> <p>You can also overwrite these settings during restore:</p> <ul> <li> <p>Read/write capacity mode</p> </li> <li> <p>Provisioned throughput capacity units</p> </li> <li> <p>Auto scaling settings</p> </li> <li> <p>Point-in-time (PITR) settings</p> </li> <li> <p>Tags</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery_HowItWorks.html#howitworks_backup_settings">PITR restore settings</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p> <p>Note that the following settings are not restored, and you must configure them manually for the new table:</p> <ul> <li> <p>Identity and Access Management (IAM) policies</p> </li> <li> <p>Amazon CloudWatch metrics and alarms</p> </li> </ul>

        Args:
            source_keyspace_name: <p>The keyspace name of the source table.</p>
            source_table_name: <p>The name of the source table.</p>
            target_keyspace_name: <p>The name of the target keyspace.</p>
            target_table_name: <p>The name of the target table.</p>
            restore_timestamp: <p>The restore timestamp in ISO 8601 format.</p>
            capacity_specification_override: <p>Specifies the read/write throughput capacity mode for the target table. The options are:</p> <ul> <li> <p> <code>throughputMode:PAY_PER_REQUEST</code> </p> </li> <li> <p> <code>throughputMode:PROVISIONED</code> - Provisioned capacity mode requires <code>readCapacityUnits</code> and <code>writeCapacityUnits</code> as input.</p> </li> </ul> <p>The default is <code>throughput_mode:PAY_PER_REQUEST</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html">Read/write capacity modes</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            encryption_specification_override: <p>Specifies the encryption settings for the target table. You can choose one of the following KMS key (KMS key):</p> <ul> <li> <p> <code>type:AWS_OWNED_KMS_KEY</code> - This key is owned by Amazon Keyspaces. </p> </li> <li> <p> <code>type:CUSTOMER_MANAGED_KMS_KEY</code> - This key is stored in your account and is created, owned, and managed by you. This option requires the <code>kms_key_identifier</code> of the KMS key in Amazon Resource Name (ARN) format as input. </p> </li> </ul> <p>The default is <code>type:AWS_OWNED_KMS_KEY</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html">Encryption at rest</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            point_in_time_recovery_override: <p>Specifies the <code>pointInTimeRecovery</code> settings for the target table. The options are:</p> <ul> <li> <p> <code>status=ENABLED</code> </p> </li> <li> <p> <code>status=DISABLED</code> </p> </li> </ul> <p>If it's not specified, the default is <code>status=DISABLED</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery.html">Point-in-time recovery</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            tags_override: <p>A list of key-value pair tags to be attached to the restored table. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html">Adding tags and labels to Amazon Keyspaces resources</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            auto_scaling_specification: <p>The optional auto scaling settings for the restored table in provisioned capacity mode. Specifies if the service can manage throughput capacity of a provisioned table automatically on your behalf. Amazon Keyspaces auto scaling helps you provision throughput capacity for variable workloads efficiently by increasing and decreasing your table's read and write capacity automatically in response to application traffic.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html">Managing throughput capacity automatically with Amazon Keyspaces auto scaling</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            replica_specifications: <p>The optional Region specific settings of a multi-Regional table.</p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.conflict_exception.ConflictException: <p>Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.restore_table_request.RestoreTableRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.restore_table_response.RestoreTableResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.restore_table

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.restore_table.async_restore_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.restore_table_request.RestoreTableRequest = {
            "source_keyspace_name": source_keyspace_name,
            "source_table_name": source_table_name,
            "target_keyspace_name": target_keyspace_name,
            "target_table_name": target_table_name,
        }
        if restore_timestamp is not None:
            input_["restore_timestamp"] = restore_timestamp
        if capacity_specification_override is not None:
            input_["capacity_specification_override"] = capacity_specification_override
        if encryption_specification_override is not None:
            input_["encryption_specification_override"] = (
                encryption_specification_override
            )
        if point_in_time_recovery_override is not None:
            input_["point_in_time_recovery_override"] = point_in_time_recovery_override
        if tags_override is not None:
            input_["tags_override"] = tags_override
        if auto_scaling_specification is not None:
            input_["auto_scaling_specification"] = auto_scaling_specification
        if replica_specifications is not None:
            input_["replica_specifications"] = replica_specifications

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_keyspaces.types.arn.ARN",
        tags: "capo_keyspaces.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
    ) -> "capo_keyspaces.types.tag_resource_response.TagResourceResponse":
        """<p>Associates a set of tags with a Amazon Keyspaces resource. You can then activate these user-defined tags so that they appear on the Cost Management Console for cost allocation tracking. For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html">Adding tags and labels to Amazon Keyspaces resources</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p> <p>For IAM policy examples that show how to control access to Amazon Keyspaces resources based on tags, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-tags">Amazon Keyspaces resource access based on tags</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Keyspaces resource to which to add tags.</p>
            tags: <p>The tags to be assigned to the Amazon Keyspaces resource.</p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.conflict_exception.ConflictException: <p>Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_keyspaces.types.arn.ARN",
        tags: "capo_keyspaces.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
    ) -> "capo_keyspaces.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the association of tags from a Amazon Keyspaces resource.</p>

        Args:
            resource_arn: <p>The Amazon Keyspaces resource that the tags will be removed from. This value is an Amazon Resource Name (ARN).</p>
            tags: <p>A list of existing tags to be removed from the Amazon Keyspaces resource.</p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.conflict_exception.ConflictException: <p>Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_keyspace(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        replication_specification: "capo_keyspaces.types.replication_specification.ReplicationSpecification",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
        client_side_timestamps: Optional[
            "capo_keyspaces.types.client_side_timestamps.ClientSideTimestamps"
        ] = None,
    ) -> "capo_keyspaces.types.update_keyspace_response.UpdateKeyspaceResponse":
        """<p> Adds a new Amazon Web Services Region to the keyspace. You can add a new Region to a keyspace that is either a single or a multi-Region keyspace. Amazon Keyspaces is going to replicate all tables in the keyspace to the new Region. To successfully replicate all tables to the new Region, they must use client-side timestamps for conflict resolution. To enable client-side timestamps, specify <code>clientSideTimestamps.status = enabled</code> when invoking the API. For more information about client-side timestamps, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/client-side-timestamps.html">Client-side timestamps in Amazon Keyspaces</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p> <p>To add a Region to a keyspace using the <code>UpdateKeyspace</code> API, the IAM principal needs permissions for the following IAM actions:</p> <ul> <li> <p> <code>cassandra:Alter</code> </p> </li> <li> <p> <code>cassandra:AlterMultiRegionResource</code> </p> </li> <li> <p> <code>cassandra:Create</code> </p> </li> <li> <p> <code>cassandra:CreateMultiRegionResource</code> </p> </li> <li> <p> <code>cassandra:Select</code> </p> </li> <li> <p> <code>cassandra:SelectMultiRegionResource</code> </p> </li> <li> <p> <code>cassandra:Modify</code> </p> </li> <li> <p> <code>cassandra:ModifyMultiRegionResource</code> </p> </li> </ul> <p>If the keyspace contains a table that is configured in provisioned mode with auto scaling enabled, the following additional IAM actions need to be allowed.</p> <ul> <li> <p> <code>application-autoscaling:RegisterScalableTarget</code> </p> </li> <li> <p> <code>application-autoscaling:DeregisterScalableTarget</code> </p> </li> <li> <p> <code>application-autoscaling:DescribeScalableTargets</code> </p> </li> <li> <p> <code>application-autoscaling:PutScalingPolicy</code> </p> </li> <li> <p> <code>application-autoscaling:DescribeScalingPolicies</code> </p> </li> </ul> <p>To use the <code>UpdateKeyspace</code> API, the IAM principal also needs permissions to create a service-linked role with the following elements:</p> <ul> <li> <p> <code>iam:CreateServiceLinkedRole</code> - The <b>action</b> the principal can perform.</p> </li> <li> <p> <code>arn:aws:iam::*:role/aws-service-role/replication.cassandra.amazonaws.com/AWSServiceRoleForKeyspacesReplication</code> - The <b>resource</b> that the action can be performed on. </p> </li> <li> <p> <code>iam:AWSServiceName: replication.cassandra.amazonaws.com</code> - The only Amazon Web Services service that this role can be attached to is Amazon Keyspaces.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/howitworks_replication_permissions_addReplica.html">Configure the IAM permissions required to add an Amazon Web Services Region to a keyspace</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>

        Args:
            keyspace_name: <p> The name of the keyspace. </p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.conflict_exception.ConflictException: <p>Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.update_keyspace_request.UpdateKeyspaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.update_keyspace_response.UpdateKeyspaceResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.update_keyspace

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.update_keyspace.async_update_keyspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.update_keyspace_request.UpdateKeyspaceRequest = {
            "keyspace_name": keyspace_name,
            "replication_specification": replication_specification,
        }
        if client_side_timestamps is not None:
            input_["client_side_timestamps"] = client_side_timestamps

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_table(
        self,
        keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName",
        table_name: "capo_keyspaces.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncKeyspacesClientConfig] = None,
        add_columns: Optional[
            "capo_keyspaces.types.column_definition_list.ColumnDefinitionList"
        ] = None,
        capacity_specification: Optional[
            "capo_keyspaces.types.capacity_specification.CapacitySpecification"
        ] = None,
        encryption_specification: Optional[
            "capo_keyspaces.types.encryption_specification.EncryptionSpecification"
        ] = None,
        point_in_time_recovery: Optional[
            "capo_keyspaces.types.point_in_time_recovery.PointInTimeRecovery"
        ] = None,
        ttl: Optional["capo_keyspaces.types.time_to_live.TimeToLive"] = None,
        default_time_to_live: Optional[
            "capo_keyspaces.types.default_time_to_live.DefaultTimeToLive"
        ] = None,
        client_side_timestamps: Optional[
            "capo_keyspaces.types.client_side_timestamps.ClientSideTimestamps"
        ] = None,
        auto_scaling_specification: Optional[
            "capo_keyspaces.types.auto_scaling_specification.AutoScalingSpecification"
        ] = None,
        replica_specifications: Optional[
            "capo_keyspaces.types.replica_specification_list.ReplicaSpecificationList"
        ] = None,
        cdc_specification: Optional[
            "capo_keyspaces.types.cdc_specification.CdcSpecification"
        ] = None,
        warm_throughput_specification: Optional[
            "capo_keyspaces.types.warm_throughput_specification.WarmThroughputSpecification"
        ] = None,
    ) -> "capo_keyspaces.types.update_table_response.UpdateTableResponse":
        """<p>Adds new columns to the table or updates one of the table's settings, for example capacity mode, auto scaling, encryption, point-in-time recovery, or ttl settings. Note that you can only update one specific table setting per update operation.</p>

        Args:
            keyspace_name: <p>The name of the keyspace the specified table is stored in.</p>
            table_name: <p>The name of the table.</p>
            add_columns: <p>For each column to be added to the specified table:</p> <ul> <li> <p> <code>name</code> - The name of the column.</p> </li> <li> <p> <code>type</code> - An Amazon Keyspaces data type. For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.data-types">Data types</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p> </li> </ul>
            capacity_specification: <p>Modifies the read/write throughput capacity mode for the table. The options are:</p> <ul> <li> <p> <code>throughputMode:PAY_PER_REQUEST</code> and </p> </li> <li> <p> <code>throughputMode:PROVISIONED</code> - Provisioned capacity mode requires <code>readCapacityUnits</code> and <code>writeCapacityUnits</code> as input.</p> </li> </ul> <p>The default is <code>throughput_mode:PAY_PER_REQUEST</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html">Read/write capacity modes</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            encryption_specification: <p>Modifies the encryption settings of the table. You can choose one of the following KMS key (KMS key):</p> <ul> <li> <p> <code>type:AWS_OWNED_KMS_KEY</code> - This key is owned by Amazon Keyspaces. </p> </li> <li> <p> <code>type:CUSTOMER_MANAGED_KMS_KEY</code> - This key is stored in your account and is created, owned, and managed by you. This option requires the <code>kms_key_identifier</code> of the KMS key in Amazon Resource Name (ARN) format as input. </p> </li> </ul> <p>The default is <code>AWS_OWNED_KMS_KEY</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html">Encryption at rest</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            point_in_time_recovery: <p>Modifies the <code>pointInTimeRecovery</code> settings of the table. The options are:</p> <ul> <li> <p> <code>status=ENABLED</code> </p> </li> <li> <p> <code>status=DISABLED</code> </p> </li> </ul> <p>If it's not specified, the default is <code>status=DISABLED</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery.html">Point-in-time recovery</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            ttl: <p>Modifies Time to Live custom settings for the table. The options are:</p> <ul> <li> <p> <code>status:enabled</code> </p> </li> <li> <p> <code>status:disabled</code> </p> </li> </ul> <p>The default is <code>status:disabled</code>. After <code>ttl</code> is enabled, you can't disable it for the table.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL.html">Expiring data by using Amazon Keyspaces Time to Live (TTL)</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            default_time_to_live: <p>The default Time to Live setting in seconds for the table.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-it-works.html#ttl-howitworks_default_ttl">Setting the default TTL value for a table</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            client_side_timestamps: <p>Enables client-side timestamps for the table. By default, the setting is disabled. You can enable client-side timestamps with the following option:</p> <ul> <li> <p> <code>status: "enabled"</code> </p> </li> </ul> <p>Once client-side timestamps are enabled for a table, this setting cannot be disabled.</p>
            auto_scaling_specification: <p>The optional auto scaling settings to update for a table in provisioned capacity mode. Specifies if the service can manage throughput capacity of a provisioned table automatically on your behalf. Amazon Keyspaces auto scaling helps you provision throughput capacity for variable workloads efficiently by increasing and decreasing your table's read and write capacity automatically in response to application traffic.</p> <p>If auto scaling is already enabled for the table, you can use <code>UpdateTable</code> to update the minimum and maximum values or the auto scaling policy settings independently.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html">Managing throughput capacity automatically with Amazon Keyspaces auto scaling</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            replica_specifications: <p>The Region specific settings of a multi-Regional table.</p>
            cdc_specification: <p>The CDC stream settings of the table.</p>
            warm_throughput_specification: <p>Modifies the warm throughput settings for the table. You can update the read and write capacity units to adjust the pre-provisioned throughput.</p>

        Raises:
            capo_keyspaces.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access permissions to perform this action. </p>
            capo_keyspaces.errors.conflict_exception.ConflictException: <p>Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists. </p>
            capo_keyspaces.errors.internal_server_exception.InternalServerException: <p>Amazon Keyspaces was unable to fully process this request because of an internal server error.</p>
            capo_keyspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_keyspaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource. For more information on service quotas, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html">Quotas</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>
            capo_keyspaces.errors.validation_exception.ValidationException: <p>The operation failed due to an invalid or malformed request.</p>
            capo_keyspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_keyspaces.types.update_table_request.UpdateTableRequest]",
        ) -> AsyncOperationResponse[
            "capo_keyspaces.types.update_table_response.UpdateTableResponse"
        ]:
            import capo_keyspaces._operations.keyspaces_service.update_table

            (
                output,
                http_response,
            ) = await capo_keyspaces._operations.keyspaces_service.update_table.async_update_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_keyspaces.types.update_table_request.UpdateTableRequest = {
            "keyspace_name": keyspace_name,
            "table_name": table_name,
        }
        if add_columns is not None:
            input_["add_columns"] = add_columns
        if capacity_specification is not None:
            input_["capacity_specification"] = capacity_specification
        if encryption_specification is not None:
            input_["encryption_specification"] = encryption_specification
        if point_in_time_recovery is not None:
            input_["point_in_time_recovery"] = point_in_time_recovery
        if ttl is not None:
            input_["ttl"] = ttl
        if default_time_to_live is not None:
            input_["default_time_to_live"] = default_time_to_live
        if client_side_timestamps is not None:
            input_["client_side_timestamps"] = client_side_timestamps
        if auto_scaling_specification is not None:
            input_["auto_scaling_specification"] = auto_scaling_specification
        if replica_specifications is not None:
            input_["replica_specifications"] = replica_specifications
        if cdc_specification is not None:
            input_["cdc_specification"] = cdc_specification
        if warm_throughput_specification is not None:
            input_["warm_throughput_specification"] = warm_throughput_specification

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
