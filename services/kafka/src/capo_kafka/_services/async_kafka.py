"""Generated from Smithy shape ``com.amazonaws.kafka#Kafka``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_kafka._auth._signers
import capo_kafka._auth._sigv4
from capo_kafka._auth._identity import Credentials
from capo_kafka._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_kafka._auth._zapros_handler import AuthMiddleware
from capo_kafka._pagination import resolve_path as _resolve_path
from capo_kafka._services._aws_config import aaws_config
from capo_kafka._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_kafka.types.__blob
    import capo_kafka.types.__integer
    import capo_kafka.types.__integer_min1
    import capo_kafka.types.__integer_min1_max15
    import capo_kafka.types.__list_of__string
    import capo_kafka.types.__list_of_broker_ebs_volume_info
    import capo_kafka.types.__list_of_kafka_cluster
    import capo_kafka.types.__list_of_replication_info
    import capo_kafka.types.__list_of_topic_configuration
    import capo_kafka.types.__long
    import capo_kafka.types.__map_of__string
    import capo_kafka.types.__string
    import capo_kafka.types.__string_max1024
    import capo_kafka.types.__string_min1_max64
    import capo_kafka.types.__string_min1_max128
    import capo_kafka.types.__string_min1_max128_pattern09_a_za_z09_a_za_z0
    import capo_kafka.types.batch_associate_scram_secret_request
    import capo_kafka.types.batch_associate_scram_secret_response
    import capo_kafka.types.batch_disassociate_scram_secret_request
    import capo_kafka.types.batch_disassociate_scram_secret_response
    import capo_kafka.types.broker_node_group_info
    import capo_kafka.types.channel_logging_info
    import capo_kafka.types.client_authentication
    import capo_kafka.types.client_vpc_connection
    import capo_kafka.types.cluster
    import capo_kafka.types.cluster_info
    import capo_kafka.types.cluster_operation_info
    import capo_kafka.types.cluster_operation_v2_summary
    import capo_kafka.types.configuration
    import capo_kafka.types.configuration_info
    import capo_kafka.types.configuration_revision
    import capo_kafka.types.connectivity_info
    import capo_kafka.types.consumer_group_replication_update
    import capo_kafka.types.create_channel_request
    import capo_kafka.types.create_channel_response
    import capo_kafka.types.create_cluster_request
    import capo_kafka.types.create_cluster_response
    import capo_kafka.types.create_cluster_v2_request
    import capo_kafka.types.create_cluster_v2_response
    import capo_kafka.types.create_configuration_request
    import capo_kafka.types.create_configuration_response
    import capo_kafka.types.create_replicator_request
    import capo_kafka.types.create_replicator_response
    import capo_kafka.types.create_topic_request
    import capo_kafka.types.create_topic_response
    import capo_kafka.types.create_vpc_connection_request
    import capo_kafka.types.create_vpc_connection_response
    import capo_kafka.types.delete_channel_request
    import capo_kafka.types.delete_channel_response
    import capo_kafka.types.delete_cluster_policy_request
    import capo_kafka.types.delete_cluster_policy_response
    import capo_kafka.types.delete_cluster_request
    import capo_kafka.types.delete_cluster_response
    import capo_kafka.types.delete_configuration_request
    import capo_kafka.types.delete_configuration_response
    import capo_kafka.types.delete_replicator_request
    import capo_kafka.types.delete_replicator_response
    import capo_kafka.types.delete_topic_request
    import capo_kafka.types.delete_topic_response
    import capo_kafka.types.delete_vpc_connection_request
    import capo_kafka.types.delete_vpc_connection_response
    import capo_kafka.types.describe_channel_request
    import capo_kafka.types.describe_channel_response
    import capo_kafka.types.describe_cluster_operation_request
    import capo_kafka.types.describe_cluster_operation_response
    import capo_kafka.types.describe_cluster_operation_v2_request
    import capo_kafka.types.describe_cluster_operation_v2_response
    import capo_kafka.types.describe_cluster_request
    import capo_kafka.types.describe_cluster_response
    import capo_kafka.types.describe_cluster_v2_request
    import capo_kafka.types.describe_cluster_v2_response
    import capo_kafka.types.describe_configuration_request
    import capo_kafka.types.describe_configuration_response
    import capo_kafka.types.describe_configuration_revision_request
    import capo_kafka.types.describe_configuration_revision_response
    import capo_kafka.types.describe_replicator_request
    import capo_kafka.types.describe_replicator_response
    import capo_kafka.types.describe_topic_partitions_request
    import capo_kafka.types.describe_topic_partitions_response
    import capo_kafka.types.describe_topic_request
    import capo_kafka.types.describe_topic_response
    import capo_kafka.types.describe_vpc_connection_request
    import capo_kafka.types.describe_vpc_connection_response
    import capo_kafka.types.encryption_configuration
    import capo_kafka.types.encryption_info
    import capo_kafka.types.enhanced_monitoring
    import capo_kafka.types.get_bootstrap_brokers_request
    import capo_kafka.types.get_bootstrap_brokers_response
    import capo_kafka.types.get_cluster_policy_request
    import capo_kafka.types.get_cluster_policy_response
    import capo_kafka.types.get_compatible_kafka_versions_request
    import capo_kafka.types.get_compatible_kafka_versions_response
    import capo_kafka.types.iceberg_destination_configuration
    import capo_kafka.types.iceberg_destination_update
    import capo_kafka.types.kafka_version
    import capo_kafka.types.list_channels_request
    import capo_kafka.types.list_channels_response
    import capo_kafka.types.list_client_vpc_connections_request
    import capo_kafka.types.list_client_vpc_connections_response
    import capo_kafka.types.list_cluster_operations_request
    import capo_kafka.types.list_cluster_operations_response
    import capo_kafka.types.list_cluster_operations_v2_request
    import capo_kafka.types.list_cluster_operations_v2_response
    import capo_kafka.types.list_clusters_request
    import capo_kafka.types.list_clusters_response
    import capo_kafka.types.list_clusters_v2_request
    import capo_kafka.types.list_clusters_v2_response
    import capo_kafka.types.list_configuration_revisions_request
    import capo_kafka.types.list_configuration_revisions_response
    import capo_kafka.types.list_configurations_request
    import capo_kafka.types.list_configurations_response
    import capo_kafka.types.list_kafka_versions_request
    import capo_kafka.types.list_kafka_versions_response
    import capo_kafka.types.list_nodes_request
    import capo_kafka.types.list_nodes_response
    import capo_kafka.types.list_replicators_request
    import capo_kafka.types.list_replicators_response
    import capo_kafka.types.list_scram_secrets_request
    import capo_kafka.types.list_scram_secrets_response
    import capo_kafka.types.list_tags_for_resource_request
    import capo_kafka.types.list_tags_for_resource_response
    import capo_kafka.types.list_topics_request
    import capo_kafka.types.list_topics_response
    import capo_kafka.types.list_vpc_connections_request
    import capo_kafka.types.list_vpc_connections_response
    import capo_kafka.types.log_delivery
    import capo_kafka.types.logging_info
    import capo_kafka.types.max_results
    import capo_kafka.types.node_info
    import capo_kafka.types.open_monitoring_info
    import capo_kafka.types.provisioned_request
    import capo_kafka.types.provisioned_throughput
    import capo_kafka.types.put_cluster_policy_request
    import capo_kafka.types.put_cluster_policy_response
    import capo_kafka.types.rebalancing
    import capo_kafka.types.reboot_broker_request
    import capo_kafka.types.reboot_broker_response
    import capo_kafka.types.reject_client_vpc_connection_request
    import capo_kafka.types.reject_client_vpc_connection_response
    import capo_kafka.types.replicator_summary
    import capo_kafka.types.s3_destination_configuration
    import capo_kafka.types.s3_destination_update
    import capo_kafka.types.serverless_request
    import capo_kafka.types.storage_mode
    import capo_kafka.types.tag_resource_request
    import capo_kafka.types.topic_info
    import capo_kafka.types.topic_partition_info
    import capo_kafka.types.topic_replication_update
    import capo_kafka.types.untag_resource_request
    import capo_kafka.types.update_broker_count_request
    import capo_kafka.types.update_broker_count_response
    import capo_kafka.types.update_broker_storage_request
    import capo_kafka.types.update_broker_storage_response
    import capo_kafka.types.update_broker_type_request
    import capo_kafka.types.update_broker_type_response
    import capo_kafka.types.update_channel_request
    import capo_kafka.types.update_channel_response
    import capo_kafka.types.update_cluster_configuration_request
    import capo_kafka.types.update_cluster_configuration_response
    import capo_kafka.types.update_cluster_kafka_version_request
    import capo_kafka.types.update_cluster_kafka_version_response
    import capo_kafka.types.update_configuration_request
    import capo_kafka.types.update_configuration_response
    import capo_kafka.types.update_connectivity_request
    import capo_kafka.types.update_connectivity_response
    import capo_kafka.types.update_monitoring_request
    import capo_kafka.types.update_monitoring_response
    import capo_kafka.types.update_rebalancing_request
    import capo_kafka.types.update_rebalancing_response
    import capo_kafka.types.update_replication_info_request
    import capo_kafka.types.update_replication_info_response
    import capo_kafka.types.update_security_request
    import capo_kafka.types.update_security_response
    import capo_kafka.types.update_storage_request
    import capo_kafka.types.update_storage_response
    import capo_kafka.types.update_topic_request
    import capo_kafka.types.update_topic_response
    import capo_kafka.types.vpc_connection
    import capo_kafka.types.zookeeper_access


class AsyncKafkaClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncKafkaClient:
    """A client for the ``Kafka`` service.

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
        self._config = AsyncKafkaClientConfig(
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
        self, config_overrides: Optional[AsyncKafkaClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncKafkaClientConfig = config_overrides or {}
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

    async def batch_associate_scram_secret(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        secret_arn_list: Optional[
            "capo_kafka.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "capo_kafka.types.batch_associate_scram_secret_response.BatchAssociateScramSecretResponse":
        """<p>Associates one or more Scram Secrets with an Amazon MSK cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster to be updated.</p>
            secret_arn_list: <p>List of AWS Secrets Manager secret ARNs.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.batch_associate_scram_secret_request.BatchAssociateScramSecretRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.batch_associate_scram_secret_response.BatchAssociateScramSecretResponse"
        ]:
            import capo_kafka._operations.kafka.batch_associate_scram_secret

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.batch_associate_scram_secret.async_batch_associate_scram_secret(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.batch_associate_scram_secret_request.BatchAssociateScramSecretRequest = {
            "cluster_arn": cluster_arn
        }
        if secret_arn_list is not None:
            input_["secret_arn_list"] = secret_arn_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_disassociate_scram_secret(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        secret_arn_list: Optional[
            "capo_kafka.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "capo_kafka.types.batch_disassociate_scram_secret_response.BatchDisassociateScramSecretResponse":
        """<p>Disassociates one or more Scram Secrets from an Amazon MSK cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster to be updated.</p>
            secret_arn_list: <p>List of AWS Secrets Manager secret ARNs.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.batch_disassociate_scram_secret_request.BatchDisassociateScramSecretRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.batch_disassociate_scram_secret_response.BatchDisassociateScramSecretResponse"
        ]:
            import capo_kafka._operations.kafka.batch_disassociate_scram_secret

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.batch_disassociate_scram_secret.async_batch_disassociate_scram_secret(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.batch_disassociate_scram_secret_request.BatchDisassociateScramSecretRequest = {
            "cluster_arn": cluster_arn
        }
        if secret_arn_list is not None:
            input_["secret_arn_list"] = secret_arn_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_channel(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        channel_name: Optional["capo_kafka.types.__string.__string"] = None,
        encryption_configuration: Optional[
            "capo_kafka.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        iceberg_destination_configuration: Optional[
            "capo_kafka.types.iceberg_destination_configuration.IcebergDestinationConfiguration"
        ] = None,
        s3_destination_configuration: Optional[
            "capo_kafka.types.s3_destination_configuration.S3DestinationConfiguration"
        ] = None,
        tags: Optional["capo_kafka.types.__map_of__string.__mapOf__string"] = None,
        topic_configuration_list: Optional[
            "capo_kafka.types.__list_of_topic_configuration.__listOfTopicConfiguration"
        ] = None,
        logging_info: Optional[
            "capo_kafka.types.channel_logging_info.ChannelLoggingInfo"
        ] = None,
    ) -> "capo_kafka.types.create_channel_response.CreateChannelResponse":
        """<p>Creates a Channel that streams records from an Amazon MSK Express cluster topic to Amazon S3 or Apache Iceberg.</p>

        Args:
            channel_name: <p>The name of the channel. Must be unique within the cluster.</p>
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            encryption_configuration: <p>The encryption configuration applied to the channel.</p>
            iceberg_destination_configuration: <p>The Apache Iceberg destination for the channel. Mutually exclusive with s3DestinationConfiguration.</p>
            s3_destination_configuration: <p>The Amazon S3 destination for the channel. Mutually exclusive with icebergDestinationConfiguration.</p>
            tags: <p>The tags attached to the channel.</p>
            topic_configuration_list: <p>The list of topic configurations for the channel. Currently exactly one topic must be specified.</p>
            logging_info: <p>The destinations to which the channel publishes operational logs.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.conflict_exception.ConflictException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.create_channel_request.CreateChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.create_channel_response.CreateChannelResponse"
        ]:
            import capo_kafka._operations.kafka.create_channel

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.create_channel.async_create_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.create_channel_request.CreateChannelRequest = {
            "cluster_arn": cluster_arn
        }
        if channel_name is not None:
            input_["channel_name"] = channel_name
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if iceberg_destination_configuration is not None:
            input_["iceberg_destination_configuration"] = (
                iceberg_destination_configuration
            )
        if s3_destination_configuration is not None:
            input_["s3_destination_configuration"] = s3_destination_configuration
        if tags is not None:
            input_["tags"] = tags
        if topic_configuration_list is not None:
            input_["topic_configuration_list"] = topic_configuration_list
        if logging_info is not None:
            input_["logging_info"] = logging_info

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cluster(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        broker_node_group_info: Optional[
            "capo_kafka.types.broker_node_group_info.BrokerNodeGroupInfo"
        ] = None,
        rebalancing: Optional["capo_kafka.types.rebalancing.Rebalancing"] = None,
        client_authentication: Optional[
            "capo_kafka.types.client_authentication.ClientAuthentication"
        ] = None,
        cluster_name: Optional[
            "capo_kafka.types.__string_min1_max64.__stringMin1Max64"
        ] = None,
        configuration_info: Optional[
            "capo_kafka.types.configuration_info.ConfigurationInfo"
        ] = None,
        encryption_info: Optional[
            "capo_kafka.types.encryption_info.EncryptionInfo"
        ] = None,
        enhanced_monitoring: Optional[
            "capo_kafka.types.enhanced_monitoring.EnhancedMonitoring"
        ] = None,
        open_monitoring: Optional[
            "capo_kafka.types.open_monitoring_info.OpenMonitoringInfo"
        ] = None,
        kafka_version: Optional[
            "capo_kafka.types.__string_min1_max128.__stringMin1Max128"
        ] = None,
        logging_info: Optional["capo_kafka.types.logging_info.LoggingInfo"] = None,
        number_of_broker_nodes: Optional[
            "capo_kafka.types.__integer_min1_max15.__integerMin1Max15"
        ] = None,
        tags: Optional["capo_kafka.types.__map_of__string.__mapOf__string"] = None,
        storage_mode: Optional["capo_kafka.types.storage_mode.StorageMode"] = None,
    ) -> "capo_kafka.types.create_cluster_response.CreateClusterResponse":
        """<p>Creates a new MSK cluster.</p>

        Args:
            broker_node_group_info: <p>Information about the broker nodes in the cluster.</p>
            rebalancing: <p>Specifies if intelligent rebalancing should be turned on for the new MSK Provisioned cluster with Express brokers. By default, intelligent rebalancing status is ACTIVE for all new clusters.</p>
            client_authentication: <p>Includes all client authentication related information.</p>
            cluster_name: <p>The name of the cluster.</p>
            configuration_info: <p>Represents the configuration that you want MSK to use for the brokers in a cluster.</p>
            encryption_info: <p>Includes all encryption-related information.</p>
            enhanced_monitoring: <p>Specifies the level of monitoring for the MSK cluster. The possible values are DEFAULT, PER_BROKER, PER_TOPIC_PER_BROKER, and PER_TOPIC_PER_PARTITION.</p>
            open_monitoring: <p>The settings for open monitoring.</p>
            kafka_version: <p>The version of Apache Kafka.</p>
            number_of_broker_nodes: <p>The number of broker nodes in the cluster.</p>
            tags: <p>Create tags when creating the cluster.</p>
            storage_mode: <p>This controls storage mode for supported storage tiers.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.conflict_exception.ConflictException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.create_cluster_request.CreateClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.create_cluster_response.CreateClusterResponse"
        ]:
            import capo_kafka._operations.kafka.create_cluster

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.create_cluster.async_create_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.create_cluster_request.CreateClusterRequest = {}
        if broker_node_group_info is not None:
            input_["broker_node_group_info"] = broker_node_group_info
        if rebalancing is not None:
            input_["rebalancing"] = rebalancing
        if client_authentication is not None:
            input_["client_authentication"] = client_authentication
        if cluster_name is not None:
            input_["cluster_name"] = cluster_name
        if configuration_info is not None:
            input_["configuration_info"] = configuration_info
        if encryption_info is not None:
            input_["encryption_info"] = encryption_info
        if enhanced_monitoring is not None:
            input_["enhanced_monitoring"] = enhanced_monitoring
        if open_monitoring is not None:
            input_["open_monitoring"] = open_monitoring
        if kafka_version is not None:
            input_["kafka_version"] = kafka_version
        if logging_info is not None:
            input_["logging_info"] = logging_info
        if number_of_broker_nodes is not None:
            input_["number_of_broker_nodes"] = number_of_broker_nodes
        if tags is not None:
            input_["tags"] = tags
        if storage_mode is not None:
            input_["storage_mode"] = storage_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cluster_v2(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        cluster_name: Optional[
            "capo_kafka.types.__string_min1_max64.__stringMin1Max64"
        ] = None,
        tags: Optional["capo_kafka.types.__map_of__string.__mapOf__string"] = None,
        provisioned: Optional[
            "capo_kafka.types.provisioned_request.ProvisionedRequest"
        ] = None,
        serverless: Optional[
            "capo_kafka.types.serverless_request.ServerlessRequest"
        ] = None,
    ) -> "capo_kafka.types.create_cluster_v2_response.CreateClusterV2Response":
        """<p>Creates a new MSK cluster.</p>

        Args:
            cluster_name: <p>The name of the cluster.</p>
            tags: <p>A map of tags that you want the cluster to have.</p>
            provisioned: <p>Information about the provisioned cluster.</p>
            serverless: <p>Information about the serverless cluster.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.conflict_exception.ConflictException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.create_cluster_v2_request.CreateClusterV2Request]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.create_cluster_v2_response.CreateClusterV2Response"
        ]:
            import capo_kafka._operations.kafka.create_cluster_v2

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.create_cluster_v2.async_create_cluster_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.create_cluster_v2_request.CreateClusterV2Request = {}
        if cluster_name is not None:
            input_["cluster_name"] = cluster_name
        if tags is not None:
            input_["tags"] = tags
        if provisioned is not None:
            input_["provisioned"] = provisioned
        if serverless is not None:
            input_["serverless"] = serverless

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_configuration(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        description: Optional["capo_kafka.types.__string.__string"] = None,
        kafka_versions: Optional[
            "capo_kafka.types.__list_of__string.__listOf__string"
        ] = None,
        name: Optional["capo_kafka.types.__string.__string"] = None,
        server_properties: Optional["capo_kafka.types.__blob.__blob"] = None,
    ) -> "capo_kafka.types.create_configuration_response.CreateConfigurationResponse":
        """<p>Creates a new MSK configuration.</p>

        Args:
            description: <p>The description of the configuration.</p>
            kafka_versions: <p>The versions of Apache Kafka with which you can use this MSK configuration.</p>
            name: <p>The name of the configuration.</p>
            server_properties: <p>Contents of the <filename>server.properties</filename> file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the AWS Management Console, the SDK, or the AWS CLI, the contents of <filename>server.properties</filename> can be in plaintext.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.conflict_exception.ConflictException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.create_configuration_request.CreateConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.create_configuration_response.CreateConfigurationResponse"
        ]:
            import capo_kafka._operations.kafka.create_configuration

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.create_configuration.async_create_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.create_configuration_request.CreateConfigurationRequest = {}
        if description is not None:
            input_["description"] = description
        if kafka_versions is not None:
            input_["kafka_versions"] = kafka_versions
        if name is not None:
            input_["name"] = name
        if server_properties is not None:
            input_["server_properties"] = server_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_replicator(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        description: Optional[
            "capo_kafka.types.__string_max1024.__stringMax1024"
        ] = None,
        kafka_clusters: Optional[
            "capo_kafka.types.__list_of_kafka_cluster.__listOfKafkaCluster"
        ] = None,
        replication_info_list: Optional[
            "capo_kafka.types.__list_of_replication_info.__listOfReplicationInfo"
        ] = None,
        replicator_name: Optional[
            "capo_kafka.types.__string_min1_max128_pattern09_a_za_z09_a_za_z0.__stringMin1Max128Pattern09AZaZ09AZaZ0"
        ] = None,
        service_execution_role_arn: Optional[
            "capo_kafka.types.__string.__string"
        ] = None,
        tags: Optional["capo_kafka.types.__map_of__string.__mapOf__string"] = None,
        log_delivery: Optional["capo_kafka.types.log_delivery.LogDelivery"] = None,
    ) -> "capo_kafka.types.create_replicator_response.CreateReplicatorResponse":
        """<p>Creates the replicator.</p>

        Args:
            description: <p>A summary description of the replicator.</p>
            kafka_clusters: <p>Kafka Clusters to use in setting up sources / targets for replication.</p>
            replication_info_list: <p>A list of replication configurations, where each configuration targets a given source cluster to target cluster replication flow.</p>
            replicator_name: <p>The name of the replicator. Alpha-numeric characters with '-' are allowed.</p>
            service_execution_role_arn: <p>The ARN of the IAM role used by the replicator to access resources in the customer's account (e.g source and target clusters)</p>
            tags: <p>List of tags to attach to created Replicator.</p>
            log_delivery: <p>Configuration for delivering replicator logs to customer destinations.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.conflict_exception.ConflictException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.create_replicator_request.CreateReplicatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.create_replicator_response.CreateReplicatorResponse"
        ]:
            import capo_kafka._operations.kafka.create_replicator

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.create_replicator.async_create_replicator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.create_replicator_request.CreateReplicatorRequest = {}
        if description is not None:
            input_["description"] = description
        if kafka_clusters is not None:
            input_["kafka_clusters"] = kafka_clusters
        if replication_info_list is not None:
            input_["replication_info_list"] = replication_info_list
        if replicator_name is not None:
            input_["replicator_name"] = replicator_name
        if service_execution_role_arn is not None:
            input_["service_execution_role_arn"] = service_execution_role_arn
        if tags is not None:
            input_["tags"] = tags
        if log_delivery is not None:
            input_["log_delivery"] = log_delivery

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_topic(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        topic_name: Optional["capo_kafka.types.__string.__string"] = None,
        partition_count: Optional[
            "capo_kafka.types.__integer_min1.__integerMin1"
        ] = None,
        replication_factor: Optional[
            "capo_kafka.types.__integer_min1.__integerMin1"
        ] = None,
        configs: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.create_topic_response.CreateTopicResponse":
        """<p>Creates a topic in the specified MSK cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            topic_name: <p>The name of the topic to create.</p>
            partition_count: <p>The number of partitions for the topic.</p>
            replication_factor: <p>The replication factor for the topic.</p>
            configs: <p>Topic configurations encoded as a Base64 string.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.cluster_connectivity_exception.ClusterConnectivityException: <p>Returns information about an error.</p>
            capo_kafka.errors.conflict_exception.ConflictException: <p>Returns information about an error.</p>
            capo_kafka.errors.controller_moved_exception.ControllerMovedException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.group_subscribed_to_topic_exception.GroupSubscribedToTopicException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.kafka_request_exception.KafkaRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.kafka_timeout_exception.KafkaTimeoutException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_controller_exception.NotControllerException: <p>Returns information about an error.</p>
            capo_kafka.errors.reassignment_in_progress_exception.ReassignmentInProgressException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.topic_exists_exception.TopicExistsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.unknown_topic_or_partition_exception.UnknownTopicOrPartitionException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.create_topic_request.CreateTopicRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.create_topic_response.CreateTopicResponse"
        ]:
            import capo_kafka._operations.kafka.create_topic

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.create_topic.async_create_topic(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.create_topic_request.CreateTopicRequest = {
            "cluster_arn": cluster_arn
        }
        if topic_name is not None:
            input_["topic_name"] = topic_name
        if partition_count is not None:
            input_["partition_count"] = partition_count
        if replication_factor is not None:
            input_["replication_factor"] = replication_factor
        if configs is not None:
            input_["configs"] = configs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_vpc_connection(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        target_cluster_arn: Optional["capo_kafka.types.__string.__string"] = None,
        authentication: Optional["capo_kafka.types.__string.__string"] = None,
        vpc_id: Optional["capo_kafka.types.__string.__string"] = None,
        client_subnets: Optional[
            "capo_kafka.types.__list_of__string.__listOf__string"
        ] = None,
        security_groups: Optional[
            "capo_kafka.types.__list_of__string.__listOf__string"
        ] = None,
        tags: Optional["capo_kafka.types.__map_of__string.__mapOf__string"] = None,
    ) -> "capo_kafka.types.create_vpc_connection_response.CreateVpcConnectionResponse":
        """<p>Creates a new MSK VPC connection.</p>

        Args:
            target_cluster_arn: <p>The cluster Amazon Resource Name (ARN) for the VPC connection.</p>
            authentication: <p>The authentication type of VPC connection.</p>
            vpc_id: <p>The VPC ID of VPC connection.</p>
            client_subnets: <p>The list of client subnets.</p>
            security_groups: <p>The list of security groups.</p>
            tags: <p>A map of tags for the VPC connection.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.create_vpc_connection_request.CreateVpcConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.create_vpc_connection_response.CreateVpcConnectionResponse"
        ]:
            import capo_kafka._operations.kafka.create_vpc_connection

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.create_vpc_connection.async_create_vpc_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.create_vpc_connection_request.CreateVpcConnectionRequest = {}
        if target_cluster_arn is not None:
            input_["target_cluster_arn"] = target_cluster_arn
        if authentication is not None:
            input_["authentication"] = authentication
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if client_subnets is not None:
            input_["client_subnets"] = client_subnets
        if security_groups is not None:
            input_["security_groups"] = security_groups
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_channel(
        self,
        channel_arn: "capo_kafka.types.__string.__string",
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.delete_channel_response.DeleteChannelResponse":
        """<p>Deletes the channel specified by channelArn from the cluster specified by clusterArn. The channel transitions through DELETING and is removed when the asynchronous delete completes.</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the channel.</p>
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.delete_channel_request.DeleteChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.delete_channel_response.DeleteChannelResponse"
        ]:
            import capo_kafka._operations.kafka.delete_channel

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.delete_channel.async_delete_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.delete_channel_request.DeleteChannelRequest = {
            "channel_arn": channel_arn,
            "cluster_arn": cluster_arn,
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
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        current_version: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.delete_cluster_response.DeleteClusterResponse":
        """<p>Deletes the MSK cluster specified by the Amazon Resource Name (ARN) in the request.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            current_version: <p>The current version of the MSK cluster.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import capo_kafka._operations.kafka.delete_cluster

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.delete_cluster.async_delete_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.delete_cluster_request.DeleteClusterRequest = {
            "cluster_arn": cluster_arn
        }
        if current_version is not None:
            input_["current_version"] = current_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cluster_policy(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.delete_cluster_policy_response.DeleteClusterPolicyResponse":
        """<p>Deletes the MSK cluster policy specified by the Amazon Resource Name (ARN) in the request.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.delete_cluster_policy_request.DeleteClusterPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.delete_cluster_policy_response.DeleteClusterPolicyResponse"
        ]:
            import capo_kafka._operations.kafka.delete_cluster_policy

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.delete_cluster_policy.async_delete_cluster_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.delete_cluster_policy_request.DeleteClusterPolicyRequest = {
            "cluster_arn": cluster_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configuration(
        self,
        arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.delete_configuration_response.DeleteConfigurationResponse":
        """<p>Deletes an MSK Configuration.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.delete_configuration_request.DeleteConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.delete_configuration_response.DeleteConfigurationResponse"
        ]:
            import capo_kafka._operations.kafka.delete_configuration

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.delete_configuration.async_delete_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.delete_configuration_request.DeleteConfigurationRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_replicator(
        self,
        replicator_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        current_version: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.delete_replicator_response.DeleteReplicatorResponse":
        """<p>Deletes a replicator.</p>

        Args:
            current_version: <p>The current version of the replicator.</p>
            replicator_arn: <p>The Amazon Resource Name (ARN) of the replicator to be deleted.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.delete_replicator_request.DeleteReplicatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.delete_replicator_response.DeleteReplicatorResponse"
        ]:
            import capo_kafka._operations.kafka.delete_replicator

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.delete_replicator.async_delete_replicator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.delete_replicator_request.DeleteReplicatorRequest = {
            "replicator_arn": replicator_arn
        }
        if current_version is not None:
            input_["current_version"] = current_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_topic(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        topic_name: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.delete_topic_response.DeleteTopicResponse":
        """<p>Deletes a topic in the specified MSK cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            topic_name: <p>The name of the topic to delete.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.cluster_connectivity_exception.ClusterConnectivityException: <p>Returns information about an error.</p>
            capo_kafka.errors.controller_moved_exception.ControllerMovedException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.group_subscribed_to_topic_exception.GroupSubscribedToTopicException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.kafka_request_exception.KafkaRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.kafka_timeout_exception.KafkaTimeoutException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_controller_exception.NotControllerException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.reassignment_in_progress_exception.ReassignmentInProgressException: <p>Returns information about an error.</p>
            capo_kafka.errors.unknown_topic_or_partition_exception.UnknownTopicOrPartitionException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.delete_topic_request.DeleteTopicRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.delete_topic_response.DeleteTopicResponse"
        ]:
            import capo_kafka._operations.kafka.delete_topic

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.delete_topic.async_delete_topic(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.delete_topic_request.DeleteTopicRequest = {
            "cluster_arn": cluster_arn,
            "topic_name": topic_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_vpc_connection(
        self,
        arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.delete_vpc_connection_response.DeleteVpcConnectionResponse":
        """<p>Deletes a MSK VPC connection.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) that uniquely identifies an MSK VPC connection.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.delete_vpc_connection_request.DeleteVpcConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.delete_vpc_connection_response.DeleteVpcConnectionResponse"
        ]:
            import capo_kafka._operations.kafka.delete_vpc_connection

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.delete_vpc_connection.async_delete_vpc_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.delete_vpc_connection_request.DeleteVpcConnectionRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_channel(
        self,
        channel_arn: "capo_kafka.types.__string.__string",
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.describe_channel_response.DescribeChannelResponse":
        """<p>Returns the current configuration and state of a channel.</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the channel.</p>
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.describe_channel_request.DescribeChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.describe_channel_response.DescribeChannelResponse"
        ]:
            import capo_kafka._operations.kafka.describe_channel

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.describe_channel.async_describe_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.describe_channel_request.DescribeChannelRequest = {
            "channel_arn": channel_arn,
            "cluster_arn": cluster_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_cluster(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.describe_cluster_response.DescribeClusterResponse":
        """<p>Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.describe_cluster_request.DescribeClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.describe_cluster_response.DescribeClusterResponse"
        ]:
            import capo_kafka._operations.kafka.describe_cluster

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.describe_cluster.async_describe_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.describe_cluster_request.DescribeClusterRequest = {
            "cluster_arn": cluster_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_cluster_operation(
        self,
        cluster_operation_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.describe_cluster_operation_response.DescribeClusterOperationResponse":
        """<p>Returns a description of the cluster operation specified by the ARN.</p>

        Args:
            cluster_operation_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the MSK cluster operation.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.describe_cluster_operation_request.DescribeClusterOperationRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.describe_cluster_operation_response.DescribeClusterOperationResponse"
        ]:
            import capo_kafka._operations.kafka.describe_cluster_operation

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.describe_cluster_operation.async_describe_cluster_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.describe_cluster_operation_request.DescribeClusterOperationRequest = {
            "cluster_operation_arn": cluster_operation_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_cluster_operation_v2(
        self,
        cluster_operation_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.describe_cluster_operation_v2_response.DescribeClusterOperationV2Response":
        """<p>Returns a description of the cluster operation specified by the ARN.</p>

        Args:
            cluster_operation_arn: ARN of the cluster operation to describe.

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.describe_cluster_operation_v2_request.DescribeClusterOperationV2Request]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.describe_cluster_operation_v2_response.DescribeClusterOperationV2Response"
        ]:
            import capo_kafka._operations.kafka.describe_cluster_operation_v2

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.describe_cluster_operation_v2.async_describe_cluster_operation_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.describe_cluster_operation_v2_request.DescribeClusterOperationV2Request = {
            "cluster_operation_arn": cluster_operation_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_cluster_v2(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.describe_cluster_v2_response.DescribeClusterV2Response":
        """<p>Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.describe_cluster_v2_request.DescribeClusterV2Request]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.describe_cluster_v2_response.DescribeClusterV2Response"
        ]:
            import capo_kafka._operations.kafka.describe_cluster_v2

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.describe_cluster_v2.async_describe_cluster_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.describe_cluster_v2_request.DescribeClusterV2Request = {
            "cluster_arn": cluster_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_configuration(
        self,
        arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> (
        "capo_kafka.types.describe_configuration_response.DescribeConfigurationResponse"
    ):
        """<p>Returns a description of this MSK configuration.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.describe_configuration_request.DescribeConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.describe_configuration_response.DescribeConfigurationResponse"
        ]:
            import capo_kafka._operations.kafka.describe_configuration

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.describe_configuration.async_describe_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.describe_configuration_request.DescribeConfigurationRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_configuration_revision(
        self,
        arn: "capo_kafka.types.__string.__string",
        revision: "capo_kafka.types.__long.__long",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.describe_configuration_revision_response.DescribeConfigurationRevisionResponse":
        """<p>Returns a description of this revision of the configuration.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.</p>
            revision: <p>A string that uniquely identifies a revision of an MSK configuration.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.describe_configuration_revision_request.DescribeConfigurationRevisionRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.describe_configuration_revision_response.DescribeConfigurationRevisionResponse"
        ]:
            import capo_kafka._operations.kafka.describe_configuration_revision

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.describe_configuration_revision.async_describe_configuration_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.describe_configuration_revision_request.DescribeConfigurationRevisionRequest = {
            "arn": arn,
            "revision": revision,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_replicator(
        self,
        replicator_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.describe_replicator_response.DescribeReplicatorResponse":
        """<p>Describes a replicator.</p>

        Args:
            replicator_arn: <p>The Amazon Resource Name (ARN) of the replicator to be described.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.describe_replicator_request.DescribeReplicatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.describe_replicator_response.DescribeReplicatorResponse"
        ]:
            import capo_kafka._operations.kafka.describe_replicator

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.describe_replicator.async_describe_replicator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.describe_replicator_request.DescribeReplicatorRequest = {
            "replicator_arn": replicator_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_topic(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        topic_name: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.describe_topic_response.DescribeTopicResponse":
        """<p>Returns topic details of this topic on a MSK cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            topic_name: <p>The Kafka topic name that uniquely identifies the topic.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.describe_topic_request.DescribeTopicRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.describe_topic_response.DescribeTopicResponse"
        ]:
            import capo_kafka._operations.kafka.describe_topic

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.describe_topic.async_describe_topic(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.describe_topic_request.DescribeTopicRequest = {
            "cluster_arn": cluster_arn,
            "topic_name": topic_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_topic_partitions(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        topic_name: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.describe_topic_partitions_response.DescribeTopicPartitionsResponse":
        """<p>Returns partition details of this topic on a MSK cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            topic_name: <p>The Kafka topic name that uniquely identifies the topic.</p>
            max_results: <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>
            next_token: <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.describe_topic_partitions_request.DescribeTopicPartitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.describe_topic_partitions_response.DescribeTopicPartitionsResponse"
        ]:
            import capo_kafka._operations.kafka.describe_topic_partitions

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.describe_topic_partitions.async_describe_topic_partitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.describe_topic_partitions_request.DescribeTopicPartitionsRequest = {
            "cluster_arn": cluster_arn,
            "topic_name": topic_name,
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

    async def iter_describe_topic_partitions(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        topic_name: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafka.types.topic_partition_info.TopicPartitionInfo]":
        _token = next_token
        while True:
            _response = await self.describe_topic_partitions(
                cluster_arn,
                topic_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("partitions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_vpc_connection(
        self,
        arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.describe_vpc_connection_response.DescribeVpcConnectionResponse":
        """<p>Returns a description of this MSK VPC connection.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) that uniquely identifies a MSK VPC connection.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.describe_vpc_connection_request.DescribeVpcConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.describe_vpc_connection_response.DescribeVpcConnectionResponse"
        ]:
            import capo_kafka._operations.kafka.describe_vpc_connection

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.describe_vpc_connection.async_describe_vpc_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.describe_vpc_connection_request.DescribeVpcConnectionRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bootstrap_brokers(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.get_bootstrap_brokers_response.GetBootstrapBrokersResponse":
        """<p>A list of brokers that a client application can use to bootstrap. This list doesn't necessarily include all of the brokers in the cluster. The following Python 3.6 example shows how you can use the Amazon Resource Name (ARN) of a cluster to get its bootstrap brokers. If you don't know the ARN of your cluster, you can use the <code>ListClusters</code> operation to get the ARNs of all the clusters in this account and Region.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.conflict_exception.ConflictException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.get_bootstrap_brokers_request.GetBootstrapBrokersRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.get_bootstrap_brokers_response.GetBootstrapBrokersResponse"
        ]:
            import capo_kafka._operations.kafka.get_bootstrap_brokers

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.get_bootstrap_brokers.async_get_bootstrap_brokers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.get_bootstrap_brokers_request.GetBootstrapBrokersRequest = {
            "cluster_arn": cluster_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_cluster_policy(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.get_cluster_policy_response.GetClusterPolicyResponse":
        """<p>Get the MSK cluster policy specified by the Amazon Resource Name (ARN) in the request.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.get_cluster_policy_request.GetClusterPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.get_cluster_policy_response.GetClusterPolicyResponse"
        ]:
            import capo_kafka._operations.kafka.get_cluster_policy

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.get_cluster_policy.async_get_cluster_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.get_cluster_policy_request.GetClusterPolicyRequest = {
            "cluster_arn": cluster_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_compatible_kafka_versions(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        cluster_arn: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.get_compatible_kafka_versions_response.GetCompatibleKafkaVersionsResponse":
        """<p>Gets the Apache Kafka versions to which you can update the MSK cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster check.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.get_compatible_kafka_versions_request.GetCompatibleKafkaVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.get_compatible_kafka_versions_response.GetCompatibleKafkaVersionsResponse"
        ]:
            import capo_kafka._operations.kafka.get_compatible_kafka_versions

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.get_compatible_kafka_versions.async_get_compatible_kafka_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.get_compatible_kafka_versions_request.GetCompatibleKafkaVersionsRequest = {}
        if cluster_arn is not None:
            input_["cluster_arn"] = cluster_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_channels(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
        topic_name_filter: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.list_channels_response.ListChannelsResponse":
        """<p>Returns the list of channels in a cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            max_results: <p>Maximum number of channels to return in a single response.</p>
            next_token: <p>If the response of ListChannels is truncated, it returns a nextToken in the response. This nextToken should be sent in the subsequent request to ListChannels.</p>
            topic_name_filter: <p>Filters results to channels whose topic name matches the specified value.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_channels_request.ListChannelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_channels_response.ListChannelsResponse"
        ]:
            import capo_kafka._operations.kafka.list_channels

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_channels.async_list_channels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_channels_request.ListChannelsRequest = {
            "cluster_arn": cluster_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if topic_name_filter is not None:
            input_["topic_name_filter"] = topic_name_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_client_vpc_connections(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.list_client_vpc_connections_response.ListClientVpcConnectionsResponse":
        """<p>Returns a list of all the VPC connections in this Region.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster.</p>
            max_results: <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>
            next_token: <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_client_vpc_connections_request.ListClientVpcConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_client_vpc_connections_response.ListClientVpcConnectionsResponse"
        ]:
            import capo_kafka._operations.kafka.list_client_vpc_connections

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_client_vpc_connections.async_list_client_vpc_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_client_vpc_connections_request.ListClientVpcConnectionsRequest = {
            "cluster_arn": cluster_arn
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

    async def iter_list_client_vpc_connections(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafka.types.client_vpc_connection.ClientVpcConnection]":
        _token = next_token
        while True:
            _response = await self.list_client_vpc_connections(
                cluster_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("client_vpc_connections",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_cluster_operations(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.list_cluster_operations_response.ListClusterOperationsResponse":
        """<p>Returns a list of all the operations that have been performed on the specified MSK cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            max_results: <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>
            next_token: <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_cluster_operations_request.ListClusterOperationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_cluster_operations_response.ListClusterOperationsResponse"
        ]:
            import capo_kafka._operations.kafka.list_cluster_operations

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_cluster_operations.async_list_cluster_operations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_cluster_operations_request.ListClusterOperationsRequest = {
            "cluster_arn": cluster_arn
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

    async def iter_list_cluster_operations(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafka.types.cluster_operation_info.ClusterOperationInfo]":
        _token = next_token
        while True:
            _response = await self.list_cluster_operations(
                cluster_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("cluster_operation_info_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_cluster_operations_v2(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.list_cluster_operations_v2_response.ListClusterOperationsV2Response":
        """<p>Returns a list of all the operations that have been performed on the specified MSK cluster.</p>

        Args:
            cluster_arn: The arn of the cluster whose operations are being requested.
            max_results: The maxResults of the query.
            next_token: The nextToken of the query.

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_cluster_operations_v2_request.ListClusterOperationsV2Request]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_cluster_operations_v2_response.ListClusterOperationsV2Response"
        ]:
            import capo_kafka._operations.kafka.list_cluster_operations_v2

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_cluster_operations_v2.async_list_cluster_operations_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_cluster_operations_v2_request.ListClusterOperationsV2Request = {
            "cluster_arn": cluster_arn
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

    async def iter_list_cluster_operations_v2(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafka.types.cluster_operation_v2_summary.ClusterOperationV2Summary]":
        _token = next_token
        while True:
            _response = await self.list_cluster_operations_v2(
                cluster_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("cluster_operation_info_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_clusters(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        cluster_name_filter: Optional["capo_kafka.types.__string.__string"] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.list_clusters_response.ListClustersResponse":
        """<p>Returns a list of all the MSK clusters in the current Region.</p>

        Args:
            cluster_name_filter: <p>Specify a prefix of the name of the clusters that you want to list. The service lists all the clusters whose names start with this prefix.</p>
            max_results: <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>
            next_token: <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_clusters_request.ListClustersRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_clusters_response.ListClustersResponse"
        ]:
            import capo_kafka._operations.kafka.list_clusters

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_clusters.async_list_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_clusters_request.ListClustersRequest = {}
        if cluster_name_filter is not None:
            input_["cluster_name_filter"] = cluster_name_filter
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

    async def iter_list_clusters(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        cluster_name_filter: Optional["capo_kafka.types.__string.__string"] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafka.types.cluster_info.ClusterInfo]":
        _token = next_token
        while True:
            _response = await self.list_clusters(
                config_overrides=config_overrides,
                cluster_name_filter=cluster_name_filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("cluster_info_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_clusters_v2(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        cluster_name_filter: Optional["capo_kafka.types.__string.__string"] = None,
        cluster_type_filter: Optional["capo_kafka.types.__string.__string"] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.list_clusters_v2_response.ListClustersV2Response":
        """<p>Returns a list of all the MSK clusters in the current Region.</p>

        Args:
            cluster_name_filter: <p>Specify a prefix of the names of the clusters that you want to list. The service lists all the clusters whose names start with this prefix.</p>
            cluster_type_filter: <p>Specify either PROVISIONED or SERVERLESS.</p>
            max_results: <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>
            next_token: <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_clusters_v2_request.ListClustersV2Request]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_clusters_v2_response.ListClustersV2Response"
        ]:
            import capo_kafka._operations.kafka.list_clusters_v2

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_clusters_v2.async_list_clusters_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_clusters_v2_request.ListClustersV2Request = {}
        if cluster_name_filter is not None:
            input_["cluster_name_filter"] = cluster_name_filter
        if cluster_type_filter is not None:
            input_["cluster_type_filter"] = cluster_type_filter
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

    async def iter_list_clusters_v2(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        cluster_name_filter: Optional["capo_kafka.types.__string.__string"] = None,
        cluster_type_filter: Optional["capo_kafka.types.__string.__string"] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafka.types.cluster.Cluster]":
        _token = next_token
        while True:
            _response = await self.list_clusters_v2(
                config_overrides=config_overrides,
                cluster_name_filter=cluster_name_filter,
                cluster_type_filter=cluster_type_filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("cluster_info_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_configuration_revisions(
        self,
        arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.list_configuration_revisions_response.ListConfigurationRevisionsResponse":
        """<p>Returns a list of all the MSK configurations in this Region.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.</p>
            max_results: <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>
            next_token: <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_configuration_revisions_request.ListConfigurationRevisionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_configuration_revisions_response.ListConfigurationRevisionsResponse"
        ]:
            import capo_kafka._operations.kafka.list_configuration_revisions

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_configuration_revisions.async_list_configuration_revisions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_configuration_revisions_request.ListConfigurationRevisionsRequest = {
            "arn": arn
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

    async def iter_list_configuration_revisions(
        self,
        arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafka.types.configuration_revision.ConfigurationRevision]":
        _token = next_token
        while True:
            _response = await self.list_configuration_revisions(
                arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("revisions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_configurations(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.list_configurations_response.ListConfigurationsResponse":
        """<p>Returns a list of all the MSK configurations in this Region.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>
            next_token: <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_configurations_request.ListConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_configurations_response.ListConfigurationsResponse"
        ]:
            import capo_kafka._operations.kafka.list_configurations

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_configurations.async_list_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_configurations_request.ListConfigurationsRequest = {}
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

    async def iter_list_configurations(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafka.types.configuration.Configuration]":
        _token = next_token
        while True:
            _response = await self.list_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_kafka_versions(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.list_kafka_versions_response.ListKafkaVersionsResponse":
        """<p>Returns a list of Apache Kafka versions.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>
            next_token: <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_kafka_versions_request.ListKafkaVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_kafka_versions_response.ListKafkaVersionsResponse"
        ]:
            import capo_kafka._operations.kafka.list_kafka_versions

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_kafka_versions.async_list_kafka_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_kafka_versions_request.ListKafkaVersionsRequest = {}
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

    async def iter_list_kafka_versions(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafka.types.kafka_version.KafkaVersion]":
        _token = next_token
        while True:
            _response = await self.list_kafka_versions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("kafka_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_nodes(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.list_nodes_response.ListNodesResponse":
        """<p>Returns a list of the broker nodes in the cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            max_results: <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>
            next_token: <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_nodes_request.ListNodesRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_nodes_response.ListNodesResponse"
        ]:
            import capo_kafka._operations.kafka.list_nodes

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_nodes.async_list_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_nodes_request.ListNodesRequest = {
            "cluster_arn": cluster_arn
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

    async def iter_list_nodes(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafka.types.node_info.NodeInfo]":
        _token = next_token
        while True:
            _response = await self.list_nodes(
                cluster_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("node_info_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_replicators(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
        replicator_name_filter: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.list_replicators_response.ListReplicatorsResponse":
        """<p>Lists the replicators.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>
            next_token: <p>If the response of ListReplicators is truncated, it returns a NextToken in the response. This NextToken should be sent in the subsequent request to ListReplicators.</p>
            replicator_name_filter: <p>Returns replicators starting with given name.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_replicators_request.ListReplicatorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_replicators_response.ListReplicatorsResponse"
        ]:
            import capo_kafka._operations.kafka.list_replicators

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_replicators.async_list_replicators(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_replicators_request.ListReplicatorsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if replicator_name_filter is not None:
            input_["replicator_name_filter"] = replicator_name_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_replicators(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
        replicator_name_filter: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafka.types.replicator_summary.ReplicatorSummary]":
        _token = next_token
        while True:
            _response = await self.list_replicators(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                replicator_name_filter=replicator_name_filter,
            )
            _page = _resolve_path(_response, ("replicators",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_scram_secrets(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.list_scram_secrets_response.ListScramSecretsResponse":
        """<p>Returns a list of the Scram Secrets associated with an Amazon MSK cluster.</p>

        Args:
            cluster_arn: <p>The arn of the cluster.</p>
            max_results: <p>The maxResults of the query.</p>
            next_token: <p>The nextToken of the query.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_scram_secrets_request.ListScramSecretsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_scram_secrets_response.ListScramSecretsResponse"
        ]:
            import capo_kafka._operations.kafka.list_scram_secrets

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_scram_secrets.async_list_scram_secrets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_scram_secrets_request.ListScramSecretsRequest = {
            "cluster_arn": cluster_arn
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

    async def iter_list_scram_secrets(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafka.types.__string.__string]":
        _token = next_token
        while True:
            _response = await self.list_scram_secrets(
                cluster_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("secret_arn_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
    ) -> "capo_kafka.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of the tags associated with the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the tags.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_kafka._operations.kafka.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_topics(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
        topic_name_filter: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.list_topics_response.ListTopicsResponse":
        """<p>List topics in a MSK cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            max_results: <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>
            next_token: <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>
            topic_name_filter: <p>Returns topics starting with given name.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_topics_request.ListTopicsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_topics_response.ListTopicsResponse"
        ]:
            import capo_kafka._operations.kafka.list_topics

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_topics.async_list_topics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_topics_request.ListTopicsRequest = {
            "cluster_arn": cluster_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if topic_name_filter is not None:
            input_["topic_name_filter"] = topic_name_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_topics(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
        topic_name_filter: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafka.types.topic_info.TopicInfo]":
        _token = next_token
        while True:
            _response = await self.list_topics(
                cluster_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                topic_name_filter=topic_name_filter,
            )
            _page = _resolve_path(_response, ("topics",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_vpc_connections(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.list_vpc_connections_response.ListVpcConnectionsResponse":
        """<p>Returns a list of all the VPC connections in this Region.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>
            next_token: <p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.list_vpc_connections_request.ListVpcConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.list_vpc_connections_response.ListVpcConnectionsResponse"
        ]:
            import capo_kafka._operations.kafka.list_vpc_connections

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.list_vpc_connections.async_list_vpc_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.list_vpc_connections_request.ListVpcConnectionsRequest = {}
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

    async def iter_list_vpc_connections(
        self,
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        max_results: Optional["capo_kafka.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafka.types.vpc_connection.VpcConnection]":
        _token = next_token
        while True:
            _response = await self.list_vpc_connections(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("vpc_connections",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_cluster_policy(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        current_version: Optional["capo_kafka.types.__string.__string"] = None,
        policy: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.put_cluster_policy_response.PutClusterPolicyResponse":
        """<p>Creates or updates the MSK cluster policy specified by the cluster Amazon Resource Name (ARN) in the request.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster.</p>
            current_version: <p>The policy version.</p>
            policy: <p>The policy.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.put_cluster_policy_request.PutClusterPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.put_cluster_policy_response.PutClusterPolicyResponse"
        ]:
            import capo_kafka._operations.kafka.put_cluster_policy

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.put_cluster_policy.async_put_cluster_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.put_cluster_policy_request.PutClusterPolicyRequest = {
            "cluster_arn": cluster_arn
        }
        if current_version is not None:
            input_["current_version"] = current_version
        if policy is not None:
            input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reboot_broker(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        broker_ids: Optional[
            "capo_kafka.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "capo_kafka.types.reboot_broker_response.RebootBrokerResponse":
        """Reboots brokers.

        Args:
            broker_ids: <p>The list of broker IDs to be rebooted. The reboot-broker operation supports rebooting one broker at a time.</p>
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster to be updated.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.reboot_broker_request.RebootBrokerRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.reboot_broker_response.RebootBrokerResponse"
        ]:
            import capo_kafka._operations.kafka.reboot_broker

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.reboot_broker.async_reboot_broker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.reboot_broker_request.RebootBrokerRequest = {
            "cluster_arn": cluster_arn
        }
        if broker_ids is not None:
            input_["broker_ids"] = broker_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_client_vpc_connection(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        vpc_connection_arn: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.reject_client_vpc_connection_response.RejectClientVpcConnectionResponse":
        """<p>Returns empty response.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster.</p>
            vpc_connection_arn: <p>The VPC connection ARN.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.reject_client_vpc_connection_request.RejectClientVpcConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.reject_client_vpc_connection_response.RejectClientVpcConnectionResponse"
        ]:
            import capo_kafka._operations.kafka.reject_client_vpc_connection

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.reject_client_vpc_connection.async_reject_client_vpc_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.reject_client_vpc_connection_request.RejectClientVpcConnectionRequest = {
            "cluster_arn": cluster_arn
        }
        if vpc_connection_arn is not None:
            input_["vpc_connection_arn"] = vpc_connection_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        tags: Optional["capo_kafka.types.__map_of__string.__mapOf__string"] = None,
    ) -> None:
        """<p>Adds tags to the specified MSK resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the tags.</p>
            tags: <p>The key-value pair for the resource tag.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_kafka._operations.kafka.tag_resource

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn
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

    async def untag_resource(
        self,
        resource_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        tag_keys: Optional[
            "capo_kafka.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> None:
        """<p>Removes the tags associated with the keys that are provided in the query.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the tags.</p>
            tag_keys: <p>Tag keys must be unique for a given cluster. In addition, the following restrictions apply:</p> <ul> <li> <p>Each tag key must be unique. If you add a tag with a key that's already in use, your new tag overwrites the existing key-value pair. </p> </li> <li> <p>You can't start a tag key with aws: because this prefix is reserved for use by AWS. AWS creates tags that begin with this prefix on your behalf, but you can't edit or delete them.</p> </li> <li> <p>Tag keys must be between 1 and 128 Unicode characters in length.</p> </li> <li> <p>Tag keys must consist of the following characters: Unicode letters, digits, white space, and the following special characters: _ . / = + - @.</p> </li> </ul>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_kafka._operations.kafka.untag_resource

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_broker_count(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        current_version: Optional["capo_kafka.types.__string.__string"] = None,
        target_number_of_broker_nodes: Optional[
            "capo_kafka.types.__integer_min1_max15.__integerMin1Max15"
        ] = None,
    ) -> "capo_kafka.types.update_broker_count_response.UpdateBrokerCountResponse":
        """<p>Updates the number of broker nodes in the cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            current_version: <p>The version of cluster to update from. A successful operation will then generate a new version.</p>
            target_number_of_broker_nodes: <p>The number of broker nodes that you want the cluster to have after this operation completes successfully.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.update_broker_count_request.UpdateBrokerCountRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.update_broker_count_response.UpdateBrokerCountResponse"
        ]:
            import capo_kafka._operations.kafka.update_broker_count

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.update_broker_count.async_update_broker_count(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.update_broker_count_request.UpdateBrokerCountRequest = {
            "cluster_arn": cluster_arn
        }
        if current_version is not None:
            input_["current_version"] = current_version
        if target_number_of_broker_nodes is not None:
            input_["target_number_of_broker_nodes"] = target_number_of_broker_nodes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_broker_storage(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        current_version: Optional["capo_kafka.types.__string.__string"] = None,
        target_broker_ebs_volume_info: Optional[
            "capo_kafka.types.__list_of_broker_ebs_volume_info.__listOfBrokerEBSVolumeInfo"
        ] = None,
    ) -> "capo_kafka.types.update_broker_storage_response.UpdateBrokerStorageResponse":
        """<p>Updates the EBS storage associated with MSK brokers.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            current_version: <p>The version of cluster to update from. A successful operation will then generate a new version.</p>
            target_broker_ebs_volume_info: <p>Describes the target volume size and the ID of the broker to apply the update to.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.update_broker_storage_request.UpdateBrokerStorageRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.update_broker_storage_response.UpdateBrokerStorageResponse"
        ]:
            import capo_kafka._operations.kafka.update_broker_storage

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.update_broker_storage.async_update_broker_storage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.update_broker_storage_request.UpdateBrokerStorageRequest = {
            "cluster_arn": cluster_arn
        }
        if current_version is not None:
            input_["current_version"] = current_version
        if target_broker_ebs_volume_info is not None:
            input_["target_broker_ebs_volume_info"] = target_broker_ebs_volume_info

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_broker_type(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        current_version: Optional["capo_kafka.types.__string.__string"] = None,
        target_instance_type: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.update_broker_type_response.UpdateBrokerTypeResponse":
        """<p>Updates EC2 instance type.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            current_version: <p>The cluster version that you want to change. After this operation completes successfully, the cluster will have a new version.</p>
            target_instance_type: <p>The Amazon MSK broker type that you want all of the brokers in this cluster to be.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.update_broker_type_request.UpdateBrokerTypeRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.update_broker_type_response.UpdateBrokerTypeResponse"
        ]:
            import capo_kafka._operations.kafka.update_broker_type

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.update_broker_type.async_update_broker_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.update_broker_type_request.UpdateBrokerTypeRequest = {
            "cluster_arn": cluster_arn
        }
        if current_version is not None:
            input_["current_version"] = current_version
        if target_instance_type is not None:
            input_["target_instance_type"] = target_instance_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_channel(
        self,
        channel_arn: "capo_kafka.types.__string.__string",
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        iceberg_destination_update: Optional[
            "capo_kafka.types.iceberg_destination_update.IcebergDestinationUpdate"
        ] = None,
        s3_destination_update: Optional[
            "capo_kafka.types.s3_destination_update.S3DestinationUpdate"
        ] = None,
    ) -> "capo_kafka.types.update_channel_response.UpdateChannelResponse":
        """<p>Updates the destination configuration of an existing channel. Exactly one of icebergDestinationUpdate or s3DestinationUpdate must be supplied.</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the channel.</p>
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            iceberg_destination_update: <p>Updates fields on an Apache Iceberg destination. Use only when the channel was created with an Iceberg destination.</p>
            s3_destination_update: <p>Updates fields on an Amazon S3 destination. Use only when the channel was created with an Amazon S3 destination.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.update_channel_request.UpdateChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.update_channel_response.UpdateChannelResponse"
        ]:
            import capo_kafka._operations.kafka.update_channel

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.update_channel.async_update_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.update_channel_request.UpdateChannelRequest = {
            "channel_arn": channel_arn,
            "cluster_arn": cluster_arn,
        }
        if iceberg_destination_update is not None:
            input_["iceberg_destination_update"] = iceberg_destination_update
        if s3_destination_update is not None:
            input_["s3_destination_update"] = s3_destination_update

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_cluster_configuration(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        configuration_info: Optional[
            "capo_kafka.types.configuration_info.ConfigurationInfo"
        ] = None,
        current_version: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.update_cluster_configuration_response.UpdateClusterConfigurationResponse":
        """<p>Updates the cluster with the configuration that is specified in the request body.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            configuration_info: <p>Represents the configuration that you want MSK to use for the brokers in a cluster.</p>
            current_version: <p>The version of the cluster that needs to be updated.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.update_cluster_configuration_request.UpdateClusterConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.update_cluster_configuration_response.UpdateClusterConfigurationResponse"
        ]:
            import capo_kafka._operations.kafka.update_cluster_configuration

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.update_cluster_configuration.async_update_cluster_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.update_cluster_configuration_request.UpdateClusterConfigurationRequest = {
            "cluster_arn": cluster_arn
        }
        if configuration_info is not None:
            input_["configuration_info"] = configuration_info
        if current_version is not None:
            input_["current_version"] = current_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_cluster_kafka_version(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        configuration_info: Optional[
            "capo_kafka.types.configuration_info.ConfigurationInfo"
        ] = None,
        current_version: Optional["capo_kafka.types.__string.__string"] = None,
        target_kafka_version: Optional["capo_kafka.types.__string.__string"] = None,
    ) -> "capo_kafka.types.update_cluster_kafka_version_response.UpdateClusterKafkaVersionResponse":
        """<p>Updates the Apache Kafka version for the cluster.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster to be updated.</p>
            configuration_info: <p>The custom configuration that should be applied on the new version of cluster.</p>
            current_version: <p>Current cluster version.</p>
            target_kafka_version: <p>Target Kafka version.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.update_cluster_kafka_version_request.UpdateClusterKafkaVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.update_cluster_kafka_version_response.UpdateClusterKafkaVersionResponse"
        ]:
            import capo_kafka._operations.kafka.update_cluster_kafka_version

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.update_cluster_kafka_version.async_update_cluster_kafka_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.update_cluster_kafka_version_request.UpdateClusterKafkaVersionRequest = {
            "cluster_arn": cluster_arn
        }
        if configuration_info is not None:
            input_["configuration_info"] = configuration_info
        if current_version is not None:
            input_["current_version"] = current_version
        if target_kafka_version is not None:
            input_["target_kafka_version"] = target_kafka_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configuration(
        self,
        arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        description: Optional["capo_kafka.types.__string.__string"] = None,
        server_properties: Optional["capo_kafka.types.__blob.__blob"] = None,
    ) -> "capo_kafka.types.update_configuration_response.UpdateConfigurationResponse":
        """<p>Updates an MSK configuration.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the configuration.</p>
            description: <p>The description of the configuration revision.</p>
            server_properties: <p>Contents of the <filename>server.properties</filename> file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the AWS Management Console, the SDK, or the AWS CLI, the contents of <filename>server.properties</filename> can be in plaintext.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.update_configuration_request.UpdateConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.update_configuration_response.UpdateConfigurationResponse"
        ]:
            import capo_kafka._operations.kafka.update_configuration

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.update_configuration.async_update_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.update_configuration_request.UpdateConfigurationRequest = {
            "arn": arn
        }
        if description is not None:
            input_["description"] = description
        if server_properties is not None:
            input_["server_properties"] = server_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connectivity(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        connectivity_info: Optional[
            "capo_kafka.types.connectivity_info.ConnectivityInfo"
        ] = None,
        current_version: Optional["capo_kafka.types.__string.__string"] = None,
        zookeeper_access: Optional[
            "capo_kafka.types.zookeeper_access.ZookeeperAccess"
        ] = None,
    ) -> "capo_kafka.types.update_connectivity_response.UpdateConnectivityResponse":
        """<p>Updates the cluster's connectivity configuration.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the configuration.</p>
            connectivity_info: <p>Information about the broker access configuration.</p>
            current_version: <p>The version of the MSK cluster to update. Cluster versions aren't simple numbers. You can describe an MSK cluster to find its version. When this update operation is successful, it generates a new cluster version.</p>
            zookeeper_access: <p>Access control settings for zookeeper</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.update_connectivity_request.UpdateConnectivityRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.update_connectivity_response.UpdateConnectivityResponse"
        ]:
            import capo_kafka._operations.kafka.update_connectivity

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.update_connectivity.async_update_connectivity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.update_connectivity_request.UpdateConnectivityRequest = {
            "cluster_arn": cluster_arn
        }
        if connectivity_info is not None:
            input_["connectivity_info"] = connectivity_info
        if current_version is not None:
            input_["current_version"] = current_version
        if zookeeper_access is not None:
            input_["zookeeper_access"] = zookeeper_access

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_monitoring(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        current_version: Optional["capo_kafka.types.__string.__string"] = None,
        enhanced_monitoring: Optional[
            "capo_kafka.types.enhanced_monitoring.EnhancedMonitoring"
        ] = None,
        open_monitoring: Optional[
            "capo_kafka.types.open_monitoring_info.OpenMonitoringInfo"
        ] = None,
        logging_info: Optional["capo_kafka.types.logging_info.LoggingInfo"] = None,
    ) -> "capo_kafka.types.update_monitoring_response.UpdateMonitoringResponse":
        """<p>Updates the monitoring settings for the cluster. You can use this operation to specify which Apache Kafka metrics you want Amazon MSK to send to Amazon CloudWatch. You can also specify settings for open monitoring with Prometheus.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            current_version: <p>The version of the MSK cluster to update. Cluster versions aren't simple numbers. You can describe an MSK cluster to find its version. When this update operation is successful, it generates a new cluster version.</p>
            enhanced_monitoring: <p>Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster.</p>
            open_monitoring: <p>The settings for open monitoring.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.update_monitoring_request.UpdateMonitoringRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.update_monitoring_response.UpdateMonitoringResponse"
        ]:
            import capo_kafka._operations.kafka.update_monitoring

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.update_monitoring.async_update_monitoring(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.update_monitoring_request.UpdateMonitoringRequest = {
            "cluster_arn": cluster_arn
        }
        if current_version is not None:
            input_["current_version"] = current_version
        if enhanced_monitoring is not None:
            input_["enhanced_monitoring"] = enhanced_monitoring
        if open_monitoring is not None:
            input_["open_monitoring"] = open_monitoring
        if logging_info is not None:
            input_["logging_info"] = logging_info

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_rebalancing(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        current_version: Optional["capo_kafka.types.__string.__string"] = None,
        rebalancing: Optional["capo_kafka.types.rebalancing.Rebalancing"] = None,
    ) -> "capo_kafka.types.update_rebalancing_response.UpdateRebalancingResponse":
        """<p>Use this resource to update the intelligent rebalancing status of an Amazon MSK Provisioned cluster with Express brokers.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster.</p>
            current_version: <p>The current version of the cluster.</p>
            rebalancing: <p>Specifies if intelligent rebalancing should be turned on for your cluster. The default intelligent rebalancing status is ACTIVE for all new MSK Provisioned clusters that you create with Express brokers.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.update_rebalancing_request.UpdateRebalancingRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.update_rebalancing_response.UpdateRebalancingResponse"
        ]:
            import capo_kafka._operations.kafka.update_rebalancing

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.update_rebalancing.async_update_rebalancing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.update_rebalancing_request.UpdateRebalancingRequest = {
            "cluster_arn": cluster_arn
        }
        if current_version is not None:
            input_["current_version"] = current_version
        if rebalancing is not None:
            input_["rebalancing"] = rebalancing

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_replication_info(
        self,
        replicator_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        consumer_group_replication: Optional[
            "capo_kafka.types.consumer_group_replication_update.ConsumerGroupReplicationUpdate"
        ] = None,
        current_version: Optional["capo_kafka.types.__string.__string"] = None,
        source_kafka_cluster_arn: Optional["capo_kafka.types.__string.__string"] = None,
        source_kafka_cluster_id: Optional["capo_kafka.types.__string.__string"] = None,
        target_kafka_cluster_arn: Optional["capo_kafka.types.__string.__string"] = None,
        target_kafka_cluster_id: Optional["capo_kafka.types.__string.__string"] = None,
        topic_replication: Optional[
            "capo_kafka.types.topic_replication_update.TopicReplicationUpdate"
        ] = None,
        log_delivery: Optional["capo_kafka.types.log_delivery.LogDelivery"] = None,
    ) -> "capo_kafka.types.update_replication_info_response.UpdateReplicationInfoResponse":
        """<p>Updates replication info of a replicator.</p>

        Args:
            consumer_group_replication: <p>Updated consumer group replication information.</p>
            current_version: <p>Current replicator version.</p>
            replicator_arn: <p>The Amazon Resource Name (ARN) of the replicator to be updated.</p>
            source_kafka_cluster_arn: <p>The ARN of the source Kafka cluster.</p>
            source_kafka_cluster_id: <p>The ID of the source Kafka cluster.</p>
            target_kafka_cluster_arn: <p>The ARN of the target Kafka cluster.</p>
            target_kafka_cluster_id: <p>The ID of the target Kafka cluster.</p>
            topic_replication: <p>Updated topic replication information.</p>
            log_delivery: <p>Configuration for delivering replicator logs to customer destinations.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.update_replication_info_request.UpdateReplicationInfoRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.update_replication_info_response.UpdateReplicationInfoResponse"
        ]:
            import capo_kafka._operations.kafka.update_replication_info

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.update_replication_info.async_update_replication_info(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.update_replication_info_request.UpdateReplicationInfoRequest = {
            "replicator_arn": replicator_arn
        }
        if consumer_group_replication is not None:
            input_["consumer_group_replication"] = consumer_group_replication
        if current_version is not None:
            input_["current_version"] = current_version
        if source_kafka_cluster_arn is not None:
            input_["source_kafka_cluster_arn"] = source_kafka_cluster_arn
        if source_kafka_cluster_id is not None:
            input_["source_kafka_cluster_id"] = source_kafka_cluster_id
        if target_kafka_cluster_arn is not None:
            input_["target_kafka_cluster_arn"] = target_kafka_cluster_arn
        if target_kafka_cluster_id is not None:
            input_["target_kafka_cluster_id"] = target_kafka_cluster_id
        if topic_replication is not None:
            input_["topic_replication"] = topic_replication
        if log_delivery is not None:
            input_["log_delivery"] = log_delivery

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_security(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        client_authentication: Optional[
            "capo_kafka.types.client_authentication.ClientAuthentication"
        ] = None,
        current_version: Optional["capo_kafka.types.__string.__string"] = None,
        encryption_info: Optional[
            "capo_kafka.types.encryption_info.EncryptionInfo"
        ] = None,
    ) -> "capo_kafka.types.update_security_response.UpdateSecurityResponse":
        """<p>Updates the security settings for the cluster. You can use this operation to specify encryption and authentication on existing clusters.</p>

        Args:
            client_authentication: <p>Includes all client authentication related information.</p>
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            current_version: <p>The version of the MSK cluster to update. Cluster versions aren't simple numbers. You can describe an MSK cluster to find its version. When this update operation is successful, it generates a new cluster version.</p>
            encryption_info: <p>Includes all encryption-related information.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.update_security_request.UpdateSecurityRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.update_security_response.UpdateSecurityResponse"
        ]:
            import capo_kafka._operations.kafka.update_security

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.update_security.async_update_security(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.update_security_request.UpdateSecurityRequest = {
            "cluster_arn": cluster_arn
        }
        if client_authentication is not None:
            input_["client_authentication"] = client_authentication
        if current_version is not None:
            input_["current_version"] = current_version
        if encryption_info is not None:
            input_["encryption_info"] = encryption_info

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_storage(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        current_version: Optional["capo_kafka.types.__string.__string"] = None,
        provisioned_throughput: Optional[
            "capo_kafka.types.provisioned_throughput.ProvisionedThroughput"
        ] = None,
        storage_mode: Optional["capo_kafka.types.storage_mode.StorageMode"] = None,
        volume_size_gb: Optional["capo_kafka.types.__integer.__integer"] = None,
    ) -> "capo_kafka.types.update_storage_response.UpdateStorageResponse":
        """Updates cluster broker volume size (or) sets cluster storage mode to TIERED.

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster to be updated.</p>
            current_version: <p>The version of cluster to update from. A successful operation will then generate a new version.</p>
            provisioned_throughput: <p>EBS volume provisioned throughput information.</p>
            storage_mode: <p>Controls storage mode for supported storage tiers.</p>
            volume_size_gb: <p>size of the EBS volume to update.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.too_many_requests_exception.TooManyRequestsException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.update_storage_request.UpdateStorageRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.update_storage_response.UpdateStorageResponse"
        ]:
            import capo_kafka._operations.kafka.update_storage

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.update_storage.async_update_storage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.update_storage_request.UpdateStorageRequest = {
            "cluster_arn": cluster_arn
        }
        if current_version is not None:
            input_["current_version"] = current_version
        if provisioned_throughput is not None:
            input_["provisioned_throughput"] = provisioned_throughput
        if storage_mode is not None:
            input_["storage_mode"] = storage_mode
        if volume_size_gb is not None:
            input_["volume_size_gb"] = volume_size_gb

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_topic(
        self,
        cluster_arn: "capo_kafka.types.__string.__string",
        topic_name: "capo_kafka.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaClientConfig] = None,
        configs: Optional["capo_kafka.types.__string.__string"] = None,
        partition_count: Optional["capo_kafka.types.__integer.__integer"] = None,
    ) -> "capo_kafka.types.update_topic_response.UpdateTopicResponse":
        """<p>Updates the configuration of the specified topic.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>
            topic_name: <p>The name of the topic to update configuration for.</p>
            configs: <p>The new topic configurations encoded as a Base64 string.</p>
            partition_count: <p>The new total number of partitions for the topic.</p>

        Raises:
            capo_kafka.errors.bad_request_exception.BadRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.cluster_connectivity_exception.ClusterConnectivityException: <p>Returns information about an error.</p>
            capo_kafka.errors.controller_moved_exception.ControllerMovedException: <p>Returns information about an error.</p>
            capo_kafka.errors.forbidden_exception.ForbiddenException: <p>Returns information about an error.</p>
            capo_kafka.errors.group_subscribed_to_topic_exception.GroupSubscribedToTopicException: <p>Returns information about an error.</p>
            capo_kafka.errors.internal_server_error_exception.InternalServerErrorException: <p>Returns information about an error.</p>
            capo_kafka.errors.kafka_request_exception.KafkaRequestException: <p>Returns information about an error.</p>
            capo_kafka.errors.kafka_timeout_exception.KafkaTimeoutException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_controller_exception.NotControllerException: <p>Returns information about an error.</p>
            capo_kafka.errors.not_found_exception.NotFoundException: <p>Returns information about an error.</p>
            capo_kafka.errors.reassignment_in_progress_exception.ReassignmentInProgressException: <p>Returns information about an error.</p>
            capo_kafka.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returns information about an error.</p>
            capo_kafka.errors.unauthorized_exception.UnauthorizedException: <p>Returns information about an error.</p>
            capo_kafka.errors.unknown_topic_or_partition_exception.UnknownTopicOrPartitionException: <p>Returns information about an error.</p>
            capo_kafka.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafka.types.update_topic_request.UpdateTopicRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafka.types.update_topic_response.UpdateTopicResponse"
        ]:
            import capo_kafka._operations.kafka.update_topic

            (
                output,
                http_response,
            ) = await capo_kafka._operations.kafka.update_topic.async_update_topic(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafka.types.update_topic_request.UpdateTopicRequest = {
            "cluster_arn": cluster_arn,
            "topic_name": topic_name,
        }
        if configs is not None:
            input_["configs"] = configs
        if partition_count is not None:
            input_["partition_count"] = partition_count

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
