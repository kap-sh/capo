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
    import capo_billingconductor.types.associate_pricing_rules_input
    import capo_billingconductor.types.associate_pricing_rules_output
    import capo_billingconductor.types.billing_period
    import capo_billingconductor.types.client_token
    import capo_billingconductor.types.create_pricing_plan_input
    import capo_billingconductor.types.create_pricing_plan_output
    import capo_billingconductor.types.delete_pricing_plan_input
    import capo_billingconductor.types.delete_pricing_plan_output
    import capo_billingconductor.types.disassociate_pricing_rules_input
    import capo_billingconductor.types.disassociate_pricing_rules_output
    import capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_input
    import capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_output
    import capo_billingconductor.types.list_pricing_plans_filter
    import capo_billingconductor.types.list_pricing_plans_input
    import capo_billingconductor.types.list_pricing_plans_output
    import capo_billingconductor.types.max_pricing_plan_results
    import capo_billingconductor.types.max_pricing_rule_results
    import capo_billingconductor.types.pricing_plan_arn
    import capo_billingconductor.types.pricing_plan_description
    import capo_billingconductor.types.pricing_plan_list_element
    import capo_billingconductor.types.pricing_plan_name
    import capo_billingconductor.types.pricing_rule_arn
    import capo_billingconductor.types.pricing_rule_arns_input
    import capo_billingconductor.types.pricing_rule_arns_non_empty_input
    import capo_billingconductor.types.tag_map
    import capo_billingconductor.types.token
    import capo_billingconductor.types.update_pricing_plan_input
    import capo_billingconductor.types.update_pricing_plan_output
    from capo_billingconductor._services.async_billingconductor import (
        AsyncbillingconductorClient,
        AsyncbillingconductorClientConfig,
    )
    from capo_billingconductor._services.billingconductor import (
        billingconductorClient,
        billingconductorClientConfig,
    )


class PricingPlan:
    def __init__(self, service: billingconductorClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_billingconductor.types.pricing_plan_name.PricingPlanName",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        client_token: Optional[
            "capo_billingconductor.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.pricing_plan_description.PricingPlanDescription"
        ] = None,
        pricing_rule_arns: Optional[
            "capo_billingconductor.types.pricing_rule_arns_input.PricingRuleArnsInput"
        ] = None,
        tags: Optional["capo_billingconductor.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_billingconductor.types.create_pricing_plan_output.CreatePricingPlanOutput"
    ):
        """<p>Creates a pricing plan that is used for computing Amazon Web Services charges for billing groups. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p>The name of the pricing plan. The names must be unique to each pricing plan. </p>
            description: <p>The description of the pricing plan. </p>
            pricing_rule_arns: <p> A list of Amazon Resource Names (ARNs) that define the pricing plan parameters. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a pricing plan. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.create_pricing_plan_input.CreatePricingPlanInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.create_pricing_plan_output.CreatePricingPlanOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.create_pricing_plan

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.create_pricing_plan.create_pricing_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_billingconductor.types.create_pricing_plan_input.CreatePricingPlanInput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.create_pricing_plan_input

            return (
                capo_billingconductor.types.create_pricing_plan_input.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreatePricingPlan", redact_input=_redact_input),
        )
        input_: capo_billingconductor.types.create_pricing_plan_input.CreatePricingPlanInput = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if pricing_rule_arns is not None:
            input_["pricing_rule_arns"] = pricing_rule_arns
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        name: Optional[
            "capo_billingconductor.types.pricing_plan_name.PricingPlanName"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.pricing_plan_description.PricingPlanDescription"
        ] = None,
    ) -> (
        "capo_billingconductor.types.update_pricing_plan_output.UpdatePricingPlanOutput"
    ):
        """<p>This updates an existing pricing plan. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pricing plan that you're updating. </p>
            name: <p>The name of the pricing plan. The name must be unique to each pricing plan. </p>
            description: <p>The description of the pricing plan. </p>

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
            req: "OperationRequest[capo_billingconductor.types.update_pricing_plan_input.UpdatePricingPlanInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.update_pricing_plan_output.UpdatePricingPlanOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.update_pricing_plan

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.update_pricing_plan.update_pricing_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_billingconductor.types.update_pricing_plan_input.UpdatePricingPlanInput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.update_pricing_plan_input

            return (
                capo_billingconductor.types.update_pricing_plan_input.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_billingconductor.types.update_pricing_plan_output.UpdatePricingPlanOutput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.update_pricing_plan_output

            return (
                capo_billingconductor.types.update_pricing_plan_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdatePricingPlan",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_billingconductor.types.update_pricing_plan_input.UpdatePricingPlanInput = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
    ) -> (
        "capo_billingconductor.types.delete_pricing_plan_output.DeletePricingPlanOutput"
    ):
        """<p>Deletes a pricing plan. The pricing plan must not be associated with any billing groups to delete successfully.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pricing plan that you're deleting. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.delete_pricing_plan_input.DeletePricingPlanInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.delete_pricing_plan_output.DeletePricingPlanOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.delete_pricing_plan

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.delete_pricing_plan.delete_pricing_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePricingPlan")
        )
        input_: capo_billingconductor.types.delete_pricing_plan_input.DeletePricingPlanInput = {
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
            "capo_billingconductor.types.list_pricing_plans_filter.ListPricingPlansFilter"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_plan_results.MaxPricingPlanResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "capo_billingconductor.types.list_pricing_plans_output.ListPricingPlansOutput":
        """<p>A paginated call to get pricing plans for the given billing period. If you don't provide a billing period, the current billing period is used. </p>

        Args:
            billing_period: <p>The preferred billing period to get pricing plan. </p>
            filters: <p>A <code>ListPricingPlansFilter</code> that specifies the Amazon Resource Name (ARNs) of pricing plans to retrieve pricing plans information.</p>
            max_results: <p>The maximum number of pricing plans to retrieve.</p>
            next_token: <p>The pagination token that's used on subsequent call to get pricing plans. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.list_pricing_plans_input.ListPricingPlansInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.list_pricing_plans_output.ListPricingPlansOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_pricing_plans

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.list_pricing_plans.list_pricing_plans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_billingconductor.types.list_pricing_plans_output.ListPricingPlansOutput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.list_pricing_plans_output

            return (
                capo_billingconductor.types.list_pricing_plans_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListPricingPlans", redact_output=_redact_output),
        )
        input_: capo_billingconductor.types.list_pricing_plans_input.ListPricingPlansInput = {}
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

    def associate_pricing_rules(
        self,
        arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        pricing_rule_arns: "capo_billingconductor.types.pricing_rule_arns_non_empty_input.PricingRuleArnsNonEmptyInput",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.associate_pricing_rules_output.AssociatePricingRulesOutput":
        """<p>Connects an array of <code>PricingRuleArns</code> to a defined <code>PricingPlan</code>. The maximum number <code>PricingRuleArn</code> that can be associated in one call is 30. </p>

        Args:
            arn: <p> The <code>PricingPlanArn</code> that the <code>PricingRuleArns</code> are associated with. </p>
            pricing_rule_arns: <p> The <code>PricingRuleArns</code> that are associated with the Pricing Plan. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billingconductor.types.associate_pricing_rules_input.AssociatePricingRulesInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.associate_pricing_rules_output.AssociatePricingRulesOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.associate_pricing_rules

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.associate_pricing_rules.associate_pricing_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociatePricingRules")
        )
        input_: capo_billingconductor.types.associate_pricing_rules_input.AssociatePricingRulesInput = {
            "arn": arn,
            "pricing_rule_arns": pricing_rule_arns,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_pricing_rules(
        self,
        arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        pricing_rule_arns: "capo_billingconductor.types.pricing_rule_arns_non_empty_input.PricingRuleArnsNonEmptyInput",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.disassociate_pricing_rules_output.DisassociatePricingRulesOutput":
        """<p> Disassociates a list of pricing rules from a pricing plan. </p>

        Args:
            arn: <p> The pricing plan Amazon Resource Name (ARN) to disassociate pricing rules from. </p>
            pricing_rule_arns: <p> A list containing the Amazon Resource Name (ARN) of the pricing rules that will be disassociated. </p>

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
            req: "OperationRequest[capo_billingconductor.types.disassociate_pricing_rules_input.DisassociatePricingRulesInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.disassociate_pricing_rules_output.DisassociatePricingRulesOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.disassociate_pricing_rules

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.disassociate_pricing_rules.disassociate_pricing_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociatePricingRules")
        )
        input_: capo_billingconductor.types.disassociate_pricing_rules_input.DisassociatePricingRulesInput = {
            "arn": arn,
            "pricing_rule_arns": pricing_rule_arns,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_pricing_plans_associated_with_pricing_rule(
        self,
        pricing_rule_arn: "capo_billingconductor.types.pricing_rule_arn.PricingRuleArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_rule_results.MaxPricingRuleResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_output.ListPricingPlansAssociatedWithPricingRuleOutput":
        """<p> A list of the pricing plans that are associated with a pricing rule. </p>

        Args:
            billing_period: <p> The pricing plan billing period for which associations will be listed. </p>
            pricing_rule_arn: <p> The pricing rule Amazon Resource Name (ARN) for which associations will be listed. </p>
            max_results: <p> The optional maximum number of pricing rule associations to retrieve. </p>
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
            req: "OperationRequest[capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_input.ListPricingPlansAssociatedWithPricingRuleInput]",
        ) -> OperationResponse[
            "capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_output.ListPricingPlansAssociatedWithPricingRuleOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_pricing_plans_associated_with_pricing_rule

            output, http_response = (
                capo_billingconductor._operations.aws_billing_conductor.list_pricing_plans_associated_with_pricing_rule.list_pricing_plans_associated_with_pricing_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListPricingPlansAssociatedWithPricingRule"),
        )
        input_: capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_input.ListPricingPlansAssociatedWithPricingRuleInput = {
            "pricing_rule_arn": pricing_rule_arn
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


class AsyncPricingPlan:
    def __init__(self, service: AsyncbillingconductorClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_billingconductor.types.pricing_plan_name.PricingPlanName",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        client_token: Optional[
            "capo_billingconductor.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.pricing_plan_description.PricingPlanDescription"
        ] = None,
        pricing_rule_arns: Optional[
            "capo_billingconductor.types.pricing_rule_arns_input.PricingRuleArnsInput"
        ] = None,
        tags: Optional["capo_billingconductor.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_billingconductor.types.create_pricing_plan_output.CreatePricingPlanOutput"
    ):
        """<p>Creates a pricing plan that is used for computing Amazon Web Services charges for billing groups. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p>The name of the pricing plan. The names must be unique to each pricing plan. </p>
            description: <p>The description of the pricing plan. </p>
            pricing_rule_arns: <p> A list of Amazon Resource Names (ARNs) that define the pricing plan parameters. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a pricing plan. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.create_pricing_plan_input.CreatePricingPlanInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.create_pricing_plan_output.CreatePricingPlanOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.create_pricing_plan

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.create_pricing_plan.async_create_pricing_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_billingconductor.types.create_pricing_plan_input.CreatePricingPlanInput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.create_pricing_plan_input

            return (
                capo_billingconductor.types.create_pricing_plan_input.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreatePricingPlan", redact_input=_redact_input),
        )
        input_: capo_billingconductor.types.create_pricing_plan_input.CreatePricingPlanInput = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if pricing_rule_arns is not None:
            input_["pricing_rule_arns"] = pricing_rule_arns
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        name: Optional[
            "capo_billingconductor.types.pricing_plan_name.PricingPlanName"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.pricing_plan_description.PricingPlanDescription"
        ] = None,
    ) -> (
        "capo_billingconductor.types.update_pricing_plan_output.UpdatePricingPlanOutput"
    ):
        """<p>This updates an existing pricing plan. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pricing plan that you're updating. </p>
            name: <p>The name of the pricing plan. The name must be unique to each pricing plan. </p>
            description: <p>The description of the pricing plan. </p>

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
            req: "AsyncOperationRequest[capo_billingconductor.types.update_pricing_plan_input.UpdatePricingPlanInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.update_pricing_plan_output.UpdatePricingPlanOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.update_pricing_plan

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.update_pricing_plan.async_update_pricing_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_billingconductor.types.update_pricing_plan_input.UpdatePricingPlanInput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.update_pricing_plan_input

            return (
                capo_billingconductor.types.update_pricing_plan_input.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_billingconductor.types.update_pricing_plan_output.UpdatePricingPlanOutput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.update_pricing_plan_output

            return (
                capo_billingconductor.types.update_pricing_plan_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdatePricingPlan",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_billingconductor.types.update_pricing_plan_input.UpdatePricingPlanInput = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> (
        "capo_billingconductor.types.delete_pricing_plan_output.DeletePricingPlanOutput"
    ):
        """<p>Deletes a pricing plan. The pricing plan must not be associated with any billing groups to delete successfully.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pricing plan that you're deleting. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.delete_pricing_plan_input.DeletePricingPlanInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.delete_pricing_plan_output.DeletePricingPlanOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.delete_pricing_plan

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.delete_pricing_plan.async_delete_pricing_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePricingPlan")
        )
        input_: capo_billingconductor.types.delete_pricing_plan_input.DeletePricingPlanInput = {
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
            "capo_billingconductor.types.list_pricing_plans_filter.ListPricingPlansFilter"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_plan_results.MaxPricingPlanResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "capo_billingconductor.types.list_pricing_plans_output.ListPricingPlansOutput":
        """<p>A paginated call to get pricing plans for the given billing period. If you don't provide a billing period, the current billing period is used. </p>

        Args:
            billing_period: <p>The preferred billing period to get pricing plan. </p>
            filters: <p>A <code>ListPricingPlansFilter</code> that specifies the Amazon Resource Name (ARNs) of pricing plans to retrieve pricing plans information.</p>
            max_results: <p>The maximum number of pricing plans to retrieve.</p>
            next_token: <p>The pagination token that's used on subsequent call to get pricing plans. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_pricing_plans_input.ListPricingPlansInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_pricing_plans_output.ListPricingPlansOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_pricing_plans

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_pricing_plans.async_list_pricing_plans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_billingconductor.types.list_pricing_plans_output.ListPricingPlansOutput",
        ) -> dict[str, Any]:
            import capo_billingconductor.types.list_pricing_plans_output

            return (
                capo_billingconductor.types.list_pricing_plans_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListPricingPlans", redact_output=_redact_output),
        )
        input_: capo_billingconductor.types.list_pricing_plans_input.ListPricingPlansInput = {}
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

    async def associate_pricing_rules(
        self,
        arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        pricing_rule_arns: "capo_billingconductor.types.pricing_rule_arns_non_empty_input.PricingRuleArnsNonEmptyInput",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.associate_pricing_rules_output.AssociatePricingRulesOutput":
        """<p>Connects an array of <code>PricingRuleArns</code> to a defined <code>PricingPlan</code>. The maximum number <code>PricingRuleArn</code> that can be associated in one call is 30. </p>

        Args:
            arn: <p> The <code>PricingPlanArn</code> that the <code>PricingRuleArns</code> are associated with. </p>
            pricing_rule_arns: <p> The <code>PricingRuleArns</code> that are associated with the Pricing Plan. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.associate_pricing_rules_input.AssociatePricingRulesInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.associate_pricing_rules_output.AssociatePricingRulesOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.associate_pricing_rules

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.associate_pricing_rules.async_associate_pricing_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociatePricingRules")
        )
        input_: capo_billingconductor.types.associate_pricing_rules_input.AssociatePricingRulesInput = {
            "arn": arn,
            "pricing_rule_arns": pricing_rule_arns,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_pricing_rules(
        self,
        arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        pricing_rule_arns: "capo_billingconductor.types.pricing_rule_arns_non_empty_input.PricingRuleArnsNonEmptyInput",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.disassociate_pricing_rules_output.DisassociatePricingRulesOutput":
        """<p> Disassociates a list of pricing rules from a pricing plan. </p>

        Args:
            arn: <p> The pricing plan Amazon Resource Name (ARN) to disassociate pricing rules from. </p>
            pricing_rule_arns: <p> A list containing the Amazon Resource Name (ARN) of the pricing rules that will be disassociated. </p>

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
            req: "AsyncOperationRequest[capo_billingconductor.types.disassociate_pricing_rules_input.DisassociatePricingRulesInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.disassociate_pricing_rules_output.DisassociatePricingRulesOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.disassociate_pricing_rules

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.disassociate_pricing_rules.async_disassociate_pricing_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociatePricingRules")
        )
        input_: capo_billingconductor.types.disassociate_pricing_rules_input.DisassociatePricingRulesInput = {
            "arn": arn,
            "pricing_rule_arns": pricing_rule_arns,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_pricing_plans_associated_with_pricing_rule(
        self,
        pricing_rule_arn: "capo_billingconductor.types.pricing_rule_arn.PricingRuleArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_rule_results.MaxPricingRuleResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_output.ListPricingPlansAssociatedWithPricingRuleOutput":
        """<p> A list of the pricing plans that are associated with a pricing rule. </p>

        Args:
            billing_period: <p> The pricing plan billing period for which associations will be listed. </p>
            pricing_rule_arn: <p> The pricing rule Amazon Resource Name (ARN) for which associations will be listed. </p>
            max_results: <p> The optional maximum number of pricing rule associations to retrieve. </p>
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
            req: "AsyncOperationRequest[capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_input.ListPricingPlansAssociatedWithPricingRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_output.ListPricingPlansAssociatedWithPricingRuleOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_pricing_plans_associated_with_pricing_rule

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_pricing_plans_associated_with_pricing_rule.async_list_pricing_plans_associated_with_pricing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListPricingPlansAssociatedWithPricingRule"),
        )
        input_: capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_input.ListPricingPlansAssociatedWithPricingRuleInput = {
            "pricing_rule_arn": pricing_rule_arn
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
