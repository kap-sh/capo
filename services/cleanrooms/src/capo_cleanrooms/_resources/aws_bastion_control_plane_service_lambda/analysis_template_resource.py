from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_cleanrooms._auth._signers
import capo_cleanrooms._auth._sigv4
from capo_cleanrooms._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_format
    import capo_cleanrooms.types.analysis_parameter_list
    import capo_cleanrooms.types.analysis_schema
    import capo_cleanrooms.types.analysis_source
    import capo_cleanrooms.types.analysis_template_identifier
    import capo_cleanrooms.types.create_analysis_template_input
    import capo_cleanrooms.types.create_analysis_template_output
    import capo_cleanrooms.types.delete_analysis_template_input
    import capo_cleanrooms.types.delete_analysis_template_output
    import capo_cleanrooms.types.error_message_configuration
    import capo_cleanrooms.types.get_analysis_template_input
    import capo_cleanrooms.types.get_analysis_template_output
    import capo_cleanrooms.types.list_analysis_templates_input
    import capo_cleanrooms.types.list_analysis_templates_output
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.synthetic_data_parameters
    import capo_cleanrooms.types.table_alias
    import capo_cleanrooms.types.tag_map
    import capo_cleanrooms.types.update_analysis_template_input
    import capo_cleanrooms.types.update_analysis_template_output
    from capo_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from capo_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class AnalysisTemplateResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        name: "capo_cleanrooms.types.table_alias.TableAlias",
        format: "capo_cleanrooms.types.analysis_format.AnalysisFormat",
        source: "capo_cleanrooms.types.analysis_source.AnalysisSource",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        analysis_parameters: Optional[
            "capo_cleanrooms.types.analysis_parameter_list.AnalysisParameterList"
        ] = None,
        schema: Optional["capo_cleanrooms.types.analysis_schema.AnalysisSchema"] = None,
        error_message_configuration: Optional[
            "capo_cleanrooms.types.error_message_configuration.ErrorMessageConfiguration"
        ] = None,
        synthetic_data_parameters: Optional[
            "capo_cleanrooms.types.synthetic_data_parameters.SyntheticDataParameters"
        ] = None,
    ) -> "capo_cleanrooms.types.create_analysis_template_output.CreateAnalysisTemplateOutput":
        """<p>Creates a new analysis template.</p>

        Args:
            description: <p>The description of the analysis template.</p>
            membership_identifier: <p>The identifier for a membership resource.</p>
            name: <p>The name of the analysis template.</p>
            format: <p>The format of the analysis template.</p>
            source: <p>The information in the analysis template.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            analysis_parameters: <p>The parameters of the analysis template.</p>
            error_message_configuration: <p>The configuration that specifies the level of detail in error messages returned by analyses using this template. When set to <code>DETAILED</code>, error messages include more information to help troubleshoot issues with PySpark jobs. Detailed error messages may expose underlying data, including sensitive information. Recommended for faster troubleshooting in development and testing environments.</p>
            synthetic_data_parameters: <p>The parameters for generating synthetic data when running the analysis template.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.create_analysis_template_input.CreateAnalysisTemplateInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.create_analysis_template_output.CreateAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_analysis_template

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_analysis_template.create_analysis_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_cleanrooms.types.create_analysis_template_input.CreateAnalysisTemplateInput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.create_analysis_template_input

            return (
                capo_cleanrooms.types.create_analysis_template_input.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_cleanrooms.types.create_analysis_template_output.CreateAnalysisTemplateOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.create_analysis_template_output

            return (
                capo_cleanrooms.types.create_analysis_template_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAnalysisTemplate",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_cleanrooms.types.create_analysis_template_input.CreateAnalysisTemplateInput = {
            "membership_identifier": membership_identifier,
            "name": name,
            "format": format,
            "source": source,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if analysis_parameters is not None:
            input_["analysis_parameters"] = analysis_parameters
        if schema is not None:
            input_["schema"] = schema
        if error_message_configuration is not None:
            input_["error_message_configuration"] = error_message_configuration
        if synthetic_data_parameters is not None:
            input_["synthetic_data_parameters"] = synthetic_data_parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "capo_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_analysis_template_output.GetAnalysisTemplateOutput":
        """<p>Retrieves an analysis template.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_analysis_template_input.GetAnalysisTemplateInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_analysis_template_output.GetAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_template

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_template.get_analysis_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanrooms.types.get_analysis_template_output.GetAnalysisTemplateOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.get_analysis_template_output

            return capo_cleanrooms.types.get_analysis_template_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAnalysisTemplate", redact_output=_redact_output),
        )
        input_: capo_cleanrooms.types.get_analysis_template_input.GetAnalysisTemplateInput = {
            "membership_identifier": membership_identifier,
            "analysis_template_identifier": analysis_template_identifier,
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
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "capo_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_cleanrooms.types.update_analysis_template_output.UpdateAnalysisTemplateOutput":
        """<p>Updates the analysis template metadata.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>
            description: <p>A new description for the analysis template.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.update_analysis_template_input.UpdateAnalysisTemplateInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_analysis_template_output.UpdateAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_analysis_template

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_analysis_template.update_analysis_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanrooms.types.update_analysis_template_output.UpdateAnalysisTemplateOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.update_analysis_template_output

            return (
                capo_cleanrooms.types.update_analysis_template_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateAnalysisTemplate", redact_output=_redact_output),
        )
        input_: capo_cleanrooms.types.update_analysis_template_input.UpdateAnalysisTemplateInput = {
            "membership_identifier": membership_identifier,
            "analysis_template_identifier": analysis_template_identifier,
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

    def delete(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "capo_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_analysis_template_output.DeleteAnalysisTemplateOutput":
        """<p>Deletes an analysis template.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.delete_analysis_template_input.DeleteAnalysisTemplateInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.delete_analysis_template_output.DeleteAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_analysis_template

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_analysis_template.delete_analysis_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAnalysisTemplate")
        )
        input_: capo_cleanrooms.types.delete_analysis_template_input.DeleteAnalysisTemplateInput = {
            "membership_identifier": membership_identifier,
            "analysis_template_identifier": analysis_template_identifier,
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
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_analysis_templates_output.ListAnalysisTemplatesOutput":
        """<p>Lists analysis templates that the caller owns.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_analysis_templates_input.ListAnalysisTemplatesInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_analysis_templates_output.ListAnalysisTemplatesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_templates

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_templates.list_analysis_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAnalysisTemplates")
        )
        input_: capo_cleanrooms.types.list_analysis_templates_input.ListAnalysisTemplatesInput = {
            "membership_identifier": membership_identifier
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


class AsyncAnalysisTemplateResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        name: "capo_cleanrooms.types.table_alias.TableAlias",
        format: "capo_cleanrooms.types.analysis_format.AnalysisFormat",
        source: "capo_cleanrooms.types.analysis_source.AnalysisSource",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        analysis_parameters: Optional[
            "capo_cleanrooms.types.analysis_parameter_list.AnalysisParameterList"
        ] = None,
        schema: Optional["capo_cleanrooms.types.analysis_schema.AnalysisSchema"] = None,
        error_message_configuration: Optional[
            "capo_cleanrooms.types.error_message_configuration.ErrorMessageConfiguration"
        ] = None,
        synthetic_data_parameters: Optional[
            "capo_cleanrooms.types.synthetic_data_parameters.SyntheticDataParameters"
        ] = None,
    ) -> "capo_cleanrooms.types.create_analysis_template_output.CreateAnalysisTemplateOutput":
        """<p>Creates a new analysis template.</p>

        Args:
            description: <p>The description of the analysis template.</p>
            membership_identifier: <p>The identifier for a membership resource.</p>
            name: <p>The name of the analysis template.</p>
            format: <p>The format of the analysis template.</p>
            source: <p>The information in the analysis template.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            analysis_parameters: <p>The parameters of the analysis template.</p>
            error_message_configuration: <p>The configuration that specifies the level of detail in error messages returned by analyses using this template. When set to <code>DETAILED</code>, error messages include more information to help troubleshoot issues with PySpark jobs. Detailed error messages may expose underlying data, including sensitive information. Recommended for faster troubleshooting in development and testing environments.</p>
            synthetic_data_parameters: <p>The parameters for generating synthetic data when running the analysis template.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_analysis_template_input.CreateAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_analysis_template_output.CreateAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_analysis_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_analysis_template.async_create_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_cleanrooms.types.create_analysis_template_input.CreateAnalysisTemplateInput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.create_analysis_template_input

            return (
                capo_cleanrooms.types.create_analysis_template_input.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_cleanrooms.types.create_analysis_template_output.CreateAnalysisTemplateOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.create_analysis_template_output

            return (
                capo_cleanrooms.types.create_analysis_template_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAnalysisTemplate",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_cleanrooms.types.create_analysis_template_input.CreateAnalysisTemplateInput = {
            "membership_identifier": membership_identifier,
            "name": name,
            "format": format,
            "source": source,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if analysis_parameters is not None:
            input_["analysis_parameters"] = analysis_parameters
        if schema is not None:
            input_["schema"] = schema
        if error_message_configuration is not None:
            input_["error_message_configuration"] = error_message_configuration
        if synthetic_data_parameters is not None:
            input_["synthetic_data_parameters"] = synthetic_data_parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "capo_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_analysis_template_output.GetAnalysisTemplateOutput":
        """<p>Retrieves an analysis template.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_analysis_template_input.GetAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_analysis_template_output.GetAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_template.async_get_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanrooms.types.get_analysis_template_output.GetAnalysisTemplateOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.get_analysis_template_output

            return capo_cleanrooms.types.get_analysis_template_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAnalysisTemplate", redact_output=_redact_output),
        )
        input_: capo_cleanrooms.types.get_analysis_template_input.GetAnalysisTemplateInput = {
            "membership_identifier": membership_identifier,
            "analysis_template_identifier": analysis_template_identifier,
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
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "capo_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_cleanrooms.types.update_analysis_template_output.UpdateAnalysisTemplateOutput":
        """<p>Updates the analysis template metadata.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>
            description: <p>A new description for the analysis template.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_analysis_template_input.UpdateAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_analysis_template_output.UpdateAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_analysis_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_analysis_template.async_update_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanrooms.types.update_analysis_template_output.UpdateAnalysisTemplateOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.update_analysis_template_output

            return (
                capo_cleanrooms.types.update_analysis_template_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateAnalysisTemplate", redact_output=_redact_output),
        )
        input_: capo_cleanrooms.types.update_analysis_template_input.UpdateAnalysisTemplateInput = {
            "membership_identifier": membership_identifier,
            "analysis_template_identifier": analysis_template_identifier,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "capo_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_analysis_template_output.DeleteAnalysisTemplateOutput":
        """<p>Deletes an analysis template.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_analysis_template_input.DeleteAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_analysis_template_output.DeleteAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_analysis_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_analysis_template.async_delete_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAnalysisTemplate")
        )
        input_: capo_cleanrooms.types.delete_analysis_template_input.DeleteAnalysisTemplateInput = {
            "membership_identifier": membership_identifier,
            "analysis_template_identifier": analysis_template_identifier,
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
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_analysis_templates_output.ListAnalysisTemplatesOutput":
        """<p>Lists analysis templates that the caller owns.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_analysis_templates_input.ListAnalysisTemplatesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_analysis_templates_output.ListAnalysisTemplatesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_templates

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_templates.async_list_analysis_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAnalysisTemplates")
        )
        input_: capo_cleanrooms.types.list_analysis_templates_input.ListAnalysisTemplatesInput = {
            "membership_identifier": membership_identifier
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
