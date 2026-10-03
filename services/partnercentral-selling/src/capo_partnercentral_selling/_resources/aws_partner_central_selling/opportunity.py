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
    import capo_partnercentral_selling.types.assign_opportunity_request
    import capo_partnercentral_selling.types.assignee_contact
    import capo_partnercentral_selling.types.associate_opportunity_request
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.create_opportunity_request
    import capo_partnercentral_selling.types.create_opportunity_response
    import capo_partnercentral_selling.types.created_date_filter
    import capo_partnercentral_selling.types.customer
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.disassociate_opportunity_request
    import capo_partnercentral_selling.types.filter_identifier
    import capo_partnercentral_selling.types.filter_life_cycle_review_status
    import capo_partnercentral_selling.types.filter_life_cycle_stage
    import capo_partnercentral_selling.types.get_aws_opportunity_summary_request
    import capo_partnercentral_selling.types.get_aws_opportunity_summary_response
    import capo_partnercentral_selling.types.get_opportunity_request
    import capo_partnercentral_selling.types.get_opportunity_response
    import capo_partnercentral_selling.types.last_modified_date
    import capo_partnercentral_selling.types.life_cycle
    import capo_partnercentral_selling.types.list_opportunities_request
    import capo_partnercentral_selling.types.list_opportunities_response
    import capo_partnercentral_selling.types.marketing
    import capo_partnercentral_selling.types.national_security
    import capo_partnercentral_selling.types.opportunity_identifier
    import capo_partnercentral_selling.types.opportunity_origin
    import capo_partnercentral_selling.types.opportunity_sort
    import capo_partnercentral_selling.types.opportunity_summary
    import capo_partnercentral_selling.types.opportunity_type
    import capo_partnercentral_selling.types.page_size
    import capo_partnercentral_selling.types.partner_opportunity_team_members_list
    import capo_partnercentral_selling.types.primary_needs_from_aws
    import capo_partnercentral_selling.types.project
    import capo_partnercentral_selling.types.related_entity_type
    import capo_partnercentral_selling.types.sales_involvement_type
    import capo_partnercentral_selling.types.software_revenue
    import capo_partnercentral_selling.types.string_list
    import capo_partnercentral_selling.types.submit_opportunity_request
    import capo_partnercentral_selling.types.tag_list
    import capo_partnercentral_selling.types.target_close_date_filter
    import capo_partnercentral_selling.types.update_opportunity_request
    import capo_partnercentral_selling.types.update_opportunity_response
    import capo_partnercentral_selling.types.visibility
    from capo_partnercentral_selling._services.async_partner_central_selling import (
        AsyncPartnerCentralSellingClient,
        AsyncPartnerCentralSellingClientConfig,
    )
    from capo_partnercentral_selling._services.partner_central_selling import (
        PartnerCentralSellingClient,
        PartnerCentralSellingClientConfig,
    )


class Opportunity:
    def __init__(self, service: PartnerCentralSellingClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        primary_needs_from_aws: Optional[
            "capo_partnercentral_selling.types.primary_needs_from_aws.PrimaryNeedsFromAws"
        ] = None,
        national_security: Optional[
            "capo_partnercentral_selling.types.national_security.NationalSecurity"
        ] = None,
        partner_opportunity_identifier: Optional[str] = None,
        customer: Optional[
            "capo_partnercentral_selling.types.customer.Customer"
        ] = None,
        project: Optional["capo_partnercentral_selling.types.project.Project"] = None,
        opportunity_type: Optional[
            "capo_partnercentral_selling.types.opportunity_type.OpportunityType"
        ] = None,
        marketing: Optional[
            "capo_partnercentral_selling.types.marketing.Marketing"
        ] = None,
        software_revenue: Optional[
            "capo_partnercentral_selling.types.software_revenue.SoftwareRevenue"
        ] = None,
        life_cycle: Optional[
            "capo_partnercentral_selling.types.life_cycle.LifeCycle"
        ] = None,
        origin: Optional[
            "capo_partnercentral_selling.types.opportunity_origin.OpportunityOrigin"
        ] = None,
        opportunity_team: Optional[
            "capo_partnercentral_selling.types.partner_opportunity_team_members_list.PartnerOpportunityTeamMembersList"
        ] = None,
        tags: Optional["capo_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_selling.types.create_opportunity_response.CreateOpportunityResponse":
        """<p>Creates an <code>Opportunity</code> record in Partner Central. Use this operation to create a potential business opportunity for submission to Amazon Web Services. Creating an opportunity sets <code>Lifecycle.ReviewStatus</code> to <code>Pending Submission</code>.</p> <p>To submit an opportunity, follow these steps:</p> <ol> <li> <p>To create the opportunity, use <code>CreateOpportunity</code>.</p> </li> <li> <p>To associate a solution with the opportunity, use <code>AssociateOpportunity</code>.</p> </li> <li> <p>To start the engagement with AWS, use <code>StartEngagementFromOpportunity</code>.</p> </li> </ol> <p>After submission, you can't edit the opportunity until the review is complete. But opportunities in the <code>Pending Submission</code> state must have complete details. You can update the opportunity while it's in the <code>Pending Submission</code> state.</p> <p>There's a set of mandatory fields to create opportunities, but consider providing optional fields to enrich the opportunity record.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity is created in. Use <code>AWS</code> to create opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            primary_needs_from_aws: <p>Identifies the type of support the partner needs from Amazon Web Services.</p> <p>Valid values:</p> <ul> <li> <p>Cosell—Architectural Validation: Confirmation from Amazon Web Services that the partner's proposed solution architecture is aligned with Amazon Web Services best practices and poses minimal architectural risks.</p> </li> <li> <p>Cosell—Business Presentation: Request Amazon Web Services seller's participation in a joint customer presentation.</p> </li> <li> <p>Cosell—Competitive Information: Access to Amazon Web Services competitive resources and support for the partner's proposed solution.</p> </li> <li> <p>Cosell—Pricing Assistance: Connect with an Amazon Web Services seller for support situations where a partner may be receiving an upfront discount on a service (for example: EDP deals).</p> </li> <li> <p>Cosell—Technical Consultation: Connect with an Amazon Web Services Solutions Architect to address the partner's questions about the proposed solution.</p> </li> <li> <p>Cosell—Total Cost of Ownership Evaluation: Assistance with quoting different cost savings of proposed solutions on Amazon Web Services versus on-premises or a traditional hosting environment.</p> </li> <li> <p>Cosell—Deal Support: Request Amazon Web Services seller's support to progress the opportunity (for example: joint customer call, strategic positioning).</p> </li> <li> <p>Cosell—Support for Public Tender/RFx: Opportunity related to the public sector where the partner needs Amazon Web Services RFx support.</p> </li> </ul>
            national_security: <p>Indicates whether the <code>Opportunity</code> pertains to a national security project. This field must be set to <code>true</code> only when the customer's industry is <i>Government</i>. Additional privacy and security measures apply during the review and management process for opportunities marked as <code>NationalSecurity</code>.</p>
            partner_opportunity_identifier: <p>Specifies the opportunity's unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload to the partner.</p> <p>This field allows partners to link an opportunity to their CRM, which helps to ensure seamless integration and accurate synchronization between the Partner Central API and the partner's internal systems.</p>
            customer: <p>Specifies customer details associated with the <code>Opportunity</code>.</p>
            project: <p>An object that contains project details for the <code>Opportunity</code>.</p>
            opportunity_type: <p>Specifies the opportunity type as a renewal, new, or expansion.</p> <p>Opportunity types:</p> <ul> <li> <p>New opportunity: Represents a new business opportunity with a potential customer that's not previously engaged with your solutions or services.</p> </li> <li> <p>Renewal opportunity: Represents an opportunity to renew an existing contract or subscription with a current customer, ensuring continuity of service.</p> </li> <li> <p>Expansion opportunity: Represents an opportunity to expand the scope of an existing contract or subscription, either by adding new services or increasing the volume of existing services for a current customer.</p> </li> </ul>
            marketing: <p>This object contains marketing details and is optional for an opportunity.</p>
            software_revenue: <p>Specifies details of a customer's procurement terms. This is required only for partners in eligible programs.</p>
            client_token: <p>Required to be unique, and should be unchanging, it can be randomly generated or a meaningful string.</p> <p>Default: None</p> <p>Best practice: To help ensure uniqueness and avoid conflicts, use a Universally Unique Identifier (UUID) as the <code>ClientToken</code>. You can use standard libraries from most programming languages to generate this. If you use the same client token, the API returns the following error: "Conflicting client token submitted for a new request body."</p>
            life_cycle: <p>An object that contains lifecycle details for the <code>Opportunity</code>.</p>
            origin: <p>Specifies the origin of the opportunity, indicating if it was sourced from Amazon Web Services or the partner. For all opportunities created with <code>Catalog: AWS</code>, this field must only be <code>Partner Referral</code>. However, when using <code>Catalog: Sandbox</code>, you can set this field to <code>AWS Referral</code> to simulate Amazon Web Services referral creation. This allows Amazon Web Services-originated flows testing in the sandbox catalog.</p>
            opportunity_team: <p>Represents the internal team handling the opportunity. Specify collaborating members of this opportunity who are within the partner's organization.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.create_opportunity_request.CreateOpportunityRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.create_opportunity_response.CreateOpportunityResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_opportunity

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.create_opportunity.create_opportunity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_opportunity_request.CreateOpportunityRequest = {
            "catalog": catalog,
            "client_token": client_token,
        }
        if primary_needs_from_aws is not None:
            input_["primary_needs_from_aws"] = primary_needs_from_aws
        if national_security is not None:
            input_["national_security"] = national_security
        if partner_opportunity_identifier is not None:
            input_["partner_opportunity_identifier"] = partner_opportunity_identifier
        if customer is not None:
            input_["customer"] = customer
        if project is not None:
            input_["project"] = project
        if opportunity_type is not None:
            input_["opportunity_type"] = opportunity_type
        if marketing is not None:
            input_["marketing"] = marketing
        if software_revenue is not None:
            input_["software_revenue"] = software_revenue
        if life_cycle is not None:
            input_["life_cycle"] = life_cycle
        if origin is not None:
            input_["origin"] = origin
        if opportunity_team is not None:
            input_["opportunity_team"] = opportunity_team
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
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_opportunity_response.GetOpportunityResponse":
        """<p>Fetches the <code>Opportunity</code> record from Partner Central by a given <code>Identifier</code>.</p> <p>Use the <code>ListOpportunities</code> action or the event notification (from Amazon EventBridge) to obtain this identifier.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity is fetched from. Use <code>AWS</code> to retrieve opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> to retrieve opportunities in a secure, isolated testing environment.</p>
            identifier: <p>Read-only, system generated <code>Opportunity</code> unique identifier.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.get_opportunity_request.GetOpportunityRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.get_opportunity_response.GetOpportunityResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_opportunity

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.get_opportunity.get_opportunity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_opportunity_request.GetOpportunityRequest = {
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

    def update(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        last_modified_date: "capo_partnercentral_selling.types.date_time.DateTime",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        primary_needs_from_aws: Optional[
            "capo_partnercentral_selling.types.primary_needs_from_aws.PrimaryNeedsFromAws"
        ] = None,
        national_security: Optional[
            "capo_partnercentral_selling.types.national_security.NationalSecurity"
        ] = None,
        partner_opportunity_identifier: Optional[str] = None,
        customer: Optional[
            "capo_partnercentral_selling.types.customer.Customer"
        ] = None,
        project: Optional["capo_partnercentral_selling.types.project.Project"] = None,
        opportunity_type: Optional[
            "capo_partnercentral_selling.types.opportunity_type.OpportunityType"
        ] = None,
        marketing: Optional[
            "capo_partnercentral_selling.types.marketing.Marketing"
        ] = None,
        software_revenue: Optional[
            "capo_partnercentral_selling.types.software_revenue.SoftwareRevenue"
        ] = None,
        life_cycle: Optional[
            "capo_partnercentral_selling.types.life_cycle.LifeCycle"
        ] = None,
    ) -> "capo_partnercentral_selling.types.update_opportunity_response.UpdateOpportunityResponse":
        """<p>Updates the <code>Opportunity</code> record identified by a given <code>Identifier</code>. This operation allows you to modify the details of an existing opportunity to reflect the latest information and progress. Use this action to keep the opportunity record up-to-date and accurate.</p> <p>When you perform updates, include the entire payload with each request. If any field is omitted, the API assumes that the field is set to <code>null</code>. The best practice is to always perform a <code>GetOpportunity</code> to retrieve the latest values, then send the complete payload with the updated values to be changed.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity is updated in. Use <code>AWS</code> to update real opportunities in the production environment, and <code>Sandbox</code> for testing in secure, isolated environments. When you use the <code>Sandbox</code> catalog, it allows you to simulate and validate your interactions with Amazon Web Services services without affecting live data or operations.</p>
            primary_needs_from_aws: <p>Identifies the type of support the partner needs from Amazon Web Services.</p> <p>Valid values:</p> <ul> <li> <p>Cosell—Architectural Validation: Confirmation from Amazon Web Services that the partner's proposed solution architecture is aligned with Amazon Web Services best practices and poses minimal architectural risks.</p> </li> <li> <p>Cosell—Business Presentation: Request Amazon Web Services seller's participation in a joint customer presentation.</p> </li> <li> <p>Cosell—Competitive Information: Access to Amazon Web Services competitive resources and support for the partner's proposed solution.</p> </li> <li> <p>Cosell—Pricing Assistance: Connect with an AWS seller for support situations where a partner may be receiving an upfront discount on a service (for example: EDP deals).</p> </li> <li> <p>Cosell—Technical Consultation: Connection with an Amazon Web Services Solutions Architect to address the partner's questions about the proposed solution.</p> </li> <li> <p>Cosell—Total Cost of Ownership Evaluation: Assistance with quoting different cost savings of proposed solutions on Amazon Web Services versus on-premises or a traditional hosting environment.</p> </li> <li> <p>Cosell—Deal Support: Request Amazon Web Services seller's support to progress the opportunity (for example: joint customer call, strategic positioning).</p> </li> <li> <p>Cosell—Support for Public Tender/RFx: Opportunity related to the public sector where the partner needs RFx support from Amazon Web Services.</p> </li> </ul>
            national_security: <p>Specifies if the opportunity is associated with national security concerns. This flag is only applicable when the industry is <code>Government</code>. For national-security-related opportunities, validation and compliance rules may apply, impacting the opportunity's visibility and processing.</p>
            partner_opportunity_identifier: <p>Specifies the opportunity's unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload sent back to the partner.</p>
            customer: <p>Specifies details of the customer associated with the <code>Opportunity</code>.</p>
            project: <p>An object that contains project details summary for the <code>Opportunity</code>.</p>
            opportunity_type: <p>Specifies the opportunity type as a renewal, new, or expansion.</p> <p>Opportunity types:</p> <ul> <li> <p>New opportunity: Represents a new business opportunity with a potential customer that's not previously engaged with your solutions or services.</p> </li> <li> <p>Renewal opportunity: Represents an opportunity to renew an existing contract or subscription with a current customer, ensuring continuity of service.</p> </li> <li> <p>Expansion opportunity: Represents an opportunity to expand the scope of an existing contract or subscription, either by adding new services or increasing the volume of existing services for a current customer.</p> </li> </ul>
            marketing: <p>An object that contains marketing details for the <code>Opportunity</code>.</p>
            software_revenue: <p>Specifies details of a customer's procurement terms. Required only for partners in eligible programs.</p>
            last_modified_date: <p> <code>DateTime</code> when the opportunity was last modified.</p>
            identifier: <p>Read-only, system generated <code>Opportunity</code> unique identifier.</p>
            life_cycle: <p>An object that contains lifecycle details for the <code>Opportunity</code>.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.update_opportunity_request.UpdateOpportunityRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.update_opportunity_response.UpdateOpportunityResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.update_opportunity

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.update_opportunity.update_opportunity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.update_opportunity_request.UpdateOpportunityRequest = {
            "catalog": catalog,
            "last_modified_date": last_modified_date,
            "identifier": identifier,
        }
        if primary_needs_from_aws is not None:
            input_["primary_needs_from_aws"] = primary_needs_from_aws
        if national_security is not None:
            input_["national_security"] = national_security
        if partner_opportunity_identifier is not None:
            input_["partner_opportunity_identifier"] = partner_opportunity_identifier
        if customer is not None:
            input_["customer"] = customer
        if project is not None:
            input_["project"] = project
        if opportunity_type is not None:
            input_["opportunity_type"] = opportunity_type
        if marketing is not None:
            input_["marketing"] = marketing
        if software_revenue is not None:
            input_["software_revenue"] = software_revenue
        if life_cycle is not None:
            input_["life_cycle"] = life_cycle

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
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.opportunity_sort.OpportunitySort"
        ] = None,
        last_modified_date: Optional[
            "capo_partnercentral_selling.types.last_modified_date.LastModifiedDate"
        ] = None,
        identifier: Optional[
            "capo_partnercentral_selling.types.filter_identifier.FilterIdentifier"
        ] = None,
        life_cycle_stage: Optional[
            "capo_partnercentral_selling.types.filter_life_cycle_stage.FilterLifeCycleStage"
        ] = None,
        life_cycle_review_status: Optional[
            "capo_partnercentral_selling.types.filter_life_cycle_review_status.FilterLifeCycleReviewStatus"
        ] = None,
        customer_company_name: Optional[
            "capo_partnercentral_selling.types.string_list.StringList"
        ] = None,
        created_date: Optional[
            "capo_partnercentral_selling.types.created_date_filter.CreatedDateFilter"
        ] = None,
        target_close_date: Optional[
            "capo_partnercentral_selling.types.target_close_date_filter.TargetCloseDateFilter"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_opportunities_response.ListOpportunitiesResponse":
        """<p>This request accepts a list of filters that retrieve opportunity subsets as well as sort options. This feature is available to partners from <a href="https://partnercentral.awspartner.com/">Partner Central</a> using the <code>ListOpportunities</code> API action.</p> <p>To synchronize your system with Amazon Web Services, list only the opportunities that were newly created or updated. We recommend you rely on events emitted by the service into your Amazon Web Services account’s Amazon EventBridge default event bus. You can also use the <code>ListOpportunities</code> action.</p> <p>We recommend the following approach:</p> <ol> <li> <p>Find the latest <code>LastModifiedDate</code> that you stored, and only use the values that came from Amazon Web Services. Don’t use values generated by your system.</p> </li> <li> <p>When you send a <code>ListOpportunities</code> request, submit the date in ISO 8601 format in the <code>AfterLastModifiedDate</code> filter.</p> </li> <li> <p>Amazon Web Services only returns opportunities created or updated on or after that date and time. Use <code>NextToken</code> to iterate over all pages.</p> </li> </ol>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunities are listed in. Use <code>AWS</code> for listing real opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            max_results: <p>Specifies the maximum number of results to return in a single call. This limits the number of opportunities returned in the response to avoid providing too many results at once.</p> <p>Default: 20</p>
            next_token: <p>A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.</p>
            sort: <p>An object that specifies how the response is sorted. The default <code>Sort.SortBy</code> value is <code>LastModifiedDate</code>.</p>
            last_modified_date: <p>Filters the opportunities based on their last modified date. This filter helps retrieve opportunities that were updated after the specified date, allowing partners to track recent changes or updates.</p>
            identifier: <p>Filters the opportunities based on the opportunity identifier. This allows partners to retrieve specific opportunities by providing their unique identifiers, ensuring precise results.</p>
            life_cycle_stage: <p>Filters the opportunities based on their lifecycle stage. This filter allows partners to retrieve opportunities at various stages in the sales cycle, such as <code>Qualified</code>, <code>Technical Validation</code>, <code>Business Validation</code>, or <code>Closed Won</code>.</p>
            life_cycle_review_status: <p>Filters the opportunities based on their current lifecycle approval status. Use this filter to retrieve opportunities with statuses such as <code>Pending Submission</code>, <code>In Review</code>, <code>Action Required</code>, or <code>Approved</code>.</p>
            customer_company_name: <p>Filters the opportunities based on the customer's company name. This allows partners to search for opportunities associated with a specific customer by matching the provided company name string.</p>
            created_date: <p>Filter opportunities by creation date criteria.</p>
            target_close_date: <p>Filters opportunities based on their target close date. This filter helps retrieve opportunities with an expected close date before or after a specified date.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.list_opportunities_request.ListOpportunitiesRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.list_opportunities_response.ListOpportunitiesResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_opportunities

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.list_opportunities.list_opportunities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_opportunities_request.ListOpportunitiesRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        if last_modified_date is not None:
            input_["last_modified_date"] = last_modified_date
        if identifier is not None:
            input_["identifier"] = identifier
        if life_cycle_stage is not None:
            input_["life_cycle_stage"] = life_cycle_stage
        if life_cycle_review_status is not None:
            input_["life_cycle_review_status"] = life_cycle_review_status
        if customer_company_name is not None:
            input_["customer_company_name"] = customer_company_name
        if created_date is not None:
            input_["created_date"] = created_date
        if target_close_date is not None:
            input_["target_close_date"] = target_close_date

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def assign_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        assignee: "capo_partnercentral_selling.types.assignee_contact.AssigneeContact",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Enables you to reassign an existing <code>Opportunity</code> to another user within your Partner Central account. The specified user receives the opportunity, and it appears on their Partner Central dashboard, allowing them to take necessary actions or proceed with the opportunity.</p> <p>This is useful for distributing opportunities to the appropriate team members or departments within your organization, ensuring that each opportunity is handled by the right person. By default, the opportunity owner is the one who creates it. Currently, there's no API to enumerate the list of available users.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity is assigned in. Use <code>AWS</code> to assign real opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            identifier: <p>Requires the <code>Opportunity</code>'s unique identifier when you want to assign it to another user. Provide the correct identifier so the intended opportunity is reassigned.</p>
            assignee: <p>Specifies the user or team member responsible for managing the assigned opportunity. This field identifies the <i>Assignee</i> based on the partner's internal team structure. Ensure that the email address is associated with a registered user in your Partner Central account.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.assign_opportunity_request.AssignOpportunityRequest]",
        ) -> OperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.assign_opportunity

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.assign_opportunity.assign_opportunity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.assign_opportunity_request.AssignOpportunityRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "assignee": assignee,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        opportunity_identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        related_entity_type: "capo_partnercentral_selling.types.related_entity_type.RelatedEntityType",
        related_entity_identifier: str,
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Enables you to create a formal association between an <code>Opportunity</code> and various related entities, enriching the context and details of the opportunity for better collaboration and decision making. You can associate an opportunity with the following entity types:</p> <ul> <li> <p>Partner Solution: A software product or consulting practice created and delivered by Partners. Partner Solutions help customers address business challenges using Amazon Web Services services.</p> </li> <li> <p>Amazon Web Services Products: Amazon Web Services offers many products and services that provide scalable, reliable, and cost-effective infrastructure solutions. For the latest list of Amazon Web Services products, see <a href="https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json">Amazon Web Services products</a>.</p> </li> <li> <p>Amazon Web Services Marketplace private offer: Allows Amazon Web Services Marketplace sellers to extend custom pricing and terms to individual Amazon Web Services customers. Sellers can negotiate custom prices, payment schedules, and end user license terms through private offers, enabling Amazon Web Services customers to acquire software solutions tailored to their specific needs. For more information, see <a href="https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-private-offers.html">Private offers in Amazon Web Services Marketplace</a>.</p> </li> </ul> <p>To obtain identifiers for these entities, use the following methods:</p> <ul> <li> <p>Solution: Use the <code>ListSolutions</code> operation.</p> </li> <li> <p>AWS Products: For the latest list of Amazon Web Services products, see <a href="https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json">Amazon Web Services products</a>.</p> </li> <li> <p>Amazon Web Services Marketplace private offer: Use the <a href="https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html">Using the Amazon Web Services Marketplace Catalog API</a> to list entities. Specifically, use the <code>ListEntities</code> operation to retrieve a list of private offers. The request returns the details of available private offers. For more information, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_ListEntities.html">ListEntities</a>.</p> </li> </ul>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity association is made in. Use <code>AWS</code> to associate opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            opportunity_identifier: <p>Requires the <code>Opportunity</code>'s unique identifier when you want to associate it with a related entity. Provide the correct identifier so the intended opportunity is updated with the association.</p>
            related_entity_type: <p>Specifies the entity type that you're associating with the <code> Opportunity</code>. This helps to categorize and properly process the association.</p>
            related_entity_identifier: <p>Requires the related entity's unique identifier when you want to associate it with the <code> Opportunity</code>. For Amazon Web Services Marketplace entities, provide the Amazon Resource Name (ARN). Use the <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html"> Amazon Web Services Marketplace API</a> to obtain the ARN.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.associate_opportunity_request.AssociateOpportunityRequest]",
        ) -> OperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.associate_opportunity

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.associate_opportunity.associate_opportunity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.associate_opportunity_request.AssociateOpportunityRequest = {
            "catalog": catalog,
            "opportunity_identifier": opportunity_identifier,
            "related_entity_type": related_entity_type,
            "related_entity_identifier": related_entity_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        opportunity_identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        related_entity_type: "capo_partnercentral_selling.types.related_entity_type.RelatedEntityType",
        related_entity_identifier: str,
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Allows you to remove an existing association between an <code>Opportunity</code> and related entities, such as a Partner Solution, Amazon Web Services product, or an Amazon Web Services Marketplace offer. This operation is the counterpart to <code>AssociateOpportunity</code>, and it provides flexibility to manage associations as business needs change.</p> <p>Use this operation to update the associations of an <code>Opportunity</code> due to changes in the related entities, or if an association was made in error. Ensuring accurate associations helps maintain clarity and accuracy to track and manage business opportunities. When you replace an entity, first attach the new entity and then disassociate the one to be removed, especially if it's the last remaining entity that's required.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity disassociation is made in. Use <code>AWS</code> to disassociate opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            opportunity_identifier: <p>The opportunity's unique identifier for when you want to disassociate it from related entities. This identifier helps to ensure that the correct opportunity is updated.</p> <p>Validation: Ensure that the provided identifier corresponds to an existing opportunity in the Amazon Web Services system because incorrect identifiers result in an error and no changes are made.</p>
            related_entity_type: <p>The type of the entity that you're disassociating from the opportunity. When you specify the entity type, it helps the system correctly process the disassociation request to ensure that the right connections are removed.</p> <p>Examples of entity types include Partner Solution, Amazon Web Services product, and Amazon Web Services Marketplaceoffer. Ensure that the value matches one of the expected entity types.</p> <p>Validation: Provide a valid entity type to help ensure successful disassociation. An invalid or incorrect entity type results in an error.</p>
            related_entity_identifier: <p>The related entity's identifier that you want to disassociate from the opportunity. Depending on the type of entity, this could be a simple identifier or an Amazon Resource Name (ARN) for entities managed through Amazon Web Services Marketplace.</p> <p>For Amazon Web Services Marketplace entities, use the Amazon Web Services Marketplace API to obtain the necessary ARNs. For guidance on retrieving these ARNs, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html"> Amazon Web Services MarketplaceUsing the Amazon Web Services Marketplace Catalog API</a>.</p> <p>Validation: Ensure the identifier or ARN is valid and corresponds to an existing entity. An incorrect or invalid identifier results in an error.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.disassociate_opportunity_request.DisassociateOpportunityRequest]",
        ) -> OperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.disassociate_opportunity

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.disassociate_opportunity.disassociate_opportunity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.disassociate_opportunity_request.DisassociateOpportunityRequest = {
            "catalog": catalog,
            "opportunity_identifier": opportunity_identifier,
            "related_entity_type": related_entity_type,
            "related_entity_identifier": related_entity_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_aws_opportunity_summary(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        related_opportunity_identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_aws_opportunity_summary_response.GetAwsOpportunitySummaryResponse":
        """<p>Retrieves a summary of an AWS Opportunity. This summary includes high-level details about the opportunity sourced from AWS, such as lifecycle information, customer details, and involvement type. It is useful for tracking updates on the AWS opportunity corresponding to an opportunity in the partner's account.</p>

        Args:
            catalog: <p>Specifies the catalog in which the AWS Opportunity is located. Accepted values include <code>AWS</code> for production opportunities or <code>Sandbox</code> for testing purposes. The catalog determines which environment the opportunity data is pulled from.</p>
            related_opportunity_identifier: <p>The unique identifier for the related partner opportunity. Use this field to correlate an AWS opportunity with its corresponding partner opportunity.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.get_aws_opportunity_summary_request.GetAwsOpportunitySummaryRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.get_aws_opportunity_summary_response.GetAwsOpportunitySummaryResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_aws_opportunity_summary

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.get_aws_opportunity_summary.get_aws_opportunity_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_aws_opportunity_summary_request.GetAwsOpportunitySummaryRequest = {
            "catalog": catalog,
            "related_opportunity_identifier": related_opportunity_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def submit_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        involvement_type: "capo_partnercentral_selling.types.sales_involvement_type.SalesInvolvementType",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        visibility: Optional[
            "capo_partnercentral_selling.types.visibility.Visibility"
        ] = None,
    ) -> None:
        """<p>Use this action to submit an Opportunity that was previously created by partner for AWS review. After you perform this action, the Opportunity becomes non-editable until it is reviewed by AWS and has <code> LifeCycle.ReviewStatus </code> as either <code>Approved</code> or <code>Action Required</code>. </p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Submits the opportunity request from the production AWS environment.</p> </li> <li> <p>Sandbox: Submits the opportunity request from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            identifier: <p>The identifier of the Opportunity previously created by partner and needs to be submitted.</p>
            involvement_type: <p>Specifies the level of AWS sellers' involvement on the opportunity. Valid values:</p> <ul> <li> <p> <code>Co-sell</code>: Indicates the user wants to co-sell with AWS. Share the opportunity with AWS to receive deal assistance and support.</p> </li> <li> <p> <code>For Visibility Only</code>: Indicates that the user does not need support from AWS Sales Rep. Share this opportunity with AWS for visibility only, you will not receive deal assistance and support.</p> </li> </ul>
            visibility: <p>Determines whether to restrict visibility of the opportunity from AWS sales. Default value is Full. Valid values:</p> <ul> <li> <p> <code>Full</code>: The opportunity is fully visible to AWS sales.</p> </li> <li> <p> <code>Limited</code>: The opportunity has restricted visibility to AWS sales.</p> </li> </ul>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.submit_opportunity_request.SubmitOpportunityRequest]",
        ) -> OperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.submit_opportunity

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.submit_opportunity.submit_opportunity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.submit_opportunity_request.SubmitOpportunityRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "involvement_type": involvement_type,
        }
        if visibility is not None:
            input_["visibility"] = visibility

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncOpportunity:
    def __init__(self, service: AsyncPartnerCentralSellingClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        primary_needs_from_aws: Optional[
            "capo_partnercentral_selling.types.primary_needs_from_aws.PrimaryNeedsFromAws"
        ] = None,
        national_security: Optional[
            "capo_partnercentral_selling.types.national_security.NationalSecurity"
        ] = None,
        partner_opportunity_identifier: Optional[str] = None,
        customer: Optional[
            "capo_partnercentral_selling.types.customer.Customer"
        ] = None,
        project: Optional["capo_partnercentral_selling.types.project.Project"] = None,
        opportunity_type: Optional[
            "capo_partnercentral_selling.types.opportunity_type.OpportunityType"
        ] = None,
        marketing: Optional[
            "capo_partnercentral_selling.types.marketing.Marketing"
        ] = None,
        software_revenue: Optional[
            "capo_partnercentral_selling.types.software_revenue.SoftwareRevenue"
        ] = None,
        life_cycle: Optional[
            "capo_partnercentral_selling.types.life_cycle.LifeCycle"
        ] = None,
        origin: Optional[
            "capo_partnercentral_selling.types.opportunity_origin.OpportunityOrigin"
        ] = None,
        opportunity_team: Optional[
            "capo_partnercentral_selling.types.partner_opportunity_team_members_list.PartnerOpportunityTeamMembersList"
        ] = None,
        tags: Optional["capo_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_selling.types.create_opportunity_response.CreateOpportunityResponse":
        """<p>Creates an <code>Opportunity</code> record in Partner Central. Use this operation to create a potential business opportunity for submission to Amazon Web Services. Creating an opportunity sets <code>Lifecycle.ReviewStatus</code> to <code>Pending Submission</code>.</p> <p>To submit an opportunity, follow these steps:</p> <ol> <li> <p>To create the opportunity, use <code>CreateOpportunity</code>.</p> </li> <li> <p>To associate a solution with the opportunity, use <code>AssociateOpportunity</code>.</p> </li> <li> <p>To start the engagement with AWS, use <code>StartEngagementFromOpportunity</code>.</p> </li> </ol> <p>After submission, you can't edit the opportunity until the review is complete. But opportunities in the <code>Pending Submission</code> state must have complete details. You can update the opportunity while it's in the <code>Pending Submission</code> state.</p> <p>There's a set of mandatory fields to create opportunities, but consider providing optional fields to enrich the opportunity record.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity is created in. Use <code>AWS</code> to create opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            primary_needs_from_aws: <p>Identifies the type of support the partner needs from Amazon Web Services.</p> <p>Valid values:</p> <ul> <li> <p>Cosell—Architectural Validation: Confirmation from Amazon Web Services that the partner's proposed solution architecture is aligned with Amazon Web Services best practices and poses minimal architectural risks.</p> </li> <li> <p>Cosell—Business Presentation: Request Amazon Web Services seller's participation in a joint customer presentation.</p> </li> <li> <p>Cosell—Competitive Information: Access to Amazon Web Services competitive resources and support for the partner's proposed solution.</p> </li> <li> <p>Cosell—Pricing Assistance: Connect with an Amazon Web Services seller for support situations where a partner may be receiving an upfront discount on a service (for example: EDP deals).</p> </li> <li> <p>Cosell—Technical Consultation: Connect with an Amazon Web Services Solutions Architect to address the partner's questions about the proposed solution.</p> </li> <li> <p>Cosell—Total Cost of Ownership Evaluation: Assistance with quoting different cost savings of proposed solutions on Amazon Web Services versus on-premises or a traditional hosting environment.</p> </li> <li> <p>Cosell—Deal Support: Request Amazon Web Services seller's support to progress the opportunity (for example: joint customer call, strategic positioning).</p> </li> <li> <p>Cosell—Support for Public Tender/RFx: Opportunity related to the public sector where the partner needs Amazon Web Services RFx support.</p> </li> </ul>
            national_security: <p>Indicates whether the <code>Opportunity</code> pertains to a national security project. This field must be set to <code>true</code> only when the customer's industry is <i>Government</i>. Additional privacy and security measures apply during the review and management process for opportunities marked as <code>NationalSecurity</code>.</p>
            partner_opportunity_identifier: <p>Specifies the opportunity's unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload to the partner.</p> <p>This field allows partners to link an opportunity to their CRM, which helps to ensure seamless integration and accurate synchronization between the Partner Central API and the partner's internal systems.</p>
            customer: <p>Specifies customer details associated with the <code>Opportunity</code>.</p>
            project: <p>An object that contains project details for the <code>Opportunity</code>.</p>
            opportunity_type: <p>Specifies the opportunity type as a renewal, new, or expansion.</p> <p>Opportunity types:</p> <ul> <li> <p>New opportunity: Represents a new business opportunity with a potential customer that's not previously engaged with your solutions or services.</p> </li> <li> <p>Renewal opportunity: Represents an opportunity to renew an existing contract or subscription with a current customer, ensuring continuity of service.</p> </li> <li> <p>Expansion opportunity: Represents an opportunity to expand the scope of an existing contract or subscription, either by adding new services or increasing the volume of existing services for a current customer.</p> </li> </ul>
            marketing: <p>This object contains marketing details and is optional for an opportunity.</p>
            software_revenue: <p>Specifies details of a customer's procurement terms. This is required only for partners in eligible programs.</p>
            client_token: <p>Required to be unique, and should be unchanging, it can be randomly generated or a meaningful string.</p> <p>Default: None</p> <p>Best practice: To help ensure uniqueness and avoid conflicts, use a Universally Unique Identifier (UUID) as the <code>ClientToken</code>. You can use standard libraries from most programming languages to generate this. If you use the same client token, the API returns the following error: "Conflicting client token submitted for a new request body."</p>
            life_cycle: <p>An object that contains lifecycle details for the <code>Opportunity</code>.</p>
            origin: <p>Specifies the origin of the opportunity, indicating if it was sourced from Amazon Web Services or the partner. For all opportunities created with <code>Catalog: AWS</code>, this field must only be <code>Partner Referral</code>. However, when using <code>Catalog: Sandbox</code>, you can set this field to <code>AWS Referral</code> to simulate Amazon Web Services referral creation. This allows Amazon Web Services-originated flows testing in the sandbox catalog.</p>
            opportunity_team: <p>Represents the internal team handling the opportunity. Specify collaborating members of this opportunity who are within the partner's organization.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.create_opportunity_request.CreateOpportunityRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.create_opportunity_response.CreateOpportunityResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_opportunity

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.create_opportunity.async_create_opportunity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_opportunity_request.CreateOpportunityRequest = {
            "catalog": catalog,
            "client_token": client_token,
        }
        if primary_needs_from_aws is not None:
            input_["primary_needs_from_aws"] = primary_needs_from_aws
        if national_security is not None:
            input_["national_security"] = national_security
        if partner_opportunity_identifier is not None:
            input_["partner_opportunity_identifier"] = partner_opportunity_identifier
        if customer is not None:
            input_["customer"] = customer
        if project is not None:
            input_["project"] = project
        if opportunity_type is not None:
            input_["opportunity_type"] = opportunity_type
        if marketing is not None:
            input_["marketing"] = marketing
        if software_revenue is not None:
            input_["software_revenue"] = software_revenue
        if life_cycle is not None:
            input_["life_cycle"] = life_cycle
        if origin is not None:
            input_["origin"] = origin
        if opportunity_team is not None:
            input_["opportunity_team"] = opportunity_team
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
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_opportunity_response.GetOpportunityResponse":
        """<p>Fetches the <code>Opportunity</code> record from Partner Central by a given <code>Identifier</code>.</p> <p>Use the <code>ListOpportunities</code> action or the event notification (from Amazon EventBridge) to obtain this identifier.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity is fetched from. Use <code>AWS</code> to retrieve opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> to retrieve opportunities in a secure, isolated testing environment.</p>
            identifier: <p>Read-only, system generated <code>Opportunity</code> unique identifier.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.get_opportunity_request.GetOpportunityRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.get_opportunity_response.GetOpportunityResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_opportunity

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.get_opportunity.async_get_opportunity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_opportunity_request.GetOpportunityRequest = {
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

    async def update(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        last_modified_date: "capo_partnercentral_selling.types.date_time.DateTime",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        primary_needs_from_aws: Optional[
            "capo_partnercentral_selling.types.primary_needs_from_aws.PrimaryNeedsFromAws"
        ] = None,
        national_security: Optional[
            "capo_partnercentral_selling.types.national_security.NationalSecurity"
        ] = None,
        partner_opportunity_identifier: Optional[str] = None,
        customer: Optional[
            "capo_partnercentral_selling.types.customer.Customer"
        ] = None,
        project: Optional["capo_partnercentral_selling.types.project.Project"] = None,
        opportunity_type: Optional[
            "capo_partnercentral_selling.types.opportunity_type.OpportunityType"
        ] = None,
        marketing: Optional[
            "capo_partnercentral_selling.types.marketing.Marketing"
        ] = None,
        software_revenue: Optional[
            "capo_partnercentral_selling.types.software_revenue.SoftwareRevenue"
        ] = None,
        life_cycle: Optional[
            "capo_partnercentral_selling.types.life_cycle.LifeCycle"
        ] = None,
    ) -> "capo_partnercentral_selling.types.update_opportunity_response.UpdateOpportunityResponse":
        """<p>Updates the <code>Opportunity</code> record identified by a given <code>Identifier</code>. This operation allows you to modify the details of an existing opportunity to reflect the latest information and progress. Use this action to keep the opportunity record up-to-date and accurate.</p> <p>When you perform updates, include the entire payload with each request. If any field is omitted, the API assumes that the field is set to <code>null</code>. The best practice is to always perform a <code>GetOpportunity</code> to retrieve the latest values, then send the complete payload with the updated values to be changed.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity is updated in. Use <code>AWS</code> to update real opportunities in the production environment, and <code>Sandbox</code> for testing in secure, isolated environments. When you use the <code>Sandbox</code> catalog, it allows you to simulate and validate your interactions with Amazon Web Services services without affecting live data or operations.</p>
            primary_needs_from_aws: <p>Identifies the type of support the partner needs from Amazon Web Services.</p> <p>Valid values:</p> <ul> <li> <p>Cosell—Architectural Validation: Confirmation from Amazon Web Services that the partner's proposed solution architecture is aligned with Amazon Web Services best practices and poses minimal architectural risks.</p> </li> <li> <p>Cosell—Business Presentation: Request Amazon Web Services seller's participation in a joint customer presentation.</p> </li> <li> <p>Cosell—Competitive Information: Access to Amazon Web Services competitive resources and support for the partner's proposed solution.</p> </li> <li> <p>Cosell—Pricing Assistance: Connect with an AWS seller for support situations where a partner may be receiving an upfront discount on a service (for example: EDP deals).</p> </li> <li> <p>Cosell—Technical Consultation: Connection with an Amazon Web Services Solutions Architect to address the partner's questions about the proposed solution.</p> </li> <li> <p>Cosell—Total Cost of Ownership Evaluation: Assistance with quoting different cost savings of proposed solutions on Amazon Web Services versus on-premises or a traditional hosting environment.</p> </li> <li> <p>Cosell—Deal Support: Request Amazon Web Services seller's support to progress the opportunity (for example: joint customer call, strategic positioning).</p> </li> <li> <p>Cosell—Support for Public Tender/RFx: Opportunity related to the public sector where the partner needs RFx support from Amazon Web Services.</p> </li> </ul>
            national_security: <p>Specifies if the opportunity is associated with national security concerns. This flag is only applicable when the industry is <code>Government</code>. For national-security-related opportunities, validation and compliance rules may apply, impacting the opportunity's visibility and processing.</p>
            partner_opportunity_identifier: <p>Specifies the opportunity's unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload sent back to the partner.</p>
            customer: <p>Specifies details of the customer associated with the <code>Opportunity</code>.</p>
            project: <p>An object that contains project details summary for the <code>Opportunity</code>.</p>
            opportunity_type: <p>Specifies the opportunity type as a renewal, new, or expansion.</p> <p>Opportunity types:</p> <ul> <li> <p>New opportunity: Represents a new business opportunity with a potential customer that's not previously engaged with your solutions or services.</p> </li> <li> <p>Renewal opportunity: Represents an opportunity to renew an existing contract or subscription with a current customer, ensuring continuity of service.</p> </li> <li> <p>Expansion opportunity: Represents an opportunity to expand the scope of an existing contract or subscription, either by adding new services or increasing the volume of existing services for a current customer.</p> </li> </ul>
            marketing: <p>An object that contains marketing details for the <code>Opportunity</code>.</p>
            software_revenue: <p>Specifies details of a customer's procurement terms. Required only for partners in eligible programs.</p>
            last_modified_date: <p> <code>DateTime</code> when the opportunity was last modified.</p>
            identifier: <p>Read-only, system generated <code>Opportunity</code> unique identifier.</p>
            life_cycle: <p>An object that contains lifecycle details for the <code>Opportunity</code>.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.update_opportunity_request.UpdateOpportunityRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.update_opportunity_response.UpdateOpportunityResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.update_opportunity

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.update_opportunity.async_update_opportunity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.update_opportunity_request.UpdateOpportunityRequest = {
            "catalog": catalog,
            "last_modified_date": last_modified_date,
            "identifier": identifier,
        }
        if primary_needs_from_aws is not None:
            input_["primary_needs_from_aws"] = primary_needs_from_aws
        if national_security is not None:
            input_["national_security"] = national_security
        if partner_opportunity_identifier is not None:
            input_["partner_opportunity_identifier"] = partner_opportunity_identifier
        if customer is not None:
            input_["customer"] = customer
        if project is not None:
            input_["project"] = project
        if opportunity_type is not None:
            input_["opportunity_type"] = opportunity_type
        if marketing is not None:
            input_["marketing"] = marketing
        if software_revenue is not None:
            input_["software_revenue"] = software_revenue
        if life_cycle is not None:
            input_["life_cycle"] = life_cycle

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
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.opportunity_sort.OpportunitySort"
        ] = None,
        last_modified_date: Optional[
            "capo_partnercentral_selling.types.last_modified_date.LastModifiedDate"
        ] = None,
        identifier: Optional[
            "capo_partnercentral_selling.types.filter_identifier.FilterIdentifier"
        ] = None,
        life_cycle_stage: Optional[
            "capo_partnercentral_selling.types.filter_life_cycle_stage.FilterLifeCycleStage"
        ] = None,
        life_cycle_review_status: Optional[
            "capo_partnercentral_selling.types.filter_life_cycle_review_status.FilterLifeCycleReviewStatus"
        ] = None,
        customer_company_name: Optional[
            "capo_partnercentral_selling.types.string_list.StringList"
        ] = None,
        created_date: Optional[
            "capo_partnercentral_selling.types.created_date_filter.CreatedDateFilter"
        ] = None,
        target_close_date: Optional[
            "capo_partnercentral_selling.types.target_close_date_filter.TargetCloseDateFilter"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_opportunities_response.ListOpportunitiesResponse":
        """<p>This request accepts a list of filters that retrieve opportunity subsets as well as sort options. This feature is available to partners from <a href="https://partnercentral.awspartner.com/">Partner Central</a> using the <code>ListOpportunities</code> API action.</p> <p>To synchronize your system with Amazon Web Services, list only the opportunities that were newly created or updated. We recommend you rely on events emitted by the service into your Amazon Web Services account’s Amazon EventBridge default event bus. You can also use the <code>ListOpportunities</code> action.</p> <p>We recommend the following approach:</p> <ol> <li> <p>Find the latest <code>LastModifiedDate</code> that you stored, and only use the values that came from Amazon Web Services. Don’t use values generated by your system.</p> </li> <li> <p>When you send a <code>ListOpportunities</code> request, submit the date in ISO 8601 format in the <code>AfterLastModifiedDate</code> filter.</p> </li> <li> <p>Amazon Web Services only returns opportunities created or updated on or after that date and time. Use <code>NextToken</code> to iterate over all pages.</p> </li> </ol>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunities are listed in. Use <code>AWS</code> for listing real opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            max_results: <p>Specifies the maximum number of results to return in a single call. This limits the number of opportunities returned in the response to avoid providing too many results at once.</p> <p>Default: 20</p>
            next_token: <p>A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.</p>
            sort: <p>An object that specifies how the response is sorted. The default <code>Sort.SortBy</code> value is <code>LastModifiedDate</code>.</p>
            last_modified_date: <p>Filters the opportunities based on their last modified date. This filter helps retrieve opportunities that were updated after the specified date, allowing partners to track recent changes or updates.</p>
            identifier: <p>Filters the opportunities based on the opportunity identifier. This allows partners to retrieve specific opportunities by providing their unique identifiers, ensuring precise results.</p>
            life_cycle_stage: <p>Filters the opportunities based on their lifecycle stage. This filter allows partners to retrieve opportunities at various stages in the sales cycle, such as <code>Qualified</code>, <code>Technical Validation</code>, <code>Business Validation</code>, or <code>Closed Won</code>.</p>
            life_cycle_review_status: <p>Filters the opportunities based on their current lifecycle approval status. Use this filter to retrieve opportunities with statuses such as <code>Pending Submission</code>, <code>In Review</code>, <code>Action Required</code>, or <code>Approved</code>.</p>
            customer_company_name: <p>Filters the opportunities based on the customer's company name. This allows partners to search for opportunities associated with a specific customer by matching the provided company name string.</p>
            created_date: <p>Filter opportunities by creation date criteria.</p>
            target_close_date: <p>Filters opportunities based on their target close date. This filter helps retrieve opportunities with an expected close date before or after a specified date.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_opportunities_request.ListOpportunitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_opportunities_response.ListOpportunitiesResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_opportunities

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_opportunities.async_list_opportunities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_opportunities_request.ListOpportunitiesRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        if last_modified_date is not None:
            input_["last_modified_date"] = last_modified_date
        if identifier is not None:
            input_["identifier"] = identifier
        if life_cycle_stage is not None:
            input_["life_cycle_stage"] = life_cycle_stage
        if life_cycle_review_status is not None:
            input_["life_cycle_review_status"] = life_cycle_review_status
        if customer_company_name is not None:
            input_["customer_company_name"] = customer_company_name
        if created_date is not None:
            input_["created_date"] = created_date
        if target_close_date is not None:
            input_["target_close_date"] = target_close_date

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def assign_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        assignee: "capo_partnercentral_selling.types.assignee_contact.AssigneeContact",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Enables you to reassign an existing <code>Opportunity</code> to another user within your Partner Central account. The specified user receives the opportunity, and it appears on their Partner Central dashboard, allowing them to take necessary actions or proceed with the opportunity.</p> <p>This is useful for distributing opportunities to the appropriate team members or departments within your organization, ensuring that each opportunity is handled by the right person. By default, the opportunity owner is the one who creates it. Currently, there's no API to enumerate the list of available users.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity is assigned in. Use <code>AWS</code> to assign real opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            identifier: <p>Requires the <code>Opportunity</code>'s unique identifier when you want to assign it to another user. Provide the correct identifier so the intended opportunity is reassigned.</p>
            assignee: <p>Specifies the user or team member responsible for managing the assigned opportunity. This field identifies the <i>Assignee</i> based on the partner's internal team structure. Ensure that the email address is associated with a registered user in your Partner Central account.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.assign_opportunity_request.AssignOpportunityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.assign_opportunity

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.assign_opportunity.async_assign_opportunity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.assign_opportunity_request.AssignOpportunityRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "assignee": assignee,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        opportunity_identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        related_entity_type: "capo_partnercentral_selling.types.related_entity_type.RelatedEntityType",
        related_entity_identifier: str,
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Enables you to create a formal association between an <code>Opportunity</code> and various related entities, enriching the context and details of the opportunity for better collaboration and decision making. You can associate an opportunity with the following entity types:</p> <ul> <li> <p>Partner Solution: A software product or consulting practice created and delivered by Partners. Partner Solutions help customers address business challenges using Amazon Web Services services.</p> </li> <li> <p>Amazon Web Services Products: Amazon Web Services offers many products and services that provide scalable, reliable, and cost-effective infrastructure solutions. For the latest list of Amazon Web Services products, see <a href="https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json">Amazon Web Services products</a>.</p> </li> <li> <p>Amazon Web Services Marketplace private offer: Allows Amazon Web Services Marketplace sellers to extend custom pricing and terms to individual Amazon Web Services customers. Sellers can negotiate custom prices, payment schedules, and end user license terms through private offers, enabling Amazon Web Services customers to acquire software solutions tailored to their specific needs. For more information, see <a href="https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-private-offers.html">Private offers in Amazon Web Services Marketplace</a>.</p> </li> </ul> <p>To obtain identifiers for these entities, use the following methods:</p> <ul> <li> <p>Solution: Use the <code>ListSolutions</code> operation.</p> </li> <li> <p>AWS Products: For the latest list of Amazon Web Services products, see <a href="https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json">Amazon Web Services products</a>.</p> </li> <li> <p>Amazon Web Services Marketplace private offer: Use the <a href="https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html">Using the Amazon Web Services Marketplace Catalog API</a> to list entities. Specifically, use the <code>ListEntities</code> operation to retrieve a list of private offers. The request returns the details of available private offers. For more information, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_ListEntities.html">ListEntities</a>.</p> </li> </ul>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity association is made in. Use <code>AWS</code> to associate opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            opportunity_identifier: <p>Requires the <code>Opportunity</code>'s unique identifier when you want to associate it with a related entity. Provide the correct identifier so the intended opportunity is updated with the association.</p>
            related_entity_type: <p>Specifies the entity type that you're associating with the <code> Opportunity</code>. This helps to categorize and properly process the association.</p>
            related_entity_identifier: <p>Requires the related entity's unique identifier when you want to associate it with the <code> Opportunity</code>. For Amazon Web Services Marketplace entities, provide the Amazon Resource Name (ARN). Use the <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html"> Amazon Web Services Marketplace API</a> to obtain the ARN.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.associate_opportunity_request.AssociateOpportunityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.associate_opportunity

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.associate_opportunity.async_associate_opportunity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.associate_opportunity_request.AssociateOpportunityRequest = {
            "catalog": catalog,
            "opportunity_identifier": opportunity_identifier,
            "related_entity_type": related_entity_type,
            "related_entity_identifier": related_entity_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        opportunity_identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        related_entity_type: "capo_partnercentral_selling.types.related_entity_type.RelatedEntityType",
        related_entity_identifier: str,
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Allows you to remove an existing association between an <code>Opportunity</code> and related entities, such as a Partner Solution, Amazon Web Services product, or an Amazon Web Services Marketplace offer. This operation is the counterpart to <code>AssociateOpportunity</code>, and it provides flexibility to manage associations as business needs change.</p> <p>Use this operation to update the associations of an <code>Opportunity</code> due to changes in the related entities, or if an association was made in error. Ensuring accurate associations helps maintain clarity and accuracy to track and manage business opportunities. When you replace an entity, first attach the new entity and then disassociate the one to be removed, especially if it's the last remaining entity that's required.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity disassociation is made in. Use <code>AWS</code> to disassociate opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            opportunity_identifier: <p>The opportunity's unique identifier for when you want to disassociate it from related entities. This identifier helps to ensure that the correct opportunity is updated.</p> <p>Validation: Ensure that the provided identifier corresponds to an existing opportunity in the Amazon Web Services system because incorrect identifiers result in an error and no changes are made.</p>
            related_entity_type: <p>The type of the entity that you're disassociating from the opportunity. When you specify the entity type, it helps the system correctly process the disassociation request to ensure that the right connections are removed.</p> <p>Examples of entity types include Partner Solution, Amazon Web Services product, and Amazon Web Services Marketplaceoffer. Ensure that the value matches one of the expected entity types.</p> <p>Validation: Provide a valid entity type to help ensure successful disassociation. An invalid or incorrect entity type results in an error.</p>
            related_entity_identifier: <p>The related entity's identifier that you want to disassociate from the opportunity. Depending on the type of entity, this could be a simple identifier or an Amazon Resource Name (ARN) for entities managed through Amazon Web Services Marketplace.</p> <p>For Amazon Web Services Marketplace entities, use the Amazon Web Services Marketplace API to obtain the necessary ARNs. For guidance on retrieving these ARNs, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html"> Amazon Web Services MarketplaceUsing the Amazon Web Services Marketplace Catalog API</a>.</p> <p>Validation: Ensure the identifier or ARN is valid and corresponds to an existing entity. An incorrect or invalid identifier results in an error.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.disassociate_opportunity_request.DisassociateOpportunityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.disassociate_opportunity

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.disassociate_opportunity.async_disassociate_opportunity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.disassociate_opportunity_request.DisassociateOpportunityRequest = {
            "catalog": catalog,
            "opportunity_identifier": opportunity_identifier,
            "related_entity_type": related_entity_type,
            "related_entity_identifier": related_entity_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_aws_opportunity_summary(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        related_opportunity_identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_aws_opportunity_summary_response.GetAwsOpportunitySummaryResponse":
        """<p>Retrieves a summary of an AWS Opportunity. This summary includes high-level details about the opportunity sourced from AWS, such as lifecycle information, customer details, and involvement type. It is useful for tracking updates on the AWS opportunity corresponding to an opportunity in the partner's account.</p>

        Args:
            catalog: <p>Specifies the catalog in which the AWS Opportunity is located. Accepted values include <code>AWS</code> for production opportunities or <code>Sandbox</code> for testing purposes. The catalog determines which environment the opportunity data is pulled from.</p>
            related_opportunity_identifier: <p>The unique identifier for the related partner opportunity. Use this field to correlate an AWS opportunity with its corresponding partner opportunity.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.get_aws_opportunity_summary_request.GetAwsOpportunitySummaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.get_aws_opportunity_summary_response.GetAwsOpportunitySummaryResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_aws_opportunity_summary

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.get_aws_opportunity_summary.async_get_aws_opportunity_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_aws_opportunity_summary_request.GetAwsOpportunitySummaryRequest = {
            "catalog": catalog,
            "related_opportunity_identifier": related_opportunity_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def submit_opportunity(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        involvement_type: "capo_partnercentral_selling.types.sales_involvement_type.SalesInvolvementType",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        visibility: Optional[
            "capo_partnercentral_selling.types.visibility.Visibility"
        ] = None,
    ) -> None:
        """<p>Use this action to submit an Opportunity that was previously created by partner for AWS review. After you perform this action, the Opportunity becomes non-editable until it is reviewed by AWS and has <code> LifeCycle.ReviewStatus </code> as either <code>Approved</code> or <code>Action Required</code>. </p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Submits the opportunity request from the production AWS environment.</p> </li> <li> <p>Sandbox: Submits the opportunity request from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            identifier: <p>The identifier of the Opportunity previously created by partner and needs to be submitted.</p>
            involvement_type: <p>Specifies the level of AWS sellers' involvement on the opportunity. Valid values:</p> <ul> <li> <p> <code>Co-sell</code>: Indicates the user wants to co-sell with AWS. Share the opportunity with AWS to receive deal assistance and support.</p> </li> <li> <p> <code>For Visibility Only</code>: Indicates that the user does not need support from AWS Sales Rep. Share this opportunity with AWS for visibility only, you will not receive deal assistance and support.</p> </li> </ul>
            visibility: <p>Determines whether to restrict visibility of the opportunity from AWS sales. Default value is Full. Valid values:</p> <ul> <li> <p> <code>Full</code>: The opportunity is fully visible to AWS sales.</p> </li> <li> <p> <code>Limited</code>: The opportunity has restricted visibility to AWS sales.</p> </li> </ul>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.submit_opportunity_request.SubmitOpportunityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.submit_opportunity

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.submit_opportunity.async_submit_opportunity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.submit_opportunity_request.SubmitOpportunityRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "involvement_type": involvement_type,
        }
        if visibility is not None:
            input_["visibility"] = visibility

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
