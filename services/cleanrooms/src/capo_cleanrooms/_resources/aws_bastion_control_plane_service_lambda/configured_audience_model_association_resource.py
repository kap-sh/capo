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
    import capo_cleanrooms.types.configured_audience_model_arn
    import capo_cleanrooms.types.configured_audience_model_association_identifier
    import capo_cleanrooms.types.configured_audience_model_association_name
    import capo_cleanrooms.types.configured_audience_model_association_summary
    import capo_cleanrooms.types.create_configured_audience_model_association_input
    import capo_cleanrooms.types.create_configured_audience_model_association_output
    import capo_cleanrooms.types.delete_configured_audience_model_association_input
    import capo_cleanrooms.types.delete_configured_audience_model_association_output
    import capo_cleanrooms.types.get_configured_audience_model_association_input
    import capo_cleanrooms.types.get_configured_audience_model_association_output
    import capo_cleanrooms.types.list_configured_audience_model_associations_input
    import capo_cleanrooms.types.list_configured_audience_model_associations_output
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.tag_map
    import capo_cleanrooms.types.update_configured_audience_model_association_input
    import capo_cleanrooms.types.update_configured_audience_model_association_output
    from capo_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from capo_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class ConfiguredAudienceModelAssociationResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_audience_model_arn: "capo_cleanrooms.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        configured_audience_model_association_name: "capo_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName",
        manage_resource_policies: bool,
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_cleanrooms.types.create_configured_audience_model_association_output.CreateConfiguredAudienceModelAssociationOutput":
        """<p>Provides the details necessary to create a configured audience model association.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The configured audience model is associated to the collaboration that this membership belongs to. Accepts a membership ID.</p>
            configured_audience_model_arn: <p>A unique identifier for the configured audience model that you want to associate.</p>
            configured_audience_model_association_name: <p>The name of the configured audience model association.</p>
            manage_resource_policies: <p>When <code>TRUE</code>, indicates that the resource policy for the configured audience model resource being associated is configured for Clean Rooms to manage permissions related to the given collaboration. When <code>FALSE</code>, indicates that the configured audience model resource owner will manage permissions related to the given collaboration.</p> <p>Setting this to <code>TRUE</code> requires you to have permissions to create, update, and delete the resource policy for the <code>cleanrooms-ml</code> resource when you call the <a>DeleteConfiguredAudienceModelAssociation</a> resource. In addition, if you are the collaboration creator and specify <code>TRUE</code>, you must have the same permissions when you call the <a>DeleteMember</a> and <a>DeleteCollaboration</a> APIs.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            description: <p>A description of the configured audience model association.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.create_configured_audience_model_association_input.CreateConfiguredAudienceModelAssociationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.create_configured_audience_model_association_output.CreateConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_audience_model_association

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_audience_model_association.create_configured_audience_model_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateConfiguredAudienceModelAssociation"),
        )
        input_: capo_cleanrooms.types.create_configured_audience_model_association_input.CreateConfiguredAudienceModelAssociationInput = {
            "membership_identifier": membership_identifier,
            "configured_audience_model_arn": configured_audience_model_arn,
            "configured_audience_model_association_name": configured_audience_model_association_name,
            "manage_resource_policies": manage_resource_policies,
        }
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_audience_model_association_output.GetConfiguredAudienceModelAssociationOutput":
        """<p>Returns information about a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to retrieve.</p>
            membership_identifier: <p>A unique identifier for the membership that contains the configured audience model association that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_configured_audience_model_association_input.GetConfiguredAudienceModelAssociationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_configured_audience_model_association_output.GetConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_audience_model_association

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_audience_model_association.get_configured_audience_model_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguredAudienceModelAssociation")
        )
        input_: capo_cleanrooms.types.get_configured_audience_model_association_input.GetConfiguredAudienceModelAssociationInput = {
            "configured_audience_model_association_identifier": configured_audience_model_association_identifier,
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
        configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        name: Optional[
            "capo_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName"
        ] = None,
    ) -> "capo_cleanrooms.types.update_configured_audience_model_association_output.UpdateConfiguredAudienceModelAssociationOutput":
        """<p>Provides the details necessary to update a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to update.</p>
            membership_identifier: <p>A unique identifier of the membership that contains the configured audience model association that you want to update.</p>
            description: <p>A new description for the configured audience model association.</p>
            name: <p>A new name for the configured audience model association.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.update_configured_audience_model_association_input.UpdateConfiguredAudienceModelAssociationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_configured_audience_model_association_output.UpdateConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_audience_model_association

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_audience_model_association.update_configured_audience_model_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateConfiguredAudienceModelAssociation"),
        )
        input_: capo_cleanrooms.types.update_configured_audience_model_association_input.UpdateConfiguredAudienceModelAssociationInput = {
            "configured_audience_model_association_identifier": configured_audience_model_association_identifier,
            "membership_identifier": membership_identifier,
        }
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_audience_model_association_output.DeleteConfiguredAudienceModelAssociationOutput":
        """<p>Provides the information necessary to delete a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier of the configured audience model association that you want to delete.</p>
            membership_identifier: <p>A unique identifier of the membership that contains the audience model association that you want to delete.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.delete_configured_audience_model_association_input.DeleteConfiguredAudienceModelAssociationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.delete_configured_audience_model_association_output.DeleteConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_audience_model_association

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_audience_model_association.delete_configured_audience_model_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteConfiguredAudienceModelAssociation"),
        )
        input_: capo_cleanrooms.types.delete_configured_audience_model_association_input.DeleteConfiguredAudienceModelAssociationInput = {
            "configured_audience_model_association_identifier": configured_audience_model_association_identifier,
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
    ) -> "capo_cleanrooms.types.list_configured_audience_model_associations_output.ListConfiguredAudienceModelAssociationsOutput":
        """<p>Lists information about requested configured audience model associations.</p>

        Args:
            membership_identifier: <p>A unique identifier for a membership that contains the configured audience model associations that you want to retrieve.</p>
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
            req: "OperationRequest[capo_cleanrooms.types.list_configured_audience_model_associations_input.ListConfiguredAudienceModelAssociationsInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_configured_audience_model_associations_output.ListConfiguredAudienceModelAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_audience_model_associations

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_audience_model_associations.list_configured_audience_model_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListConfiguredAudienceModelAssociations"),
        )
        input_: capo_cleanrooms.types.list_configured_audience_model_associations_input.ListConfiguredAudienceModelAssociationsInput = {
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


class AsyncConfiguredAudienceModelAssociationResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_audience_model_arn: "capo_cleanrooms.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        configured_audience_model_association_name: "capo_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName",
        manage_resource_policies: bool,
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_cleanrooms.types.create_configured_audience_model_association_output.CreateConfiguredAudienceModelAssociationOutput":
        """<p>Provides the details necessary to create a configured audience model association.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The configured audience model is associated to the collaboration that this membership belongs to. Accepts a membership ID.</p>
            configured_audience_model_arn: <p>A unique identifier for the configured audience model that you want to associate.</p>
            configured_audience_model_association_name: <p>The name of the configured audience model association.</p>
            manage_resource_policies: <p>When <code>TRUE</code>, indicates that the resource policy for the configured audience model resource being associated is configured for Clean Rooms to manage permissions related to the given collaboration. When <code>FALSE</code>, indicates that the configured audience model resource owner will manage permissions related to the given collaboration.</p> <p>Setting this to <code>TRUE</code> requires you to have permissions to create, update, and delete the resource policy for the <code>cleanrooms-ml</code> resource when you call the <a>DeleteConfiguredAudienceModelAssociation</a> resource. In addition, if you are the collaboration creator and specify <code>TRUE</code>, you must have the same permissions when you call the <a>DeleteMember</a> and <a>DeleteCollaboration</a> APIs.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            description: <p>A description of the configured audience model association.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_configured_audience_model_association_input.CreateConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_configured_audience_model_association_output.CreateConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_audience_model_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_audience_model_association.async_create_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateConfiguredAudienceModelAssociation"),
        )
        input_: capo_cleanrooms.types.create_configured_audience_model_association_input.CreateConfiguredAudienceModelAssociationInput = {
            "membership_identifier": membership_identifier,
            "configured_audience_model_arn": configured_audience_model_arn,
            "configured_audience_model_association_name": configured_audience_model_association_name,
            "manage_resource_policies": manage_resource_policies,
        }
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_audience_model_association_output.GetConfiguredAudienceModelAssociationOutput":
        """<p>Returns information about a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to retrieve.</p>
            membership_identifier: <p>A unique identifier for the membership that contains the configured audience model association that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_configured_audience_model_association_input.GetConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_configured_audience_model_association_output.GetConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_audience_model_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_audience_model_association.async_get_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguredAudienceModelAssociation")
        )
        input_: capo_cleanrooms.types.get_configured_audience_model_association_input.GetConfiguredAudienceModelAssociationInput = {
            "configured_audience_model_association_identifier": configured_audience_model_association_identifier,
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
        configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        name: Optional[
            "capo_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName"
        ] = None,
    ) -> "capo_cleanrooms.types.update_configured_audience_model_association_output.UpdateConfiguredAudienceModelAssociationOutput":
        """<p>Provides the details necessary to update a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to update.</p>
            membership_identifier: <p>A unique identifier of the membership that contains the configured audience model association that you want to update.</p>
            description: <p>A new description for the configured audience model association.</p>
            name: <p>A new name for the configured audience model association.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_configured_audience_model_association_input.UpdateConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_configured_audience_model_association_output.UpdateConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_audience_model_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_audience_model_association.async_update_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateConfiguredAudienceModelAssociation"),
        )
        input_: capo_cleanrooms.types.update_configured_audience_model_association_input.UpdateConfiguredAudienceModelAssociationInput = {
            "configured_audience_model_association_identifier": configured_audience_model_association_identifier,
            "membership_identifier": membership_identifier,
        }
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_audience_model_association_output.DeleteConfiguredAudienceModelAssociationOutput":
        """<p>Provides the information necessary to delete a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier of the configured audience model association that you want to delete.</p>
            membership_identifier: <p>A unique identifier of the membership that contains the audience model association that you want to delete.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_configured_audience_model_association_input.DeleteConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_configured_audience_model_association_output.DeleteConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_audience_model_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_audience_model_association.async_delete_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteConfiguredAudienceModelAssociation"),
        )
        input_: capo_cleanrooms.types.delete_configured_audience_model_association_input.DeleteConfiguredAudienceModelAssociationInput = {
            "configured_audience_model_association_identifier": configured_audience_model_association_identifier,
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
    ) -> "capo_cleanrooms.types.list_configured_audience_model_associations_output.ListConfiguredAudienceModelAssociationsOutput":
        """<p>Lists information about requested configured audience model associations.</p>

        Args:
            membership_identifier: <p>A unique identifier for a membership that contains the configured audience model associations that you want to retrieve.</p>
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
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_configured_audience_model_associations_input.ListConfiguredAudienceModelAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_configured_audience_model_associations_output.ListConfiguredAudienceModelAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_audience_model_associations

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_audience_model_associations.async_list_configured_audience_model_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListConfiguredAudienceModelAssociations"),
        )
        input_: capo_cleanrooms.types.list_configured_audience_model_associations_input.ListConfiguredAudienceModelAssociationsInput = {
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
