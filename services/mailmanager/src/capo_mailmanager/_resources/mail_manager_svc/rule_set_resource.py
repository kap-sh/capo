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
    import capo_mailmanager.types.create_rule_set_request
    import capo_mailmanager.types.create_rule_set_response
    import capo_mailmanager.types.delete_rule_set_request
    import capo_mailmanager.types.delete_rule_set_response
    import capo_mailmanager.types.get_rule_set_request
    import capo_mailmanager.types.get_rule_set_response
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.list_rule_sets_request
    import capo_mailmanager.types.list_rule_sets_response
    import capo_mailmanager.types.page_size
    import capo_mailmanager.types.pagination_token
    import capo_mailmanager.types.rule_set
    import capo_mailmanager.types.rule_set_id
    import capo_mailmanager.types.rule_set_name
    import capo_mailmanager.types.rules
    import capo_mailmanager.types.tag_list
    import capo_mailmanager.types.update_rule_set_request
    import capo_mailmanager.types.update_rule_set_response
    from capo_mailmanager._services.async_mail_manager import (
        AsyncMailManagerClient,
        AsyncMailManagerClientConfig,
    )
    from capo_mailmanager._services.mail_manager import (
        MailManagerClient,
        MailManagerClientConfig,
    )


class RuleSetResource:
    def __init__(self, service: MailManagerClient) -> None:
        self._service = service

    def create(
        self,
        rule_set_name: "capo_mailmanager.types.rule_set_name.RuleSetName",
        rules: "capo_mailmanager.types.rules.Rules",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_rule_set_response.CreateRuleSetResponse":
        """<p>Provision a new rule set.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            rule_set_name: <p>A user-friendly name for the rule set.</p>
            rules: <p>Conditional rules that are evaluated for determining actions on email.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.create_rule_set_request.CreateRuleSetRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.create_rule_set_response.CreateRuleSetResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_rule_set

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.create_rule_set.create_rule_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_rule_set_request.CreateRuleSetRequest = {
            "rule_set_name": rule_set_name,
            "rules": rules,
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
        rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_rule_set_response.GetRuleSetResponse":
        """<p>Fetch attributes of a rule set.</p>

        Args:
            rule_set_id: <p>The identifier of an existing rule set to be retrieved.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.get_rule_set_request.GetRuleSetRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.get_rule_set_response.GetRuleSetResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_rule_set

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.get_rule_set.get_rule_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_rule_set_request.GetRuleSetRequest = {
            "rule_set_id": rule_set_id
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
        rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        rule_set_name: Optional[
            "capo_mailmanager.types.rule_set_name.RuleSetName"
        ] = None,
        rules: Optional["capo_mailmanager.types.rules.Rules"] = None,
    ) -> "capo_mailmanager.types.update_rule_set_response.UpdateRuleSetResponse":
        """<p>Update attributes of an already provisioned rule set.</p>

        Args:
            rule_set_id: <p>The identifier of a rule set you want to update.</p>
            rule_set_name: <p>A user-friendly name for the rule set resource.</p>
            rules: <p>A new set of rules to replace the current rules of the rule set—these rules will override all the rules of the rule set.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.update_rule_set_request.UpdateRuleSetRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.update_rule_set_response.UpdateRuleSetResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_rule_set

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.update_rule_set.update_rule_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_rule_set_request.UpdateRuleSetRequest = {
            "rule_set_id": rule_set_id
        }
        if rule_set_name is not None:
            input_["rule_set_name"] = rule_set_name
        if rules is not None:
            input_["rules"] = rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_rule_set_response.DeleteRuleSetResponse":
        """<p>Delete a rule set.</p>

        Args:
            rule_set_id: <p>The identifier of an existing rule set resource to delete.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.delete_rule_set_request.DeleteRuleSetRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.delete_rule_set_response.DeleteRuleSetResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_rule_set

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.delete_rule_set.delete_rule_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_rule_set_request.DeleteRuleSetRequest = {
            "rule_set_id": rule_set_id
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
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "capo_mailmanager.types.list_rule_sets_response.ListRuleSetsResponse":
        """<p>List rule sets for this account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of rule set resources that are returned per call. You can use NextToken to obtain further rule sets.</p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.list_rule_sets_request.ListRuleSetsRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.list_rule_sets_response.ListRuleSetsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_rule_sets

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.list_rule_sets.list_rule_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_rule_sets_request.ListRuleSetsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRuleSetResource:
    def __init__(self, service: AsyncMailManagerClient) -> None:
        self._service = service

    async def create(
        self,
        rule_set_name: "capo_mailmanager.types.rule_set_name.RuleSetName",
        rules: "capo_mailmanager.types.rules.Rules",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_rule_set_response.CreateRuleSetResponse":
        """<p>Provision a new rule set.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            rule_set_name: <p>A user-friendly name for the rule set.</p>
            rules: <p>Conditional rules that are evaluated for determining actions on email.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_rule_set_request.CreateRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_rule_set_response.CreateRuleSetResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_rule_set

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_rule_set.async_create_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_rule_set_request.CreateRuleSetRequest = {
            "rule_set_name": rule_set_name,
            "rules": rules,
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
        rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_rule_set_response.GetRuleSetResponse":
        """<p>Fetch attributes of a rule set.</p>

        Args:
            rule_set_id: <p>The identifier of an existing rule set to be retrieved.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_rule_set_request.GetRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_rule_set_response.GetRuleSetResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_rule_set

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_rule_set.async_get_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_rule_set_request.GetRuleSetRequest = {
            "rule_set_id": rule_set_id
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
        rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        rule_set_name: Optional[
            "capo_mailmanager.types.rule_set_name.RuleSetName"
        ] = None,
        rules: Optional["capo_mailmanager.types.rules.Rules"] = None,
    ) -> "capo_mailmanager.types.update_rule_set_response.UpdateRuleSetResponse":
        """<p>Update attributes of an already provisioned rule set.</p>

        Args:
            rule_set_id: <p>The identifier of a rule set you want to update.</p>
            rule_set_name: <p>A user-friendly name for the rule set resource.</p>
            rules: <p>A new set of rules to replace the current rules of the rule set—these rules will override all the rules of the rule set.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.update_rule_set_request.UpdateRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.update_rule_set_response.UpdateRuleSetResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_rule_set

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.update_rule_set.async_update_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_rule_set_request.UpdateRuleSetRequest = {
            "rule_set_id": rule_set_id
        }
        if rule_set_name is not None:
            input_["rule_set_name"] = rule_set_name
        if rules is not None:
            input_["rules"] = rules

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_rule_set_response.DeleteRuleSetResponse":
        """<p>Delete a rule set.</p>

        Args:
            rule_set_id: <p>The identifier of an existing rule set resource to delete.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_rule_set_request.DeleteRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_rule_set_response.DeleteRuleSetResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_rule_set

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_rule_set.async_delete_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_rule_set_request.DeleteRuleSetRequest = {
            "rule_set_id": rule_set_id
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
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "capo_mailmanager.types.list_rule_sets_response.ListRuleSetsResponse":
        """<p>List rule sets for this account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of rule set resources that are returned per call. You can use NextToken to obtain further rule sets.</p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_rule_sets_request.ListRuleSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_rule_sets_response.ListRuleSetsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_rule_sets

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_rule_sets.async_list_rule_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_rule_sets_request.ListRuleSetsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
