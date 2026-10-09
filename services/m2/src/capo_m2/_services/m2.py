"""Generated from Smithy shape ``com.amazonaws.m2#AwsSupernovaControlPlaneService``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_m2._auth._signers
import capo_m2._auth._sigv4
from capo_m2._auth._identity import Credentials
from capo_m2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_m2._auth._zapros_handler import AuthMiddleware
from capo_m2._pagination import resolve_path as _resolve_path
from capo_m2._resources.aws_supernova_control_plane_service.application import (
    Application,
)
from capo_m2._resources.aws_supernova_control_plane_service.environment import (
    Environment,
)
from capo_m2._services._aws_config import aws_config
from capo_m2._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_m2.types.application_summary
    import capo_m2.types.application_version_summary
    import capo_m2.types.arn
    import capo_m2.types.auth_secrets_manager_arn
    import capo_m2.types.batch_job_definition
    import capo_m2.types.batch_job_execution_status
    import capo_m2.types.batch_job_execution_summary
    import capo_m2.types.batch_job_identifier
    import capo_m2.types.batch_job_parameters_map
    import capo_m2.types.boolean
    import capo_m2.types.cancel_batch_job_execution_request
    import capo_m2.types.cancel_batch_job_execution_response
    import capo_m2.types.capacity_value
    import capo_m2.types.client_token
    import capo_m2.types.create_application_request
    import capo_m2.types.create_application_response
    import capo_m2.types.create_data_set_export_task_request
    import capo_m2.types.create_data_set_export_task_response
    import capo_m2.types.create_data_set_import_task_request
    import capo_m2.types.create_data_set_import_task_response
    import capo_m2.types.create_deployment_request
    import capo_m2.types.create_deployment_response
    import capo_m2.types.create_environment_request
    import capo_m2.types.create_environment_response
    import capo_m2.types.data_set_export_config
    import capo_m2.types.data_set_export_task
    import capo_m2.types.data_set_import_config
    import capo_m2.types.data_set_import_task
    import capo_m2.types.data_set_summary
    import capo_m2.types.definition
    import capo_m2.types.delete_application_from_environment_request
    import capo_m2.types.delete_application_from_environment_response
    import capo_m2.types.delete_application_request
    import capo_m2.types.delete_application_response
    import capo_m2.types.delete_environment_request
    import capo_m2.types.delete_environment_response
    import capo_m2.types.deployment_summary
    import capo_m2.types.engine_type
    import capo_m2.types.engine_version
    import capo_m2.types.engine_versions_summary
    import capo_m2.types.entity_description
    import capo_m2.types.entity_name
    import capo_m2.types.entity_name_list
    import capo_m2.types.environment_summary
    import capo_m2.types.get_application_request
    import capo_m2.types.get_application_response
    import capo_m2.types.get_application_version_request
    import capo_m2.types.get_application_version_response
    import capo_m2.types.get_batch_job_execution_request
    import capo_m2.types.get_batch_job_execution_response
    import capo_m2.types.get_data_set_details_request
    import capo_m2.types.get_data_set_details_response
    import capo_m2.types.get_data_set_export_task_request
    import capo_m2.types.get_data_set_export_task_response
    import capo_m2.types.get_data_set_import_task_request
    import capo_m2.types.get_data_set_import_task_response
    import capo_m2.types.get_deployment_request
    import capo_m2.types.get_deployment_response
    import capo_m2.types.get_environment_request
    import capo_m2.types.get_environment_response
    import capo_m2.types.get_signed_bluinsights_url_response
    import capo_m2.types.high_availability_config
    import capo_m2.types.identifier
    import capo_m2.types.identifier_list
    import capo_m2.types.kms_key_id
    import capo_m2.types.list_application_versions_request
    import capo_m2.types.list_application_versions_response
    import capo_m2.types.list_applications_request
    import capo_m2.types.list_applications_response
    import capo_m2.types.list_batch_job_definitions_request
    import capo_m2.types.list_batch_job_definitions_response
    import capo_m2.types.list_batch_job_executions_request
    import capo_m2.types.list_batch_job_executions_response
    import capo_m2.types.list_batch_job_restart_points_request
    import capo_m2.types.list_batch_job_restart_points_response
    import capo_m2.types.list_data_set_export_history_request
    import capo_m2.types.list_data_set_export_history_response
    import capo_m2.types.list_data_set_import_history_request
    import capo_m2.types.list_data_set_import_history_response
    import capo_m2.types.list_data_sets_request
    import capo_m2.types.list_data_sets_response
    import capo_m2.types.list_deployments_request
    import capo_m2.types.list_deployments_response
    import capo_m2.types.list_engine_versions_request
    import capo_m2.types.list_engine_versions_response
    import capo_m2.types.list_environments_request
    import capo_m2.types.list_environments_response
    import capo_m2.types.list_tags_for_resource_request
    import capo_m2.types.list_tags_for_resource_response
    import capo_m2.types.max_results
    import capo_m2.types.network_type
    import capo_m2.types.next_token
    import capo_m2.types.start_application_request
    import capo_m2.types.start_application_response
    import capo_m2.types.start_batch_job_request
    import capo_m2.types.start_batch_job_response
    import capo_m2.types.stop_application_request
    import capo_m2.types.stop_application_response
    import capo_m2.types.storage_configuration_list
    import capo_m2.types.string20
    import capo_m2.types.string50
    import capo_m2.types.string50_list
    import capo_m2.types.string100
    import capo_m2.types.string200
    import capo_m2.types.tag_key_list
    import capo_m2.types.tag_map
    import capo_m2.types.tag_resource_request
    import capo_m2.types.tag_resource_response
    import capo_m2.types.timestamp
    import capo_m2.types.untag_resource_request
    import capo_m2.types.untag_resource_response
    import capo_m2.types.update_application_request
    import capo_m2.types.update_application_response
    import capo_m2.types.update_environment_request
    import capo_m2.types.update_environment_response
    import capo_m2.types.version


class m2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class m2Client:
    """A client for the ``m2`` service.

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
        self._config = m2ClientConfig(
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
        self.application = Application(self)
        self.environment = Environment(self)

    def operation_options(
        self, config_overrides: Optional[m2ClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: m2ClientConfig = config_overrides or {}
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

    def get_signed_bluinsights_url(
        self, *, config_overrides: Optional[m2ClientConfig] = None
    ) -> "capo_m2.types.get_signed_bluinsights_url_response.GetSignedBluinsightsUrlResponse":
        """<p>Gets a single sign-on URL that can be used to connect to AWS Blu Insights.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_m2.types.get_signed_bluinsights_url_response.GetSignedBluinsightsUrlResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_signed_bluinsights_url

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_signed_bluinsights_url.get_signed_bluinsights_url(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_engine_versions(
        self,
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        engine_type: Optional["capo_m2.types.engine_type.EngineType"] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "capo_m2.types.list_engine_versions_response.ListEngineVersionsResponse":
        """<p>Lists the available engine versions.</p>

        Args:
            engine_type: <p>The type of target platform.</p>
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_engine_versions_request.ListEngineVersionsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_engine_versions_response.ListEngineVersionsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_engine_versions

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_engine_versions.list_engine_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.list_engine_versions_request.ListEngineVersionsRequest = {}
        if engine_type is not None:
            input_["engine_type"] = engine_type
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

    def iter_list_engine_versions(
        self,
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        engine_type: Optional["capo_m2.types.engine_type.EngineType"] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_m2.types.engine_versions_summary.EngineVersionsSummary]":
        _token = next_token
        while True:
            _response = self.list_engine_versions(
                config_overrides=config_overrides,
                engine_type=engine_type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("engine_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_m2.types.arn.Arn",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_tags_for_resource

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_m2.types.arn.Arn",
        tags: "capo_m2.types.tag_map.TagMap",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags to add to the resource.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_m2.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.tag_resource

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_m2.types.arn.Arn",
        tag_keys: "capo_m2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The keys of the tags to remove.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_m2.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.untag_resource

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.untag_resource_request.UntagResourceRequest = {
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

    def create_application(
        self,
        name: "capo_m2.types.entity_name.EntityName",
        engine_type: "capo_m2.types.engine_type.EngineType",
        definition: "capo_m2.types.definition.Definition",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        description: Optional[
            "capo_m2.types.entity_description.EntityDescription"
        ] = None,
        tags: Optional["capo_m2.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_m2.types.client_token.ClientToken"] = None,
        kms_key_id: Optional[str] = None,
        role_arn: Optional["capo_m2.types.arn.Arn"] = None,
    ) -> "capo_m2.types.create_application_response.CreateApplicationResponse":
        """<p>Creates a new application with given parameters. Requires an existing runtime environment and application definition file.</p>

        Args:
            name: <p>The unique identifier of the application.</p>
            description: <p>The description of the application.</p>
            engine_type: <p>The type of the target platform for this application.</p>
            definition: <p>The application definition for this application. You can specify either inline JSON or an S3 bucket location.</p>
            tags: <p>A list of tags to apply to the application.</p>
            client_token: <p>A client token is a unique, case-sensitive string of up to 128 ASCII characters with ASCII values of 33-126 inclusive. It's generated by the client to ensure idempotent operations, allowing for safe retries without unintended side effects.</p>
            kms_key_id: <p>The identifier of a customer managed key.</p>
            role_arn: <p>The Amazon Resource Name (ARN) that identifies a role that the application uses to access Amazon Web Services resources that are not part of the application or are in a different Amazon Web Services account.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "capo_m2.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.create_application

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.create_application_request.CreateApplicationRequest = {
            "name": name,
            "engine_type": engine_type,
            "definition": definition,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_application(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_application_response.GetApplicationResponse":
        """<p>Describes the details of a specific application.</p>

        Args:
            application_id: <p>The identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_application_request.GetApplicationRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_application

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_application.get_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.get_application_request.GetApplicationRequest = {
            "application_id": application_id
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
        application_id: "capo_m2.types.identifier.Identifier",
        current_application_version: "capo_m2.types.version.Version",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        description: Optional[
            "capo_m2.types.entity_description.EntityDescription"
        ] = None,
        definition: Optional["capo_m2.types.definition.Definition"] = None,
    ) -> "capo_m2.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates an application and creates a new version.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to update.</p>
            description: <p>The description of the application to update.</p>
            current_application_version: <p>The current version of the application to update.</p>
            definition: <p>The application definition for this application. You can specify either inline JSON or an S3 bucket location.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse[
            "capo_m2.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.update_application

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id,
            "current_application_version": current_application_version,
        }
        if description is not None:
            input_["description"] = description
        if definition is not None:
            input_["definition"] = definition

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes a specific application. You cannot delete a running application.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to delete.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "capo_m2.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.delete_application

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_applications(
        self,
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        names: Optional["capo_m2.types.entity_name_list.EntityNameList"] = None,
        environment_id: Optional["capo_m2.types.identifier.Identifier"] = None,
    ) -> "capo_m2.types.list_applications_response.ListApplicationsResponse":
        """<p>Lists the applications associated with a specific Amazon Web Services account. You can provide the unique identifier of a specific runtime environment in a query parameter to see all applications associated with that environment.</p>

        Args:
            next_token: <p>A pagination token to control the number of applications displayed in the list.</p>
            max_results: <p>The maximum number of applications to return.</p>
            names: <p>The names of the applications.</p>
            environment_id: <p>The unique identifier of the runtime environment where the applications are deployed.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_applications

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.list_applications_request.ListApplicationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if names is not None:
            input_["names"] = names
        if environment_id is not None:
            input_["environment_id"] = environment_id

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
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        names: Optional["capo_m2.types.entity_name_list.EntityNameList"] = None,
        environment_id: Optional["capo_m2.types.identifier.Identifier"] = None,
    ) -> "Iterator[capo_m2.types.application_summary.ApplicationSummary]":
        _token = next_token
        while True:
            _response = self.list_applications(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                names=names,
                environment_id=environment_id,
            )
            _page = _resolve_path(_response, ("applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def cancel_batch_job_execution(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        execution_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        auth_secrets_manager_arn: Optional[
            "capo_m2.types.auth_secrets_manager_arn.AuthSecretsManagerArn"
        ] = None,
    ) -> "capo_m2.types.cancel_batch_job_execution_response.CancelBatchJobExecutionResponse":
        """<p>Cancels the running of a specific batch job execution.</p>

        Args:
            application_id: <p>The unique identifier of the application.</p>
            execution_id: <p>The unique identifier of the batch job execution.</p>
            auth_secrets_manager_arn: <p>The Amazon Web Services Secrets Manager containing user's credentials for authentication and authorization for Cancel Batch Job Execution operation.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.cancel_batch_job_execution_request.CancelBatchJobExecutionRequest]",
        ) -> OperationResponse[
            "capo_m2.types.cancel_batch_job_execution_response.CancelBatchJobExecutionResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.cancel_batch_job_execution

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.cancel_batch_job_execution.cancel_batch_job_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.cancel_batch_job_execution_request.CancelBatchJobExecutionRequest = {
            "application_id": application_id,
            "execution_id": execution_id,
        }
        if auth_secrets_manager_arn is not None:
            input_["auth_secrets_manager_arn"] = auth_secrets_manager_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_set_export_task(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        export_config: "capo_m2.types.data_set_export_config.DataSetExportConfig",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        client_token: Optional["capo_m2.types.client_token.ClientToken"] = None,
        kms_key_id: Optional["capo_m2.types.kms_key_id.KMSKeyId"] = None,
    ) -> "capo_m2.types.create_data_set_export_task_response.CreateDataSetExportTaskResponse":
        """<p>Starts a data set export task for a specific application.</p>

        Args:
            application_id: <p>The unique identifier of the application for which you want to export data sets.</p>
            export_config: <p>The data set export task configuration.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a data set export. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires.</p>
            kms_key_id: <p>The identifier of a customer managed key.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.create_data_set_export_task_request.CreateDataSetExportTaskRequest]",
        ) -> OperationResponse[
            "capo_m2.types.create_data_set_export_task_response.CreateDataSetExportTaskResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.create_data_set_export_task

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.create_data_set_export_task.create_data_set_export_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.create_data_set_export_task_request.CreateDataSetExportTaskRequest = {
            "application_id": application_id,
            "export_config": export_config,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_set_import_task(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        import_config: "capo_m2.types.data_set_import_config.DataSetImportConfig",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        client_token: Optional["capo_m2.types.client_token.ClientToken"] = None,
    ) -> "capo_m2.types.create_data_set_import_task_response.CreateDataSetImportTaskResponse":
        """<p>Starts a data set import task for a specific application.</p>

        Args:
            application_id: <p>The unique identifier of the application for which you want to import data sets.</p>
            import_config: <p>The data set import task configuration.</p>
            client_token: <p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a data set import. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires. </p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.create_data_set_import_task_request.CreateDataSetImportTaskRequest]",
        ) -> OperationResponse[
            "capo_m2.types.create_data_set_import_task_response.CreateDataSetImportTaskResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.create_data_set_import_task

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.create_data_set_import_task.create_data_set_import_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.create_data_set_import_task_request.CreateDataSetImportTaskRequest = {
            "application_id": application_id,
            "import_config": import_config,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_deployment(
        self,
        environment_id: "capo_m2.types.identifier.Identifier",
        application_id: "capo_m2.types.identifier.Identifier",
        application_version: "capo_m2.types.version.Version",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        client_token: Optional["capo_m2.types.client_token.ClientToken"] = None,
    ) -> "capo_m2.types.create_deployment_response.CreateDeploymentResponse":
        """<p>Creates and starts a deployment to deploy an application into a runtime environment.</p>

        Args:
            environment_id: <p>The identifier of the runtime environment where you want to deploy this application.</p>
            application_id: <p>The application identifier.</p>
            application_version: <p>The version of the application to deploy.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a deployment. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires. </p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.create_deployment_request.CreateDeploymentRequest]",
        ) -> OperationResponse[
            "capo_m2.types.create_deployment_response.CreateDeploymentResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.create_deployment

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.create_deployment.create_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.create_deployment_request.CreateDeploymentRequest = {
            "environment_id": environment_id,
            "application_id": application_id,
            "application_version": application_version,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application_from_environment(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        environment_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.delete_application_from_environment_response.DeleteApplicationFromEnvironmentResponse":
        """<p>Deletes a specific application from the specific runtime environment where it was previously deployed. You cannot delete a runtime environment using DeleteEnvironment if any application has ever been deployed to it. This API removes the association of the application with the runtime environment so you can delete the environment smoothly.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to delete.</p>
            environment_id: <p>The unique identifier of the runtime environment where the application was previously deployed.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.delete_application_from_environment_request.DeleteApplicationFromEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_m2.types.delete_application_from_environment_response.DeleteApplicationFromEnvironmentResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.delete_application_from_environment

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.delete_application_from_environment.delete_application_from_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.delete_application_from_environment_request.DeleteApplicationFromEnvironmentRequest = {
            "application_id": application_id,
            "environment_id": environment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_application_version(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        application_version: "capo_m2.types.version.Version",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_application_version_response.GetApplicationVersionResponse":
        """<p>Returns details about a specific version of a specific application.</p>

        Args:
            application_id: <p>The unique identifier of the application.</p>
            application_version: <p>The specific version of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_application_version_request.GetApplicationVersionRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_application_version_response.GetApplicationVersionResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_application_version

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_application_version.get_application_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.get_application_version_request.GetApplicationVersionRequest = {
            "application_id": application_id,
            "application_version": application_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_batch_job_execution(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        execution_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_batch_job_execution_response.GetBatchJobExecutionResponse":
        """<p>Gets the details of a specific batch job execution for a specific application.</p>

        Args:
            application_id: <p>The identifier of the application.</p>
            execution_id: <p>The unique identifier of the batch job execution.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_batch_job_execution_request.GetBatchJobExecutionRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_batch_job_execution_response.GetBatchJobExecutionResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_batch_job_execution

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_batch_job_execution.get_batch_job_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.get_batch_job_execution_request.GetBatchJobExecutionRequest = {
            "application_id": application_id,
            "execution_id": execution_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_set_details(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        data_set_name: "capo_m2.types.string200.String200",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_data_set_details_response.GetDataSetDetailsResponse":
        """<p>Gets the details of a specific data set.</p>

        Args:
            application_id: <p>The unique identifier of the application that this data set is associated with.</p>
            data_set_name: <p>The name of the data set.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.execution_timeout_exception.ExecutionTimeoutException: <p> Failed to connect to server, or didn’t receive response within expected time period.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_unavailable_exception.ServiceUnavailableException: <p>Server cannot process the request at the moment.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_data_set_details_request.GetDataSetDetailsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_data_set_details_response.GetDataSetDetailsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_data_set_details

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_data_set_details.get_data_set_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.get_data_set_details_request.GetDataSetDetailsRequest = {
            "application_id": application_id,
            "data_set_name": data_set_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_set_export_task(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        task_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_data_set_export_task_response.GetDataSetExportTaskResponse":
        """<p>Gets the status of a data set import task initiated with the <a>CreateDataSetExportTask</a> operation.</p>

        Args:
            application_id: <p>The application identifier.</p>
            task_id: <p>The task identifier returned by the <a>CreateDataSetExportTask</a> operation.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_data_set_export_task_request.GetDataSetExportTaskRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_data_set_export_task_response.GetDataSetExportTaskResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_data_set_export_task

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_data_set_export_task.get_data_set_export_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.get_data_set_export_task_request.GetDataSetExportTaskRequest = {
            "application_id": application_id,
            "task_id": task_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_set_import_task(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        task_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_data_set_import_task_response.GetDataSetImportTaskResponse":
        """<p>Gets the status of a data set import task initiated with the <a>CreateDataSetImportTask</a> operation.</p>

        Args:
            application_id: <p>The application identifier.</p>
            task_id: <p>The task identifier returned by the <a>CreateDataSetImportTask</a> operation. </p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_data_set_import_task_request.GetDataSetImportTaskRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_data_set_import_task_response.GetDataSetImportTaskResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_data_set_import_task

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_data_set_import_task.get_data_set_import_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.get_data_set_import_task_request.GetDataSetImportTaskRequest = {
            "application_id": application_id,
            "task_id": task_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_deployment(
        self,
        deployment_id: "capo_m2.types.identifier.Identifier",
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_deployment_response.GetDeploymentResponse":
        """<p>Gets details of a specific deployment with a given deployment identifier.</p>

        Args:
            deployment_id: <p>The unique identifier for the deployment.</p>
            application_id: <p>The unique identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_deployment_request.GetDeploymentRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_deployment_response.GetDeploymentResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_deployment

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_deployment.get_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.get_deployment_request.GetDeploymentRequest = {
            "deployment_id": deployment_id,
            "application_id": application_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_application_versions(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "capo_m2.types.list_application_versions_response.ListApplicationVersionsResponse":
        """<p>Returns a list of the application versions for a specific application.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of application versions to return.</p>
            application_id: <p>The unique identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_application_versions_request.ListApplicationVersionsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_application_versions_response.ListApplicationVersionsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_application_versions

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_application_versions.list_application_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.list_application_versions_request.ListApplicationVersionsRequest = {
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

    def iter_list_application_versions(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> (
        "Iterator[capo_m2.types.application_version_summary.ApplicationVersionSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_application_versions(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("application_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_batch_job_definitions(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        prefix: Optional[str] = None,
    ) -> "capo_m2.types.list_batch_job_definitions_response.ListBatchJobDefinitionsResponse":
        """<p>Lists all the available batch job definitions based on the batch job resources uploaded during the application creation. You can use the batch job definitions in the list to start a batch job.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of batch job definitions to return.</p>
            application_id: <p>The identifier of the application.</p>
            prefix: <p>If the batch job definition is a FileBatchJobDefinition, the prefix allows you to search on the file names of FileBatchJobDefinitions.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_batch_job_definitions_request.ListBatchJobDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_batch_job_definitions_response.ListBatchJobDefinitionsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_definitions

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_definitions.list_batch_job_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.list_batch_job_definitions_request.ListBatchJobDefinitionsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if prefix is not None:
            input_["prefix"] = prefix

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_batch_job_definitions(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        prefix: Optional[str] = None,
    ) -> "Iterator[capo_m2.types.batch_job_definition.BatchJobDefinition]":
        _token = next_token
        while True:
            _response = self.list_batch_job_definitions(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                prefix=prefix,
            )
            _page = _resolve_path(_response, ("batch_job_definitions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_batch_job_executions(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        execution_ids: Optional["capo_m2.types.identifier_list.IdentifierList"] = None,
        job_name: Optional["capo_m2.types.string100.String100"] = None,
        status: Optional[
            "capo_m2.types.batch_job_execution_status.BatchJobExecutionStatus"
        ] = None,
        started_after: Optional["capo_m2.types.timestamp.Timestamp"] = None,
        started_before: Optional["capo_m2.types.timestamp.Timestamp"] = None,
    ) -> "capo_m2.types.list_batch_job_executions_response.ListBatchJobExecutionsResponse":
        """<p>Lists historical, current, and scheduled batch job executions for a specific application.</p>

        Args:
            next_token: <p>A pagination token to control the number of batch job executions displayed in the list.</p>
            max_results: <p>The maximum number of batch job executions to return.</p>
            application_id: <p>The unique identifier of the application.</p>
            execution_ids: <p>The unique identifier of each batch job execution.</p>
            job_name: <p>The name of each batch job execution.</p>
            status: <p>The status of the batch job executions.</p>
            started_after: <p>The time after which the batch job executions started.</p>
            started_before: <p>The time before the batch job executions started.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_batch_job_executions_request.ListBatchJobExecutionsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_batch_job_executions_response.ListBatchJobExecutionsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_executions

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_executions.list_batch_job_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.list_batch_job_executions_request.ListBatchJobExecutionsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if execution_ids is not None:
            input_["execution_ids"] = execution_ids
        if job_name is not None:
            input_["job_name"] = job_name
        if status is not None:
            input_["status"] = status
        if started_after is not None:
            input_["started_after"] = started_after
        if started_before is not None:
            input_["started_before"] = started_before

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_batch_job_executions(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        execution_ids: Optional["capo_m2.types.identifier_list.IdentifierList"] = None,
        job_name: Optional["capo_m2.types.string100.String100"] = None,
        status: Optional[
            "capo_m2.types.batch_job_execution_status.BatchJobExecutionStatus"
        ] = None,
        started_after: Optional["capo_m2.types.timestamp.Timestamp"] = None,
        started_before: Optional["capo_m2.types.timestamp.Timestamp"] = None,
    ) -> "Iterator[capo_m2.types.batch_job_execution_summary.BatchJobExecutionSummary]":
        _token = next_token
        while True:
            _response = self.list_batch_job_executions(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                execution_ids=execution_ids,
                job_name=job_name,
                status=status,
                started_after=started_after,
                started_before=started_before,
            )
            _page = _resolve_path(_response, ("batch_job_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_batch_job_restart_points(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        execution_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        auth_secrets_manager_arn: Optional[
            "capo_m2.types.auth_secrets_manager_arn.AuthSecretsManagerArn"
        ] = None,
    ) -> "capo_m2.types.list_batch_job_restart_points_response.ListBatchJobRestartPointsResponse":
        """<p>Lists all the job steps for a JCL file to restart a batch job. This is only applicable for Micro Focus engine with versions 8.0.6 and above.</p>

        Args:
            application_id: <p>The unique identifier of the application.</p>
            execution_id: <p>The unique identifier of the batch job execution.</p>
            auth_secrets_manager_arn: <p>The Amazon Web Services Secrets Manager containing user's credentials for authentication and authorization for List Batch Job Restart Points operation.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_batch_job_restart_points_request.ListBatchJobRestartPointsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_batch_job_restart_points_response.ListBatchJobRestartPointsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_restart_points

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_restart_points.list_batch_job_restart_points(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.list_batch_job_restart_points_request.ListBatchJobRestartPointsRequest = {
            "application_id": application_id,
            "execution_id": execution_id,
        }
        if auth_secrets_manager_arn is not None:
            input_["auth_secrets_manager_arn"] = auth_secrets_manager_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_data_set_export_history(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "capo_m2.types.list_data_set_export_history_response.ListDataSetExportHistoryResponse":
        """<p>Lists the data set exports for the specified application.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>
            application_id: <p>The unique identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_data_set_export_history_request.ListDataSetExportHistoryRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_data_set_export_history_response.ListDataSetExportHistoryResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_data_set_export_history

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_data_set_export_history.list_data_set_export_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.list_data_set_export_history_request.ListDataSetExportHistoryRequest = {
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

    def iter_list_data_set_export_history(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_m2.types.data_set_export_task.DataSetExportTask]":
        _token = next_token
        while True:
            _response = self.list_data_set_export_history(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_set_export_tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_data_set_import_history(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "capo_m2.types.list_data_set_import_history_response.ListDataSetImportHistoryResponse":
        """<p>Lists the data set imports for the specified application.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>
            application_id: <p>The unique identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_data_set_import_history_request.ListDataSetImportHistoryRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_data_set_import_history_response.ListDataSetImportHistoryResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_data_set_import_history

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_data_set_import_history.list_data_set_import_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.list_data_set_import_history_request.ListDataSetImportHistoryRequest = {
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

    def iter_list_data_set_import_history(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_m2.types.data_set_import_task.DataSetImportTask]":
        _token = next_token
        while True:
            _response = self.list_data_set_import_history(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_set_import_tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_data_sets(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        prefix: Optional["capo_m2.types.string200.String200"] = None,
        name_filter: Optional["capo_m2.types.string200.String200"] = None,
    ) -> "capo_m2.types.list_data_sets_response.ListDataSetsResponse":
        """<p>Lists the data sets imported for a specific application. In Amazon Web Services Mainframe Modernization, data sets are associated with applications deployed on runtime environments. This is known as importing data sets. Currently, Amazon Web Services Mainframe Modernization can import data sets into catalogs using <a href="https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateDataSetImportTask.html">CreateDataSetImportTask</a>.</p>

        Args:
            application_id: <p>The unique identifier of the application for which you want to list the associated data sets.</p>
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>
            prefix: <p>The prefix of the data set name, which you can use to filter the list of data sets.</p>
            name_filter: <p>Filter dataset name matching the specified pattern. Can use * and % as wild cards.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.execution_timeout_exception.ExecutionTimeoutException: <p> Failed to connect to server, or didn’t receive response within expected time period.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_unavailable_exception.ServiceUnavailableException: <p>Server cannot process the request at the moment.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_data_sets_request.ListDataSetsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_data_sets_response.ListDataSetsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_data_sets

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_data_sets.list_data_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.list_data_sets_request.ListDataSetsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if prefix is not None:
            input_["prefix"] = prefix
        if name_filter is not None:
            input_["name_filter"] = name_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_data_sets(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        prefix: Optional["capo_m2.types.string200.String200"] = None,
        name_filter: Optional["capo_m2.types.string200.String200"] = None,
    ) -> "Iterator[capo_m2.types.data_set_summary.DataSetSummary]":
        _token = next_token
        while True:
            _response = self.list_data_sets(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                prefix=prefix,
                name_filter=name_filter,
            )
            _page = _resolve_path(_response, ("data_sets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_deployments(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "capo_m2.types.list_deployments_response.ListDeploymentsResponse":
        """<p>Returns a list of all deployments of a specific application. A deployment is a combination of a specific application and a specific version of that application. Each deployment is mapped to a particular application version.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>
            application_id: <p>The application identifier.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_deployments_request.ListDeploymentsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_deployments_response.ListDeploymentsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_deployments

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_deployments.list_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.list_deployments_request.ListDeploymentsRequest = {
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

    def iter_list_deployments(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_m2.types.deployment_summary.DeploymentSummary]":
        _token = next_token
        while True:
            _response = self.list_deployments(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("deployments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_application(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.start_application_response.StartApplicationResponse":
        """<p>Starts an application that is currently stopped.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to start.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.start_application_request.StartApplicationRequest]",
        ) -> OperationResponse[
            "capo_m2.types.start_application_response.StartApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.start_application

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.start_application.start_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.start_application_request.StartApplicationRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_batch_job(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        batch_job_identifier: "capo_m2.types.batch_job_identifier.BatchJobIdentifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        job_params: Optional[
            "capo_m2.types.batch_job_parameters_map.BatchJobParametersMap"
        ] = None,
        auth_secrets_manager_arn: Optional[
            "capo_m2.types.auth_secrets_manager_arn.AuthSecretsManagerArn"
        ] = None,
    ) -> "capo_m2.types.start_batch_job_response.StartBatchJobResponse":
        """<p>Starts a batch job and returns the unique identifier of this execution of the batch job. The associated application must be running in order to start the batch job.</p>

        Args:
            application_id: <p>The unique identifier of the application associated with this batch job.</p>
            batch_job_identifier: <p>The unique identifier of the batch job.</p>
            job_params: <p>The collection of batch job parameters. For details about limits for keys and values, see <a href="https://www.ibm.com/docs/en/workload-automation/9.3.0?topic=zos-coding-variables-in-jcl">Coding variables in JCL</a>.</p>
            auth_secrets_manager_arn: <p>The Amazon Web Services Secrets Manager containing user's credentials for authentication and authorization for Start Batch Job execution operation.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.start_batch_job_request.StartBatchJobRequest]",
        ) -> OperationResponse[
            "capo_m2.types.start_batch_job_response.StartBatchJobResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.start_batch_job

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.start_batch_job.start_batch_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.start_batch_job_request.StartBatchJobRequest = {
            "application_id": application_id,
            "batch_job_identifier": batch_job_identifier,
        }
        if job_params is not None:
            input_["job_params"] = job_params
        if auth_secrets_manager_arn is not None:
            input_["auth_secrets_manager_arn"] = auth_secrets_manager_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_application(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        force_stop: Optional["capo_m2.types.boolean.Boolean"] = None,
    ) -> "capo_m2.types.stop_application_response.StopApplicationResponse":
        """<p>Stops a running application.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to stop.</p>
            force_stop: <p>Stopping an application process can take a long time. Setting this parameter to true lets you force stop the application so you don't need to wait until the process finishes to apply another action on the application. The default value is false.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.stop_application_request.StopApplicationRequest]",
        ) -> OperationResponse[
            "capo_m2.types.stop_application_response.StopApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.stop_application

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.stop_application.stop_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.stop_application_request.StopApplicationRequest = {
            "application_id": application_id
        }
        if force_stop is not None:
            input_["force_stop"] = force_stop

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_environment(
        self,
        name: "capo_m2.types.entity_name.EntityName",
        instance_type: "capo_m2.types.string20.String20",
        engine_type: "capo_m2.types.engine_type.EngineType",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        description: Optional[
            "capo_m2.types.entity_description.EntityDescription"
        ] = None,
        engine_version: Optional["capo_m2.types.engine_version.EngineVersion"] = None,
        subnet_ids: Optional["capo_m2.types.string50_list.String50List"] = None,
        security_group_ids: Optional["capo_m2.types.string50_list.String50List"] = None,
        storage_configurations: Optional[
            "capo_m2.types.storage_configuration_list.StorageConfigurationList"
        ] = None,
        publicly_accessible: Optional["capo_m2.types.boolean.Boolean"] = None,
        high_availability_config: Optional[
            "capo_m2.types.high_availability_config.HighAvailabilityConfig"
        ] = None,
        tags: Optional["capo_m2.types.tag_map.TagMap"] = None,
        preferred_maintenance_window: Optional[
            "capo_m2.types.string50.String50"
        ] = None,
        network_type: Optional["capo_m2.types.network_type.NetworkType"] = None,
        client_token: Optional["capo_m2.types.client_token.ClientToken"] = None,
        kms_key_id: Optional[str] = None,
    ) -> "capo_m2.types.create_environment_response.CreateEnvironmentResponse":
        """<p>Creates a runtime environment for a given runtime engine.</p>

        Args:
            name: <p>The name of the runtime environment. Must be unique within the account.</p>
            instance_type: <p>The type of instance for the runtime environment.</p>
            description: <p>The description of the runtime environment.</p>
            engine_type: <p>The engine type for the runtime environment.</p>
            engine_version: <p>The version of the engine type for the runtime environment.</p>
            subnet_ids: <p>The list of subnets associated with the VPC for this runtime environment.</p>
            security_group_ids: <p>The list of security groups for the VPC associated with this runtime environment.</p>
            storage_configurations: <p>Optional. The storage configurations for this runtime environment.</p>
            publicly_accessible: <p>Specifies whether the runtime environment is publicly accessible.</p>
            high_availability_config: <p>The details of a high availability configuration for this runtime environment.</p>
            tags: <p>The tags for the runtime environment.</p>
            preferred_maintenance_window: <p>Configures the maintenance window that you want for the runtime environment. The maintenance window must have the format <code>ddd:hh24:mi-ddd:hh24:mi</code> and must be less than 24 hours. The following two examples are valid maintenance windows: <code>sun:23:45-mon:00:15</code> or <code>sat:01:00-sat:03:00</code>. </p> <p>If you do not provide a value, a random system-generated value will be assigned.</p>
            network_type: <p>The network type required for the runtime environment.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create an environment. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires. </p>
            kms_key_id: <p>The identifier of a customer managed key.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.create_environment_request.CreateEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_m2.types.create_environment_response.CreateEnvironmentResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.create_environment

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.create_environment.create_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.create_environment_request.CreateEnvironmentRequest = {
            "name": name,
            "instance_type": instance_type,
            "engine_type": engine_type,
        }
        if description is not None:
            input_["description"] = description
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if storage_configurations is not None:
            input_["storage_configurations"] = storage_configurations
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if high_availability_config is not None:
            input_["high_availability_config"] = high_availability_config
        if tags is not None:
            input_["tags"] = tags
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if network_type is not None:
            input_["network_type"] = network_type
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_environment(
        self,
        environment_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_environment_response.GetEnvironmentResponse":
        """<p>Describes a specific runtime environment.</p>

        Args:
            environment_id: <p>The unique identifier of the runtime environment.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_environment_request.GetEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_environment_response.GetEnvironmentResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_environment

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_environment.get_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.get_environment_request.GetEnvironmentRequest = {
            "environment_id": environment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_environment(
        self,
        environment_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        desired_capacity: Optional["capo_m2.types.capacity_value.CapacityValue"] = None,
        instance_type: Optional["capo_m2.types.string20.String20"] = None,
        engine_version: Optional["capo_m2.types.engine_version.EngineVersion"] = None,
        preferred_maintenance_window: Optional[str] = None,
        apply_during_maintenance_window: Optional[
            "capo_m2.types.boolean.Boolean"
        ] = None,
        force_update: Optional["capo_m2.types.boolean.Boolean"] = None,
    ) -> "capo_m2.types.update_environment_response.UpdateEnvironmentResponse":
        """<p>Updates the configuration details for a specific runtime environment.</p>

        Args:
            environment_id: <p>The unique identifier of the runtime environment that you want to update.</p>
            desired_capacity: <p>The desired capacity for the runtime environment to update. The minimum possible value is 0 and the maximum is 100.</p>
            instance_type: <p>The instance type for the runtime environment to update.</p>
            engine_version: <p>The version of the runtime engine for the runtime environment.</p>
            preferred_maintenance_window: <p>Configures the maintenance window that you want for the runtime environment. The maintenance window must have the format <code>ddd:hh24:mi-ddd:hh24:mi</code> and must be less than 24 hours. The following two examples are valid maintenance windows: <code>sun:23:45-mon:00:15</code> or <code>sat:01:00-sat:03:00</code>. </p> <p>If you do not provide a value, a random system-generated value will be assigned.</p>
            apply_during_maintenance_window: <p>Indicates whether to update the runtime environment during the maintenance window. The default is false. Currently, Amazon Web Services Mainframe Modernization accepts the <code>engineVersion</code> parameter only if <code>applyDuringMaintenanceWindow</code> is true. If any parameter other than <code>engineVersion</code> is provided in <code>UpdateEnvironmentRequest</code>, it will fail if <code>applyDuringMaintenanceWindow</code> is set to true.</p>
            force_update: <p>Forces the updates on the environment. This option is needed if the applications in the environment are not stopped or if there are ongoing application-related activities in the environment.</p> <p>If you use this option, be aware that it could lead to data corruption in the applications, and that you might need to perform repair and recovery procedures for the applications.</p> <p>This option is not needed if the attribute being updated is <code>preferredMaintenanceWindow</code>.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.update_environment_request.UpdateEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_m2.types.update_environment_response.UpdateEnvironmentResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.update_environment

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.update_environment.update_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.update_environment_request.UpdateEnvironmentRequest = {
            "environment_id": environment_id
        }
        if desired_capacity is not None:
            input_["desired_capacity"] = desired_capacity
        if instance_type is not None:
            input_["instance_type"] = instance_type
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if apply_during_maintenance_window is not None:
            input_["apply_during_maintenance_window"] = apply_during_maintenance_window
        if force_update is not None:
            input_["force_update"] = force_update

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_environment(
        self,
        environment_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.delete_environment_response.DeleteEnvironmentResponse":
        """<p>Deletes a specific runtime environment. The environment cannot contain deployed applications. If it does, you must delete those applications before you delete the environment.</p>

        Args:
            environment_id: <p>The unique identifier of the runtime environment you want to delete.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.delete_environment_request.DeleteEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_m2.types.delete_environment_response.DeleteEnvironmentResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.delete_environment

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.delete_environment.delete_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.delete_environment_request.DeleteEnvironmentRequest = {
            "environment_id": environment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_environments(
        self,
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        names: Optional["capo_m2.types.entity_name_list.EntityNameList"] = None,
        engine_type: Optional["capo_m2.types.engine_type.EngineType"] = None,
    ) -> "capo_m2.types.list_environments_response.ListEnvironmentsResponse":
        """<p>Lists the runtime environments.</p>

        Args:
            next_token: <p>A pagination token to control the number of runtime environments displayed in the list.</p>
            max_results: <p>The maximum number of runtime environments to return.</p>
            names: <p>The names of the runtime environments. Must be unique within the account.</p>
            engine_type: <p>The engine type for the runtime environment.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_environments_response.ListEnvironmentsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_environments

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_environments.list_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_m2.types.list_environments_request.ListEnvironmentsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if names is not None:
            input_["names"] = names
        if engine_type is not None:
            input_["engine_type"] = engine_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_environments(
        self,
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        names: Optional["capo_m2.types.entity_name_list.EntityNameList"] = None,
        engine_type: Optional["capo_m2.types.engine_type.EngineType"] = None,
    ) -> "Iterator[capo_m2.types.environment_summary.EnvironmentSummary]":
        _token = next_token
        while True:
            _response = self.list_environments(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                names=names,
                engine_type=engine_type,
            )
            _page = _resolve_path(_response, ("environments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
