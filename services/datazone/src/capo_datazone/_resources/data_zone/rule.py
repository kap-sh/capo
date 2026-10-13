from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_datazone._auth._signers
import capo_datazone._auth._sigv4
from capo_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_datazone.types.asset_type_identifiers
    import capo_datazone.types.client_token
    import capo_datazone.types.create_rule_input
    import capo_datazone.types.create_rule_output
    import capo_datazone.types.delete_rule_input
    import capo_datazone.types.delete_rule_output
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.get_rule_input
    import capo_datazone.types.get_rule_output
    import capo_datazone.types.list_rules_input
    import capo_datazone.types.list_rules_output
    import capo_datazone.types.pagination_token
    import capo_datazone.types.project_ids
    import capo_datazone.types.revision
    import capo_datazone.types.rule_action
    import capo_datazone.types.rule_detail
    import capo_datazone.types.rule_id
    import capo_datazone.types.rule_name
    import capo_datazone.types.rule_scope
    import capo_datazone.types.rule_summary
    import capo_datazone.types.rule_target
    import capo_datazone.types.rule_target_type
    import capo_datazone.types.rule_type
    import capo_datazone.types.update_rule_input
    import capo_datazone.types.update_rule_output
    from capo_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from capo_datazone._services.data_zone import DataZoneClient, DataZoneClientConfig


class Rule:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.rule_name.RuleName",
        target: "capo_datazone.types.rule_target.RuleTarget",
        action: "capo_datazone.types.rule_action.RuleAction",
        scope: "capo_datazone.types.rule_scope.RuleScope",
        detail: "capo_datazone.types.rule_detail.RuleDetail",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_rule_output.CreateRuleOutput":
        """<p>Creates a rule in Amazon DataZone. A rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain where the rule is created.</p>
            name: <p>The name of the rule.</p>
            target: <p>The target of the rule.</p>
            action: <p>The action of the rule.</p>
            scope: <p>The scope of the rule.</p>
            detail: <p>The detail of the rule.</p>
            description: <p>The description of the rule.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.create_rule_input.CreateRuleInput]",
        ) -> OperationResponse[
            "capo_datazone.types.create_rule_output.CreateRuleOutput"
        ]:
            import capo_datazone._operations.data_zone.create_rule

            output, http_response = (
                capo_datazone._operations.data_zone.create_rule.create_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.create_rule_input.CreateRuleInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_rule_input

            return capo_datazone.types.create_rule_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.create_rule_output.CreateRuleOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_rule_output

            return capo_datazone.types.create_rule_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateRule", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_datazone.types.create_rule_input.CreateRuleInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "target": target,
            "action": action,
            "scope": scope,
            "detail": detail,
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.rule_id.RuleId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.get_rule_output.GetRuleOutput":
        """<p>Gets the details of a rule in Amazon DataZone. A rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain where the <code>GetRule</code> action is to be invoked.</p>
            identifier: <p>The ID of the rule.</p>
            revision: <p>The revision of the rule.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.get_rule_input.GetRuleInput]",
        ) -> OperationResponse["capo_datazone.types.get_rule_output.GetRuleOutput"]:
            import capo_datazone._operations.data_zone.get_rule

            output, http_response = (
                capo_datazone._operations.data_zone.get_rule.get_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.get_rule_output.GetRuleOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.get_rule_output

            return capo_datazone.types.get_rule_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRule", redact_output=_redact_output)
        )
        input_: capo_datazone.types.get_rule_input.GetRuleInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if revision is not None:
            input_["revision"] = revision

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.rule_id.RuleId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        name: Optional["capo_datazone.types.rule_name.RuleName"] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        scope: Optional["capo_datazone.types.rule_scope.RuleScope"] = None,
        detail: Optional["capo_datazone.types.rule_detail.RuleDetail"] = None,
        include_child_domain_units: Optional[bool] = None,
    ) -> "capo_datazone.types.update_rule_output.UpdateRuleOutput":
        """<p>Updates a rule. In Amazon DataZone, a rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which a rule is to be updated.</p>
            identifier: <p>The ID of the rule that is to be updated</p>
            name: <p>The name of the rule.</p>
            description: <p>The description of the rule.</p>
            scope: <p>The scrope of the rule.</p>
            detail: <p>The detail of the rule.</p>
            include_child_domain_units: <p>Specifies whether to update this rule in the child domain units.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.update_rule_input.UpdateRuleInput]",
        ) -> OperationResponse[
            "capo_datazone.types.update_rule_output.UpdateRuleOutput"
        ]:
            import capo_datazone._operations.data_zone.update_rule

            output, http_response = (
                capo_datazone._operations.data_zone.update_rule.update_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.update_rule_input.UpdateRuleInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.update_rule_input

            return capo_datazone.types.update_rule_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.update_rule_output.UpdateRuleOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.update_rule_output

            return capo_datazone.types.update_rule_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateRule", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_datazone.types.update_rule_input.UpdateRuleInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if scope is not None:
            input_["scope"] = scope
        if detail is not None:
            input_["detail"] = detail
        if include_child_domain_units is not None:
            input_["include_child_domain_units"] = include_child_domain_units

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.rule_id.RuleId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_rule_output.DeleteRuleOutput":
        """<p>Deletes a rule in Amazon DataZone. A rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain that where the rule is to be deleted.</p>
            identifier: <p>The ID of the rule that is to be deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.delete_rule_input.DeleteRuleInput]",
        ) -> OperationResponse[
            "capo_datazone.types.delete_rule_output.DeleteRuleOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_rule

            output, http_response = (
                capo_datazone._operations.data_zone.delete_rule.delete_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRule")
        )
        input_: capo_datazone.types.delete_rule_input.DeleteRuleInput = {
            "domain_identifier": domain_identifier,
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        target_type: "capo_datazone.types.rule_target_type.RuleTargetType",
        target_identifier: str,
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        rule_type: Optional["capo_datazone.types.rule_type.RuleType"] = None,
        action: Optional["capo_datazone.types.rule_action.RuleAction"] = None,
        project_ids: Optional["capo_datazone.types.project_ids.ProjectIds"] = None,
        asset_types: Optional[
            "capo_datazone.types.asset_type_identifiers.AssetTypeIdentifiers"
        ] = None,
        data_product: Optional[bool] = None,
        include_cascaded: Optional[bool] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_rules_output.ListRulesOutput":
        """<p>Lists existing rules. In Amazon DataZone, a rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which the rules are to be listed.</p>
            target_type: <p>The target type of the rule.</p>
            target_identifier: <p>The target ID of the rule.</p>
            rule_type: <p>The type of the rule.</p>
            action: <p>The action of the rule.</p>
            project_ids: <p>The IDs of projects in which rules are to be listed.</p>
            asset_types: <p>The asset types of the rule.</p>
            data_product: <p>The data product of the rule.</p>
            include_cascaded: <p>Specifies whether to include cascading rules in the results.</p>
            max_results: <p>The maximum number of rules to return in a single call to <code>ListRules</code>. When the number of rules to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListRules</code> to list the next set of rules.</p>
            next_token: <p>When the number of rules is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of rules, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListRules</code> to list the next set of rules.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.list_rules_input.ListRulesInput]",
        ) -> OperationResponse["capo_datazone.types.list_rules_output.ListRulesOutput"]:
            import capo_datazone._operations.data_zone.list_rules

            output, http_response = (
                capo_datazone._operations.data_zone.list_rules.list_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.list_rules_output.ListRulesOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.list_rules_output

            return capo_datazone.types.list_rules_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListRules", redact_output=_redact_output),
        )
        input_: capo_datazone.types.list_rules_input.ListRulesInput = {
            "domain_identifier": domain_identifier,
            "target_type": target_type,
            "target_identifier": target_identifier,
        }
        if rule_type is not None:
            input_["rule_type"] = rule_type
        if action is not None:
            input_["action"] = action
        if project_ids is not None:
            input_["project_ids"] = project_ids
        if asset_types is not None:
            input_["asset_types"] = asset_types
        if data_product is not None:
            input_["data_product"] = data_product
        if include_cascaded is not None:
            input_["include_cascaded"] = include_cascaded
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


class AsyncRule:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.rule_name.RuleName",
        target: "capo_datazone.types.rule_target.RuleTarget",
        action: "capo_datazone.types.rule_action.RuleAction",
        scope: "capo_datazone.types.rule_scope.RuleScope",
        detail: "capo_datazone.types.rule_detail.RuleDetail",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_rule_output.CreateRuleOutput":
        """<p>Creates a rule in Amazon DataZone. A rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain where the rule is created.</p>
            name: <p>The name of the rule.</p>
            target: <p>The target of the rule.</p>
            action: <p>The action of the rule.</p>
            scope: <p>The scope of the rule.</p>
            detail: <p>The detail of the rule.</p>
            description: <p>The description of the rule.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_rule_input.CreateRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_rule_output.CreateRuleOutput"
        ]:
            import capo_datazone._operations.data_zone.create_rule

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_rule.async_create_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.create_rule_input.CreateRuleInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_rule_input

            return capo_datazone.types.create_rule_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.create_rule_output.CreateRuleOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_rule_output

            return capo_datazone.types.create_rule_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateRule", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_datazone.types.create_rule_input.CreateRuleInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "target": target,
            "action": action,
            "scope": scope,
            "detail": detail,
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.rule_id.RuleId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.get_rule_output.GetRuleOutput":
        """<p>Gets the details of a rule in Amazon DataZone. A rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain where the <code>GetRule</code> action is to be invoked.</p>
            identifier: <p>The ID of the rule.</p>
            revision: <p>The revision of the rule.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_rule_input.GetRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_rule_output.GetRuleOutput"
        ]:
            import capo_datazone._operations.data_zone.get_rule

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_rule.async_get_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.get_rule_output.GetRuleOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.get_rule_output

            return capo_datazone.types.get_rule_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRule", redact_output=_redact_output)
        )
        input_: capo_datazone.types.get_rule_input.GetRuleInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if revision is not None:
            input_["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.rule_id.RuleId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional["capo_datazone.types.rule_name.RuleName"] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        scope: Optional["capo_datazone.types.rule_scope.RuleScope"] = None,
        detail: Optional["capo_datazone.types.rule_detail.RuleDetail"] = None,
        include_child_domain_units: Optional[bool] = None,
    ) -> "capo_datazone.types.update_rule_output.UpdateRuleOutput":
        """<p>Updates a rule. In Amazon DataZone, a rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which a rule is to be updated.</p>
            identifier: <p>The ID of the rule that is to be updated</p>
            name: <p>The name of the rule.</p>
            description: <p>The description of the rule.</p>
            scope: <p>The scrope of the rule.</p>
            detail: <p>The detail of the rule.</p>
            include_child_domain_units: <p>Specifies whether to update this rule in the child domain units.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_rule_input.UpdateRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_rule_output.UpdateRuleOutput"
        ]:
            import capo_datazone._operations.data_zone.update_rule

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_rule.async_update_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.update_rule_input.UpdateRuleInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.update_rule_input

            return capo_datazone.types.update_rule_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.update_rule_output.UpdateRuleOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.update_rule_output

            return capo_datazone.types.update_rule_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateRule", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_datazone.types.update_rule_input.UpdateRuleInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if scope is not None:
            input_["scope"] = scope
        if detail is not None:
            input_["detail"] = detail
        if include_child_domain_units is not None:
            input_["include_child_domain_units"] = include_child_domain_units

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.rule_id.RuleId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_rule_output.DeleteRuleOutput":
        """<p>Deletes a rule in Amazon DataZone. A rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain that where the rule is to be deleted.</p>
            identifier: <p>The ID of the rule that is to be deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_rule_input.DeleteRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_rule_output.DeleteRuleOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_rule

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_rule.async_delete_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRule")
        )
        input_: capo_datazone.types.delete_rule_input.DeleteRuleInput = {
            "domain_identifier": domain_identifier,
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        target_type: "capo_datazone.types.rule_target_type.RuleTargetType",
        target_identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        rule_type: Optional["capo_datazone.types.rule_type.RuleType"] = None,
        action: Optional["capo_datazone.types.rule_action.RuleAction"] = None,
        project_ids: Optional["capo_datazone.types.project_ids.ProjectIds"] = None,
        asset_types: Optional[
            "capo_datazone.types.asset_type_identifiers.AssetTypeIdentifiers"
        ] = None,
        data_product: Optional[bool] = None,
        include_cascaded: Optional[bool] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_rules_output.ListRulesOutput":
        """<p>Lists existing rules. In Amazon DataZone, a rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which the rules are to be listed.</p>
            target_type: <p>The target type of the rule.</p>
            target_identifier: <p>The target ID of the rule.</p>
            rule_type: <p>The type of the rule.</p>
            action: <p>The action of the rule.</p>
            project_ids: <p>The IDs of projects in which rules are to be listed.</p>
            asset_types: <p>The asset types of the rule.</p>
            data_product: <p>The data product of the rule.</p>
            include_cascaded: <p>Specifies whether to include cascading rules in the results.</p>
            max_results: <p>The maximum number of rules to return in a single call to <code>ListRules</code>. When the number of rules to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListRules</code> to list the next set of rules.</p>
            next_token: <p>When the number of rules is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of rules, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListRules</code> to list the next set of rules.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_rules_input.ListRulesInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_rules_output.ListRulesOutput"
        ]:
            import capo_datazone._operations.data_zone.list_rules

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_rules.async_list_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.list_rules_output.ListRulesOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.list_rules_output

            return capo_datazone.types.list_rules_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListRules", redact_output=_redact_output),
        )
        input_: capo_datazone.types.list_rules_input.ListRulesInput = {
            "domain_identifier": domain_identifier,
            "target_type": target_type,
            "target_identifier": target_identifier,
        }
        if rule_type is not None:
            input_["rule_type"] = rule_type
        if action is not None:
            input_["action"] = action
        if project_ids is not None:
            input_["project_ids"] = project_ids
        if asset_types is not None:
            input_["asset_types"] = asset_types
        if data_product is not None:
            input_["data_product"] = data_product
        if include_cascaded is not None:
            input_["include_cascaded"] = include_cascaded
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
