from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_observabilityadmin._auth._signers
import capo_observabilityadmin._auth._sigv4
from capo_observabilityadmin._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_observabilityadmin.types.create_telemetry_pipeline_input
    import capo_observabilityadmin.types.create_telemetry_pipeline_output
    import capo_observabilityadmin.types.delete_telemetry_pipeline_input
    import capo_observabilityadmin.types.delete_telemetry_pipeline_output
    import capo_observabilityadmin.types.get_telemetry_pipeline_input
    import capo_observabilityadmin.types.get_telemetry_pipeline_output
    import capo_observabilityadmin.types.list_telemetry_pipelines_input
    import capo_observabilityadmin.types.list_telemetry_pipelines_max_results
    import capo_observabilityadmin.types.list_telemetry_pipelines_output
    import capo_observabilityadmin.types.next_token
    import capo_observabilityadmin.types.tag_map_input
    import capo_observabilityadmin.types.telemetry_pipeline_configuration
    import capo_observabilityadmin.types.telemetry_pipeline_identifier
    import capo_observabilityadmin.types.telemetry_pipeline_name
    import capo_observabilityadmin.types.telemetry_pipeline_summary
    import capo_observabilityadmin.types.update_telemetry_pipeline_input
    import capo_observabilityadmin.types.update_telemetry_pipeline_output
    from capo_observabilityadmin._services.async_observability_admin import (
        AsyncObservabilityAdminClient,
        AsyncObservabilityAdminClientConfig,
    )
    from capo_observabilityadmin._services.observability_admin import (
        ObservabilityAdminClient,
        ObservabilityAdminClientConfig,
    )


class TelemetryPipelineResource:
    def __init__(self, service: ObservabilityAdminClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_observabilityadmin.types.telemetry_pipeline_name.TelemetryPipelineName",
        configuration: "capo_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        tags: Optional[
            "capo_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
    ) -> "capo_observabilityadmin.types.create_telemetry_pipeline_output.CreateTelemetryPipelineOutput":
        """<p>Creates a telemetry pipeline for processing and transforming telemetry data. The pipeline defines how data flows from sources through processors to destinations, enabling data transformation and delivering capabilities. </p>

        Args:
            name: <p>The name of the telemetry pipeline to create. The name must be unique within your account.</p>
            configuration: <p>The configuration that defines how the telemetry pipeline processes data, including sources, processors, and destinations. For more information about pipeline components, see the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/pipeline-components-reference.html">Amazon CloudWatch User Guide</a> </p>
            tags: <p>The key-value pairs to associate with the telemetry pipeline resource for categorization and management purposes.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.conflict_exception.ConflictException: <p> The requested operation conflicts with the current state of the specified resource or with another request. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The requested operation would exceed the allowed quota for the specified resource type. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_observabilityadmin.types.create_telemetry_pipeline_input.CreateTelemetryPipelineInput]",
        ) -> OperationResponse[
            "capo_observabilityadmin.types.create_telemetry_pipeline_output.CreateTelemetryPipelineOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.create_telemetry_pipeline

            output, http_response = (
                capo_observabilityadmin._operations.observability_admin.create_telemetry_pipeline.create_telemetry_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.create_telemetry_pipeline_input.CreateTelemetryPipelineInput = {
            "name": name,
            "configuration": configuration,
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

    def read(
        self,
        pipeline_identifier: "capo_observabilityadmin.types.telemetry_pipeline_identifier.TelemetryPipelineIdentifier",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.get_telemetry_pipeline_output.GetTelemetryPipelineOutput":
        """<p>Retrieves information about a specific telemetry pipeline, including its configuration, status, and metadata.</p>

        Args:
            pipeline_identifier: <p>The identifier (name or ARN) of the telemetry pipeline to retrieve.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_observabilityadmin.types.get_telemetry_pipeline_input.GetTelemetryPipelineInput]",
        ) -> OperationResponse[
            "capo_observabilityadmin.types.get_telemetry_pipeline_output.GetTelemetryPipelineOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.get_telemetry_pipeline

            output, http_response = (
                capo_observabilityadmin._operations.observability_admin.get_telemetry_pipeline.get_telemetry_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.get_telemetry_pipeline_input.GetTelemetryPipelineInput = {
            "pipeline_identifier": pipeline_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        pipeline_identifier: "capo_observabilityadmin.types.telemetry_pipeline_identifier.TelemetryPipelineIdentifier",
        configuration: "capo_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.update_telemetry_pipeline_output.UpdateTelemetryPipelineOutput":
        """<p>Updates the configuration of an existing telemetry pipeline.</p> <note> <p>The following attributes cannot be updated after pipeline creation:</p> <ul> <li> <p> <b>Pipeline name</b> - The pipeline name is immutable</p> </li> <li> <p> <b>Pipeline ARN</b> - The ARN is automatically generated and cannot be changed</p> </li> <li> <p> <b>Source type</b> - Once a pipeline is created with a specific source type (such as S3, CloudWatch Logs, GitHub, or third-party sources), it cannot be changed to a different source type</p> </li> </ul> <p>Processors can be added, removed, or modified. However, some processors are not supported for third-party pipelines and cannot be added through updates.</p> </note> <p> <b>Source-Specific Update Rules</b> </p> <dl> <dt>CloudWatch Logs Sources (Vended and Custom)</dt> <dd> <p> <b>Updatable:</b> <code>sts_role_arn</code> </p> <p> <b>Fixed:</b> <code>data_source_name</code>, <code>data_source_type</code>, sink (must remain <code>@original</code>)</p> </dd> <dt>S3 Sources (Crowdstrike, Zscaler, SentinelOne, Custom)</dt> <dd> <p> <b>Updatable:</b> All SQS configuration parameters, <code>sts_role_arn</code>, codec settings, compression type, bucket ownership settings, sink log group</p> <p> <b>Fixed:</b> <code>notification_type</code>, <code>aws.region</code> </p> </dd> <dt>GitHub Audit Logs</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>scope</code> (can switch between ORGANIZATION/ENTERPRISE), <code>organization</code> or <code>enterprise</code> name, <code>range</code>, authentication credentials (PAT or GitHub App)</p> </dd> <dt>Microsoft Sources (Entra ID, Office365, Windows)</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>tenant_id</code>, <code>workspace_id</code> (Windows only), OAuth2 credentials (<code>client_id</code>, <code>client_secret</code>)</p> </dd> <dt>Okta Sources (SSO, Auth0)</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>domain</code>, <code>range</code>, OAuth2 credentials (<code>client_id</code>, <code>client_secret</code>)</p> </dd> <dt>Palo Alto Networks</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>hostname</code>, basic authentication credentials (<code>username</code>, <code>password</code>)</p> </dd> <dt>ServiceNow CMDB</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>instance_url</code>, <code>range</code>, OAuth2 credentials (<code>client_id</code>, <code>client_secret</code>)</p> </dd> <dt>Wiz CNAPP</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>region</code>, <code>range</code>, OAuth2 credentials (<code>client_id</code>, <code>client_secret</code>)</p> </dd> </dl>

        Args:
            pipeline_identifier: <p>The ARN of the telemetry pipeline to update.</p>
            configuration: <p>The new configuration for the telemetry pipeline, including updated sources, processors, and destinations.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_observabilityadmin.types.update_telemetry_pipeline_input.UpdateTelemetryPipelineInput]",
        ) -> OperationResponse[
            "capo_observabilityadmin.types.update_telemetry_pipeline_output.UpdateTelemetryPipelineOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.update_telemetry_pipeline

            output, http_response = (
                capo_observabilityadmin._operations.observability_admin.update_telemetry_pipeline.update_telemetry_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.update_telemetry_pipeline_input.UpdateTelemetryPipelineInput = {
            "pipeline_identifier": pipeline_identifier,
            "configuration": configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        pipeline_identifier: "capo_observabilityadmin.types.telemetry_pipeline_identifier.TelemetryPipelineIdentifier",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.delete_telemetry_pipeline_output.DeleteTelemetryPipelineOutput":
        """<p>Deletes a telemetry pipeline and its associated resources. This operation stops data processing and removes the pipeline configuration.</p>

        Args:
            pipeline_identifier: <p>The ARN of the telemetry pipeline to delete.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.conflict_exception.ConflictException: <p> The requested operation conflicts with the current state of the specified resource or with another request. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_observabilityadmin.types.delete_telemetry_pipeline_input.DeleteTelemetryPipelineInput]",
        ) -> OperationResponse[
            "capo_observabilityadmin.types.delete_telemetry_pipeline_output.DeleteTelemetryPipelineOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.delete_telemetry_pipeline

            output, http_response = (
                capo_observabilityadmin._operations.observability_admin.delete_telemetry_pipeline.delete_telemetry_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.delete_telemetry_pipeline_input.DeleteTelemetryPipelineInput = {
            "pipeline_identifier": pipeline_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_telemetry_pipelines_max_results.ListTelemetryPipelinesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "capo_observabilityadmin.types.list_telemetry_pipelines_output.ListTelemetryPipelinesOutput":
        """<p>Returns a list of telemetry pipelines in your account. Returns up to 100 results. If more than 100 telemetry pipelines exist, include the <code>NextToken</code> value from the response to retrieve the next set of results.</p>

        Args:
            max_results: <p>The maximum number of telemetry pipelines to return in a single call.</p>
            next_token: <p>The token for the next set of results. A previous call generates this token.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_observabilityadmin.types.list_telemetry_pipelines_input.ListTelemetryPipelinesInput]",
        ) -> OperationResponse[
            "capo_observabilityadmin.types.list_telemetry_pipelines_output.ListTelemetryPipelinesOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.list_telemetry_pipelines

            output, http_response = (
                capo_observabilityadmin._operations.observability_admin.list_telemetry_pipelines.list_telemetry_pipelines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.list_telemetry_pipelines_input.ListTelemetryPipelinesInput = {}
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


class AsyncTelemetryPipelineResource:
    def __init__(self, service: AsyncObservabilityAdminClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_observabilityadmin.types.telemetry_pipeline_name.TelemetryPipelineName",
        configuration: "capo_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        tags: Optional[
            "capo_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
    ) -> "capo_observabilityadmin.types.create_telemetry_pipeline_output.CreateTelemetryPipelineOutput":
        """<p>Creates a telemetry pipeline for processing and transforming telemetry data. The pipeline defines how data flows from sources through processors to destinations, enabling data transformation and delivering capabilities. </p>

        Args:
            name: <p>The name of the telemetry pipeline to create. The name must be unique within your account.</p>
            configuration: <p>The configuration that defines how the telemetry pipeline processes data, including sources, processors, and destinations. For more information about pipeline components, see the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/pipeline-components-reference.html">Amazon CloudWatch User Guide</a> </p>
            tags: <p>The key-value pairs to associate with the telemetry pipeline resource for categorization and management purposes.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.conflict_exception.ConflictException: <p> The requested operation conflicts with the current state of the specified resource or with another request. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The requested operation would exceed the allowed quota for the specified resource type. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.create_telemetry_pipeline_input.CreateTelemetryPipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.create_telemetry_pipeline_output.CreateTelemetryPipelineOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.create_telemetry_pipeline

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.create_telemetry_pipeline.async_create_telemetry_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.create_telemetry_pipeline_input.CreateTelemetryPipelineInput = {
            "name": name,
            "configuration": configuration,
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

    async def read(
        self,
        pipeline_identifier: "capo_observabilityadmin.types.telemetry_pipeline_identifier.TelemetryPipelineIdentifier",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.get_telemetry_pipeline_output.GetTelemetryPipelineOutput":
        """<p>Retrieves information about a specific telemetry pipeline, including its configuration, status, and metadata.</p>

        Args:
            pipeline_identifier: <p>The identifier (name or ARN) of the telemetry pipeline to retrieve.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.get_telemetry_pipeline_input.GetTelemetryPipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.get_telemetry_pipeline_output.GetTelemetryPipelineOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.get_telemetry_pipeline

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.get_telemetry_pipeline.async_get_telemetry_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.get_telemetry_pipeline_input.GetTelemetryPipelineInput = {
            "pipeline_identifier": pipeline_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        pipeline_identifier: "capo_observabilityadmin.types.telemetry_pipeline_identifier.TelemetryPipelineIdentifier",
        configuration: "capo_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.update_telemetry_pipeline_output.UpdateTelemetryPipelineOutput":
        """<p>Updates the configuration of an existing telemetry pipeline.</p> <note> <p>The following attributes cannot be updated after pipeline creation:</p> <ul> <li> <p> <b>Pipeline name</b> - The pipeline name is immutable</p> </li> <li> <p> <b>Pipeline ARN</b> - The ARN is automatically generated and cannot be changed</p> </li> <li> <p> <b>Source type</b> - Once a pipeline is created with a specific source type (such as S3, CloudWatch Logs, GitHub, or third-party sources), it cannot be changed to a different source type</p> </li> </ul> <p>Processors can be added, removed, or modified. However, some processors are not supported for third-party pipelines and cannot be added through updates.</p> </note> <p> <b>Source-Specific Update Rules</b> </p> <dl> <dt>CloudWatch Logs Sources (Vended and Custom)</dt> <dd> <p> <b>Updatable:</b> <code>sts_role_arn</code> </p> <p> <b>Fixed:</b> <code>data_source_name</code>, <code>data_source_type</code>, sink (must remain <code>@original</code>)</p> </dd> <dt>S3 Sources (Crowdstrike, Zscaler, SentinelOne, Custom)</dt> <dd> <p> <b>Updatable:</b> All SQS configuration parameters, <code>sts_role_arn</code>, codec settings, compression type, bucket ownership settings, sink log group</p> <p> <b>Fixed:</b> <code>notification_type</code>, <code>aws.region</code> </p> </dd> <dt>GitHub Audit Logs</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>scope</code> (can switch between ORGANIZATION/ENTERPRISE), <code>organization</code> or <code>enterprise</code> name, <code>range</code>, authentication credentials (PAT or GitHub App)</p> </dd> <dt>Microsoft Sources (Entra ID, Office365, Windows)</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>tenant_id</code>, <code>workspace_id</code> (Windows only), OAuth2 credentials (<code>client_id</code>, <code>client_secret</code>)</p> </dd> <dt>Okta Sources (SSO, Auth0)</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>domain</code>, <code>range</code>, OAuth2 credentials (<code>client_id</code>, <code>client_secret</code>)</p> </dd> <dt>Palo Alto Networks</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>hostname</code>, basic authentication credentials (<code>username</code>, <code>password</code>)</p> </dd> <dt>ServiceNow CMDB</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>instance_url</code>, <code>range</code>, OAuth2 credentials (<code>client_id</code>, <code>client_secret</code>)</p> </dd> <dt>Wiz CNAPP</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>region</code>, <code>range</code>, OAuth2 credentials (<code>client_id</code>, <code>client_secret</code>)</p> </dd> </dl>

        Args:
            pipeline_identifier: <p>The ARN of the telemetry pipeline to update.</p>
            configuration: <p>The new configuration for the telemetry pipeline, including updated sources, processors, and destinations.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.update_telemetry_pipeline_input.UpdateTelemetryPipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.update_telemetry_pipeline_output.UpdateTelemetryPipelineOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.update_telemetry_pipeline

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.update_telemetry_pipeline.async_update_telemetry_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.update_telemetry_pipeline_input.UpdateTelemetryPipelineInput = {
            "pipeline_identifier": pipeline_identifier,
            "configuration": configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        pipeline_identifier: "capo_observabilityadmin.types.telemetry_pipeline_identifier.TelemetryPipelineIdentifier",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.delete_telemetry_pipeline_output.DeleteTelemetryPipelineOutput":
        """<p>Deletes a telemetry pipeline and its associated resources. This operation stops data processing and removes the pipeline configuration.</p>

        Args:
            pipeline_identifier: <p>The ARN of the telemetry pipeline to delete.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.conflict_exception.ConflictException: <p> The requested operation conflicts with the current state of the specified resource or with another request. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.delete_telemetry_pipeline_input.DeleteTelemetryPipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.delete_telemetry_pipeline_output.DeleteTelemetryPipelineOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.delete_telemetry_pipeline

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.delete_telemetry_pipeline.async_delete_telemetry_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.delete_telemetry_pipeline_input.DeleteTelemetryPipelineInput = {
            "pipeline_identifier": pipeline_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_telemetry_pipelines_max_results.ListTelemetryPipelinesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "capo_observabilityadmin.types.list_telemetry_pipelines_output.ListTelemetryPipelinesOutput":
        """<p>Returns a list of telemetry pipelines in your account. Returns up to 100 results. If more than 100 telemetry pipelines exist, include the <code>NextToken</code> value from the response to retrieve the next set of results.</p>

        Args:
            max_results: <p>The maximum number of telemetry pipelines to return in a single call.</p>
            next_token: <p>The token for the next set of results. A previous call generates this token.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.list_telemetry_pipelines_input.ListTelemetryPipelinesInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.list_telemetry_pipelines_output.ListTelemetryPipelinesOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.list_telemetry_pipelines

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.list_telemetry_pipelines.async_list_telemetry_pipelines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.list_telemetry_pipelines_input.ListTelemetryPipelinesInput = {}
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
