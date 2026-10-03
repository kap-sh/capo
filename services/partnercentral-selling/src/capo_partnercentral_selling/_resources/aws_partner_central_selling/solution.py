from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_partnercentral_selling._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_marketplace_solution_arn_list
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.filter_status
    import capo_partnercentral_selling.types.list_solutions_request
    import capo_partnercentral_selling.types.list_solutions_response
    import capo_partnercentral_selling.types.page_size
    import capo_partnercentral_selling.types.solution_base
    import capo_partnercentral_selling.types.solution_identifiers
    import capo_partnercentral_selling.types.solution_sort
    import capo_partnercentral_selling.types.string_list
    from capo_partnercentral_selling._services.async_partner_central_selling import (
        AsyncPartnerCentralSellingClient,
        AsyncPartnerCentralSellingClientConfig,
    )
    from capo_partnercentral_selling._services.partner_central_selling import (
        PartnerCentralSellingClient,
        PartnerCentralSellingClientConfig,
    )


class Solution:
    def __init__(self, service: PartnerCentralSellingClient) -> None:
        self._service = service

    def list(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.solution_sort.SolutionSort"
        ] = None,
        status: Optional[
            "capo_partnercentral_selling.types.filter_status.FilterStatus"
        ] = None,
        identifier: Optional[
            "capo_partnercentral_selling.types.solution_identifiers.SolutionIdentifiers"
        ] = None,
        category: Optional[
            "capo_partnercentral_selling.types.string_list.StringList"
        ] = None,
        aws_marketplace_solution_arn: Optional[
            "capo_partnercentral_selling.types.aws_marketplace_solution_arn_list.AwsMarketplaceSolutionArnList"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_solutions_response.ListSolutionsResponse":
        """<p>Retrieves a list of Partner Solutions that the partner registered on Partner Central. This API is used to generate a list of solutions that an end user selects from for association with an opportunity.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the solutions are listed in. Use <code>AWS</code> to list solutions in the Amazon Web Services catalog, and <code>Sandbox</code> to list solutions in a secure and isolated testing environment.</p>
            max_results: <p>The maximum number of results returned by a single call. This value must be provided in the next call to retrieve the next set of results.</p> <p>Default: 20</p>
            next_token: <p>A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.</p>
            sort: <p>Object that configures sorting done on the response. Default <code>Sort.SortBy</code> is <code>Identifier</code>.</p>
            status: <p>Filters solutions based on their status. This filter helps partners manage their solution portfolios effectively.</p>
            identifier: <p>Filters the solutions based on their unique identifier. Use this filter to retrieve specific solutions by providing the solution's identifier for accurate results.</p>
            category: <p>Filters the solutions based on the category to which they belong. This allows partners to search for solutions within specific categories, such as <code>Software</code>, <code>Consulting</code>, or <code>Managed Services</code>.</p>
            aws_marketplace_solution_arn: <p>Filters results by AWS Marketplace solution ARN. You can provide up to 10 ARNs.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.list_solutions_request.ListSolutionsRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.list_solutions_response.ListSolutionsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_solutions

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.list_solutions.list_solutions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_solutions_request.ListSolutionsRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        if status is not None:
            input_["status"] = status
        if identifier is not None:
            input_["identifier"] = identifier
        if category is not None:
            input_["category"] = category
        if aws_marketplace_solution_arn is not None:
            input_["aws_marketplace_solution_arn"] = aws_marketplace_solution_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncSolution:
    def __init__(self, service: AsyncPartnerCentralSellingClient) -> None:
        self._service = service

    async def list(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.solution_sort.SolutionSort"
        ] = None,
        status: Optional[
            "capo_partnercentral_selling.types.filter_status.FilterStatus"
        ] = None,
        identifier: Optional[
            "capo_partnercentral_selling.types.solution_identifiers.SolutionIdentifiers"
        ] = None,
        category: Optional[
            "capo_partnercentral_selling.types.string_list.StringList"
        ] = None,
        aws_marketplace_solution_arn: Optional[
            "capo_partnercentral_selling.types.aws_marketplace_solution_arn_list.AwsMarketplaceSolutionArnList"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_solutions_response.ListSolutionsResponse":
        """<p>Retrieves a list of Partner Solutions that the partner registered on Partner Central. This API is used to generate a list of solutions that an end user selects from for association with an opportunity.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the solutions are listed in. Use <code>AWS</code> to list solutions in the Amazon Web Services catalog, and <code>Sandbox</code> to list solutions in a secure and isolated testing environment.</p>
            max_results: <p>The maximum number of results returned by a single call. This value must be provided in the next call to retrieve the next set of results.</p> <p>Default: 20</p>
            next_token: <p>A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.</p>
            sort: <p>Object that configures sorting done on the response. Default <code>Sort.SortBy</code> is <code>Identifier</code>.</p>
            status: <p>Filters solutions based on their status. This filter helps partners manage their solution portfolios effectively.</p>
            identifier: <p>Filters the solutions based on their unique identifier. Use this filter to retrieve specific solutions by providing the solution's identifier for accurate results.</p>
            category: <p>Filters the solutions based on the category to which they belong. This allows partners to search for solutions within specific categories, such as <code>Software</code>, <code>Consulting</code>, or <code>Managed Services</code>.</p>
            aws_marketplace_solution_arn: <p>Filters results by AWS Marketplace solution ARN. You can provide up to 10 ARNs.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_solutions_request.ListSolutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_solutions_response.ListSolutionsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_solutions

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_solutions.async_list_solutions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_solutions_request.ListSolutionsRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        if status is not None:
            input_["status"] = status
        if identifier is not None:
            input_["identifier"] = identifier
        if category is not None:
            input_["category"] = category
        if aws_marketplace_solution_arn is not None:
            input_["aws_marketplace_solution_arn"] = aws_marketplace_solution_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
