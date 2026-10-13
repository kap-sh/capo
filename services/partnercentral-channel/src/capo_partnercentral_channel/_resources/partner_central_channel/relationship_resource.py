from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_partnercentral_channel._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.account_id
    import capo_partnercentral_channel.types.account_id_list
    import capo_partnercentral_channel.types.association_type
    import capo_partnercentral_channel.types.association_type_list
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.client_token
    import capo_partnercentral_channel.types.create_relationship_request
    import capo_partnercentral_channel.types.create_relationship_response
    import capo_partnercentral_channel.types.delete_relationship_request
    import capo_partnercentral_channel.types.delete_relationship_response
    import capo_partnercentral_channel.types.get_relationship_request
    import capo_partnercentral_channel.types.get_relationship_response
    import capo_partnercentral_channel.types.list_relationships_request
    import capo_partnercentral_channel.types.list_relationships_response
    import capo_partnercentral_channel.types.list_relationships_sort_base
    import capo_partnercentral_channel.types.next_token
    import capo_partnercentral_channel.types.program_management_account_identifier
    import capo_partnercentral_channel.types.program_management_account_identifier_list
    import capo_partnercentral_channel.types.relationship_display_name
    import capo_partnercentral_channel.types.relationship_display_name_list
    import capo_partnercentral_channel.types.relationship_identifier
    import capo_partnercentral_channel.types.relationship_summary
    import capo_partnercentral_channel.types.resale_account_model
    import capo_partnercentral_channel.types.revision
    import capo_partnercentral_channel.types.sector
    import capo_partnercentral_channel.types.support_plan
    import capo_partnercentral_channel.types.tag_list
    import capo_partnercentral_channel.types.update_relationship_request
    import capo_partnercentral_channel.types.update_relationship_response
    from capo_partnercentral_channel._services.async_partner_central_channel import (
        AsyncPartnerCentralChannelClient,
        AsyncPartnerCentralChannelClientConfig,
    )
    from capo_partnercentral_channel._services.partner_central_channel import (
        PartnerCentralChannelClient,
        PartnerCentralChannelClientConfig,
    )


class RelationshipResource:
    def __init__(self, service: PartnerCentralChannelClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        association_type: "capo_partnercentral_channel.types.association_type.AssociationType",
        program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        associated_account_id: "capo_partnercentral_channel.types.account_id.AccountId",
        display_name: "capo_partnercentral_channel.types.relationship_display_name.RelationshipDisplayName",
        sector: "capo_partnercentral_channel.types.sector.Sector",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        resale_account_model: Optional[
            "capo_partnercentral_channel.types.resale_account_model.ResaleAccountModel"
        ] = None,
        client_token: Optional[
            "capo_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_partnercentral_channel.types.tag_list.TagList"] = None,
        requested_support_plan: Optional[
            "capo_partnercentral_channel.types.support_plan.SupportPlan"
        ] = None,
    ) -> "capo_partnercentral_channel.types.create_relationship_response.CreateRelationshipResponse":
        """<p>Creates a new partner relationship between accounts.</p>

        Args:
            catalog: <p>The catalog identifier for the relationship.</p>
            association_type: <p>The type of association for the relationship (e.g., reseller, distributor).</p>
            program_management_account_identifier: <p>The identifier of the program management account for this relationship.</p>
            associated_account_id: <p>The AWS account ID to associate in this relationship.</p>
            display_name: <p>A human-readable name for the relationship.</p>
            resale_account_model: <p>The resale account model for the relationship.</p>
            sector: <p>The business sector for the relationship.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>Key-value pairs to associate with the relationship.</p>
            requested_support_plan: <p>The support plan requested for this relationship.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for CreateRelationship

            >>> client.create(catalog='AWS', association_type='DOWNSTREAM_SELLER', program_management_account_identifier='pma-u8ic702rtzng8', associated_account_id='987654321012', display_name='TestDisplayName', resale_account_model='END_CUSTOMER', sector='COMMERCIAL', client_token='clientToken')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.create_relationship_request.CreateRelationshipRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.create_relationship_response.CreateRelationshipResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.create_relationship

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.create_relationship.create_relationship(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateRelationship")
        )
        input_: capo_partnercentral_channel.types.create_relationship_request.CreateRelationshipRequest = {
            "catalog": catalog,
            "association_type": association_type,
            "program_management_account_identifier": program_management_account_identifier,
            "associated_account_id": associated_account_id,
            "display_name": display_name,
            "sector": sector,
        }
        if resale_account_model is not None:
            input_["resale_account_model"] = resale_account_model
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if requested_support_plan is not None:
            input_["requested_support_plan"] = requested_support_plan

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        identifier: "capo_partnercentral_channel.types.relationship_identifier.RelationshipIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
    ) -> "capo_partnercentral_channel.types.get_relationship_response.GetRelationshipResponse":
        """<p>Retrieves details of a specific partner relationship.</p>

        Args:
            catalog: <p>The catalog identifier for the relationship.</p>
            program_management_account_identifier: <p>The identifier of the program management account associated with the relationship.</p>
            identifier: <p>The unique identifier of the relationship to retrieve.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for GetRelationship

            >>> client.read(catalog='AWS', program_management_account_identifier='pma-u8ic702rtzng8', identifier='rs-l9o4fj3b5zb91')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.get_relationship_request.GetRelationshipRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.get_relationship_response.GetRelationshipResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.get_relationship

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.get_relationship.get_relationship(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRelationship")
        )
        input_: capo_partnercentral_channel.types.get_relationship_request.GetRelationshipRequest = {
            "catalog": catalog,
            "program_management_account_identifier": program_management_account_identifier,
            "identifier": identifier,
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
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.relationship_identifier.RelationshipIdentifier",
        program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        revision: Optional[
            "capo_partnercentral_channel.types.revision.Revision"
        ] = None,
        display_name: Optional[
            "capo_partnercentral_channel.types.relationship_display_name.RelationshipDisplayName"
        ] = None,
        requested_support_plan: Optional[
            "capo_partnercentral_channel.types.support_plan.SupportPlan"
        ] = None,
    ) -> "capo_partnercentral_channel.types.update_relationship_response.UpdateRelationshipResponse":
        """<p>Updates the properties of a partner relationship.</p>

        Args:
            catalog: <p>The catalog identifier for the relationship.</p>
            identifier: <p>The unique identifier of the relationship to update.</p>
            program_management_account_identifier: <p>The identifier of the program management account associated with the relationship.</p>
            revision: <p>The current revision number of the relationship.</p>
            display_name: <p>The new display name for the relationship.</p>
            requested_support_plan: <p>The updated support plan for the relationship.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for UpdateRelationship

            >>> client.update(catalog='AWS', program_management_account_identifier='pma-u8ic702rtzng8', identifier='rs-l9o4fj3b5zb91', revision='3', display_name='TestDisplayName')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.update_relationship_request.UpdateRelationshipRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.update_relationship_response.UpdateRelationshipResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.update_relationship

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.update_relationship.update_relationship(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateRelationship")
        )
        input_: capo_partnercentral_channel.types.update_relationship_request.UpdateRelationshipRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "program_management_account_identifier": program_management_account_identifier,
        }
        if revision is not None:
            input_["revision"] = revision
        if display_name is not None:
            input_["display_name"] = display_name
        if requested_support_plan is not None:
            input_["requested_support_plan"] = requested_support_plan

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.relationship_identifier.RelationshipIdentifier",
        program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_channel.types.delete_relationship_response.DeleteRelationshipResponse":
        """<p>Deletes a partner relationship.</p>

        Args:
            catalog: <p>The catalog identifier for the relationship.</p>
            identifier: <p>The unique identifier of the relationship to delete.</p>
            program_management_account_identifier: <p>The identifier of the program management account associated with the relationship.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for DeleteRelationship

            >>> client.delete(catalog='AWS', program_management_account_identifier='pma-u8ic702rtzng8', identifier='rs-l9o4fj3b5zb91', client_token='clientToken')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.delete_relationship_request.DeleteRelationshipRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.delete_relationship_response.DeleteRelationshipResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.delete_relationship

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.delete_relationship.delete_relationship(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRelationship")
        )
        input_: capo_partnercentral_channel.types.delete_relationship_request.DeleteRelationshipRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "program_management_account_identifier": program_management_account_identifier,
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

    def list(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        max_results: Optional[int] = None,
        associated_account_ids: Optional[
            "capo_partnercentral_channel.types.account_id_list.AccountIdList"
        ] = None,
        association_types: Optional[
            "capo_partnercentral_channel.types.association_type_list.AssociationTypeList"
        ] = None,
        display_names: Optional[
            "capo_partnercentral_channel.types.relationship_display_name_list.RelationshipDisplayNameList"
        ] = None,
        program_management_account_identifiers: Optional[
            "capo_partnercentral_channel.types.program_management_account_identifier_list.ProgramManagementAccountIdentifierList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_channel.types.list_relationships_sort_base.ListRelationshipsSortBase"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_channel.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_channel.types.list_relationships_response.ListRelationshipsResponse":
        """<p>Lists partner relationships based on specified criteria.</p>

        Args:
            catalog: <p>The catalog identifier to filter relationships.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            associated_account_ids: <p>Filter by associated AWS account IDs.</p>
            association_types: <p>Filter by association types.</p>
            display_names: <p>Filter by display names.</p>
            program_management_account_identifiers: <p>Filter by program management account identifiers.</p>
            sort: <p>Sorting options for the results.</p>
            next_token: <p>Token for retrieving the next page of results.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for ListRelationships

            >>> client.list(catalog='AWS', max_results=100, associated_account_ids=['123456789012'], association_types=['DOWNSTREAM_SELLER'], display_names=['TestDisplayName'], program_management_account_identifiers=['pma-u8ic702rtzng8'], sort={'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'}, next_token='nextToken')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.list_relationships_request.ListRelationshipsRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.list_relationships_response.ListRelationshipsResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.list_relationships

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.list_relationships.list_relationships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRelationships")
        )
        input_: capo_partnercentral_channel.types.list_relationships_request.ListRelationshipsRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if associated_account_ids is not None:
            input_["associated_account_ids"] = associated_account_ids
        if association_types is not None:
            input_["association_types"] = association_types
        if display_names is not None:
            input_["display_names"] = display_names
        if program_management_account_identifiers is not None:
            input_["program_management_account_identifiers"] = (
                program_management_account_identifiers
            )
        if sort is not None:
            input_["sort"] = sort
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRelationshipResource:
    def __init__(self, service: AsyncPartnerCentralChannelClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        association_type: "capo_partnercentral_channel.types.association_type.AssociationType",
        program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        associated_account_id: "capo_partnercentral_channel.types.account_id.AccountId",
        display_name: "capo_partnercentral_channel.types.relationship_display_name.RelationshipDisplayName",
        sector: "capo_partnercentral_channel.types.sector.Sector",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
        resale_account_model: Optional[
            "capo_partnercentral_channel.types.resale_account_model.ResaleAccountModel"
        ] = None,
        client_token: Optional[
            "capo_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_partnercentral_channel.types.tag_list.TagList"] = None,
        requested_support_plan: Optional[
            "capo_partnercentral_channel.types.support_plan.SupportPlan"
        ] = None,
    ) -> "capo_partnercentral_channel.types.create_relationship_response.CreateRelationshipResponse":
        """<p>Creates a new partner relationship between accounts.</p>

        Args:
            catalog: <p>The catalog identifier for the relationship.</p>
            association_type: <p>The type of association for the relationship (e.g., reseller, distributor).</p>
            program_management_account_identifier: <p>The identifier of the program management account for this relationship.</p>
            associated_account_id: <p>The AWS account ID to associate in this relationship.</p>
            display_name: <p>A human-readable name for the relationship.</p>
            resale_account_model: <p>The resale account model for the relationship.</p>
            sector: <p>The business sector for the relationship.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>Key-value pairs to associate with the relationship.</p>
            requested_support_plan: <p>The support plan requested for this relationship.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for CreateRelationship

            >>> await client.create(catalog='AWS', association_type='DOWNSTREAM_SELLER', program_management_account_identifier='pma-u8ic702rtzng8', associated_account_id='987654321012', display_name='TestDisplayName', resale_account_model='END_CUSTOMER', sector='COMMERCIAL', client_token='clientToken')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_channel.types.create_relationship_request.CreateRelationshipRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_channel.types.create_relationship_response.CreateRelationshipResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.create_relationship

            (
                output,
                http_response,
            ) = await capo_partnercentral_channel._operations.partner_central_channel.create_relationship.async_create_relationship(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateRelationship")
        )
        input_: capo_partnercentral_channel.types.create_relationship_request.CreateRelationshipRequest = {
            "catalog": catalog,
            "association_type": association_type,
            "program_management_account_identifier": program_management_account_identifier,
            "associated_account_id": associated_account_id,
            "display_name": display_name,
            "sector": sector,
        }
        if resale_account_model is not None:
            input_["resale_account_model"] = resale_account_model
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if requested_support_plan is not None:
            input_["requested_support_plan"] = requested_support_plan

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        identifier: "capo_partnercentral_channel.types.relationship_identifier.RelationshipIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
    ) -> "capo_partnercentral_channel.types.get_relationship_response.GetRelationshipResponse":
        """<p>Retrieves details of a specific partner relationship.</p>

        Args:
            catalog: <p>The catalog identifier for the relationship.</p>
            program_management_account_identifier: <p>The identifier of the program management account associated with the relationship.</p>
            identifier: <p>The unique identifier of the relationship to retrieve.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for GetRelationship

            >>> await client.read(catalog='AWS', program_management_account_identifier='pma-u8ic702rtzng8', identifier='rs-l9o4fj3b5zb91')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_channel.types.get_relationship_request.GetRelationshipRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_channel.types.get_relationship_response.GetRelationshipResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.get_relationship

            (
                output,
                http_response,
            ) = await capo_partnercentral_channel._operations.partner_central_channel.get_relationship.async_get_relationship(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRelationship")
        )
        input_: capo_partnercentral_channel.types.get_relationship_request.GetRelationshipRequest = {
            "catalog": catalog,
            "program_management_account_identifier": program_management_account_identifier,
            "identifier": identifier,
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
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.relationship_identifier.RelationshipIdentifier",
        program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
        revision: Optional[
            "capo_partnercentral_channel.types.revision.Revision"
        ] = None,
        display_name: Optional[
            "capo_partnercentral_channel.types.relationship_display_name.RelationshipDisplayName"
        ] = None,
        requested_support_plan: Optional[
            "capo_partnercentral_channel.types.support_plan.SupportPlan"
        ] = None,
    ) -> "capo_partnercentral_channel.types.update_relationship_response.UpdateRelationshipResponse":
        """<p>Updates the properties of a partner relationship.</p>

        Args:
            catalog: <p>The catalog identifier for the relationship.</p>
            identifier: <p>The unique identifier of the relationship to update.</p>
            program_management_account_identifier: <p>The identifier of the program management account associated with the relationship.</p>
            revision: <p>The current revision number of the relationship.</p>
            display_name: <p>The new display name for the relationship.</p>
            requested_support_plan: <p>The updated support plan for the relationship.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for UpdateRelationship

            >>> await client.update(catalog='AWS', program_management_account_identifier='pma-u8ic702rtzng8', identifier='rs-l9o4fj3b5zb91', revision='3', display_name='TestDisplayName')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_channel.types.update_relationship_request.UpdateRelationshipRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_channel.types.update_relationship_response.UpdateRelationshipResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.update_relationship

            (
                output,
                http_response,
            ) = await capo_partnercentral_channel._operations.partner_central_channel.update_relationship.async_update_relationship(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateRelationship")
        )
        input_: capo_partnercentral_channel.types.update_relationship_request.UpdateRelationshipRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "program_management_account_identifier": program_management_account_identifier,
        }
        if revision is not None:
            input_["revision"] = revision
        if display_name is not None:
            input_["display_name"] = display_name
        if requested_support_plan is not None:
            input_["requested_support_plan"] = requested_support_plan

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.relationship_identifier.RelationshipIdentifier",
        program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_channel.types.delete_relationship_response.DeleteRelationshipResponse":
        """<p>Deletes a partner relationship.</p>

        Args:
            catalog: <p>The catalog identifier for the relationship.</p>
            identifier: <p>The unique identifier of the relationship to delete.</p>
            program_management_account_identifier: <p>The identifier of the program management account associated with the relationship.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for DeleteRelationship

            >>> await client.delete(catalog='AWS', program_management_account_identifier='pma-u8ic702rtzng8', identifier='rs-l9o4fj3b5zb91', client_token='clientToken')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_channel.types.delete_relationship_request.DeleteRelationshipRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_channel.types.delete_relationship_response.DeleteRelationshipResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.delete_relationship

            (
                output,
                http_response,
            ) = await capo_partnercentral_channel._operations.partner_central_channel.delete_relationship.async_delete_relationship(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRelationship")
        )
        input_: capo_partnercentral_channel.types.delete_relationship_request.DeleteRelationshipRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "program_management_account_identifier": program_management_account_identifier,
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

    async def list(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
        max_results: Optional[int] = None,
        associated_account_ids: Optional[
            "capo_partnercentral_channel.types.account_id_list.AccountIdList"
        ] = None,
        association_types: Optional[
            "capo_partnercentral_channel.types.association_type_list.AssociationTypeList"
        ] = None,
        display_names: Optional[
            "capo_partnercentral_channel.types.relationship_display_name_list.RelationshipDisplayNameList"
        ] = None,
        program_management_account_identifiers: Optional[
            "capo_partnercentral_channel.types.program_management_account_identifier_list.ProgramManagementAccountIdentifierList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_channel.types.list_relationships_sort_base.ListRelationshipsSortBase"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_channel.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_channel.types.list_relationships_response.ListRelationshipsResponse":
        """<p>Lists partner relationships based on specified criteria.</p>

        Args:
            catalog: <p>The catalog identifier to filter relationships.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            associated_account_ids: <p>Filter by associated AWS account IDs.</p>
            association_types: <p>Filter by association types.</p>
            display_names: <p>Filter by display names.</p>
            program_management_account_identifiers: <p>Filter by program management account identifiers.</p>
            sort: <p>Sorting options for the results.</p>
            next_token: <p>Token for retrieving the next page of results.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for ListRelationships

            >>> await client.list(catalog='AWS', max_results=100, associated_account_ids=['123456789012'], association_types=['DOWNSTREAM_SELLER'], display_names=['TestDisplayName'], program_management_account_identifiers=['pma-u8ic702rtzng8'], sort={'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'}, next_token='nextToken')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_channel.types.list_relationships_request.ListRelationshipsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_channel.types.list_relationships_response.ListRelationshipsResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.list_relationships

            (
                output,
                http_response,
            ) = await capo_partnercentral_channel._operations.partner_central_channel.list_relationships.async_list_relationships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRelationships")
        )
        input_: capo_partnercentral_channel.types.list_relationships_request.ListRelationshipsRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if associated_account_ids is not None:
            input_["associated_account_ids"] = associated_account_ids
        if association_types is not None:
            input_["association_types"] = association_types
        if display_names is not None:
            input_["display_names"] = display_names
        if program_management_account_identifiers is not None:
            input_["program_management_account_identifiers"] = (
                program_management_account_identifiers
            )
        if sort is not None:
            input_["sort"] = sort
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
