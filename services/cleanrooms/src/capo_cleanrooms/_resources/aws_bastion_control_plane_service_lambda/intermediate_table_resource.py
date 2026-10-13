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
    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.create_intermediate_table_analysis_rule_input
    import capo_cleanrooms.types.create_intermediate_table_analysis_rule_output
    import capo_cleanrooms.types.create_intermediate_table_input
    import capo_cleanrooms.types.create_intermediate_table_output
    import capo_cleanrooms.types.delete_intermediate_table_analysis_rule_input
    import capo_cleanrooms.types.delete_intermediate_table_analysis_rule_output
    import capo_cleanrooms.types.delete_intermediate_table_input
    import capo_cleanrooms.types.delete_intermediate_table_output
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.get_intermediate_table_analysis_rule_input
    import capo_cleanrooms.types.get_intermediate_table_analysis_rule_output
    import capo_cleanrooms.types.get_intermediate_table_input
    import capo_cleanrooms.types.get_intermediate_table_output
    import capo_cleanrooms.types.intermediate_table_analysis_rule_policy
    import capo_cleanrooms.types.intermediate_table_analysis_rule_type
    import capo_cleanrooms.types.intermediate_table_column_list
    import capo_cleanrooms.types.intermediate_table_compute_configuration
    import capo_cleanrooms.types.intermediate_table_identifier
    import capo_cleanrooms.types.intermediate_table_summary
    import capo_cleanrooms.types.intermediate_table_version_summary
    import capo_cleanrooms.types.kms_key_arn
    import capo_cleanrooms.types.list_intermediate_table_versions_input
    import capo_cleanrooms.types.list_intermediate_table_versions_output
    import capo_cleanrooms.types.list_intermediate_tables_input
    import capo_cleanrooms.types.list_intermediate_tables_output
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.parameter_map
    import capo_cleanrooms.types.populate_intermediate_table_input
    import capo_cleanrooms.types.populate_intermediate_table_output
    import capo_cleanrooms.types.population_analysis_configuration
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.tag_map
    import capo_cleanrooms.types.update_intermediate_table_analysis_rule_input
    import capo_cleanrooms.types.update_intermediate_table_analysis_rule_output
    import capo_cleanrooms.types.update_intermediate_table_input
    import capo_cleanrooms.types.update_intermediate_table_output
    from capo_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from capo_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class IntermediateTableResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        name: "capo_cleanrooms.types.display_name.DisplayName",
        population_analysis_configuration: "capo_cleanrooms.types.population_analysis_configuration.PopulationAnalysisConfiguration",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        kms_key_arn: Optional["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None,
        retention_in_days: Optional[int] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanrooms.types.create_intermediate_table_output.CreateIntermediateTableOutput":
        """<p>Creates an intermediate table in a membership. The intermediate table is owned by the member with the CAN_QUERY ability. To populate the table with results, use <code>PopulateIntermediateTable</code>.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership where the intermediate table is created.</p>
            name: <p>The display name for the intermediate table.</p>
            description: <p>A description of the intermediate table.</p>
            population_analysis_configuration: <p>The configuration that defines the analysis used to populate the intermediate table.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the customer-managed KMS key used to encrypt the intermediate table data.</p>
            retention_in_days: <p>The number of days to retain populated data versions.</p>
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
            req: "OperationRequest[capo_cleanrooms.types.create_intermediate_table_input.CreateIntermediateTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.create_intermediate_table_output.CreateIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_intermediate_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_intermediate_table.create_intermediate_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_cleanrooms.types.create_intermediate_table_input.CreateIntermediateTableInput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.create_intermediate_table_input

            return (
                capo_cleanrooms.types.create_intermediate_table_input.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_cleanrooms.types.create_intermediate_table_output.CreateIntermediateTableOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.create_intermediate_table_output

            return (
                capo_cleanrooms.types.create_intermediate_table_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateIntermediateTable",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_cleanrooms.types.create_intermediate_table_input.CreateIntermediateTableInput = {
            "membership_identifier": membership_identifier,
            "name": name,
            "population_analysis_configuration": population_analysis_configuration,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if retention_in_days is not None:
            input_["retention_in_days"] = retention_in_days
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
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> (
        "capo_cleanrooms.types.get_intermediate_table_output.GetIntermediateTableOutput"
    ):
        """<p>Retrieves an intermediate table. Returns the full details of the intermediate table, including schema, table dependencies, inherited constraints, child resources, and status. Only the intermediate table owner can call this operation.</p>

        Args:
            intermediate_table_identifier: <p>The unique identifier of the intermediate table to retrieve.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_intermediate_table_input.GetIntermediateTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_intermediate_table_output.GetIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_intermediate_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_intermediate_table.get_intermediate_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanrooms.types.get_intermediate_table_output.GetIntermediateTableOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.get_intermediate_table_output

            return capo_cleanrooms.types.get_intermediate_table_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetIntermediateTable", redact_output=_redact_output),
        )
        input_: capo_cleanrooms.types.get_intermediate_table_input.GetIntermediateTableInput = {
            "intermediate_table_identifier": intermediate_table_identifier,
            "membership_identifier": membership_identifier,
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
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        kms_key_arn: Optional["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None,
        columns: Optional[
            "capo_cleanrooms.types.intermediate_table_column_list.IntermediateTableColumnList"
        ] = None,
    ) -> "capo_cleanrooms.types.update_intermediate_table_output.UpdateIntermediateTableOutput":
        """<p>Updates an intermediate table. You can update the description, KMS key ARN, and column types of existing columns. Only the intermediate table owner can call this operation.</p>

        Args:
            intermediate_table_identifier: <p>The unique identifier of the intermediate table to update.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            description: <p>A new description for the intermediate table.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the customer-managed KMS key to use for encrypting future population data.</p>
            columns: <p>The list of columns with updated type definitions. Only the type of existing columns can be updated.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.update_intermediate_table_input.UpdateIntermediateTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_intermediate_table_output.UpdateIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_intermediate_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_intermediate_table.update_intermediate_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanrooms.types.update_intermediate_table_output.UpdateIntermediateTableOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.update_intermediate_table_output

            return (
                capo_cleanrooms.types.update_intermediate_table_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateIntermediateTable", redact_output=_redact_output),
        )
        input_: capo_cleanrooms.types.update_intermediate_table_input.UpdateIntermediateTableInput = {
            "intermediate_table_identifier": intermediate_table_identifier,
            "membership_identifier": membership_identifier,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if columns is not None:
            input_["columns"] = columns

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
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_intermediate_table_output.DeleteIntermediateTableOutput":
        """<p>Deletes an intermediate table. The delete is idempotent. Only the intermediate table owner can call this operation.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table to delete.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.delete_intermediate_table_input.DeleteIntermediateTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.delete_intermediate_table_output.DeleteIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_intermediate_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_intermediate_table.delete_intermediate_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteIntermediateTable")
        )
        input_: capo_cleanrooms.types.delete_intermediate_table_input.DeleteIntermediateTableInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
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
    ) -> "capo_cleanrooms.types.list_intermediate_tables_output.ListIntermediateTablesOutput":
        """<p>Lists intermediate tables owned by the caller in a membership. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership for which to list intermediate tables.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a <code>nextToken</code> even if the <code>maxResults</code> value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_intermediate_tables_input.ListIntermediateTablesInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_intermediate_tables_output.ListIntermediateTablesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_intermediate_tables

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_intermediate_tables.list_intermediate_tables(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListIntermediateTables")
        )
        input_: capo_cleanrooms.types.list_intermediate_tables_input.ListIntermediateTablesInput = {
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

    def create_intermediate_table_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.intermediate_table_analysis_rule_policy.IntermediateTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.create_intermediate_table_analysis_rule_output.CreateIntermediateTableAnalysisRuleOutput":
        """<p>Creates an analysis rule for an intermediate table. Only the CUSTOM analysis rule type is supported. Only the intermediate table owner can call this operation.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table for which to create the analysis rule.</p>
            analysis_rule_type: <p>The type of analysis rule to create. Currently, only <code>CUSTOM</code> is supported.</p>
            analysis_rule_policy: <p>The analysis rule policy to apply to the intermediate table.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.create_intermediate_table_analysis_rule_input.CreateIntermediateTableAnalysisRuleInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.create_intermediate_table_analysis_rule_output.CreateIntermediateTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_intermediate_table_analysis_rule

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_intermediate_table_analysis_rule.create_intermediate_table_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateIntermediateTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.create_intermediate_table_analysis_rule_input.CreateIntermediateTableAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
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

    def delete_intermediate_table_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_intermediate_table_analysis_rule_output.DeleteIntermediateTableAnalysisRuleOutput":
        """<p>Deletes an analysis rule from an intermediate table. After the analysis rule is deleted, the intermediate table becomes unqueryable until a new analysis rule is attached. Only the intermediate table owner can call this operation.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table from which to delete the analysis rule.</p>
            analysis_rule_type: <p>The type of analysis rule to delete. Currently, only <code>CUSTOM</code> is supported.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.delete_intermediate_table_analysis_rule_input.DeleteIntermediateTableAnalysisRuleInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.delete_intermediate_table_analysis_rule_output.DeleteIntermediateTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_intermediate_table_analysis_rule

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_intermediate_table_analysis_rule.delete_intermediate_table_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteIntermediateTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.delete_intermediate_table_analysis_rule_input.DeleteIntermediateTableAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_intermediate_table_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_intermediate_table_analysis_rule_output.GetIntermediateTableAnalysisRuleOutput":
        """<p>Retrieves the analysis rule for an intermediate table.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table for which to retrieve the analysis rule.</p>
            analysis_rule_type: <p>The type of analysis rule to retrieve. Currently, only <code>CUSTOM</code> is supported.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_intermediate_table_analysis_rule_input.GetIntermediateTableAnalysisRuleInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_intermediate_table_analysis_rule_output.GetIntermediateTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_intermediate_table_analysis_rule

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_intermediate_table_analysis_rule.get_intermediate_table_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetIntermediateTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.get_intermediate_table_analysis_rule_input.GetIntermediateTableAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_intermediate_table_versions(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_intermediate_table_versions_output.ListIntermediateTableVersionsOutput":
        """<p>Lists the version history of an intermediate table. Each call to <code>PopulateIntermediateTable</code> creates a new version. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table for which to list versions.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a <code>nextToken</code> even if the <code>maxResults</code> value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_intermediate_table_versions_input.ListIntermediateTableVersionsInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_intermediate_table_versions_output.ListIntermediateTableVersionsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_intermediate_table_versions

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_intermediate_table_versions.list_intermediate_table_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListIntermediateTableVersions")
        )
        input_: capo_cleanrooms.types.list_intermediate_table_versions_input.ListIntermediateTableVersionsInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
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

    def populate_intermediate_table(
        self,
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        parameters: Optional["capo_cleanrooms.types.parameter_map.ParameterMap"] = None,
        compute_configuration: Optional[
            "capo_cleanrooms.types.intermediate_table_compute_configuration.IntermediateTableComputeConfiguration"
        ] = None,
        analysis_payer_account_id: Optional[
            "capo_cleanrooms.types.account_id.AccountId"
        ] = None,
    ) -> "capo_cleanrooms.types.populate_intermediate_table_output.PopulateIntermediateTableOutput":
        """<p>Runs the stored query of an intermediate table and makes the results available for querying. Each call creates a new version. Use <code>GetProtectedQuery</code> with the returned analysis ID to track progress. Only the intermediate table owner can call this operation.</p>

        Args:
            intermediate_table_identifier: <p>The unique identifier of the intermediate table to populate.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            parameters: <p>The runtime parameter values that override the defaults in the stored query.</p>
            compute_configuration: <p>The compute configuration for the population query execution.</p>
            analysis_payer_account_id: <p>The account ID of the member that pays for the analysis compute costs.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.populate_intermediate_table_input.PopulateIntermediateTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.populate_intermediate_table_output.PopulateIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_intermediate_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_intermediate_table.populate_intermediate_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_cleanrooms.types.populate_intermediate_table_input.PopulateIntermediateTableInput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.populate_intermediate_table_input

            return capo_cleanrooms.types.populate_intermediate_table_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("PopulateIntermediateTable", redact_input=_redact_input),
        )
        input_: capo_cleanrooms.types.populate_intermediate_table_input.PopulateIntermediateTableInput = {
            "intermediate_table_identifier": intermediate_table_identifier,
            "membership_identifier": membership_identifier,
        }
        if parameters is not None:
            input_["parameters"] = parameters
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if analysis_payer_account_id is not None:
            input_["analysis_payer_account_id"] = analysis_payer_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_intermediate_table_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.intermediate_table_analysis_rule_policy.IntermediateTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_intermediate_table_analysis_rule_output.UpdateIntermediateTableAnalysisRuleOutput":
        """<p>Updates the analysis rule policy for an intermediate table. Only the intermediate table owner can call this operation.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table for which to update the analysis rule.</p>
            analysis_rule_type: <p>The type of analysis rule to update. Currently, only <code>CUSTOM</code> is supported.</p>
            analysis_rule_policy: <p>The updated analysis rule policy for the intermediate table.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.update_intermediate_table_analysis_rule_input.UpdateIntermediateTableAnalysisRuleInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_intermediate_table_analysis_rule_output.UpdateIntermediateTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_intermediate_table_analysis_rule

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_intermediate_table_analysis_rule.update_intermediate_table_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateIntermediateTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.update_intermediate_table_analysis_rule_input.UpdateIntermediateTableAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
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


class AsyncIntermediateTableResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        name: "capo_cleanrooms.types.display_name.DisplayName",
        population_analysis_configuration: "capo_cleanrooms.types.population_analysis_configuration.PopulationAnalysisConfiguration",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        kms_key_arn: Optional["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None,
        retention_in_days: Optional[int] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanrooms.types.create_intermediate_table_output.CreateIntermediateTableOutput":
        """<p>Creates an intermediate table in a membership. The intermediate table is owned by the member with the CAN_QUERY ability. To populate the table with results, use <code>PopulateIntermediateTable</code>.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership where the intermediate table is created.</p>
            name: <p>The display name for the intermediate table.</p>
            description: <p>A description of the intermediate table.</p>
            population_analysis_configuration: <p>The configuration that defines the analysis used to populate the intermediate table.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the customer-managed KMS key used to encrypt the intermediate table data.</p>
            retention_in_days: <p>The number of days to retain populated data versions.</p>
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
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_intermediate_table_input.CreateIntermediateTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_intermediate_table_output.CreateIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_intermediate_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_intermediate_table.async_create_intermediate_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_cleanrooms.types.create_intermediate_table_input.CreateIntermediateTableInput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.create_intermediate_table_input

            return (
                capo_cleanrooms.types.create_intermediate_table_input.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_cleanrooms.types.create_intermediate_table_output.CreateIntermediateTableOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.create_intermediate_table_output

            return (
                capo_cleanrooms.types.create_intermediate_table_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateIntermediateTable",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_cleanrooms.types.create_intermediate_table_input.CreateIntermediateTableInput = {
            "membership_identifier": membership_identifier,
            "name": name,
            "population_analysis_configuration": population_analysis_configuration,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if retention_in_days is not None:
            input_["retention_in_days"] = retention_in_days
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
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> (
        "capo_cleanrooms.types.get_intermediate_table_output.GetIntermediateTableOutput"
    ):
        """<p>Retrieves an intermediate table. Returns the full details of the intermediate table, including schema, table dependencies, inherited constraints, child resources, and status. Only the intermediate table owner can call this operation.</p>

        Args:
            intermediate_table_identifier: <p>The unique identifier of the intermediate table to retrieve.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_intermediate_table_input.GetIntermediateTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_intermediate_table_output.GetIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_intermediate_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_intermediate_table.async_get_intermediate_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanrooms.types.get_intermediate_table_output.GetIntermediateTableOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.get_intermediate_table_output

            return capo_cleanrooms.types.get_intermediate_table_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetIntermediateTable", redact_output=_redact_output),
        )
        input_: capo_cleanrooms.types.get_intermediate_table_input.GetIntermediateTableInput = {
            "intermediate_table_identifier": intermediate_table_identifier,
            "membership_identifier": membership_identifier,
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
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        kms_key_arn: Optional["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None,
        columns: Optional[
            "capo_cleanrooms.types.intermediate_table_column_list.IntermediateTableColumnList"
        ] = None,
    ) -> "capo_cleanrooms.types.update_intermediate_table_output.UpdateIntermediateTableOutput":
        """<p>Updates an intermediate table. You can update the description, KMS key ARN, and column types of existing columns. Only the intermediate table owner can call this operation.</p>

        Args:
            intermediate_table_identifier: <p>The unique identifier of the intermediate table to update.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            description: <p>A new description for the intermediate table.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the customer-managed KMS key to use for encrypting future population data.</p>
            columns: <p>The list of columns with updated type definitions. Only the type of existing columns can be updated.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_intermediate_table_input.UpdateIntermediateTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_intermediate_table_output.UpdateIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_intermediate_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_intermediate_table.async_update_intermediate_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanrooms.types.update_intermediate_table_output.UpdateIntermediateTableOutput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.update_intermediate_table_output

            return (
                capo_cleanrooms.types.update_intermediate_table_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateIntermediateTable", redact_output=_redact_output),
        )
        input_: capo_cleanrooms.types.update_intermediate_table_input.UpdateIntermediateTableInput = {
            "intermediate_table_identifier": intermediate_table_identifier,
            "membership_identifier": membership_identifier,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if columns is not None:
            input_["columns"] = columns

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
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_intermediate_table_output.DeleteIntermediateTableOutput":
        """<p>Deletes an intermediate table. The delete is idempotent. Only the intermediate table owner can call this operation.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table to delete.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_intermediate_table_input.DeleteIntermediateTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_intermediate_table_output.DeleteIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_intermediate_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_intermediate_table.async_delete_intermediate_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteIntermediateTable")
        )
        input_: capo_cleanrooms.types.delete_intermediate_table_input.DeleteIntermediateTableInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
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
    ) -> "capo_cleanrooms.types.list_intermediate_tables_output.ListIntermediateTablesOutput":
        """<p>Lists intermediate tables owned by the caller in a membership. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership for which to list intermediate tables.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a <code>nextToken</code> even if the <code>maxResults</code> value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_intermediate_tables_input.ListIntermediateTablesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_intermediate_tables_output.ListIntermediateTablesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_intermediate_tables

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_intermediate_tables.async_list_intermediate_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListIntermediateTables")
        )
        input_: capo_cleanrooms.types.list_intermediate_tables_input.ListIntermediateTablesInput = {
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

    async def create_intermediate_table_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.intermediate_table_analysis_rule_policy.IntermediateTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.create_intermediate_table_analysis_rule_output.CreateIntermediateTableAnalysisRuleOutput":
        """<p>Creates an analysis rule for an intermediate table. Only the CUSTOM analysis rule type is supported. Only the intermediate table owner can call this operation.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table for which to create the analysis rule.</p>
            analysis_rule_type: <p>The type of analysis rule to create. Currently, only <code>CUSTOM</code> is supported.</p>
            analysis_rule_policy: <p>The analysis rule policy to apply to the intermediate table.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_intermediate_table_analysis_rule_input.CreateIntermediateTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_intermediate_table_analysis_rule_output.CreateIntermediateTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_intermediate_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_intermediate_table_analysis_rule.async_create_intermediate_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateIntermediateTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.create_intermediate_table_analysis_rule_input.CreateIntermediateTableAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
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

    async def delete_intermediate_table_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_intermediate_table_analysis_rule_output.DeleteIntermediateTableAnalysisRuleOutput":
        """<p>Deletes an analysis rule from an intermediate table. After the analysis rule is deleted, the intermediate table becomes unqueryable until a new analysis rule is attached. Only the intermediate table owner can call this operation.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table from which to delete the analysis rule.</p>
            analysis_rule_type: <p>The type of analysis rule to delete. Currently, only <code>CUSTOM</code> is supported.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_intermediate_table_analysis_rule_input.DeleteIntermediateTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_intermediate_table_analysis_rule_output.DeleteIntermediateTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_intermediate_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_intermediate_table_analysis_rule.async_delete_intermediate_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteIntermediateTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.delete_intermediate_table_analysis_rule_input.DeleteIntermediateTableAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_intermediate_table_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_intermediate_table_analysis_rule_output.GetIntermediateTableAnalysisRuleOutput":
        """<p>Retrieves the analysis rule for an intermediate table.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table for which to retrieve the analysis rule.</p>
            analysis_rule_type: <p>The type of analysis rule to retrieve. Currently, only <code>CUSTOM</code> is supported.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_intermediate_table_analysis_rule_input.GetIntermediateTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_intermediate_table_analysis_rule_output.GetIntermediateTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_intermediate_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_intermediate_table_analysis_rule.async_get_intermediate_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetIntermediateTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.get_intermediate_table_analysis_rule_input.GetIntermediateTableAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_intermediate_table_versions(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_intermediate_table_versions_output.ListIntermediateTableVersionsOutput":
        """<p>Lists the version history of an intermediate table. Each call to <code>PopulateIntermediateTable</code> creates a new version. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table for which to list versions.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a <code>nextToken</code> even if the <code>maxResults</code> value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_intermediate_table_versions_input.ListIntermediateTableVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_intermediate_table_versions_output.ListIntermediateTableVersionsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_intermediate_table_versions

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_intermediate_table_versions.async_list_intermediate_table_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListIntermediateTableVersions")
        )
        input_: capo_cleanrooms.types.list_intermediate_table_versions_input.ListIntermediateTableVersionsInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
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

    async def populate_intermediate_table(
        self,
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        parameters: Optional["capo_cleanrooms.types.parameter_map.ParameterMap"] = None,
        compute_configuration: Optional[
            "capo_cleanrooms.types.intermediate_table_compute_configuration.IntermediateTableComputeConfiguration"
        ] = None,
        analysis_payer_account_id: Optional[
            "capo_cleanrooms.types.account_id.AccountId"
        ] = None,
    ) -> "capo_cleanrooms.types.populate_intermediate_table_output.PopulateIntermediateTableOutput":
        """<p>Runs the stored query of an intermediate table and makes the results available for querying. Each call creates a new version. Use <code>GetProtectedQuery</code> with the returned analysis ID to track progress. Only the intermediate table owner can call this operation.</p>

        Args:
            intermediate_table_identifier: <p>The unique identifier of the intermediate table to populate.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            parameters: <p>The runtime parameter values that override the defaults in the stored query.</p>
            compute_configuration: <p>The compute configuration for the population query execution.</p>
            analysis_payer_account_id: <p>The account ID of the member that pays for the analysis compute costs.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.populate_intermediate_table_input.PopulateIntermediateTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.populate_intermediate_table_output.PopulateIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_intermediate_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_intermediate_table.async_populate_intermediate_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_cleanrooms.types.populate_intermediate_table_input.PopulateIntermediateTableInput",
        ) -> dict[str, Any]:
            import capo_cleanrooms.types.populate_intermediate_table_input

            return capo_cleanrooms.types.populate_intermediate_table_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("PopulateIntermediateTable", redact_input=_redact_input),
        )
        input_: capo_cleanrooms.types.populate_intermediate_table_input.PopulateIntermediateTableInput = {
            "intermediate_table_identifier": intermediate_table_identifier,
            "membership_identifier": membership_identifier,
        }
        if parameters is not None:
            input_["parameters"] = parameters
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if analysis_payer_account_id is not None:
            input_["analysis_payer_account_id"] = analysis_payer_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_intermediate_table_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.intermediate_table_analysis_rule_policy.IntermediateTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_intermediate_table_analysis_rule_output.UpdateIntermediateTableAnalysisRuleOutput":
        """<p>Updates the analysis rule policy for an intermediate table. Only the intermediate table owner can call this operation.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table for which to update the analysis rule.</p>
            analysis_rule_type: <p>The type of analysis rule to update. Currently, only <code>CUSTOM</code> is supported.</p>
            analysis_rule_policy: <p>The updated analysis rule policy for the intermediate table.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_intermediate_table_analysis_rule_input.UpdateIntermediateTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_intermediate_table_analysis_rule_output.UpdateIntermediateTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_intermediate_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_intermediate_table_analysis_rule.async_update_intermediate_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateIntermediateTableAnalysisRule")
        )
        input_: capo_cleanrooms.types.update_intermediate_table_analysis_rule_input.UpdateIntermediateTableAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
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
