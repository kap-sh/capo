from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_rtbfabric._auth._signers
import capo_rtbfabric._auth._sigv4
from capo_rtbfabric._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_rtbfabric.types.acm_certificate_arn
    import capo_rtbfabric.types.associate_certificate_request
    import capo_rtbfabric.types.associate_certificate_response
    import capo_rtbfabric.types.certificate_association_summary
    import capo_rtbfabric.types.client_routing_policy
    import capo_rtbfabric.types.create_responder_gateway_request
    import capo_rtbfabric.types.create_responder_gateway_response
    import capo_rtbfabric.types.delete_responder_gateway_request
    import capo_rtbfabric.types.delete_responder_gateway_response
    import capo_rtbfabric.types.disassociate_certificate_request
    import capo_rtbfabric.types.disassociate_certificate_response
    import capo_rtbfabric.types.domain_name
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.gateway_type
    import capo_rtbfabric.types.get_certificate_association_request
    import capo_rtbfabric.types.get_certificate_association_response
    import capo_rtbfabric.types.get_responder_gateway_request
    import capo_rtbfabric.types.get_responder_gateway_response
    import capo_rtbfabric.types.list_certificate_associations_request
    import capo_rtbfabric.types.list_certificate_associations_response
    import capo_rtbfabric.types.listener_config
    import capo_rtbfabric.types.managed_endpoint_configuration
    import capo_rtbfabric.types.protocol
    import capo_rtbfabric.types.security_group_id_list
    import capo_rtbfabric.types.subnet_id_list
    import capo_rtbfabric.types.tags_map
    import capo_rtbfabric.types.trust_store_configuration
    import capo_rtbfabric.types.update_responder_gateway_request
    import capo_rtbfabric.types.update_responder_gateway_response
    import capo_rtbfabric.types.vpc_id
    from capo_rtbfabric._services.async_rtb_fabric import (
        AsyncRTBFabricClient,
        AsyncRTBFabricClientConfig,
    )
    from capo_rtbfabric._services.rtb_fabric import (
        RTBFabricClient,
        RTBFabricClientConfig,
    )


class ResponderGateway:
    def __init__(self, service: RTBFabricClient) -> None:
        self._service = service

    def create(
        self,
        vpc_id: "capo_rtbfabric.types.vpc_id.VpcId",
        subnet_ids: "capo_rtbfabric.types.subnet_id_list.SubnetIdList",
        security_group_ids: "capo_rtbfabric.types.security_group_id_list.SecurityGroupIdList",
        port: int,
        protocol: "capo_rtbfabric.types.protocol.Protocol",
        client_token: str,
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        domain_name: Optional["capo_rtbfabric.types.domain_name.DomainName"] = None,
        listener_config: Optional[
            "capo_rtbfabric.types.listener_config.ListenerConfig"
        ] = None,
        trust_store_configuration: Optional[
            "capo_rtbfabric.types.trust_store_configuration.TrustStoreConfiguration"
        ] = None,
        managed_endpoint_configuration: Optional[
            "capo_rtbfabric.types.managed_endpoint_configuration.ManagedEndpointConfiguration"
        ] = None,
        description: Optional[str] = None,
        tags: Optional["capo_rtbfabric.types.tags_map.TagsMap"] = None,
        gateway_type: Optional["capo_rtbfabric.types.gateway_type.GatewayType"] = None,
        client_routing_policy: Optional[
            "capo_rtbfabric.types.client_routing_policy.ClientRoutingPolicy"
        ] = None,
    ) -> "capo_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse":
        """<p>Creates a responder gateway.</p> <important> <p>A domain name or managed endpoint is required.</p> </important>

        Args:
            vpc_id: <p>The unique identifier of the Virtual Private Cloud (VPC).</p>
            subnet_ids: <p>Unique identifiers of the subnets. A service quota for your account sets the number of Availability Zones that your subnets can span. By default, this quota is one Availability Zone. To span more Availability Zones, request a quota increase.</p>
            security_group_ids: <p>The unique identifiers of the security groups.</p>
            domain_name: <p>The domain name for the responder gateway.</p>
            port: <p>The networking port to use.</p>
            protocol: <p>The networking protocol to use.</p>
            trust_store_configuration: <p>The configuration of the trust store.</p>
            managed_endpoint_configuration: <p>The configuration for the managed endpoint.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            description: <p>An optional description for the responder gateway.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>
            gateway_type: <p>The type of gateway. Valid values are <code>EXTERNAL</code> or <code>INTERNAL</code>.</p>
            client_routing_policy: <p>The client routing policy of the gateway. This policy controls which Availability Zones RTB Fabric uses to reach the gateway for the requester gateways that send traffic to it. Valid values are the following:</p> <ul> <li> <p> <code>AVAILABILITY_ZONE_AFFINITY</code>: RTB Fabric routes each requester's traffic to gateway capacity in the requester's own Availability Zone when the gateway has capacity available there. Otherwise, RTB Fabric routes the traffic to gateway capacity in the other Availability Zones of the gateway.</p> </li> <li> <p> <code>ANY_AVAILABILITY_ZONE</code>: RTB Fabric routes each requester's traffic to gateway capacity in every Availability Zone that the subnets of the gateway span. The Availability Zone that the requester is in does not change this.</p> </li> </ul> <p>If you don't specify a value, RTB Fabric uses <code>AVAILABILITY_ZONE_AFFINITY</code>. To get the behavior of <code>ANY_AVAILABILITY_ZONE</code>, create the gateway with subnets in more than one Availability Zone. RTB Fabric does not support partial Availability Zone affinity, so <code>PARTIAL_AVAILABILITY_ZONE_AFFINITY</code> is not a valid value. For more information, see <a href="https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-responder-gateways.html#configuring-availability-zone-affinity">Configuring Availability Zone affinity</a> in the <i>Amazon Web Services RTB Fabric User Guide</i>.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a responder gateway
            Create responder gateway

            >>> client.create(description='My responder gateway', vpc_id='vpc-12345678', subnet_ids=['subnet-12345678', 'subnet-87654321'], security_group_ids=['sg-12345678'], port=443, protocol='HTTPS', client_token='12345678-1234-1234-1234-123456789012')
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.create_responder_gateway_request.CreateResponderGatewayRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.create_responder_gateway

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.create_responder_gateway.create_responder_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.create_responder_gateway_request.CreateResponderGatewayRequest = {
            "vpc_id": vpc_id,
            "subnet_ids": subnet_ids,
            "security_group_ids": security_group_ids,
            "port": port,
            "protocol": protocol,
            "client_token": client_token,
        }
        if domain_name is not None:
            input_["domain_name"] = domain_name
        if listener_config is not None:
            input_["listener_config"] = listener_config
        if trust_store_configuration is not None:
            input_["trust_store_configuration"] = trust_store_configuration
        if managed_endpoint_configuration is not None:
            input_["managed_endpoint_configuration"] = managed_endpoint_configuration
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if gateway_type is not None:
            input_["gateway_type"] = gateway_type
        if client_routing_policy is not None:
            input_["client_routing_policy"] = client_routing_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.get_responder_gateway_response.GetResponderGatewayResponse":
        """<p>Retrieves information about a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get responder gateway details
            Get responder gateway

            >>> client.read(gateway_id='rtb-gw-12345678')
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.get_responder_gateway_request.GetResponderGatewayRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.get_responder_gateway_response.GetResponderGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.get_responder_gateway

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.get_responder_gateway.get_responder_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.get_responder_gateway_request.GetResponderGatewayRequest = {
            "gateway_id": gateway_id
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
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.delete_responder_gateway_response.DeleteResponderGatewayResponse":
        """<p>Deletes a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a responder gateway
            Delete responder gateway

            >>> client.delete(gateway_id='rtb-gw-12345678')
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.delete_responder_gateway_request.DeleteResponderGatewayRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.delete_responder_gateway_response.DeleteResponderGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.delete_responder_gateway

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.delete_responder_gateway.delete_responder_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.delete_responder_gateway_request.DeleteResponderGatewayRequest = {
            "gateway_id": gateway_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_certificate(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "capo_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        client_token: str,
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.associate_certificate_response.AssociateCertificateResponse":
        """<p>Associates an ACM certificate with a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate to associate.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Associate a certificate with a responder gateway
            Associate an ACM certificate with a responder gateway

            >>> client.associate_certificate(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012', client_token='550e8400-e29b-41d4-a716-446655440000')
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.associate_certificate_request.AssociateCertificateRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.associate_certificate_response.AssociateCertificateResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.associate_certificate

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.associate_certificate.associate_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.associate_certificate_request.AssociateCertificateRequest = {
            "gateway_id": gateway_id,
            "acm_certificate_arn": acm_certificate_arn,
            "client_token": client_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_certificate(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "capo_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.disassociate_certificate_response.DisassociateCertificateResponse":
        """<p>Removes a certificate association from a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate to disassociate.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Disassociate a certificate from a responder gateway
            Remove an ACM certificate association from a responder gateway

            >>> client.disassociate_certificate(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012')
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.disassociate_certificate_request.DisassociateCertificateRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.disassociate_certificate_response.DisassociateCertificateResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.disassociate_certificate

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.disassociate_certificate.disassociate_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.disassociate_certificate_request.DisassociateCertificateRequest = {
            "gateway_id": gateway_id,
            "acm_certificate_arn": acm_certificate_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_certificate_association(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "capo_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.get_certificate_association_response.GetCertificateAssociationResponse":
        """<p>Retrieves the details of a certificate association with a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get certificate association details from a responder gateway
            Retrieve details of an ACM certificate association with a responder gateway

            >>> client.get_certificate_association(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012')
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.get_certificate_association_request.GetCertificateAssociationRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.get_certificate_association_response.GetCertificateAssociationResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.get_certificate_association

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.get_certificate_association.get_certificate_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.get_certificate_association_request.GetCertificateAssociationRequest = {
            "gateway_id": gateway_id,
            "acm_certificate_arn": acm_certificate_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_certificate_associations(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_rtbfabric.types.list_certificate_associations_response.ListCertificateAssociationsResponse":
        """<p>Lists the certificate associations for a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List certificate associations for a responder gateway
            Retrieve all certificate associations for a responder gateway

            >>> client.list_certificate_associations(gateway_id='rtb-gw-12345678', max_results=5)
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.list_certificate_associations_request.ListCertificateAssociationsRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.list_certificate_associations_response.ListCertificateAssociationsResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.list_certificate_associations

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.list_certificate_associations.list_certificate_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.list_certificate_associations_request.ListCertificateAssociationsRequest = {
            "gateway_id": gateway_id
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

    def update_responder_gateway(
        self,
        port: int,
        protocol: "capo_rtbfabric.types.protocol.Protocol",
        client_token: str,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        domain_name: Optional["capo_rtbfabric.types.domain_name.DomainName"] = None,
        listener_config: Optional[
            "capo_rtbfabric.types.listener_config.ListenerConfig"
        ] = None,
        trust_store_configuration: Optional[
            "capo_rtbfabric.types.trust_store_configuration.TrustStoreConfiguration"
        ] = None,
        managed_endpoint_configuration: Optional[
            "capo_rtbfabric.types.managed_endpoint_configuration.ManagedEndpointConfiguration"
        ] = None,
        description: Optional[str] = None,
        client_routing_policy: Optional[
            "capo_rtbfabric.types.client_routing_policy.ClientRoutingPolicy"
        ] = None,
    ) -> "capo_rtbfabric.types.update_responder_gateway_response.UpdateResponderGatewayResponse":
        """<p>Updates the description, Auto Scaling group managed endpoint configuration, trust store configuration, and client routing policy of a responder gateway. This operation also updates the <code>protocols</code> list in the listener configuration.</p> <p>You cannot change the <code>domainName</code>, <code>port</code>, and <code>protocol</code> values that you set when you create a responder gateway. To change any of them, delete the gateway and create a new one.</p>

        Args:
            domain_name: <p>Domain name for the responder gateway. This operation does not change the domain name of an existing gateway. To use a different domain name, delete the gateway and create a new one.</p>
            port: <p>Networking port to use. This operation does not change the port of an existing gateway. To use a different port, delete the gateway and create a new one.</p>
            protocol: <p>Networking protocol to use. This operation does not change the protocol of an existing gateway. To use a different protocol, delete the gateway and create a new one.</p>
            listener_config: <p>The listener configuration for the responder gateway.</p>
            trust_store_configuration: <p>The configuration of the trust store.</p>
            managed_endpoint_configuration: <p>The configuration for the managed endpoint.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            gateway_id: <p>The unique identifier of the gateway.</p>
            description: <p>An optional description for the responder gateway.</p>
            client_routing_policy: <p>The client routing policy of the gateway. This policy controls which Availability Zones RTB Fabric uses to reach the gateway for the requester gateways that send traffic to it. Valid values are the following:</p> <ul> <li> <p> <code>AVAILABILITY_ZONE_AFFINITY</code>: RTB Fabric routes each requester's traffic to gateway capacity in the requester's own Availability Zone when the gateway has capacity available there. Otherwise, RTB Fabric routes the traffic to gateway capacity in the other Availability Zones of the gateway.</p> </li> <li> <p> <code>ANY_AVAILABILITY_ZONE</code>: RTB Fabric routes each requester's traffic to gateway capacity in every Availability Zone that the subnets of the gateway span. The Availability Zone that the requester is in does not change this.</p> </li> </ul> <p>If you don't specify a value, the gateway keeps its current client routing policy. Changing the policy sets the gateway status to <code>PENDING_UPDATE</code> until the change is complete. RTB Fabric does not support partial Availability Zone affinity, so <code>PARTIAL_AVAILABILITY_ZONE_AFFINITY</code> is not a valid value. For more information, see <a href="https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-responder-gateways.html#configuring-availability-zone-affinity">Configuring Availability Zone affinity</a> in the <i>Amazon Web Services RTB Fabric User Guide</i>.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update responder gateway
            Update responder gateway

            >>> client.update_responder_gateway(gateway_id='rtb-gw-12345678', description='Updated responder gateway description', port=8080, protocol='HTTP', client_token='12345678-1234-1234-1234-123456789012')
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.update_responder_gateway_request.UpdateResponderGatewayRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.update_responder_gateway_response.UpdateResponderGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.update_responder_gateway

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.update_responder_gateway.update_responder_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.update_responder_gateway_request.UpdateResponderGatewayRequest = {
            "port": port,
            "protocol": protocol,
            "client_token": client_token,
            "gateway_id": gateway_id,
        }
        if domain_name is not None:
            input_["domain_name"] = domain_name
        if listener_config is not None:
            input_["listener_config"] = listener_config
        if trust_store_configuration is not None:
            input_["trust_store_configuration"] = trust_store_configuration
        if managed_endpoint_configuration is not None:
            input_["managed_endpoint_configuration"] = managed_endpoint_configuration
        if description is not None:
            input_["description"] = description
        if client_routing_policy is not None:
            input_["client_routing_policy"] = client_routing_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncResponderGateway:
    def __init__(self, service: AsyncRTBFabricClient) -> None:
        self._service = service

    async def create(
        self,
        vpc_id: "capo_rtbfabric.types.vpc_id.VpcId",
        subnet_ids: "capo_rtbfabric.types.subnet_id_list.SubnetIdList",
        security_group_ids: "capo_rtbfabric.types.security_group_id_list.SecurityGroupIdList",
        port: int,
        protocol: "capo_rtbfabric.types.protocol.Protocol",
        client_token: str,
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        domain_name: Optional["capo_rtbfabric.types.domain_name.DomainName"] = None,
        listener_config: Optional[
            "capo_rtbfabric.types.listener_config.ListenerConfig"
        ] = None,
        trust_store_configuration: Optional[
            "capo_rtbfabric.types.trust_store_configuration.TrustStoreConfiguration"
        ] = None,
        managed_endpoint_configuration: Optional[
            "capo_rtbfabric.types.managed_endpoint_configuration.ManagedEndpointConfiguration"
        ] = None,
        description: Optional[str] = None,
        tags: Optional["capo_rtbfabric.types.tags_map.TagsMap"] = None,
        gateway_type: Optional["capo_rtbfabric.types.gateway_type.GatewayType"] = None,
        client_routing_policy: Optional[
            "capo_rtbfabric.types.client_routing_policy.ClientRoutingPolicy"
        ] = None,
    ) -> "capo_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse":
        """<p>Creates a responder gateway.</p> <important> <p>A domain name or managed endpoint is required.</p> </important>

        Args:
            vpc_id: <p>The unique identifier of the Virtual Private Cloud (VPC).</p>
            subnet_ids: <p>Unique identifiers of the subnets. A service quota for your account sets the number of Availability Zones that your subnets can span. By default, this quota is one Availability Zone. To span more Availability Zones, request a quota increase.</p>
            security_group_ids: <p>The unique identifiers of the security groups.</p>
            domain_name: <p>The domain name for the responder gateway.</p>
            port: <p>The networking port to use.</p>
            protocol: <p>The networking protocol to use.</p>
            trust_store_configuration: <p>The configuration of the trust store.</p>
            managed_endpoint_configuration: <p>The configuration for the managed endpoint.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            description: <p>An optional description for the responder gateway.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>
            gateway_type: <p>The type of gateway. Valid values are <code>EXTERNAL</code> or <code>INTERNAL</code>.</p>
            client_routing_policy: <p>The client routing policy of the gateway. This policy controls which Availability Zones RTB Fabric uses to reach the gateway for the requester gateways that send traffic to it. Valid values are the following:</p> <ul> <li> <p> <code>AVAILABILITY_ZONE_AFFINITY</code>: RTB Fabric routes each requester's traffic to gateway capacity in the requester's own Availability Zone when the gateway has capacity available there. Otherwise, RTB Fabric routes the traffic to gateway capacity in the other Availability Zones of the gateway.</p> </li> <li> <p> <code>ANY_AVAILABILITY_ZONE</code>: RTB Fabric routes each requester's traffic to gateway capacity in every Availability Zone that the subnets of the gateway span. The Availability Zone that the requester is in does not change this.</p> </li> </ul> <p>If you don't specify a value, RTB Fabric uses <code>AVAILABILITY_ZONE_AFFINITY</code>. To get the behavior of <code>ANY_AVAILABILITY_ZONE</code>, create the gateway with subnets in more than one Availability Zone. RTB Fabric does not support partial Availability Zone affinity, so <code>PARTIAL_AVAILABILITY_ZONE_AFFINITY</code> is not a valid value. For more information, see <a href="https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-responder-gateways.html#configuring-availability-zone-affinity">Configuring Availability Zone affinity</a> in the <i>Amazon Web Services RTB Fabric User Guide</i>.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a responder gateway
            Create responder gateway

            >>> await client.create(description='My responder gateway', vpc_id='vpc-12345678', subnet_ids=['subnet-12345678', 'subnet-87654321'], security_group_ids=['sg-12345678'], port=443, protocol='HTTPS', client_token='12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.create_responder_gateway_request.CreateResponderGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.create_responder_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.create_responder_gateway.async_create_responder_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.create_responder_gateway_request.CreateResponderGatewayRequest = {
            "vpc_id": vpc_id,
            "subnet_ids": subnet_ids,
            "security_group_ids": security_group_ids,
            "port": port,
            "protocol": protocol,
            "client_token": client_token,
        }
        if domain_name is not None:
            input_["domain_name"] = domain_name
        if listener_config is not None:
            input_["listener_config"] = listener_config
        if trust_store_configuration is not None:
            input_["trust_store_configuration"] = trust_store_configuration
        if managed_endpoint_configuration is not None:
            input_["managed_endpoint_configuration"] = managed_endpoint_configuration
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if gateway_type is not None:
            input_["gateway_type"] = gateway_type
        if client_routing_policy is not None:
            input_["client_routing_policy"] = client_routing_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.get_responder_gateway_response.GetResponderGatewayResponse":
        """<p>Retrieves information about a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get responder gateway details
            Get responder gateway

            >>> await client.read(gateway_id='rtb-gw-12345678')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.get_responder_gateway_request.GetResponderGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.get_responder_gateway_response.GetResponderGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.get_responder_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.get_responder_gateway.async_get_responder_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.get_responder_gateway_request.GetResponderGatewayRequest = {
            "gateway_id": gateway_id
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
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.delete_responder_gateway_response.DeleteResponderGatewayResponse":
        """<p>Deletes a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a responder gateway
            Delete responder gateway

            >>> await client.delete(gateway_id='rtb-gw-12345678')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.delete_responder_gateway_request.DeleteResponderGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.delete_responder_gateway_response.DeleteResponderGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.delete_responder_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.delete_responder_gateway.async_delete_responder_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.delete_responder_gateway_request.DeleteResponderGatewayRequest = {
            "gateway_id": gateway_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_certificate(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "capo_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        client_token: str,
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.associate_certificate_response.AssociateCertificateResponse":
        """<p>Associates an ACM certificate with a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate to associate.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Associate a certificate with a responder gateway
            Associate an ACM certificate with a responder gateway

            >>> await client.associate_certificate(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012', client_token='550e8400-e29b-41d4-a716-446655440000')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.associate_certificate_request.AssociateCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.associate_certificate_response.AssociateCertificateResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.associate_certificate

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.associate_certificate.async_associate_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.associate_certificate_request.AssociateCertificateRequest = {
            "gateway_id": gateway_id,
            "acm_certificate_arn": acm_certificate_arn,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_certificate(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "capo_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.disassociate_certificate_response.DisassociateCertificateResponse":
        """<p>Removes a certificate association from a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate to disassociate.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Disassociate a certificate from a responder gateway
            Remove an ACM certificate association from a responder gateway

            >>> await client.disassociate_certificate(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.disassociate_certificate_request.DisassociateCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.disassociate_certificate_response.DisassociateCertificateResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.disassociate_certificate

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.disassociate_certificate.async_disassociate_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.disassociate_certificate_request.DisassociateCertificateRequest = {
            "gateway_id": gateway_id,
            "acm_certificate_arn": acm_certificate_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_certificate_association(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "capo_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.get_certificate_association_response.GetCertificateAssociationResponse":
        """<p>Retrieves the details of a certificate association with a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get certificate association details from a responder gateway
            Retrieve details of an ACM certificate association with a responder gateway

            >>> await client.get_certificate_association(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.get_certificate_association_request.GetCertificateAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.get_certificate_association_response.GetCertificateAssociationResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.get_certificate_association

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.get_certificate_association.async_get_certificate_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.get_certificate_association_request.GetCertificateAssociationRequest = {
            "gateway_id": gateway_id,
            "acm_certificate_arn": acm_certificate_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_certificate_associations(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_rtbfabric.types.list_certificate_associations_response.ListCertificateAssociationsResponse":
        """<p>Lists the certificate associations for a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List certificate associations for a responder gateway
            Retrieve all certificate associations for a responder gateway

            >>> await client.list_certificate_associations(gateway_id='rtb-gw-12345678', max_results=5)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.list_certificate_associations_request.ListCertificateAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.list_certificate_associations_response.ListCertificateAssociationsResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.list_certificate_associations

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.list_certificate_associations.async_list_certificate_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.list_certificate_associations_request.ListCertificateAssociationsRequest = {
            "gateway_id": gateway_id
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

    async def update_responder_gateway(
        self,
        port: int,
        protocol: "capo_rtbfabric.types.protocol.Protocol",
        client_token: str,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        domain_name: Optional["capo_rtbfabric.types.domain_name.DomainName"] = None,
        listener_config: Optional[
            "capo_rtbfabric.types.listener_config.ListenerConfig"
        ] = None,
        trust_store_configuration: Optional[
            "capo_rtbfabric.types.trust_store_configuration.TrustStoreConfiguration"
        ] = None,
        managed_endpoint_configuration: Optional[
            "capo_rtbfabric.types.managed_endpoint_configuration.ManagedEndpointConfiguration"
        ] = None,
        description: Optional[str] = None,
        client_routing_policy: Optional[
            "capo_rtbfabric.types.client_routing_policy.ClientRoutingPolicy"
        ] = None,
    ) -> "capo_rtbfabric.types.update_responder_gateway_response.UpdateResponderGatewayResponse":
        """<p>Updates the description, Auto Scaling group managed endpoint configuration, trust store configuration, and client routing policy of a responder gateway. This operation also updates the <code>protocols</code> list in the listener configuration.</p> <p>You cannot change the <code>domainName</code>, <code>port</code>, and <code>protocol</code> values that you set when you create a responder gateway. To change any of them, delete the gateway and create a new one.</p>

        Args:
            domain_name: <p>Domain name for the responder gateway. This operation does not change the domain name of an existing gateway. To use a different domain name, delete the gateway and create a new one.</p>
            port: <p>Networking port to use. This operation does not change the port of an existing gateway. To use a different port, delete the gateway and create a new one.</p>
            protocol: <p>Networking protocol to use. This operation does not change the protocol of an existing gateway. To use a different protocol, delete the gateway and create a new one.</p>
            listener_config: <p>The listener configuration for the responder gateway.</p>
            trust_store_configuration: <p>The configuration of the trust store.</p>
            managed_endpoint_configuration: <p>The configuration for the managed endpoint.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            gateway_id: <p>The unique identifier of the gateway.</p>
            description: <p>An optional description for the responder gateway.</p>
            client_routing_policy: <p>The client routing policy of the gateway. This policy controls which Availability Zones RTB Fabric uses to reach the gateway for the requester gateways that send traffic to it. Valid values are the following:</p> <ul> <li> <p> <code>AVAILABILITY_ZONE_AFFINITY</code>: RTB Fabric routes each requester's traffic to gateway capacity in the requester's own Availability Zone when the gateway has capacity available there. Otherwise, RTB Fabric routes the traffic to gateway capacity in the other Availability Zones of the gateway.</p> </li> <li> <p> <code>ANY_AVAILABILITY_ZONE</code>: RTB Fabric routes each requester's traffic to gateway capacity in every Availability Zone that the subnets of the gateway span. The Availability Zone that the requester is in does not change this.</p> </li> </ul> <p>If you don't specify a value, the gateway keeps its current client routing policy. Changing the policy sets the gateway status to <code>PENDING_UPDATE</code> until the change is complete. RTB Fabric does not support partial Availability Zone affinity, so <code>PARTIAL_AVAILABILITY_ZONE_AFFINITY</code> is not a valid value. For more information, see <a href="https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-responder-gateways.html#configuring-availability-zone-affinity">Configuring Availability Zone affinity</a> in the <i>Amazon Web Services RTB Fabric User Guide</i>.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update responder gateway
            Update responder gateway

            >>> await client.update_responder_gateway(gateway_id='rtb-gw-12345678', description='Updated responder gateway description', port=8080, protocol='HTTP', client_token='12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.update_responder_gateway_request.UpdateResponderGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.update_responder_gateway_response.UpdateResponderGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.update_responder_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.update_responder_gateway.async_update_responder_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.update_responder_gateway_request.UpdateResponderGatewayRequest = {
            "port": port,
            "protocol": protocol,
            "client_token": client_token,
            "gateway_id": gateway_id,
        }
        if domain_name is not None:
            input_["domain_name"] = domain_name
        if listener_config is not None:
            input_["listener_config"] = listener_config
        if trust_store_configuration is not None:
            input_["trust_store_configuration"] = trust_store_configuration
        if managed_endpoint_configuration is not None:
            input_["managed_endpoint_configuration"] = managed_endpoint_configuration
        if description is not None:
            input_["description"] = description
        if client_routing_policy is not None:
            input_["client_routing_policy"] = client_routing_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
