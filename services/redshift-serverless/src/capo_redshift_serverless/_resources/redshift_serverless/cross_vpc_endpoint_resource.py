from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_redshift_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_redshift_serverless.types.create_endpoint_access_request
    import capo_redshift_serverless.types.create_endpoint_access_response
    import capo_redshift_serverless.types.delete_endpoint_access_request
    import capo_redshift_serverless.types.delete_endpoint_access_response
    import capo_redshift_serverless.types.endpoint_access
    import capo_redshift_serverless.types.get_endpoint_access_request
    import capo_redshift_serverless.types.get_endpoint_access_response
    import capo_redshift_serverless.types.list_endpoint_access_request
    import capo_redshift_serverless.types.list_endpoint_access_response
    import capo_redshift_serverless.types.owner_account
    import capo_redshift_serverless.types.subnet_id_list
    import capo_redshift_serverless.types.update_endpoint_access_request
    import capo_redshift_serverless.types.update_endpoint_access_response
    import capo_redshift_serverless.types.vpc_security_group_id_list
    from capo_redshift_serverless._services.async_redshift_serverless import (
        AsyncRedshiftServerlessClient,
        AsyncRedshiftServerlessClientConfig,
    )
    from capo_redshift_serverless._services.redshift_serverless import (
        RedshiftServerlessClient,
        RedshiftServerlessClientConfig,
    )


class CrossVpcEndpointResource:
    def __init__(self, service: RedshiftServerlessClient) -> None:
        self._service = service

    def create_endpoint_access(
        self,
        endpoint_name: str,
        subnet_ids: "capo_redshift_serverless.types.subnet_id_list.SubnetIdList",
        workgroup_name: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        vpc_security_group_ids: Optional[
            "capo_redshift_serverless.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        owner_account: Optional[
            "capo_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> "capo_redshift_serverless.types.create_endpoint_access_response.CreateEndpointAccessResponse":
        """<p>Creates an Amazon Redshift Serverless managed VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint. An endpoint name must contain 1-30 characters. Valid characters are A-Z, a-z, 0-9, and hyphen(-). The first character must be a letter. The name can't contain two consecutive hyphens or end with a hyphen.</p>
            subnet_ids: <p>The unique identifers of subnets from which Amazon Redshift Serverless chooses one to deploy a VPC endpoint.</p>
            workgroup_name: <p>The name of the workgroup to associate with the VPC endpoint.</p>
            vpc_security_group_ids: <p>The unique identifiers of the security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>
            owner_account: <p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.create_endpoint_access_request.CreateEndpointAccessRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.create_endpoint_access_response.CreateEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_endpoint_access

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.create_endpoint_access.create_endpoint_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateEndpointAccess")
        )
        input_: capo_redshift_serverless.types.create_endpoint_access_request.CreateEndpointAccessRequest = {
            "endpoint_name": endpoint_name,
            "subnet_ids": subnet_ids,
            "workgroup_name": workgroup_name,
        }
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.delete_endpoint_access_response.DeleteEndpointAccessResponse":
        """<p>Deletes an Amazon Redshift Serverless managed VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to delete.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.delete_endpoint_access_request.DeleteEndpointAccessRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.delete_endpoint_access_response.DeleteEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_endpoint_access

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.delete_endpoint_access.delete_endpoint_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteEndpointAccess")
        )
        input_: capo_redshift_serverless.types.delete_endpoint_access_request.DeleteEndpointAccessRequest = {
            "endpoint_name": endpoint_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_endpoint_access_response.GetEndpointAccessResponse":
        """<p>Returns information, such as the name, about a VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to return information for.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.get_endpoint_access_request.GetEndpointAccessRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.get_endpoint_access_response.GetEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_endpoint_access

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.get_endpoint_access.get_endpoint_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetEndpointAccess")
        )
        input_: capo_redshift_serverless.types.get_endpoint_access_request.GetEndpointAccessRequest = {
            "endpoint_name": endpoint_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_endpoint_access(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        workgroup_name: Optional[str] = None,
        vpc_id: Optional[str] = None,
        owner_account: Optional[
            "capo_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> "capo_redshift_serverless.types.list_endpoint_access_response.ListEndpointAccessResponse":
        """<p>Returns an array of <code>EndpointAccess</code> objects and relevant information.</p>

        Args:
            next_token: <p>If your initial <code>ListEndpointAccess</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListEndpointAccess</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            workgroup_name: <p>The name of the workgroup associated with the VPC endpoint to return.</p>
            vpc_id: <p>The unique identifier of the virtual private cloud with access to Amazon Redshift Serverless.</p>
            owner_account: <p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.list_endpoint_access_request.ListEndpointAccessRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.list_endpoint_access_response.ListEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_endpoint_access

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.list_endpoint_access.list_endpoint_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListEndpointAccess")
        )
        input_: capo_redshift_serverless.types.list_endpoint_access_request.ListEndpointAccessRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        vpc_security_group_ids: Optional[
            "capo_redshift_serverless.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
    ) -> "capo_redshift_serverless.types.update_endpoint_access_response.UpdateEndpointAccessResponse":
        """<p>Updates an Amazon Redshift Serverless managed endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to update.</p>
            vpc_security_group_ids: <p>The list of VPC security groups associated with the endpoint after the endpoint is modified.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.update_endpoint_access_request.UpdateEndpointAccessRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.update_endpoint_access_response.UpdateEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_endpoint_access

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.update_endpoint_access.update_endpoint_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateEndpointAccess")
        )
        input_: capo_redshift_serverless.types.update_endpoint_access_request.UpdateEndpointAccessRequest = {
            "endpoint_name": endpoint_name
        }
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCrossVpcEndpointResource:
    def __init__(self, service: AsyncRedshiftServerlessClient) -> None:
        self._service = service

    async def create_endpoint_access(
        self,
        endpoint_name: str,
        subnet_ids: "capo_redshift_serverless.types.subnet_id_list.SubnetIdList",
        workgroup_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        vpc_security_group_ids: Optional[
            "capo_redshift_serverless.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        owner_account: Optional[
            "capo_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> "capo_redshift_serverless.types.create_endpoint_access_response.CreateEndpointAccessResponse":
        """<p>Creates an Amazon Redshift Serverless managed VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint. An endpoint name must contain 1-30 characters. Valid characters are A-Z, a-z, 0-9, and hyphen(-). The first character must be a letter. The name can't contain two consecutive hyphens or end with a hyphen.</p>
            subnet_ids: <p>The unique identifers of subnets from which Amazon Redshift Serverless chooses one to deploy a VPC endpoint.</p>
            workgroup_name: <p>The name of the workgroup to associate with the VPC endpoint.</p>
            vpc_security_group_ids: <p>The unique identifiers of the security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>
            owner_account: <p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.create_endpoint_access_request.CreateEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.create_endpoint_access_response.CreateEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.create_endpoint_access.async_create_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateEndpointAccess")
        )
        input_: capo_redshift_serverless.types.create_endpoint_access_request.CreateEndpointAccessRequest = {
            "endpoint_name": endpoint_name,
            "subnet_ids": subnet_ids,
            "workgroup_name": workgroup_name,
        }
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.delete_endpoint_access_response.DeleteEndpointAccessResponse":
        """<p>Deletes an Amazon Redshift Serverless managed VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to delete.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.delete_endpoint_access_request.DeleteEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.delete_endpoint_access_response.DeleteEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.delete_endpoint_access.async_delete_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteEndpointAccess")
        )
        input_: capo_redshift_serverless.types.delete_endpoint_access_request.DeleteEndpointAccessRequest = {
            "endpoint_name": endpoint_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_endpoint_access_response.GetEndpointAccessResponse":
        """<p>Returns information, such as the name, about a VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to return information for.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_endpoint_access_request.GetEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_endpoint_access_response.GetEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_endpoint_access.async_get_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetEndpointAccess")
        )
        input_: capo_redshift_serverless.types.get_endpoint_access_request.GetEndpointAccessRequest = {
            "endpoint_name": endpoint_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_endpoint_access(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        workgroup_name: Optional[str] = None,
        vpc_id: Optional[str] = None,
        owner_account: Optional[
            "capo_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> "capo_redshift_serverless.types.list_endpoint_access_response.ListEndpointAccessResponse":
        """<p>Returns an array of <code>EndpointAccess</code> objects and relevant information.</p>

        Args:
            next_token: <p>If your initial <code>ListEndpointAccess</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListEndpointAccess</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            workgroup_name: <p>The name of the workgroup associated with the VPC endpoint to return.</p>
            vpc_id: <p>The unique identifier of the virtual private cloud with access to Amazon Redshift Serverless.</p>
            owner_account: <p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_endpoint_access_request.ListEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_endpoint_access_response.ListEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_endpoint_access.async_list_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListEndpointAccess")
        )
        input_: capo_redshift_serverless.types.list_endpoint_access_request.ListEndpointAccessRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        vpc_security_group_ids: Optional[
            "capo_redshift_serverless.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
    ) -> "capo_redshift_serverless.types.update_endpoint_access_response.UpdateEndpointAccessResponse":
        """<p>Updates an Amazon Redshift Serverless managed endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to update.</p>
            vpc_security_group_ids: <p>The list of VPC security groups associated with the endpoint after the endpoint is modified.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.update_endpoint_access_request.UpdateEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.update_endpoint_access_response.UpdateEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.update_endpoint_access.async_update_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateEndpointAccess")
        )
        input_: capo_redshift_serverless.types.update_endpoint_access_request.UpdateEndpointAccessRequest = {
            "endpoint_name": endpoint_name
        }
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
