from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_elementalinference._auth._signers
import capo_elementalinference._auth._sigv4
from capo_elementalinference._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_elementalinference.types.create_function_request
    import capo_elementalinference.types.create_function_response
    import capo_elementalinference.types.delete_function_request
    import capo_elementalinference.types.delete_function_response
    import capo_elementalinference.types.event_bridge_delivery_mode
    import capo_elementalinference.types.function_description
    import capo_elementalinference.types.function_id
    import capo_elementalinference.types.function_summary
    import capo_elementalinference.types.function_target
    import capo_elementalinference.types.get_function_request
    import capo_elementalinference.types.get_function_response
    import capo_elementalinference.types.jsonata_expression
    import capo_elementalinference.types.list_functions_request
    import capo_elementalinference.types.list_functions_response
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.tag_map
    import capo_elementalinference.types.update_function_request
    import capo_elementalinference.types.update_function_response
    from capo_elementalinference._services.async_elemental_inference import (
        AsyncElementalInferenceClient,
        AsyncElementalInferenceClientConfig,
    )
    from capo_elementalinference._services.elemental_inference import (
        ElementalInferenceClient,
        ElementalInferenceClientConfig,
    )


class FunctionResource:
    def __init__(self, service: ElementalInferenceClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        target: "capo_elementalinference.types.function_target.FunctionTarget",
        request_expression: "capo_elementalinference.types.jsonata_expression.JsonataExpression",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        response_expression: Optional[
            "capo_elementalinference.types.jsonata_expression.JsonataExpression"
        ] = None,
        description: Optional[
            "capo_elementalinference.types.function_description.FunctionDescription"
        ] = None,
        event_bridge_delivery: Optional[
            "capo_elementalinference.types.event_bridge_delivery_mode.EventBridgeDeliveryMode"
        ] = None,
        tags: Optional["capo_elementalinference.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_elementalinference.types.create_function_response.CreateFunctionResponse"
    ):
        """<p>Creates a function. A function analyzes a feed by building a request from the feed's media and metadata, optionally sending that request to an Amazon Bedrock model in your account, and publishing the result to the feed's metadata timeline. </p> <p>A function runs only after you attach it to a feed as a function output. For more information, see <a href="https://docs.aws.amazon.com/elemental-inference/latest/userguide/functions.html">Using functions</a> in the <i>AWS Elemental Inference User Guide</i>. </p>

        Args:
            name: <p>A name for this function.</p>
            target: <p>The destination for the request that the function builds.</p>
            request_expression: <p>The JSONata expression that builds the request. Elemental Inference evaluates it against the media object of the feed, which holds the media and metadata that the function asked for. Maximum length: 5,120 characters. </p> <p>When you save the function, Elemental Inference evaluates the expression against sample media and rejects it if the evaluation fails. For a Bedrock target, the result must be a JSON object; Elemental Inference doesn't check that the object is a valid request body for the model. The expression can reference at most one of media.transcript, media.contextual, and media.clip. For a passthrough target, it can't reference media.frames. </p>
            response_expression: <p>The JSONata expression that selects what to store. Elemental Inference evaluates it against the result as its root: the model response for a Bedrock target, or the output of the request expression for a passthrough target. If a function has no response expression, Elemental Inference stores the entire result. Maximum length: 5,120 characters. </p> <p>When you save the function, Elemental Inference checks that the expression is valid JSONata. For a passthrough target, it also evaluates the request and response expressions together against sample media, and rejects them if they produce no value. </p>
            description: <p>The description of the function. Maximum length: 1,024 characters.</p>
            event_bridge_delivery: <p>Specifies whether Elemental Inference also sends this function's results to Amazon EventBridge. Elemental Inference sends a result only when the result is a JSON object with a top-level <code>eventBridge</code> field set to <code>true</code>. It sends the result, unchanged, as a Function Metadata Generated event to the default event bus in your account, after the result is available from GetMetadata. If the result is larger than 64 KB, the event has <code>resultOmitted</code> set to <code>true</code> in place of the result. </p> <p>Valid values:</p> <ul> <li> <p>ENABLED – Elemental Inference sends each marked result as an event.</p> </li> <li> <p>DISABLED (default) – Elemental Inference doesn't send events.</p> </li> </ul> <p>For a Bedrock target, ENABLED requires a response expression, because the model response itself never has a top-level <code>eventBridge</code> field. A feed output that runs a function with ENABLED can't use a fixedInterval trigger shorter than 4 seconds. </p>
            tags: <p>The tags to associate with this function.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.create_function_request.CreateFunctionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.create_function_response.CreateFunctionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_function

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.create_function.create_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_elementalinference.types.create_function_request.CreateFunctionRequest",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.create_function_request

            return (
                capo_elementalinference.types.create_function_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_elementalinference.types.create_function_response.CreateFunctionResponse",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.create_function_response

            return (
                capo_elementalinference.types.create_function_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateFunction",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_elementalinference.types.create_function_request.CreateFunctionRequest = {
            "name": name,
            "target": target,
            "request_expression": request_expression,
        }
        if response_expression is not None:
            input_["response_expression"] = response_expression
        if description is not None:
            input_["description"] = description
        if event_bridge_delivery is not None:
            input_["event_bridge_delivery"] = event_bridge_delivery
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
        id: "capo_elementalinference.types.function_id.FunctionId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.get_function_response.GetFunctionResponse":
        """<p>Retrieves the details of a function, including its expressions, the media context that Elemental Inference derived from the request expression, and the feeds that currently reference it. </p>

        Args:
            id: <p>The ID of the function.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.get_function_request.GetFunctionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.get_function_response.GetFunctionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_function

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.get_function.get_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_elementalinference.types.get_function_response.GetFunctionResponse",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.get_function_response

            return capo_elementalinference.types.get_function_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetFunction", redact_output=_redact_output),
        )
        input_: capo_elementalinference.types.get_function_request.GetFunctionRequest = {
            "id": id
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
        id: "capo_elementalinference.types.function_id.FunctionId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        name: Optional[
            "capo_elementalinference.types.resource_name.ResourceName"
        ] = None,
        target: Optional[
            "capo_elementalinference.types.function_target.FunctionTarget"
        ] = None,
        request_expression: Optional[
            "capo_elementalinference.types.jsonata_expression.JsonataExpression"
        ] = None,
        response_expression: Optional[
            "capo_elementalinference.types.jsonata_expression.JsonataExpression"
        ] = None,
        description: Optional[
            "capo_elementalinference.types.function_description.FunctionDescription"
        ] = None,
        event_bridge_delivery: Optional[
            "capo_elementalinference.types.event_bridge_delivery_mode.EventBridgeDeliveryMode"
        ] = None,
    ) -> (
        "capo_elementalinference.types.update_function_response.UpdateFunctionResponse"
    ):
        """<p>Updates a function. Include only the parameters that you want to change; parameters that you don't include aren't affected. Elemental Inference validates the updated expressions in the same way as CreateFunction. </p> <p>While a feed references the function, you can change only its expressions and its description, and you can set eventBridgeDelivery to DISABLED but not to ENABLED. The request expression must keep referencing the same media context, as reported in contextTypes. Changing an expression changes the behavior of every feed that references the function. </p>

        Args:
            id: <p>The ID of the function.</p>
            name: <p>A new name for the function. You can't change the name while the function is referenced by a feed. </p>
            target: <p>A new target for the function. You can't change the target while the function is referenced by a feed. </p>
            request_expression: <p>A new request expression for the function. Elemental Inference derives contextTypes again from the new expression. While a feed references the function, the new expression must reference the same media context as the current one. </p>
            response_expression: <p>A new response expression for the function. To remove the response expression, specify an empty string. A function with a Bedrock target and eventBridgeDelivery set to ENABLED must keep a response expression. </p>
            description: <p>A new description for the function.</p>
            event_bridge_delivery: <p>Specifies whether Elemental Inference also sends this function's marked results to Amazon EventBridge, as described for CreateFunction. If you omit this parameter, the current value is kept. While a feed references the function, you can change this value to DISABLED, but not to ENABLED. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.update_function_request.UpdateFunctionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.update_function_response.UpdateFunctionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.update_function

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.update_function.update_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_elementalinference.types.update_function_request.UpdateFunctionRequest",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.update_function_request

            return (
                capo_elementalinference.types.update_function_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_elementalinference.types.update_function_response.UpdateFunctionResponse",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.update_function_response

            return (
                capo_elementalinference.types.update_function_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateFunction",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_elementalinference.types.update_function_request.UpdateFunctionRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if target is not None:
            input_["target"] = target
        if request_expression is not None:
            input_["request_expression"] = request_expression
        if response_expression is not None:
            input_["response_expression"] = response_expression
        if description is not None:
            input_["description"] = description
        if event_bridge_delivery is not None:
            input_["event_bridge_delivery"] = event_bridge_delivery

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_elementalinference.types.function_id.FunctionId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> (
        "capo_elementalinference.types.delete_function_response.DeleteFunctionResponse"
    ):
        """<p>Deletes a function. If any feed still references the function, the operation returns a ConflictException. A disabled function output still references the function. Use GetFunction to find those feeds, then remove the function output from each one with UpdateFeed, or delete the feed, before retrying. </p> <p>Deleting a function doesn't delete the metadata that it has already produced.</p>

        Args:
            id: <p>The ID of the function.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.delete_function_request.DeleteFunctionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.delete_function_response.DeleteFunctionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_function

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_function.delete_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteFunction")
        )
        input_: capo_elementalinference.types.delete_function_request.DeleteFunctionRequest = {
            "id": id
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
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_functions_response.ListFunctionsResponse":
        """<p>Lists the functions in this account, in this Region. Each entry is a summary. To get the expressions of a function, use GetFunction. </p>

        Args:
            max_results: <p>The maximum number of functions to return in one response. Valid range: 1 to 100. The default is 100. </p>
            next_token: <p>The token that identifies the page of results to return. Use the nextToken value from a previous response. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.list_functions_request.ListFunctionsRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_functions_response.ListFunctionsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_functions

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_functions.list_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_elementalinference.types.list_functions_response.ListFunctionsResponse",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.list_functions_response

            return (
                capo_elementalinference.types.list_functions_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListFunctions", redact_output=_redact_output),
        )
        input_: capo_elementalinference.types.list_functions_request.ListFunctionsRequest = {}
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


class AsyncFunctionResource:
    def __init__(self, service: AsyncElementalInferenceClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        target: "capo_elementalinference.types.function_target.FunctionTarget",
        request_expression: "capo_elementalinference.types.jsonata_expression.JsonataExpression",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        response_expression: Optional[
            "capo_elementalinference.types.jsonata_expression.JsonataExpression"
        ] = None,
        description: Optional[
            "capo_elementalinference.types.function_description.FunctionDescription"
        ] = None,
        event_bridge_delivery: Optional[
            "capo_elementalinference.types.event_bridge_delivery_mode.EventBridgeDeliveryMode"
        ] = None,
        tags: Optional["capo_elementalinference.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_elementalinference.types.create_function_response.CreateFunctionResponse"
    ):
        """<p>Creates a function. A function analyzes a feed by building a request from the feed's media and metadata, optionally sending that request to an Amazon Bedrock model in your account, and publishing the result to the feed's metadata timeline. </p> <p>A function runs only after you attach it to a feed as a function output. For more information, see <a href="https://docs.aws.amazon.com/elemental-inference/latest/userguide/functions.html">Using functions</a> in the <i>AWS Elemental Inference User Guide</i>. </p>

        Args:
            name: <p>A name for this function.</p>
            target: <p>The destination for the request that the function builds.</p>
            request_expression: <p>The JSONata expression that builds the request. Elemental Inference evaluates it against the media object of the feed, which holds the media and metadata that the function asked for. Maximum length: 5,120 characters. </p> <p>When you save the function, Elemental Inference evaluates the expression against sample media and rejects it if the evaluation fails. For a Bedrock target, the result must be a JSON object; Elemental Inference doesn't check that the object is a valid request body for the model. The expression can reference at most one of media.transcript, media.contextual, and media.clip. For a passthrough target, it can't reference media.frames. </p>
            response_expression: <p>The JSONata expression that selects what to store. Elemental Inference evaluates it against the result as its root: the model response for a Bedrock target, or the output of the request expression for a passthrough target. If a function has no response expression, Elemental Inference stores the entire result. Maximum length: 5,120 characters. </p> <p>When you save the function, Elemental Inference checks that the expression is valid JSONata. For a passthrough target, it also evaluates the request and response expressions together against sample media, and rejects them if they produce no value. </p>
            description: <p>The description of the function. Maximum length: 1,024 characters.</p>
            event_bridge_delivery: <p>Specifies whether Elemental Inference also sends this function's results to Amazon EventBridge. Elemental Inference sends a result only when the result is a JSON object with a top-level <code>eventBridge</code> field set to <code>true</code>. It sends the result, unchanged, as a Function Metadata Generated event to the default event bus in your account, after the result is available from GetMetadata. If the result is larger than 64 KB, the event has <code>resultOmitted</code> set to <code>true</code> in place of the result. </p> <p>Valid values:</p> <ul> <li> <p>ENABLED – Elemental Inference sends each marked result as an event.</p> </li> <li> <p>DISABLED (default) – Elemental Inference doesn't send events.</p> </li> </ul> <p>For a Bedrock target, ENABLED requires a response expression, because the model response itself never has a top-level <code>eventBridge</code> field. A feed output that runs a function with ENABLED can't use a fixedInterval trigger shorter than 4 seconds. </p>
            tags: <p>The tags to associate with this function.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.create_function_request.CreateFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.create_function_response.CreateFunctionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_function

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.create_function.async_create_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_elementalinference.types.create_function_request.CreateFunctionRequest",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.create_function_request

            return (
                capo_elementalinference.types.create_function_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_elementalinference.types.create_function_response.CreateFunctionResponse",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.create_function_response

            return (
                capo_elementalinference.types.create_function_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateFunction",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_elementalinference.types.create_function_request.CreateFunctionRequest = {
            "name": name,
            "target": target,
            "request_expression": request_expression,
        }
        if response_expression is not None:
            input_["response_expression"] = response_expression
        if description is not None:
            input_["description"] = description
        if event_bridge_delivery is not None:
            input_["event_bridge_delivery"] = event_bridge_delivery
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
        id: "capo_elementalinference.types.function_id.FunctionId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.get_function_response.GetFunctionResponse":
        """<p>Retrieves the details of a function, including its expressions, the media context that Elemental Inference derived from the request expression, and the feeds that currently reference it. </p>

        Args:
            id: <p>The ID of the function.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.get_function_request.GetFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.get_function_response.GetFunctionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_function

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.get_function.async_get_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_elementalinference.types.get_function_response.GetFunctionResponse",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.get_function_response

            return capo_elementalinference.types.get_function_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetFunction", redact_output=_redact_output),
        )
        input_: capo_elementalinference.types.get_function_request.GetFunctionRequest = {
            "id": id
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
        id: "capo_elementalinference.types.function_id.FunctionId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        name: Optional[
            "capo_elementalinference.types.resource_name.ResourceName"
        ] = None,
        target: Optional[
            "capo_elementalinference.types.function_target.FunctionTarget"
        ] = None,
        request_expression: Optional[
            "capo_elementalinference.types.jsonata_expression.JsonataExpression"
        ] = None,
        response_expression: Optional[
            "capo_elementalinference.types.jsonata_expression.JsonataExpression"
        ] = None,
        description: Optional[
            "capo_elementalinference.types.function_description.FunctionDescription"
        ] = None,
        event_bridge_delivery: Optional[
            "capo_elementalinference.types.event_bridge_delivery_mode.EventBridgeDeliveryMode"
        ] = None,
    ) -> (
        "capo_elementalinference.types.update_function_response.UpdateFunctionResponse"
    ):
        """<p>Updates a function. Include only the parameters that you want to change; parameters that you don't include aren't affected. Elemental Inference validates the updated expressions in the same way as CreateFunction. </p> <p>While a feed references the function, you can change only its expressions and its description, and you can set eventBridgeDelivery to DISABLED but not to ENABLED. The request expression must keep referencing the same media context, as reported in contextTypes. Changing an expression changes the behavior of every feed that references the function. </p>

        Args:
            id: <p>The ID of the function.</p>
            name: <p>A new name for the function. You can't change the name while the function is referenced by a feed. </p>
            target: <p>A new target for the function. You can't change the target while the function is referenced by a feed. </p>
            request_expression: <p>A new request expression for the function. Elemental Inference derives contextTypes again from the new expression. While a feed references the function, the new expression must reference the same media context as the current one. </p>
            response_expression: <p>A new response expression for the function. To remove the response expression, specify an empty string. A function with a Bedrock target and eventBridgeDelivery set to ENABLED must keep a response expression. </p>
            description: <p>A new description for the function.</p>
            event_bridge_delivery: <p>Specifies whether Elemental Inference also sends this function's marked results to Amazon EventBridge, as described for CreateFunction. If you omit this parameter, the current value is kept. While a feed references the function, you can change this value to DISABLED, but not to ENABLED. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.update_function_request.UpdateFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.update_function_response.UpdateFunctionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.update_function

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.update_function.async_update_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_elementalinference.types.update_function_request.UpdateFunctionRequest",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.update_function_request

            return (
                capo_elementalinference.types.update_function_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_elementalinference.types.update_function_response.UpdateFunctionResponse",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.update_function_response

            return (
                capo_elementalinference.types.update_function_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateFunction",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_elementalinference.types.update_function_request.UpdateFunctionRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if target is not None:
            input_["target"] = target
        if request_expression is not None:
            input_["request_expression"] = request_expression
        if response_expression is not None:
            input_["response_expression"] = response_expression
        if description is not None:
            input_["description"] = description
        if event_bridge_delivery is not None:
            input_["event_bridge_delivery"] = event_bridge_delivery

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id: "capo_elementalinference.types.function_id.FunctionId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> (
        "capo_elementalinference.types.delete_function_response.DeleteFunctionResponse"
    ):
        """<p>Deletes a function. If any feed still references the function, the operation returns a ConflictException. A disabled function output still references the function. Use GetFunction to find those feeds, then remove the function output from each one with UpdateFeed, or delete the feed, before retrying. </p> <p>Deleting a function doesn't delete the metadata that it has already produced.</p>

        Args:
            id: <p>The ID of the function.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.delete_function_request.DeleteFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.delete_function_response.DeleteFunctionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_function

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.delete_function.async_delete_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteFunction")
        )
        input_: capo_elementalinference.types.delete_function_request.DeleteFunctionRequest = {
            "id": id
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
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_functions_response.ListFunctionsResponse":
        """<p>Lists the functions in this account, in this Region. Each entry is a summary. To get the expressions of a function, use GetFunction. </p>

        Args:
            max_results: <p>The maximum number of functions to return in one response. Valid range: 1 to 100. The default is 100. </p>
            next_token: <p>The token that identifies the page of results to return. Use the nextToken value from a previous response. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elementalinference.types.list_functions_request.ListFunctionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_elementalinference.types.list_functions_response.ListFunctionsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_functions

            (
                output,
                http_response,
            ) = await capo_elementalinference._operations.elemental_inference.list_functions.async_list_functions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_elementalinference.types.list_functions_response.ListFunctionsResponse",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.list_functions_response

            return (
                capo_elementalinference.types.list_functions_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListFunctions", redact_output=_redact_output),
        )
        input_: capo_elementalinference.types.list_functions_request.ListFunctionsRequest = {}
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
