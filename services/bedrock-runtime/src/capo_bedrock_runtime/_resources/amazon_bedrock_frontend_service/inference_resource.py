from __future__ import annotations

from collections.abc import AsyncGenerator, AsyncIterator, Generator, Iterator
from contextlib import asynccontextmanager, contextmanager
from typing import TYPE_CHECKING, Optional

import capo_bedrock_runtime._auth._signers
import capo_bedrock_runtime._auth._sigv4
from capo_bedrock_runtime._iter import ensure_async_iterator, ensure_sync_iterator
from capo_bedrock_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.additional_model_response_field_paths
    import capo_bedrock_runtime.types.body
    import capo_bedrock_runtime.types.conversational_model_id
    import capo_bedrock_runtime.types.converse_request
    import capo_bedrock_runtime.types.converse_response
    import capo_bedrock_runtime.types.converse_stream_request
    import capo_bedrock_runtime.types.converse_stream_response
    import capo_bedrock_runtime.types.guardrail_configuration
    import capo_bedrock_runtime.types.guardrail_identifier
    import capo_bedrock_runtime.types.guardrail_stream_configuration
    import capo_bedrock_runtime.types.guardrail_version
    import capo_bedrock_runtime.types.inference_configuration
    import capo_bedrock_runtime.types.invoke_model_identifier
    import capo_bedrock_runtime.types.invoke_model_request
    import capo_bedrock_runtime.types.invoke_model_response
    import capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input
    import capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request
    import capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response
    import capo_bedrock_runtime.types.invoke_model_with_response_stream_request
    import capo_bedrock_runtime.types.invoke_model_with_response_stream_response
    import capo_bedrock_runtime.types.messages
    import capo_bedrock_runtime.types.mime_type
    import capo_bedrock_runtime.types.output_config
    import capo_bedrock_runtime.types.performance_config_latency
    import capo_bedrock_runtime.types.performance_configuration
    import capo_bedrock_runtime.types.prompt_variable_map
    import capo_bedrock_runtime.types.request_metadata
    import capo_bedrock_runtime.types.request_metadata_json
    import capo_bedrock_runtime.types.service_tier
    import capo_bedrock_runtime.types.service_tier_type
    import capo_bedrock_runtime.types.system_content_blocks
    import capo_bedrock_runtime.types.tool_configuration
    import capo_bedrock_runtime.types.trace
    from capo_bedrock_runtime._services.async_bedrock_runtime import (
        AsyncBedrockRuntimeClient,
        AsyncBedrockRuntimeClientConfig,
    )
    from capo_bedrock_runtime._services.bedrock_runtime import (
        BedrockRuntimeClient,
        BedrockRuntimeClientConfig,
    )


class InferenceResource:
    def __init__(self, service: BedrockRuntimeClient) -> None:
        self._service = service

    def converse(
        self,
        model_id: "capo_bedrock_runtime.types.conversational_model_id.ConversationalModelId",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
        messages: Optional["capo_bedrock_runtime.types.messages.Messages"] = None,
        system: Optional[
            "capo_bedrock_runtime.types.system_content_blocks.SystemContentBlocks"
        ] = None,
        inference_config: Optional[
            "capo_bedrock_runtime.types.inference_configuration.InferenceConfiguration"
        ] = None,
        tool_config: Optional[
            "capo_bedrock_runtime.types.tool_configuration.ToolConfiguration"
        ] = None,
        guardrail_config: Optional[
            "capo_bedrock_runtime.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        additional_model_request_fields: Optional[object] = None,
        prompt_variables: Optional[
            "capo_bedrock_runtime.types.prompt_variable_map.PromptVariableMap"
        ] = None,
        additional_model_response_field_paths: Optional[
            "capo_bedrock_runtime.types.additional_model_response_field_paths.AdditionalModelResponseFieldPaths"
        ] = None,
        request_metadata: Optional[
            "capo_bedrock_runtime.types.request_metadata.RequestMetadata"
        ] = None,
        performance_config: Optional[
            "capo_bedrock_runtime.types.performance_configuration.PerformanceConfiguration"
        ] = None,
        service_tier: Optional[
            "capo_bedrock_runtime.types.service_tier.ServiceTier"
        ] = None,
        output_config: Optional[
            "capo_bedrock_runtime.types.output_config.OutputConfig"
        ] = None,
    ) -> "capo_bedrock_runtime.types.converse_response.ConverseResponse":
        """<p>Sends messages to the specified Amazon Bedrock model. <code>Converse</code> provides a consistent interface that works with all models that support messages. This allows you to write code once and use it with different models. If a model has unique inference parameters, you can also pass those unique parameters to the model.</p> <p>Amazon Bedrock doesn't store any text, images, or documents that you provide as content. The data is only used to generate the response.</p> <p>You can submit a prompt by including it in the <code>messages</code> field, specifying the <code>modelId</code> of a foundation model or inference profile to run inference on it, and including any other fields that are relevant to your use case.</p> <p>You can also submit a prompt from Prompt management by specifying the ARN of the prompt version and including a map of variables to values in the <code>promptVariables</code> field. You can append more messages to the prompt by using the <code>messages</code> field. If you use a prompt from Prompt management, you can't include the following fields in the request: <code>additionalModelRequestFields</code>, <code>inferenceConfig</code>, <code>system</code>, or <code>toolConfig</code>. Instead, these fields must be defined through Prompt management. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-use.html">Use a prompt from Prompt management</a>.</p> <p>For information about the Converse API, see <i>Use the Converse API</i> in the <i>Amazon Bedrock User Guide</i>. To use a guardrail, see <i>Use a guardrail with the Converse API</i> in the <i>Amazon Bedrock User Guide</i>. To use a tool with a model, see <i>Tool use (Function calling)</i> in the <i>Amazon Bedrock User Guide</i> </p> <p>For example code, see <i>Converse API examples</i> in the <i>Amazon Bedrock User Guide</i>. </p> <p>This operation requires permission for the <code>bedrock:InvokeModel</code> action. </p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the base inference actions (<a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html">InvokeModel</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html">InvokeModelWithResponseStream</a>). For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference">Deny access for inference on specific models</a>. </p> </important> <p>For troubleshooting some of the common errors you might encounter when using the <code>Converse</code> API, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            model_id: <p>Specifies the model or throughput with which to run inference, or the prompt resource to use in inference. The value depends on the resource that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>To include a prompt that was defined in <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html">Prompt management</a>, specify the ARN of the prompt version to use.</p> </li> </ul> <p>The Converse API doesn't support <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported models</a>.</p>
            messages: <p>The messages that you want to send to the model.</p>
            system: <p>A prompt that provides instructions or context to the model about the task it should perform, or the persona it should adopt during the conversation.</p>
            inference_config: <p>Inference parameters to pass to the model. <code>Converse</code> and <code>ConverseStream</code> support a base set of inference parameters. If you need to pass additional parameters that the model supports, use the <code>additionalModelRequestFields</code> request field.</p>
            tool_config: <p>Configuration information for the tools that the model can use when generating a response. </p> <p>For information about models that support tool use, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html#conversation-inference-supported-models-features">Supported models and model features</a>.</p>
            guardrail_config: <p>Configuration information for a guardrail that you want to use in the request. If you include <code>guardContent</code> blocks in the <code>content</code> field in the <code>messages</code> field, the guardrail operates only on those messages. If you include no <code>guardContent</code> blocks, the guardrail operates on all messages in the request body and in any included prompt resource.</p>
            additional_model_request_fields: <p>Additional inference parameters that the model supports, beyond the base set of inference parameters that <code>Converse</code> and <code>ConverseStream</code> support in the <code>inferenceConfig</code> field. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Model parameters</a>.</p>
            prompt_variables: <p>Contains a map of variables in a prompt from Prompt management to objects containing the values to fill in for them when running model invocation. This field is ignored if you don't specify a prompt resource in the <code>modelId</code> field.</p>
            additional_model_response_field_paths: <p>Additional model parameters field paths to return in the response. <code>Converse</code> and <code>ConverseStream</code> return the requested fields as a JSON Pointer object in the <code>additionalModelResponseFields</code> field. The following is example JSON for <code>additionalModelResponseFieldPaths</code>.</p> <p> <code>[ "/stop_sequence" ]</code> </p> <p>For information about the JSON Pointer syntax, see the <a href="https://datatracker.ietf.org/doc/html/rfc6901">Internet Engineering Task Force (IETF)</a> documentation.</p> <p> <code>Converse</code> and <code>ConverseStream</code> reject an empty JSON Pointer or incorrectly structured JSON Pointer with a <code>400</code> error code. if the JSON Pointer is valid, but the requested field is not in the model response, it is ignored by <code>Converse</code>.</p>
            request_metadata: <p>Key-value pairs that you can use to filter invocation logs.</p>
            performance_config: <p>Model performance settings for the request.</p>
            service_tier: <p>Specifies the processing tier configuration used for serving the request.</p>
            output_config: <p>Output configuration for a model response.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.converse_request.ConverseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.converse_response.ConverseResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.converse

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.converse.converse(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.converse_request.ConverseRequest = {
            "model_id": model_id
        }
        if messages is not None:
            input_["messages"] = messages
        if system is not None:
            input_["system"] = system
        if inference_config is not None:
            input_["inference_config"] = inference_config
        if tool_config is not None:
            input_["tool_config"] = tool_config
        if guardrail_config is not None:
            input_["guardrail_config"] = guardrail_config
        if additional_model_request_fields is not None:
            input_["additional_model_request_fields"] = additional_model_request_fields
        if prompt_variables is not None:
            input_["prompt_variables"] = prompt_variables
        if additional_model_response_field_paths is not None:
            input_["additional_model_response_field_paths"] = (
                additional_model_response_field_paths
            )
        if request_metadata is not None:
            input_["request_metadata"] = request_metadata
        if performance_config is not None:
            input_["performance_config"] = performance_config
        if service_tier is not None:
            input_["service_tier"] = service_tier
        if output_config is not None:
            input_["output_config"] = output_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def converse_stream(
        self,
        model_id: "capo_bedrock_runtime.types.conversational_model_id.ConversationalModelId",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
        messages: Optional["capo_bedrock_runtime.types.messages.Messages"] = None,
        system: Optional[
            "capo_bedrock_runtime.types.system_content_blocks.SystemContentBlocks"
        ] = None,
        inference_config: Optional[
            "capo_bedrock_runtime.types.inference_configuration.InferenceConfiguration"
        ] = None,
        tool_config: Optional[
            "capo_bedrock_runtime.types.tool_configuration.ToolConfiguration"
        ] = None,
        guardrail_config: Optional[
            "capo_bedrock_runtime.types.guardrail_stream_configuration.GuardrailStreamConfiguration"
        ] = None,
        additional_model_request_fields: Optional[object] = None,
        prompt_variables: Optional[
            "capo_bedrock_runtime.types.prompt_variable_map.PromptVariableMap"
        ] = None,
        additional_model_response_field_paths: Optional[
            "capo_bedrock_runtime.types.additional_model_response_field_paths.AdditionalModelResponseFieldPaths"
        ] = None,
        request_metadata: Optional[
            "capo_bedrock_runtime.types.request_metadata.RequestMetadata"
        ] = None,
        performance_config: Optional[
            "capo_bedrock_runtime.types.performance_configuration.PerformanceConfiguration"
        ] = None,
        service_tier: Optional[
            "capo_bedrock_runtime.types.service_tier.ServiceTier"
        ] = None,
        output_config: Optional[
            "capo_bedrock_runtime.types.output_config.OutputConfig"
        ] = None,
    ) -> "Generator[capo_bedrock_runtime.types.converse_stream_response.ConverseStreamResponse]":
        """<p>Sends messages to the specified Amazon Bedrock model and returns the response in a stream. <code>ConverseStream</code> provides a consistent API that works with all Amazon Bedrock models that support messages. This allows you to write code once and use it with different models. Should a model have unique inference parameters, you can also pass those unique parameters to the model. </p> <p>To find out if a model supports streaming, call <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetFoundationModel.html">GetFoundationModel</a> and check the <code>responseStreamingSupported</code> field in the response.</p> <note> <p>The CLI doesn't support streaming operations in Amazon Bedrock, including <code>ConverseStream</code>.</p> </note> <p>Amazon Bedrock doesn't store any text, images, or documents that you provide as content. The data is only used to generate the response.</p> <p>You can submit a prompt by including it in the <code>messages</code> field, specifying the <code>modelId</code> of a foundation model or inference profile to run inference on it, and including any other fields that are relevant to your use case.</p> <p>You can also submit a prompt from Prompt management by specifying the ARN of the prompt version and including a map of variables to values in the <code>promptVariables</code> field. You can append more messages to the prompt by using the <code>messages</code> field. If you use a prompt from Prompt management, you can't include the following fields in the request: <code>additionalModelRequestFields</code>, <code>inferenceConfig</code>, <code>system</code>, or <code>toolConfig</code>. Instead, these fields must be defined through Prompt management. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-use.html">Use a prompt from Prompt management</a>.</p> <p>For information about the Converse API, see <i>Use the Converse API</i> in the <i>Amazon Bedrock User Guide</i>. To use a guardrail, see <i>Use a guardrail with the Converse API</i> in the <i>Amazon Bedrock User Guide</i>. To use a tool with a model, see <i>Tool use (Function calling)</i> in the <i>Amazon Bedrock User Guide</i> </p> <p>For example code, see <i>Conversation streaming example</i> in the <i>Amazon Bedrock User Guide</i>. </p> <p>This operation requires permission for the <code>bedrock:InvokeModelWithResponseStream</code> action.</p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the base inference actions (<a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html">InvokeModel</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html">InvokeModelWithResponseStream</a>). For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference">Deny access for inference on specific models</a>. </p> </important> <p>For troubleshooting some of the common errors you might encounter when using the <code>ConverseStream</code> API, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            model_id: <p>Specifies the model or throughput with which to run inference, or the prompt resource to use in inference. The value depends on the resource that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>To include a prompt that was defined in <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html">Prompt management</a>, specify the ARN of the prompt version to use.</p> </li> </ul> <p>The Converse API doesn't support <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported models</a>.</p>
            messages: <p>The messages that you want to send to the model.</p>
            system: <p>A prompt that provides instructions or context to the model about the task it should perform, or the persona it should adopt during the conversation.</p>
            inference_config: <p>Inference parameters to pass to the model. <code>Converse</code> and <code>ConverseStream</code> support a base set of inference parameters. If you need to pass additional parameters that the model supports, use the <code>additionalModelRequestFields</code> request field.</p>
            tool_config: <p>Configuration information for the tools that the model can use when generating a response.</p> <p>For information about models that support streaming tool use, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html#conversation-inference-supported-models-features">Supported models and model features</a>.</p>
            guardrail_config: <p>Configuration information for a guardrail that you want to use in the request. If you include <code>guardContent</code> blocks in the <code>content</code> field in the <code>messages</code> field, the guardrail operates only on those messages. If you include no <code>guardContent</code> blocks, the guardrail operates on all messages in the request body and in any included prompt resource.</p>
            additional_model_request_fields: <p>Additional inference parameters that the model supports, beyond the base set of inference parameters that <code>Converse</code> and <code>ConverseStream</code> support in the <code>inferenceConfig</code> field. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Model parameters</a>.</p>
            prompt_variables: <p>Contains a map of variables in a prompt from Prompt management to objects containing the values to fill in for them when running model invocation. This field is ignored if you don't specify a prompt resource in the <code>modelId</code> field.</p>
            additional_model_response_field_paths: <p>Additional model parameters field paths to return in the response. <code>Converse</code> and <code>ConverseStream</code> return the requested fields as a JSON Pointer object in the <code>additionalModelResponseFields</code> field. The following is example JSON for <code>additionalModelResponseFieldPaths</code>.</p> <p> <code>[ "/stop_sequence" ]</code> </p> <p>For information about the JSON Pointer syntax, see the <a href="https://datatracker.ietf.org/doc/html/rfc6901">Internet Engineering Task Force (IETF)</a> documentation.</p> <p> <code>Converse</code> and <code>ConverseStream</code> reject an empty JSON Pointer or incorrectly structured JSON Pointer with a <code>400</code> error code. if the JSON Pointer is valid, but the requested field is not in the model response, it is ignored by <code>Converse</code>.</p>
            request_metadata: <p>Key-value pairs that you can use to filter invocation logs.</p>
            performance_config: <p>Model performance settings for the request.</p>
            service_tier: <p>Specifies the processing tier configuration used for serving the request.</p>
            output_config: <p>Output configuration for a model response.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.converse_stream_request.ConverseStreamRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.converse_stream_response.ConverseStreamResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.converse_stream

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.converse_stream.converse_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.converse_stream_request.ConverseStreamRequest = {
            "model_id": model_id
        }
        if messages is not None:
            input_["messages"] = messages
        if system is not None:
            input_["system"] = system
        if inference_config is not None:
            input_["inference_config"] = inference_config
        if tool_config is not None:
            input_["tool_config"] = tool_config
        if guardrail_config is not None:
            input_["guardrail_config"] = guardrail_config
        if additional_model_request_fields is not None:
            input_["additional_model_request_fields"] = additional_model_request_fields
        if prompt_variables is not None:
            input_["prompt_variables"] = prompt_variables
        if additional_model_response_field_paths is not None:
            input_["additional_model_response_field_paths"] = (
                additional_model_response_field_paths
            )
        if request_metadata is not None:
            input_["request_metadata"] = request_metadata
        if performance_config is not None:
            input_["performance_config"] = performance_config
        if service_tier is not None:
            input_["service_tier"] = service_tier
        if output_config is not None:
            input_["output_config"] = output_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def invoke_model(
        self,
        model_id: "capo_bedrock_runtime.types.invoke_model_identifier.InvokeModelIdentifier",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
        body: Optional["capo_bedrock_runtime.types.body.Body"] = None,
        content_type: Optional["capo_bedrock_runtime.types.mime_type.MimeType"] = None,
        accept: Optional["capo_bedrock_runtime.types.mime_type.MimeType"] = None,
        trace: Optional["capo_bedrock_runtime.types.trace.Trace"] = None,
        guardrail_identifier: Optional[
            "capo_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier"
        ] = None,
        guardrail_version: Optional[
            "capo_bedrock_runtime.types.guardrail_version.GuardrailVersion"
        ] = None,
        performance_config_latency: Optional[
            "capo_bedrock_runtime.types.performance_config_latency.PerformanceConfigLatency"
        ] = None,
        service_tier: Optional[
            "capo_bedrock_runtime.types.service_tier_type.ServiceTierType"
        ] = None,
        request_metadata: Optional[
            "capo_bedrock_runtime.types.request_metadata_json.RequestMetadataJson"
        ] = None,
    ) -> "capo_bedrock_runtime.types.invoke_model_response.InvokeModelResponse":
        """<p>Invokes the specified Amazon Bedrock model to run inference using the prompt and inference parameters provided in the request body. You use model inference to generate text, images, and embeddings.</p> <p>For example code, see <i>Invoke model code examples</i> in the <i>Amazon Bedrock User Guide</i>. </p> <p>This operation requires permission for the <code>bedrock:InvokeModel</code> action.</p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the Converse API actions (<a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html">Converse</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html">ConverseStream</a>). For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference">Deny access for inference on specific models</a>. </p> </important> <p>For troubleshooting some of the common errors you might encounter when using the <code>InvokeModel</code> API, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            body: <p>The prompt and inference parameters in the format specified in the <code>contentType</code> in the header. You must provide the body in JSON format. To see the format and content of the request and response bodies for different models, refer to <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters</a>. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/api-methods-run.html">Run inference</a> in the Bedrock User Guide.</p>
            content_type: <p>The MIME type of the input data in the request. You must specify <code>application/json</code>.</p>
            accept: <p>The desired MIME type of the inference body in the response. The default value is <code>application/json</code>.</p>
            model_id: <p>The unique identifier of the model to invoke to run inference.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, specify the ARN of the custom model deployment (for on-demand inference) or the ARN of your provisioned model (for Provisioned Throughput). For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            trace: <p>Specifies whether to enable or disable the Bedrock trace. If enabled, you can see the full Bedrock trace.</p>
            guardrail_identifier: <p>The unique identifier of the guardrail that you want to use. If you don't provide a value, no guardrail is applied to the invocation.</p> <p>An error will be thrown in the following situations.</p> <ul> <li> <p>You don't provide a guardrail identifier but you specify the <code>amazon-bedrock-guardrailConfig</code> field in the request body.</p> </li> <li> <p>You enable the guardrail but the <code>contentType</code> isn't <code>application/json</code>.</p> </li> <li> <p>You provide a guardrail identifier, but <code>guardrailVersion</code> isn't specified.</p> </li> </ul>
            guardrail_version: <p>The version number for the guardrail. The value can also be <code>DRAFT</code>.</p>
            performance_config_latency: <p>Model performance settings for the request.</p>
            service_tier: <p>Specifies the processing tier type used for serving the request.</p>
            request_metadata: <p>Key-value pairs that you can use to filter invocation logs.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds the service quota for your account. You can view your quotas at <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html">Viewing service quotas</a>. You can resubmit your request later.</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.invoke_model_request.InvokeModelRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.invoke_model_response.InvokeModelResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model.invoke_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.invoke_model_request.InvokeModelRequest = {
            "model_id": model_id
        }
        if body is not None:
            input_["body"] = body
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if trace is not None:
            input_["trace"] = trace
        if guardrail_identifier is not None:
            input_["guardrail_identifier"] = guardrail_identifier
        if guardrail_version is not None:
            input_["guardrail_version"] = guardrail_version
        if performance_config_latency is not None:
            input_["performance_config_latency"] = performance_config_latency
        if service_tier is not None:
            input_["service_tier"] = service_tier
        if request_metadata is not None:
            input_["request_metadata"] = request_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def invoke_model_with_bidirectional_stream(
        self,
        model_id: "capo_bedrock_runtime.types.invoke_model_identifier.InvokeModelIdentifier",
        body: "Iterator[capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input._InvokeModelWithBidirectionalStreamInput] | capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input._InvokeModelWithBidirectionalStreamInput",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
    ) -> "Generator[capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse]":
        """<p>Invoke the specified Amazon Bedrock model to run inference using the bidirectional stream. The response is returned in a stream that remains open for 8 minutes. A single session can contain multiple prompts and responses from the model. The prompts to the model are provided as audio files and the model's responses are spoken back to the user and transcribed.</p> <p>It is possible for users to interrupt the model's response with a new prompt, which will halt the response speech. The model will retain contextual awareness of the conversation while pivoting to respond to the new prompt.</p>

        Args:
            model_id: <p>The model ID or ARN of the model ID to use. Currently, only <code>amazon.nova-sonic-v1:0</code> is supported.</p>
            body: <p>The prompt and inference parameters in the format specified in the <code>BidirectionalInputPayloadPart</code> in the header. You must provide the body in JSON format. To see the format and content of the request and response bodies for different models, refer to <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters</a>. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/api-methods-run.html">Run inference</a> in the Bedrock User Guide.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException: <p>An error occurred while streaming the response. Retry your request.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds the service quota for your account. You can view your quotas at <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html">Viewing service quotas</a>. You can resubmit your request later.</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model_with_bidirectional_stream

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model_with_bidirectional_stream.invoke_model_with_bidirectional_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest = {
            "model_id": model_id,
            "body": ensure_sync_iterator(body),
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    @contextmanager
    def invoke_model_with_response_stream(
        self,
        model_id: "capo_bedrock_runtime.types.invoke_model_identifier.InvokeModelIdentifier",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
        body: Optional["capo_bedrock_runtime.types.body.Body"] = None,
        content_type: Optional["capo_bedrock_runtime.types.mime_type.MimeType"] = None,
        accept: Optional["capo_bedrock_runtime.types.mime_type.MimeType"] = None,
        trace: Optional["capo_bedrock_runtime.types.trace.Trace"] = None,
        guardrail_identifier: Optional[
            "capo_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier"
        ] = None,
        guardrail_version: Optional[
            "capo_bedrock_runtime.types.guardrail_version.GuardrailVersion"
        ] = None,
        performance_config_latency: Optional[
            "capo_bedrock_runtime.types.performance_config_latency.PerformanceConfigLatency"
        ] = None,
        service_tier: Optional[
            "capo_bedrock_runtime.types.service_tier_type.ServiceTierType"
        ] = None,
        request_metadata: Optional[
            "capo_bedrock_runtime.types.request_metadata_json.RequestMetadataJson"
        ] = None,
    ) -> "Generator[capo_bedrock_runtime.types.invoke_model_with_response_stream_response.InvokeModelWithResponseStreamResponse]":
        """<p>Invoke the specified Amazon Bedrock model to run inference using the prompt and inference parameters provided in the request body. The response is returned in a stream.</p> <p>To see if a model supports streaming, call <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetFoundationModel.html">GetFoundationModel</a> and check the <code>responseStreamingSupported</code> field in the response.</p> <note> <p>The CLI doesn't support streaming operations in Amazon Bedrock, including <code>InvokeModelWithResponseStream</code>.</p> </note> <p>For example code, see <i>Invoke model with streaming code example</i> in the <i>Amazon Bedrock User Guide</i>. </p> <p>This operation requires permissions to perform the <code>bedrock:InvokeModelWithResponseStream</code> action. </p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the Converse API actions (<a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html">Converse</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html">ConverseStream</a>). For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference">Deny access for inference on specific models</a>. </p> </important> <p>For troubleshooting some of the common errors you might encounter when using the <code>InvokeModelWithResponseStream</code> API, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            body: <p>The prompt and inference parameters in the format specified in the <code>contentType</code> in the header. You must provide the body in JSON format. To see the format and content of the request and response bodies for different models, refer to <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters</a>. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/api-methods-run.html">Run inference</a> in the Bedrock User Guide.</p>
            content_type: <p>The MIME type of the input data in the request. You must specify <code>application/json</code>.</p>
            accept: <p>The desired MIME type of the inference body in the response. The default value is <code>application/json</code>.</p>
            model_id: <p>The unique identifier of the model to invoke to run inference.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, specify the ARN of the custom model deployment (for on-demand inference) or the ARN of your provisioned model (for Provisioned Throughput). For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            trace: <p>Specifies whether to enable or disable the Bedrock trace. If enabled, you can see the full Bedrock trace.</p>
            guardrail_identifier: <p>The unique identifier of the guardrail that you want to use. If you don't provide a value, no guardrail is applied to the invocation.</p> <p>An error is thrown in the following situations.</p> <ul> <li> <p>You don't provide a guardrail identifier but you specify the <code>amazon-bedrock-guardrailConfig</code> field in the request body.</p> </li> <li> <p>You enable the guardrail but the <code>contentType</code> isn't <code>application/json</code>.</p> </li> <li> <p>You provide a guardrail identifier, but <code>guardrailVersion</code> isn't specified.</p> </li> </ul>
            guardrail_version: <p>The version number for the guardrail. The value can also be <code>DRAFT</code>.</p>
            performance_config_latency: <p>Model performance settings for the request.</p>
            service_tier: <p>Specifies the processing tier type used for serving the request.</p>
            request_metadata: <p>Key-value pairs that you can use to filter invocation logs.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException: <p>An error occurred while streaming the response. Retry your request.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds the service quota for your account. You can view your quotas at <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html">Viewing service quotas</a>. You can resubmit your request later.</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.invoke_model_with_response_stream_request.InvokeModelWithResponseStreamRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.invoke_model_with_response_stream_response.InvokeModelWithResponseStreamResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model_with_response_stream

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model_with_response_stream.invoke_model_with_response_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.invoke_model_with_response_stream_request.InvokeModelWithResponseStreamRequest = {
            "model_id": model_id
        }
        if body is not None:
            input_["body"] = body
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if trace is not None:
            input_["trace"] = trace
        if guardrail_identifier is not None:
            input_["guardrail_identifier"] = guardrail_identifier
        if guardrail_version is not None:
            input_["guardrail_version"] = guardrail_version
        if performance_config_latency is not None:
            input_["performance_config_latency"] = performance_config_latency
        if service_tier is not None:
            input_["service_tier"] = service_tier
        if request_metadata is not None:
            input_["request_metadata"] = request_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()


class AsyncInferenceResource:
    def __init__(self, service: AsyncBedrockRuntimeClient) -> None:
        self._service = service

    async def converse(
        self,
        model_id: "capo_bedrock_runtime.types.conversational_model_id.ConversationalModelId",
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
        messages: Optional["capo_bedrock_runtime.types.messages.Messages"] = None,
        system: Optional[
            "capo_bedrock_runtime.types.system_content_blocks.SystemContentBlocks"
        ] = None,
        inference_config: Optional[
            "capo_bedrock_runtime.types.inference_configuration.InferenceConfiguration"
        ] = None,
        tool_config: Optional[
            "capo_bedrock_runtime.types.tool_configuration.ToolConfiguration"
        ] = None,
        guardrail_config: Optional[
            "capo_bedrock_runtime.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        additional_model_request_fields: Optional[object] = None,
        prompt_variables: Optional[
            "capo_bedrock_runtime.types.prompt_variable_map.PromptVariableMap"
        ] = None,
        additional_model_response_field_paths: Optional[
            "capo_bedrock_runtime.types.additional_model_response_field_paths.AdditionalModelResponseFieldPaths"
        ] = None,
        request_metadata: Optional[
            "capo_bedrock_runtime.types.request_metadata.RequestMetadata"
        ] = None,
        performance_config: Optional[
            "capo_bedrock_runtime.types.performance_configuration.PerformanceConfiguration"
        ] = None,
        service_tier: Optional[
            "capo_bedrock_runtime.types.service_tier.ServiceTier"
        ] = None,
        output_config: Optional[
            "capo_bedrock_runtime.types.output_config.OutputConfig"
        ] = None,
    ) -> "capo_bedrock_runtime.types.converse_response.ConverseResponse":
        """<p>Sends messages to the specified Amazon Bedrock model. <code>Converse</code> provides a consistent interface that works with all models that support messages. This allows you to write code once and use it with different models. If a model has unique inference parameters, you can also pass those unique parameters to the model.</p> <p>Amazon Bedrock doesn't store any text, images, or documents that you provide as content. The data is only used to generate the response.</p> <p>You can submit a prompt by including it in the <code>messages</code> field, specifying the <code>modelId</code> of a foundation model or inference profile to run inference on it, and including any other fields that are relevant to your use case.</p> <p>You can also submit a prompt from Prompt management by specifying the ARN of the prompt version and including a map of variables to values in the <code>promptVariables</code> field. You can append more messages to the prompt by using the <code>messages</code> field. If you use a prompt from Prompt management, you can't include the following fields in the request: <code>additionalModelRequestFields</code>, <code>inferenceConfig</code>, <code>system</code>, or <code>toolConfig</code>. Instead, these fields must be defined through Prompt management. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-use.html">Use a prompt from Prompt management</a>.</p> <p>For information about the Converse API, see <i>Use the Converse API</i> in the <i>Amazon Bedrock User Guide</i>. To use a guardrail, see <i>Use a guardrail with the Converse API</i> in the <i>Amazon Bedrock User Guide</i>. To use a tool with a model, see <i>Tool use (Function calling)</i> in the <i>Amazon Bedrock User Guide</i> </p> <p>For example code, see <i>Converse API examples</i> in the <i>Amazon Bedrock User Guide</i>. </p> <p>This operation requires permission for the <code>bedrock:InvokeModel</code> action. </p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the base inference actions (<a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html">InvokeModel</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html">InvokeModelWithResponseStream</a>). For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference">Deny access for inference on specific models</a>. </p> </important> <p>For troubleshooting some of the common errors you might encounter when using the <code>Converse</code> API, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            model_id: <p>Specifies the model or throughput with which to run inference, or the prompt resource to use in inference. The value depends on the resource that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>To include a prompt that was defined in <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html">Prompt management</a>, specify the ARN of the prompt version to use.</p> </li> </ul> <p>The Converse API doesn't support <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported models</a>.</p>
            messages: <p>The messages that you want to send to the model.</p>
            system: <p>A prompt that provides instructions or context to the model about the task it should perform, or the persona it should adopt during the conversation.</p>
            inference_config: <p>Inference parameters to pass to the model. <code>Converse</code> and <code>ConverseStream</code> support a base set of inference parameters. If you need to pass additional parameters that the model supports, use the <code>additionalModelRequestFields</code> request field.</p>
            tool_config: <p>Configuration information for the tools that the model can use when generating a response. </p> <p>For information about models that support tool use, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html#conversation-inference-supported-models-features">Supported models and model features</a>.</p>
            guardrail_config: <p>Configuration information for a guardrail that you want to use in the request. If you include <code>guardContent</code> blocks in the <code>content</code> field in the <code>messages</code> field, the guardrail operates only on those messages. If you include no <code>guardContent</code> blocks, the guardrail operates on all messages in the request body and in any included prompt resource.</p>
            additional_model_request_fields: <p>Additional inference parameters that the model supports, beyond the base set of inference parameters that <code>Converse</code> and <code>ConverseStream</code> support in the <code>inferenceConfig</code> field. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Model parameters</a>.</p>
            prompt_variables: <p>Contains a map of variables in a prompt from Prompt management to objects containing the values to fill in for them when running model invocation. This field is ignored if you don't specify a prompt resource in the <code>modelId</code> field.</p>
            additional_model_response_field_paths: <p>Additional model parameters field paths to return in the response. <code>Converse</code> and <code>ConverseStream</code> return the requested fields as a JSON Pointer object in the <code>additionalModelResponseFields</code> field. The following is example JSON for <code>additionalModelResponseFieldPaths</code>.</p> <p> <code>[ "/stop_sequence" ]</code> </p> <p>For information about the JSON Pointer syntax, see the <a href="https://datatracker.ietf.org/doc/html/rfc6901">Internet Engineering Task Force (IETF)</a> documentation.</p> <p> <code>Converse</code> and <code>ConverseStream</code> reject an empty JSON Pointer or incorrectly structured JSON Pointer with a <code>400</code> error code. if the JSON Pointer is valid, but the requested field is not in the model response, it is ignored by <code>Converse</code>.</p>
            request_metadata: <p>Key-value pairs that you can use to filter invocation logs.</p>
            performance_config: <p>Model performance settings for the request.</p>
            service_tier: <p>Specifies the processing tier configuration used for serving the request.</p>
            output_config: <p>Output configuration for a model response.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_runtime.types.converse_request.ConverseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_runtime.types.converse_response.ConverseResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.converse

            (
                output,
                http_response,
            ) = await capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.converse.async_converse(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.converse_request.ConverseRequest = {
            "model_id": model_id
        }
        if messages is not None:
            input_["messages"] = messages
        if system is not None:
            input_["system"] = system
        if inference_config is not None:
            input_["inference_config"] = inference_config
        if tool_config is not None:
            input_["tool_config"] = tool_config
        if guardrail_config is not None:
            input_["guardrail_config"] = guardrail_config
        if additional_model_request_fields is not None:
            input_["additional_model_request_fields"] = additional_model_request_fields
        if prompt_variables is not None:
            input_["prompt_variables"] = prompt_variables
        if additional_model_response_field_paths is not None:
            input_["additional_model_response_field_paths"] = (
                additional_model_response_field_paths
            )
        if request_metadata is not None:
            input_["request_metadata"] = request_metadata
        if performance_config is not None:
            input_["performance_config"] = performance_config
        if service_tier is not None:
            input_["service_tier"] = service_tier
        if output_config is not None:
            input_["output_config"] = output_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def converse_stream(
        self,
        model_id: "capo_bedrock_runtime.types.conversational_model_id.ConversationalModelId",
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
        messages: Optional["capo_bedrock_runtime.types.messages.Messages"] = None,
        system: Optional[
            "capo_bedrock_runtime.types.system_content_blocks.SystemContentBlocks"
        ] = None,
        inference_config: Optional[
            "capo_bedrock_runtime.types.inference_configuration.InferenceConfiguration"
        ] = None,
        tool_config: Optional[
            "capo_bedrock_runtime.types.tool_configuration.ToolConfiguration"
        ] = None,
        guardrail_config: Optional[
            "capo_bedrock_runtime.types.guardrail_stream_configuration.GuardrailStreamConfiguration"
        ] = None,
        additional_model_request_fields: Optional[object] = None,
        prompt_variables: Optional[
            "capo_bedrock_runtime.types.prompt_variable_map.PromptVariableMap"
        ] = None,
        additional_model_response_field_paths: Optional[
            "capo_bedrock_runtime.types.additional_model_response_field_paths.AdditionalModelResponseFieldPaths"
        ] = None,
        request_metadata: Optional[
            "capo_bedrock_runtime.types.request_metadata.RequestMetadata"
        ] = None,
        performance_config: Optional[
            "capo_bedrock_runtime.types.performance_configuration.PerformanceConfiguration"
        ] = None,
        service_tier: Optional[
            "capo_bedrock_runtime.types.service_tier.ServiceTier"
        ] = None,
        output_config: Optional[
            "capo_bedrock_runtime.types.output_config.OutputConfig"
        ] = None,
    ) -> "AsyncGenerator[capo_bedrock_runtime.types.converse_stream_response.ConverseStreamResponse]":
        """<p>Sends messages to the specified Amazon Bedrock model and returns the response in a stream. <code>ConverseStream</code> provides a consistent API that works with all Amazon Bedrock models that support messages. This allows you to write code once and use it with different models. Should a model have unique inference parameters, you can also pass those unique parameters to the model. </p> <p>To find out if a model supports streaming, call <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetFoundationModel.html">GetFoundationModel</a> and check the <code>responseStreamingSupported</code> field in the response.</p> <note> <p>The CLI doesn't support streaming operations in Amazon Bedrock, including <code>ConverseStream</code>.</p> </note> <p>Amazon Bedrock doesn't store any text, images, or documents that you provide as content. The data is only used to generate the response.</p> <p>You can submit a prompt by including it in the <code>messages</code> field, specifying the <code>modelId</code> of a foundation model or inference profile to run inference on it, and including any other fields that are relevant to your use case.</p> <p>You can also submit a prompt from Prompt management by specifying the ARN of the prompt version and including a map of variables to values in the <code>promptVariables</code> field. You can append more messages to the prompt by using the <code>messages</code> field. If you use a prompt from Prompt management, you can't include the following fields in the request: <code>additionalModelRequestFields</code>, <code>inferenceConfig</code>, <code>system</code>, or <code>toolConfig</code>. Instead, these fields must be defined through Prompt management. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-use.html">Use a prompt from Prompt management</a>.</p> <p>For information about the Converse API, see <i>Use the Converse API</i> in the <i>Amazon Bedrock User Guide</i>. To use a guardrail, see <i>Use a guardrail with the Converse API</i> in the <i>Amazon Bedrock User Guide</i>. To use a tool with a model, see <i>Tool use (Function calling)</i> in the <i>Amazon Bedrock User Guide</i> </p> <p>For example code, see <i>Conversation streaming example</i> in the <i>Amazon Bedrock User Guide</i>. </p> <p>This operation requires permission for the <code>bedrock:InvokeModelWithResponseStream</code> action.</p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the base inference actions (<a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html">InvokeModel</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html">InvokeModelWithResponseStream</a>). For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference">Deny access for inference on specific models</a>. </p> </important> <p>For troubleshooting some of the common errors you might encounter when using the <code>ConverseStream</code> API, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            model_id: <p>Specifies the model or throughput with which to run inference, or the prompt resource to use in inference. The value depends on the resource that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>To include a prompt that was defined in <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html">Prompt management</a>, specify the ARN of the prompt version to use.</p> </li> </ul> <p>The Converse API doesn't support <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported models</a>.</p>
            messages: <p>The messages that you want to send to the model.</p>
            system: <p>A prompt that provides instructions or context to the model about the task it should perform, or the persona it should adopt during the conversation.</p>
            inference_config: <p>Inference parameters to pass to the model. <code>Converse</code> and <code>ConverseStream</code> support a base set of inference parameters. If you need to pass additional parameters that the model supports, use the <code>additionalModelRequestFields</code> request field.</p>
            tool_config: <p>Configuration information for the tools that the model can use when generating a response.</p> <p>For information about models that support streaming tool use, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html#conversation-inference-supported-models-features">Supported models and model features</a>.</p>
            guardrail_config: <p>Configuration information for a guardrail that you want to use in the request. If you include <code>guardContent</code> blocks in the <code>content</code> field in the <code>messages</code> field, the guardrail operates only on those messages. If you include no <code>guardContent</code> blocks, the guardrail operates on all messages in the request body and in any included prompt resource.</p>
            additional_model_request_fields: <p>Additional inference parameters that the model supports, beyond the base set of inference parameters that <code>Converse</code> and <code>ConverseStream</code> support in the <code>inferenceConfig</code> field. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Model parameters</a>.</p>
            prompt_variables: <p>Contains a map of variables in a prompt from Prompt management to objects containing the values to fill in for them when running model invocation. This field is ignored if you don't specify a prompt resource in the <code>modelId</code> field.</p>
            additional_model_response_field_paths: <p>Additional model parameters field paths to return in the response. <code>Converse</code> and <code>ConverseStream</code> return the requested fields as a JSON Pointer object in the <code>additionalModelResponseFields</code> field. The following is example JSON for <code>additionalModelResponseFieldPaths</code>.</p> <p> <code>[ "/stop_sequence" ]</code> </p> <p>For information about the JSON Pointer syntax, see the <a href="https://datatracker.ietf.org/doc/html/rfc6901">Internet Engineering Task Force (IETF)</a> documentation.</p> <p> <code>Converse</code> and <code>ConverseStream</code> reject an empty JSON Pointer or incorrectly structured JSON Pointer with a <code>400</code> error code. if the JSON Pointer is valid, but the requested field is not in the model response, it is ignored by <code>Converse</code>.</p>
            request_metadata: <p>Key-value pairs that you can use to filter invocation logs.</p>
            performance_config: <p>Model performance settings for the request.</p>
            service_tier: <p>Specifies the processing tier configuration used for serving the request.</p>
            output_config: <p>Output configuration for a model response.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_runtime.types.converse_stream_request.ConverseStreamRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_runtime.types.converse_stream_response.ConverseStreamResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.converse_stream

            (
                output,
                http_response,
            ) = await capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.converse_stream.async_converse_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.converse_stream_request.ConverseStreamRequest = {
            "model_id": model_id
        }
        if messages is not None:
            input_["messages"] = messages
        if system is not None:
            input_["system"] = system
        if inference_config is not None:
            input_["inference_config"] = inference_config
        if tool_config is not None:
            input_["tool_config"] = tool_config
        if guardrail_config is not None:
            input_["guardrail_config"] = guardrail_config
        if additional_model_request_fields is not None:
            input_["additional_model_request_fields"] = additional_model_request_fields
        if prompt_variables is not None:
            input_["prompt_variables"] = prompt_variables
        if additional_model_response_field_paths is not None:
            input_["additional_model_response_field_paths"] = (
                additional_model_response_field_paths
            )
        if request_metadata is not None:
            input_["request_metadata"] = request_metadata
        if performance_config is not None:
            input_["performance_config"] = performance_config
        if service_tier is not None:
            input_["service_tier"] = service_tier
        if output_config is not None:
            input_["output_config"] = output_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def invoke_model(
        self,
        model_id: "capo_bedrock_runtime.types.invoke_model_identifier.InvokeModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
        body: Optional["capo_bedrock_runtime.types.body.Body"] = None,
        content_type: Optional["capo_bedrock_runtime.types.mime_type.MimeType"] = None,
        accept: Optional["capo_bedrock_runtime.types.mime_type.MimeType"] = None,
        trace: Optional["capo_bedrock_runtime.types.trace.Trace"] = None,
        guardrail_identifier: Optional[
            "capo_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier"
        ] = None,
        guardrail_version: Optional[
            "capo_bedrock_runtime.types.guardrail_version.GuardrailVersion"
        ] = None,
        performance_config_latency: Optional[
            "capo_bedrock_runtime.types.performance_config_latency.PerformanceConfigLatency"
        ] = None,
        service_tier: Optional[
            "capo_bedrock_runtime.types.service_tier_type.ServiceTierType"
        ] = None,
        request_metadata: Optional[
            "capo_bedrock_runtime.types.request_metadata_json.RequestMetadataJson"
        ] = None,
    ) -> "capo_bedrock_runtime.types.invoke_model_response.InvokeModelResponse":
        """<p>Invokes the specified Amazon Bedrock model to run inference using the prompt and inference parameters provided in the request body. You use model inference to generate text, images, and embeddings.</p> <p>For example code, see <i>Invoke model code examples</i> in the <i>Amazon Bedrock User Guide</i>. </p> <p>This operation requires permission for the <code>bedrock:InvokeModel</code> action.</p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the Converse API actions (<a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html">Converse</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html">ConverseStream</a>). For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference">Deny access for inference on specific models</a>. </p> </important> <p>For troubleshooting some of the common errors you might encounter when using the <code>InvokeModel</code> API, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            body: <p>The prompt and inference parameters in the format specified in the <code>contentType</code> in the header. You must provide the body in JSON format. To see the format and content of the request and response bodies for different models, refer to <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters</a>. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/api-methods-run.html">Run inference</a> in the Bedrock User Guide.</p>
            content_type: <p>The MIME type of the input data in the request. You must specify <code>application/json</code>.</p>
            accept: <p>The desired MIME type of the inference body in the response. The default value is <code>application/json</code>.</p>
            model_id: <p>The unique identifier of the model to invoke to run inference.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, specify the ARN of the custom model deployment (for on-demand inference) or the ARN of your provisioned model (for Provisioned Throughput). For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            trace: <p>Specifies whether to enable or disable the Bedrock trace. If enabled, you can see the full Bedrock trace.</p>
            guardrail_identifier: <p>The unique identifier of the guardrail that you want to use. If you don't provide a value, no guardrail is applied to the invocation.</p> <p>An error will be thrown in the following situations.</p> <ul> <li> <p>You don't provide a guardrail identifier but you specify the <code>amazon-bedrock-guardrailConfig</code> field in the request body.</p> </li> <li> <p>You enable the guardrail but the <code>contentType</code> isn't <code>application/json</code>.</p> </li> <li> <p>You provide a guardrail identifier, but <code>guardrailVersion</code> isn't specified.</p> </li> </ul>
            guardrail_version: <p>The version number for the guardrail. The value can also be <code>DRAFT</code>.</p>
            performance_config_latency: <p>Model performance settings for the request.</p>
            service_tier: <p>Specifies the processing tier type used for serving the request.</p>
            request_metadata: <p>Key-value pairs that you can use to filter invocation logs.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds the service quota for your account. You can view your quotas at <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html">Viewing service quotas</a>. You can resubmit your request later.</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_runtime.types.invoke_model_request.InvokeModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_runtime.types.invoke_model_response.InvokeModelResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model

            (
                output,
                http_response,
            ) = await capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model.async_invoke_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.invoke_model_request.InvokeModelRequest = {
            "model_id": model_id
        }
        if body is not None:
            input_["body"] = body
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if trace is not None:
            input_["trace"] = trace
        if guardrail_identifier is not None:
            input_["guardrail_identifier"] = guardrail_identifier
        if guardrail_version is not None:
            input_["guardrail_version"] = guardrail_version
        if performance_config_latency is not None:
            input_["performance_config_latency"] = performance_config_latency
        if service_tier is not None:
            input_["service_tier"] = service_tier
        if request_metadata is not None:
            input_["request_metadata"] = request_metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def invoke_model_with_bidirectional_stream(
        self,
        model_id: "capo_bedrock_runtime.types.invoke_model_identifier.InvokeModelIdentifier",
        body: "AsyncIterator[capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input._InvokeModelWithBidirectionalStreamInput] | capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input._InvokeModelWithBidirectionalStreamInput",
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
    ) -> "AsyncGenerator[capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse]":
        """<p>Invoke the specified Amazon Bedrock model to run inference using the bidirectional stream. The response is returned in a stream that remains open for 8 minutes. A single session can contain multiple prompts and responses from the model. The prompts to the model are provided as audio files and the model's responses are spoken back to the user and transcribed.</p> <p>It is possible for users to interrupt the model's response with a new prompt, which will halt the response speech. The model will retain contextual awareness of the conversation while pivoting to respond to the new prompt.</p>

        Args:
            model_id: <p>The model ID or ARN of the model ID to use. Currently, only <code>amazon.nova-sonic-v1:0</code> is supported.</p>
            body: <p>The prompt and inference parameters in the format specified in the <code>BidirectionalInputPayloadPart</code> in the header. You must provide the body in JSON format. To see the format and content of the request and response bodies for different models, refer to <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters</a>. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/api-methods-run.html">Run inference</a> in the Bedrock User Guide.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException: <p>An error occurred while streaming the response. Retry your request.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds the service quota for your account. You can view your quotas at <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html">Viewing service quotas</a>. You can resubmit your request later.</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model_with_bidirectional_stream

            (
                output,
                http_response,
            ) = await capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model_with_bidirectional_stream.async_invoke_model_with_bidirectional_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest = {
            "model_id": model_id,
            "body": ensure_async_iterator(body),
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    @asynccontextmanager
    async def invoke_model_with_response_stream(
        self,
        model_id: "capo_bedrock_runtime.types.invoke_model_identifier.InvokeModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
        body: Optional["capo_bedrock_runtime.types.body.Body"] = None,
        content_type: Optional["capo_bedrock_runtime.types.mime_type.MimeType"] = None,
        accept: Optional["capo_bedrock_runtime.types.mime_type.MimeType"] = None,
        trace: Optional["capo_bedrock_runtime.types.trace.Trace"] = None,
        guardrail_identifier: Optional[
            "capo_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier"
        ] = None,
        guardrail_version: Optional[
            "capo_bedrock_runtime.types.guardrail_version.GuardrailVersion"
        ] = None,
        performance_config_latency: Optional[
            "capo_bedrock_runtime.types.performance_config_latency.PerformanceConfigLatency"
        ] = None,
        service_tier: Optional[
            "capo_bedrock_runtime.types.service_tier_type.ServiceTierType"
        ] = None,
        request_metadata: Optional[
            "capo_bedrock_runtime.types.request_metadata_json.RequestMetadataJson"
        ] = None,
    ) -> "AsyncGenerator[capo_bedrock_runtime.types.invoke_model_with_response_stream_response.InvokeModelWithResponseStreamResponse]":
        """<p>Invoke the specified Amazon Bedrock model to run inference using the prompt and inference parameters provided in the request body. The response is returned in a stream.</p> <p>To see if a model supports streaming, call <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetFoundationModel.html">GetFoundationModel</a> and check the <code>responseStreamingSupported</code> field in the response.</p> <note> <p>The CLI doesn't support streaming operations in Amazon Bedrock, including <code>InvokeModelWithResponseStream</code>.</p> </note> <p>For example code, see <i>Invoke model with streaming code example</i> in the <i>Amazon Bedrock User Guide</i>. </p> <p>This operation requires permissions to perform the <code>bedrock:InvokeModelWithResponseStream</code> action. </p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the Converse API actions (<a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html">Converse</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html">ConverseStream</a>). For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference">Deny access for inference on specific models</a>. </p> </important> <p>For troubleshooting some of the common errors you might encounter when using the <code>InvokeModelWithResponseStream</code> API, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            body: <p>The prompt and inference parameters in the format specified in the <code>contentType</code> in the header. You must provide the body in JSON format. To see the format and content of the request and response bodies for different models, refer to <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters</a>. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/api-methods-run.html">Run inference</a> in the Bedrock User Guide.</p>
            content_type: <p>The MIME type of the input data in the request. You must specify <code>application/json</code>.</p>
            accept: <p>The desired MIME type of the inference body in the response. The default value is <code>application/json</code>.</p>
            model_id: <p>The unique identifier of the model to invoke to run inference.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, specify the ARN of the custom model deployment (for on-demand inference) or the ARN of your provisioned model (for Provisioned Throughput). For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            trace: <p>Specifies whether to enable or disable the Bedrock trace. If enabled, you can see the full Bedrock trace.</p>
            guardrail_identifier: <p>The unique identifier of the guardrail that you want to use. If you don't provide a value, no guardrail is applied to the invocation.</p> <p>An error is thrown in the following situations.</p> <ul> <li> <p>You don't provide a guardrail identifier but you specify the <code>amazon-bedrock-guardrailConfig</code> field in the request body.</p> </li> <li> <p>You enable the guardrail but the <code>contentType</code> isn't <code>application/json</code>.</p> </li> <li> <p>You provide a guardrail identifier, but <code>guardrailVersion</code> isn't specified.</p> </li> </ul>
            guardrail_version: <p>The version number for the guardrail. The value can also be <code>DRAFT</code>.</p>
            performance_config_latency: <p>Model performance settings for the request.</p>
            service_tier: <p>Specifies the processing tier type used for serving the request.</p>
            request_metadata: <p>Key-value pairs that you can use to filter invocation logs.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException: <p>An error occurred while streaming the response. Retry your request.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds the service quota for your account. You can view your quotas at <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html">Viewing service quotas</a>. You can resubmit your request later.</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_runtime.types.invoke_model_with_response_stream_request.InvokeModelWithResponseStreamRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_runtime.types.invoke_model_with_response_stream_response.InvokeModelWithResponseStreamResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model_with_response_stream

            (
                output,
                http_response,
            ) = await capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model_with_response_stream.async_invoke_model_with_response_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.invoke_model_with_response_stream_request.InvokeModelWithResponseStreamRequest = {
            "model_id": model_id
        }
        if body is not None:
            input_["body"] = body
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if trace is not None:
            input_["trace"] = trace
        if guardrail_identifier is not None:
            input_["guardrail_identifier"] = guardrail_identifier
        if guardrail_version is not None:
            input_["guardrail_version"] = guardrail_version
        if performance_config_latency is not None:
            input_["performance_config_latency"] = performance_config_latency
        if service_tier is not None:
            input_["service_tier"] = service_tier
        if request_metadata is not None:
            input_["request_metadata"] = request_metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()
