from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_mailmanager._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mailmanager.types.create_ingress_point_request
    import capo_mailmanager.types.create_ingress_point_response
    import capo_mailmanager.types.delete_ingress_point_request
    import capo_mailmanager.types.delete_ingress_point_response
    import capo_mailmanager.types.get_ingress_point_request
    import capo_mailmanager.types.get_ingress_point_response
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.ingress_point
    import capo_mailmanager.types.ingress_point_configuration
    import capo_mailmanager.types.ingress_point_id
    import capo_mailmanager.types.ingress_point_name
    import capo_mailmanager.types.ingress_point_status_to_update
    import capo_mailmanager.types.ingress_point_type
    import capo_mailmanager.types.list_ingress_points_request
    import capo_mailmanager.types.list_ingress_points_response
    import capo_mailmanager.types.network_configuration
    import capo_mailmanager.types.page_size
    import capo_mailmanager.types.pagination_token
    import capo_mailmanager.types.rule_set_id
    import capo_mailmanager.types.tag_list
    import capo_mailmanager.types.tls_policy
    import capo_mailmanager.types.traffic_policy_id
    import capo_mailmanager.types.trust_store_response_option
    import capo_mailmanager.types.update_ingress_point_request
    import capo_mailmanager.types.update_ingress_point_response
    from capo_mailmanager._services.async_mail_manager import (
        AsyncMailManagerClient,
        AsyncMailManagerClientConfig,
    )
    from capo_mailmanager._services.mail_manager import (
        MailManagerClient,
        MailManagerClientConfig,
    )


class IngressPointResource:
    def __init__(self, service: MailManagerClient) -> None:
        self._service = service

    def create(
        self,
        ingress_point_name: "capo_mailmanager.types.ingress_point_name.IngressPointName",
        type: "capo_mailmanager.types.ingress_point_type.IngressPointType",
        rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId",
        traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        ingress_point_configuration: Optional[
            "capo_mailmanager.types.ingress_point_configuration.IngressPointConfiguration"
        ] = None,
        network_configuration: Optional[
            "capo_mailmanager.types.network_configuration.NetworkConfiguration"
        ] = None,
        tls_policy: Optional["capo_mailmanager.types.tls_policy.TlsPolicy"] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_ingress_point_response.CreateIngressPointResponse":
        """<p>Provision a new ingress endpoint resource.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            ingress_point_name: <p>A user friendly name for an ingress endpoint resource.</p>
            type: <p>The type of the ingress endpoint to create.</p>
            rule_set_id: <p>The identifier of an existing rule set that you attach to an ingress endpoint resource.</p>
            traffic_policy_id: <p>The identifier of an existing traffic policy that you attach to an ingress endpoint resource.</p>
            ingress_point_configuration: <p>If you choose an Authenticated ingress endpoint, you must configure either an SMTP password or a secret ARN.</p>
            network_configuration: <p>Specifies the network configuration for the ingress point. This allows you to create an IPv4-only, Dual-Stack, or PrivateLink type of ingress point. If not specified, the default network type is IPv4-only. </p>
            tls_policy: <p>The Transport Layer Security (TLS) policy for the ingress point. The FIPS value is only valid in US and Canada regions.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create Open IngressPoint

            >>> client.create(ingress_point_name='ingressPointName', type='OPEN', rule_set_id='rs-12345', traffic_policy_id='tp-12345', tags=[{'Key': 'key', 'Value': 'value'}])
            Create Auth IngressPoint with Password

            >>> client.create(ingress_point_name='ingressPointName', type='AUTH', rule_set_id='rs-12345', traffic_policy_id='tp-12345', ingress_point_configuration={'SmtpPassword': 'smtpPassword'}, tags=[{'Key': 'key', 'Value': 'value'}])
            Create Auth IngressPoint with SecretsManager Secret

            >>> client.create(ingress_point_name='ingressPointName', type='AUTH', rule_set_id='rs-12345', traffic_policy_id='tp-12345', ingress_point_configuration={'SecretArn': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:abcde'}, tags=[{'Key': 'key', 'Value': 'value'}])
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.create_ingress_point_request.CreateIngressPointRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.create_ingress_point_response.CreateIngressPointResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_ingress_point

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.create_ingress_point.create_ingress_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_ingress_point_request.CreateIngressPointRequest = {
            "ingress_point_name": ingress_point_name,
            "type": type,
            "rule_set_id": rule_set_id,
            "traffic_policy_id": traffic_policy_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if ingress_point_configuration is not None:
            input_["ingress_point_configuration"] = ingress_point_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if tls_policy is not None:
            input_["tls_policy"] = tls_policy
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
        ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        include_trust_store_contents: Optional[
            "capo_mailmanager.types.trust_store_response_option.TrustStoreResponseOption"
        ] = None,
    ) -> "capo_mailmanager.types.get_ingress_point_response.GetIngressPointResponse":
        """<p>Fetch ingress endpoint resource attributes.</p>

        Args:
            ingress_point_id: <p>The identifier of an ingress endpoint.</p>
            include_trust_store_contents: <p>Whether to include the trust store contents in the response. Use INCLUDE to retrieve trust store certificate and CRL contents.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get Open IngressPoint

            >>> client.read(ingress_point_id='inp-12345')
            Get Auth IngressPoint

            >>> client.read(ingress_point_id='inp-12345')
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.get_ingress_point_request.GetIngressPointRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.get_ingress_point_response.GetIngressPointResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_ingress_point

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.get_ingress_point.get_ingress_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_ingress_point_request.GetIngressPointRequest = {
            "ingress_point_id": ingress_point_id
        }
        if include_trust_store_contents is not None:
            input_["include_trust_store_contents"] = include_trust_store_contents

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        ingress_point_name: Optional[
            "capo_mailmanager.types.ingress_point_name.IngressPointName"
        ] = None,
        status_to_update: Optional[
            "capo_mailmanager.types.ingress_point_status_to_update.IngressPointStatusToUpdate"
        ] = None,
        rule_set_id: Optional["capo_mailmanager.types.rule_set_id.RuleSetId"] = None,
        traffic_policy_id: Optional[
            "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId"
        ] = None,
        ingress_point_configuration: Optional[
            "capo_mailmanager.types.ingress_point_configuration.IngressPointConfiguration"
        ] = None,
        tls_policy: Optional["capo_mailmanager.types.tls_policy.TlsPolicy"] = None,
    ) -> "capo_mailmanager.types.update_ingress_point_response.UpdateIngressPointResponse":
        """<p>Update attributes of a provisioned ingress endpoint resource.</p>

        Args:
            ingress_point_id: <p>The identifier for the ingress endpoint you want to update.</p>
            ingress_point_name: <p>A user friendly name for the ingress endpoint resource.</p>
            status_to_update: <p>The update status of an ingress endpoint.</p>
            rule_set_id: <p>The identifier of an existing rule set that you attach to an ingress endpoint resource.</p>
            traffic_policy_id: <p>The identifier of an existing traffic policy that you attach to an ingress endpoint resource.</p>
            ingress_point_configuration: <p>If you choose an Authenticated ingress endpoint, you must configure either an SMTP password or a secret ARN.</p>
            tls_policy: <p>The Transport Layer Security (TLS) policy for the ingress point. Valid values are REQUIRED, OPTIONAL. Only ingress endpoints using REQUIRED or OPTIONAL as TlsPolicy can be updated.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update Open/Auth IngressPoint with new Name

            >>> client.update(ingress_point_id='inp-12345', ingress_point_name='ingressPointNewName')
            Update Open/Auth IngressPoint with new RuleSetId / TrafficPolicyId

            >>> client.update(ingress_point_id='inp-12345', rule_set_id='rs-12345', traffic_policy_id='tp-12345')
            Update Auth IngressPoint with new SmtpPassword

            >>> client.update(ingress_point_id='inp-12345', ingress_point_configuration={'SmtpPassword': 'newSmtpPassword'})
            Update Auth IngressPoint with new SecretArn

            >>> client.update(ingress_point_id='inp-12345', ingress_point_configuration={'SecretArn': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:abcde'})
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.update_ingress_point_request.UpdateIngressPointRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.update_ingress_point_response.UpdateIngressPointResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_ingress_point

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.update_ingress_point.update_ingress_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_ingress_point_request.UpdateIngressPointRequest = {
            "ingress_point_id": ingress_point_id
        }
        if ingress_point_name is not None:
            input_["ingress_point_name"] = ingress_point_name
        if status_to_update is not None:
            input_["status_to_update"] = status_to_update
        if rule_set_id is not None:
            input_["rule_set_id"] = rule_set_id
        if traffic_policy_id is not None:
            input_["traffic_policy_id"] = traffic_policy_id
        if ingress_point_configuration is not None:
            input_["ingress_point_configuration"] = ingress_point_configuration
        if tls_policy is not None:
            input_["tls_policy"] = tls_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_ingress_point_response.DeleteIngressPointResponse":
        """<p>Delete an ingress endpoint resource.</p>

        Args:
            ingress_point_id: <p>The identifier of the ingress endpoint resource that you want to delete.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete IngressPoint

            >>> client.delete(ingress_point_id='inp-12345')
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.delete_ingress_point_request.DeleteIngressPointRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.delete_ingress_point_response.DeleteIngressPointResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_ingress_point

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.delete_ingress_point.delete_ingress_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_ingress_point_request.DeleteIngressPointRequest = {
            "ingress_point_id": ingress_point_id
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
        config_overrides: Optional[MailManagerClientConfig] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "capo_mailmanager.types.list_ingress_points_response.ListIngressPointsResponse"
    ):
        """<p>List all ingress endpoint resources.</p>

        Args:
            page_size: <p>The maximum number of ingress endpoint resources that are returned per call. You can use NextToken to obtain further ingress endpoints.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List IngressPoints

            >>> client.list()
            List IngressPoints with PageSize

            >>> client.list(page_size=10)
            List IngressPoints with NextToken

            >>> client.list(next_token='nextToken')
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.list_ingress_points_request.ListIngressPointsRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.list_ingress_points_response.ListIngressPointsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_ingress_points

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.list_ingress_points.list_ingress_points(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_ingress_points_request.ListIngressPointsRequest = {}
        if page_size is not None:
            input_["page_size"] = page_size
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncIngressPointResource:
    def __init__(self, service: AsyncMailManagerClient) -> None:
        self._service = service

    async def create(
        self,
        ingress_point_name: "capo_mailmanager.types.ingress_point_name.IngressPointName",
        type: "capo_mailmanager.types.ingress_point_type.IngressPointType",
        rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId",
        traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        ingress_point_configuration: Optional[
            "capo_mailmanager.types.ingress_point_configuration.IngressPointConfiguration"
        ] = None,
        network_configuration: Optional[
            "capo_mailmanager.types.network_configuration.NetworkConfiguration"
        ] = None,
        tls_policy: Optional["capo_mailmanager.types.tls_policy.TlsPolicy"] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_ingress_point_response.CreateIngressPointResponse":
        """<p>Provision a new ingress endpoint resource.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            ingress_point_name: <p>A user friendly name for an ingress endpoint resource.</p>
            type: <p>The type of the ingress endpoint to create.</p>
            rule_set_id: <p>The identifier of an existing rule set that you attach to an ingress endpoint resource.</p>
            traffic_policy_id: <p>The identifier of an existing traffic policy that you attach to an ingress endpoint resource.</p>
            ingress_point_configuration: <p>If you choose an Authenticated ingress endpoint, you must configure either an SMTP password or a secret ARN.</p>
            network_configuration: <p>Specifies the network configuration for the ingress point. This allows you to create an IPv4-only, Dual-Stack, or PrivateLink type of ingress point. If not specified, the default network type is IPv4-only. </p>
            tls_policy: <p>The Transport Layer Security (TLS) policy for the ingress point. The FIPS value is only valid in US and Canada regions.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create Open IngressPoint

            >>> await client.create(ingress_point_name='ingressPointName', type='OPEN', rule_set_id='rs-12345', traffic_policy_id='tp-12345', tags=[{'Key': 'key', 'Value': 'value'}])
            Create Auth IngressPoint with Password

            >>> await client.create(ingress_point_name='ingressPointName', type='AUTH', rule_set_id='rs-12345', traffic_policy_id='tp-12345', ingress_point_configuration={'SmtpPassword': 'smtpPassword'}, tags=[{'Key': 'key', 'Value': 'value'}])
            Create Auth IngressPoint with SecretsManager Secret

            >>> await client.create(ingress_point_name='ingressPointName', type='AUTH', rule_set_id='rs-12345', traffic_policy_id='tp-12345', ingress_point_configuration={'SecretArn': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:abcde'}, tags=[{'Key': 'key', 'Value': 'value'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_ingress_point_request.CreateIngressPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_ingress_point_response.CreateIngressPointResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_ingress_point

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_ingress_point.async_create_ingress_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_ingress_point_request.CreateIngressPointRequest = {
            "ingress_point_name": ingress_point_name,
            "type": type,
            "rule_set_id": rule_set_id,
            "traffic_policy_id": traffic_policy_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if ingress_point_configuration is not None:
            input_["ingress_point_configuration"] = ingress_point_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if tls_policy is not None:
            input_["tls_policy"] = tls_policy
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
        ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        include_trust_store_contents: Optional[
            "capo_mailmanager.types.trust_store_response_option.TrustStoreResponseOption"
        ] = None,
    ) -> "capo_mailmanager.types.get_ingress_point_response.GetIngressPointResponse":
        """<p>Fetch ingress endpoint resource attributes.</p>

        Args:
            ingress_point_id: <p>The identifier of an ingress endpoint.</p>
            include_trust_store_contents: <p>Whether to include the trust store contents in the response. Use INCLUDE to retrieve trust store certificate and CRL contents.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get Open IngressPoint

            >>> await client.read(ingress_point_id='inp-12345')
            Get Auth IngressPoint

            >>> await client.read(ingress_point_id='inp-12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_ingress_point_request.GetIngressPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_ingress_point_response.GetIngressPointResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_ingress_point

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_ingress_point.async_get_ingress_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_ingress_point_request.GetIngressPointRequest = {
            "ingress_point_id": ingress_point_id
        }
        if include_trust_store_contents is not None:
            input_["include_trust_store_contents"] = include_trust_store_contents

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        ingress_point_name: Optional[
            "capo_mailmanager.types.ingress_point_name.IngressPointName"
        ] = None,
        status_to_update: Optional[
            "capo_mailmanager.types.ingress_point_status_to_update.IngressPointStatusToUpdate"
        ] = None,
        rule_set_id: Optional["capo_mailmanager.types.rule_set_id.RuleSetId"] = None,
        traffic_policy_id: Optional[
            "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId"
        ] = None,
        ingress_point_configuration: Optional[
            "capo_mailmanager.types.ingress_point_configuration.IngressPointConfiguration"
        ] = None,
        tls_policy: Optional["capo_mailmanager.types.tls_policy.TlsPolicy"] = None,
    ) -> "capo_mailmanager.types.update_ingress_point_response.UpdateIngressPointResponse":
        """<p>Update attributes of a provisioned ingress endpoint resource.</p>

        Args:
            ingress_point_id: <p>The identifier for the ingress endpoint you want to update.</p>
            ingress_point_name: <p>A user friendly name for the ingress endpoint resource.</p>
            status_to_update: <p>The update status of an ingress endpoint.</p>
            rule_set_id: <p>The identifier of an existing rule set that you attach to an ingress endpoint resource.</p>
            traffic_policy_id: <p>The identifier of an existing traffic policy that you attach to an ingress endpoint resource.</p>
            ingress_point_configuration: <p>If you choose an Authenticated ingress endpoint, you must configure either an SMTP password or a secret ARN.</p>
            tls_policy: <p>The Transport Layer Security (TLS) policy for the ingress point. Valid values are REQUIRED, OPTIONAL. Only ingress endpoints using REQUIRED or OPTIONAL as TlsPolicy can be updated.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update Open/Auth IngressPoint with new Name

            >>> await client.update(ingress_point_id='inp-12345', ingress_point_name='ingressPointNewName')
            Update Open/Auth IngressPoint with new RuleSetId / TrafficPolicyId

            >>> await client.update(ingress_point_id='inp-12345', rule_set_id='rs-12345', traffic_policy_id='tp-12345')
            Update Auth IngressPoint with new SmtpPassword

            >>> await client.update(ingress_point_id='inp-12345', ingress_point_configuration={'SmtpPassword': 'newSmtpPassword'})
            Update Auth IngressPoint with new SecretArn

            >>> await client.update(ingress_point_id='inp-12345', ingress_point_configuration={'SecretArn': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:abcde'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.update_ingress_point_request.UpdateIngressPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.update_ingress_point_response.UpdateIngressPointResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_ingress_point

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.update_ingress_point.async_update_ingress_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_ingress_point_request.UpdateIngressPointRequest = {
            "ingress_point_id": ingress_point_id
        }
        if ingress_point_name is not None:
            input_["ingress_point_name"] = ingress_point_name
        if status_to_update is not None:
            input_["status_to_update"] = status_to_update
        if rule_set_id is not None:
            input_["rule_set_id"] = rule_set_id
        if traffic_policy_id is not None:
            input_["traffic_policy_id"] = traffic_policy_id
        if ingress_point_configuration is not None:
            input_["ingress_point_configuration"] = ingress_point_configuration
        if tls_policy is not None:
            input_["tls_policy"] = tls_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_ingress_point_response.DeleteIngressPointResponse":
        """<p>Delete an ingress endpoint resource.</p>

        Args:
            ingress_point_id: <p>The identifier of the ingress endpoint resource that you want to delete.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete IngressPoint

            >>> await client.delete(ingress_point_id='inp-12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_ingress_point_request.DeleteIngressPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_ingress_point_response.DeleteIngressPointResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_ingress_point

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_ingress_point.async_delete_ingress_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_ingress_point_request.DeleteIngressPointRequest = {
            "ingress_point_id": ingress_point_id
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
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "capo_mailmanager.types.list_ingress_points_response.ListIngressPointsResponse"
    ):
        """<p>List all ingress endpoint resources.</p>

        Args:
            page_size: <p>The maximum number of ingress endpoint resources that are returned per call. You can use NextToken to obtain further ingress endpoints.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List IngressPoints

            >>> await client.list()
            List IngressPoints with PageSize

            >>> await client.list(page_size=10)
            List IngressPoints with NextToken

            >>> await client.list(next_token='nextToken')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_ingress_points_request.ListIngressPointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_ingress_points_response.ListIngressPointsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_ingress_points

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_ingress_points.async_list_ingress_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_ingress_points_request.ListIngressPointsRequest = {}
        if page_size is not None:
            input_["page_size"] = page_size
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
