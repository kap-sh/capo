from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_vpc_lattice._auth._signers
import capo_vpc_lattice._auth._sigv4
from capo_vpc_lattice._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.create_resource_configuration_request
    import capo_vpc_lattice.types.create_resource_configuration_response
    import capo_vpc_lattice.types.delete_resource_configuration_request
    import capo_vpc_lattice.types.delete_resource_configuration_response
    import capo_vpc_lattice.types.domain_name
    import capo_vpc_lattice.types.domain_verification_identifier
    import capo_vpc_lattice.types.get_resource_configuration_request
    import capo_vpc_lattice.types.get_resource_configuration_response
    import capo_vpc_lattice.types.list_resource_configurations_request
    import capo_vpc_lattice.types.list_resource_configurations_response
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.port_range_list
    import capo_vpc_lattice.types.protocol_type
    import capo_vpc_lattice.types.resource_configuration_definition
    import capo_vpc_lattice.types.resource_configuration_identifier
    import capo_vpc_lattice.types.resource_configuration_name
    import capo_vpc_lattice.types.resource_configuration_summary
    import capo_vpc_lattice.types.resource_configuration_type
    import capo_vpc_lattice.types.resource_gateway_identifier
    import capo_vpc_lattice.types.tag_map
    import capo_vpc_lattice.types.update_resource_configuration_request
    import capo_vpc_lattice.types.update_resource_configuration_response
    from capo_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from capo_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class ResourceConfiguration:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_vpc_lattice.types.resource_configuration_name.ResourceConfigurationName",
        type: "capo_vpc_lattice.types.resource_configuration_type.ResourceConfigurationType",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        port_ranges: Optional[
            "capo_vpc_lattice.types.port_range_list.PortRangeList"
        ] = None,
        protocol: Optional["capo_vpc_lattice.types.protocol_type.ProtocolType"] = None,
        resource_gateway_identifier: Optional[
            "capo_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
        ] = None,
        resource_configuration_group_identifier: Optional[
            "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        resource_configuration_definition: Optional[
            "capo_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
        ] = None,
        allow_association_to_shareable_service_network: Optional[
            "capo_vpc_lattice.types.boolean.Boolean"
        ] = None,
        custom_domain_name: Optional[
            "capo_vpc_lattice.types.domain_name.DomainName"
        ] = None,
        group_domain: Optional["capo_vpc_lattice.types.domain_name.DomainName"] = None,
        domain_verification_identifier: Optional[
            "capo_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
        ] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_resource_configuration_response.CreateResourceConfigurationResponse":
        """<p>Creates a resource configuration. A resource configuration defines a specific resource. You can associate a resource configuration with a service network or a VPC endpoint.</p>

        Args:
            name: <p>The name of the resource configuration. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            type: <p>The type of resource configuration. A resource configuration can be one of the following types:</p> <ul> <li> <p> <b>SINGLE</b> - A single resource.</p> </li> <li> <p> <b>GROUP</b> - A group of resources. You must create a group resource configuration before you create a child resource configuration.</p> </li> <li> <p> <b>CHILD</b> - A single resource that is part of a group resource configuration.</p> </li> <li> <p> <b>ARN</b> - An Amazon Web Services resource.</p> </li> <li> <p> <b>CIDR</b> - A network segment, expressed as a range of IP addresses (a CIDR block). Use this type to share a portion of your network rather than an individual resource. A consumer accesses the resources within the CIDR range through a <code>Tunnel</code> VPC endpoint. You can't add a CIDR resource configuration to a service network. A CIDR resource configuration must be associated with a resource gateway whose DNS resolution is set to <code>IN_VPC</code>.</p> </li> </ul>
            port_ranges: <p>(SINGLE, GROUP, CHILD, CIDR) The port ranges that a consumer can use to access a resource configuration (for example: 1-65535). You can separate port ranges using commas (for example: 1,2,22-30). To resolve DNS through a CIDR resource configuration, include port 53 in the port ranges.</p>
            protocol: <p>(SINGLE, GROUP, CIDR) The protocol accepted by the resource configuration. The default is <code>TCP</code>. <code>TCP_UDP</code> is supported only for CIDR resource configurations; specify it for a CIDR resource configuration to allow DNS resolution, which uses UDP.</p>
            resource_gateway_identifier: <p>(SINGLE, GROUP, ARN, CIDR) The ID or ARN of the resource gateway used to connect to the resource configuration. For a child resource configuration, this value is inherited from the parent resource configuration. For a CIDR resource configuration, the associated resource gateway must have its DNS resolution set to <code>IN_VPC</code> so that DNS queries resolve in the context of your VPC.</p>
            resource_configuration_group_identifier: <p>(CHILD) The ID or ARN of the parent resource configuration of type <code>GROUP</code>. This is used to associate a child resource configuration with a group resource configuration.</p>
            resource_configuration_definition: <p>Identifies the resource configuration in one of the following ways:</p> <ul> <li> <p> <b>Amazon Resource Name (ARN)</b> - Supported resource-types that are provisioned by Amazon Web Services services, such as RDS databases, can be identified by their ARN.</p> </li> <li> <p> <b>Domain name</b> - Any domain name that is publicly resolvable.</p> </li> <li> <p> <b>IP address</b> - For IPv4 and IPv6, only IP addresses in the VPC are supported.</p> </li> <li> <p> <b>CIDR range</b> - For a resource configuration of type CIDR, specify a <code>cidrResource</code> with one or more <code>cidrRanges</code> (for example, <code>10.0.0.0/16</code>) that cover the IP addresses of the resources you want to make accessible. You can specify up to 10 ranges, using IPv4, IPv6, or both, and each range must include a prefix length. To represent your entire network, specify <code>0.0.0.0/0</code> (IPv4) or <code>::/0</code> (IPv6) as the only range. You can't use reserved ranges such as <code>169.254.0.0/16</code>, <code>100.64.0.0/10</code>, <code>224.0.0.0/4</code>, <code>fe80::/10</code>, or <code>ff00::/8</code>.</p> </li> </ul>
            allow_association_to_shareable_service_network: <p>(SINGLE, GROUP, ARN) Specifies whether the resource configuration can be associated with a sharable service network. The default is false.</p>
            custom_domain_name: <p> A custom domain name for your resource configuration. Additionally, provide a DomainVerificationID to prove your ownership of a domain. </p>
            group_domain: <p> (GROUP) The group domain for a group resource configuration. Any domains that you create for the child resource are subdomains of the group domain. Child resources inherit the verification status of the domain. </p>
            domain_verification_identifier: <p> The domain verification ID of your verified custom domain name. If you don't provide an ID, you must configure the DNS settings yourself. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the resource configuration.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_resource_configuration_request.CreateResourceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_resource_configuration_response.CreateResourceConfigurationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_resource_configuration

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_resource_configuration.create_resource_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateResourceConfiguration")
        )
        input_: capo_vpc_lattice.types.create_resource_configuration_request.CreateResourceConfigurationRequest = {
            "name": name,
            "type": type,
        }
        if port_ranges is not None:
            input_["port_ranges"] = port_ranges
        if protocol is not None:
            input_["protocol"] = protocol
        if resource_gateway_identifier is not None:
            input_["resource_gateway_identifier"] = resource_gateway_identifier
        if resource_configuration_group_identifier is not None:
            input_["resource_configuration_group_identifier"] = (
                resource_configuration_group_identifier
            )
        if resource_configuration_definition is not None:
            input_["resource_configuration_definition"] = (
                resource_configuration_definition
            )
        if allow_association_to_shareable_service_network is not None:
            input_["allow_association_to_shareable_service_network"] = (
                allow_association_to_shareable_service_network
            )
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if group_domain is not None:
            input_["group_domain"] = group_domain
        if domain_verification_identifier is not None:
            input_["domain_verification_identifier"] = domain_verification_identifier
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
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_resource_configuration_response.GetResourceConfigurationResponse":
        """<p>Retrieves information about the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID of the resource configuration.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_resource_configuration_request.GetResourceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_resource_configuration_response.GetResourceConfigurationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_resource_configuration

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_resource_configuration.get_resource_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetResourceConfiguration")
        )
        input_: capo_vpc_lattice.types.get_resource_configuration_request.GetResourceConfigurationRequest = {
            "resource_configuration_identifier": resource_configuration_identifier
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
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        resource_configuration_definition: Optional[
            "capo_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
        ] = None,
        allow_association_to_shareable_service_network: Optional[
            "capo_vpc_lattice.types.boolean.Boolean"
        ] = None,
        port_ranges: Optional[
            "capo_vpc_lattice.types.port_range_list.PortRangeList"
        ] = None,
    ) -> "capo_vpc_lattice.types.update_resource_configuration_response.UpdateResourceConfigurationResponse":
        """<p>Updates the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID of the resource configuration.</p>
            resource_configuration_definition: <p>Identifies the resource configuration in one of the following ways:</p> <ul> <li> <p> <b>Amazon Resource Name (ARN)</b> - Supported resource-types that are provisioned by Amazon Web Services services, such as RDS databases, can be identified by their ARN.</p> </li> <li> <p> <b>Domain name</b> - Any domain name that is publicly resolvable.</p> </li> <li> <p> <b>IP address</b> - For IPv4 and IPv6, only IP addresses in the VPC are supported.</p> </li> </ul>
            allow_association_to_shareable_service_network: <p>Indicates whether to add the resource configuration to service networks that are shared with other accounts.</p>
            port_ranges: <p>The TCP port ranges that a consumer can use to access a resource configuration. You can separate port ranges with a comma. Example: 1-65535 or 1,2,22-30</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.update_resource_configuration_request.UpdateResourceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.update_resource_configuration_response.UpdateResourceConfigurationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_resource_configuration

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.update_resource_configuration.update_resource_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateResourceConfiguration")
        )
        input_: capo_vpc_lattice.types.update_resource_configuration_request.UpdateResourceConfigurationRequest = {
            "resource_configuration_identifier": resource_configuration_identifier
        }
        if resource_configuration_definition is not None:
            input_["resource_configuration_definition"] = (
                resource_configuration_definition
            )
        if allow_association_to_shareable_service_network is not None:
            input_["allow_association_to_shareable_service_network"] = (
                allow_association_to_shareable_service_network
            )
        if port_ranges is not None:
            input_["port_ranges"] = port_ranges

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_resource_configuration_response.DeleteResourceConfigurationResponse":
        """<p>Deletes the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID or ARN of the resource configuration.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_resource_configuration_request.DeleteResourceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_resource_configuration_response.DeleteResourceConfigurationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_resource_configuration

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_resource_configuration.delete_resource_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteResourceConfiguration")
        )
        input_: capo_vpc_lattice.types.delete_resource_configuration_request.DeleteResourceConfigurationRequest = {
            "resource_configuration_identifier": resource_configuration_identifier
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
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        resource_gateway_identifier: Optional[
            "capo_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
        ] = None,
        resource_configuration_group_identifier: Optional[
            "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        domain_verification_identifier: Optional[
            "capo_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_resource_configurations_response.ListResourceConfigurationsResponse":
        """<p>Lists the resource configurations owned by or shared with this account.</p>

        Args:
            resource_gateway_identifier: <p>The ID of the resource gateway for the resource configuration.</p>
            resource_configuration_group_identifier: <p>The ID of the resource configuration of type <code>Group</code>.</p>
            domain_verification_identifier: <p> The domain verification ID. </p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_resource_configurations_request.ListResourceConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_resource_configurations_response.ListResourceConfigurationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_resource_configurations

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_resource_configurations.list_resource_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListResourceConfigurations")
        )
        input_: capo_vpc_lattice.types.list_resource_configurations_request.ListResourceConfigurationsRequest = {}
        if resource_gateway_identifier is not None:
            input_["resource_gateway_identifier"] = resource_gateway_identifier
        if resource_configuration_group_identifier is not None:
            input_["resource_configuration_group_identifier"] = (
                resource_configuration_group_identifier
            )
        if domain_verification_identifier is not None:
            input_["domain_verification_identifier"] = domain_verification_identifier
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


class AsyncResourceConfiguration:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_vpc_lattice.types.resource_configuration_name.ResourceConfigurationName",
        type: "capo_vpc_lattice.types.resource_configuration_type.ResourceConfigurationType",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        port_ranges: Optional[
            "capo_vpc_lattice.types.port_range_list.PortRangeList"
        ] = None,
        protocol: Optional["capo_vpc_lattice.types.protocol_type.ProtocolType"] = None,
        resource_gateway_identifier: Optional[
            "capo_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
        ] = None,
        resource_configuration_group_identifier: Optional[
            "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        resource_configuration_definition: Optional[
            "capo_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
        ] = None,
        allow_association_to_shareable_service_network: Optional[
            "capo_vpc_lattice.types.boolean.Boolean"
        ] = None,
        custom_domain_name: Optional[
            "capo_vpc_lattice.types.domain_name.DomainName"
        ] = None,
        group_domain: Optional["capo_vpc_lattice.types.domain_name.DomainName"] = None,
        domain_verification_identifier: Optional[
            "capo_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
        ] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_resource_configuration_response.CreateResourceConfigurationResponse":
        """<p>Creates a resource configuration. A resource configuration defines a specific resource. You can associate a resource configuration with a service network or a VPC endpoint.</p>

        Args:
            name: <p>The name of the resource configuration. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            type: <p>The type of resource configuration. A resource configuration can be one of the following types:</p> <ul> <li> <p> <b>SINGLE</b> - A single resource.</p> </li> <li> <p> <b>GROUP</b> - A group of resources. You must create a group resource configuration before you create a child resource configuration.</p> </li> <li> <p> <b>CHILD</b> - A single resource that is part of a group resource configuration.</p> </li> <li> <p> <b>ARN</b> - An Amazon Web Services resource.</p> </li> <li> <p> <b>CIDR</b> - A network segment, expressed as a range of IP addresses (a CIDR block). Use this type to share a portion of your network rather than an individual resource. A consumer accesses the resources within the CIDR range through a <code>Tunnel</code> VPC endpoint. You can't add a CIDR resource configuration to a service network. A CIDR resource configuration must be associated with a resource gateway whose DNS resolution is set to <code>IN_VPC</code>.</p> </li> </ul>
            port_ranges: <p>(SINGLE, GROUP, CHILD, CIDR) The port ranges that a consumer can use to access a resource configuration (for example: 1-65535). You can separate port ranges using commas (for example: 1,2,22-30). To resolve DNS through a CIDR resource configuration, include port 53 in the port ranges.</p>
            protocol: <p>(SINGLE, GROUP, CIDR) The protocol accepted by the resource configuration. The default is <code>TCP</code>. <code>TCP_UDP</code> is supported only for CIDR resource configurations; specify it for a CIDR resource configuration to allow DNS resolution, which uses UDP.</p>
            resource_gateway_identifier: <p>(SINGLE, GROUP, ARN, CIDR) The ID or ARN of the resource gateway used to connect to the resource configuration. For a child resource configuration, this value is inherited from the parent resource configuration. For a CIDR resource configuration, the associated resource gateway must have its DNS resolution set to <code>IN_VPC</code> so that DNS queries resolve in the context of your VPC.</p>
            resource_configuration_group_identifier: <p>(CHILD) The ID or ARN of the parent resource configuration of type <code>GROUP</code>. This is used to associate a child resource configuration with a group resource configuration.</p>
            resource_configuration_definition: <p>Identifies the resource configuration in one of the following ways:</p> <ul> <li> <p> <b>Amazon Resource Name (ARN)</b> - Supported resource-types that are provisioned by Amazon Web Services services, such as RDS databases, can be identified by their ARN.</p> </li> <li> <p> <b>Domain name</b> - Any domain name that is publicly resolvable.</p> </li> <li> <p> <b>IP address</b> - For IPv4 and IPv6, only IP addresses in the VPC are supported.</p> </li> <li> <p> <b>CIDR range</b> - For a resource configuration of type CIDR, specify a <code>cidrResource</code> with one or more <code>cidrRanges</code> (for example, <code>10.0.0.0/16</code>) that cover the IP addresses of the resources you want to make accessible. You can specify up to 10 ranges, using IPv4, IPv6, or both, and each range must include a prefix length. To represent your entire network, specify <code>0.0.0.0/0</code> (IPv4) or <code>::/0</code> (IPv6) as the only range. You can't use reserved ranges such as <code>169.254.0.0/16</code>, <code>100.64.0.0/10</code>, <code>224.0.0.0/4</code>, <code>fe80::/10</code>, or <code>ff00::/8</code>.</p> </li> </ul>
            allow_association_to_shareable_service_network: <p>(SINGLE, GROUP, ARN) Specifies whether the resource configuration can be associated with a sharable service network. The default is false.</p>
            custom_domain_name: <p> A custom domain name for your resource configuration. Additionally, provide a DomainVerificationID to prove your ownership of a domain. </p>
            group_domain: <p> (GROUP) The group domain for a group resource configuration. Any domains that you create for the child resource are subdomains of the group domain. Child resources inherit the verification status of the domain. </p>
            domain_verification_identifier: <p> The domain verification ID of your verified custom domain name. If you don't provide an ID, you must configure the DNS settings yourself. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the resource configuration.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.create_resource_configuration_request.CreateResourceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.create_resource_configuration_response.CreateResourceConfigurationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_resource_configuration

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.create_resource_configuration.async_create_resource_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateResourceConfiguration")
        )
        input_: capo_vpc_lattice.types.create_resource_configuration_request.CreateResourceConfigurationRequest = {
            "name": name,
            "type": type,
        }
        if port_ranges is not None:
            input_["port_ranges"] = port_ranges
        if protocol is not None:
            input_["protocol"] = protocol
        if resource_gateway_identifier is not None:
            input_["resource_gateway_identifier"] = resource_gateway_identifier
        if resource_configuration_group_identifier is not None:
            input_["resource_configuration_group_identifier"] = (
                resource_configuration_group_identifier
            )
        if resource_configuration_definition is not None:
            input_["resource_configuration_definition"] = (
                resource_configuration_definition
            )
        if allow_association_to_shareable_service_network is not None:
            input_["allow_association_to_shareable_service_network"] = (
                allow_association_to_shareable_service_network
            )
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if group_domain is not None:
            input_["group_domain"] = group_domain
        if domain_verification_identifier is not None:
            input_["domain_verification_identifier"] = domain_verification_identifier
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
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_resource_configuration_response.GetResourceConfigurationResponse":
        """<p>Retrieves information about the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID of the resource configuration.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.get_resource_configuration_request.GetResourceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.get_resource_configuration_response.GetResourceConfigurationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_resource_configuration

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.get_resource_configuration.async_get_resource_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetResourceConfiguration")
        )
        input_: capo_vpc_lattice.types.get_resource_configuration_request.GetResourceConfigurationRequest = {
            "resource_configuration_identifier": resource_configuration_identifier
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
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        resource_configuration_definition: Optional[
            "capo_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
        ] = None,
        allow_association_to_shareable_service_network: Optional[
            "capo_vpc_lattice.types.boolean.Boolean"
        ] = None,
        port_ranges: Optional[
            "capo_vpc_lattice.types.port_range_list.PortRangeList"
        ] = None,
    ) -> "capo_vpc_lattice.types.update_resource_configuration_response.UpdateResourceConfigurationResponse":
        """<p>Updates the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID of the resource configuration.</p>
            resource_configuration_definition: <p>Identifies the resource configuration in one of the following ways:</p> <ul> <li> <p> <b>Amazon Resource Name (ARN)</b> - Supported resource-types that are provisioned by Amazon Web Services services, such as RDS databases, can be identified by their ARN.</p> </li> <li> <p> <b>Domain name</b> - Any domain name that is publicly resolvable.</p> </li> <li> <p> <b>IP address</b> - For IPv4 and IPv6, only IP addresses in the VPC are supported.</p> </li> </ul>
            allow_association_to_shareable_service_network: <p>Indicates whether to add the resource configuration to service networks that are shared with other accounts.</p>
            port_ranges: <p>The TCP port ranges that a consumer can use to access a resource configuration. You can separate port ranges with a comma. Example: 1-65535 or 1,2,22-30</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.update_resource_configuration_request.UpdateResourceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.update_resource_configuration_response.UpdateResourceConfigurationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_resource_configuration

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.update_resource_configuration.async_update_resource_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateResourceConfiguration")
        )
        input_: capo_vpc_lattice.types.update_resource_configuration_request.UpdateResourceConfigurationRequest = {
            "resource_configuration_identifier": resource_configuration_identifier
        }
        if resource_configuration_definition is not None:
            input_["resource_configuration_definition"] = (
                resource_configuration_definition
            )
        if allow_association_to_shareable_service_network is not None:
            input_["allow_association_to_shareable_service_network"] = (
                allow_association_to_shareable_service_network
            )
        if port_ranges is not None:
            input_["port_ranges"] = port_ranges

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_resource_configuration_response.DeleteResourceConfigurationResponse":
        """<p>Deletes the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID or ARN of the resource configuration.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.delete_resource_configuration_request.DeleteResourceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.delete_resource_configuration_response.DeleteResourceConfigurationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_resource_configuration

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.delete_resource_configuration.async_delete_resource_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteResourceConfiguration")
        )
        input_: capo_vpc_lattice.types.delete_resource_configuration_request.DeleteResourceConfigurationRequest = {
            "resource_configuration_identifier": resource_configuration_identifier
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
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        resource_gateway_identifier: Optional[
            "capo_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
        ] = None,
        resource_configuration_group_identifier: Optional[
            "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        domain_verification_identifier: Optional[
            "capo_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_resource_configurations_response.ListResourceConfigurationsResponse":
        """<p>Lists the resource configurations owned by or shared with this account.</p>

        Args:
            resource_gateway_identifier: <p>The ID of the resource gateway for the resource configuration.</p>
            resource_configuration_group_identifier: <p>The ID of the resource configuration of type <code>Group</code>.</p>
            domain_verification_identifier: <p> The domain verification ID. </p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.list_resource_configurations_request.ListResourceConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.list_resource_configurations_response.ListResourceConfigurationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_resource_configurations

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.list_resource_configurations.async_list_resource_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListResourceConfigurations")
        )
        input_: capo_vpc_lattice.types.list_resource_configurations_request.ListResourceConfigurationsRequest = {}
        if resource_gateway_identifier is not None:
            input_["resource_gateway_identifier"] = resource_gateway_identifier
        if resource_configuration_group_identifier is not None:
            input_["resource_configuration_group_identifier"] = (
                resource_configuration_group_identifier
            )
        if domain_verification_identifier is not None:
            input_["domain_verification_identifier"] = domain_verification_identifier
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
