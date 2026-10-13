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
    import capo_route53globalresolver.types.access_sources_item
    import capo_route53globalresolver.types.cidr
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.create_access_source_input
    import capo_route53globalresolver.types.create_access_source_output
    import capo_route53globalresolver.types.delete_access_source_input
    import capo_route53globalresolver.types.delete_access_source_output
    import capo_route53globalresolver.types.dns_protocol
    import capo_route53globalresolver.types.filters
    import capo_route53globalresolver.types.get_access_source_input
    import capo_route53globalresolver.types.get_access_source_output
    import capo_route53globalresolver.types.ip_address_type
    import capo_route53globalresolver.types.list_access_sources_input
    import capo_route53globalresolver.types.list_access_sources_output
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name_short
    import capo_route53globalresolver.types.tags
    import capo_route53globalresolver.types.update_access_source_input
    import capo_route53globalresolver.types.update_access_source_output
    from capo_route53globalresolver._services.async_route53_global_resolver import (
        AsyncRoute53GlobalResolverClient,
        AsyncRoute53GlobalResolverClientConfig,
    )
    from capo_route53globalresolver._services.route53_global_resolver import (
        Route53GlobalResolverClient,
        Route53GlobalResolverClientConfig,
    )


class AccessSource:
    def __init__(self, service: Route53GlobalResolverClient) -> None:
        self._service = service

    def create(
        self,
        cidr: "capo_route53globalresolver.types.cidr.Cidr",
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        protocol: "capo_route53globalresolver.types.dns_protocol.DnsProtocol",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        ip_address_type: Optional[
            "capo_route53globalresolver.types.ip_address_type.IpAddressType"
        ] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
        ] = None,
        tags: Optional["capo_route53globalresolver.types.tags.Tags"] = None,
    ) -> "capo_route53globalresolver.types.create_access_source_output.CreateAccessSourceOutput":
        """<p>Creates an access source for a DNS view. Access sources define IP addresses or CIDR ranges that are allowed to send DNS queries to the Route 53 Global Resolver, along with the permitted DNS protocols.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            cidr: <p>The IP address or CIDR range that is allowed to send DNS queries to the Route 53 Global Resolver.</p>
            client_token: <p>A unique string that identifies the request and ensures idempotency.</p>
            ip_address_type: <p>The IP address type for this access source. Valid values are IPv4 and IPv6 (if the Route 53 Global Resolver supports dual-stack).</p>
            name: <p>A descriptive name for the access source.</p>
            dns_view_id: <p>The ID of the DNS view to associate with this access source.</p>
            protocol: <p>The DNS protocol that is permitted for this access source. Valid values are Do53 (DNS over port 53), DoT (DNS over TLS), and DoH (DNS over HTTPS).</p>
            tags: <p>Tags to associate with the access source.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateAccessSource example

            >>> client.create(cidr='85.90.183.3/30', client_token='9fas9-9usdfa-xbi8-kco', dns_view_id='dnsv-123456789', ip_address_type='IPV4', name='My Access Source', protocol='DO53', tags={'Key1': 'Value1'})
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.create_access_source_input.CreateAccessSourceInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.create_access_source_output.CreateAccessSourceOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_source

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_source.create_access_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateAccessSource")
        )
        input_: capo_route53globalresolver.types.create_access_source_input.CreateAccessSourceInput = {
            "cidr": cidr,
            "dns_view_id": dns_view_id,
            "protocol": protocol,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if name is not None:
            input_["name"] = name
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
        access_source_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_access_source_output.GetAccessSourceOutput":
        """<p>Retrieves information about an access source.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to retrieve.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.get_access_source_input.GetAccessSourceInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.get_access_source_output.GetAccessSourceOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_source

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_source.get_access_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAccessSource")
        )
        input_: capo_route53globalresolver.types.get_access_source_input.GetAccessSourceInput = {
            "access_source_id": access_source_id
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
        access_source_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        cidr: Optional["capo_route53globalresolver.types.cidr.Cidr"] = None,
        ip_address_type: Optional[
            "capo_route53globalresolver.types.ip_address_type.IpAddressType"
        ] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
        ] = None,
        protocol: Optional[
            "capo_route53globalresolver.types.dns_protocol.DnsProtocol"
        ] = None,
    ) -> "capo_route53globalresolver.types.update_access_source_output.UpdateAccessSourceOutput":
        """<p>Updates the configuration of an access source.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to update.</p>
            cidr: <p>The CIDR block for the access source.</p>
            ip_address_type: <p>The IP address type for the access source.</p>
            name: <p>The name of the access source.</p>
            protocol: <p>The protocol for the access source.</p>

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
            req: "OperationRequest[capo_route53globalresolver.types.update_access_source_input.UpdateAccessSourceInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.update_access_source_output.UpdateAccessSourceOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_source

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_source.update_access_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAccessSource")
        )
        input_: capo_route53globalresolver.types.update_access_source_input.UpdateAccessSourceInput = {
            "access_source_id": access_source_id
        }
        if cidr is not None:
            input_["cidr"] = cidr
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if name is not None:
            input_["name"] = name
        if protocol is not None:
            input_["protocol"] = protocol

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        access_source_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_access_source_output.DeleteAccessSourceOutput":
        """<p>Deletes an access source. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to delete.</p>

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
            req: "OperationRequest[capo_route53globalresolver.types.delete_access_source_input.DeleteAccessSourceInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.delete_access_source_output.DeleteAccessSourceOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_source

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_source.delete_access_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAccessSource")
        )
        input_: capo_route53globalresolver.types.delete_access_source_input.DeleteAccessSourceInput = {
            "access_source_id": access_source_id
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
        filters: Optional["capo_route53globalresolver.types.filters.Filters"] = None,
    ) -> "capo_route53globalresolver.types.list_access_sources_output.ListAccessSourcesOutput":
        """<p>Lists all access sources with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            filters: <p>Values to filter the results.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.list_access_sources_input.ListAccessSourcesInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.list_access_sources_output.ListAccessSourcesOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_sources

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_sources.list_access_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAccessSources")
        )
        input_: capo_route53globalresolver.types.list_access_sources_input.ListAccessSourcesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAccessSource:
    def __init__(self, service: AsyncRoute53GlobalResolverClient) -> None:
        self._service = service

    async def create(
        self,
        cidr: "capo_route53globalresolver.types.cidr.Cidr",
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        protocol: "capo_route53globalresolver.types.dns_protocol.DnsProtocol",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        ip_address_type: Optional[
            "capo_route53globalresolver.types.ip_address_type.IpAddressType"
        ] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
        ] = None,
        tags: Optional["capo_route53globalresolver.types.tags.Tags"] = None,
    ) -> "capo_route53globalresolver.types.create_access_source_output.CreateAccessSourceOutput":
        """<p>Creates an access source for a DNS view. Access sources define IP addresses or CIDR ranges that are allowed to send DNS queries to the Route 53 Global Resolver, along with the permitted DNS protocols.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            cidr: <p>The IP address or CIDR range that is allowed to send DNS queries to the Route 53 Global Resolver.</p>
            client_token: <p>A unique string that identifies the request and ensures idempotency.</p>
            ip_address_type: <p>The IP address type for this access source. Valid values are IPv4 and IPv6 (if the Route 53 Global Resolver supports dual-stack).</p>
            name: <p>A descriptive name for the access source.</p>
            dns_view_id: <p>The ID of the DNS view to associate with this access source.</p>
            protocol: <p>The DNS protocol that is permitted for this access source. Valid values are Do53 (DNS over port 53), DoT (DNS over TLS), and DoH (DNS over HTTPS).</p>
            tags: <p>Tags to associate with the access source.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateAccessSource example

            >>> await client.create(cidr='85.90.183.3/30', client_token='9fas9-9usdfa-xbi8-kco', dns_view_id='dnsv-123456789', ip_address_type='IPV4', name='My Access Source', protocol='DO53', tags={'Key1': 'Value1'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.create_access_source_input.CreateAccessSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.create_access_source_output.CreateAccessSourceOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_source

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_source.async_create_access_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateAccessSource")
        )
        input_: capo_route53globalresolver.types.create_access_source_input.CreateAccessSourceInput = {
            "cidr": cidr,
            "dns_view_id": dns_view_id,
            "protocol": protocol,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if name is not None:
            input_["name"] = name
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
        access_source_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_access_source_output.GetAccessSourceOutput":
        """<p>Retrieves information about an access source.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to retrieve.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.get_access_source_input.GetAccessSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.get_access_source_output.GetAccessSourceOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_source

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_source.async_get_access_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAccessSource")
        )
        input_: capo_route53globalresolver.types.get_access_source_input.GetAccessSourceInput = {
            "access_source_id": access_source_id
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
        access_source_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        cidr: Optional["capo_route53globalresolver.types.cidr.Cidr"] = None,
        ip_address_type: Optional[
            "capo_route53globalresolver.types.ip_address_type.IpAddressType"
        ] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
        ] = None,
        protocol: Optional[
            "capo_route53globalresolver.types.dns_protocol.DnsProtocol"
        ] = None,
    ) -> "capo_route53globalresolver.types.update_access_source_output.UpdateAccessSourceOutput":
        """<p>Updates the configuration of an access source.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to update.</p>
            cidr: <p>The CIDR block for the access source.</p>
            ip_address_type: <p>The IP address type for the access source.</p>
            name: <p>The name of the access source.</p>
            protocol: <p>The protocol for the access source.</p>

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
            req: "AsyncOperationRequest[capo_route53globalresolver.types.update_access_source_input.UpdateAccessSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.update_access_source_output.UpdateAccessSourceOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_source

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_source.async_update_access_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAccessSource")
        )
        input_: capo_route53globalresolver.types.update_access_source_input.UpdateAccessSourceInput = {
            "access_source_id": access_source_id
        }
        if cidr is not None:
            input_["cidr"] = cidr
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if name is not None:
            input_["name"] = name
        if protocol is not None:
            input_["protocol"] = protocol

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        access_source_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_access_source_output.DeleteAccessSourceOutput":
        """<p>Deletes an access source. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to delete.</p>

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
            req: "AsyncOperationRequest[capo_route53globalresolver.types.delete_access_source_input.DeleteAccessSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.delete_access_source_output.DeleteAccessSourceOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_source

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_source.async_delete_access_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAccessSource")
        )
        input_: capo_route53globalresolver.types.delete_access_source_input.DeleteAccessSourceInput = {
            "access_source_id": access_source_id
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
        filters: Optional["capo_route53globalresolver.types.filters.Filters"] = None,
    ) -> "capo_route53globalresolver.types.list_access_sources_output.ListAccessSourcesOutput":
        """<p>Lists all access sources with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            filters: <p>Values to filter the results.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_access_sources_input.ListAccessSourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_access_sources_output.ListAccessSourcesOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_sources

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_sources.async_list_access_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAccessSources")
        )
        input_: capo_route53globalresolver.types.list_access_sources_input.ListAccessSourcesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
