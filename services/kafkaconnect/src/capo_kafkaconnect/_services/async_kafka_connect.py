"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#KafkaConnect``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_kafkaconnect._auth._signers
import capo_kafkaconnect._auth._sigv4
from capo_kafkaconnect._auth._identity import Credentials
from capo_kafkaconnect._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_kafkaconnect._auth._zapros_handler import AuthMiddleware
from capo_kafkaconnect._pagination import resolve_path as _resolve_path
from capo_kafkaconnect._services._aws_config import aaws_config
from capo_kafkaconnect._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__boolean
    import capo_kafkaconnect.types.__list_of_plugin
    import capo_kafkaconnect.types.__sensitive_string
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.__string_max1024
    import capo_kafkaconnect.types.__string_min1_max128
    import capo_kafkaconnect.types.capacity
    import capo_kafkaconnect.types.capacity_update
    import capo_kafkaconnect.types.connector_configuration
    import capo_kafkaconnect.types.connector_configuration_update
    import capo_kafkaconnect.types.connector_operation_summary
    import capo_kafkaconnect.types.connector_summary
    import capo_kafkaconnect.types.create_connector_request
    import capo_kafkaconnect.types.create_connector_response
    import capo_kafkaconnect.types.create_custom_plugin_request
    import capo_kafkaconnect.types.create_custom_plugin_response
    import capo_kafkaconnect.types.create_worker_configuration_request
    import capo_kafkaconnect.types.create_worker_configuration_response
    import capo_kafkaconnect.types.custom_plugin_content_type
    import capo_kafkaconnect.types.custom_plugin_location
    import capo_kafkaconnect.types.custom_plugin_summary
    import capo_kafkaconnect.types.delete_connector_request
    import capo_kafkaconnect.types.delete_connector_response
    import capo_kafkaconnect.types.delete_custom_plugin_request
    import capo_kafkaconnect.types.delete_custom_plugin_response
    import capo_kafkaconnect.types.delete_worker_configuration_request
    import capo_kafkaconnect.types.delete_worker_configuration_response
    import capo_kafkaconnect.types.describe_connector_operation_request
    import capo_kafkaconnect.types.describe_connector_operation_response
    import capo_kafkaconnect.types.describe_connector_request
    import capo_kafkaconnect.types.describe_connector_response
    import capo_kafkaconnect.types.describe_custom_plugin_request
    import capo_kafkaconnect.types.describe_custom_plugin_response
    import capo_kafkaconnect.types.describe_worker_configuration_request
    import capo_kafkaconnect.types.describe_worker_configuration_response
    import capo_kafkaconnect.types.kafka_cluster
    import capo_kafkaconnect.types.kafka_cluster_client_authentication
    import capo_kafkaconnect.types.kafka_cluster_encryption_in_transit
    import capo_kafkaconnect.types.list_connector_operations_request
    import capo_kafkaconnect.types.list_connector_operations_response
    import capo_kafkaconnect.types.list_connectors_request
    import capo_kafkaconnect.types.list_connectors_response
    import capo_kafkaconnect.types.list_custom_plugins_request
    import capo_kafkaconnect.types.list_custom_plugins_response
    import capo_kafkaconnect.types.list_tags_for_resource_request
    import capo_kafkaconnect.types.list_tags_for_resource_response
    import capo_kafkaconnect.types.list_worker_configurations_request
    import capo_kafkaconnect.types.list_worker_configurations_response
    import capo_kafkaconnect.types.log_delivery
    import capo_kafkaconnect.types.max_results
    import capo_kafkaconnect.types.network_type
    import capo_kafkaconnect.types.restart_connector_request
    import capo_kafkaconnect.types.restart_connector_response
    import capo_kafkaconnect.types.tag_key_list
    import capo_kafkaconnect.types.tag_resource_request
    import capo_kafkaconnect.types.tag_resource_response
    import capo_kafkaconnect.types.tags
    import capo_kafkaconnect.types.untag_resource_request
    import capo_kafkaconnect.types.untag_resource_response
    import capo_kafkaconnect.types.update_connector_request
    import capo_kafkaconnect.types.update_connector_response
    import capo_kafkaconnect.types.worker_configuration
    import capo_kafkaconnect.types.worker_configuration_summary


class AsyncKafkaConnectClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncKafkaConnectClient:
    """A client for the ``KafkaConnect`` service.

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
        self._config = AsyncKafkaConnectClientConfig(
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
        self, config_overrides: Optional[AsyncKafkaConnectClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncKafkaConnectClientConfig = config_overrides or {}
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

    async def create_connector(
        self,
        capacity: "capo_kafkaconnect.types.capacity.Capacity",
        connector_configuration: "capo_kafkaconnect.types.connector_configuration.ConnectorConfiguration",
        connector_name: "capo_kafkaconnect.types.__string_min1_max128.__stringMin1Max128",
        kafka_cluster: "capo_kafkaconnect.types.kafka_cluster.KafkaCluster",
        kafka_cluster_client_authentication: "capo_kafkaconnect.types.kafka_cluster_client_authentication.KafkaClusterClientAuthentication",
        kafka_cluster_encryption_in_transit: "capo_kafkaconnect.types.kafka_cluster_encryption_in_transit.KafkaClusterEncryptionInTransit",
        kafka_connect_version: "capo_kafkaconnect.types.__string.__string",
        plugins: "capo_kafkaconnect.types.__list_of_plugin.__listOfPlugin",
        service_execution_role_arn: "capo_kafkaconnect.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
        connector_description: Optional[
            "capo_kafkaconnect.types.__string_max1024.__stringMax1024"
        ] = None,
        log_delivery: Optional[
            "capo_kafkaconnect.types.log_delivery.LogDelivery"
        ] = None,
        network_type: Optional[
            "capo_kafkaconnect.types.network_type.NetworkType"
        ] = None,
        worker_configuration: Optional[
            "capo_kafkaconnect.types.worker_configuration.WorkerConfiguration"
        ] = None,
        tags: Optional["capo_kafkaconnect.types.tags.Tags"] = None,
    ) -> "capo_kafkaconnect.types.create_connector_response.CreateConnectorResponse":
        """<p>Creates a connector using the specified properties. </p>

        Args:
            capacity: <p>Information about the capacity allocated to the connector. Exactly one of the two properties must be specified.</p>
            connector_configuration: <p>A map of keys to values that represent the configuration for the connector.</p>
            connector_description: <p>A summary description of the connector.</p>
            connector_name: <p>The name of the connector.</p>
            kafka_cluster: <p>Specifies which Apache Kafka cluster to connect to.</p>
            kafka_cluster_client_authentication: <p>Details of the client authentication used by the Apache Kafka cluster.</p>
            kafka_cluster_encryption_in_transit: <p>Details of encryption in transit to the Apache Kafka cluster.</p>
            kafka_connect_version: <p>The version of Kafka Connect. It has to be compatible with both the Apache Kafka cluster's version and the plugins.</p>
            log_delivery: <p>Details about log delivery.</p>
            network_type: <p>The network type of the connector. It gives connectors connectivity to either IPv4 (IPV4) or IPv4 and IPv6 (DUAL) destinations. Defaults to IPV4.</p>
            plugins: <important> <p>Amazon MSK Connect does not currently support specifying multiple plugins as a list. To use more than one plugin for your connector, you can create a single custom plugin using a ZIP file that bundles multiple plugins together.</p> </important> <p>Specifies which plugin to use for the connector. You must specify a single-element list containing one <code>customPlugin</code> object.</p>
            service_execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role used by the connector to access the Amazon Web Services resources that it needs. The types of resources depends on the logic of the connector. For example, a connector that has Amazon S3 as a destination must have permissions that allow it to write to the S3 destination bucket.</p>
            worker_configuration: <p>Specifies which worker configuration to use with the connector.</p>
            tags: <p>The tags you want to attach to the connector.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.conflict_exception.ConflictException: <p>HTTP Status Code 409: Conflict. A resource with this name already exists. Retry your request with another name.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.create_connector_request.CreateConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.create_connector_response.CreateConnectorResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.create_connector

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.create_connector.async_create_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.create_connector_request.CreateConnectorRequest = {
            "capacity": capacity,
            "connector_configuration": connector_configuration,
            "connector_name": connector_name,
            "kafka_cluster": kafka_cluster,
            "kafka_cluster_client_authentication": kafka_cluster_client_authentication,
            "kafka_cluster_encryption_in_transit": kafka_cluster_encryption_in_transit,
            "kafka_connect_version": kafka_connect_version,
            "plugins": plugins,
            "service_execution_role_arn": service_execution_role_arn,
        }
        if connector_description is not None:
            input_["connector_description"] = connector_description
        if log_delivery is not None:
            input_["log_delivery"] = log_delivery
        if network_type is not None:
            input_["network_type"] = network_type
        if worker_configuration is not None:
            input_["worker_configuration"] = worker_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_custom_plugin(
        self,
        content_type: "capo_kafkaconnect.types.custom_plugin_content_type.CustomPluginContentType",
        location: "capo_kafkaconnect.types.custom_plugin_location.CustomPluginLocation",
        name: "capo_kafkaconnect.types.__string_min1_max128.__stringMin1Max128",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
        description: Optional[
            "capo_kafkaconnect.types.__string_max1024.__stringMax1024"
        ] = None,
        tags: Optional["capo_kafkaconnect.types.tags.Tags"] = None,
    ) -> "capo_kafkaconnect.types.create_custom_plugin_response.CreateCustomPluginResponse":
        """<p>Creates a custom plugin using the specified properties.</p>

        Args:
            content_type: <p>The type of the plugin file.</p>
            description: <p>A summary description of the custom plugin.</p>
            location: <p>Information about the location of a custom plugin.</p>
            name: <p>The name of the custom plugin.</p>
            tags: <p>The tags you want to attach to the custom plugin.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.conflict_exception.ConflictException: <p>HTTP Status Code 409: Conflict. A resource with this name already exists. Retry your request with another name.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.create_custom_plugin_request.CreateCustomPluginRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.create_custom_plugin_response.CreateCustomPluginResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.create_custom_plugin

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.create_custom_plugin.async_create_custom_plugin(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.create_custom_plugin_request.CreateCustomPluginRequest = {
            "content_type": content_type,
            "location": location,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_worker_configuration(
        self,
        name: "capo_kafkaconnect.types.__string_min1_max128.__stringMin1Max128",
        properties_file_content: "capo_kafkaconnect.types.__sensitive_string.__sensitiveString",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
        description: Optional[
            "capo_kafkaconnect.types.__string_max1024.__stringMax1024"
        ] = None,
        tags: Optional["capo_kafkaconnect.types.tags.Tags"] = None,
    ) -> "capo_kafkaconnect.types.create_worker_configuration_response.CreateWorkerConfigurationResponse":
        """<p>Creates a worker configuration using the specified properties.</p>

        Args:
            description: <p>A summary description of the worker configuration.</p>
            name: <p>The name of the worker configuration.</p>
            properties_file_content: <p>Base64 encoded contents of connect-distributed.properties file.</p>
            tags: <p>The tags you want to attach to the worker configuration.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.conflict_exception.ConflictException: <p>HTTP Status Code 409: Conflict. A resource with this name already exists. Retry your request with another name.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.create_worker_configuration_request.CreateWorkerConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.create_worker_configuration_response.CreateWorkerConfigurationResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.create_worker_configuration

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.create_worker_configuration.async_create_worker_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.create_worker_configuration_request.CreateWorkerConfigurationRequest = {
            "name": name,
            "properties_file_content": properties_file_content,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connector(
        self,
        connector_arn: "capo_kafkaconnect.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
        current_version: Optional["capo_kafkaconnect.types.__string.__string"] = None,
    ) -> "capo_kafkaconnect.types.delete_connector_response.DeleteConnectorResponse":
        """<p>Deletes the specified connector.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector that you want to delete.</p>
            current_version: <p>The current version of the connector that you want to delete.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.delete_connector_response.DeleteConnectorResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.delete_connector

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.delete_connector.async_delete_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.delete_connector_request.DeleteConnectorRequest = {
            "connector_arn": connector_arn
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

    async def delete_custom_plugin(
        self,
        custom_plugin_arn: "capo_kafkaconnect.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
    ) -> "capo_kafkaconnect.types.delete_custom_plugin_response.DeleteCustomPluginResponse":
        """<p>Deletes a custom plugin.</p>

        Args:
            custom_plugin_arn: <p>The Amazon Resource Name (ARN) of the custom plugin that you want to delete.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.delete_custom_plugin_request.DeleteCustomPluginRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.delete_custom_plugin_response.DeleteCustomPluginResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.delete_custom_plugin

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.delete_custom_plugin.async_delete_custom_plugin(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.delete_custom_plugin_request.DeleteCustomPluginRequest = {
            "custom_plugin_arn": custom_plugin_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_worker_configuration(
        self,
        worker_configuration_arn: "capo_kafkaconnect.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
    ) -> "capo_kafkaconnect.types.delete_worker_configuration_response.DeleteWorkerConfigurationResponse":
        """<p>Deletes the specified worker configuration.</p>

        Args:
            worker_configuration_arn: <p>The Amazon Resource Name (ARN) of the worker configuration that you want to delete.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.delete_worker_configuration_request.DeleteWorkerConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.delete_worker_configuration_response.DeleteWorkerConfigurationResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.delete_worker_configuration

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.delete_worker_configuration.async_delete_worker_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.delete_worker_configuration_request.DeleteWorkerConfigurationRequest = {
            "worker_configuration_arn": worker_configuration_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_connector(
        self,
        connector_arn: "capo_kafkaconnect.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
    ) -> (
        "capo_kafkaconnect.types.describe_connector_response.DescribeConnectorResponse"
    ):
        """<p>Returns summary information about the connector.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector that you want to describe.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.describe_connector_request.DescribeConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.describe_connector_response.DescribeConnectorResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.describe_connector

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.describe_connector.async_describe_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.describe_connector_request.DescribeConnectorRequest = {
            "connector_arn": connector_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_connector_operation(
        self,
        connector_operation_arn: "capo_kafkaconnect.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
    ) -> "capo_kafkaconnect.types.describe_connector_operation_response.DescribeConnectorOperationResponse":
        """<p>Returns information about the specified connector's operations.</p>

        Args:
            connector_operation_arn: <p>ARN of the connector operation to be described.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.describe_connector_operation_request.DescribeConnectorOperationRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.describe_connector_operation_response.DescribeConnectorOperationResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.describe_connector_operation

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.describe_connector_operation.async_describe_connector_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.describe_connector_operation_request.DescribeConnectorOperationRequest = {
            "connector_operation_arn": connector_operation_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_custom_plugin(
        self,
        custom_plugin_arn: "capo_kafkaconnect.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
    ) -> "capo_kafkaconnect.types.describe_custom_plugin_response.DescribeCustomPluginResponse":
        """<p>A summary description of the custom plugin.</p>

        Args:
            custom_plugin_arn: <p>Returns information about a custom plugin.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.describe_custom_plugin_request.DescribeCustomPluginRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.describe_custom_plugin_response.DescribeCustomPluginResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.describe_custom_plugin

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.describe_custom_plugin.async_describe_custom_plugin(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.describe_custom_plugin_request.DescribeCustomPluginRequest = {
            "custom_plugin_arn": custom_plugin_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_worker_configuration(
        self,
        worker_configuration_arn: "capo_kafkaconnect.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
    ) -> "capo_kafkaconnect.types.describe_worker_configuration_response.DescribeWorkerConfigurationResponse":
        """<p>Returns information about a worker configuration.</p>

        Args:
            worker_configuration_arn: <p>The Amazon Resource Name (ARN) of the worker configuration that you want to get information about.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.describe_worker_configuration_request.DescribeWorkerConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.describe_worker_configuration_response.DescribeWorkerConfigurationResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.describe_worker_configuration

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.describe_worker_configuration.async_describe_worker_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.describe_worker_configuration_request.DescribeWorkerConfigurationRequest = {
            "worker_configuration_arn": worker_configuration_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_connector_operations(
        self,
        connector_arn: "capo_kafkaconnect.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
        max_results: Optional["capo_kafkaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafkaconnect.types.__string.__string"] = None,
    ) -> "capo_kafkaconnect.types.list_connector_operations_response.ListConnectorOperationsResponse":
        """<p>Lists information about a connector's operation(s).</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector for which to list operations.</p>
            max_results: <p>Maximum number of connector operations to fetch in one get request.</p>
            next_token: <p>If the response is truncated, it includes a NextToken. Send this NextToken in a subsequent request to continue listing from where it left off.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.list_connector_operations_request.ListConnectorOperationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.list_connector_operations_response.ListConnectorOperationsResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.list_connector_operations

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.list_connector_operations.async_list_connector_operations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.list_connector_operations_request.ListConnectorOperationsRequest = {
            "connector_arn": connector_arn
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

    async def iter_list_connector_operations(
        self,
        connector_arn: "capo_kafkaconnect.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
        max_results: Optional["capo_kafkaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafkaconnect.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafkaconnect.types.connector_operation_summary.ConnectorOperationSummary]":
        _token = next_token
        while True:
            _response = await self.list_connector_operations(
                connector_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("connector_operations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_connectors(
        self,
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
        connector_name_prefix: Optional[
            "capo_kafkaconnect.types.__string.__string"
        ] = None,
        max_results: Optional["capo_kafkaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafkaconnect.types.__string.__string"] = None,
    ) -> "capo_kafkaconnect.types.list_connectors_response.ListConnectorsResponse":
        """<p>Returns a list of all the connectors in this account and Region. The list is limited to connectors whose name starts with the specified prefix. The response also includes a description of each of the listed connectors.</p>

        Args:
            connector_name_prefix: <p>The name prefix that you want to use to search for and list connectors.</p>
            max_results: <p>The maximum number of connectors to list in one response.</p>
            next_token: <p>If the response of a ListConnectors operation is truncated, it will include a NextToken. Send this NextToken in a subsequent request to continue listing from where the previous operation left off.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.list_connectors_request.ListConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.list_connectors

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.list_connectors.async_list_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.list_connectors_request.ListConnectorsRequest = {}
        if connector_name_prefix is not None:
            input_["connector_name_prefix"] = connector_name_prefix
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

    async def iter_list_connectors(
        self,
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
        connector_name_prefix: Optional[
            "capo_kafkaconnect.types.__string.__string"
        ] = None,
        max_results: Optional["capo_kafkaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafkaconnect.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafkaconnect.types.connector_summary.ConnectorSummary]":
        _token = next_token
        while True:
            _response = await self.list_connectors(
                config_overrides=config_overrides,
                connector_name_prefix=connector_name_prefix,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("connectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_custom_plugins(
        self,
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
        max_results: Optional["capo_kafkaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafkaconnect.types.__string.__string"] = None,
        name_prefix: Optional["capo_kafkaconnect.types.__string.__string"] = None,
    ) -> (
        "capo_kafkaconnect.types.list_custom_plugins_response.ListCustomPluginsResponse"
    ):
        """<p>Returns a list of all of the custom plugins in this account and Region.</p>

        Args:
            max_results: <p>The maximum number of custom plugins to list in one response.</p>
            next_token: <p>If the response of a ListCustomPlugins operation is truncated, it will include a NextToken. Send this NextToken in a subsequent request to continue listing from where the previous operation left off.</p>
            name_prefix: <p>Lists custom plugin names that start with the specified text string.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.list_custom_plugins_request.ListCustomPluginsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.list_custom_plugins_response.ListCustomPluginsResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.list_custom_plugins

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.list_custom_plugins.async_list_custom_plugins(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.list_custom_plugins_request.ListCustomPluginsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_custom_plugins(
        self,
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
        max_results: Optional["capo_kafkaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafkaconnect.types.__string.__string"] = None,
        name_prefix: Optional["capo_kafkaconnect.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafkaconnect.types.custom_plugin_summary.CustomPluginSummary]":
        _token = next_token
        while True:
            _response = await self.list_custom_plugins(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                name_prefix=name_prefix,
            )
            _page = _resolve_path(_response, ("custom_plugins",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_kafkaconnect.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
    ) -> "capo_kafkaconnect.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all the tags attached to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to list all attached tags.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_worker_configurations(
        self,
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
        max_results: Optional["capo_kafkaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafkaconnect.types.__string.__string"] = None,
        name_prefix: Optional["capo_kafkaconnect.types.__string.__string"] = None,
    ) -> "capo_kafkaconnect.types.list_worker_configurations_response.ListWorkerConfigurationsResponse":
        """<p>Returns a list of all of the worker configurations in this account and Region.</p>

        Args:
            max_results: <p>The maximum number of worker configurations to list in one response.</p>
            next_token: <p>If the response of a ListWorkerConfigurations operation is truncated, it will include a NextToken. Send this NextToken in a subsequent request to continue listing from where the previous operation left off.</p>
            name_prefix: <p>Lists worker configuration names that start with the specified text string.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.list_worker_configurations_request.ListWorkerConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.list_worker_configurations_response.ListWorkerConfigurationsResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.list_worker_configurations

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.list_worker_configurations.async_list_worker_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.list_worker_configurations_request.ListWorkerConfigurationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_worker_configurations(
        self,
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
        max_results: Optional["capo_kafkaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_kafkaconnect.types.__string.__string"] = None,
        name_prefix: Optional["capo_kafkaconnect.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_kafkaconnect.types.worker_configuration_summary.WorkerConfigurationSummary]":
        _token = next_token
        while True:
            _response = await self.list_worker_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                name_prefix=name_prefix,
            )
            _page = _resolve_path(_response, ("worker_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def restart_connector(
        self,
        connector_arn: "capo_kafkaconnect.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
        only_failed_tasks: Optional[
            "capo_kafkaconnect.types.__boolean.__boolean"
        ] = None,
    ) -> "capo_kafkaconnect.types.restart_connector_response.RestartConnectorResponse":
        """<p>Restarts the specified connector. By default, this operation restarts the connector and all of its tasks. This operation is asynchronous and returns a connector operation ARN that you can pass to <code>DescribeConnectorOperation</code> to track the state of the restart.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector that you want to restart.</p>
            only_failed_tasks: <p>Specifies whether to restart only the connector's failed tasks. If <code>true</code>, the operation restarts only the tasks that are currently in a failed state, and healthy tasks continue running. If <code>false</code> or not specified, the operation restarts the connector and all of its tasks.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.restart_connector_request.RestartConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.restart_connector_response.RestartConnectorResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.restart_connector

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.restart_connector.async_restart_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.restart_connector_request.RestartConnectorRequest = {
            "connector_arn": connector_arn
        }
        if only_failed_tasks is not None:
            input_["only_failed_tasks"] = only_failed_tasks

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_kafkaconnect.types.__string.__string",
        tags: "capo_kafkaconnect.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
    ) -> "capo_kafkaconnect.types.tag_resource_response.TagResourceResponse":
        """<p>Attaches tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which you want to attach tags.</p>
            tags: <p>The tags that you want to attach to the resource.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.conflict_exception.ConflictException: <p>HTTP Status Code 409: Conflict. A resource with this name already exists. Retry your request with another name.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.tag_resource

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_kafkaconnect.types.__string.__string",
        tag_keys: "capo_kafkaconnect.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
    ) -> "capo_kafkaconnect.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which you want to remove tags.</p>
            tag_keys: <p>The keys of the tags that you want to remove from the resource.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.untag_resource

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_connector(
        self,
        connector_arn: "capo_kafkaconnect.types.__string.__string",
        current_version: "capo_kafkaconnect.types.__string.__string",
        *,
        config_overrides: Optional[AsyncKafkaConnectClientConfig] = None,
        capacity: Optional[
            "capo_kafkaconnect.types.capacity_update.CapacityUpdate"
        ] = None,
        connector_configuration: Optional[
            "capo_kafkaconnect.types.connector_configuration_update.ConnectorConfigurationUpdate"
        ] = None,
    ) -> "capo_kafkaconnect.types.update_connector_response.UpdateConnectorResponse":
        """<p>Updates the specified connector. For request body, specify only one parameter: either <code>capacity</code> or <code>connectorConfiguration</code>.</p>

        Args:
            capacity: <p>The target capacity.</p>
            connector_configuration: <p>A map of keys to values that represent the configuration for the connector.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector that you want to update.</p>
            current_version: <p>The current version of the connector that you want to update.</p>

        Raises:
            capo_kafkaconnect.errors.bad_request_exception.BadRequestException: <p>HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.forbidden_exception.ForbiddenException: <p>HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.</p>
            capo_kafkaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.</p>
            capo_kafkaconnect.errors.not_found_exception.NotFoundException: <p>HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.</p>
            capo_kafkaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.</p>
            capo_kafkaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>HTTP Status Code 429: Limit exceeded. Resource limit reached.</p>
            capo_kafkaconnect.errors.unauthorized_exception.UnauthorizedException: <p>HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.</p>
            capo_kafkaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kafkaconnect.types.update_connector_request.UpdateConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_kafkaconnect.types.update_connector_response.UpdateConnectorResponse"
        ]:
            import capo_kafkaconnect._operations.kafka_connect.update_connector

            (
                output,
                http_response,
            ) = await capo_kafkaconnect._operations.kafka_connect.update_connector.async_update_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kafkaconnect.types.update_connector_request.UpdateConnectorRequest = {
            "connector_arn": connector_arn,
            "current_version": current_version,
        }
        if capacity is not None:
            input_["capacity"] = capacity
        if connector_configuration is not None:
            input_["connector_configuration"] = connector_configuration

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
