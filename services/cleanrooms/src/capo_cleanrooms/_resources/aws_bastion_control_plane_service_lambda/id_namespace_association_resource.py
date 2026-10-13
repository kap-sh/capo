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
    import capo_cleanrooms.types.create_id_namespace_association_input
    import capo_cleanrooms.types.create_id_namespace_association_output
    import capo_cleanrooms.types.delete_id_namespace_association_input
    import capo_cleanrooms.types.delete_id_namespace_association_output
    import capo_cleanrooms.types.generic_resource_name
    import capo_cleanrooms.types.get_id_namespace_association_input
    import capo_cleanrooms.types.get_id_namespace_association_output
    import capo_cleanrooms.types.id_mapping_config
    import capo_cleanrooms.types.id_namespace_association_identifier
    import capo_cleanrooms.types.id_namespace_association_input_reference_config
    import capo_cleanrooms.types.id_namespace_association_summary
    import capo_cleanrooms.types.list_id_namespace_associations_input
    import capo_cleanrooms.types.list_id_namespace_associations_output
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.tag_map
    import capo_cleanrooms.types.update_id_namespace_association_input
    import capo_cleanrooms.types.update_id_namespace_association_output
    from capo_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from capo_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class IdNamespaceAssociationResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        input_reference_config: "capo_cleanrooms.types.id_namespace_association_input_reference_config.IdNamespaceAssociationInputReferenceConfig",
        name: "capo_cleanrooms.types.generic_resource_name.GenericResourceName",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        id_mapping_config: Optional[
            "capo_cleanrooms.types.id_mapping_config.IdMappingConfig"
        ] = None,
    ) -> "capo_cleanrooms.types.create_id_namespace_association_output.CreateIdNamespaceAssociationOutput":
        """<p>Creates an ID namespace association.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association.</p>
            input_reference_config: <p>The input reference configuration needed to create the ID namespace association.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            name: <p>The name for the ID namespace association.</p>
            description: <p>The description of the ID namespace association.</p>
            id_mapping_config: <p>The configuration settings for the ID mapping table.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.create_id_namespace_association_input.CreateIdNamespaceAssociationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.create_id_namespace_association_output.CreateIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_namespace_association

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_namespace_association.create_id_namespace_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateIdNamespaceAssociation")
        )
        input_: capo_cleanrooms.types.create_id_namespace_association_input.CreateIdNamespaceAssociationInput = {
            "membership_identifier": membership_identifier,
            "input_reference_config": input_reference_config,
            "name": name,
        }
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description
        if id_mapping_config is not None:
            input_["id_mapping_config"] = id_mapping_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        id_namespace_association_identifier: "capo_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_id_namespace_association_output.GetIdNamespaceAssociationOutput":
        """<p>Retrieves an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to retrieve.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_id_namespace_association_input.GetIdNamespaceAssociationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_id_namespace_association_output.GetIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_namespace_association

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_namespace_association.get_id_namespace_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetIdNamespaceAssociation")
        )
        input_: capo_cleanrooms.types.get_id_namespace_association_input.GetIdNamespaceAssociationInput = {
            "id_namespace_association_identifier": id_namespace_association_identifier,
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
        id_namespace_association_identifier: "capo_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        name: Optional[
            "capo_cleanrooms.types.generic_resource_name.GenericResourceName"
        ] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        id_mapping_config: Optional[
            "capo_cleanrooms.types.id_mapping_config.IdMappingConfig"
        ] = None,
    ) -> "capo_cleanrooms.types.update_id_namespace_association_output.UpdateIdNamespaceAssociationOutput":
        """<p>Provides the details that are necessary to update an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to update.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to update.</p>
            name: <p>A new name for the ID namespace association.</p>
            description: <p>A new description for the ID namespace association.</p>
            id_mapping_config: <p>The configuration settings for the ID mapping table.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.update_id_namespace_association_input.UpdateIdNamespaceAssociationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_id_namespace_association_output.UpdateIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_namespace_association

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_namespace_association.update_id_namespace_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateIdNamespaceAssociation")
        )
        input_: capo_cleanrooms.types.update_id_namespace_association_input.UpdateIdNamespaceAssociationInput = {
            "id_namespace_association_identifier": id_namespace_association_identifier,
            "membership_identifier": membership_identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if id_mapping_config is not None:
            input_["id_mapping_config"] = id_mapping_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id_namespace_association_identifier: "capo_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_id_namespace_association_output.DeleteIdNamespaceAssociationOutput":
        """<p>Deletes an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to delete.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to delete.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.delete_id_namespace_association_input.DeleteIdNamespaceAssociationInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.delete_id_namespace_association_output.DeleteIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_namespace_association

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_namespace_association.delete_id_namespace_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteIdNamespaceAssociation")
        )
        input_: capo_cleanrooms.types.delete_id_namespace_association_input.DeleteIdNamespaceAssociationInput = {
            "id_namespace_association_identifier": id_namespace_association_identifier,
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
    ) -> "capo_cleanrooms.types.list_id_namespace_associations_output.ListIdNamespaceAssociationsOutput":
        """<p>Returns a list of ID namespace associations.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to view.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_id_namespace_associations_input.ListIdNamespaceAssociationsInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_id_namespace_associations_output.ListIdNamespaceAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_namespace_associations

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_namespace_associations.list_id_namespace_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListIdNamespaceAssociations")
        )
        input_: capo_cleanrooms.types.list_id_namespace_associations_input.ListIdNamespaceAssociationsInput = {
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


class AsyncIdNamespaceAssociationResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        input_reference_config: "capo_cleanrooms.types.id_namespace_association_input_reference_config.IdNamespaceAssociationInputReferenceConfig",
        name: "capo_cleanrooms.types.generic_resource_name.GenericResourceName",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        id_mapping_config: Optional[
            "capo_cleanrooms.types.id_mapping_config.IdMappingConfig"
        ] = None,
    ) -> "capo_cleanrooms.types.create_id_namespace_association_output.CreateIdNamespaceAssociationOutput":
        """<p>Creates an ID namespace association.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association.</p>
            input_reference_config: <p>The input reference configuration needed to create the ID namespace association.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            name: <p>The name for the ID namespace association.</p>
            description: <p>The description of the ID namespace association.</p>
            id_mapping_config: <p>The configuration settings for the ID mapping table.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_id_namespace_association_input.CreateIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_id_namespace_association_output.CreateIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_namespace_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_namespace_association.async_create_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateIdNamespaceAssociation")
        )
        input_: capo_cleanrooms.types.create_id_namespace_association_input.CreateIdNamespaceAssociationInput = {
            "membership_identifier": membership_identifier,
            "input_reference_config": input_reference_config,
            "name": name,
        }
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description
        if id_mapping_config is not None:
            input_["id_mapping_config"] = id_mapping_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        id_namespace_association_identifier: "capo_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_id_namespace_association_output.GetIdNamespaceAssociationOutput":
        """<p>Retrieves an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to retrieve.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_id_namespace_association_input.GetIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_id_namespace_association_output.GetIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_namespace_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_namespace_association.async_get_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetIdNamespaceAssociation")
        )
        input_: capo_cleanrooms.types.get_id_namespace_association_input.GetIdNamespaceAssociationInput = {
            "id_namespace_association_identifier": id_namespace_association_identifier,
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
        id_namespace_association_identifier: "capo_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        name: Optional[
            "capo_cleanrooms.types.generic_resource_name.GenericResourceName"
        ] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        id_mapping_config: Optional[
            "capo_cleanrooms.types.id_mapping_config.IdMappingConfig"
        ] = None,
    ) -> "capo_cleanrooms.types.update_id_namespace_association_output.UpdateIdNamespaceAssociationOutput":
        """<p>Provides the details that are necessary to update an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to update.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to update.</p>
            name: <p>A new name for the ID namespace association.</p>
            description: <p>A new description for the ID namespace association.</p>
            id_mapping_config: <p>The configuration settings for the ID mapping table.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_id_namespace_association_input.UpdateIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_id_namespace_association_output.UpdateIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_namespace_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_namespace_association.async_update_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateIdNamespaceAssociation")
        )
        input_: capo_cleanrooms.types.update_id_namespace_association_input.UpdateIdNamespaceAssociationInput = {
            "id_namespace_association_identifier": id_namespace_association_identifier,
            "membership_identifier": membership_identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if id_mapping_config is not None:
            input_["id_mapping_config"] = id_mapping_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id_namespace_association_identifier: "capo_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_id_namespace_association_output.DeleteIdNamespaceAssociationOutput":
        """<p>Deletes an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to delete.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to delete.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_id_namespace_association_input.DeleteIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_id_namespace_association_output.DeleteIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_namespace_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_namespace_association.async_delete_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteIdNamespaceAssociation")
        )
        input_: capo_cleanrooms.types.delete_id_namespace_association_input.DeleteIdNamespaceAssociationInput = {
            "id_namespace_association_identifier": id_namespace_association_identifier,
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
    ) -> "capo_cleanrooms.types.list_id_namespace_associations_output.ListIdNamespaceAssociationsOutput":
        """<p>Returns a list of ID namespace associations.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to view.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_id_namespace_associations_input.ListIdNamespaceAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_id_namespace_associations_output.ListIdNamespaceAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_namespace_associations

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_namespace_associations.async_list_id_namespace_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListIdNamespaceAssociations")
        )
        input_: capo_cleanrooms.types.list_id_namespace_associations_input.ListIdNamespaceAssociationsInput = {
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
