"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#AWSIoTTwinMaker``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_iottwinmaker._auth._signers
import capo_iottwinmaker._auth._sigv4
from capo_iottwinmaker._auth._identity import Credentials
from capo_iottwinmaker._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_iottwinmaker._auth._zapros_handler import AuthMiddleware
from capo_iottwinmaker._pagination import resolve_path as _resolve_path
from capo_iottwinmaker._services._aws_config import aws_config
from capo_iottwinmaker._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_iottwinmaker.types.batch_put_property_values_request
    import capo_iottwinmaker.types.batch_put_property_values_response
    import capo_iottwinmaker.types.boolean
    import capo_iottwinmaker.types.cancel_metadata_transfer_job_request
    import capo_iottwinmaker.types.cancel_metadata_transfer_job_response
    import capo_iottwinmaker.types.component_path
    import capo_iottwinmaker.types.component_type_id
    import capo_iottwinmaker.types.component_type_name
    import capo_iottwinmaker.types.component_updates_map_request
    import capo_iottwinmaker.types.components_map_request
    import capo_iottwinmaker.types.composite_component_types_request
    import capo_iottwinmaker.types.composite_component_updates_map_request
    import capo_iottwinmaker.types.composite_components_map_request
    import capo_iottwinmaker.types.create_component_type_request
    import capo_iottwinmaker.types.create_component_type_response
    import capo_iottwinmaker.types.create_entity_request
    import capo_iottwinmaker.types.create_entity_response
    import capo_iottwinmaker.types.create_metadata_transfer_job_request
    import capo_iottwinmaker.types.create_metadata_transfer_job_response
    import capo_iottwinmaker.types.create_scene_request
    import capo_iottwinmaker.types.create_scene_response
    import capo_iottwinmaker.types.create_sync_job_request
    import capo_iottwinmaker.types.create_sync_job_response
    import capo_iottwinmaker.types.create_workspace_request
    import capo_iottwinmaker.types.create_workspace_response
    import capo_iottwinmaker.types.delete_component_type_request
    import capo_iottwinmaker.types.delete_component_type_response
    import capo_iottwinmaker.types.delete_entity_request
    import capo_iottwinmaker.types.delete_entity_response
    import capo_iottwinmaker.types.delete_scene_request
    import capo_iottwinmaker.types.delete_scene_response
    import capo_iottwinmaker.types.delete_sync_job_request
    import capo_iottwinmaker.types.delete_sync_job_response
    import capo_iottwinmaker.types.delete_workspace_request
    import capo_iottwinmaker.types.delete_workspace_response
    import capo_iottwinmaker.types.description
    import capo_iottwinmaker.types.destination_configuration
    import capo_iottwinmaker.types.destination_type
    import capo_iottwinmaker.types.entity_id
    import capo_iottwinmaker.types.entity_name
    import capo_iottwinmaker.types.entries
    import capo_iottwinmaker.types.execute_query_request
    import capo_iottwinmaker.types.execute_query_response
    import capo_iottwinmaker.types.extends_from
    import capo_iottwinmaker.types.functions_request
    import capo_iottwinmaker.types.get_component_type_request
    import capo_iottwinmaker.types.get_component_type_response
    import capo_iottwinmaker.types.get_entity_request
    import capo_iottwinmaker.types.get_entity_response
    import capo_iottwinmaker.types.get_metadata_transfer_job_request
    import capo_iottwinmaker.types.get_metadata_transfer_job_response
    import capo_iottwinmaker.types.get_pricing_plan_request
    import capo_iottwinmaker.types.get_pricing_plan_response
    import capo_iottwinmaker.types.get_property_value_history_request
    import capo_iottwinmaker.types.get_property_value_history_response
    import capo_iottwinmaker.types.get_property_value_request
    import capo_iottwinmaker.types.get_property_value_response
    import capo_iottwinmaker.types.get_scene_request
    import capo_iottwinmaker.types.get_scene_response
    import capo_iottwinmaker.types.get_sync_job_request
    import capo_iottwinmaker.types.get_sync_job_response
    import capo_iottwinmaker.types.get_workspace_request
    import capo_iottwinmaker.types.get_workspace_response
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.id_or_arn
    import capo_iottwinmaker.types.interpolation_parameters
    import capo_iottwinmaker.types.list_component_types_filters
    import capo_iottwinmaker.types.list_component_types_request
    import capo_iottwinmaker.types.list_component_types_response
    import capo_iottwinmaker.types.list_components_request
    import capo_iottwinmaker.types.list_components_response
    import capo_iottwinmaker.types.list_entities_filters
    import capo_iottwinmaker.types.list_entities_request
    import capo_iottwinmaker.types.list_entities_response
    import capo_iottwinmaker.types.list_metadata_transfer_jobs_filters
    import capo_iottwinmaker.types.list_metadata_transfer_jobs_request
    import capo_iottwinmaker.types.list_metadata_transfer_jobs_response
    import capo_iottwinmaker.types.list_properties_request
    import capo_iottwinmaker.types.list_properties_response
    import capo_iottwinmaker.types.list_scenes_request
    import capo_iottwinmaker.types.list_scenes_response
    import capo_iottwinmaker.types.list_sync_jobs_request
    import capo_iottwinmaker.types.list_sync_jobs_response
    import capo_iottwinmaker.types.list_sync_resources_request
    import capo_iottwinmaker.types.list_sync_resources_response
    import capo_iottwinmaker.types.list_tags_for_resource_request
    import capo_iottwinmaker.types.list_tags_for_resource_response
    import capo_iottwinmaker.types.list_workspaces_request
    import capo_iottwinmaker.types.list_workspaces_response
    import capo_iottwinmaker.types.max_results
    import capo_iottwinmaker.types.name
    import capo_iottwinmaker.types.next_token
    import capo_iottwinmaker.types.order_by_time
    import capo_iottwinmaker.types.parent_entity_id
    import capo_iottwinmaker.types.parent_entity_update_request
    import capo_iottwinmaker.types.pricing_bundles
    import capo_iottwinmaker.types.pricing_mode
    import capo_iottwinmaker.types.property_definitions_request
    import capo_iottwinmaker.types.property_filters
    import capo_iottwinmaker.types.property_groups_request
    import capo_iottwinmaker.types.query_service_max_results
    import capo_iottwinmaker.types.query_statement
    import capo_iottwinmaker.types.role_arn
    import capo_iottwinmaker.types.s3_location
    import capo_iottwinmaker.types.s3_url
    import capo_iottwinmaker.types.scene_capabilities
    import capo_iottwinmaker.types.scene_metadata_map
    import capo_iottwinmaker.types.selected_property_list
    import capo_iottwinmaker.types.source_configurations
    import capo_iottwinmaker.types.source_type
    import capo_iottwinmaker.types.sync_resource_filters
    import capo_iottwinmaker.types.sync_source
    import capo_iottwinmaker.types.tabular_conditions
    import capo_iottwinmaker.types.tag_key_list
    import capo_iottwinmaker.types.tag_map
    import capo_iottwinmaker.types.tag_resource_request
    import capo_iottwinmaker.types.tag_resource_response
    import capo_iottwinmaker.types.time
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn
    import capo_iottwinmaker.types.untag_resource_request
    import capo_iottwinmaker.types.untag_resource_response
    import capo_iottwinmaker.types.update_component_type_request
    import capo_iottwinmaker.types.update_component_type_response
    import capo_iottwinmaker.types.update_entity_request
    import capo_iottwinmaker.types.update_entity_response
    import capo_iottwinmaker.types.update_pricing_plan_request
    import capo_iottwinmaker.types.update_pricing_plan_response
    import capo_iottwinmaker.types.update_scene_request
    import capo_iottwinmaker.types.update_scene_response
    import capo_iottwinmaker.types.update_workspace_request
    import capo_iottwinmaker.types.update_workspace_response


class IoTTwinMakerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class IoTTwinMakerClient:
    """A client for the ``IoTTwinMaker`` service.

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
        self._config = IoTTwinMakerClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[IoTTwinMakerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: IoTTwinMakerClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    def batch_put_property_values(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        entries: "capo_iottwinmaker.types.entries.Entries",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
    ) -> "capo_iottwinmaker.types.batch_put_property_values_response.BatchPutPropertyValuesResponse":
        """<p>Sets values for multiple time series properties.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the properties to set.</p>
            entries: <p>An object that maps strings to the property value entries to set. Each string in the mapping must be unique to this object.</p>

        Raises:
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.batch_put_property_values_request.BatchPutPropertyValuesRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.batch_put_property_values_response.BatchPutPropertyValuesResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.batch_put_property_values

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.batch_put_property_values.batch_put_property_values(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.batch_put_property_values_request.BatchPutPropertyValuesRequest = {
            "workspace_id": workspace_id,
            "entries": entries,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_metadata_transfer_job(
        self,
        metadata_transfer_job_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
    ) -> "capo_iottwinmaker.types.cancel_metadata_transfer_job_response.CancelMetadataTransferJobResponse":
        """<p>Cancels the metadata transfer job.</p>

        Args:
            metadata_transfer_job_id: <p>The metadata transfer job Id.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.cancel_metadata_transfer_job_request.CancelMetadataTransferJobRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.cancel_metadata_transfer_job_response.CancelMetadataTransferJobResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.cancel_metadata_transfer_job

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.cancel_metadata_transfer_job.cancel_metadata_transfer_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.cancel_metadata_transfer_job_request.CancelMetadataTransferJobRequest = {
            "metadata_transfer_job_id": metadata_transfer_job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_component_type(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        component_type_id: "capo_iottwinmaker.types.component_type_id.ComponentTypeId",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        is_singleton: Optional["capo_iottwinmaker.types.boolean.Boolean"] = None,
        description: Optional["capo_iottwinmaker.types.description.Description"] = None,
        property_definitions: Optional[
            "capo_iottwinmaker.types.property_definitions_request.PropertyDefinitionsRequest"
        ] = None,
        extends_from: Optional[
            "capo_iottwinmaker.types.extends_from.ExtendsFrom"
        ] = None,
        functions: Optional[
            "capo_iottwinmaker.types.functions_request.FunctionsRequest"
        ] = None,
        tags: Optional["capo_iottwinmaker.types.tag_map.TagMap"] = None,
        property_groups: Optional[
            "capo_iottwinmaker.types.property_groups_request.PropertyGroupsRequest"
        ] = None,
        component_type_name: Optional[
            "capo_iottwinmaker.types.component_type_name.ComponentTypeName"
        ] = None,
        composite_component_types: Optional[
            "capo_iottwinmaker.types.composite_component_types_request.CompositeComponentTypesRequest"
        ] = None,
    ) -> "capo_iottwinmaker.types.create_component_type_response.CreateComponentTypeResponse":
        """<p>Creates a component type.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the component type.</p>
            is_singleton: <p>A Boolean value that specifies whether an entity can have more than one component of this type.</p>
            component_type_id: <p>The ID of the component type.</p>
            description: <p>The description of the component type.</p>
            property_definitions: <p>An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.</p>
            extends_from: <p>Specifies the parent component type to extend.</p>
            functions: <p>An object that maps strings to the functions in the component type. Each string in the mapping must be unique to this object.</p>
            tags: <p>Metadata that you can use to manage the component type.</p>
            property_groups: <p/>
            component_type_name: <p>A friendly name for the component type.</p>
            composite_component_types: <p>This is an object that maps strings to <code>compositeComponentTypes</code> of the <code>componentType</code>. <code>CompositeComponentType</code> is referenced by <code>componentTypeId</code>.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.create_component_type_request.CreateComponentTypeRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.create_component_type_response.CreateComponentTypeResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.create_component_type

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.create_component_type.create_component_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.create_component_type_request.CreateComponentTypeRequest = {
            "workspace_id": workspace_id,
            "component_type_id": component_type_id,
        }
        if is_singleton is not None:
            input_["is_singleton"] = is_singleton
        if description is not None:
            input_["description"] = description
        if property_definitions is not None:
            input_["property_definitions"] = property_definitions
        if extends_from is not None:
            input_["extends_from"] = extends_from
        if functions is not None:
            input_["functions"] = functions
        if tags is not None:
            input_["tags"] = tags
        if property_groups is not None:
            input_["property_groups"] = property_groups
        if component_type_name is not None:
            input_["component_type_name"] = component_type_name
        if composite_component_types is not None:
            input_["composite_component_types"] = composite_component_types

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_entity(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        entity_name: "capo_iottwinmaker.types.entity_name.EntityName",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        entity_id: Optional["capo_iottwinmaker.types.entity_id.EntityId"] = None,
        description: Optional["capo_iottwinmaker.types.description.Description"] = None,
        components: Optional[
            "capo_iottwinmaker.types.components_map_request.ComponentsMapRequest"
        ] = None,
        composite_components: Optional[
            "capo_iottwinmaker.types.composite_components_map_request.CompositeComponentsMapRequest"
        ] = None,
        parent_entity_id: Optional[
            "capo_iottwinmaker.types.parent_entity_id.ParentEntityId"
        ] = None,
        tags: Optional["capo_iottwinmaker.types.tag_map.TagMap"] = None,
    ) -> "capo_iottwinmaker.types.create_entity_response.CreateEntityResponse":
        """<p>Creates an entity.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the entity.</p>
            entity_id: <p>The ID of the entity.</p>
            entity_name: <p>The name of the entity.</p>
            description: <p>The description of the entity.</p>
            components: <p>An object that maps strings to the components in the entity. Each string in the mapping must be unique to this object.</p>
            composite_components: <p>This is an object that maps strings to <code>compositeComponent</code> updates in the request. Each key of the map represents the <code>componentPath</code> of the <code>compositeComponent</code>.</p>
            parent_entity_id: <p>The ID of the entity's parent entity.</p>
            tags: <p>Metadata that you can use to manage the entity.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.create_entity_request.CreateEntityRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.create_entity_response.CreateEntityResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.create_entity

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.create_entity.create_entity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.create_entity_request.CreateEntityRequest = {
            "workspace_id": workspace_id,
            "entity_name": entity_name,
        }
        if entity_id is not None:
            input_["entity_id"] = entity_id
        if description is not None:
            input_["description"] = description
        if components is not None:
            input_["components"] = components
        if composite_components is not None:
            input_["composite_components"] = composite_components
        if parent_entity_id is not None:
            input_["parent_entity_id"] = parent_entity_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_metadata_transfer_job(
        self,
        sources: "capo_iottwinmaker.types.source_configurations.SourceConfigurations",
        destination: "capo_iottwinmaker.types.destination_configuration.DestinationConfiguration",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        metadata_transfer_job_id: Optional["capo_iottwinmaker.types.id.Id"] = None,
        description: Optional["capo_iottwinmaker.types.description.Description"] = None,
    ) -> "capo_iottwinmaker.types.create_metadata_transfer_job_response.CreateMetadataTransferJobResponse":
        """<p>Creates a new metadata transfer job.</p>

        Args:
            metadata_transfer_job_id: <p>The metadata transfer job Id.</p>
            description: <p>The metadata transfer job description.</p>
            sources: <p>The metadata transfer job sources.</p>
            destination: <p>The metadata transfer job destination.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.create_metadata_transfer_job_request.CreateMetadataTransferJobRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.create_metadata_transfer_job_response.CreateMetadataTransferJobResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.create_metadata_transfer_job

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.create_metadata_transfer_job.create_metadata_transfer_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.create_metadata_transfer_job_request.CreateMetadataTransferJobRequest = {
            "sources": sources,
            "destination": destination,
        }
        if metadata_transfer_job_id is not None:
            input_["metadata_transfer_job_id"] = metadata_transfer_job_id
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_scene(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        scene_id: "capo_iottwinmaker.types.id.Id",
        content_location: "capo_iottwinmaker.types.s3_url.S3Url",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        description: Optional["capo_iottwinmaker.types.description.Description"] = None,
        capabilities: Optional[
            "capo_iottwinmaker.types.scene_capabilities.SceneCapabilities"
        ] = None,
        tags: Optional["capo_iottwinmaker.types.tag_map.TagMap"] = None,
        scene_metadata: Optional[
            "capo_iottwinmaker.types.scene_metadata_map.SceneMetadataMap"
        ] = None,
    ) -> "capo_iottwinmaker.types.create_scene_response.CreateSceneResponse":
        """<p>Creates a scene.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the scene.</p>
            scene_id: <p>The ID of the scene.</p>
            content_location: <p>The relative path that specifies the location of the content definition file.</p>
            description: <p>The description for this scene.</p>
            capabilities: <p>A list of capabilities that the scene uses to render itself.</p>
            tags: <p>Metadata that you can use to manage the scene.</p>
            scene_metadata: <p>The request metadata.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.create_scene_request.CreateSceneRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.create_scene_response.CreateSceneResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.create_scene

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.create_scene.create_scene(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.create_scene_request.CreateSceneRequest = {
            "workspace_id": workspace_id,
            "scene_id": scene_id,
            "content_location": content_location,
        }
        if description is not None:
            input_["description"] = description
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if tags is not None:
            input_["tags"] = tags
        if scene_metadata is not None:
            input_["scene_metadata"] = scene_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_sync_job(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        sync_source: "capo_iottwinmaker.types.sync_source.SyncSource",
        sync_role: "capo_iottwinmaker.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        tags: Optional["capo_iottwinmaker.types.tag_map.TagMap"] = None,
    ) -> "capo_iottwinmaker.types.create_sync_job_response.CreateSyncJobResponse":
        """<p>This action creates a SyncJob.</p>

        Args:
            workspace_id: <p>The workspace ID.</p>
            sync_source: <p>The sync source.</p> <note> <p>Currently the only supported syncSoource is <code>SITEWISE </code>.</p> </note>
            sync_role: <p>The SyncJob IAM role. This IAM role is used by the SyncJob to read from the syncSource, and create, update, or delete the corresponding resources.</p>
            tags: <p>The SyncJob tags.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.create_sync_job_request.CreateSyncJobRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.create_sync_job_response.CreateSyncJobResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.create_sync_job

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.create_sync_job.create_sync_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.create_sync_job_request.CreateSyncJobRequest = {
            "workspace_id": workspace_id,
            "sync_source": sync_source,
            "sync_role": sync_role,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_workspace(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        description: Optional["capo_iottwinmaker.types.description.Description"] = None,
        s3_location: Optional["capo_iottwinmaker.types.s3_location.S3Location"] = None,
        role: Optional["capo_iottwinmaker.types.role_arn.RoleArn"] = None,
        tags: Optional["capo_iottwinmaker.types.tag_map.TagMap"] = None,
    ) -> "capo_iottwinmaker.types.create_workspace_response.CreateWorkspaceResponse":
        """<p>Creates a workplace.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            description: <p>The description of the workspace.</p>
            s3_location: <p>The ARN of the S3 bucket where resources associated with the workspace are stored.</p>
            role: <p>The ARN of the execution role associated with the workspace.</p>
            tags: <p>Metadata that you can use to manage the workspace</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.create_workspace_request.CreateWorkspaceRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.create_workspace_response.CreateWorkspaceResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.create_workspace

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.create_workspace.create_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.create_workspace_request.CreateWorkspaceRequest = {
            "workspace_id": workspace_id
        }
        if description is not None:
            input_["description"] = description
        if s3_location is not None:
            input_["s3_location"] = s3_location
        if role is not None:
            input_["role"] = role
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_component_type(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        component_type_id: "capo_iottwinmaker.types.component_type_id.ComponentTypeId",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
    ) -> "capo_iottwinmaker.types.delete_component_type_response.DeleteComponentTypeResponse":
        """<p>Deletes a component type.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the component type.</p>
            component_type_id: <p>The ID of the component type to delete.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.delete_component_type_request.DeleteComponentTypeRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.delete_component_type_response.DeleteComponentTypeResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.delete_component_type

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.delete_component_type.delete_component_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.delete_component_type_request.DeleteComponentTypeRequest = {
            "workspace_id": workspace_id,
            "component_type_id": component_type_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_entity(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        entity_id: "capo_iottwinmaker.types.entity_id.EntityId",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        is_recursive: Optional["capo_iottwinmaker.types.boolean.Boolean"] = None,
    ) -> "capo_iottwinmaker.types.delete_entity_response.DeleteEntityResponse":
        """<p>Deletes an entity.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the entity to delete.</p>
            entity_id: <p>The ID of the entity to delete.</p>
            is_recursive: <p>A Boolean value that specifies whether the operation deletes child entities.</p>

        Raises:
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.delete_entity_request.DeleteEntityRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.delete_entity_response.DeleteEntityResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.delete_entity

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.delete_entity.delete_entity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.delete_entity_request.DeleteEntityRequest = {
            "workspace_id": workspace_id,
            "entity_id": entity_id,
        }
        if is_recursive is not None:
            input_["is_recursive"] = is_recursive

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_scene(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        scene_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
    ) -> "capo_iottwinmaker.types.delete_scene_response.DeleteSceneResponse":
        """<p>Deletes a scene.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            scene_id: <p>The ID of the scene to delete.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.delete_scene_request.DeleteSceneRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.delete_scene_response.DeleteSceneResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.delete_scene

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.delete_scene.delete_scene(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.delete_scene_request.DeleteSceneRequest = {
            "workspace_id": workspace_id,
            "scene_id": scene_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_sync_job(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        sync_source: "capo_iottwinmaker.types.sync_source.SyncSource",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
    ) -> "capo_iottwinmaker.types.delete_sync_job_response.DeleteSyncJobResponse":
        """<p>Delete the SyncJob.</p>

        Args:
            workspace_id: <p>The workspace ID.</p>
            sync_source: <p>The sync source.</p> <note> <p>Currently the only supported syncSource is <code>SITEWISE </code>.</p> </note>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.delete_sync_job_request.DeleteSyncJobRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.delete_sync_job_response.DeleteSyncJobResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.delete_sync_job

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.delete_sync_job.delete_sync_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.delete_sync_job_request.DeleteSyncJobRequest = {
            "workspace_id": workspace_id,
            "sync_source": sync_source,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_workspace(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
    ) -> "capo_iottwinmaker.types.delete_workspace_response.DeleteWorkspaceResponse":
        """<p>Deletes a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to delete.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.delete_workspace_request.DeleteWorkspaceRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.delete_workspace_response.DeleteWorkspaceResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.delete_workspace

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.delete_workspace.delete_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.delete_workspace_request.DeleteWorkspaceRequest = {
            "workspace_id": workspace_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def execute_query(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        query_statement: "capo_iottwinmaker.types.query_statement.QueryStatement",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        max_results: Optional[
            "capo_iottwinmaker.types.query_service_max_results.QueryServiceMaxResults"
        ] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "capo_iottwinmaker.types.execute_query_response.ExecuteQueryResponse":
        """<p>Run queries to access information from your knowledge graph of entities within individual workspaces.</p> <note> <p>The ExecuteQuery action only works with <a href="https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html">Amazon Web Services Java SDK2</a>. ExecuteQuery will not work with any Amazon Web Services Java SDK version &lt; 2.x.</p> </note>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            query_statement: <p>The query statement.</p>
            max_results: <p>The maximum number of results to return at one time. The default is 50.</p>
            next_token: <p>The string that specifies the next page of results.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.query_timeout_exception.QueryTimeoutException: <p>The query timeout exception.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.execute_query_request.ExecuteQueryRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.execute_query_response.ExecuteQueryResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.execute_query

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.execute_query.execute_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.execute_query_request.ExecuteQueryRequest = {
            "workspace_id": workspace_id,
            "query_statement": query_statement,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_execute_query(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        query_statement: "capo_iottwinmaker.types.query_statement.QueryStatement",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        max_results: Optional[
            "capo_iottwinmaker.types.query_service_max_results.QueryServiceMaxResults"
        ] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> (
        "Iterator[capo_iottwinmaker.types.execute_query_response.ExecuteQueryResponse]"
    ):
        _token = next_token
        while True:
            _response = self.execute_query(
                workspace_id,
                query_statement,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_component_type(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        component_type_id: "capo_iottwinmaker.types.component_type_id.ComponentTypeId",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
    ) -> "capo_iottwinmaker.types.get_component_type_response.GetComponentTypeResponse":
        """<p>Retrieves information about a component type.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the component type.</p>
            component_type_id: <p>The ID of the component type.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.get_component_type_request.GetComponentTypeRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.get_component_type_response.GetComponentTypeResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.get_component_type

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.get_component_type.get_component_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.get_component_type_request.GetComponentTypeRequest = {
            "workspace_id": workspace_id,
            "component_type_id": component_type_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_entity(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        entity_id: "capo_iottwinmaker.types.entity_id.EntityId",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
    ) -> "capo_iottwinmaker.types.get_entity_response.GetEntityResponse":
        """<p>Retrieves information about an entity.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            entity_id: <p>The ID of the entity.</p>

        Raises:
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.get_entity_request.GetEntityRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.get_entity_response.GetEntityResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.get_entity

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.get_entity.get_entity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.get_entity_request.GetEntityRequest = {
            "workspace_id": workspace_id,
            "entity_id": entity_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_metadata_transfer_job(
        self,
        metadata_transfer_job_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
    ) -> "capo_iottwinmaker.types.get_metadata_transfer_job_response.GetMetadataTransferJobResponse":
        """<p>Gets a nmetadata transfer job.</p>

        Args:
            metadata_transfer_job_id: <p>The metadata transfer job Id.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.get_metadata_transfer_job_request.GetMetadataTransferJobRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.get_metadata_transfer_job_response.GetMetadataTransferJobResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.get_metadata_transfer_job

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.get_metadata_transfer_job.get_metadata_transfer_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.get_metadata_transfer_job_request.GetMetadataTransferJobRequest = {
            "metadata_transfer_job_id": metadata_transfer_job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_pricing_plan(
        self, *, config_overrides: Optional[IoTTwinMakerClientConfig] = None
    ) -> "capo_iottwinmaker.types.get_pricing_plan_response.GetPricingPlanResponse":
        """<p>Gets the pricing plan.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.get_pricing_plan_request.GetPricingPlanRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.get_pricing_plan_response.GetPricingPlanResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.get_pricing_plan

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.get_pricing_plan.get_pricing_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.get_pricing_plan_request.GetPricingPlanRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_property_value(
        self,
        selected_properties: "capo_iottwinmaker.types.selected_property_list.SelectedPropertyList",
        workspace_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        component_name: Optional["capo_iottwinmaker.types.name.Name"] = None,
        component_path: Optional[
            "capo_iottwinmaker.types.component_path.ComponentPath"
        ] = None,
        component_type_id: Optional[
            "capo_iottwinmaker.types.component_type_id.ComponentTypeId"
        ] = None,
        entity_id: Optional["capo_iottwinmaker.types.entity_id.EntityId"] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
        property_group_name: Optional["capo_iottwinmaker.types.name.Name"] = None,
        tabular_conditions: Optional[
            "capo_iottwinmaker.types.tabular_conditions.TabularConditions"
        ] = None,
    ) -> "capo_iottwinmaker.types.get_property_value_response.GetPropertyValueResponse":
        """<p>Gets the property values for a component, component type, entity, or workspace.</p> <p>You must specify a value for either <code>componentName</code>, <code>componentTypeId</code>, <code>entityId</code>, or <code>workspaceId</code>.</p>

        Args:
            component_name: <p>The name of the component whose property values the operation returns.</p>
            component_path: <p>This string specifies the path to the composite component, starting from the top-level component.</p>
            component_type_id: <p>The ID of the component type whose property values the operation returns.</p>
            entity_id: <p>The ID of the entity whose property values the operation returns.</p>
            selected_properties: <p>The properties whose values the operation returns.</p>
            workspace_id: <p>The ID of the workspace whose values the operation returns.</p>
            max_results: <p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>
            next_token: <p>The string that specifies the next page of results.</p>
            property_group_name: <p>The property group name.</p>
            tabular_conditions: <p>The tabular conditions.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.connector_failure_exception.ConnectorFailureException: <p>The connector failed.</p>
            capo_iottwinmaker.errors.connector_timeout_exception.ConnectorTimeoutException: <p>The connector timed out.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.get_property_value_request.GetPropertyValueRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.get_property_value_response.GetPropertyValueResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.get_property_value

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.get_property_value.get_property_value(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.get_property_value_request.GetPropertyValueRequest = {
            "selected_properties": selected_properties,
            "workspace_id": workspace_id,
        }
        if component_name is not None:
            input_["component_name"] = component_name
        if component_path is not None:
            input_["component_path"] = component_path
        if component_type_id is not None:
            input_["component_type_id"] = component_type_id
        if entity_id is not None:
            input_["entity_id"] = entity_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if property_group_name is not None:
            input_["property_group_name"] = property_group_name
        if tabular_conditions is not None:
            input_["tabular_conditions"] = tabular_conditions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_property_value(
        self,
        selected_properties: "capo_iottwinmaker.types.selected_property_list.SelectedPropertyList",
        workspace_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        component_name: Optional["capo_iottwinmaker.types.name.Name"] = None,
        component_path: Optional[
            "capo_iottwinmaker.types.component_path.ComponentPath"
        ] = None,
        component_type_id: Optional[
            "capo_iottwinmaker.types.component_type_id.ComponentTypeId"
        ] = None,
        entity_id: Optional["capo_iottwinmaker.types.entity_id.EntityId"] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
        property_group_name: Optional["capo_iottwinmaker.types.name.Name"] = None,
        tabular_conditions: Optional[
            "capo_iottwinmaker.types.tabular_conditions.TabularConditions"
        ] = None,
    ) -> "Iterator[capo_iottwinmaker.types.get_property_value_response.GetPropertyValueResponse]":
        _token = next_token
        while True:
            _response = self.get_property_value(
                selected_properties,
                workspace_id,
                config_overrides=config_overrides,
                component_name=component_name,
                component_path=component_path,
                component_type_id=component_type_id,
                entity_id=entity_id,
                max_results=max_results,
                next_token=_token,
                property_group_name=property_group_name,
                tabular_conditions=tabular_conditions,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_property_value_history(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        selected_properties: "capo_iottwinmaker.types.selected_property_list.SelectedPropertyList",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        entity_id: Optional["capo_iottwinmaker.types.entity_id.EntityId"] = None,
        component_name: Optional["capo_iottwinmaker.types.name.Name"] = None,
        component_path: Optional[
            "capo_iottwinmaker.types.component_path.ComponentPath"
        ] = None,
        component_type_id: Optional[
            "capo_iottwinmaker.types.component_type_id.ComponentTypeId"
        ] = None,
        property_filters: Optional[
            "capo_iottwinmaker.types.property_filters.PropertyFilters"
        ] = None,
        start_date_time: Optional["capo_iottwinmaker.types.timestamp.Timestamp"] = None,
        end_date_time: Optional["capo_iottwinmaker.types.timestamp.Timestamp"] = None,
        interpolation: Optional[
            "capo_iottwinmaker.types.interpolation_parameters.InterpolationParameters"
        ] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        order_by_time: Optional[
            "capo_iottwinmaker.types.order_by_time.OrderByTime"
        ] = None,
        start_time: Optional["capo_iottwinmaker.types.time.Time"] = None,
        end_time: Optional["capo_iottwinmaker.types.time.Time"] = None,
    ) -> "capo_iottwinmaker.types.get_property_value_history_response.GetPropertyValueHistoryResponse":
        """<p>Retrieves information about the history of a time series property value for a component, component type, entity, or workspace.</p> <p>You must specify a value for <code>workspaceId</code>. For entity-specific queries, specify values for <code>componentName</code> and <code>entityId</code>. For cross-entity quries, specify a value for <code>componentTypeId</code>.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            entity_id: <p>The ID of the entity.</p>
            component_name: <p>The name of the component.</p>
            component_path: <p>This string specifies the path to the composite component, starting from the top-level component.</p>
            component_type_id: <p>The ID of the component type.</p>
            selected_properties: <p>A list of properties whose value histories the request retrieves.</p>
            property_filters: <p>A list of objects that filter the property value history request.</p>
            start_date_time: <p>The date and time of the earliest property value to return.</p>
            end_date_time: <p>The date and time of the latest property value to return.</p>
            interpolation: <p>An object that specifies the interpolation type and the interval over which to interpolate data.</p>
            next_token: <p>The string that specifies the next page of results.</p>
            max_results: <p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>
            order_by_time: <p>The time direction to use in the result order.</p>
            start_time: <p>The ISO8601 DateTime of the earliest property value to return.</p> <p>For more information about the ISO8601 DateTime format, see the data type <a href="https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertyValue.html">PropertyValue</a>.</p>
            end_time: <p>The ISO8601 DateTime of the latest property value to return.</p> <p>For more information about the ISO8601 DateTime format, see the data type <a href="https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertyValue.html">PropertyValue</a>.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.connector_failure_exception.ConnectorFailureException: <p>The connector failed.</p>
            capo_iottwinmaker.errors.connector_timeout_exception.ConnectorTimeoutException: <p>The connector timed out.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.get_property_value_history_request.GetPropertyValueHistoryRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.get_property_value_history_response.GetPropertyValueHistoryResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.get_property_value_history

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.get_property_value_history.get_property_value_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.get_property_value_history_request.GetPropertyValueHistoryRequest = {
            "workspace_id": workspace_id,
            "selected_properties": selected_properties,
        }
        if entity_id is not None:
            input_["entity_id"] = entity_id
        if component_name is not None:
            input_["component_name"] = component_name
        if component_path is not None:
            input_["component_path"] = component_path
        if component_type_id is not None:
            input_["component_type_id"] = component_type_id
        if property_filters is not None:
            input_["property_filters"] = property_filters
        if start_date_time is not None:
            input_["start_date_time"] = start_date_time
        if end_date_time is not None:
            input_["end_date_time"] = end_date_time
        if interpolation is not None:
            input_["interpolation"] = interpolation
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if order_by_time is not None:
            input_["order_by_time"] = order_by_time
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_property_value_history(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        selected_properties: "capo_iottwinmaker.types.selected_property_list.SelectedPropertyList",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        entity_id: Optional["capo_iottwinmaker.types.entity_id.EntityId"] = None,
        component_name: Optional["capo_iottwinmaker.types.name.Name"] = None,
        component_path: Optional[
            "capo_iottwinmaker.types.component_path.ComponentPath"
        ] = None,
        component_type_id: Optional[
            "capo_iottwinmaker.types.component_type_id.ComponentTypeId"
        ] = None,
        property_filters: Optional[
            "capo_iottwinmaker.types.property_filters.PropertyFilters"
        ] = None,
        start_date_time: Optional["capo_iottwinmaker.types.timestamp.Timestamp"] = None,
        end_date_time: Optional["capo_iottwinmaker.types.timestamp.Timestamp"] = None,
        interpolation: Optional[
            "capo_iottwinmaker.types.interpolation_parameters.InterpolationParameters"
        ] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        order_by_time: Optional[
            "capo_iottwinmaker.types.order_by_time.OrderByTime"
        ] = None,
        start_time: Optional["capo_iottwinmaker.types.time.Time"] = None,
        end_time: Optional["capo_iottwinmaker.types.time.Time"] = None,
    ) -> "Iterator[capo_iottwinmaker.types.get_property_value_history_response.GetPropertyValueHistoryResponse]":
        _token = next_token
        while True:
            _response = self.get_property_value_history(
                workspace_id,
                selected_properties,
                config_overrides=config_overrides,
                entity_id=entity_id,
                component_name=component_name,
                component_path=component_path,
                component_type_id=component_type_id,
                property_filters=property_filters,
                start_date_time=start_date_time,
                end_date_time=end_date_time,
                interpolation=interpolation,
                next_token=_token,
                max_results=max_results,
                order_by_time=order_by_time,
                start_time=start_time,
                end_time=end_time,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_scene(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        scene_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
    ) -> "capo_iottwinmaker.types.get_scene_response.GetSceneResponse":
        """<p>Retrieves information about a scene.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the scene.</p>
            scene_id: <p>The ID of the scene.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.get_scene_request.GetSceneRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.get_scene_response.GetSceneResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.get_scene

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.get_scene.get_scene(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.get_scene_request.GetSceneRequest = {
            "workspace_id": workspace_id,
            "scene_id": scene_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sync_job(
        self,
        sync_source: "capo_iottwinmaker.types.sync_source.SyncSource",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        workspace_id: Optional["capo_iottwinmaker.types.id.Id"] = None,
    ) -> "capo_iottwinmaker.types.get_sync_job_response.GetSyncJobResponse":
        """<p>Gets the SyncJob.</p>

        Args:
            sync_source: <p>The sync source.</p> <note> <p>Currently the only supported syncSource is <code>SITEWISE </code>.</p> </note>
            workspace_id: <p>The workspace ID.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.get_sync_job_request.GetSyncJobRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.get_sync_job_response.GetSyncJobResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.get_sync_job

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.get_sync_job.get_sync_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.get_sync_job_request.GetSyncJobRequest = {
            "sync_source": sync_source
        }
        if workspace_id is not None:
            input_["workspace_id"] = workspace_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workspace(
        self,
        workspace_id: "capo_iottwinmaker.types.id_or_arn.IdOrArn",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
    ) -> "capo_iottwinmaker.types.get_workspace_response.GetWorkspaceResponse":
        """<p>Retrieves information about a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>

        Raises:
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.get_workspace_request.GetWorkspaceRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.get_workspace_response.GetWorkspaceResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.get_workspace

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.get_workspace.get_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.get_workspace_request.GetWorkspaceRequest = {
            "workspace_id": workspace_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_components(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        entity_id: "capo_iottwinmaker.types.entity_id.EntityId",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        component_path: Optional[
            "capo_iottwinmaker.types.component_path.ComponentPath"
        ] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "capo_iottwinmaker.types.list_components_response.ListComponentsResponse":
        """<p>This API lists the components of an entity.</p>

        Args:
            workspace_id: <p>The workspace ID.</p>
            entity_id: <p>The ID for the entity whose metadata (component/properties) is returned by the operation.</p>
            component_path: <p>This string specifies the path to the composite component, starting from the top-level component.</p>
            max_results: <p>The maximum number of results returned at one time. The default is 25.</p>
            next_token: <p>The string that specifies the next page of results.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.list_components_request.ListComponentsRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.list_components_response.ListComponentsResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.list_components

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.list_components.list_components(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.list_components_request.ListComponentsRequest = {
            "workspace_id": workspace_id,
            "entity_id": entity_id,
        }
        if component_path is not None:
            input_["component_path"] = component_path
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_components(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        entity_id: "capo_iottwinmaker.types.entity_id.EntityId",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        component_path: Optional[
            "capo_iottwinmaker.types.component_path.ComponentPath"
        ] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_iottwinmaker.types.list_components_response.ListComponentsResponse]":
        _token = next_token
        while True:
            _response = self.list_components(
                workspace_id,
                entity_id,
                config_overrides=config_overrides,
                component_path=component_path,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_component_types(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        filters: Optional[
            "capo_iottwinmaker.types.list_component_types_filters.ListComponentTypesFilters"
        ] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
    ) -> "capo_iottwinmaker.types.list_component_types_response.ListComponentTypesResponse":
        """<p>Lists all component types in a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            filters: <p>A list of objects that filter the request.</p>
            next_token: <p>The string that specifies the next page of results.</p>
            max_results: <p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.list_component_types_request.ListComponentTypesRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.list_component_types_response.ListComponentTypesResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.list_component_types

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.list_component_types.list_component_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.list_component_types_request.ListComponentTypesRequest = {
            "workspace_id": workspace_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_component_types(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        filters: Optional[
            "capo_iottwinmaker.types.list_component_types_filters.ListComponentTypesFilters"
        ] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_iottwinmaker.types.list_component_types_response.ListComponentTypesResponse]":
        _token = next_token
        while True:
            _response = self.list_component_types(
                workspace_id,
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_entities(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        filters: Optional[
            "capo_iottwinmaker.types.list_entities_filters.ListEntitiesFilters"
        ] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "capo_iottwinmaker.types.list_entities_response.ListEntitiesResponse":
        """<p>Lists all entities in a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            filters: <p>A list of objects that filter the request.</p> <note> <p>Only one object is accepted as a valid input.</p> </note>
            max_results: <p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>
            next_token: <p>The string that specifies the next page of results.</p>

        Raises:
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.list_entities_request.ListEntitiesRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.list_entities_response.ListEntitiesResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.list_entities

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.list_entities.list_entities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.list_entities_request.ListEntitiesRequest = {
            "workspace_id": workspace_id
        }
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_entities(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        filters: Optional[
            "capo_iottwinmaker.types.list_entities_filters.ListEntitiesFilters"
        ] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> (
        "Iterator[capo_iottwinmaker.types.list_entities_response.ListEntitiesResponse]"
    ):
        _token = next_token
        while True:
            _response = self.list_entities(
                workspace_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_metadata_transfer_jobs(
        self,
        source_type: "capo_iottwinmaker.types.source_type.SourceType",
        destination_type: "capo_iottwinmaker.types.destination_type.DestinationType",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        filters: Optional[
            "capo_iottwinmaker.types.list_metadata_transfer_jobs_filters.ListMetadataTransferJobsFilters"
        ] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
    ) -> "capo_iottwinmaker.types.list_metadata_transfer_jobs_response.ListMetadataTransferJobsResponse":
        """<p>Lists the metadata transfer jobs.</p>

        Args:
            source_type: <p>The metadata transfer job's source type.</p>
            destination_type: <p>The metadata transfer job's destination type.</p>
            filters: <p>An object that filters metadata transfer jobs.</p>
            next_token: <p>The string that specifies the next page of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.list_metadata_transfer_jobs_request.ListMetadataTransferJobsRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.list_metadata_transfer_jobs_response.ListMetadataTransferJobsResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.list_metadata_transfer_jobs

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.list_metadata_transfer_jobs.list_metadata_transfer_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.list_metadata_transfer_jobs_request.ListMetadataTransferJobsRequest = {
            "source_type": source_type,
            "destination_type": destination_type,
        }
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_metadata_transfer_jobs(
        self,
        source_type: "capo_iottwinmaker.types.source_type.SourceType",
        destination_type: "capo_iottwinmaker.types.destination_type.DestinationType",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        filters: Optional[
            "capo_iottwinmaker.types.list_metadata_transfer_jobs_filters.ListMetadataTransferJobsFilters"
        ] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_iottwinmaker.types.list_metadata_transfer_jobs_response.ListMetadataTransferJobsResponse]":
        _token = next_token
        while True:
            _response = self.list_metadata_transfer_jobs(
                source_type,
                destination_type,
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_properties(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        entity_id: "capo_iottwinmaker.types.entity_id.EntityId",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        component_name: Optional["capo_iottwinmaker.types.name.Name"] = None,
        component_path: Optional[
            "capo_iottwinmaker.types.component_path.ComponentPath"
        ] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "capo_iottwinmaker.types.list_properties_response.ListPropertiesResponse":
        """<p>This API lists the properties of a component.</p>

        Args:
            workspace_id: <p>The workspace ID.</p>
            component_name: <p>The name of the component whose properties are returned by the operation.</p>
            component_path: <p>This string specifies the path to the composite component, starting from the top-level component.</p>
            entity_id: <p>The ID for the entity whose metadata (component/properties) is returned by the operation.</p>
            max_results: <p>The maximum number of results returned at one time. The default is 25.</p>
            next_token: <p>The string that specifies the next page of results.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.list_properties_request.ListPropertiesRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.list_properties_response.ListPropertiesResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.list_properties

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.list_properties.list_properties(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.list_properties_request.ListPropertiesRequest = {
            "workspace_id": workspace_id,
            "entity_id": entity_id,
        }
        if component_name is not None:
            input_["component_name"] = component_name
        if component_path is not None:
            input_["component_path"] = component_path
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_properties(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        entity_id: "capo_iottwinmaker.types.entity_id.EntityId",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        component_name: Optional["capo_iottwinmaker.types.name.Name"] = None,
        component_path: Optional[
            "capo_iottwinmaker.types.component_path.ComponentPath"
        ] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_iottwinmaker.types.list_properties_response.ListPropertiesResponse]":
        _token = next_token
        while True:
            _response = self.list_properties(
                workspace_id,
                entity_id,
                config_overrides=config_overrides,
                component_name=component_name,
                component_path=component_path,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_scenes(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "capo_iottwinmaker.types.list_scenes_response.ListScenesResponse":
        """<p>Lists all scenes in a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the scenes.</p>
            max_results: <p>Specifies the maximum number of results to display.</p>
            next_token: <p>The string that specifies the next page of results.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.list_scenes_request.ListScenesRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.list_scenes_response.ListScenesResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.list_scenes

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.list_scenes.list_scenes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.list_scenes_request.ListScenesRequest = {
            "workspace_id": workspace_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_scenes(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_iottwinmaker.types.list_scenes_response.ListScenesResponse]":
        _token = next_token
        while True:
            _response = self.list_scenes(
                workspace_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sync_jobs(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "capo_iottwinmaker.types.list_sync_jobs_response.ListSyncJobsResponse":
        """<p>List all SyncJobs.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the sync job.</p>
            max_results: <p>The maximum number of results to return at one time. The default is 50.</p> <p>Valid Range: Minimum value of 0. Maximum value of 200.</p>
            next_token: <p>The string that specifies the next page of results.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.list_sync_jobs_request.ListSyncJobsRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.list_sync_jobs_response.ListSyncJobsResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.list_sync_jobs

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.list_sync_jobs.list_sync_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.list_sync_jobs_request.ListSyncJobsRequest = {
            "workspace_id": workspace_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_sync_jobs(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> (
        "Iterator[capo_iottwinmaker.types.list_sync_jobs_response.ListSyncJobsResponse]"
    ):
        _token = next_token
        while True:
            _response = self.list_sync_jobs(
                workspace_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sync_resources(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        sync_source: "capo_iottwinmaker.types.sync_source.SyncSource",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        filters: Optional[
            "capo_iottwinmaker.types.sync_resource_filters.SyncResourceFilters"
        ] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> (
        "capo_iottwinmaker.types.list_sync_resources_response.ListSyncResourcesResponse"
    ):
        """<p>Lists the sync resources.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the sync job.</p>
            sync_source: <p>The sync source.</p> <note> <p>Currently the only supported syncSource is <code>SITEWISE </code>.</p> </note>
            filters: <p>A list of objects that filter the request.</p> <p>The following filter combinations are supported:</p> <ul> <li> <p>Filter with state</p> </li> <li> <p>Filter with ResourceType and ResourceId</p> </li> <li> <p>Filter with ResourceType and ExternalId</p> </li> </ul>
            max_results: <p>The maximum number of results to return at one time. The default is 50.</p> <p>Valid Range: Minimum value of 0. Maximum value of 200.</p>
            next_token: <p>The string that specifies the next page of results.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.list_sync_resources_request.ListSyncResourcesRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.list_sync_resources_response.ListSyncResourcesResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.list_sync_resources

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.list_sync_resources.list_sync_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.list_sync_resources_request.ListSyncResourcesRequest = {
            "workspace_id": workspace_id,
            "sync_source": sync_source,
        }
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_sync_resources(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        sync_source: "capo_iottwinmaker.types.sync_source.SyncSource",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        filters: Optional[
            "capo_iottwinmaker.types.sync_resource_filters.SyncResourceFilters"
        ] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_iottwinmaker.types.list_sync_resources_response.ListSyncResourcesResponse]":
        _token = next_token
        while True:
            _response = self.list_sync_resources(
                workspace_id,
                sync_source,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "capo_iottwinmaker.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags associated with a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            max_results: <p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>
            next_token: <p>The string that specifies the next page of results.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.list_tags_for_resource

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_workspaces(
        self,
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "capo_iottwinmaker.types.list_workspaces_response.ListWorkspacesResponse":
        """<p>Retrieves information about workspaces in the current account.</p>

        Args:
            max_results: <p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>
            next_token: <p>The string that specifies the next page of results.</p>

        Raises:
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.list_workspaces_request.ListWorkspacesRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.list_workspaces_response.ListWorkspacesResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.list_workspaces

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.list_workspaces.list_workspaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.list_workspaces_request.ListWorkspacesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_workspaces(
        self,
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        max_results: Optional["capo_iottwinmaker.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iottwinmaker.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_iottwinmaker.types.list_workspaces_response.ListWorkspacesResponse]":
        _token = next_token
        while True:
            _response = self.list_workspaces(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def tag_resource(
        self,
        resource_arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn",
        tags: "capo_iottwinmaker.types.tag_map.TagMap",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
    ) -> "capo_iottwinmaker.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>Metadata to add to this resource.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.too_many_tags_exception.TooManyTagsException: <p>The number of tags exceeds the limit.</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.tag_resource

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn",
        tag_keys: "capo_iottwinmaker.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
    ) -> "capo_iottwinmaker.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>A list of tag key names to remove from the resource. You don't specify the value. Both the key and its associated value are removed.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.untag_resource

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.untag_resource_request.UntagResourceRequest = {
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

    def update_component_type(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        component_type_id: "capo_iottwinmaker.types.component_type_id.ComponentTypeId",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        is_singleton: Optional["capo_iottwinmaker.types.boolean.Boolean"] = None,
        description: Optional["capo_iottwinmaker.types.description.Description"] = None,
        property_definitions: Optional[
            "capo_iottwinmaker.types.property_definitions_request.PropertyDefinitionsRequest"
        ] = None,
        extends_from: Optional[
            "capo_iottwinmaker.types.extends_from.ExtendsFrom"
        ] = None,
        functions: Optional[
            "capo_iottwinmaker.types.functions_request.FunctionsRequest"
        ] = None,
        property_groups: Optional[
            "capo_iottwinmaker.types.property_groups_request.PropertyGroupsRequest"
        ] = None,
        component_type_name: Optional[
            "capo_iottwinmaker.types.component_type_name.ComponentTypeName"
        ] = None,
        composite_component_types: Optional[
            "capo_iottwinmaker.types.composite_component_types_request.CompositeComponentTypesRequest"
        ] = None,
    ) -> "capo_iottwinmaker.types.update_component_type_response.UpdateComponentTypeResponse":
        """<p>Updates information in a component type.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            is_singleton: <p>A Boolean value that specifies whether an entity can have more than one component of this type.</p>
            component_type_id: <p>The ID of the component type.</p>
            description: <p>The description of the component type.</p>
            property_definitions: <p>An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.</p>
            extends_from: <p>Specifies the component type that this component type extends.</p>
            functions: <p>An object that maps strings to the functions in the component type. Each string in the mapping must be unique to this object.</p>
            property_groups: <p>The property groups.</p>
            component_type_name: <p>The component type name.</p>
            composite_component_types: <p>This is an object that maps strings to <code>compositeComponentTypes</code> of the <code>componentType</code>. <code>CompositeComponentType</code> is referenced by <code>componentTypeId</code>.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.update_component_type_request.UpdateComponentTypeRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.update_component_type_response.UpdateComponentTypeResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.update_component_type

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.update_component_type.update_component_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.update_component_type_request.UpdateComponentTypeRequest = {
            "workspace_id": workspace_id,
            "component_type_id": component_type_id,
        }
        if is_singleton is not None:
            input_["is_singleton"] = is_singleton
        if description is not None:
            input_["description"] = description
        if property_definitions is not None:
            input_["property_definitions"] = property_definitions
        if extends_from is not None:
            input_["extends_from"] = extends_from
        if functions is not None:
            input_["functions"] = functions
        if property_groups is not None:
            input_["property_groups"] = property_groups
        if component_type_name is not None:
            input_["component_type_name"] = component_type_name
        if composite_component_types is not None:
            input_["composite_component_types"] = composite_component_types

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_entity(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        entity_id: "capo_iottwinmaker.types.entity_id.EntityId",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        entity_name: Optional["capo_iottwinmaker.types.entity_name.EntityName"] = None,
        description: Optional["capo_iottwinmaker.types.description.Description"] = None,
        component_updates: Optional[
            "capo_iottwinmaker.types.component_updates_map_request.ComponentUpdatesMapRequest"
        ] = None,
        composite_component_updates: Optional[
            "capo_iottwinmaker.types.composite_component_updates_map_request.CompositeComponentUpdatesMapRequest"
        ] = None,
        parent_entity_update: Optional[
            "capo_iottwinmaker.types.parent_entity_update_request.ParentEntityUpdateRequest"
        ] = None,
    ) -> "capo_iottwinmaker.types.update_entity_response.UpdateEntityResponse":
        """<p>Updates an entity.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the entity.</p>
            entity_id: <p>The ID of the entity.</p>
            entity_name: <p>The name of the entity.</p>
            description: <p>The description of the entity.</p>
            component_updates: <p>An object that maps strings to the component updates in the request. Each string in the mapping must be unique to this object.</p>
            composite_component_updates: <p>This is an object that maps strings to <code>compositeComponent</code> updates in the request. Each key of the map represents the <code>componentPath</code> of the <code>compositeComponent</code>.</p>
            parent_entity_update: <p>An object that describes the update request for a parent entity.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.update_entity_request.UpdateEntityRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.update_entity_response.UpdateEntityResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.update_entity

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.update_entity.update_entity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.update_entity_request.UpdateEntityRequest = {
            "workspace_id": workspace_id,
            "entity_id": entity_id,
        }
        if entity_name is not None:
            input_["entity_name"] = entity_name
        if description is not None:
            input_["description"] = description
        if component_updates is not None:
            input_["component_updates"] = component_updates
        if composite_component_updates is not None:
            input_["composite_component_updates"] = composite_component_updates
        if parent_entity_update is not None:
            input_["parent_entity_update"] = parent_entity_update

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_pricing_plan(
        self,
        pricing_mode: "capo_iottwinmaker.types.pricing_mode.PricingMode",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        bundle_names: Optional[
            "capo_iottwinmaker.types.pricing_bundles.PricingBundles"
        ] = None,
    ) -> (
        "capo_iottwinmaker.types.update_pricing_plan_response.UpdatePricingPlanResponse"
    ):
        """<p>Update the pricing plan.</p>

        Args:
            pricing_mode: <p>The pricing mode.</p>
            bundle_names: <p>The bundle names.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.update_pricing_plan_request.UpdatePricingPlanRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.update_pricing_plan_response.UpdatePricingPlanResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.update_pricing_plan

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.update_pricing_plan.update_pricing_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.update_pricing_plan_request.UpdatePricingPlanRequest = {
            "pricing_mode": pricing_mode
        }
        if bundle_names is not None:
            input_["bundle_names"] = bundle_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_scene(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        scene_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        content_location: Optional["capo_iottwinmaker.types.s3_url.S3Url"] = None,
        description: Optional["capo_iottwinmaker.types.description.Description"] = None,
        capabilities: Optional[
            "capo_iottwinmaker.types.scene_capabilities.SceneCapabilities"
        ] = None,
        scene_metadata: Optional[
            "capo_iottwinmaker.types.scene_metadata_map.SceneMetadataMap"
        ] = None,
    ) -> "capo_iottwinmaker.types.update_scene_response.UpdateSceneResponse":
        """<p>Updates a scene.</p>

        Args:
            workspace_id: <p>The ID of the workspace that contains the scene.</p>
            scene_id: <p>The ID of the scene.</p>
            content_location: <p>The relative path that specifies the location of the content definition file.</p>
            description: <p>The description of this scene.</p>
            capabilities: <p>A list of capabilities that the scene uses to render.</p>
            scene_metadata: <p>The scene metadata.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.update_scene_request.UpdateSceneRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.update_scene_response.UpdateSceneResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.update_scene

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.update_scene.update_scene(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.update_scene_request.UpdateSceneRequest = {
            "workspace_id": workspace_id,
            "scene_id": scene_id,
        }
        if content_location is not None:
            input_["content_location"] = content_location
        if description is not None:
            input_["description"] = description
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if scene_metadata is not None:
            input_["scene_metadata"] = scene_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_workspace(
        self,
        workspace_id: "capo_iottwinmaker.types.id.Id",
        *,
        config_overrides: Optional[IoTTwinMakerClientConfig] = None,
        description: Optional["capo_iottwinmaker.types.description.Description"] = None,
        role: Optional["capo_iottwinmaker.types.role_arn.RoleArn"] = None,
        s3_location: Optional["capo_iottwinmaker.types.s3_location.S3Location"] = None,
    ) -> "capo_iottwinmaker.types.update_workspace_response.UpdateWorkspaceResponse":
        """<p>Updates a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace.</p>
            description: <p>The description of the workspace.</p>
            role: <p>The ARN of the execution role associated with the workspace.</p>
            s3_location: <p>The ARN of the S3 bucket where resources associated with the workspace are stored.</p>

        Raises:
            capo_iottwinmaker.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iottwinmaker.errors.internal_server_exception.InternalServerException: <p>An unexpected error has occurred.</p>
            capo_iottwinmaker.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iottwinmaker.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota was exceeded.</p>
            capo_iottwinmaker.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iottwinmaker.errors.validation_exception.ValidationException: <p>Failed</p>
            capo_iottwinmaker.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iottwinmaker.types.update_workspace_request.UpdateWorkspaceRequest]",
        ) -> OperationResponse[
            "capo_iottwinmaker.types.update_workspace_response.UpdateWorkspaceResponse"
        ]:
            import capo_iottwinmaker._operations.aws_io_t_twin_maker.update_workspace

            output, http_response = (
                capo_iottwinmaker._operations.aws_io_t_twin_maker.update_workspace.update_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iottwinmaker.types.update_workspace_request.UpdateWorkspaceRequest = {
            "workspace_id": workspace_id
        }
        if description is not None:
            input_["description"] = description
        if role is not None:
            input_["role"] = role
        if s3_location is not None:
            input_["s3_location"] = s3_location

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
