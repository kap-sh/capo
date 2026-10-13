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
    import capo_cleanrooms.types.configured_table_association_analysis_rule_policy
    import capo_cleanrooms.types.configured_table_association_analysis_rule_type
    import capo_cleanrooms.types.configured_table_association_identifier
    import capo_cleanrooms.types.configured_table_identifier
    import capo_cleanrooms.types.create_configured_table_association_analysis_rule_input
    import capo_cleanrooms.types.create_configured_table_association_analysis_rule_output
    import capo_cleanrooms.types.create_configured_table_association_input
    import capo_cleanrooms.types.create_configured_table_association_output
    import capo_cleanrooms.types.delete_configured_table_association_analysis_rule_input
    import capo_cleanrooms.types.delete_configured_table_association_analysis_rule_output
    import capo_cleanrooms.types.delete_configured_table_association_input
    import capo_cleanrooms.types.delete_configured_table_association_output
    import capo_cleanrooms.types.get_configured_table_association_analysis_rule_input
    import capo_cleanrooms.types.get_configured_table_association_analysis_rule_output
    import capo_cleanrooms.types.get_configured_table_association_input
    import capo_cleanrooms.types.get_configured_table_association_output
    import capo_cleanrooms.types.list_configured_table_associations_input
    import capo_cleanrooms.types.list_configured_table_associations_output
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.role_arn
    import capo_cleanrooms.types.table_alias
    import capo_cleanrooms.types.table_description
    import capo_cleanrooms.types.tag_map
    import capo_cleanrooms.types.update_configured_table_association_analysis_rule_input
    import capo_cleanrooms.types.update_configured_table_association_analysis_rule_output
    import capo_cleanrooms.types.update_configured_table_association_input
    import capo_cleanrooms.types.update_configured_table_association_output
    from capo_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from capo_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class ConfiguredTableAssociationResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_cleanrooms.types.table_alias.TableAlias",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        role_arn: "capo_cleanrooms.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.table_description.TableDescription"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanrooms.types.create_configured_table_association_output.CreateConfiguredTableAssociationOutput":
        """<p>Creates a configured table association. A configured table association links a configured table with a collaboration.</p>

        Args:
            name: <p>The name of the configured table association. This name is used to query the underlying configured table.</p>
            description: <p>A description for the configured table association.</p>
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The configured table is associated to the collaboration that this membership belongs to. Currently accepts a membership ID.</p>
            configured_table_identifier: <p>A unique identifier for the configured table to be associated to. Currently accepts a configured table ID.</p>
            role_arn: <p>The service will assume this role to access catalog metadata and query the table.</p>
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
            req: "OperationRequest[capo_cleanrooms.types.create_configured_table_association_input.CreateConfiguredTableAssociationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.create_configured_table_association_output.CreateConfiguredTableAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association.create_configured_table_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConfiguredTableAssociation")
        )
        input_: capo_cleanrooms.types.create_configured_table_association_input.CreateConfiguredTableAssociationInput = {
            "name": name,
            "membership_identifier": membership_identifier,
            "configured_table_identifier": configured_table_identifier,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
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
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_table_association_output.GetConfiguredTableAssociationOutput":
        """<p>Retrieves a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique ID for the configured table association to retrieve. Currently accepts the configured table ID.</p>
            membership_identifier: <p>A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_configured_table_association_input.GetConfiguredTableAssociationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_configured_table_association_output.GetConfiguredTableAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association.get_configured_table_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguredTableAssociation")
        )
        input_: capo_cleanrooms.types.get_configured_table_association_input.GetConfiguredTableAssociationInput = {
            "configured_table_association_identifier": configured_table_association_identifier,
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
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.table_description.TableDescription"
        ] = None,
        role_arn: Optional["capo_cleanrooms.types.role_arn.RoleArn"] = None,
    ) -> "capo_cleanrooms.types.update_configured_table_association_output.UpdateConfiguredTableAssociationOutput":
        """<p>Updates a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique identifier for the configured table association to update. Currently accepts the configured table association ID.</p>
            membership_identifier: <p>The unique ID for the membership that the configured table association belongs to.</p>
            description: <p>A new description for the configured table association.</p>
            role_arn: <p>The service will assume this role to access catalog metadata and query the table.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.update_configured_table_association_input.UpdateConfiguredTableAssociationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_configured_table_association_output.UpdateConfiguredTableAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association.update_configured_table_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateConfiguredTableAssociation")
        )
        input_: capo_cleanrooms.types.update_configured_table_association_input.UpdateConfiguredTableAssociationInput = {
            "configured_table_association_identifier": configured_table_association_identifier,
            "membership_identifier": membership_identifier,
        }
        if description is not None:
            input_["description"] = description
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_table_association_output.DeleteConfiguredTableAssociationOutput":
        """<p>Deletes a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique ID for the configured table association to be deleted. Currently accepts the configured table ID.</p>
            membership_identifier: <p>A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.delete_configured_table_association_input.DeleteConfiguredTableAssociationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.delete_configured_table_association_output.DeleteConfiguredTableAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association.delete_configured_table_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfiguredTableAssociation")
        )
        input_: capo_cleanrooms.types.delete_configured_table_association_input.DeleteConfiguredTableAssociationInput = {
            "configured_table_association_identifier": configured_table_association_identifier,
            "membership_identifier": membership_identifier,
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
    ) -> "capo_cleanrooms.types.list_configured_table_associations_output.ListConfiguredTableAssociationsOutput":
        """<p>Lists configured table associations for a membership.</p>

        Args:
            membership_identifier: <p>A unique identifier for the membership to list configured table associations for. Currently accepts the membership ID.</p>
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
            req: "OperationRequest[capo_cleanrooms.types.list_configured_table_associations_input.ListConfiguredTableAssociationsInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_configured_table_associations_output.ListConfiguredTableAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_table_associations

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_table_associations.list_configured_table_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConfiguredTableAssociations")
        )
        input_: capo_cleanrooms.types.list_configured_table_associations_input.ListConfiguredTableAssociationsInput = {
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

    def create_configured_table_association_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.create_configured_table_association_analysis_rule_output.CreateConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Creates a new analysis rule for an associated configured table.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The unique ID for the configured table association. Currently accepts the configured table association ID.</p>
            analysis_rule_type: <p> The type of analysis rule.</p>
            analysis_rule_policy: <p>The analysis rule policy that was created for the configured table association.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.create_configured_table_association_analysis_rule_input.CreateConfiguredTableAssociationAnalysisRuleInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.create_configured_table_association_analysis_rule_output.CreateConfiguredTableAssociationAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association_analysis_rule

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association_analysis_rule.create_configured_table_association_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateConfiguredTableAssociationAnalysisRule"),
        )
        input_: capo_cleanrooms.types.create_configured_table_association_analysis_rule_input.CreateConfiguredTableAssociationAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "configured_table_association_identifier": configured_table_association_identifier,
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

    def delete_configured_table_association_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_table_association_analysis_rule_output.DeleteConfiguredTableAssociationAnalysisRuleOutput":
        """<p>Deletes an analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p>The identiﬁer for the conﬁgured table association that's related to the analysis rule that you want to delete.</p>
            analysis_rule_type: <p>The type of the analysis rule that you want to delete.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.delete_configured_table_association_analysis_rule_input.DeleteConfiguredTableAssociationAnalysisRuleInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.delete_configured_table_association_analysis_rule_output.DeleteConfiguredTableAssociationAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association_analysis_rule

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association_analysis_rule.delete_configured_table_association_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteConfiguredTableAssociationAnalysisRule"),
        )
        input_: capo_cleanrooms.types.delete_configured_table_association_analysis_rule_input.DeleteConfiguredTableAssociationAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "configured_table_association_identifier": configured_table_association_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_configured_table_association_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_table_association_analysis_rule_output.GetConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Retrieves the analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The identiﬁer for the conﬁgured table association that's related to the analysis rule.</p>
            analysis_rule_type: <p> The type of analysis rule that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_configured_table_association_analysis_rule_input.GetConfiguredTableAssociationAnalysisRuleInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_configured_table_association_analysis_rule_output.GetConfiguredTableAssociationAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association_analysis_rule

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association_analysis_rule.get_configured_table_association_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetConfiguredTableAssociationAnalysisRule"),
        )
        input_: capo_cleanrooms.types.get_configured_table_association_analysis_rule_input.GetConfiguredTableAssociationAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "configured_table_association_identifier": configured_table_association_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_configured_table_association_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_configured_table_association_analysis_rule_output.UpdateConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Updates the analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The identifier for the configured table association to update.</p>
            analysis_rule_type: <p> The analysis rule type that you want to update.</p>
            analysis_rule_policy: <p> The updated analysis rule policy for the conﬁgured table association.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.update_configured_table_association_analysis_rule_input.UpdateConfiguredTableAssociationAnalysisRuleInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_configured_table_association_analysis_rule_output.UpdateConfiguredTableAssociationAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association_analysis_rule

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association_analysis_rule.update_configured_table_association_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateConfiguredTableAssociationAnalysisRule"),
        )
        input_: capo_cleanrooms.types.update_configured_table_association_analysis_rule_input.UpdateConfiguredTableAssociationAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "configured_table_association_identifier": configured_table_association_identifier,
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


class AsyncConfiguredTableAssociationResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_cleanrooms.types.table_alias.TableAlias",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        role_arn: "capo_cleanrooms.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.table_description.TableDescription"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanrooms.types.create_configured_table_association_output.CreateConfiguredTableAssociationOutput":
        """<p>Creates a configured table association. A configured table association links a configured table with a collaboration.</p>

        Args:
            name: <p>The name of the configured table association. This name is used to query the underlying configured table.</p>
            description: <p>A description for the configured table association.</p>
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The configured table is associated to the collaboration that this membership belongs to. Currently accepts a membership ID.</p>
            configured_table_identifier: <p>A unique identifier for the configured table to be associated to. Currently accepts a configured table ID.</p>
            role_arn: <p>The service will assume this role to access catalog metadata and query the table.</p>
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
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_configured_table_association_input.CreateConfiguredTableAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_configured_table_association_output.CreateConfiguredTableAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association.async_create_configured_table_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConfiguredTableAssociation")
        )
        input_: capo_cleanrooms.types.create_configured_table_association_input.CreateConfiguredTableAssociationInput = {
            "name": name,
            "membership_identifier": membership_identifier,
            "configured_table_identifier": configured_table_identifier,
            "role_arn": role_arn,
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

    async def read(
        self,
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_table_association_output.GetConfiguredTableAssociationOutput":
        """<p>Retrieves a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique ID for the configured table association to retrieve. Currently accepts the configured table ID.</p>
            membership_identifier: <p>A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_configured_table_association_input.GetConfiguredTableAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_configured_table_association_output.GetConfiguredTableAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association.async_get_configured_table_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguredTableAssociation")
        )
        input_: capo_cleanrooms.types.get_configured_table_association_input.GetConfiguredTableAssociationInput = {
            "configured_table_association_identifier": configured_table_association_identifier,
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
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.table_description.TableDescription"
        ] = None,
        role_arn: Optional["capo_cleanrooms.types.role_arn.RoleArn"] = None,
    ) -> "capo_cleanrooms.types.update_configured_table_association_output.UpdateConfiguredTableAssociationOutput":
        """<p>Updates a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique identifier for the configured table association to update. Currently accepts the configured table association ID.</p>
            membership_identifier: <p>The unique ID for the membership that the configured table association belongs to.</p>
            description: <p>A new description for the configured table association.</p>
            role_arn: <p>The service will assume this role to access catalog metadata and query the table.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_configured_table_association_input.UpdateConfiguredTableAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_configured_table_association_output.UpdateConfiguredTableAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association.async_update_configured_table_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateConfiguredTableAssociation")
        )
        input_: capo_cleanrooms.types.update_configured_table_association_input.UpdateConfiguredTableAssociationInput = {
            "configured_table_association_identifier": configured_table_association_identifier,
            "membership_identifier": membership_identifier,
        }
        if description is not None:
            input_["description"] = description
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_table_association_output.DeleteConfiguredTableAssociationOutput":
        """<p>Deletes a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique ID for the configured table association to be deleted. Currently accepts the configured table ID.</p>
            membership_identifier: <p>A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_configured_table_association_input.DeleteConfiguredTableAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_configured_table_association_output.DeleteConfiguredTableAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association.async_delete_configured_table_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfiguredTableAssociation")
        )
        input_: capo_cleanrooms.types.delete_configured_table_association_input.DeleteConfiguredTableAssociationInput = {
            "configured_table_association_identifier": configured_table_association_identifier,
            "membership_identifier": membership_identifier,
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
    ) -> "capo_cleanrooms.types.list_configured_table_associations_output.ListConfiguredTableAssociationsOutput":
        """<p>Lists configured table associations for a membership.</p>

        Args:
            membership_identifier: <p>A unique identifier for the membership to list configured table associations for. Currently accepts the membership ID.</p>
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
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_configured_table_associations_input.ListConfiguredTableAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_configured_table_associations_output.ListConfiguredTableAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_table_associations

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_table_associations.async_list_configured_table_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConfiguredTableAssociations")
        )
        input_: capo_cleanrooms.types.list_configured_table_associations_input.ListConfiguredTableAssociationsInput = {
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

    async def create_configured_table_association_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.create_configured_table_association_analysis_rule_output.CreateConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Creates a new analysis rule for an associated configured table.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The unique ID for the configured table association. Currently accepts the configured table association ID.</p>
            analysis_rule_type: <p> The type of analysis rule.</p>
            analysis_rule_policy: <p>The analysis rule policy that was created for the configured table association.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_configured_table_association_analysis_rule_input.CreateConfiguredTableAssociationAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_configured_table_association_analysis_rule_output.CreateConfiguredTableAssociationAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association_analysis_rule.async_create_configured_table_association_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateConfiguredTableAssociationAnalysisRule"),
        )
        input_: capo_cleanrooms.types.create_configured_table_association_analysis_rule_input.CreateConfiguredTableAssociationAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "configured_table_association_identifier": configured_table_association_identifier,
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

    async def delete_configured_table_association_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_table_association_analysis_rule_output.DeleteConfiguredTableAssociationAnalysisRuleOutput":
        """<p>Deletes an analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p>The identiﬁer for the conﬁgured table association that's related to the analysis rule that you want to delete.</p>
            analysis_rule_type: <p>The type of the analysis rule that you want to delete.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_configured_table_association_analysis_rule_input.DeleteConfiguredTableAssociationAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_configured_table_association_analysis_rule_output.DeleteConfiguredTableAssociationAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association_analysis_rule.async_delete_configured_table_association_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteConfiguredTableAssociationAnalysisRule"),
        )
        input_: capo_cleanrooms.types.delete_configured_table_association_analysis_rule_input.DeleteConfiguredTableAssociationAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "configured_table_association_identifier": configured_table_association_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configured_table_association_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_table_association_analysis_rule_output.GetConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Retrieves the analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The identiﬁer for the conﬁgured table association that's related to the analysis rule.</p>
            analysis_rule_type: <p> The type of analysis rule that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_configured_table_association_analysis_rule_input.GetConfiguredTableAssociationAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_configured_table_association_analysis_rule_output.GetConfiguredTableAssociationAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association_analysis_rule.async_get_configured_table_association_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetConfiguredTableAssociationAnalysisRule"),
        )
        input_: capo_cleanrooms.types.get_configured_table_association_analysis_rule_input.GetConfiguredTableAssociationAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "configured_table_association_identifier": configured_table_association_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configured_table_association_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_configured_table_association_analysis_rule_output.UpdateConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Updates the analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The identifier for the configured table association to update.</p>
            analysis_rule_type: <p> The analysis rule type that you want to update.</p>
            analysis_rule_policy: <p> The updated analysis rule policy for the conﬁgured table association.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_configured_table_association_analysis_rule_input.UpdateConfiguredTableAssociationAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_configured_table_association_analysis_rule_output.UpdateConfiguredTableAssociationAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association_analysis_rule.async_update_configured_table_association_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateConfiguredTableAssociationAnalysisRule"),
        )
        input_: capo_cleanrooms.types.update_configured_table_association_analysis_rule_input.UpdateConfiguredTableAssociationAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "configured_table_association_identifier": configured_table_association_identifier,
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
