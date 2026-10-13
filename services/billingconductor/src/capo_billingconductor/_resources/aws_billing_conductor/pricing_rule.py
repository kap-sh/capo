from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_billingconductor._auth._signers
import capo_billingconductor._auth._sigv4
from capo_billingconductor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_entity
    import capo_billingconductor.types.billing_period
    import capo_billingconductor.types.client_token
    import capo_billingconductor.types.create_pricing_rule_input
    import capo_billingconductor.types.create_pricing_rule_output
    import capo_billingconductor.types.create_tiering_input
    import capo_billingconductor.types.delete_pricing_rule_input
    import capo_billingconductor.types.delete_pricing_rule_output
    import capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_input
    import capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_output
    import capo_billingconductor.types.list_pricing_rules_filter
    import capo_billingconductor.types.list_pricing_rules_input
    import capo_billingconductor.types.list_pricing_rules_output
    import capo_billingconductor.types.max_pricing_plan_results
    import capo_billingconductor.types.max_pricing_rule_results
    import capo_billingconductor.types.modifier_percentage
    import capo_billingconductor.types.operation
    import capo_billingconductor.types.pricing_plan_arn
    import capo_billingconductor.types.pricing_rule_arn
    import capo_billingconductor.types.pricing_rule_description
    import capo_billingconductor.types.pricing_rule_list_element
    import capo_billingconductor.types.pricing_rule_name
    import capo_billingconductor.types.pricing_rule_scope
    import capo_billingconductor.types.pricing_rule_type
    import capo_billingconductor.types.service
    import capo_billingconductor.types.tag_map
    import capo_billingconductor.types.token
    import capo_billingconductor.types.update_pricing_rule_input
    import capo_billingconductor.types.update_pricing_rule_output
    import capo_billingconductor.types.update_tiering_input
    import capo_billingconductor.types.usage_type
    from capo_billingconductor._services.async_billingconductor import (
        AsyncbillingconductorClient,
        AsyncbillingconductorClientConfig,
    )
    from capo_billingconductor._services.billingconductor import (
        billingconductorClient,
        billingconductorClientConfig,
    )


class PricingRule:
    def __init__(self, service: billingconductorClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_billingconductor.types.pricing_rule_name.PricingRuleName",
        scope: "capo_billingconductor.types.pricing_rule_scope.PricingRuleScope",
        type: "capo_billingconductor.types.pricing_rule_type.PricingRuleType",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        client_token: Optional[
            "capo_billingconductor.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.pricing_rule_description.PricingRuleDescription"
        ] = None,
        modifier_percentage: Optional[
            "capo_billingconductor.types.modifier_percentage.ModifierPercentage"
        ] = None,
        service: Optional["capo_billingconductor.types.service.Service"] = None,
        tags: Optional["capo_billingconductor.types.tag_map.TagMap"] = None,
        billing_entity: Optional[
            "capo_billingconductor.types.billing_entity.BillingEntity"
        ] = None,
        tiering: Optional[
            "capo_billingconductor.types.create_tiering_input.CreateTieringInput"
        ] = None,
        usage_type: Optional["capo_billingconductor.types.usage_type.UsageType"] = None,
        operation: Optional["capo_billingconductor.types.operation.Operation"] = None,
    ) -> (
        "capo_billingconductor.types.create_pricing_rule_output.CreatePricingRuleOutput"
    ):
        """<p> Creates a pricing rule can be associated to a pricing plan, or a set of pricing plans. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p> The pricing rule name. The names must be unique to each pricing rule. </p>
            description: <p> The pricing rule description. </p>
            scope: <p> The scope of pricing rule that indicates if it's globally applicable, or it's service-specific. </p>
            type: <p> The type of pricing rule. </p>
            modifier_percentage: <p>A percentage modifier that's applied on the public pricing rates. Your entry will be rounded to the nearest 2 decimal places.</p>
            service: <p> If the <code>Scope</code> attribute is set to <code>SERVICE</code> or <code>SKU</code>, the attribute indicates which service the <code>PricingRule</code> is applicable for. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a pricing rule. </p>
            billing_entity: <p> The seller of services provided by Amazon Web Services, their affiliates, or third-party providers selling services via Amazon Web Services Marketplace. </p>
            tiering: <p> The set of tiering configurations for the pricing rule. </p>
            usage_type: <p> Usage type is the unit that each service uses to measure the usage of a specific type of resource.</p> <p>If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which usage type the <code>PricingRule</code> is modifying. For example, <code>USW2-BoxUsage:m2.2xlarge</code> describes an<code> M2 High Memory Double Extra Large</code> instance in the US West (Oregon) Region. </p>
            operation: <p> Operation is the specific Amazon Web Services action covered by this line item. This describes the specific usage of the line item.</p> <p> If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which operation the <code>PricingRule</code> is modifying. For example, a value of <code>RunInstances:0202</code> indicates the operation of running an Amazon EC2 instance.</p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.create_pricing_rule_input.CreatePricingRuleInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.create_pricing_rule_output.CreatePricingRuleOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.create_pricing_rule

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.create_pricing_rule.create_pricing_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_billingconductor.types.create_pricing_rule_input.CreatePricingRuleInput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.create_pricing_rule_input

            return (
                capo_billingconductor.types.create_pricing_rule_input.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreatePricingRule", redact_input=_redact_input),
        )
        input_: capo_billingconductor.types.create_pricing_rule_input.CreatePricingRuleInput = {
            "name": name,
            "scope": scope,
            "type": type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if modifier_percentage is not None:
            input_["modifier_percentage"] = modifier_percentage
        if service is not None:
            input_["service"] = service
        if tags is not None:
            input_["tags"] = tags
        if billing_entity is not None:
            input_["billing_entity"] = billing_entity
        if tiering is not None:
            input_["tiering"] = tiering
        if usage_type is not None:
            input_["usage_type"] = usage_type
        if operation is not None:
            input_["operation"] = operation

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        arn: "capo_billingconductor.types.pricing_rule_arn.PricingRuleArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        name: Optional[
            "capo_billingconductor.types.pricing_rule_name.PricingRuleName"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.pricing_rule_description.PricingRuleDescription"
        ] = None,
        type: Optional[
            "capo_billingconductor.types.pricing_rule_type.PricingRuleType"
        ] = None,
        modifier_percentage: Optional[
            "capo_billingconductor.types.modifier_percentage.ModifierPercentage"
        ] = None,
        tiering: Optional[
            "capo_billingconductor.types.update_tiering_input.UpdateTieringInput"
        ] = None,
    ) -> (
        "capo_billingconductor.types.update_pricing_rule_output.UpdatePricingRuleOutput"
    ):
        """<p> Updates an existing pricing rule. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the pricing rule to update. </p>
            name: <p> The new name of the pricing rule. The name must be unique to each pricing rule. </p>
            description: <p> The new description for the pricing rule. </p>
            type: <p> The new pricing rule type. </p>
            modifier_percentage: <p> The new modifier to show pricing plan rates as a percentage. Your entry will be rounded to the nearest 2 decimal places. </p>
            tiering: <p> The set of tiering configurations for the pricing rule. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.update_pricing_rule_input.UpdatePricingRuleInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.update_pricing_rule_output.UpdatePricingRuleOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.update_pricing_rule

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.update_pricing_rule.update_pricing_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_billingconductor.types.update_pricing_rule_input.UpdatePricingRuleInput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.update_pricing_rule_input

            return (
                capo_billingconductor.types.update_pricing_rule_input.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_billingconductor.types.update_pricing_rule_output.UpdatePricingRuleOutput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.update_pricing_rule_output

            return (
                capo_billingconductor.types.update_pricing_rule_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdatePricingRule",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_billingconductor.types.update_pricing_rule_input.UpdatePricingRuleInput = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
        if modifier_percentage is not None:
            input_["modifier_percentage"] = modifier_percentage
        if tiering is not None:
            input_["tiering"] = tiering

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        arn: "capo_billingconductor.types.pricing_rule_arn.PricingRuleArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
    ) -> (
        "capo_billingconductor.types.delete_pricing_rule_output.DeletePricingRuleOutput"
    ):
        """<p> Deletes the pricing rule that's identified by the input Amazon Resource Name (ARN). </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the pricing rule that you are deleting. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.delete_pricing_rule_input.DeletePricingRuleInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.delete_pricing_rule_output.DeletePricingRuleOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.delete_pricing_rule

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.delete_pricing_rule.delete_pricing_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePricingRule")
        )
        input_: capo_billingconductor.types.delete_pricing_rule_input.DeletePricingRuleInput = {
            "arn": arn
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
        config_overrides: Optional[billingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        filters: Optional[
            "capo_billingconductor.types.list_pricing_rules_filter.ListPricingRulesFilter"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_rule_results.MaxPricingRuleResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "capo_billingconductor.types.list_pricing_rules_output.ListPricingRulesOutput":
        """<p> Describes a pricing rule that can be associated to a pricing plan, or set of pricing plans. </p>

        Args:
            billing_period: <p> The preferred billing period to get the pricing plan. </p>
            filters: <p> A <code>DescribePricingRuleFilter</code> that specifies the Amazon Resource Name (ARNs) of pricing rules to retrieve pricing rules information. </p>
            max_results: <p> The maximum number of pricing rules to retrieve. </p>
            next_token: <p> The pagination token that's used on subsequent call to get pricing rules. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.list_pricing_rules_input.ListPricingRulesInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.list_pricing_rules_output.ListPricingRulesOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_pricing_rules

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.list_pricing_rules.list_pricing_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_billingconductor.types.list_pricing_rules_output.ListPricingRulesOutput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.list_pricing_rules_output

            return (
                capo_billingconductor.types.list_pricing_rules_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListPricingRules", redact_output=_redact_output),
        )
        input_: capo_billingconductor.types.list_pricing_rules_input.ListPricingRulesInput = {}
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if filters is not None:
            input_["filters"] = filters
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

    def list_pricing_rules_associated_to_pricing_plan(
        self,
        pricing_plan_arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_plan_results.MaxPricingPlanResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_output.ListPricingRulesAssociatedToPricingPlanOutput":
        """<p> Lists the pricing rules that are associated with a pricing plan. </p>

        Args:
            billing_period: <p> The billing period for which the pricing rule associations are to be listed. </p>
            pricing_plan_arn: <p> The Amazon Resource Name (ARN) of the pricing plan for which associations are to be listed.</p>
            max_results: <p>The optional maximum number of pricing rule associations to retrieve.</p>
            next_token: <p> The optional pagination token returned by a previous call. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_input.ListPricingRulesAssociatedToPricingPlanInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_output.ListPricingRulesAssociatedToPricingPlanOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_pricing_rules_associated_to_pricing_plan

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.list_pricing_rules_associated_to_pricing_plan.list_pricing_rules_associated_to_pricing_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListPricingRulesAssociatedToPricingPlan"),
        )
        input_: capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_input.ListPricingRulesAssociatedToPricingPlanInput = {
            "pricing_plan_arn": pricing_plan_arn
        }
        if billing_period is not None:
            input_["billing_period"] = billing_period
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


class AsyncPricingRule:
    def __init__(self, service: AsyncbillingconductorClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_billingconductor.types.pricing_rule_name.PricingRuleName",
        scope: "capo_billingconductor.types.pricing_rule_scope.PricingRuleScope",
        type: "capo_billingconductor.types.pricing_rule_type.PricingRuleType",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        client_token: Optional[
            "capo_billingconductor.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.pricing_rule_description.PricingRuleDescription"
        ] = None,
        modifier_percentage: Optional[
            "capo_billingconductor.types.modifier_percentage.ModifierPercentage"
        ] = None,
        service: Optional["capo_billingconductor.types.service.Service"] = None,
        tags: Optional["capo_billingconductor.types.tag_map.TagMap"] = None,
        billing_entity: Optional[
            "capo_billingconductor.types.billing_entity.BillingEntity"
        ] = None,
        tiering: Optional[
            "capo_billingconductor.types.create_tiering_input.CreateTieringInput"
        ] = None,
        usage_type: Optional["capo_billingconductor.types.usage_type.UsageType"] = None,
        operation: Optional["capo_billingconductor.types.operation.Operation"] = None,
    ) -> (
        "capo_billingconductor.types.create_pricing_rule_output.CreatePricingRuleOutput"
    ):
        """<p> Creates a pricing rule can be associated to a pricing plan, or a set of pricing plans. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p> The pricing rule name. The names must be unique to each pricing rule. </p>
            description: <p> The pricing rule description. </p>
            scope: <p> The scope of pricing rule that indicates if it's globally applicable, or it's service-specific. </p>
            type: <p> The type of pricing rule. </p>
            modifier_percentage: <p>A percentage modifier that's applied on the public pricing rates. Your entry will be rounded to the nearest 2 decimal places.</p>
            service: <p> If the <code>Scope</code> attribute is set to <code>SERVICE</code> or <code>SKU</code>, the attribute indicates which service the <code>PricingRule</code> is applicable for. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a pricing rule. </p>
            billing_entity: <p> The seller of services provided by Amazon Web Services, their affiliates, or third-party providers selling services via Amazon Web Services Marketplace. </p>
            tiering: <p> The set of tiering configurations for the pricing rule. </p>
            usage_type: <p> Usage type is the unit that each service uses to measure the usage of a specific type of resource.</p> <p>If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which usage type the <code>PricingRule</code> is modifying. For example, <code>USW2-BoxUsage:m2.2xlarge</code> describes an<code> M2 High Memory Double Extra Large</code> instance in the US West (Oregon) Region. </p>
            operation: <p> Operation is the specific Amazon Web Services action covered by this line item. This describes the specific usage of the line item.</p> <p> If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which operation the <code>PricingRule</code> is modifying. For example, a value of <code>RunInstances:0202</code> indicates the operation of running an Amazon EC2 instance.</p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.create_pricing_rule_input.CreatePricingRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.create_pricing_rule_output.CreatePricingRuleOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.create_pricing_rule

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.create_pricing_rule.async_create_pricing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_billingconductor.types.create_pricing_rule_input.CreatePricingRuleInput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.create_pricing_rule_input

            return (
                capo_billingconductor.types.create_pricing_rule_input.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreatePricingRule", redact_input=_redact_input),
        )
        input_: capo_billingconductor.types.create_pricing_rule_input.CreatePricingRuleInput = {
            "name": name,
            "scope": scope,
            "type": type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if modifier_percentage is not None:
            input_["modifier_percentage"] = modifier_percentage
        if service is not None:
            input_["service"] = service
        if tags is not None:
            input_["tags"] = tags
        if billing_entity is not None:
            input_["billing_entity"] = billing_entity
        if tiering is not None:
            input_["tiering"] = tiering
        if usage_type is not None:
            input_["usage_type"] = usage_type
        if operation is not None:
            input_["operation"] = operation

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        arn: "capo_billingconductor.types.pricing_rule_arn.PricingRuleArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        name: Optional[
            "capo_billingconductor.types.pricing_rule_name.PricingRuleName"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.pricing_rule_description.PricingRuleDescription"
        ] = None,
        type: Optional[
            "capo_billingconductor.types.pricing_rule_type.PricingRuleType"
        ] = None,
        modifier_percentage: Optional[
            "capo_billingconductor.types.modifier_percentage.ModifierPercentage"
        ] = None,
        tiering: Optional[
            "capo_billingconductor.types.update_tiering_input.UpdateTieringInput"
        ] = None,
    ) -> (
        "capo_billingconductor.types.update_pricing_rule_output.UpdatePricingRuleOutput"
    ):
        """<p> Updates an existing pricing rule. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the pricing rule to update. </p>
            name: <p> The new name of the pricing rule. The name must be unique to each pricing rule. </p>
            description: <p> The new description for the pricing rule. </p>
            type: <p> The new pricing rule type. </p>
            modifier_percentage: <p> The new modifier to show pricing plan rates as a percentage. Your entry will be rounded to the nearest 2 decimal places. </p>
            tiering: <p> The set of tiering configurations for the pricing rule. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.update_pricing_rule_input.UpdatePricingRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.update_pricing_rule_output.UpdatePricingRuleOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.update_pricing_rule

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.update_pricing_rule.async_update_pricing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_billingconductor.types.update_pricing_rule_input.UpdatePricingRuleInput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.update_pricing_rule_input

            return (
                capo_billingconductor.types.update_pricing_rule_input.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_billingconductor.types.update_pricing_rule_output.UpdatePricingRuleOutput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.update_pricing_rule_output

            return (
                capo_billingconductor.types.update_pricing_rule_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdatePricingRule",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_billingconductor.types.update_pricing_rule_input.UpdatePricingRuleInput = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
        if modifier_percentage is not None:
            input_["modifier_percentage"] = modifier_percentage
        if tiering is not None:
            input_["tiering"] = tiering

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        arn: "capo_billingconductor.types.pricing_rule_arn.PricingRuleArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> (
        "capo_billingconductor.types.delete_pricing_rule_output.DeletePricingRuleOutput"
    ):
        """<p> Deletes the pricing rule that's identified by the input Amazon Resource Name (ARN). </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the pricing rule that you are deleting. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.delete_pricing_rule_input.DeletePricingRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.delete_pricing_rule_output.DeletePricingRuleOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.delete_pricing_rule

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.delete_pricing_rule.async_delete_pricing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePricingRule")
        )
        input_: capo_billingconductor.types.delete_pricing_rule_input.DeletePricingRuleInput = {
            "arn": arn
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
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        filters: Optional[
            "capo_billingconductor.types.list_pricing_rules_filter.ListPricingRulesFilter"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_rule_results.MaxPricingRuleResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "capo_billingconductor.types.list_pricing_rules_output.ListPricingRulesOutput":
        """<p> Describes a pricing rule that can be associated to a pricing plan, or set of pricing plans. </p>

        Args:
            billing_period: <p> The preferred billing period to get the pricing plan. </p>
            filters: <p> A <code>DescribePricingRuleFilter</code> that specifies the Amazon Resource Name (ARNs) of pricing rules to retrieve pricing rules information. </p>
            max_results: <p> The maximum number of pricing rules to retrieve. </p>
            next_token: <p> The pagination token that's used on subsequent call to get pricing rules. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_pricing_rules_input.ListPricingRulesInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_pricing_rules_output.ListPricingRulesOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_pricing_rules

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_pricing_rules.async_list_pricing_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_billingconductor.types.list_pricing_rules_output.ListPricingRulesOutput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.list_pricing_rules_output

            return (
                capo_billingconductor.types.list_pricing_rules_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListPricingRules", redact_output=_redact_output),
        )
        input_: capo_billingconductor.types.list_pricing_rules_input.ListPricingRulesInput = {}
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if filters is not None:
            input_["filters"] = filters
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

    async def list_pricing_rules_associated_to_pricing_plan(
        self,
        pricing_plan_arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_plan_results.MaxPricingPlanResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_output.ListPricingRulesAssociatedToPricingPlanOutput":
        """<p> Lists the pricing rules that are associated with a pricing plan. </p>

        Args:
            billing_period: <p> The billing period for which the pricing rule associations are to be listed. </p>
            pricing_plan_arn: <p> The Amazon Resource Name (ARN) of the pricing plan for which associations are to be listed.</p>
            max_results: <p>The optional maximum number of pricing rule associations to retrieve.</p>
            next_token: <p> The optional pagination token returned by a previous call. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_input.ListPricingRulesAssociatedToPricingPlanInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_output.ListPricingRulesAssociatedToPricingPlanOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_pricing_rules_associated_to_pricing_plan

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_pricing_rules_associated_to_pricing_plan.async_list_pricing_rules_associated_to_pricing_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListPricingRulesAssociatedToPricingPlan"),
        )
        input_: capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_input.ListPricingRulesAssociatedToPricingPlanInput = {
            "pricing_plan_arn": pricing_plan_arn
        }
        if billing_period is not None:
            input_["billing_period"] = billing_period
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
