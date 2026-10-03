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
    import capo_partnercentral_selling.types.aws_account_list
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.create_engagement_request
    import capo_partnercentral_selling.types.create_engagement_response
    import capo_partnercentral_selling.types.engagement_arn_or_identifier
    import capo_partnercentral_selling.types.engagement_context_type_list
    import capo_partnercentral_selling.types.engagement_contexts
    import capo_partnercentral_selling.types.engagement_description
    import capo_partnercentral_selling.types.engagement_identifiers
    import capo_partnercentral_selling.types.engagement_member
    import capo_partnercentral_selling.types.engagement_page_size
    import capo_partnercentral_selling.types.engagement_sort
    import capo_partnercentral_selling.types.engagement_summary
    import capo_partnercentral_selling.types.engagement_title
    import capo_partnercentral_selling.types.get_engagement_request
    import capo_partnercentral_selling.types.get_engagement_response
    import capo_partnercentral_selling.types.list_engagement_members_request
    import capo_partnercentral_selling.types.list_engagement_members_response
    import capo_partnercentral_selling.types.list_engagements_request
    import capo_partnercentral_selling.types.list_engagements_response
    import capo_partnercentral_selling.types.member_page_size
    from capo_partnercentral_selling._services.async_partner_central_selling import (
        AsyncPartnerCentralSellingClient,
        AsyncPartnerCentralSellingClientConfig,
    )
    from capo_partnercentral_selling._services.partner_central_selling import (
        PartnerCentralSellingClient,
        PartnerCentralSellingClientConfig,
    )


class Engagement:
    def __init__(self, service: PartnerCentralSellingClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        title: Optional[
            "capo_partnercentral_selling.types.engagement_title.EngagementTitle"
        ] = None,
        description: Optional[
            "capo_partnercentral_selling.types.engagement_description.EngagementDescription"
        ] = None,
        contexts: Optional[
            "capo_partnercentral_selling.types.engagement_contexts.EngagementContexts"
        ] = None,
    ) -> "capo_partnercentral_selling.types.create_engagement_response.CreateEngagementResponse":
        """<p>The <code>CreateEngagement</code> action allows you to create an <code>Engagement</code>, which serves as a collaborative space between different parties such as AWS Partners and AWS Sellers. This action automatically adds the caller's AWS account as an active member of the newly created <code>Engagement</code>.</p>

        Args:
            catalog: <p>The <code>CreateEngagementRequest$Catalog</code> parameter specifies the catalog related to the engagement. Accepted values are <code>AWS</code> and <code>Sandbox</code>, which determine the environment in which the engagement is managed.</p>
            client_token: <p>The <code>CreateEngagementRequest$ClientToken</code> parameter specifies a unique, case-sensitive identifier to ensure that the request is handled exactly once. The value must not exceed sixty-four alphanumeric characters.</p>
            title: <p>Specifies the title of the <code>Engagement</code>.</p>
            description: <p>Provides a description of the <code>Engagement</code>.</p>
            contexts: <p>The <code>Contexts</code> field is a required array of objects, with a maximum of 5 contexts allowed, specifying detailed information about customer projects associated with the Engagement. Each context object contains a <code>Type</code> field indicating the context type, which must be <code>CustomerProject</code> in this version, and a <code>Payload</code> field containing the <code>CustomerProject</code> details. The <code>CustomerProject</code> object is composed of two main components: <code>Customer</code> and <code>Project</code>. The <code>Customer</code> object includes information such as <code>CompanyName</code>, <code>WebsiteUrl</code>, <code>Industry</code>, and <code>CountryCode</code>, providing essential details about the customer. The <code>Project</code> object contains <code>Title</code>, <code>BusinessProblem</code>, and <code>TargetCompletionDate</code>, offering insights into the specific project associated with the customer. This structure allows comprehensive context to be included within the Engagement, facilitating effective collaboration between parties by providing relevant customer and project information.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.create_engagement_request.CreateEngagementRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.create_engagement_response.CreateEngagementResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement.create_engagement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_engagement_request.CreateEngagementRequest = {
            "catalog": catalog,
            "client_token": client_token,
        }
        if title is not None:
            input_["title"] = title
        if description is not None:
            input_["description"] = description
        if contexts is not None:
            input_["contexts"] = contexts

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_engagement_response.GetEngagementResponse":
        """<p>Use this action to retrieve the engagement record for a given <code>EngagementIdentifier</code>.</p>

        Args:
            catalog: <p>Specifies the catalog related to the engagement request. Valid values are <code>AWS</code> and <code>Sandbox</code>.</p>
            identifier: <p>Specifies the identifier of the Engagement record to retrieve.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.get_engagement_request.GetEngagementRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.get_engagement_response.GetEngagementResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_engagement

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.get_engagement.get_engagement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_engagement_request.GetEngagementRequest = {
            "catalog": catalog,
            "identifier": identifier,
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
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        created_by: Optional[
            "capo_partnercentral_selling.types.aws_account_list.AwsAccountList"
        ] = None,
        exclude_created_by: Optional[
            "capo_partnercentral_selling.types.aws_account_list.AwsAccountList"
        ] = None,
        context_types: Optional[
            "capo_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
        ] = None,
        exclude_context_types: Optional[
            "capo_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.engagement_sort.EngagementSort"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.engagement_page_size.EngagementPageSize"
        ] = None,
        next_token: Optional[str] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_engagements_response.ListEngagementsResponse":
        """<p>This action allows users to retrieve a list of Engagement records from Partner Central. This action can be used to manage and track various engagements across different stages of the partner selling process. </p>

        Args:
            catalog: <p> Specifies the catalog related to the request. </p>
            created_by: <p> A list of AWS account IDs. When specified, the response includes engagements created by these accounts. This filter is useful for finding engagements created by specific team members. </p>
            exclude_created_by: <p>An array of strings representing AWS Account IDs. Use this to exclude engagements created by specific users. </p>
            context_types: <p>Filters engagements to include only those containing the specified context types, such as "CustomerProject" or "Lead". Use this to find engagements that have specific types of contextual information associated with them.</p>
            exclude_context_types: <p>Filters engagements to exclude those containing the specified context types. Use this to find engagements that do not have certain types of contextual information, helping to narrow results based on context exclusion criteria.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results. This value is returned from a previous call.</p>
            engagement_identifier: <p>An array of strings representing engagement identifiers to retrieve.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.list_engagements_request.ListEngagementsRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.list_engagements_response.ListEngagementsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagements

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagements.list_engagements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_engagements_request.ListEngagementsRequest = {
            "catalog": catalog
        }
        if created_by is not None:
            input_["created_by"] = created_by
        if exclude_created_by is not None:
            input_["exclude_created_by"] = exclude_created_by
        if context_types is not None:
            input_["context_types"] = context_types
        if exclude_context_types is not None:
            input_["exclude_context_types"] = exclude_context_types
        if sort is not None:
            input_["sort"] = sort
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_engagement_members(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.member_page_size.MemberPageSize"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_partnercentral_selling.types.list_engagement_members_response.ListEngagementMembersResponse":
        """<p>Retrieves the details of member partners in an Engagement. This operation can only be invoked by members of the Engagement. The <code>ListEngagementMembers</code> operation allows you to fetch information about the members of a specific Engagement. This action is restricted to members of the Engagement being queried. </p>

        Args:
            catalog: <p>The catalog related to the request.</p>
            identifier: <p>Identifier of the Engagement record to retrieve members from.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.list_engagement_members_request.ListEngagementMembersRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.list_engagement_members_response.ListEngagementMembersResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_members

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_members.list_engagement_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_engagement_members_request.ListEngagementMembersRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }
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


class AsyncEngagement:
    def __init__(self, service: AsyncPartnerCentralSellingClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        title: Optional[
            "capo_partnercentral_selling.types.engagement_title.EngagementTitle"
        ] = None,
        description: Optional[
            "capo_partnercentral_selling.types.engagement_description.EngagementDescription"
        ] = None,
        contexts: Optional[
            "capo_partnercentral_selling.types.engagement_contexts.EngagementContexts"
        ] = None,
    ) -> "capo_partnercentral_selling.types.create_engagement_response.CreateEngagementResponse":
        """<p>The <code>CreateEngagement</code> action allows you to create an <code>Engagement</code>, which serves as a collaborative space between different parties such as AWS Partners and AWS Sellers. This action automatically adds the caller's AWS account as an active member of the newly created <code>Engagement</code>.</p>

        Args:
            catalog: <p>The <code>CreateEngagementRequest$Catalog</code> parameter specifies the catalog related to the engagement. Accepted values are <code>AWS</code> and <code>Sandbox</code>, which determine the environment in which the engagement is managed.</p>
            client_token: <p>The <code>CreateEngagementRequest$ClientToken</code> parameter specifies a unique, case-sensitive identifier to ensure that the request is handled exactly once. The value must not exceed sixty-four alphanumeric characters.</p>
            title: <p>Specifies the title of the <code>Engagement</code>.</p>
            description: <p>Provides a description of the <code>Engagement</code>.</p>
            contexts: <p>The <code>Contexts</code> field is a required array of objects, with a maximum of 5 contexts allowed, specifying detailed information about customer projects associated with the Engagement. Each context object contains a <code>Type</code> field indicating the context type, which must be <code>CustomerProject</code> in this version, and a <code>Payload</code> field containing the <code>CustomerProject</code> details. The <code>CustomerProject</code> object is composed of two main components: <code>Customer</code> and <code>Project</code>. The <code>Customer</code> object includes information such as <code>CompanyName</code>, <code>WebsiteUrl</code>, <code>Industry</code>, and <code>CountryCode</code>, providing essential details about the customer. The <code>Project</code> object contains <code>Title</code>, <code>BusinessProblem</code>, and <code>TargetCompletionDate</code>, offering insights into the specific project associated with the customer. This structure allows comprehensive context to be included within the Engagement, facilitating effective collaboration between parties by providing relevant customer and project information.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.create_engagement_request.CreateEngagementRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.create_engagement_response.CreateEngagementResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement.async_create_engagement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_engagement_request.CreateEngagementRequest = {
            "catalog": catalog,
            "client_token": client_token,
        }
        if title is not None:
            input_["title"] = title
        if description is not None:
            input_["description"] = description
        if contexts is not None:
            input_["contexts"] = contexts

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_engagement_response.GetEngagementResponse":
        """<p>Use this action to retrieve the engagement record for a given <code>EngagementIdentifier</code>.</p>

        Args:
            catalog: <p>Specifies the catalog related to the engagement request. Valid values are <code>AWS</code> and <code>Sandbox</code>.</p>
            identifier: <p>Specifies the identifier of the Engagement record to retrieve.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.get_engagement_request.GetEngagementRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.get_engagement_response.GetEngagementResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_engagement

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.get_engagement.async_get_engagement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_engagement_request.GetEngagementRequest = {
            "catalog": catalog,
            "identifier": identifier,
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
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        created_by: Optional[
            "capo_partnercentral_selling.types.aws_account_list.AwsAccountList"
        ] = None,
        exclude_created_by: Optional[
            "capo_partnercentral_selling.types.aws_account_list.AwsAccountList"
        ] = None,
        context_types: Optional[
            "capo_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
        ] = None,
        exclude_context_types: Optional[
            "capo_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.engagement_sort.EngagementSort"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.engagement_page_size.EngagementPageSize"
        ] = None,
        next_token: Optional[str] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_engagements_response.ListEngagementsResponse":
        """<p>This action allows users to retrieve a list of Engagement records from Partner Central. This action can be used to manage and track various engagements across different stages of the partner selling process. </p>

        Args:
            catalog: <p> Specifies the catalog related to the request. </p>
            created_by: <p> A list of AWS account IDs. When specified, the response includes engagements created by these accounts. This filter is useful for finding engagements created by specific team members. </p>
            exclude_created_by: <p>An array of strings representing AWS Account IDs. Use this to exclude engagements created by specific users. </p>
            context_types: <p>Filters engagements to include only those containing the specified context types, such as "CustomerProject" or "Lead". Use this to find engagements that have specific types of contextual information associated with them.</p>
            exclude_context_types: <p>Filters engagements to exclude those containing the specified context types. Use this to find engagements that do not have certain types of contextual information, helping to narrow results based on context exclusion criteria.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results. This value is returned from a previous call.</p>
            engagement_identifier: <p>An array of strings representing engagement identifiers to retrieve.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_engagements_request.ListEngagementsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_engagements_response.ListEngagementsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagements

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagements.async_list_engagements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_engagements_request.ListEngagementsRequest = {
            "catalog": catalog
        }
        if created_by is not None:
            input_["created_by"] = created_by
        if exclude_created_by is not None:
            input_["exclude_created_by"] = exclude_created_by
        if context_types is not None:
            input_["context_types"] = context_types
        if exclude_context_types is not None:
            input_["exclude_context_types"] = exclude_context_types
        if sort is not None:
            input_["sort"] = sort
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_engagement_members(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.member_page_size.MemberPageSize"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_partnercentral_selling.types.list_engagement_members_response.ListEngagementMembersResponse":
        """<p>Retrieves the details of member partners in an Engagement. This operation can only be invoked by members of the Engagement. The <code>ListEngagementMembers</code> operation allows you to fetch information about the members of a specific Engagement. This action is restricted to members of the Engagement being queried. </p>

        Args:
            catalog: <p>The catalog related to the request.</p>
            identifier: <p>Identifier of the Engagement record to retrieve members from.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_engagement_members_request.ListEngagementMembersRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_engagement_members_response.ListEngagementMembersResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_members

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_members.async_list_engagement_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_engagement_members_request.ListEngagementMembersRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }
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
