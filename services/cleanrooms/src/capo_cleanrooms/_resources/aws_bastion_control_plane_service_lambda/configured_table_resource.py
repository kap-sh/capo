from __future__ import annotations

from typing import TYPE_CHECKING, Optional

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
    import capo_cleanrooms.types.allowed_column_list
    import capo_cleanrooms.types.analysis_method
    import capo_cleanrooms.types.configured_table_analysis_rule_policy
    import capo_cleanrooms.types.configured_table_analysis_rule_type
    import capo_cleanrooms.types.configured_table_identifier
    import capo_cleanrooms.types.create_configured_table_analysis_rule_input
    import capo_cleanrooms.types.create_configured_table_analysis_rule_output
    import capo_cleanrooms.types.create_configured_table_input
    import capo_cleanrooms.types.create_configured_table_output
    import capo_cleanrooms.types.delete_configured_table_analysis_rule_input
    import capo_cleanrooms.types.delete_configured_table_analysis_rule_output
    import capo_cleanrooms.types.delete_configured_table_input
    import capo_cleanrooms.types.delete_configured_table_output
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.get_configured_table_analysis_rule_input
    import capo_cleanrooms.types.get_configured_table_analysis_rule_output
    import capo_cleanrooms.types.get_configured_table_input
    import capo_cleanrooms.types.get_configured_table_output
    import capo_cleanrooms.types.list_configured_tables_input
    import capo_cleanrooms.types.list_configured_tables_output
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.selected_analysis_methods
    import capo_cleanrooms.types.table_description
    import capo_cleanrooms.types.table_reference
    import capo_cleanrooms.types.tag_map
    import capo_cleanrooms.types.update_configured_table_analysis_rule_input
    import capo_cleanrooms.types.update_configured_table_analysis_rule_output
    import capo_cleanrooms.types.update_configured_table_input
    import capo_cleanrooms.types.update_configured_table_output
    from capo_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from capo_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class ConfiguredTableResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_cleanrooms.types.display_name.DisplayName",
        table_reference: "capo_cleanrooms.types.table_reference.TableReference",
        allowed_columns: "capo_cleanrooms.types.allowed_column_list.AllowedColumnList",
        analysis_method: "capo_cleanrooms.types.analysis_method.AnalysisMethod",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.table_description.TableDescription"
        ] = None,
        selected_analysis_methods: Optional[
            "capo_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanrooms.types.create_configured_table_output.CreateConfiguredTableOutput":
        """<p>Creates a new configured table resource.</p>

        Args:
            name: <p>The name of the configured table.</p>
            description: <p>A description for the configured table.</p>
            table_reference: <p>A reference to the table being configured.</p>
            allowed_columns: <p>The columns of the underlying table that can be used by collaborations or analysis rules.</p>
            analysis_method: <p>The analysis method allowed for the configured tables.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>
            selected_analysis_methods: <p> The analysis methods to enable for the configured table. When configured, you must specify at least two analysis methods.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.create_configured_table_input.CreateConfiguredTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.create_configured_table_output.CreateConfiguredTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table.create_configured_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConfiguredTable")
        )
        input_: capo_cleanrooms.types.create_configured_table_input.CreateConfiguredTableInput = {
            "name": name,
            "table_reference": table_reference,
            "allowed_columns": allowed_columns,
            "analysis_method": analysis_method,
        }
        if description is not None:
            input_["description"] = description
        if selected_analysis_methods is not None:
            input_["selected_analysis_methods"] = selected_analysis_methods
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
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_table_output.GetConfiguredTableOutput":
        """<p>Retrieves a configured table.</p>

        Args:
            configured_table_identifier: <p>The unique ID for the configured table to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_configured_table_input.GetConfiguredTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_configured_table_output.GetConfiguredTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table.get_configured_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguredTable")
        )
        input_: capo_cleanrooms.types.get_configured_table_input.GetConfiguredTableInput = {
            "configured_table_identifier": configured_table_identifier
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
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        name: Optional["capo_cleanrooms.types.display_name.DisplayName"] = None,
        description: Optional[
            "capo_cleanrooms.types.table_description.TableDescription"
        ] = None,
        table_reference: Optional[
            "capo_cleanrooms.types.table_reference.TableReference"
        ] = None,
        allowed_columns: Optional[
            "capo_cleanrooms.types.allowed_column_list.AllowedColumnList"
        ] = None,
        analysis_method: Optional[
            "capo_cleanrooms.types.analysis_method.AnalysisMethod"
        ] = None,
        selected_analysis_methods: Optional[
            "capo_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
        ] = None,
    ) -> "capo_cleanrooms.types.update_configured_table_output.UpdateConfiguredTableOutput":
        """<p>Updates a configured table.</p>

        Args:
            configured_table_identifier: <p>The identifier for the configured table to update. Currently accepts the configured table ID.</p>
            name: <p>A new name for the configured table.</p>
            description: <p>A new description for the configured table.</p>
            allowed_columns: <p>The columns of the underlying table that can be used by collaborations or analysis rules.</p>
            analysis_method: <p> The analysis method for the configured table.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>
            selected_analysis_methods: <p> The selected analysis methods for the table configuration update.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.update_configured_table_input.UpdateConfiguredTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_configured_table_output.UpdateConfiguredTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table.update_configured_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateConfiguredTable")
        )
        input_: capo_cleanrooms.types.update_configured_table_input.UpdateConfiguredTableInput = {
            "configured_table_identifier": configured_table_identifier
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if table_reference is not None:
            input_["table_reference"] = table_reference
        if allowed_columns is not None:
            input_["allowed_columns"] = allowed_columns
        if analysis_method is not None:
            input_["analysis_method"] = analysis_method
        if selected_analysis_methods is not None:
            input_["selected_analysis_methods"] = selected_analysis_methods

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_table_output.DeleteConfiguredTableOutput":
        """<p>Deletes a configured table.</p>

        Args:
            configured_table_identifier: <p>The unique ID for the configured table to delete.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.delete_configured_table_input.DeleteConfiguredTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.delete_configured_table_output.DeleteConfiguredTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table.delete_configured_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfiguredTable")
        )
        input_: capo_cleanrooms.types.delete_configured_table_input.DeleteConfiguredTableInput = {
            "configured_table_identifier": configured_table_identifier
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
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_cleanrooms.types.list_configured_tables_output.ListConfiguredTablesOutput"
    ):
        """<p>Lists configured tables.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_configured_tables_input.ListConfiguredTablesInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_configured_tables_output.ListConfiguredTablesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_tables

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_tables.list_configured_tables(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConfiguredTables")
        )
        input_: capo_cleanrooms.types.list_configured_tables_input.ListConfiguredTablesInput = {}
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

    def create_configured_table_analysis_rule(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.create_configured_table_analysis_rule_output.CreateConfiguredTableAnalysisRuleOutput":
        """<p>Creates a new analysis rule for a configured table. Currently, only one analysis rule can be created for a given configured table.</p>

        Args:
            configured_table_identifier: <p>The identifier for the configured table to create the analysis rule for. Currently accepts the configured table ID. </p>
            analysis_rule_type: <p>The type of analysis rule.</p>
            analysis_rule_policy: <p>The analysis rule policy that was created for the configured table.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.create_configured_table_analysis_rule_input.CreateConfiguredTableAnalysisRuleInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.create_configured_table_analysis_rule_output.CreateConfiguredTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_analysis_rule

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_analysis_rule.create_configured_table_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConfiguredTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.create_configured_table_analysis_rule_input.CreateConfiguredTableAnalysisRuleInput = {
            "configured_table_identifier": configured_table_identifier,
            "analysis_rule_type": analysis_rule_type,
            "analysis_rule_policy": analysis_rule_policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_configured_table_analysis_rule(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_table_analysis_rule_output.DeleteConfiguredTableAnalysisRuleOutput":
        """<p>Deletes a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule type to be deleted. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.delete_configured_table_analysis_rule_input.DeleteConfiguredTableAnalysisRuleInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.delete_configured_table_analysis_rule_output.DeleteConfiguredTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_analysis_rule

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_analysis_rule.delete_configured_table_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfiguredTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.delete_configured_table_analysis_rule_input.DeleteConfiguredTableAnalysisRuleInput = {
            "configured_table_identifier": configured_table_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_configured_table_analysis_rule(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_table_analysis_rule_output.GetConfiguredTableAnalysisRuleOutput":
        """<p>Retrieves a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table to retrieve. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule to be retrieved. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_configured_table_analysis_rule_input.GetConfiguredTableAnalysisRuleInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_configured_table_analysis_rule_output.GetConfiguredTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_analysis_rule

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_analysis_rule.get_configured_table_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguredTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.get_configured_table_analysis_rule_input.GetConfiguredTableAnalysisRuleInput = {
            "configured_table_identifier": configured_table_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_configured_table_analysis_rule(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_configured_table_analysis_rule_output.UpdateConfiguredTableAnalysisRuleOutput":
        """<p>Updates a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule type to be updated. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>
            analysis_rule_policy: <p>The new analysis rule policy for the configured table analysis rule.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.update_configured_table_analysis_rule_input.UpdateConfiguredTableAnalysisRuleInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_configured_table_analysis_rule_output.UpdateConfiguredTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_analysis_rule

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_analysis_rule.update_configured_table_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateConfiguredTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.update_configured_table_analysis_rule_input.UpdateConfiguredTableAnalysisRuleInput = {
            "configured_table_identifier": configured_table_identifier,
            "analysis_rule_type": analysis_rule_type,
            "analysis_rule_policy": analysis_rule_policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncConfiguredTableResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_cleanrooms.types.display_name.DisplayName",
        table_reference: "capo_cleanrooms.types.table_reference.TableReference",
        allowed_columns: "capo_cleanrooms.types.allowed_column_list.AllowedColumnList",
        analysis_method: "capo_cleanrooms.types.analysis_method.AnalysisMethod",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.table_description.TableDescription"
        ] = None,
        selected_analysis_methods: Optional[
            "capo_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanrooms.types.create_configured_table_output.CreateConfiguredTableOutput":
        """<p>Creates a new configured table resource.</p>

        Args:
            name: <p>The name of the configured table.</p>
            description: <p>A description for the configured table.</p>
            table_reference: <p>A reference to the table being configured.</p>
            allowed_columns: <p>The columns of the underlying table that can be used by collaborations or analysis rules.</p>
            analysis_method: <p>The analysis method allowed for the configured tables.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>
            selected_analysis_methods: <p> The analysis methods to enable for the configured table. When configured, you must specify at least two analysis methods.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_configured_table_input.CreateConfiguredTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_configured_table_output.CreateConfiguredTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table.async_create_configured_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConfiguredTable")
        )
        input_: capo_cleanrooms.types.create_configured_table_input.CreateConfiguredTableInput = {
            "name": name,
            "table_reference": table_reference,
            "allowed_columns": allowed_columns,
            "analysis_method": analysis_method,
        }
        if description is not None:
            input_["description"] = description
        if selected_analysis_methods is not None:
            input_["selected_analysis_methods"] = selected_analysis_methods
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
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_table_output.GetConfiguredTableOutput":
        """<p>Retrieves a configured table.</p>

        Args:
            configured_table_identifier: <p>The unique ID for the configured table to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_configured_table_input.GetConfiguredTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_configured_table_output.GetConfiguredTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table.async_get_configured_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguredTable")
        )
        input_: capo_cleanrooms.types.get_configured_table_input.GetConfiguredTableInput = {
            "configured_table_identifier": configured_table_identifier
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
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        name: Optional["capo_cleanrooms.types.display_name.DisplayName"] = None,
        description: Optional[
            "capo_cleanrooms.types.table_description.TableDescription"
        ] = None,
        table_reference: Optional[
            "capo_cleanrooms.types.table_reference.TableReference"
        ] = None,
        allowed_columns: Optional[
            "capo_cleanrooms.types.allowed_column_list.AllowedColumnList"
        ] = None,
        analysis_method: Optional[
            "capo_cleanrooms.types.analysis_method.AnalysisMethod"
        ] = None,
        selected_analysis_methods: Optional[
            "capo_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
        ] = None,
    ) -> "capo_cleanrooms.types.update_configured_table_output.UpdateConfiguredTableOutput":
        """<p>Updates a configured table.</p>

        Args:
            configured_table_identifier: <p>The identifier for the configured table to update. Currently accepts the configured table ID.</p>
            name: <p>A new name for the configured table.</p>
            description: <p>A new description for the configured table.</p>
            allowed_columns: <p>The columns of the underlying table that can be used by collaborations or analysis rules.</p>
            analysis_method: <p> The analysis method for the configured table.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>
            selected_analysis_methods: <p> The selected analysis methods for the table configuration update.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_configured_table_input.UpdateConfiguredTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_configured_table_output.UpdateConfiguredTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table.async_update_configured_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateConfiguredTable")
        )
        input_: capo_cleanrooms.types.update_configured_table_input.UpdateConfiguredTableInput = {
            "configured_table_identifier": configured_table_identifier
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if table_reference is not None:
            input_["table_reference"] = table_reference
        if allowed_columns is not None:
            input_["allowed_columns"] = allowed_columns
        if analysis_method is not None:
            input_["analysis_method"] = analysis_method
        if selected_analysis_methods is not None:
            input_["selected_analysis_methods"] = selected_analysis_methods

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_table_output.DeleteConfiguredTableOutput":
        """<p>Deletes a configured table.</p>

        Args:
            configured_table_identifier: <p>The unique ID for the configured table to delete.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_configured_table_input.DeleteConfiguredTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_configured_table_output.DeleteConfiguredTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table.async_delete_configured_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfiguredTable")
        )
        input_: capo_cleanrooms.types.delete_configured_table_input.DeleteConfiguredTableInput = {
            "configured_table_identifier": configured_table_identifier
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
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_cleanrooms.types.list_configured_tables_output.ListConfiguredTablesOutput"
    ):
        """<p>Lists configured tables.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_configured_tables_input.ListConfiguredTablesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_configured_tables_output.ListConfiguredTablesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_tables

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_tables.async_list_configured_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConfiguredTables")
        )
        input_: capo_cleanrooms.types.list_configured_tables_input.ListConfiguredTablesInput = {}
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

    async def create_configured_table_analysis_rule(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.create_configured_table_analysis_rule_output.CreateConfiguredTableAnalysisRuleOutput":
        """<p>Creates a new analysis rule for a configured table. Currently, only one analysis rule can be created for a given configured table.</p>

        Args:
            configured_table_identifier: <p>The identifier for the configured table to create the analysis rule for. Currently accepts the configured table ID. </p>
            analysis_rule_type: <p>The type of analysis rule.</p>
            analysis_rule_policy: <p>The analysis rule policy that was created for the configured table.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_configured_table_analysis_rule_input.CreateConfiguredTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_configured_table_analysis_rule_output.CreateConfiguredTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_analysis_rule.async_create_configured_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConfiguredTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.create_configured_table_analysis_rule_input.CreateConfiguredTableAnalysisRuleInput = {
            "configured_table_identifier": configured_table_identifier,
            "analysis_rule_type": analysis_rule_type,
            "analysis_rule_policy": analysis_rule_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configured_table_analysis_rule(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_table_analysis_rule_output.DeleteConfiguredTableAnalysisRuleOutput":
        """<p>Deletes a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule type to be deleted. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_configured_table_analysis_rule_input.DeleteConfiguredTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_configured_table_analysis_rule_output.DeleteConfiguredTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_analysis_rule.async_delete_configured_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfiguredTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.delete_configured_table_analysis_rule_input.DeleteConfiguredTableAnalysisRuleInput = {
            "configured_table_identifier": configured_table_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configured_table_analysis_rule(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_table_analysis_rule_output.GetConfiguredTableAnalysisRuleOutput":
        """<p>Retrieves a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table to retrieve. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule to be retrieved. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_configured_table_analysis_rule_input.GetConfiguredTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_configured_table_analysis_rule_output.GetConfiguredTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_analysis_rule.async_get_configured_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguredTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.get_configured_table_analysis_rule_input.GetConfiguredTableAnalysisRuleInput = {
            "configured_table_identifier": configured_table_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configured_table_analysis_rule(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_configured_table_analysis_rule_output.UpdateConfiguredTableAnalysisRuleOutput":
        """<p>Updates a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule type to be updated. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>
            analysis_rule_policy: <p>The new analysis rule policy for the configured table analysis rule.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_configured_table_analysis_rule_input.UpdateConfiguredTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_configured_table_analysis_rule_output.UpdateConfiguredTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_analysis_rule.async_update_configured_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateConfiguredTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.update_configured_table_analysis_rule_input.UpdateConfiguredTableAnalysisRuleInput = {
            "configured_table_identifier": configured_table_identifier,
            "analysis_rule_type": analysis_rule_type,
            "analysis_rule_policy": analysis_rule_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
