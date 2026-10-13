from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_route53globalresolver._auth._signers
import capo_route53globalresolver._auth._sigv4
from capo_route53globalresolver._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.create_firewall_domain_list_input
    import capo_route53globalresolver.types.create_firewall_domain_list_output
    import capo_route53globalresolver.types.delete_firewall_domain_list_input
    import capo_route53globalresolver.types.delete_firewall_domain_list_output
    import capo_route53globalresolver.types.domain
    import capo_route53globalresolver.types.domains
    import capo_route53globalresolver.types.firewall_domain_lists_item
    import capo_route53globalresolver.types.get_firewall_domain_list_input
    import capo_route53globalresolver.types.get_firewall_domain_list_output
    import capo_route53globalresolver.types.import_firewall_domains_input
    import capo_route53globalresolver.types.import_firewall_domains_output
    import capo_route53globalresolver.types.list_firewall_domain_lists_input
    import capo_route53globalresolver.types.list_firewall_domain_lists_output
    import capo_route53globalresolver.types.list_firewall_domains_input
    import capo_route53globalresolver.types.list_firewall_domains_output
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name
    import capo_route53globalresolver.types.tags
    import capo_route53globalresolver.types.update_firewall_domains_input
    import capo_route53globalresolver.types.update_firewall_domains_output
    from capo_route53globalresolver._services.async_route53_global_resolver import (
        AsyncRoute53GlobalResolverClient,
        AsyncRoute53GlobalResolverClientConfig,
    )
    from capo_route53globalresolver._services.route53_global_resolver import (
        Route53GlobalResolverClient,
        Route53GlobalResolverClientConfig,
    )


class FirewallDomainList:
    def __init__(self, service: Route53GlobalResolverClient) -> None:
        self._service = service

    def create(
        self,
        global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        name: "capo_route53globalresolver.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_route53globalresolver.types.tags.Tags"] = None,
    ) -> "capo_route53globalresolver.types.create_firewall_domain_list_output.CreateFirewallDomainListOutput":
        """<p>Creates a firewall domain list. Domain lists are reusable sets of domain specifications that you use in DNS firewall rules to allow, block, or alert on DNS queries to specific domains.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            global_resolver_id: <p>The ID of the Route 53 Global Resolver that the domain list will be associated with.</p>
            description: <p>An optional description for the firewall domain list.</p>
            name: <p>A descriptive name for the firewall domain list.</p>
            tags: <p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.create_firewall_domain_list_input.CreateFirewallDomainListInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.create_firewall_domain_list_output.CreateFirewallDomainListOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_domain_list

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_domain_list.create_firewall_domain_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateFirewallDomainList")
        )
        input_: capo_route53globalresolver.types.create_firewall_domain_list_input.CreateFirewallDomainListInput = {
            "global_resolver_id": global_resolver_id,
            "name": name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
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
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_firewall_domain_list_output.GetFirewallDomainListOutput":
        """<p>Retrieves information about a firewall domain list.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_domain_list_id: <p>ID of the domain list.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.get_firewall_domain_list_input.GetFirewallDomainListInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.get_firewall_domain_list_output.GetFirewallDomainListOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_domain_list

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_domain_list.get_firewall_domain_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFirewallDomainList")
        )
        input_: capo_route53globalresolver.types.get_firewall_domain_list_input.GetFirewallDomainListInput = {
            "firewall_domain_list_id": firewall_domain_list_id
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
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_firewall_domain_list_output.DeleteFirewallDomainListOutput":
        """<p>Deletes a firewall domain list. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_domain_list_id: <p>The unique identifier of the firewall domain list to delete.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.delete_firewall_domain_list_input.DeleteFirewallDomainListInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.delete_firewall_domain_list_output.DeleteFirewallDomainListOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_domain_list

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_domain_list.delete_firewall_domain_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteFirewallDomainList")
        )
        input_: capo_route53globalresolver.types.delete_firewall_domain_list_input.DeleteFirewallDomainListInput = {
            "firewall_domain_list_id": firewall_domain_list_id
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
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        global_resolver_id: Optional[
            "capo_route53globalresolver.types.resource_id.ResourceId"
        ] = None,
    ) -> "capo_route53globalresolver.types.list_firewall_domain_lists_output.ListFirewallDomainListsOutput":
        """<p>Lists all firewall domain lists for a Route 53 Global Resolver with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            global_resolver_id: <p>The ID of the Global Resolver that contains the DNS view the domain lists are associated to.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.list_firewall_domain_lists_input.ListFirewallDomainListsInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.list_firewall_domain_lists_output.ListFirewallDomainListsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domain_lists

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domain_lists.list_firewall_domain_lists(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFirewallDomainLists")
        )
        input_: capo_route53globalresolver.types.list_firewall_domain_lists_input.ListFirewallDomainListsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if global_resolver_id is not None:
            input_["global_resolver_id"] = global_resolver_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_firewall_domains(
        self,
        domain_file_url: str,
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        operation: str,
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.import_firewall_domains_output.ImportFirewallDomainsOutput":
        """<p>Imports a list of domains from an Amazon S3 file into a firewall domain list. The file should contain one domain per line.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            domain_file_url: <p>The fully qualified URL of the file in Amazon S3 that contains the list of domains to import. The file should contain one domain per line.</p>
            firewall_domain_list_id: <p>ID of the DNS Firewall domain list that you want to import the domain list to.</p>
            operation: <p>This value is <code>REPLACE</code>, and it updates the domain list to match the list of domains in the imported file.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.import_firewall_domains_input.ImportFirewallDomainsInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.import_firewall_domains_output.ImportFirewallDomainsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.import_firewall_domains

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.import_firewall_domains.import_firewall_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ImportFirewallDomains")
        )
        input_: capo_route53globalresolver.types.import_firewall_domains_input.ImportFirewallDomainsInput = {
            "domain_file_url": domain_file_url,
            "firewall_domain_list_id": firewall_domain_list_id,
            "operation": operation,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_firewall_domains(
        self,
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_route53globalresolver.types.list_firewall_domains_output.ListFirewallDomainsOutput":
        """<p>Lists all the domains in DNS Firewall domain list you have created.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            firewall_domain_list_id: <p>ID of the DNS Firewall domain list.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.list_firewall_domains_input.ListFirewallDomainsInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.list_firewall_domains_output.ListFirewallDomainsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domains

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domains.list_firewall_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFirewallDomains")
        )
        input_: capo_route53globalresolver.types.list_firewall_domains_input.ListFirewallDomainsInput = {
            "firewall_domain_list_id": firewall_domain_list_id
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

    def update_firewall_domains(
        self,
        domains: "capo_route53globalresolver.types.domains.Domains",
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        operation: str,
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.update_firewall_domains_output.UpdateFirewallDomainsOutput":
        """<p>Updates a DNS Firewall domain list from an array of specified domains.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            domains: <p>A list of the domains. You can add up to 1000 domains per request.</p>
            firewall_domain_list_id: <p>The ID of the DNS Firewall domain list to which you want to add the domains.</p>
            operation: <p>The operation for updating the domain list. The allowed values are ADD, REMOVE, and REPLACE.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.update_firewall_domains_input.UpdateFirewallDomainsInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.update_firewall_domains_output.UpdateFirewallDomainsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_domains

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_domains.update_firewall_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateFirewallDomains")
        )
        input_: capo_route53globalresolver.types.update_firewall_domains_input.UpdateFirewallDomainsInput = {
            "domains": domains,
            "firewall_domain_list_id": firewall_domain_list_id,
            "operation": operation,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncFirewallDomainList:
    def __init__(self, service: AsyncRoute53GlobalResolverClient) -> None:
        self._service = service

    async def create(
        self,
        global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        name: "capo_route53globalresolver.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_route53globalresolver.types.tags.Tags"] = None,
    ) -> "capo_route53globalresolver.types.create_firewall_domain_list_output.CreateFirewallDomainListOutput":
        """<p>Creates a firewall domain list. Domain lists are reusable sets of domain specifications that you use in DNS firewall rules to allow, block, or alert on DNS queries to specific domains.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            global_resolver_id: <p>The ID of the Route 53 Global Resolver that the domain list will be associated with.</p>
            description: <p>An optional description for the firewall domain list.</p>
            name: <p>A descriptive name for the firewall domain list.</p>
            tags: <p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.create_firewall_domain_list_input.CreateFirewallDomainListInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.create_firewall_domain_list_output.CreateFirewallDomainListOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_domain_list

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_domain_list.async_create_firewall_domain_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateFirewallDomainList")
        )
        input_: capo_route53globalresolver.types.create_firewall_domain_list_input.CreateFirewallDomainListInput = {
            "global_resolver_id": global_resolver_id,
            "name": name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
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
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_firewall_domain_list_output.GetFirewallDomainListOutput":
        """<p>Retrieves information about a firewall domain list.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_domain_list_id: <p>ID of the domain list.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.get_firewall_domain_list_input.GetFirewallDomainListInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.get_firewall_domain_list_output.GetFirewallDomainListOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_domain_list

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_domain_list.async_get_firewall_domain_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFirewallDomainList")
        )
        input_: capo_route53globalresolver.types.get_firewall_domain_list_input.GetFirewallDomainListInput = {
            "firewall_domain_list_id": firewall_domain_list_id
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
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_firewall_domain_list_output.DeleteFirewallDomainListOutput":
        """<p>Deletes a firewall domain list. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_domain_list_id: <p>The unique identifier of the firewall domain list to delete.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.delete_firewall_domain_list_input.DeleteFirewallDomainListInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.delete_firewall_domain_list_output.DeleteFirewallDomainListOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_domain_list

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_domain_list.async_delete_firewall_domain_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteFirewallDomainList")
        )
        input_: capo_route53globalresolver.types.delete_firewall_domain_list_input.DeleteFirewallDomainListInput = {
            "firewall_domain_list_id": firewall_domain_list_id
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
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        global_resolver_id: Optional[
            "capo_route53globalresolver.types.resource_id.ResourceId"
        ] = None,
    ) -> "capo_route53globalresolver.types.list_firewall_domain_lists_output.ListFirewallDomainListsOutput":
        """<p>Lists all firewall domain lists for a Route 53 Global Resolver with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            global_resolver_id: <p>The ID of the Global Resolver that contains the DNS view the domain lists are associated to.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_firewall_domain_lists_input.ListFirewallDomainListsInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_firewall_domain_lists_output.ListFirewallDomainListsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domain_lists

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domain_lists.async_list_firewall_domain_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFirewallDomainLists")
        )
        input_: capo_route53globalresolver.types.list_firewall_domain_lists_input.ListFirewallDomainListsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if global_resolver_id is not None:
            input_["global_resolver_id"] = global_resolver_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_firewall_domains(
        self,
        domain_file_url: str,
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        operation: str,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.import_firewall_domains_output.ImportFirewallDomainsOutput":
        """<p>Imports a list of domains from an Amazon S3 file into a firewall domain list. The file should contain one domain per line.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            domain_file_url: <p>The fully qualified URL of the file in Amazon S3 that contains the list of domains to import. The file should contain one domain per line.</p>
            firewall_domain_list_id: <p>ID of the DNS Firewall domain list that you want to import the domain list to.</p>
            operation: <p>This value is <code>REPLACE</code>, and it updates the domain list to match the list of domains in the imported file.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.import_firewall_domains_input.ImportFirewallDomainsInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.import_firewall_domains_output.ImportFirewallDomainsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.import_firewall_domains

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.import_firewall_domains.async_import_firewall_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ImportFirewallDomains")
        )
        input_: capo_route53globalresolver.types.import_firewall_domains_input.ImportFirewallDomainsInput = {
            "domain_file_url": domain_file_url,
            "firewall_domain_list_id": firewall_domain_list_id,
            "operation": operation,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_firewall_domains(
        self,
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_route53globalresolver.types.list_firewall_domains_output.ListFirewallDomainsOutput":
        """<p>Lists all the domains in DNS Firewall domain list you have created.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            firewall_domain_list_id: <p>ID of the DNS Firewall domain list.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_firewall_domains_input.ListFirewallDomainsInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_firewall_domains_output.ListFirewallDomainsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domains

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domains.async_list_firewall_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFirewallDomains")
        )
        input_: capo_route53globalresolver.types.list_firewall_domains_input.ListFirewallDomainsInput = {
            "firewall_domain_list_id": firewall_domain_list_id
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

    async def update_firewall_domains(
        self,
        domains: "capo_route53globalresolver.types.domains.Domains",
        firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        operation: str,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.update_firewall_domains_output.UpdateFirewallDomainsOutput":
        """<p>Updates a DNS Firewall domain list from an array of specified domains.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            domains: <p>A list of the domains. You can add up to 1000 domains per request.</p>
            firewall_domain_list_id: <p>The ID of the DNS Firewall domain list to which you want to add the domains.</p>
            operation: <p>The operation for updating the domain list. The allowed values are ADD, REMOVE, and REPLACE.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.update_firewall_domains_input.UpdateFirewallDomainsInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.update_firewall_domains_output.UpdateFirewallDomainsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_domains

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_domains.async_update_firewall_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateFirewallDomains")
        )
        input_: capo_route53globalresolver.types.update_firewall_domains_input.UpdateFirewallDomainsInput = {
            "domains": domains,
            "firewall_domain_list_id": firewall_domain_list_id,
            "operation": operation,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
