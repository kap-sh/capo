"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AmazonBedrockKeystoneBuildTimeService``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_bedrock_data_automation._auth._signers
import capo_bedrock_data_automation._auth._sigv4
from capo_bedrock_data_automation._auth._identity import Credentials
from capo_bedrock_data_automation._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_bedrock_data_automation._auth._zapros_handler import AuthMiddleware
from capo_bedrock_data_automation._pagination import resolve_path as _resolve_path
from capo_bedrock_data_automation._resources.amazon_bedrock_keystone_build_time_service.blueprint_optimization_job_resource import (
    AsyncBlueprintOptimizationJobResource,
)
from capo_bedrock_data_automation._resources.amazon_bedrock_keystone_build_time_service.blueprint_resource import (
    AsyncBlueprintResource,
)
from capo_bedrock_data_automation._resources.amazon_bedrock_keystone_build_time_service.data_automation_library_ingestion_job_resource import (
    AsyncDataAutomationLibraryIngestionJobResource,
)
from capo_bedrock_data_automation._resources.amazon_bedrock_keystone_build_time_service.data_automation_library_resource import (
    AsyncDataAutomationLibraryResource,
)
from capo_bedrock_data_automation._resources.amazon_bedrock_keystone_build_time_service.data_automation_project_resource import (
    AsyncDataAutomationProjectResource,
)
from capo_bedrock_data_automation._services._aws_config import aaws_config
from capo_bedrock_data_automation._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_arn
    import capo_bedrock_data_automation.types.blueprint_filter
    import capo_bedrock_data_automation.types.blueprint_name
    import capo_bedrock_data_automation.types.blueprint_optimization_invocation_arn
    import capo_bedrock_data_automation.types.blueprint_optimization_object
    import capo_bedrock_data_automation.types.blueprint_optimization_output_configuration
    import capo_bedrock_data_automation.types.blueprint_optimization_samples
    import capo_bedrock_data_automation.types.blueprint_schema
    import capo_bedrock_data_automation.types.blueprint_stage
    import capo_bedrock_data_automation.types.blueprint_stage_filter
    import capo_bedrock_data_automation.types.blueprint_summary
    import capo_bedrock_data_automation.types.blueprint_version
    import capo_bedrock_data_automation.types.client_token
    import capo_bedrock_data_automation.types.copy_blueprint_stage_request
    import capo_bedrock_data_automation.types.copy_blueprint_stage_response
    import capo_bedrock_data_automation.types.create_blueprint_request
    import capo_bedrock_data_automation.types.create_blueprint_response
    import capo_bedrock_data_automation.types.create_blueprint_version_request
    import capo_bedrock_data_automation.types.create_blueprint_version_response
    import capo_bedrock_data_automation.types.create_data_automation_library_request
    import capo_bedrock_data_automation.types.create_data_automation_library_response
    import capo_bedrock_data_automation.types.create_data_automation_project_request
    import capo_bedrock_data_automation.types.create_data_automation_project_response
    import capo_bedrock_data_automation.types.custom_output_configuration
    import capo_bedrock_data_automation.types.data_automation_library_arn
    import capo_bedrock_data_automation.types.data_automation_library_configuration
    import capo_bedrock_data_automation.types.data_automation_library_description
    import capo_bedrock_data_automation.types.data_automation_library_entity_summary
    import capo_bedrock_data_automation.types.data_automation_library_filter
    import capo_bedrock_data_automation.types.data_automation_library_ingestion_job_arn
    import capo_bedrock_data_automation.types.data_automation_library_ingestion_job_summary
    import capo_bedrock_data_automation.types.data_automation_library_name
    import capo_bedrock_data_automation.types.data_automation_library_summary
    import capo_bedrock_data_automation.types.data_automation_profile_arn
    import capo_bedrock_data_automation.types.data_automation_project_arn
    import capo_bedrock_data_automation.types.data_automation_project_description
    import capo_bedrock_data_automation.types.data_automation_project_filter
    import capo_bedrock_data_automation.types.data_automation_project_name
    import capo_bedrock_data_automation.types.data_automation_project_stage
    import capo_bedrock_data_automation.types.data_automation_project_stage_filter
    import capo_bedrock_data_automation.types.data_automation_project_summary
    import capo_bedrock_data_automation.types.data_automation_project_type
    import capo_bedrock_data_automation.types.delete_blueprint_request
    import capo_bedrock_data_automation.types.delete_blueprint_response
    import capo_bedrock_data_automation.types.delete_data_automation_library_request
    import capo_bedrock_data_automation.types.delete_data_automation_library_response
    import capo_bedrock_data_automation.types.delete_data_automation_project_request
    import capo_bedrock_data_automation.types.delete_data_automation_project_response
    import capo_bedrock_data_automation.types.encryption_configuration
    import capo_bedrock_data_automation.types.entity_id
    import capo_bedrock_data_automation.types.entity_type
    import capo_bedrock_data_automation.types.get_blueprint_optimization_status_request
    import capo_bedrock_data_automation.types.get_blueprint_optimization_status_response
    import capo_bedrock_data_automation.types.get_blueprint_request
    import capo_bedrock_data_automation.types.get_blueprint_response
    import capo_bedrock_data_automation.types.get_data_automation_library_entity_request
    import capo_bedrock_data_automation.types.get_data_automation_library_entity_response
    import capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_request
    import capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_response
    import capo_bedrock_data_automation.types.get_data_automation_library_request
    import capo_bedrock_data_automation.types.get_data_automation_library_response
    import capo_bedrock_data_automation.types.get_data_automation_project_request
    import capo_bedrock_data_automation.types.get_data_automation_project_response
    import capo_bedrock_data_automation.types.input_configuration
    import capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_request
    import capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_response
    import capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request
    import capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_response
    import capo_bedrock_data_automation.types.library_ingestion_job_operation_type
    import capo_bedrock_data_automation.types.list_blueprints_request
    import capo_bedrock_data_automation.types.list_blueprints_response
    import capo_bedrock_data_automation.types.list_data_automation_libraries_request
    import capo_bedrock_data_automation.types.list_data_automation_libraries_response
    import capo_bedrock_data_automation.types.list_data_automation_library_entities_request
    import capo_bedrock_data_automation.types.list_data_automation_library_entities_response
    import capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_request
    import capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_response
    import capo_bedrock_data_automation.types.list_data_automation_projects_request
    import capo_bedrock_data_automation.types.list_data_automation_projects_response
    import capo_bedrock_data_automation.types.list_tags_for_resource_request
    import capo_bedrock_data_automation.types.list_tags_for_resource_response
    import capo_bedrock_data_automation.types.max_results
    import capo_bedrock_data_automation.types.next_token
    import capo_bedrock_data_automation.types.notification_configuration
    import capo_bedrock_data_automation.types.output_configuration
    import capo_bedrock_data_automation.types.override_configuration
    import capo_bedrock_data_automation.types.resource_owner
    import capo_bedrock_data_automation.types.standard_output_configuration
    import capo_bedrock_data_automation.types.tag_key_list
    import capo_bedrock_data_automation.types.tag_list
    import capo_bedrock_data_automation.types.tag_resource_request
    import capo_bedrock_data_automation.types.tag_resource_response
    import capo_bedrock_data_automation.types.taggable_resource_arn
    import capo_bedrock_data_automation.types.type
    import capo_bedrock_data_automation.types.untag_resource_request
    import capo_bedrock_data_automation.types.untag_resource_response
    import capo_bedrock_data_automation.types.update_blueprint_request
    import capo_bedrock_data_automation.types.update_blueprint_response
    import capo_bedrock_data_automation.types.update_data_automation_library_request
    import capo_bedrock_data_automation.types.update_data_automation_library_response
    import capo_bedrock_data_automation.types.update_data_automation_project_request
    import capo_bedrock_data_automation.types.update_data_automation_project_response


class AsyncBedrockDataAutomationClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncBedrockDataAutomationClient:
    """A client for the ``BedrockDataAutomation`` service.

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
        self._config = AsyncBedrockDataAutomationClientConfig(
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
        self.blueprint_optimization_job_resource = (
            AsyncBlueprintOptimizationJobResource(self)
        )
        self.blueprint_resource = AsyncBlueprintResource(self)
        self.data_automation_library_ingestion_job_resource = (
            AsyncDataAutomationLibraryIngestionJobResource(self)
        )
        self.data_automation_library_resource = AsyncDataAutomationLibraryResource(self)
        self.data_automation_project_resource = AsyncDataAutomationProjectResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBedrockDataAutomationClientConfig = config_overrides or {}
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

    async def copy_blueprint_stage(
        self,
        blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        source_stage: "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage",
        target_stage: "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.copy_blueprint_stage_response.CopyBlueprintStageResponse":
        """Copies a Blueprint from one stage to another

        Args:
            blueprint_arn: Blueprint to be copied
            source_stage: Source stage to copy from
            target_stage: Target stage to copy to
            client_token: Client token for idempotency

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.copy_blueprint_stage_request.CopyBlueprintStageRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.copy_blueprint_stage_response.CopyBlueprintStageResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.copy_blueprint_stage

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.copy_blueprint_stage.async_copy_blueprint_stage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.copy_blueprint_stage_request.CopyBlueprintStageRequest = {
            "blueprint_arn": blueprint_arn,
            "source_stage": source_stage,
            "target_stage": target_stage,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_blueprint_version(
        self,
        blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.create_blueprint_version_response.CreateBlueprintVersionResponse":
        """Creates a new version of an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.create_blueprint_version_request.CreateBlueprintVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.create_blueprint_version_response.CreateBlueprintVersionResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_blueprint_version

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_blueprint_version.async_create_blueprint_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.create_blueprint_version_request.CreateBlueprintVersionRequest = {
            "blueprint_arn": blueprint_arn
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_automation_library_entity(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        entity_type: "capo_bedrock_data_automation.types.entity_type.EntityType",
        entity_id: "capo_bedrock_data_automation.types.entity_id.EntityId",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.get_data_automation_library_entity_response.GetDataAutomationLibraryEntityResponse":
        """Gets an existing entity based on entity type from the library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            entity_type: The entity type for which the entity is requested
            entity_id: Unique identifier for the entity

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.get_data_automation_library_entity_request.GetDataAutomationLibraryEntityRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.get_data_automation_library_entity_response.GetDataAutomationLibraryEntityResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library_entity

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library_entity.async_get_data_automation_library_entity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.get_data_automation_library_entity_request.GetDataAutomationLibraryEntityRequest = {
            "library_arn": library_arn,
            "entity_type": entity_type,
            "entity_id": entity_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_automation_library_entities(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        entity_type: "capo_bedrock_data_automation.types.entity_type.EntityType",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.list_data_automation_library_entities_response.ListDataAutomationLibraryEntitiesResponse":
        """Lists all stored entities in the library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            entity_type: The entity type for which the entity list is requested
            next_token: Pagination token for retrieving the next set of results

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.list_data_automation_library_entities_request.ListDataAutomationLibraryEntitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.list_data_automation_library_entities_response.ListDataAutomationLibraryEntitiesResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_library_entities

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_library_entities.async_list_data_automation_library_entities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.list_data_automation_library_entities_request.ListDataAutomationLibraryEntitiesRequest = {
            "library_arn": library_arn,
            "entity_type": entity_type,
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

    async def iter_list_data_automation_library_entities(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        entity_type: "capo_bedrock_data_automation.types.entity_type.EntityType",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock_data_automation.types.data_automation_library_entity_summary.DataAutomationLibraryEntitySummary]":
        _token = next_token
        while True:
            _response = await self.list_data_automation_library_entities(
                library_arn,
                entity_type,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_bedrock_data_automation.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """List tags for an Amazon Bedrock Data Automation resource

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_bedrock_data_automation.types.taggable_resource_arn.TaggableResourceArn",
        tags: "capo_bedrock_data_automation.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.tag_resource_response.TagResourceResponse":
        """Tag an Amazon Bedrock Data Automation resource

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_bedrock_data_automation.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "capo_bedrock_data_automation.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.untag_resource_response.UntagResourceResponse":
        """Untag an Amazon Bedrock Data Automation resource

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.untag_resource_request.UntagResourceRequest = {
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

    async def invoke_blueprint_optimization_async(
        self,
        blueprint: "capo_bedrock_data_automation.types.blueprint_optimization_object.BlueprintOptimizationObject",
        samples: "capo_bedrock_data_automation.types.blueprint_optimization_samples.BlueprintOptimizationSamples",
        output_configuration: "capo_bedrock_data_automation.types.blueprint_optimization_output_configuration.BlueprintOptimizationOutputConfiguration",
        data_automation_profile_arn: "capo_bedrock_data_automation.types.data_automation_profile_arn.DataAutomationProfileArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_response.InvokeBlueprintOptimizationAsyncResponse":
        """Invoke an async job to perform Blueprint Optimization

        Args:
            blueprint: Blueprint to be optimized
            samples: List of Blueprint Optimization Samples
            output_configuration: Output configuration where the results should be placed
            data_automation_profile_arn: Data automation profile ARN
            encryption_configuration: Encryption configuration.
            tags: List of tags.

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_request.InvokeBlueprintOptimizationAsyncRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_response.InvokeBlueprintOptimizationAsyncResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_blueprint_optimization_async

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_blueprint_optimization_async.async_invoke_blueprint_optimization_async(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.invoke_blueprint_optimization_async_request.InvokeBlueprintOptimizationAsyncRequest = {
            "blueprint": blueprint,
            "samples": samples,
            "output_configuration": output_configuration,
            "data_automation_profile_arn": data_automation_profile_arn,
        }
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_blueprint_optimization_status(
        self,
        invocation_arn: "capo_bedrock_data_automation.types.blueprint_optimization_invocation_arn.BlueprintOptimizationInvocationArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.get_blueprint_optimization_status_response.GetBlueprintOptimizationStatusResponse":
        """API used to get blueprint optimization status.

        Args:
            invocation_arn: Invocation arn.

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.get_blueprint_optimization_status_request.GetBlueprintOptimizationStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.get_blueprint_optimization_status_response.GetBlueprintOptimizationStatusResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint_optimization_status

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint_optimization_status.async_get_blueprint_optimization_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.get_blueprint_optimization_status_request.GetBlueprintOptimizationStatusRequest = {
            "invocation_arn": invocation_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_blueprint(
        self,
        blueprint_name: "capo_bedrock_data_automation.types.blueprint_name.BlueprintName",
        type: "capo_bedrock_data_automation.types.type.Type",
        schema: "capo_bedrock_data_automation.types.blueprint_schema.BlueprintSchema",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        blueprint_stage: Optional[
            "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.create_blueprint_response.CreateBlueprintResponse":
        """Creates an Amazon Bedrock Data Automation Blueprint

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.create_blueprint_request.CreateBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.create_blueprint_response.CreateBlueprintResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_blueprint

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_blueprint.async_create_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.create_blueprint_request.CreateBlueprintRequest = {
            "blueprint_name": blueprint_name,
            "type": type,
            "schema": schema,
        }
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_blueprint(
        self,
        blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        blueprint_version: Optional[
            "capo_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
        ] = None,
        blueprint_stage: Optional[
            "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
    ) -> (
        "capo_bedrock_data_automation.types.get_blueprint_response.GetBlueprintResponse"
    ):
        """Gets an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created
            blueprint_version: Optional field to get a specific Blueprint version
            blueprint_stage: Optional field to get a specific Blueprint stage

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.get_blueprint_request.GetBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.get_blueprint_response.GetBlueprintResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint.async_get_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.get_blueprint_request.GetBlueprintRequest = {
            "blueprint_arn": blueprint_arn
        }
        if blueprint_version is not None:
            input_["blueprint_version"] = blueprint_version
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_blueprint(
        self,
        blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        schema: "capo_bedrock_data_automation.types.blueprint_schema.BlueprintSchema",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        blueprint_stage: Optional[
            "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.update_blueprint_response.UpdateBlueprintResponse":
        """Updates an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.update_blueprint_request.UpdateBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.update_blueprint_response.UpdateBlueprintResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_blueprint

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_blueprint.async_update_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.update_blueprint_request.UpdateBlueprintRequest = {
            "blueprint_arn": blueprint_arn,
            "schema": schema,
        }
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_blueprint(
        self,
        blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        blueprint_version: Optional[
            "capo_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.delete_blueprint_response.DeleteBlueprintResponse":
        """Deletes an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created
            blueprint_version: Optional field to delete a specific Blueprint version

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.delete_blueprint_request.DeleteBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.delete_blueprint_response.DeleteBlueprintResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_blueprint

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_blueprint.async_delete_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.delete_blueprint_request.DeleteBlueprintRequest = {
            "blueprint_arn": blueprint_arn
        }
        if blueprint_version is not None:
            input_["blueprint_version"] = blueprint_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_blueprints(
        self,
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        blueprint_arn: Optional[
            "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
        ] = None,
        resource_owner: Optional[
            "capo_bedrock_data_automation.types.resource_owner.ResourceOwner"
        ] = None,
        blueprint_stage_filter: Optional[
            "capo_bedrock_data_automation.types.blueprint_stage_filter.BlueprintStageFilter"
        ] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
        project_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_filter.DataAutomationProjectFilter"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.list_blueprints_response.ListBlueprintsResponse":
        """Lists all existing Amazon Bedrock Data Automation Blueprints

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.list_blueprints_request.ListBlueprintsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.list_blueprints_response.ListBlueprintsResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_blueprints

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_blueprints.async_list_blueprints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.list_blueprints_request.ListBlueprintsRequest = {}
        if blueprint_arn is not None:
            input_["blueprint_arn"] = blueprint_arn
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner
        if blueprint_stage_filter is not None:
            input_["blueprint_stage_filter"] = blueprint_stage_filter
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if project_filter is not None:
            input_["project_filter"] = project_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_blueprints(
        self,
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        blueprint_arn: Optional[
            "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
        ] = None,
        resource_owner: Optional[
            "capo_bedrock_data_automation.types.resource_owner.ResourceOwner"
        ] = None,
        blueprint_stage_filter: Optional[
            "capo_bedrock_data_automation.types.blueprint_stage_filter.BlueprintStageFilter"
        ] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
        project_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_filter.DataAutomationProjectFilter"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock_data_automation.types.blueprint_summary.BlueprintSummary]":
        _token = next_token
        while True:
            _response = await self.list_blueprints(
                config_overrides=config_overrides,
                blueprint_arn=blueprint_arn,
                resource_owner=resource_owner,
                blueprint_stage_filter=blueprint_stage_filter,
                max_results=max_results,
                next_token=_token,
                project_filter=project_filter,
            )
            _page = _resolve_path(_response, ("blueprints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def invoke_data_automation_library_ingestion_job(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        input_configuration: "capo_bedrock_data_automation.types.input_configuration.InputConfiguration",
        entity_type: "capo_bedrock_data_automation.types.entity_type.EntityType",
        operation_type: "capo_bedrock_data_automation.types.library_ingestion_job_operation_type.LibraryIngestionJobOperationType",
        output_configuration: "capo_bedrock_data_automation.types.output_configuration.OutputConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        notification_configuration: Optional[
            "capo_bedrock_data_automation.types.notification_configuration.NotificationConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_response.InvokeDataAutomationLibraryIngestionJobResponse":
        """Async API: Invoke data automation library ingestion job

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            client_token: Idempotency token
            input_configuration: Input configuration of DataAutomationLibraryIngestionJob request
            entity_type: The entity type for which DataAutomationLibraryIngestionJob is being run
            operation_type: The operation to be performed by DataAutomationLibraryIngestionJob
            output_configuration: Output configuration of DataAutomationLibraryIngestionJob
            notification_configuration: Notification configuration.
            tags: List of tags

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request.InvokeDataAutomationLibraryIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_response.InvokeDataAutomationLibraryIngestionJobResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_data_automation_library_ingestion_job

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_data_automation_library_ingestion_job.async_invoke_data_automation_library_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request.InvokeDataAutomationLibraryIngestionJobRequest = {
            "library_arn": library_arn,
            "input_configuration": input_configuration,
            "entity_type": entity_type,
            "operation_type": operation_type,
            "output_configuration": output_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if notification_configuration is not None:
            input_["notification_configuration"] = notification_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_automation_library_ingestion_job(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        job_arn: "capo_bedrock_data_automation.types.data_automation_library_ingestion_job_arn.DataAutomationLibraryIngestionJobArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_response.GetDataAutomationLibraryIngestionJobResponse":
        """API used to get status of data automation library ingestion job

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            job_arn: ARN of the DataAutomationLibraryIngestionJob

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_request.GetDataAutomationLibraryIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_response.GetDataAutomationLibraryIngestionJobResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library_ingestion_job

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library_ingestion_job.async_get_data_automation_library_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_request.GetDataAutomationLibraryIngestionJobRequest = {
            "library_arn": library_arn,
            "job_arn": job_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_automation_library_ingestion_jobs(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_response.ListDataAutomationLibraryIngestionJobsResponse":
        """Lists all data automation library ingestion jobs

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            next_token: Pagination token for retrieving the next set of results

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_request.ListDataAutomationLibraryIngestionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_response.ListDataAutomationLibraryIngestionJobsResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_library_ingestion_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_library_ingestion_jobs.async_list_data_automation_library_ingestion_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_request.ListDataAutomationLibraryIngestionJobsRequest = {
            "library_arn": library_arn
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

    async def iter_list_data_automation_library_ingestion_jobs(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock_data_automation.types.data_automation_library_ingestion_job_summary.DataAutomationLibraryIngestionJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_data_automation_library_ingestion_jobs(
                library_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_data_automation_library(
        self,
        library_name: "capo_bedrock_data_automation.types.data_automation_library_name.DataAutomationLibraryName",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        library_description: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.create_data_automation_library_response.CreateDataAutomationLibraryResponse":
        """Creates an Amazon Bedrock Data Automation Library

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.create_data_automation_library_request.CreateDataAutomationLibraryRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.create_data_automation_library_response.CreateDataAutomationLibraryResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_library

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_library.async_create_data_automation_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.create_data_automation_library_request.CreateDataAutomationLibraryRequest = {
            "library_name": library_name
        }
        if library_description is not None:
            input_["library_description"] = library_description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_automation_library(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.get_data_automation_library_response.GetDataAutomationLibraryResponse":
        """Gets an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.get_data_automation_library_request.GetDataAutomationLibraryRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.get_data_automation_library_response.GetDataAutomationLibraryResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library.async_get_data_automation_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.get_data_automation_library_request.GetDataAutomationLibraryRequest = {
            "library_arn": library_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_data_automation_library(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        library_description: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.update_data_automation_library_response.UpdateDataAutomationLibraryResponse":
        """Updates an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.update_data_automation_library_request.UpdateDataAutomationLibraryRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.update_data_automation_library_response.UpdateDataAutomationLibraryResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_library

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_library.async_update_data_automation_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.update_data_automation_library_request.UpdateDataAutomationLibraryRequest = {
            "library_arn": library_arn
        }
        if library_description is not None:
            input_["library_description"] = library_description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_automation_library(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.delete_data_automation_library_response.DeleteDataAutomationLibraryResponse":
        """Deletes an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.delete_data_automation_library_request.DeleteDataAutomationLibraryRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.delete_data_automation_library_response.DeleteDataAutomationLibraryResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_library

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_library.async_delete_data_automation_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.delete_data_automation_library_request.DeleteDataAutomationLibraryRequest = {
            "library_arn": library_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_automation_libraries(
        self,
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
        project_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_filter.DataAutomationProjectFilter"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.list_data_automation_libraries_response.ListDataAutomationLibrariesResponse":
        """Lists all existing Amazon Bedrock Data Automation Libraries

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.list_data_automation_libraries_request.ListDataAutomationLibrariesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.list_data_automation_libraries_response.ListDataAutomationLibrariesResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_libraries

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_libraries.async_list_data_automation_libraries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.list_data_automation_libraries_request.ListDataAutomationLibrariesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if project_filter is not None:
            input_["project_filter"] = project_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_data_automation_libraries(
        self,
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
        project_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_filter.DataAutomationProjectFilter"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock_data_automation.types.data_automation_library_summary.DataAutomationLibrarySummary]":
        _token = next_token
        while True:
            _response = await self.list_data_automation_libraries(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                project_filter=project_filter,
            )
            _page = _resolve_path(_response, ("libraries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_data_automation_project(
        self,
        project_name: "capo_bedrock_data_automation.types.data_automation_project_name.DataAutomationProjectName",
        standard_output_configuration: "capo_bedrock_data_automation.types.standard_output_configuration.StandardOutputConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        project_description: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
        ] = None,
        project_stage: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
        project_type: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_type.DataAutomationProjectType"
        ] = None,
        custom_output_configuration: Optional[
            "capo_bedrock_data_automation.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        override_configuration: Optional[
            "capo_bedrock_data_automation.types.override_configuration.OverrideConfiguration"
        ] = None,
        data_automation_library_configuration: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_configuration.DataAutomationLibraryConfiguration"
        ] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.create_data_automation_project_response.CreateDataAutomationProjectResponse":
        """Creates an Amazon Bedrock Data Automation Project

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.create_data_automation_project_request.CreateDataAutomationProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.create_data_automation_project_response.CreateDataAutomationProjectResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_project

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_project.async_create_data_automation_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.create_data_automation_project_request.CreateDataAutomationProjectRequest = {
            "project_name": project_name,
            "standard_output_configuration": standard_output_configuration,
        }
        if project_description is not None:
            input_["project_description"] = project_description
        if project_stage is not None:
            input_["project_stage"] = project_stage
        if project_type is not None:
            input_["project_type"] = project_type
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if override_configuration is not None:
            input_["override_configuration"] = override_configuration
        if data_automation_library_configuration is not None:
            input_["data_automation_library_configuration"] = (
                data_automation_library_configuration
            )
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_automation_project(
        self,
        project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        project_stage: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.get_data_automation_project_response.GetDataAutomationProjectResponse":
        """Gets an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created
            project_stage: Optional field to delete a specific DataAutomationProject stage

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.get_data_automation_project_request.GetDataAutomationProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.get_data_automation_project_response.GetDataAutomationProjectResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_project

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_project.async_get_data_automation_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.get_data_automation_project_request.GetDataAutomationProjectRequest = {
            "project_arn": project_arn
        }
        if project_stage is not None:
            input_["project_stage"] = project_stage

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_data_automation_project(
        self,
        project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        standard_output_configuration: "capo_bedrock_data_automation.types.standard_output_configuration.StandardOutputConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        project_stage: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
        project_description: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
        ] = None,
        custom_output_configuration: Optional[
            "capo_bedrock_data_automation.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        override_configuration: Optional[
            "capo_bedrock_data_automation.types.override_configuration.OverrideConfiguration"
        ] = None,
        data_automation_library_configuration: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_configuration.DataAutomationLibraryConfiguration"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.update_data_automation_project_response.UpdateDataAutomationProjectResponse":
        """Updates an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.update_data_automation_project_request.UpdateDataAutomationProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.update_data_automation_project_response.UpdateDataAutomationProjectResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_project

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_project.async_update_data_automation_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.update_data_automation_project_request.UpdateDataAutomationProjectRequest = {
            "project_arn": project_arn,
            "standard_output_configuration": standard_output_configuration,
        }
        if project_stage is not None:
            input_["project_stage"] = project_stage
        if project_description is not None:
            input_["project_description"] = project_description
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if override_configuration is not None:
            input_["override_configuration"] = override_configuration
        if data_automation_library_configuration is not None:
            input_["data_automation_library_configuration"] = (
                data_automation_library_configuration
            )
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_automation_project(
        self,
        project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.delete_data_automation_project_response.DeleteDataAutomationProjectResponse":
        """Deletes an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.delete_data_automation_project_request.DeleteDataAutomationProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.delete_data_automation_project_response.DeleteDataAutomationProjectResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_project

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_project.async_delete_data_automation_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.delete_data_automation_project_request.DeleteDataAutomationProjectRequest = {
            "project_arn": project_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_automation_projects(
        self,
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
        project_stage_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_stage_filter.DataAutomationProjectStageFilter"
        ] = None,
        blueprint_filter: Optional[
            "capo_bedrock_data_automation.types.blueprint_filter.BlueprintFilter"
        ] = None,
        resource_owner: Optional[
            "capo_bedrock_data_automation.types.resource_owner.ResourceOwner"
        ] = None,
        library_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_filter.DataAutomationLibraryFilter"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.list_data_automation_projects_response.ListDataAutomationProjectsResponse":
        """Lists all existing Amazon Bedrock Data Automation Projects

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.list_data_automation_projects_request.ListDataAutomationProjectsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.list_data_automation_projects_response.ListDataAutomationProjectsResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_projects

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_projects.async_list_data_automation_projects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation.types.list_data_automation_projects_request.ListDataAutomationProjectsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if project_stage_filter is not None:
            input_["project_stage_filter"] = project_stage_filter
        if blueprint_filter is not None:
            input_["blueprint_filter"] = blueprint_filter
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner
        if library_filter is not None:
            input_["library_filter"] = library_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_data_automation_projects(
        self,
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
        project_stage_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_stage_filter.DataAutomationProjectStageFilter"
        ] = None,
        blueprint_filter: Optional[
            "capo_bedrock_data_automation.types.blueprint_filter.BlueprintFilter"
        ] = None,
        resource_owner: Optional[
            "capo_bedrock_data_automation.types.resource_owner.ResourceOwner"
        ] = None,
        library_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_filter.DataAutomationLibraryFilter"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock_data_automation.types.data_automation_project_summary.DataAutomationProjectSummary]":
        _token = next_token
        while True:
            _response = await self.list_data_automation_projects(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                project_stage_filter=project_stage_filter,
                blueprint_filter=blueprint_filter,
                resource_owner=resource_owner,
                library_filter=library_filter,
            )
            _page = _resolve_path(_response, ("projects",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
