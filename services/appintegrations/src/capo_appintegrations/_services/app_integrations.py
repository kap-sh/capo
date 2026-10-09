"""Generated from Smithy shape ``com.amazonaws.appintegrations#AmazonAppIntegrationService``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_appintegrations._auth._signers
import capo_appintegrations._auth._sigv4
from capo_appintegrations._auth._identity import Credentials
from capo_appintegrations._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_appintegrations._auth._zapros_handler import AuthMiddleware
from capo_appintegrations._pagination import resolve_path as _resolve_path
from capo_appintegrations._services._aws_config import aws_config
from capo_appintegrations._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_appintegrations.types.application_association_summary
    import capo_appintegrations.types.application_config
    import capo_appintegrations.types.application_name
    import capo_appintegrations.types.application_namespace
    import capo_appintegrations.types.application_source_config
    import capo_appintegrations.types.application_summary
    import capo_appintegrations.types.application_type
    import capo_appintegrations.types.arn
    import capo_appintegrations.types.arn_or_uuid
    import capo_appintegrations.types.auth_config
    import capo_appintegrations.types.boolean
    import capo_appintegrations.types.client_association_metadata
    import capo_appintegrations.types.client_id
    import capo_appintegrations.types.create_application_request
    import capo_appintegrations.types.create_application_response
    import capo_appintegrations.types.create_data_integration_association_request
    import capo_appintegrations.types.create_data_integration_association_response
    import capo_appintegrations.types.create_data_integration_request
    import capo_appintegrations.types.create_data_integration_response
    import capo_appintegrations.types.create_event_integration_request
    import capo_appintegrations.types.create_event_integration_response
    import capo_appintegrations.types.data_integration_association_summary
    import capo_appintegrations.types.data_integration_summary
    import capo_appintegrations.types.delete_application_request
    import capo_appintegrations.types.delete_application_response
    import capo_appintegrations.types.delete_data_integration_request
    import capo_appintegrations.types.delete_data_integration_response
    import capo_appintegrations.types.delete_event_integration_request
    import capo_appintegrations.types.delete_event_integration_response
    import capo_appintegrations.types.description
    import capo_appintegrations.types.destination_uri
    import capo_appintegrations.types.event_bridge_bus
    import capo_appintegrations.types.event_filter
    import capo_appintegrations.types.event_integration
    import capo_appintegrations.types.event_integration_association
    import capo_appintegrations.types.execution_configuration
    import capo_appintegrations.types.file_configuration
    import capo_appintegrations.types.get_application_request
    import capo_appintegrations.types.get_application_response
    import capo_appintegrations.types.get_data_integration_request
    import capo_appintegrations.types.get_data_integration_response
    import capo_appintegrations.types.get_event_integration_request
    import capo_appintegrations.types.get_event_integration_response
    import capo_appintegrations.types.idempotency_token
    import capo_appintegrations.types.identifier
    import capo_appintegrations.types.iframe_config
    import capo_appintegrations.types.initialization_timeout
    import capo_appintegrations.types.list_application_associations_request
    import capo_appintegrations.types.list_application_associations_response
    import capo_appintegrations.types.list_applications_request
    import capo_appintegrations.types.list_applications_response
    import capo_appintegrations.types.list_data_integration_associations_request
    import capo_appintegrations.types.list_data_integration_associations_response
    import capo_appintegrations.types.list_data_integrations_request
    import capo_appintegrations.types.list_data_integrations_response
    import capo_appintegrations.types.list_event_integration_associations_request
    import capo_appintegrations.types.list_event_integration_associations_response
    import capo_appintegrations.types.list_event_integrations_request
    import capo_appintegrations.types.list_event_integrations_response
    import capo_appintegrations.types.list_tags_for_resource_request
    import capo_appintegrations.types.list_tags_for_resource_response
    import capo_appintegrations.types.max_results
    import capo_appintegrations.types.name
    import capo_appintegrations.types.next_token
    import capo_appintegrations.types.non_blank_string
    import capo_appintegrations.types.object_configuration
    import capo_appintegrations.types.permission_list
    import capo_appintegrations.types.publication_list
    import capo_appintegrations.types.schedule_configuration
    import capo_appintegrations.types.source_uri
    import capo_appintegrations.types.subscription_list
    import capo_appintegrations.types.tag_key_list
    import capo_appintegrations.types.tag_map
    import capo_appintegrations.types.tag_resource_request
    import capo_appintegrations.types.tag_resource_response
    import capo_appintegrations.types.untag_resource_request
    import capo_appintegrations.types.untag_resource_response
    import capo_appintegrations.types.update_application_request
    import capo_appintegrations.types.update_application_response
    import capo_appintegrations.types.update_data_integration_association_request
    import capo_appintegrations.types.update_data_integration_association_response
    import capo_appintegrations.types.update_data_integration_request
    import capo_appintegrations.types.update_data_integration_response
    import capo_appintegrations.types.update_event_integration_request
    import capo_appintegrations.types.update_event_integration_response


class AppIntegrationsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AppIntegrationsClient:
    """A client for the ``AppIntegrations`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = AppIntegrationsClientConfig(
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
        self, config_overrides: Optional[AppIntegrationsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AppIntegrationsClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def create_application(
        self,
        name: "capo_appintegrations.types.application_name.ApplicationName",
        namespace: "capo_appintegrations.types.application_namespace.ApplicationNamespace",
        application_source_config: "capo_appintegrations.types.application_source_config.ApplicationSourceConfig",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        description: Optional[
            "capo_appintegrations.types.description.Description"
        ] = None,
        subscriptions: Optional[
            "capo_appintegrations.types.subscription_list.SubscriptionList"
        ] = None,
        publications: Optional[
            "capo_appintegrations.types.publication_list.PublicationList"
        ] = None,
        client_token: Optional[
            "capo_appintegrations.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_appintegrations.types.tag_map.TagMap"] = None,
        permissions: Optional[
            "capo_appintegrations.types.permission_list.PermissionList"
        ] = None,
        is_service: Optional["capo_appintegrations.types.boolean.Boolean"] = None,
        initialization_timeout: Optional[
            "capo_appintegrations.types.initialization_timeout.InitializationTimeout"
        ] = None,
        application_config: Optional[
            "capo_appintegrations.types.application_config.ApplicationConfig"
        ] = None,
        iframe_config: Optional[
            "capo_appintegrations.types.iframe_config.IframeConfig"
        ] = None,
        application_type: Optional[
            "capo_appintegrations.types.application_type.ApplicationType"
        ] = None,
        auth_config: Optional[
            "capo_appintegrations.types.auth_config.AuthConfig"
        ] = None,
    ) -> "capo_appintegrations.types.create_application_response.CreateApplicationResponse":
        """<p>Creates and persists an Application resource.</p>

        Args:
            name: <p>The name of the application.</p>
            namespace: <p>The namespace of the application.</p>
            description: <p>The description of the application.</p>
            application_source_config: <p>The configuration for where the application should be loaded from.</p>
            subscriptions: <p>The events that the application subscribes.</p>
            publications: <p>The events that the application publishes.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>
            permissions: <p>The configuration of events or requests that the application has access to.</p>
            is_service: <p>Indicates whether the application is a service.</p>
            initialization_timeout: <p>The maximum time in milliseconds allowed to establish a connection with the workspace.</p>
            application_config: <p>The configuration settings for the application.</p>
            iframe_config: <p>The iframe configuration for the application.</p>
            application_type: <p>The type of application.</p>
            auth_config: <p>The authentication settings that Connect Customer uses when calling the external application.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.duplicate_resource_exception.DuplicateResourceException: <p>A resource with the specified name already exists.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_quota_exceeded_exception.ResourceQuotaExceededException: <p>The allowed quota for the resource has been exceeded.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an application
            The following creates an application named My Application with access url https://example.com.

            >>> client.create_application(name='My Application', namespace='myapplication', description='My first application.', application_source_config={'ExternalUrlConfig': {'AccessUrl': 'https://example.com'}})
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.create_application

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.create_application_request.CreateApplicationRequest = {
            "name": name,
            "namespace": namespace,
            "application_source_config": application_source_config,
        }
        if description is not None:
            input_["description"] = description
        if subscriptions is not None:
            input_["subscriptions"] = subscriptions
        if publications is not None:
            input_["publications"] = publications
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if permissions is not None:
            input_["permissions"] = permissions
        if is_service is not None:
            input_["is_service"] = is_service
        if initialization_timeout is not None:
            input_["initialization_timeout"] = initialization_timeout
        if application_config is not None:
            input_["application_config"] = application_config
        if iframe_config is not None:
            input_["iframe_config"] = iframe_config
        if application_type is not None:
            input_["application_type"] = application_type
        if auth_config is not None:
            input_["auth_config"] = auth_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_integration(
        self,
        name: "capo_appintegrations.types.name.Name",
        kms_key: "capo_appintegrations.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        description: Optional[
            "capo_appintegrations.types.description.Description"
        ] = None,
        source_uri: Optional["capo_appintegrations.types.source_uri.SourceURI"] = None,
        schedule_config: Optional[
            "capo_appintegrations.types.schedule_configuration.ScheduleConfiguration"
        ] = None,
        tags: Optional["capo_appintegrations.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_appintegrations.types.idempotency_token.IdempotencyToken"
        ] = None,
        file_configuration: Optional[
            "capo_appintegrations.types.file_configuration.FileConfiguration"
        ] = None,
        object_configuration: Optional[
            "capo_appintegrations.types.object_configuration.ObjectConfiguration"
        ] = None,
    ) -> "capo_appintegrations.types.create_data_integration_response.CreateDataIntegrationResponse":
        """<p>Creates and persists a DataIntegration resource.</p> <note> <p>You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the <code>CreateDataIntegration</code> API.</p> </note>

        Args:
            name: <p>The name of the DataIntegration.</p>
            description: <p>A description of the DataIntegration.</p>
            kms_key: <p>The KMS key ARN for the DataIntegration.</p>
            source_uri: <p>The URI of the data source.</p>
            schedule_config: <p>The name of the data and how often it should be pulled from the source.</p>
            tags: <p>The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            file_configuration: <p>The configuration for what files should be pulled from the source.</p>
            object_configuration: <p>The configuration for what data should be pulled from the source.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.duplicate_resource_exception.DuplicateResourceException: <p>A resource with the specified name already exists.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_quota_exceeded_exception.ResourceQuotaExceededException: <p>The allowed quota for the resource has been exceeded.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.create_data_integration_request.CreateDataIntegrationRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.create_data_integration_response.CreateDataIntegrationResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.create_data_integration

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.create_data_integration.create_data_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.create_data_integration_request.CreateDataIntegrationRequest = {
            "name": name,
            "kms_key": kms_key,
        }
        if description is not None:
            input_["description"] = description
        if source_uri is not None:
            input_["source_uri"] = source_uri
        if schedule_config is not None:
            input_["schedule_config"] = schedule_config
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if file_configuration is not None:
            input_["file_configuration"] = file_configuration
        if object_configuration is not None:
            input_["object_configuration"] = object_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_integration_association(
        self,
        data_integration_identifier: "capo_appintegrations.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        client_id: Optional["capo_appintegrations.types.client_id.ClientId"] = None,
        object_configuration: Optional[
            "capo_appintegrations.types.object_configuration.ObjectConfiguration"
        ] = None,
        destination_uri: Optional[
            "capo_appintegrations.types.destination_uri.DestinationURI"
        ] = None,
        client_association_metadata: Optional[
            "capo_appintegrations.types.client_association_metadata.ClientAssociationMetadata"
        ] = None,
        client_token: Optional[
            "capo_appintegrations.types.idempotency_token.IdempotencyToken"
        ] = None,
        execution_configuration: Optional[
            "capo_appintegrations.types.execution_configuration.ExecutionConfiguration"
        ] = None,
    ) -> "capo_appintegrations.types.create_data_integration_association_response.CreateDataIntegrationAssociationResponse":
        """<p>Creates and persists a DataIntegrationAssociation resource.</p>

        Args:
            data_integration_identifier: <p>A unique identifier for the DataIntegration.</p>
            client_id: <p>The identifier for the client that is associated with the DataIntegration association.</p>
            destination_uri: <p>The URI of the data destination.</p>
            client_association_metadata: <p>The mapping of metadata to be extracted from the data.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            execution_configuration: <p>The configuration for how the files should be pulled from the source.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.resource_quota_exceeded_exception.ResourceQuotaExceededException: <p>The allowed quota for the resource has been exceeded.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.create_data_integration_association_request.CreateDataIntegrationAssociationRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.create_data_integration_association_response.CreateDataIntegrationAssociationResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.create_data_integration_association

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.create_data_integration_association.create_data_integration_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.create_data_integration_association_request.CreateDataIntegrationAssociationRequest = {
            "data_integration_identifier": data_integration_identifier
        }
        if client_id is not None:
            input_["client_id"] = client_id
        if object_configuration is not None:
            input_["object_configuration"] = object_configuration
        if destination_uri is not None:
            input_["destination_uri"] = destination_uri
        if client_association_metadata is not None:
            input_["client_association_metadata"] = client_association_metadata
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if execution_configuration is not None:
            input_["execution_configuration"] = execution_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_event_integration(
        self,
        name: "capo_appintegrations.types.name.Name",
        event_filter: "capo_appintegrations.types.event_filter.EventFilter",
        event_bridge_bus: "capo_appintegrations.types.event_bridge_bus.EventBridgeBus",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        description: Optional[
            "capo_appintegrations.types.description.Description"
        ] = None,
        client_token: Optional[
            "capo_appintegrations.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_appintegrations.types.tag_map.TagMap"] = None,
    ) -> "capo_appintegrations.types.create_event_integration_response.CreateEventIntegrationResponse":
        """<p>Creates an EventIntegration, given a specified name, description, and a reference to an Amazon EventBridge bus in your account and a partner event source that pushes events to that bus. No objects are created in the your account, only metadata that is persisted on the EventIntegration control plane.</p>

        Args:
            name: <p>The name of the event integration.</p>
            description: <p>The description of the event integration.</p>
            event_filter: <p>The event filter.</p>
            event_bridge_bus: <p>The EventBridge bus.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.duplicate_resource_exception.DuplicateResourceException: <p>A resource with the specified name already exists.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_quota_exceeded_exception.ResourceQuotaExceededException: <p>The allowed quota for the resource has been exceeded.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.create_event_integration_request.CreateEventIntegrationRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.create_event_integration_response.CreateEventIntegrationResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.create_event_integration

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.create_event_integration.create_event_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.create_event_integration_request.CreateEventIntegrationRequest = {
            "name": name,
            "event_filter": event_filter,
            "event_bridge_bus": event_bridge_bus,
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application(
        self,
        arn: "capo_appintegrations.types.arn_or_uuid.ArnOrUUID",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        force: Optional["capo_appintegrations.types.boolean.Boolean"] = None,
    ) -> "capo_appintegrations.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes an application. If the application has associations, you must delete them first. Alternatively, use the <code>force</code> option to delete the application and remove its associations.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Application.</p>
            force: <p>Specifies whether to delete the application even if it still has application associations. If <code>true</code>, the operation removes the application and its associations. If <code>false</code> or absent, the delete fails when associations exist.</p> <important> <p>Setting this parameter to <code>true</code> permanently removes all of the application's associations. Doing so might impact other resources that rely on and reference the application. This action can't be undone.</p> </important>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an application
            The following deletes an application.

            >>> client.delete_application(arn='arn:aws:app-integrations:us-west-2:0123456789012:application/98542c53-e8ac-4570-9c85-c6552c8d9c5e')
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.delete_application

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.delete_application_request.DeleteApplicationRequest = {
            "arn": arn
        }
        if force is not None:
            input_["force"] = force

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_data_integration(
        self,
        data_integration_identifier: "capo_appintegrations.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
    ) -> "capo_appintegrations.types.delete_data_integration_response.DeleteDataIntegrationResponse":
        """<p>Deletes the DataIntegration. Only DataIntegrations that don't have any DataIntegrationAssociations can be deleted. Deleting a DataIntegration also deletes the underlying Amazon AppFlow flow and service linked role. </p> <note> <p>You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html">CreateDataIntegration</a> API.</p> </note>

        Args:
            data_integration_identifier: <p>A unique identifier for the DataIntegration.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.delete_data_integration_request.DeleteDataIntegrationRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.delete_data_integration_response.DeleteDataIntegrationResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.delete_data_integration

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.delete_data_integration.delete_data_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.delete_data_integration_request.DeleteDataIntegrationRequest = {
            "data_integration_identifier": data_integration_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_event_integration(
        self,
        name: "capo_appintegrations.types.name.Name",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
    ) -> "capo_appintegrations.types.delete_event_integration_response.DeleteEventIntegrationResponse":
        """<p>Deletes the specified existing event integration. If the event integration is associated with clients, the request is rejected.</p>

        Args:
            name: <p>The name of the event integration.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.delete_event_integration_request.DeleteEventIntegrationRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.delete_event_integration_response.DeleteEventIntegrationResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.delete_event_integration

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.delete_event_integration.delete_event_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.delete_event_integration_request.DeleteEventIntegrationRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_application(
        self,
        arn: "capo_appintegrations.types.arn_or_uuid.ArnOrUUID",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
    ) -> "capo_appintegrations.types.get_application_response.GetApplicationResponse":
        """<p>Get an Application resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Application.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get an application
            The following retrives an application.

            >>> client.get_application(arn='arn:aws:app-integrations:us-west-2:0123456789012:application/98542c53-e8ac-4570-9c85-c6552c8d9c5e')
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.get_application_request.GetApplicationRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.get_application

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.get_application.get_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.get_application_request.GetApplicationRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_integration(
        self,
        identifier: "capo_appintegrations.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
    ) -> "capo_appintegrations.types.get_data_integration_response.GetDataIntegrationResponse":
        """<p>Returns information about the DataIntegration.</p> <note> <p>You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html">CreateDataIntegration</a> API.</p> </note>

        Args:
            identifier: <p>A unique identifier.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.get_data_integration_request.GetDataIntegrationRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.get_data_integration_response.GetDataIntegrationResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.get_data_integration

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.get_data_integration.get_data_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.get_data_integration_request.GetDataIntegrationRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event_integration(
        self,
        name: "capo_appintegrations.types.name.Name",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
    ) -> "capo_appintegrations.types.get_event_integration_response.GetEventIntegrationResponse":
        """<p>Returns information about the event integration.</p>

        Args:
            name: <p>The name of the event integration. </p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.get_event_integration_request.GetEventIntegrationRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.get_event_integration_response.GetEventIntegrationResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.get_event_integration

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.get_event_integration.get_event_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.get_event_integration_request.GetEventIntegrationRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_application_associations(
        self,
        application_id: "capo_appintegrations.types.arn_or_uuid.ArnOrUUID",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        next_token: Optional["capo_appintegrations.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_appintegrations.types.list_application_associations_response.ListApplicationAssociationsResponse":
        """<p>Returns a paginated list of application associations for an application.</p>

        Args:
            application_id: <p>A unique identifier for the Application.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list application associations of an application
            The following retrives application associations of an application

            >>> client.list_application_associations(application_id='98542c53-e8ac-4570-9c85-c6552c8d9c5e')
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.list_application_associations_request.ListApplicationAssociationsRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.list_application_associations_response.ListApplicationAssociationsResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.list_application_associations

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.list_application_associations.list_application_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.list_application_associations_request.ListApplicationAssociationsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_application_associations(
        self,
        application_id: "capo_appintegrations.types.arn_or_uuid.ArnOrUUID",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        next_token: Optional["capo_appintegrations.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_appintegrations.types.application_association_summary.ApplicationAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_application_associations(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("application_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_applications(
        self,
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        next_token: Optional["capo_appintegrations.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_appintegrations.types.max_results.MaxResults"
        ] = None,
        application_type: Optional[
            "capo_appintegrations.types.application_type.ApplicationType"
        ] = None,
    ) -> (
        "capo_appintegrations.types.list_applications_response.ListApplicationsResponse"
    ):
        """<p>Lists applications in the account.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            application_type: <p>The type of application.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list applications in the account
            The following lists application summary in the account.

            >>> client.list_applications(max_results=1)
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.list_applications

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.list_applications_request.ListApplicationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if application_type is not None:
            input_["application_type"] = application_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_applications(
        self,
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        next_token: Optional["capo_appintegrations.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_appintegrations.types.max_results.MaxResults"
        ] = None,
        application_type: Optional[
            "capo_appintegrations.types.application_type.ApplicationType"
        ] = None,
    ) -> "Iterator[capo_appintegrations.types.application_summary.ApplicationSummary]":
        _token = next_token
        while True:
            _response = self.list_applications(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                application_type=application_type,
            )
            _page = _resolve_path(_response, ("applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_data_integration_associations(
        self,
        data_integration_identifier: "capo_appintegrations.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        next_token: Optional["capo_appintegrations.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_appintegrations.types.list_data_integration_associations_response.ListDataIntegrationAssociationsResponse":
        """<p>Returns a paginated list of DataIntegration associations in the account.</p> <note> <p>You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html">CreateDataIntegration</a> API.</p> </note>

        Args:
            data_integration_identifier: <p>A unique identifier for the DataIntegration.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.list_data_integration_associations_request.ListDataIntegrationAssociationsRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.list_data_integration_associations_response.ListDataIntegrationAssociationsResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.list_data_integration_associations

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.list_data_integration_associations.list_data_integration_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.list_data_integration_associations_request.ListDataIntegrationAssociationsRequest = {
            "data_integration_identifier": data_integration_identifier
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_data_integration_associations(
        self,
        data_integration_identifier: "capo_appintegrations.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        next_token: Optional["capo_appintegrations.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_appintegrations.types.data_integration_association_summary.DataIntegrationAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_data_integration_associations(
                data_integration_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_integration_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_data_integrations(
        self,
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        next_token: Optional["capo_appintegrations.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_appintegrations.types.list_data_integrations_response.ListDataIntegrationsResponse":
        """<p>Returns a paginated list of DataIntegrations in the account.</p> <note> <p>You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html">CreateDataIntegration</a> API.</p> </note>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.list_data_integrations_request.ListDataIntegrationsRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.list_data_integrations_response.ListDataIntegrationsResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.list_data_integrations

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.list_data_integrations.list_data_integrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.list_data_integrations_request.ListDataIntegrationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_data_integrations(
        self,
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        next_token: Optional["capo_appintegrations.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_appintegrations.types.data_integration_summary.DataIntegrationSummary]":
        _token = next_token
        while True:
            _response = self.list_data_integrations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_integrations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_event_integration_associations(
        self,
        event_integration_name: "capo_appintegrations.types.name.Name",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        next_token: Optional["capo_appintegrations.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_appintegrations.types.list_event_integration_associations_response.ListEventIntegrationAssociationsResponse":
        """<p>Returns a paginated list of event integration associations in the account. </p>

        Args:
            event_integration_name: <p>The name of the event integration. </p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.list_event_integration_associations_request.ListEventIntegrationAssociationsRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.list_event_integration_associations_response.ListEventIntegrationAssociationsResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.list_event_integration_associations

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.list_event_integration_associations.list_event_integration_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.list_event_integration_associations_request.ListEventIntegrationAssociationsRequest = {
            "event_integration_name": event_integration_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_event_integration_associations(
        self,
        event_integration_name: "capo_appintegrations.types.name.Name",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        next_token: Optional["capo_appintegrations.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_appintegrations.types.event_integration_association.EventIntegrationAssociation]":
        _token = next_token
        while True:
            _response = self.list_event_integration_associations(
                event_integration_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("event_integration_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_event_integrations(
        self,
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        next_token: Optional["capo_appintegrations.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_appintegrations.types.list_event_integrations_response.ListEventIntegrationsResponse":
        """<p>Returns a paginated list of event integrations in the account.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.list_event_integrations_request.ListEventIntegrationsRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.list_event_integrations_response.ListEventIntegrationsResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.list_event_integrations

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.list_event_integrations.list_event_integrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.list_event_integrations_request.ListEventIntegrationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_event_integrations(
        self,
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        next_token: Optional["capo_appintegrations.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_appintegrations.types.event_integration.EventIntegration]":
        _token = next_token
        while True:
            _response = self.list_event_integrations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("event_integrations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_appintegrations.types.arn.Arn",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
    ) -> "capo_appintegrations.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. </p>

        Raises:
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.list_tags_for_resource

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_appintegrations.types.arn.Arn",
        tags: "capo_appintegrations.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
    ) -> "capo_appintegrations.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.tag_resource

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_appintegrations.types.arn.Arn",
        tag_keys: "capo_appintegrations.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
    ) -> "capo_appintegrations.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys.</p>

        Raises:
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.untag_resource

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_application(
        self,
        arn: "capo_appintegrations.types.arn_or_uuid.ArnOrUUID",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        name: Optional[
            "capo_appintegrations.types.application_name.ApplicationName"
        ] = None,
        description: Optional[
            "capo_appintegrations.types.description.Description"
        ] = None,
        application_source_config: Optional[
            "capo_appintegrations.types.application_source_config.ApplicationSourceConfig"
        ] = None,
        subscriptions: Optional[
            "capo_appintegrations.types.subscription_list.SubscriptionList"
        ] = None,
        publications: Optional[
            "capo_appintegrations.types.publication_list.PublicationList"
        ] = None,
        permissions: Optional[
            "capo_appintegrations.types.permission_list.PermissionList"
        ] = None,
        is_service: Optional["capo_appintegrations.types.boolean.Boolean"] = None,
        initialization_timeout: Optional[
            "capo_appintegrations.types.initialization_timeout.InitializationTimeout"
        ] = None,
        application_config: Optional[
            "capo_appintegrations.types.application_config.ApplicationConfig"
        ] = None,
        iframe_config: Optional[
            "capo_appintegrations.types.iframe_config.IframeConfig"
        ] = None,
        application_type: Optional[
            "capo_appintegrations.types.application_type.ApplicationType"
        ] = None,
        auth_config: Optional[
            "capo_appintegrations.types.auth_config.AuthConfig"
        ] = None,
    ) -> "capo_appintegrations.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates and persists an Application resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Application.</p>
            name: <p>The name of the application.</p>
            description: <p>The description of the application.</p>
            application_source_config: <p>The configuration for where the application should be loaded from.</p>
            subscriptions: <p>The events that the application subscribes.</p>
            publications: <p>The events that the application publishes.</p>
            permissions: <p>The configuration of events or requests that the application has access to.</p>
            is_service: <p>Indicates whether the application is a service.</p>
            initialization_timeout: <p>The maximum time in milliseconds allowed to establish a connection with the workspace.</p>
            application_config: <p>The configuration settings for the application.</p>
            iframe_config: <p>The iframe configuration for the application.</p>
            application_type: <p>The type of application.</p>
            auth_config: <p>The authentication settings that Connect Customer uses when calling the external application.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Verify the application's current state and retry the request.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update an application
            The following updates an existing application named with a new name.

            >>> client.update_application(arn='arn:aws:app-integrations:us-west-2:0123456789012:application/98542c53-e8ac-4570-9c85-c6552c8d9c5e', name='My New Application Name')
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.update_application

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.update_application_request.UpdateApplicationRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if application_source_config is not None:
            input_["application_source_config"] = application_source_config
        if subscriptions is not None:
            input_["subscriptions"] = subscriptions
        if publications is not None:
            input_["publications"] = publications
        if permissions is not None:
            input_["permissions"] = permissions
        if is_service is not None:
            input_["is_service"] = is_service
        if initialization_timeout is not None:
            input_["initialization_timeout"] = initialization_timeout
        if application_config is not None:
            input_["application_config"] = application_config
        if iframe_config is not None:
            input_["iframe_config"] = iframe_config
        if application_type is not None:
            input_["application_type"] = application_type
        if auth_config is not None:
            input_["auth_config"] = auth_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_data_integration(
        self,
        identifier: "capo_appintegrations.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        name: Optional["capo_appintegrations.types.name.Name"] = None,
        description: Optional[
            "capo_appintegrations.types.description.Description"
        ] = None,
    ) -> "capo_appintegrations.types.update_data_integration_response.UpdateDataIntegrationResponse":
        """<p>Updates the description of a DataIntegration.</p> <note> <p>You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html">CreateDataIntegration</a> API.</p> </note>

        Args:
            identifier: <p>A unique identifier for the DataIntegration.</p>
            name: <p>The name of the DataIntegration.</p>
            description: <p>A description of the DataIntegration.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.update_data_integration_request.UpdateDataIntegrationRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.update_data_integration_response.UpdateDataIntegrationResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.update_data_integration

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.update_data_integration.update_data_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.update_data_integration_request.UpdateDataIntegrationRequest = {
            "identifier": identifier
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_data_integration_association(
        self,
        data_integration_identifier: "capo_appintegrations.types.identifier.Identifier",
        data_integration_association_identifier: "capo_appintegrations.types.identifier.Identifier",
        execution_configuration: "capo_appintegrations.types.execution_configuration.ExecutionConfiguration",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
    ) -> "capo_appintegrations.types.update_data_integration_association_response.UpdateDataIntegrationAssociationResponse":
        """<p>Updates and persists a DataIntegrationAssociation resource.</p> <note> <p> Updating a DataIntegrationAssociation with ExecutionConfiguration will rerun the on-demand job. </p> </note>

        Args:
            data_integration_identifier: <p>A unique identifier for the DataIntegration.</p>
            data_integration_association_identifier: <p>A unique identifier. of the DataIntegrationAssociation resource</p>
            execution_configuration: <p>The configuration for how the files should be pulled from the source.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.update_data_integration_association_request.UpdateDataIntegrationAssociationRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.update_data_integration_association_response.UpdateDataIntegrationAssociationResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.update_data_integration_association

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.update_data_integration_association.update_data_integration_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.update_data_integration_association_request.UpdateDataIntegrationAssociationRequest = {
            "data_integration_identifier": data_integration_identifier,
            "data_integration_association_identifier": data_integration_association_identifier,
            "execution_configuration": execution_configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_event_integration(
        self,
        name: "capo_appintegrations.types.name.Name",
        *,
        config_overrides: Optional[AppIntegrationsClientConfig] = None,
        description: Optional[
            "capo_appintegrations.types.description.Description"
        ] = None,
    ) -> "capo_appintegrations.types.update_event_integration_response.UpdateEventIntegrationResponse":
        """<p>Updates the description of an event integration.</p>

        Args:
            name: <p>The name of the event integration.</p>
            description: <p>The description of the event integration.</p>

        Raises:
            capo_appintegrations.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_appintegrations.errors.internal_service_error.InternalServiceError: <p>Request processing failed due to an error or failure with the service.</p>
            capo_appintegrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid. </p>
            capo_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_appintegrations.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_appintegrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appintegrations.types.update_event_integration_request.UpdateEventIntegrationRequest]",
        ) -> OperationResponse[
            "capo_appintegrations.types.update_event_integration_response.UpdateEventIntegrationResponse"
        ]:
            import capo_appintegrations._operations.amazon_app_integration_service.update_event_integration

            output, http_response = (
                capo_appintegrations._operations.amazon_app_integration_service.update_event_integration.update_event_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appintegrations.types.update_event_integration_request.UpdateEventIntegrationRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
