from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_datazone._auth._signers
import capo_datazone._auth._sigv4
from capo_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_datazone.types.create_domain_input
    import capo_datazone.types.create_domain_output
    import capo_datazone.types.delete_domain_input
    import capo_datazone.types.delete_domain_output
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_status
    import capo_datazone.types.domain_summary
    import capo_datazone.types.domain_version
    import capo_datazone.types.get_domain_input
    import capo_datazone.types.get_domain_output
    import capo_datazone.types.kms_key_arn
    import capo_datazone.types.list_domains_input
    import capo_datazone.types.list_domains_output
    import capo_datazone.types.max_results_for_list_domains
    import capo_datazone.types.pagination_token
    import capo_datazone.types.role_arn
    import capo_datazone.types.single_sign_on
    import capo_datazone.types.tags
    import capo_datazone.types.update_domain_input
    import capo_datazone.types.update_domain_output
    from capo_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from capo_datazone._services.data_zone import DataZoneClient, DataZoneClientConfig


class Domain:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        name: str,
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional[str] = None,
        single_sign_on: Optional[
            "capo_datazone.types.single_sign_on.SingleSignOn"
        ] = None,
        domain_execution_role: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        kms_key_identifier: Optional[
            "capo_datazone.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_datazone.types.tags.Tags"] = None,
        domain_version: Optional[
            "capo_datazone.types.domain_version.DomainVersion"
        ] = None,
        service_role: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.create_domain_output.CreateDomainOutput":
        """<p>Creates an Amazon DataZone domain.</p>

        Args:
            name: <p>The name of the Amazon DataZone domain.</p>
            description: <p>The description of the Amazon DataZone domain.</p>
            single_sign_on: <p>The single-sign on configuration of the Amazon DataZone domain.</p>
            domain_execution_role: <p>The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the Amazon Web Services account that houses the Amazon DataZone domain.</p>
            kms_key_identifier: <p>The identifier of the Amazon Web Services Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data. </p>
            tags: <p>The tags specified for the Amazon DataZone domain.</p>
            domain_version: <p>The version of the domain that is created.</p>
            service_role: <p>The service role of the domain that is created.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.create_domain_input.CreateDomainInput]",
        ) -> OperationResponse[
            "capo_datazone.types.create_domain_output.CreateDomainOutput"
        ]:
            import capo_datazone._operations.data_zone.create_domain

            output, http_response = (
                capo_datazone._operations.data_zone.create_domain.create_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateDomain")
        )
        input_: capo_datazone.types.create_domain_input.CreateDomainInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if single_sign_on is not None:
            input_["single_sign_on"] = single_sign_on
        if domain_execution_role is not None:
            input_["domain_execution_role"] = domain_execution_role
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier
        if tags is not None:
            input_["tags"] = tags
        if domain_version is not None:
            input_["domain_version"] = domain_version
        if service_role is not None:
            input_["service_role"] = service_role
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

    def read(
        self,
        identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_domain_output.GetDomainOutput":
        """<p>Gets an Amazon DataZone domain.</p>

        Args:
            identifier: <p>The identifier of the specified Amazon DataZone domain.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.get_domain_input.GetDomainInput]",
        ) -> OperationResponse["capo_datazone.types.get_domain_output.GetDomainOutput"]:
            import capo_datazone._operations.data_zone.get_domain

            output, http_response = (
                capo_datazone._operations.data_zone.get_domain.get_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDomain")
        )
        input_: capo_datazone.types.get_domain_input.GetDomainInput = {
            "identifier": identifier
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
        identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional[str] = None,
        single_sign_on: Optional[
            "capo_datazone.types.single_sign_on.SingleSignOn"
        ] = None,
        domain_execution_role: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        service_role: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        name: Optional[str] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.update_domain_output.UpdateDomainOutput":
        """<p>Updates a Amazon DataZone domain.</p>

        Args:
            identifier: <p>The ID of the Amazon Web Services domain that is to be updated.</p>
            description: <p>The description to be updated as part of the <code>UpdateDomain</code> action.</p>
            single_sign_on: <p>The single sign-on option to be updated as part of the <code>UpdateDomain</code> action.</p>
            domain_execution_role: <p>The domain execution role to be updated as part of the <code>UpdateDomain</code> action.</p>
            service_role: <p>The service role of the domain.</p>
            name: <p>The name to be updated as part of the <code>UpdateDomain</code> action.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.update_domain_input.UpdateDomainInput]",
        ) -> OperationResponse[
            "capo_datazone.types.update_domain_output.UpdateDomainOutput"
        ]:
            import capo_datazone._operations.data_zone.update_domain

            output, http_response = (
                capo_datazone._operations.data_zone.update_domain.update_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateDomain")
        )
        input_: capo_datazone.types.update_domain_input.UpdateDomainInput = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description
        if single_sign_on is not None:
            input_["single_sign_on"] = single_sign_on
        if domain_execution_role is not None:
            input_["domain_execution_role"] = domain_execution_role
        if service_role is not None:
            input_["service_role"] = service_role
        if name is not None:
            input_["name"] = name
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

    def delete(
        self,
        identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        client_token: Optional[str] = None,
        skip_deletion_check: Optional[bool] = None,
        cascade_delete: Optional[bool] = None,
    ) -> "capo_datazone.types.delete_domain_output.DeleteDomainOutput":
        """<p>Deletes a Amazon DataZone domain.</p>

        Args:
            identifier: <p>The identifier of the Amazon Web Services domain that is to be deleted.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
            skip_deletion_check: <p>Specifies whether to skip the check that prevents deletion of a domain that still contains resources. When you use this parameter, Amazon DataZone deletes the domain but might not remove its associated resources, which can leave orphaned resources behind. To delete a domain and fully clean up its associated resources, use <code>cascadeDelete</code> instead. You can't use this parameter together with <code>cascadeDelete</code>.</p>
            cascade_delete: <p>Specifies whether to delete the domain along with all of its associated resources. When you use this parameter, Amazon DataZone deletes the domain and cleanly removes its associated resources without leaving orphaned resources behind. Amazon DataZone reports deletion progress in the <code>deleteProgress</code> field. Amazon DataZone reports any resources that it can't delete in the <code>failureReasons</code> field of the <code>GetDomain</code> response. You can't use this parameter together with <code>skipDeletionCheck</code>. If you don't specify a value, the default is <code>false</code>.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.delete_domain_input.DeleteDomainInput]",
        ) -> OperationResponse[
            "capo_datazone.types.delete_domain_output.DeleteDomainOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_domain

            output, http_response = (
                capo_datazone._operations.data_zone.delete_domain.delete_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDomain")
        )
        input_: capo_datazone.types.delete_domain_input.DeleteDomainInput = {
            "identifier": identifier
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if skip_deletion_check is not None:
            input_["skip_deletion_check"] = skip_deletion_check
        if cascade_delete is not None:
            input_["cascade_delete"] = cascade_delete

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
        config_overrides: Optional[DataZoneClientConfig] = None,
        status: Optional["capo_datazone.types.domain_status.DomainStatus"] = None,
        max_results: Optional[
            "capo_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_domains_output.ListDomainsOutput":
        """<p>Lists Amazon DataZone domains.</p>

        Args:
            status: <p>The status of the data source.</p>
            max_results: <p>The maximum number of domains to return in a single call to <code>ListDomains</code>. When the number of domains to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDomains</code> to list the next set of domains.</p>
            next_token: <p>When the number of domains is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of domains, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDomains</code> to list the next set of domains.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.list_domains_input.ListDomainsInput]",
        ) -> OperationResponse[
            "capo_datazone.types.list_domains_output.ListDomainsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_domains

            output, http_response = (
                capo_datazone._operations.data_zone.list_domains.list_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.list_domains_output.ListDomainsOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.list_domains_output

            return capo_datazone.types.list_domains_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListDomains", redact_output=_redact_output),
        )
        input_: capo_datazone.types.list_domains_input.ListDomainsInput = {}
        if status is not None:
            input_["status"] = status
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


class AsyncDomain:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[str] = None,
        single_sign_on: Optional[
            "capo_datazone.types.single_sign_on.SingleSignOn"
        ] = None,
        domain_execution_role: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        kms_key_identifier: Optional[
            "capo_datazone.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_datazone.types.tags.Tags"] = None,
        domain_version: Optional[
            "capo_datazone.types.domain_version.DomainVersion"
        ] = None,
        service_role: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.create_domain_output.CreateDomainOutput":
        """<p>Creates an Amazon DataZone domain.</p>

        Args:
            name: <p>The name of the Amazon DataZone domain.</p>
            description: <p>The description of the Amazon DataZone domain.</p>
            single_sign_on: <p>The single-sign on configuration of the Amazon DataZone domain.</p>
            domain_execution_role: <p>The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the Amazon Web Services account that houses the Amazon DataZone domain.</p>
            kms_key_identifier: <p>The identifier of the Amazon Web Services Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data. </p>
            tags: <p>The tags specified for the Amazon DataZone domain.</p>
            domain_version: <p>The version of the domain that is created.</p>
            service_role: <p>The service role of the domain that is created.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_domain_input.CreateDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_domain_output.CreateDomainOutput"
        ]:
            import capo_datazone._operations.data_zone.create_domain

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateDomain")
        )
        input_: capo_datazone.types.create_domain_input.CreateDomainInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if single_sign_on is not None:
            input_["single_sign_on"] = single_sign_on
        if domain_execution_role is not None:
            input_["domain_execution_role"] = domain_execution_role
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier
        if tags is not None:
            input_["tags"] = tags
        if domain_version is not None:
            input_["domain_version"] = domain_version
        if service_role is not None:
            input_["service_role"] = service_role
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

    async def read(
        self,
        identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_domain_output.GetDomainOutput":
        """<p>Gets an Amazon DataZone domain.</p>

        Args:
            identifier: <p>The identifier of the specified Amazon DataZone domain.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_domain_input.GetDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_domain_output.GetDomainOutput"
        ]:
            import capo_datazone._operations.data_zone.get_domain

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_domain.async_get_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDomain")
        )
        input_: capo_datazone.types.get_domain_input.GetDomainInput = {
            "identifier": identifier
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
        identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[str] = None,
        single_sign_on: Optional[
            "capo_datazone.types.single_sign_on.SingleSignOn"
        ] = None,
        domain_execution_role: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        service_role: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        name: Optional[str] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.update_domain_output.UpdateDomainOutput":
        """<p>Updates a Amazon DataZone domain.</p>

        Args:
            identifier: <p>The ID of the Amazon Web Services domain that is to be updated.</p>
            description: <p>The description to be updated as part of the <code>UpdateDomain</code> action.</p>
            single_sign_on: <p>The single sign-on option to be updated as part of the <code>UpdateDomain</code> action.</p>
            domain_execution_role: <p>The domain execution role to be updated as part of the <code>UpdateDomain</code> action.</p>
            service_role: <p>The service role of the domain.</p>
            name: <p>The name to be updated as part of the <code>UpdateDomain</code> action.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_domain_input.UpdateDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_domain_output.UpdateDomainOutput"
        ]:
            import capo_datazone._operations.data_zone.update_domain

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_domain.async_update_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateDomain")
        )
        input_: capo_datazone.types.update_domain_input.UpdateDomainInput = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description
        if single_sign_on is not None:
            input_["single_sign_on"] = single_sign_on
        if domain_execution_role is not None:
            input_["domain_execution_role"] = domain_execution_role
        if service_role is not None:
            input_["service_role"] = service_role
        if name is not None:
            input_["name"] = name
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

    async def delete(
        self,
        identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[str] = None,
        skip_deletion_check: Optional[bool] = None,
        cascade_delete: Optional[bool] = None,
    ) -> "capo_datazone.types.delete_domain_output.DeleteDomainOutput":
        """<p>Deletes a Amazon DataZone domain.</p>

        Args:
            identifier: <p>The identifier of the Amazon Web Services domain that is to be deleted.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
            skip_deletion_check: <p>Specifies whether to skip the check that prevents deletion of a domain that still contains resources. When you use this parameter, Amazon DataZone deletes the domain but might not remove its associated resources, which can leave orphaned resources behind. To delete a domain and fully clean up its associated resources, use <code>cascadeDelete</code> instead. You can't use this parameter together with <code>cascadeDelete</code>.</p>
            cascade_delete: <p>Specifies whether to delete the domain along with all of its associated resources. When you use this parameter, Amazon DataZone deletes the domain and cleanly removes its associated resources without leaving orphaned resources behind. Amazon DataZone reports deletion progress in the <code>deleteProgress</code> field. Amazon DataZone reports any resources that it can't delete in the <code>failureReasons</code> field of the <code>GetDomain</code> response. You can't use this parameter together with <code>skipDeletionCheck</code>. If you don't specify a value, the default is <code>false</code>.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_domain_input.DeleteDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_domain_output.DeleteDomainOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_domain

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDomain")
        )
        input_: capo_datazone.types.delete_domain_input.DeleteDomainInput = {
            "identifier": identifier
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if skip_deletion_check is not None:
            input_["skip_deletion_check"] = skip_deletion_check
        if cascade_delete is not None:
            input_["cascade_delete"] = cascade_delete

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
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional["capo_datazone.types.domain_status.DomainStatus"] = None,
        max_results: Optional[
            "capo_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_domains_output.ListDomainsOutput":
        """<p>Lists Amazon DataZone domains.</p>

        Args:
            status: <p>The status of the data source.</p>
            max_results: <p>The maximum number of domains to return in a single call to <code>ListDomains</code>. When the number of domains to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDomains</code> to list the next set of domains.</p>
            next_token: <p>When the number of domains is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of domains, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDomains</code> to list the next set of domains.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_domains_input.ListDomainsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_domains_output.ListDomainsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_domains

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_domains.async_list_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.list_domains_output.ListDomainsOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.list_domains_output

            return capo_datazone.types.list_domains_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListDomains", redact_output=_redact_output),
        )
        input_: capo_datazone.types.list_domains_input.ListDomainsInput = {}
        if status is not None:
            input_["status"] = status
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
