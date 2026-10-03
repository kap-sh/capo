from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_connectcases._auth._signers
import capo_connectcases._auth._sigv4
from capo_connectcases._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_connectcases.types.batch_get_case_rule_request
    import capo_connectcases.types.batch_get_case_rule_response
    import capo_connectcases.types.case_rule_description
    import capo_connectcases.types.case_rule_details
    import capo_connectcases.types.case_rule_id
    import capo_connectcases.types.case_rule_identifier_list
    import capo_connectcases.types.case_rule_name
    import capo_connectcases.types.case_rule_summary
    import capo_connectcases.types.create_case_rule_request
    import capo_connectcases.types.create_case_rule_response
    import capo_connectcases.types.delete_case_rule_request
    import capo_connectcases.types.delete_case_rule_response
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.list_case_rules_request
    import capo_connectcases.types.list_case_rules_response
    import capo_connectcases.types.max_results
    import capo_connectcases.types.next_token
    import capo_connectcases.types.update_case_rule_request
    import capo_connectcases.types.update_case_rule_response
    from capo_connectcases._services.async_connect_cases import (
        AsyncConnectCasesClient,
        AsyncConnectCasesClientConfig,
    )
    from capo_connectcases._services.connect_cases import (
        ConnectCasesClient,
        ConnectCasesClientConfig,
    )


class CaseRule:
    def __init__(self, service: ConnectCasesClient) -> None:
        self._service = service

    def create(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        name: "capo_connectcases.types.case_rule_name.CaseRuleName",
        rule: "capo_connectcases.types.case_rule_details.CaseRuleDetails",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        description: Optional[
            "capo_connectcases.types.case_rule_description.CaseRuleDescription"
        ] = None,
    ) -> "capo_connectcases.types.create_case_rule_response.CreateCaseRuleResponse":
        """<p>Creates a new case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            name: <p>Name of the case rule.</p>
            description: <p>The description of a case rule.</p>
            rule: <p>Represents what rule type should take place, under what conditions.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.create_case_rule_request.CreateCaseRuleRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.create_case_rule_response.CreateCaseRuleResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_case_rule

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.create_case_rule.create_case_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.create_case_rule_request.CreateCaseRuleRequest = {
            "domain_id": domain_id,
            "name": name,
            "rule": rule,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_rule_id: "capo_connectcases.types.case_rule_id.CaseRuleId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        name: Optional["capo_connectcases.types.case_rule_name.CaseRuleName"] = None,
        description: Optional[
            "capo_connectcases.types.case_rule_description.CaseRuleDescription"
        ] = None,
        rule: Optional[
            "capo_connectcases.types.case_rule_details.CaseRuleDetails"
        ] = None,
    ) -> "capo_connectcases.types.update_case_rule_response.UpdateCaseRuleResponse":
        """<p>Updates a case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rule_id: <p>Unique identifier of a case rule.</p>
            name: <p>Name of the case rule.</p>
            description: <p>Description of a case rule.</p>
            rule: <p>Represents what rule type should take place, under what conditions.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.update_case_rule_request.UpdateCaseRuleRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.update_case_rule_response.UpdateCaseRuleResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.update_case_rule

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.update_case_rule.update_case_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.update_case_rule_request.UpdateCaseRuleRequest = {
            "domain_id": domain_id,
            "case_rule_id": case_rule_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if rule is not None:
            input_["rule"] = rule

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_rule_id: "capo_connectcases.types.case_rule_id.CaseRuleId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_case_rule_response.DeleteCaseRuleResponse":
        """<p>Deletes a case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rule_id: <p>Unique identifier of a case rule.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.delete_case_rule_request.DeleteCaseRuleRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.delete_case_rule_response.DeleteCaseRuleResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_case_rule

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.delete_case_rule.delete_case_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_case_rule_request.DeleteCaseRuleRequest = {
            "domain_id": domain_id,
            "case_rule_id": case_rule_id,
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
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.list_case_rules_response.ListCaseRulesResponse":
        """<p>Lists all case rules in a Cases domain. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.list_case_rules_request.ListCaseRulesRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.list_case_rules_response.ListCaseRulesResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_case_rules

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.list_case_rules.list_case_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.list_case_rules_request.ListCaseRulesRequest = {
            "domain_id": domain_id
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

    def batch_get_case_rule(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_rules: "capo_connectcases.types.case_rule_identifier_list.CaseRuleIdentifierList",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> (
        "capo_connectcases.types.batch_get_case_rule_response.BatchGetCaseRuleResponse"
    ):
        """<p>Gets a batch of case rules. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rules: <p>A list of case rule identifiers.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.batch_get_case_rule_request.BatchGetCaseRuleRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.batch_get_case_rule_response.BatchGetCaseRuleResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.batch_get_case_rule

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.batch_get_case_rule.batch_get_case_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.batch_get_case_rule_request.BatchGetCaseRuleRequest = {
            "domain_id": domain_id,
            "case_rules": case_rules,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCaseRule:
    def __init__(self, service: AsyncConnectCasesClient) -> None:
        self._service = service

    async def create(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        name: "capo_connectcases.types.case_rule_name.CaseRuleName",
        rule: "capo_connectcases.types.case_rule_details.CaseRuleDetails",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        description: Optional[
            "capo_connectcases.types.case_rule_description.CaseRuleDescription"
        ] = None,
    ) -> "capo_connectcases.types.create_case_rule_response.CreateCaseRuleResponse":
        """<p>Creates a new case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            name: <p>Name of the case rule.</p>
            description: <p>The description of a case rule.</p>
            rule: <p>Represents what rule type should take place, under what conditions.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.create_case_rule_request.CreateCaseRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.create_case_rule_response.CreateCaseRuleResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_case_rule

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.create_case_rule.async_create_case_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.create_case_rule_request.CreateCaseRuleRequest = {
            "domain_id": domain_id,
            "name": name,
            "rule": rule,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_rule_id: "capo_connectcases.types.case_rule_id.CaseRuleId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        name: Optional["capo_connectcases.types.case_rule_name.CaseRuleName"] = None,
        description: Optional[
            "capo_connectcases.types.case_rule_description.CaseRuleDescription"
        ] = None,
        rule: Optional[
            "capo_connectcases.types.case_rule_details.CaseRuleDetails"
        ] = None,
    ) -> "capo_connectcases.types.update_case_rule_response.UpdateCaseRuleResponse":
        """<p>Updates a case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rule_id: <p>Unique identifier of a case rule.</p>
            name: <p>Name of the case rule.</p>
            description: <p>Description of a case rule.</p>
            rule: <p>Represents what rule type should take place, under what conditions.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.update_case_rule_request.UpdateCaseRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.update_case_rule_response.UpdateCaseRuleResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.update_case_rule

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.update_case_rule.async_update_case_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.update_case_rule_request.UpdateCaseRuleRequest = {
            "domain_id": domain_id,
            "case_rule_id": case_rule_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if rule is not None:
            input_["rule"] = rule

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_rule_id: "capo_connectcases.types.case_rule_id.CaseRuleId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_case_rule_response.DeleteCaseRuleResponse":
        """<p>Deletes a case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rule_id: <p>Unique identifier of a case rule.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.delete_case_rule_request.DeleteCaseRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.delete_case_rule_response.DeleteCaseRuleResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_case_rule

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.delete_case_rule.async_delete_case_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_case_rule_request.DeleteCaseRuleRequest = {
            "domain_id": domain_id,
            "case_rule_id": case_rule_id,
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
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.list_case_rules_response.ListCaseRulesResponse":
        """<p>Lists all case rules in a Cases domain. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.list_case_rules_request.ListCaseRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.list_case_rules_response.ListCaseRulesResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_case_rules

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.list_case_rules.async_list_case_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.list_case_rules_request.ListCaseRulesRequest = {
            "domain_id": domain_id
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

    async def batch_get_case_rule(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_rules: "capo_connectcases.types.case_rule_identifier_list.CaseRuleIdentifierList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> (
        "capo_connectcases.types.batch_get_case_rule_response.BatchGetCaseRuleResponse"
    ):
        """<p>Gets a batch of case rules. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rules: <p>A list of case rule identifiers.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.batch_get_case_rule_request.BatchGetCaseRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.batch_get_case_rule_response.BatchGetCaseRuleResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.batch_get_case_rule

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.batch_get_case_rule.async_batch_get_case_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.batch_get_case_rule_request.BatchGetCaseRuleRequest = {
            "domain_id": domain_id,
            "case_rules": case_rules,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
