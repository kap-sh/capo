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
    import capo_mailmanager.types.accept_action
    import capo_mailmanager.types.create_traffic_policy_request
    import capo_mailmanager.types.create_traffic_policy_response
    import capo_mailmanager.types.delete_traffic_policy_request
    import capo_mailmanager.types.delete_traffic_policy_response
    import capo_mailmanager.types.get_traffic_policy_request
    import capo_mailmanager.types.get_traffic_policy_response
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.list_traffic_policies_request
    import capo_mailmanager.types.list_traffic_policies_response
    import capo_mailmanager.types.max_message_size_bytes
    import capo_mailmanager.types.page_size
    import capo_mailmanager.types.pagination_token
    import capo_mailmanager.types.policy_statement_list
    import capo_mailmanager.types.tag_list
    import capo_mailmanager.types.traffic_policy
    import capo_mailmanager.types.traffic_policy_id
    import capo_mailmanager.types.traffic_policy_name
    import capo_mailmanager.types.update_traffic_policy_request
    import capo_mailmanager.types.update_traffic_policy_response
    from capo_mailmanager._services.async_mail_manager import (
        AsyncMailManagerClient,
        AsyncMailManagerClientConfig,
    )
    from capo_mailmanager._services.mail_manager import (
        MailManagerClient,
        MailManagerClientConfig,
    )


class TrafficPolicyResource:
    def __init__(self, service: MailManagerClient) -> None:
        self._service = service

    def create(
        self,
        traffic_policy_name: "capo_mailmanager.types.traffic_policy_name.TrafficPolicyName",
        policy_statements: "capo_mailmanager.types.policy_statement_list.PolicyStatementList",
        default_action: "capo_mailmanager.types.accept_action.AcceptAction",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        max_message_size_bytes: Optional[
            "capo_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_traffic_policy_response.CreateTrafficPolicyResponse":
        """<p>Provision a new traffic policy resource.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            traffic_policy_name: <p>A user-friendly name for the traffic policy resource.</p>
            policy_statements: <p>Conditional statements for filtering email traffic.</p>
            default_action: <p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>
            max_message_size_bytes: <p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create TrafficPolicy

            >>> client.create(traffic_policy_name='trafficPolicyName', policy_statements=[{'Conditions': [{'IpExpression': {'Evaluate': {'Attribute': 'SENDER_IP'}, 'Operator': 'CIDR_MATCHES', 'Values': ['0.0.0.0/12']}}], 'Action': 'ALLOW'}], default_action='DENY')
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.create_traffic_policy_request.CreateTrafficPolicyRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.create_traffic_policy_response.CreateTrafficPolicyResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_traffic_policy

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.create_traffic_policy.create_traffic_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_traffic_policy_request.CreateTrafficPolicyRequest = {
            "traffic_policy_name": traffic_policy_name,
            "policy_statements": policy_statements,
            "default_action": default_action,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if max_message_size_bytes is not None:
            input_["max_message_size_bytes"] = max_message_size_bytes
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
        traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_traffic_policy_response.GetTrafficPolicyResponse":
        """<p>Fetch attributes of a traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy resource.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get TrafficPolicy

            >>> client.read(traffic_policy_id='tp-12345')
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.get_traffic_policy_request.GetTrafficPolicyRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.get_traffic_policy_response.GetTrafficPolicyResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_traffic_policy

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.get_traffic_policy.get_traffic_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_traffic_policy_request.GetTrafficPolicyRequest = {
            "traffic_policy_id": traffic_policy_id
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
        traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        traffic_policy_name: Optional[
            "capo_mailmanager.types.traffic_policy_name.TrafficPolicyName"
        ] = None,
        policy_statements: Optional[
            "capo_mailmanager.types.policy_statement_list.PolicyStatementList"
        ] = None,
        default_action: Optional[
            "capo_mailmanager.types.accept_action.AcceptAction"
        ] = None,
        max_message_size_bytes: Optional[
            "capo_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
        ] = None,
    ) -> "capo_mailmanager.types.update_traffic_policy_response.UpdateTrafficPolicyResponse":
        """<p>Update attributes of an already provisioned traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy that you want to update.</p>
            traffic_policy_name: <p>A user-friendly name for the traffic policy resource.</p>
            policy_statements: <p>The list of conditions to be updated for filtering email traffic.</p>
            default_action: <p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>
            max_message_size_bytes: <p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update TrafficPolicy with new Name

            >>> client.update(traffic_policy_id='tp-12345', traffic_policy_name='trafficPolicyNewName')
            Update TrafficPolicy with new PolicyStatements

            >>> client.update(traffic_policy_id='tp-12345', policy_statements=[{'Conditions': [{'StringExpression': {'Evaluate': {'Attribute': 'RECIPIENT'}, 'Operator': 'EQUALS', 'Values': ['example@amazon.com', 'example@gmail.com']}}], 'Action': 'ALLOW'}])
            Update TrafficPolicy with new DefaultAction

            >>> client.update(traffic_policy_id='tp-12345', default_action='ALLOW')
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.update_traffic_policy_request.UpdateTrafficPolicyRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.update_traffic_policy_response.UpdateTrafficPolicyResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_traffic_policy

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.update_traffic_policy.update_traffic_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_traffic_policy_request.UpdateTrafficPolicyRequest = {
            "traffic_policy_id": traffic_policy_id
        }
        if traffic_policy_name is not None:
            input_["traffic_policy_name"] = traffic_policy_name
        if policy_statements is not None:
            input_["policy_statements"] = policy_statements
        if default_action is not None:
            input_["default_action"] = default_action
        if max_message_size_bytes is not None:
            input_["max_message_size_bytes"] = max_message_size_bytes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_traffic_policy_response.DeleteTrafficPolicyResponse":
        """<p>Delete a traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy that you want to delete.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete TrafficPolicy

            >>> client.delete(traffic_policy_id='tp-12345')
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.delete_traffic_policy_request.DeleteTrafficPolicyRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.delete_traffic_policy_response.DeleteTrafficPolicyResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_traffic_policy

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.delete_traffic_policy.delete_traffic_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_traffic_policy_request.DeleteTrafficPolicyRequest = {
            "traffic_policy_id": traffic_policy_id
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
    ) -> "capo_mailmanager.types.list_traffic_policies_response.ListTrafficPoliciesResponse":
        """<p>List traffic policy resources.</p>

        Args:
            page_size: <p>The maximum number of traffic policy resources that are returned per call. You can use NextToken to obtain further traffic policies.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List TrafficPolicies

            >>> client.list()
            List TrafficPolicies with PageSize

            >>> client.list(page_size=10)
            List TrafficPolicies with NextToken

            >>> client.list(next_token='nextToken')
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.list_traffic_policies_request.ListTrafficPoliciesRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.list_traffic_policies_response.ListTrafficPoliciesResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_traffic_policies

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.list_traffic_policies.list_traffic_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_traffic_policies_request.ListTrafficPoliciesRequest = {}
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


class AsyncTrafficPolicyResource:
    def __init__(self, service: AsyncMailManagerClient) -> None:
        self._service = service

    async def create(
        self,
        traffic_policy_name: "capo_mailmanager.types.traffic_policy_name.TrafficPolicyName",
        policy_statements: "capo_mailmanager.types.policy_statement_list.PolicyStatementList",
        default_action: "capo_mailmanager.types.accept_action.AcceptAction",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        max_message_size_bytes: Optional[
            "capo_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_traffic_policy_response.CreateTrafficPolicyResponse":
        """<p>Provision a new traffic policy resource.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            traffic_policy_name: <p>A user-friendly name for the traffic policy resource.</p>
            policy_statements: <p>Conditional statements for filtering email traffic.</p>
            default_action: <p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>
            max_message_size_bytes: <p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create TrafficPolicy

            >>> await client.create(traffic_policy_name='trafficPolicyName', policy_statements=[{'Conditions': [{'IpExpression': {'Evaluate': {'Attribute': 'SENDER_IP'}, 'Operator': 'CIDR_MATCHES', 'Values': ['0.0.0.0/12']}}], 'Action': 'ALLOW'}], default_action='DENY')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_traffic_policy_request.CreateTrafficPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_traffic_policy_response.CreateTrafficPolicyResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_traffic_policy

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_traffic_policy.async_create_traffic_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_traffic_policy_request.CreateTrafficPolicyRequest = {
            "traffic_policy_name": traffic_policy_name,
            "policy_statements": policy_statements,
            "default_action": default_action,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if max_message_size_bytes is not None:
            input_["max_message_size_bytes"] = max_message_size_bytes
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
        traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_traffic_policy_response.GetTrafficPolicyResponse":
        """<p>Fetch attributes of a traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy resource.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get TrafficPolicy

            >>> await client.read(traffic_policy_id='tp-12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_traffic_policy_request.GetTrafficPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_traffic_policy_response.GetTrafficPolicyResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_traffic_policy

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_traffic_policy.async_get_traffic_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_traffic_policy_request.GetTrafficPolicyRequest = {
            "traffic_policy_id": traffic_policy_id
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
        traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        traffic_policy_name: Optional[
            "capo_mailmanager.types.traffic_policy_name.TrafficPolicyName"
        ] = None,
        policy_statements: Optional[
            "capo_mailmanager.types.policy_statement_list.PolicyStatementList"
        ] = None,
        default_action: Optional[
            "capo_mailmanager.types.accept_action.AcceptAction"
        ] = None,
        max_message_size_bytes: Optional[
            "capo_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
        ] = None,
    ) -> "capo_mailmanager.types.update_traffic_policy_response.UpdateTrafficPolicyResponse":
        """<p>Update attributes of an already provisioned traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy that you want to update.</p>
            traffic_policy_name: <p>A user-friendly name for the traffic policy resource.</p>
            policy_statements: <p>The list of conditions to be updated for filtering email traffic.</p>
            default_action: <p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>
            max_message_size_bytes: <p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update TrafficPolicy with new Name

            >>> await client.update(traffic_policy_id='tp-12345', traffic_policy_name='trafficPolicyNewName')
            Update TrafficPolicy with new PolicyStatements

            >>> await client.update(traffic_policy_id='tp-12345', policy_statements=[{'Conditions': [{'StringExpression': {'Evaluate': {'Attribute': 'RECIPIENT'}, 'Operator': 'EQUALS', 'Values': ['example@amazon.com', 'example@gmail.com']}}], 'Action': 'ALLOW'}])
            Update TrafficPolicy with new DefaultAction

            >>> await client.update(traffic_policy_id='tp-12345', default_action='ALLOW')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.update_traffic_policy_request.UpdateTrafficPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.update_traffic_policy_response.UpdateTrafficPolicyResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_traffic_policy

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.update_traffic_policy.async_update_traffic_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_traffic_policy_request.UpdateTrafficPolicyRequest = {
            "traffic_policy_id": traffic_policy_id
        }
        if traffic_policy_name is not None:
            input_["traffic_policy_name"] = traffic_policy_name
        if policy_statements is not None:
            input_["policy_statements"] = policy_statements
        if default_action is not None:
            input_["default_action"] = default_action
        if max_message_size_bytes is not None:
            input_["max_message_size_bytes"] = max_message_size_bytes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_traffic_policy_response.DeleteTrafficPolicyResponse":
        """<p>Delete a traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy that you want to delete.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete TrafficPolicy

            >>> await client.delete(traffic_policy_id='tp-12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_traffic_policy_request.DeleteTrafficPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_traffic_policy_response.DeleteTrafficPolicyResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_traffic_policy

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_traffic_policy.async_delete_traffic_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_traffic_policy_request.DeleteTrafficPolicyRequest = {
            "traffic_policy_id": traffic_policy_id
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
    ) -> "capo_mailmanager.types.list_traffic_policies_response.ListTrafficPoliciesResponse":
        """<p>List traffic policy resources.</p>

        Args:
            page_size: <p>The maximum number of traffic policy resources that are returned per call. You can use NextToken to obtain further traffic policies.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List TrafficPolicies

            >>> await client.list()
            List TrafficPolicies with PageSize

            >>> await client.list(page_size=10)
            List TrafficPolicies with NextToken

            >>> await client.list(next_token='nextToken')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_traffic_policies_request.ListTrafficPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_traffic_policies_response.ListTrafficPoliciesResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_traffic_policies

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_traffic_policies.async_list_traffic_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_traffic_policies_request.ListTrafficPoliciesRequest = {}
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
