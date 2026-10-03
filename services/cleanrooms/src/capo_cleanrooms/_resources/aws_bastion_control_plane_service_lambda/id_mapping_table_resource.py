from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_cleanrooms._auth._signers
import capo_cleanrooms._auth._sigv4
from capo_cleanrooms._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_cleanrooms.types.create_id_mapping_table_input
    import capo_cleanrooms.types.create_id_mapping_table_output
    import capo_cleanrooms.types.delete_id_mapping_table_input
    import capo_cleanrooms.types.delete_id_mapping_table_output
    import capo_cleanrooms.types.get_id_mapping_table_input
    import capo_cleanrooms.types.get_id_mapping_table_output
    import capo_cleanrooms.types.id_mapping_table_input_reference_config
    import capo_cleanrooms.types.id_mapping_table_summary
    import capo_cleanrooms.types.job_type
    import capo_cleanrooms.types.kms_key_arn
    import capo_cleanrooms.types.list_id_mapping_tables_input
    import capo_cleanrooms.types.list_id_mapping_tables_output
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.populate_id_mapping_table_input
    import capo_cleanrooms.types.populate_id_mapping_table_output
    import capo_cleanrooms.types.resource_alias
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.tag_map
    import capo_cleanrooms.types.update_id_mapping_table_input
    import capo_cleanrooms.types.update_id_mapping_table_output
    import capo_cleanrooms.types.uuid
    from capo_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from capo_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class IdMappingTableResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        name: "capo_cleanrooms.types.resource_alias.ResourceAlias",
        input_reference_config: "capo_cleanrooms.types.id_mapping_table_input_reference_config.IdMappingTableInputReferenceConfig",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None,
    ) -> "capo_cleanrooms.types.create_id_mapping_table_output.CreateIdMappingTableOutput":
        """<p>Creates an ID mapping table.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table.</p>
            name: <p>A name for the ID mapping table.</p>
            description: <p>A description of the ID mapping table.</p>
            input_reference_config: <p>The input reference configuration needed to create the ID mapping table.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key. This value is used to encrypt the mapping table data that is stored by Clean Rooms.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.create_id_mapping_table_input.CreateIdMappingTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.create_id_mapping_table_output.CreateIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_mapping_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_mapping_table.create_id_mapping_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_id_mapping_table_input.CreateIdMappingTableInput = {
            "membership_identifier": membership_identifier,
            "name": name,
            "input_reference_config": input_reference_config,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_id_mapping_table_output.GetIdMappingTableOutput":
        """<p>Retrieves an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table identifier that you want to retrieve.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_id_mapping_table_input.GetIdMappingTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_id_mapping_table_output.GetIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_mapping_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_mapping_table.get_id_mapping_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_id_mapping_table_input.GetIdMappingTableInput = {
            "id_mapping_table_identifier": id_mapping_table_identifier,
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
        id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        kms_key_arn: Optional["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None,
    ) -> "capo_cleanrooms.types.update_id_mapping_table_output.UpdateIdMappingTableOutput":
        """<p>Provides the details that are necessary to update an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to update.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to update.</p>
            description: <p>A new description for the ID mapping table.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.update_id_mapping_table_input.UpdateIdMappingTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_id_mapping_table_output.UpdateIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_mapping_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_mapping_table.update_id_mapping_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_id_mapping_table_input.UpdateIdMappingTableInput = {
            "id_mapping_table_identifier": id_mapping_table_identifier,
            "membership_identifier": membership_identifier,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_id_mapping_table_output.DeleteIdMappingTableOutput":
        """<p>Deletes an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to delete.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to delete.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.delete_id_mapping_table_input.DeleteIdMappingTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.delete_id_mapping_table_output.DeleteIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_mapping_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_mapping_table.delete_id_mapping_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_id_mapping_table_input.DeleteIdMappingTableInput = {
            "id_mapping_table_identifier": id_mapping_table_identifier,
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
    ) -> (
        "capo_cleanrooms.types.list_id_mapping_tables_output.ListIdMappingTablesOutput"
    ):
        """<p>Returns a list of ID mapping tables.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping tables that you want to view.</p>
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
            req: "OperationRequest[capo_cleanrooms.types.list_id_mapping_tables_input.ListIdMappingTablesInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_id_mapping_tables_output.ListIdMappingTablesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_mapping_tables

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_mapping_tables.list_id_mapping_tables(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_id_mapping_tables_input.ListIdMappingTablesInput = {
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

    def populate_id_mapping_table(
        self,
        id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        job_type: Optional["capo_cleanrooms.types.job_type.JobType"] = None,
    ) -> "capo_cleanrooms.types.populate_id_mapping_table_output.PopulateIdMappingTableOutput":
        """<p>Defines the information that's necessary to populate an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to populate.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to populate.</p>
            job_type: <p>The job type of the rule-based ID mapping job. Valid values include:</p> <p> <code>INCREMENTAL</code>: Processes only new or changed data since the last job run. This is the default job type if the ID mapping workflow was created in Entity Resolution with <code>incrementalRunConfig</code> specified.</p> <p> <code>BATCH</code>: Processes all data from the input source, regardless of previous job runs. This is the default job type if the ID mapping workflow was created in Entity Resolution but <code>incrementalRunConfig</code> wasn't specified.</p> <p> <code>DELETE_ONLY</code>: Processes only deletion requests from <code>BatchDeleteUniqueId</code>, which is set in Entity Resolution.</p> <p>For more information about <code>incrementalRunConfig</code> and <code>BatchDeleteUniqueId</code>, see the <a href="https://docs.aws.amazon.com/entityresolution/latest/apireference/Welcome.html">Entity Resolution API Reference</a>.</p>

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
            req: "OperationRequest[capo_cleanrooms.types.populate_id_mapping_table_input.PopulateIdMappingTableInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.populate_id_mapping_table_output.PopulateIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_id_mapping_table

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_id_mapping_table.populate_id_mapping_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.populate_id_mapping_table_input.PopulateIdMappingTableInput = {
            "id_mapping_table_identifier": id_mapping_table_identifier,
            "membership_identifier": membership_identifier,
        }
        if job_type is not None:
            input_["job_type"] = job_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncIdMappingTableResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        name: "capo_cleanrooms.types.resource_alias.ResourceAlias",
        input_reference_config: "capo_cleanrooms.types.id_mapping_table_input_reference_config.IdMappingTableInputReferenceConfig",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None,
    ) -> "capo_cleanrooms.types.create_id_mapping_table_output.CreateIdMappingTableOutput":
        """<p>Creates an ID mapping table.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table.</p>
            name: <p>A name for the ID mapping table.</p>
            description: <p>A description of the ID mapping table.</p>
            input_reference_config: <p>The input reference configuration needed to create the ID mapping table.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key. This value is used to encrypt the mapping table data that is stored by Clean Rooms.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_id_mapping_table_input.CreateIdMappingTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_id_mapping_table_output.CreateIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_mapping_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_mapping_table.async_create_id_mapping_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_id_mapping_table_input.CreateIdMappingTableInput = {
            "membership_identifier": membership_identifier,
            "name": name,
            "input_reference_config": input_reference_config,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_id_mapping_table_output.GetIdMappingTableOutput":
        """<p>Retrieves an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table identifier that you want to retrieve.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_id_mapping_table_input.GetIdMappingTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_id_mapping_table_output.GetIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_mapping_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_mapping_table.async_get_id_mapping_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_id_mapping_table_input.GetIdMappingTableInput = {
            "id_mapping_table_identifier": id_mapping_table_identifier,
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
        id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        kms_key_arn: Optional["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None,
    ) -> "capo_cleanrooms.types.update_id_mapping_table_output.UpdateIdMappingTableOutput":
        """<p>Provides the details that are necessary to update an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to update.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to update.</p>
            description: <p>A new description for the ID mapping table.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_id_mapping_table_input.UpdateIdMappingTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_id_mapping_table_output.UpdateIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_mapping_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_mapping_table.async_update_id_mapping_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_id_mapping_table_input.UpdateIdMappingTableInput = {
            "id_mapping_table_identifier": id_mapping_table_identifier,
            "membership_identifier": membership_identifier,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_id_mapping_table_output.DeleteIdMappingTableOutput":
        """<p>Deletes an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to delete.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to delete.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_id_mapping_table_input.DeleteIdMappingTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_id_mapping_table_output.DeleteIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_mapping_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_mapping_table.async_delete_id_mapping_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_id_mapping_table_input.DeleteIdMappingTableInput = {
            "id_mapping_table_identifier": id_mapping_table_identifier,
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
    ) -> (
        "capo_cleanrooms.types.list_id_mapping_tables_output.ListIdMappingTablesOutput"
    ):
        """<p>Returns a list of ID mapping tables.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping tables that you want to view.</p>
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
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_id_mapping_tables_input.ListIdMappingTablesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_id_mapping_tables_output.ListIdMappingTablesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_mapping_tables

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_mapping_tables.async_list_id_mapping_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_id_mapping_tables_input.ListIdMappingTablesInput = {
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

    async def populate_id_mapping_table(
        self,
        id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        job_type: Optional["capo_cleanrooms.types.job_type.JobType"] = None,
    ) -> "capo_cleanrooms.types.populate_id_mapping_table_output.PopulateIdMappingTableOutput":
        """<p>Defines the information that's necessary to populate an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to populate.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to populate.</p>
            job_type: <p>The job type of the rule-based ID mapping job. Valid values include:</p> <p> <code>INCREMENTAL</code>: Processes only new or changed data since the last job run. This is the default job type if the ID mapping workflow was created in Entity Resolution with <code>incrementalRunConfig</code> specified.</p> <p> <code>BATCH</code>: Processes all data from the input source, regardless of previous job runs. This is the default job type if the ID mapping workflow was created in Entity Resolution but <code>incrementalRunConfig</code> wasn't specified.</p> <p> <code>DELETE_ONLY</code>: Processes only deletion requests from <code>BatchDeleteUniqueId</code>, which is set in Entity Resolution.</p> <p>For more information about <code>incrementalRunConfig</code> and <code>BatchDeleteUniqueId</code>, see the <a href="https://docs.aws.amazon.com/entityresolution/latest/apireference/Welcome.html">Entity Resolution API Reference</a>.</p>

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
            req: "AsyncOperationRequest[capo_cleanrooms.types.populate_id_mapping_table_input.PopulateIdMappingTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.populate_id_mapping_table_output.PopulateIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_id_mapping_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_id_mapping_table.async_populate_id_mapping_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_cleanrooms.types.populate_id_mapping_table_input.PopulateIdMappingTableInput = {
            "id_mapping_table_identifier": id_mapping_table_identifier,
            "membership_identifier": membership_identifier,
        }
        if job_type is not None:
            input_["job_type"] = job_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
