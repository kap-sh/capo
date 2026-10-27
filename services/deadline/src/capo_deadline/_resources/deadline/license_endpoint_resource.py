from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_deadline._auth._signers
import capo_deadline._auth._sigv4
from capo_deadline._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.create_license_endpoint_request
    import capo_deadline.types.create_license_endpoint_response
    import capo_deadline.types.delete_license_endpoint_request
    import capo_deadline.types.delete_license_endpoint_response
    import capo_deadline.types.delete_metered_product_request
    import capo_deadline.types.delete_metered_product_response
    import capo_deadline.types.get_license_endpoint_request
    import capo_deadline.types.get_license_endpoint_response
    import capo_deadline.types.license_endpoint_id
    import capo_deadline.types.license_endpoint_summary
    import capo_deadline.types.list_license_endpoints_request
    import capo_deadline.types.list_license_endpoints_response
    import capo_deadline.types.list_metered_products_request
    import capo_deadline.types.list_metered_products_response
    import capo_deadline.types.max_results
    import capo_deadline.types.metered_product_id
    import capo_deadline.types.metered_product_summary
    import capo_deadline.types.next_token
    import capo_deadline.types.put_metered_product_request
    import capo_deadline.types.put_metered_product_response
    import capo_deadline.types.security_group_id_list
    import capo_deadline.types.subnet_id_list
    import capo_deadline.types.tags
    import capo_deadline.types.vpc_id
    from capo_deadline._services.async_deadline import (
        AsyncdeadlineClient,
        AsyncdeadlineClientConfig,
    )
    from capo_deadline._services.deadline import deadlineClient, deadlineClientConfig


class LicenseEndpointResource:
    def __init__(self, service: deadlineClient) -> None:
        self._service = service

    def create(
        self,
        vpc_id: "capo_deadline.types.vpc_id.VpcId",
        subnet_ids: "capo_deadline.types.subnet_id_list.SubnetIdList",
        security_group_ids: "capo_deadline.types.security_group_id_list.SecurityGroupIdList",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
    ) -> "capo_deadline.types.create_license_endpoint_response.CreateLicenseEndpointResponse":
        """Creates a license endpoint to integrate your various licensed software used for rendering on Deadline Cloud.

        Args:
            client_token: The unique token which the server uses to recognize retries of the same request.
            vpc_id: The VPC (virtual private cloud) ID to use with the license endpoint.
            subnet_ids: The subnet IDs.
            security_group_ids: The security group IDs.
            tags: Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.conflict_exception.ConflictException: Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_license_endpoint_request.CreateLicenseEndpointRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_license_endpoint_response.CreateLicenseEndpointResponse"
        ]:
            import capo_deadline._operations.deadline.create_license_endpoint

            output, http_response = (
                capo_deadline._operations.deadline.create_license_endpoint.create_license_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateLicenseEndpoint")
        )
        input_: capo_deadline.types.create_license_endpoint_request.CreateLicenseEndpointRequest = {
            "vpc_id": vpc_id,
            "subnet_ids": subnet_ids,
            "security_group_ids": security_group_ids,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_license_endpoint_response.GetLicenseEndpointResponse":
        """Gets a licence endpoint.

        Args:
            license_endpoint_id: The license endpoint ID.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_license_endpoint_request.GetLicenseEndpointRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_license_endpoint_response.GetLicenseEndpointResponse"
        ]:
            import capo_deadline._operations.deadline.get_license_endpoint

            output, http_response = (
                capo_deadline._operations.deadline.get_license_endpoint.get_license_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetLicenseEndpoint")
        )
        input_: capo_deadline.types.get_license_endpoint_request.GetLicenseEndpointRequest = {
            "license_endpoint_id": license_endpoint_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_license_endpoint_response.DeleteLicenseEndpointResponse":
        """Deletes a license endpoint.

        Args:
            license_endpoint_id: The license endpoint ID of the license endpoint to delete.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.conflict_exception.ConflictException: Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_license_endpoint_request.DeleteLicenseEndpointRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_license_endpoint_response.DeleteLicenseEndpointResponse"
        ]:
            import capo_deadline._operations.deadline.delete_license_endpoint

            output, http_response = (
                capo_deadline._operations.deadline.delete_license_endpoint.delete_license_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteLicenseEndpoint")
        )
        input_: capo_deadline.types.delete_license_endpoint_request.DeleteLicenseEndpointRequest = {
            "license_endpoint_id": license_endpoint_id
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
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_license_endpoints_response.ListLicenseEndpointsResponse":
        """Lists license endpoints.

        Args:
            next_token: The token for the next set of results, or <code>null</code> to start from the beginning.
            max_results: The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_license_endpoints_request.ListLicenseEndpointsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_license_endpoints_response.ListLicenseEndpointsResponse"
        ]:
            import capo_deadline._operations.deadline.list_license_endpoints

            output, http_response = (
                capo_deadline._operations.deadline.list_license_endpoints.list_license_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListLicenseEndpoints")
        )
        input_: capo_deadline.types.list_license_endpoints_request.ListLicenseEndpointsRequest = {}
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

    def delete_metered_product(
        self,
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        product_id: "capo_deadline.types.metered_product_id.MeteredProductId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_metered_product_response.DeleteMeteredProductResponse":
        """Deletes a metered product.

        Args:
            license_endpoint_id: The ID of the license endpoint from which to remove the metered product.
            product_id: The product ID to remove from the license endpoint.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_metered_product_request.DeleteMeteredProductRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_metered_product_response.DeleteMeteredProductResponse"
        ]:
            import capo_deadline._operations.deadline.delete_metered_product

            output, http_response = (
                capo_deadline._operations.deadline.delete_metered_product.delete_metered_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMeteredProduct")
        )
        input_: capo_deadline.types.delete_metered_product_request.DeleteMeteredProductRequest = {
            "license_endpoint_id": license_endpoint_id,
            "product_id": product_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_metered_products(
        self,
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_deadline.types.list_metered_products_response.ListMeteredProductsResponse"
    ):
        """Lists metered products.

        Args:
            license_endpoint_id: The license endpoint ID to include on the list of metered products.
            next_token: The token for the next set of results, or <code>null</code> to start from the beginning.
            max_results: The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_metered_products_request.ListMeteredProductsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_metered_products_response.ListMeteredProductsResponse"
        ]:
            import capo_deadline._operations.deadline.list_metered_products

            output, http_response = (
                capo_deadline._operations.deadline.list_metered_products.list_metered_products(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMeteredProducts")
        )
        input_: capo_deadline.types.list_metered_products_request.ListMeteredProductsRequest = {
            "license_endpoint_id": license_endpoint_id
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

    def put_metered_product(
        self,
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        product_id: "capo_deadline.types.metered_product_id.MeteredProductId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.put_metered_product_response.PutMeteredProductResponse":
        """Adds a metered product.

        Args:
            license_endpoint_id: The license endpoint ID to add to the metered product.
            product_id: The product ID to add to the metered product.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.put_metered_product_request.PutMeteredProductRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.put_metered_product_response.PutMeteredProductResponse"
        ]:
            import capo_deadline._operations.deadline.put_metered_product

            output, http_response = (
                capo_deadline._operations.deadline.put_metered_product.put_metered_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutMeteredProduct")
        )
        input_: capo_deadline.types.put_metered_product_request.PutMeteredProductRequest = {
            "license_endpoint_id": license_endpoint_id,
            "product_id": product_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncLicenseEndpointResource:
    def __init__(self, service: AsyncdeadlineClient) -> None:
        self._service = service

    async def create(
        self,
        vpc_id: "capo_deadline.types.vpc_id.VpcId",
        subnet_ids: "capo_deadline.types.subnet_id_list.SubnetIdList",
        security_group_ids: "capo_deadline.types.security_group_id_list.SecurityGroupIdList",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
    ) -> "capo_deadline.types.create_license_endpoint_response.CreateLicenseEndpointResponse":
        """Creates a license endpoint to integrate your various licensed software used for rendering on Deadline Cloud.

        Args:
            client_token: The unique token which the server uses to recognize retries of the same request.
            vpc_id: The VPC (virtual private cloud) ID to use with the license endpoint.
            subnet_ids: The subnet IDs.
            security_group_ids: The security group IDs.
            tags: Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.conflict_exception.ConflictException: Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.create_license_endpoint_request.CreateLicenseEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.create_license_endpoint_response.CreateLicenseEndpointResponse"
        ]:
            import capo_deadline._operations.deadline.create_license_endpoint

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.create_license_endpoint.async_create_license_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateLicenseEndpoint")
        )
        input_: capo_deadline.types.create_license_endpoint_request.CreateLicenseEndpointRequest = {
            "vpc_id": vpc_id,
            "subnet_ids": subnet_ids,
            "security_group_ids": security_group_ids,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_license_endpoint_response.GetLicenseEndpointResponse":
        """Gets a licence endpoint.

        Args:
            license_endpoint_id: The license endpoint ID.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.get_license_endpoint_request.GetLicenseEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.get_license_endpoint_response.GetLicenseEndpointResponse"
        ]:
            import capo_deadline._operations.deadline.get_license_endpoint

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.get_license_endpoint.async_get_license_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetLicenseEndpoint")
        )
        input_: capo_deadline.types.get_license_endpoint_request.GetLicenseEndpointRequest = {
            "license_endpoint_id": license_endpoint_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_license_endpoint_response.DeleteLicenseEndpointResponse":
        """Deletes a license endpoint.

        Args:
            license_endpoint_id: The license endpoint ID of the license endpoint to delete.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.conflict_exception.ConflictException: Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.delete_license_endpoint_request.DeleteLicenseEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.delete_license_endpoint_response.DeleteLicenseEndpointResponse"
        ]:
            import capo_deadline._operations.deadline.delete_license_endpoint

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.delete_license_endpoint.async_delete_license_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteLicenseEndpoint")
        )
        input_: capo_deadline.types.delete_license_endpoint_request.DeleteLicenseEndpointRequest = {
            "license_endpoint_id": license_endpoint_id
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
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_license_endpoints_response.ListLicenseEndpointsResponse":
        """Lists license endpoints.

        Args:
            next_token: The token for the next set of results, or <code>null</code> to start from the beginning.
            max_results: The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.list_license_endpoints_request.ListLicenseEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.list_license_endpoints_response.ListLicenseEndpointsResponse"
        ]:
            import capo_deadline._operations.deadline.list_license_endpoints

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.list_license_endpoints.async_list_license_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListLicenseEndpoints")
        )
        input_: capo_deadline.types.list_license_endpoints_request.ListLicenseEndpointsRequest = {}
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

    async def delete_metered_product(
        self,
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        product_id: "capo_deadline.types.metered_product_id.MeteredProductId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_metered_product_response.DeleteMeteredProductResponse":
        """Deletes a metered product.

        Args:
            license_endpoint_id: The ID of the license endpoint from which to remove the metered product.
            product_id: The product ID to remove from the license endpoint.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.delete_metered_product_request.DeleteMeteredProductRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.delete_metered_product_response.DeleteMeteredProductResponse"
        ]:
            import capo_deadline._operations.deadline.delete_metered_product

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.delete_metered_product.async_delete_metered_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMeteredProduct")
        )
        input_: capo_deadline.types.delete_metered_product_request.DeleteMeteredProductRequest = {
            "license_endpoint_id": license_endpoint_id,
            "product_id": product_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_metered_products(
        self,
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_deadline.types.list_metered_products_response.ListMeteredProductsResponse"
    ):
        """Lists metered products.

        Args:
            license_endpoint_id: The license endpoint ID to include on the list of metered products.
            next_token: The token for the next set of results, or <code>null</code> to start from the beginning.
            max_results: The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.list_metered_products_request.ListMeteredProductsRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.list_metered_products_response.ListMeteredProductsResponse"
        ]:
            import capo_deadline._operations.deadline.list_metered_products

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.list_metered_products.async_list_metered_products(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMeteredProducts")
        )
        input_: capo_deadline.types.list_metered_products_request.ListMeteredProductsRequest = {
            "license_endpoint_id": license_endpoint_id
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

    async def put_metered_product(
        self,
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        product_id: "capo_deadline.types.metered_product_id.MeteredProductId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.put_metered_product_response.PutMeteredProductResponse":
        """Adds a metered product.

        Args:
            license_endpoint_id: The license endpoint ID to add to the metered product.
            product_id: The product ID to add to the metered product.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.put_metered_product_request.PutMeteredProductRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.put_metered_product_response.PutMeteredProductResponse"
        ]:
            import capo_deadline._operations.deadline.put_metered_product

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.put_metered_product.async_put_metered_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutMeteredProduct")
        )
        input_: capo_deadline.types.put_metered_product_request.PutMeteredProductRequest = {
            "license_endpoint_id": license_endpoint_id,
            "product_id": product_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
