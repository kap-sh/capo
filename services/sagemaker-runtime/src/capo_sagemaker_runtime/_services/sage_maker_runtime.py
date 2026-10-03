"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#AmazonSageMakerRuntime``."""

import warnings
from collections.abc import Generator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_sagemaker_runtime._auth._signers
import capo_sagemaker_runtime._auth._sigv4
from capo_sagemaker_runtime._auth._identity import Credentials
from capo_sagemaker_runtime._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sagemaker_runtime._auth._zapros_handler import AuthMiddleware
from capo_sagemaker_runtime._services._aws_config import aws_config
from capo_sagemaker_runtime._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_sagemaker_runtime.types.async_body_blob
    import capo_sagemaker_runtime.types.body_blob
    import capo_sagemaker_runtime.types.custom_attributes_header
    import capo_sagemaker_runtime.types.enable_explanations_header
    import capo_sagemaker_runtime.types.endpoint_name
    import capo_sagemaker_runtime.types.filename_header
    import capo_sagemaker_runtime.types.header
    import capo_sagemaker_runtime.types.inference_component_header
    import capo_sagemaker_runtime.types.inference_id
    import capo_sagemaker_runtime.types.input_location_header
    import capo_sagemaker_runtime.types.invocation_timeout_seconds_header
    import capo_sagemaker_runtime.types.invoke_endpoint_async_input
    import capo_sagemaker_runtime.types.invoke_endpoint_async_output
    import capo_sagemaker_runtime.types.invoke_endpoint_input
    import capo_sagemaker_runtime.types.invoke_endpoint_output
    import capo_sagemaker_runtime.types.invoke_endpoint_with_response_stream_input
    import capo_sagemaker_runtime.types.invoke_endpoint_with_response_stream_output
    import capo_sagemaker_runtime.types.prefix_aware_id_header
    import capo_sagemaker_runtime.types.request_ttl_seconds_header
    import capo_sagemaker_runtime.types.s3_output_path_extension_header
    import capo_sagemaker_runtime.types.session_id_header
    import capo_sagemaker_runtime.types.session_id_or_new_session_constant_header
    import capo_sagemaker_runtime.types.target_container_hostname_header
    import capo_sagemaker_runtime.types.target_model_header
    import capo_sagemaker_runtime.types.target_variant_header


class SageMakerRuntimeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class SageMakerRuntimeClient:
    """A client for the ``SageMakerRuntime`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = SageMakerRuntimeClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[SageMakerRuntimeClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SageMakerRuntimeClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def invoke_endpoint(
        self,
        endpoint_name: "capo_sagemaker_runtime.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[SageMakerRuntimeClientConfig] = None,
        body: Optional["capo_sagemaker_runtime.types.body_blob.BodyBlob"] = None,
        content_type: Optional["capo_sagemaker_runtime.types.header.Header"] = None,
        accept: Optional["capo_sagemaker_runtime.types.header.Header"] = None,
        custom_attributes: Optional[
            "capo_sagemaker_runtime.types.custom_attributes_header.CustomAttributesHeader"
        ] = None,
        target_model: Optional[
            "capo_sagemaker_runtime.types.target_model_header.TargetModelHeader"
        ] = None,
        target_variant: Optional[
            "capo_sagemaker_runtime.types.target_variant_header.TargetVariantHeader"
        ] = None,
        target_container_hostname: Optional[
            "capo_sagemaker_runtime.types.target_container_hostname_header.TargetContainerHostnameHeader"
        ] = None,
        inference_id: Optional[
            "capo_sagemaker_runtime.types.inference_id.InferenceId"
        ] = None,
        enable_explanations: Optional[
            "capo_sagemaker_runtime.types.enable_explanations_header.EnableExplanationsHeader"
        ] = None,
        inference_component_name: Optional[
            "capo_sagemaker_runtime.types.inference_component_header.InferenceComponentHeader"
        ] = None,
        session_id: Optional[
            "capo_sagemaker_runtime.types.session_id_or_new_session_constant_header.SessionIdOrNewSessionConstantHeader"
        ] = None,
        prefix_aware_id: Optional[
            "capo_sagemaker_runtime.types.prefix_aware_id_header.PrefixAwareIdHeader"
        ] = None,
    ) -> "capo_sagemaker_runtime.types.invoke_endpoint_output.InvokeEndpointOutput":
        """<p>After you deploy a model into production using Amazon SageMaker AI hosting services, your client applications use this API to get inferences from the model hosted at the specified endpoint. </p> <p>For an overview of Amazon SageMaker AI, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html">How It Works</a>. </p> <p>Amazon SageMaker AI strips all POST headers except those supported by the API. Amazon SageMaker AI might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax. </p> <p>Calls to <code>InvokeEndpoint</code> are authenticated by using Amazon Web Services Signature Version 4. For information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon S3 API Reference</i>.</p> <p>A customer's model containers must respond to requests within 60 seconds. The model itself can have a maximum processing time of 60 seconds before responding to invocations. If your model is going to take 50-60 seconds of processing time, the SDK socket timeout should be set to be 70 seconds.</p> <note> <p>Endpoints are scoped to an individual account, and are not public. The URL does not contain the account ID, but Amazon SageMaker AI determines the account ID from the authentication token that is supplied by the caller.</p> </note>

        Args:
            endpoint_name: <p>The name of the endpoint that you specified when you created the endpoint using the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html">CreateEndpoint</a> API.</p>
            body: <p>Provides input data, in the format specified in the <code>ContentType</code> request header. Amazon SageMaker AI passes all of the data in the body to the model. </p> <p>For information about the format of the request body, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html">Common Data Formats-Inference</a>.</p>
            content_type: <p>The MIME type of the input data in the request body.</p>
            accept: <p>The desired MIME type of the inference response from the model container.</p>
            custom_attributes: <p>Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker AI endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in <a href="https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6">Section 3.3.6. Field Value Components</a> of the Hypertext Transfer Protocol (HTTP/1.1). </p> <p>The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with <code>Trace ID:</code> in your post-processing function. </p> <p>This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker AI Python SDK. </p>
            target_model: <p>The model to request for inference when invoking a multi-model endpoint.</p>
            target_variant: <p>Specify the production variant to send the inference request to when invoking an endpoint that is running two or more variants. Note that this parameter overrides the default behavior for the endpoint, which is to distribute the invocation traffic based on the variant weights.</p> <p>For information about how to use variant targeting to perform a/b testing, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html">Test models in production</a> </p>
            target_container_hostname: <p>If the endpoint hosts multiple containers and is configured to use direct invocation, this parameter specifies the host name of the container to invoke.</p>
            inference_id: <p>If you provide a value, it is added to the captured data when you enable data capture on the endpoint. For information about data capture, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html">Capture Data</a>.</p>
            enable_explanations: <p>An optional JMESPath expression used to override the <code>EnableExplanations</code> parameter of the <code>ClarifyExplainerConfig</code> API. See the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint-enable">EnableExplanations</a> section in the developer guide for more information. </p>
            inference_component_name: <p>If the endpoint hosts one or more inference components, this parameter specifies the name of inference component to invoke.</p>
            session_id: <p>Creates a stateful session or identifies an existing one. You can do one of the following:</p> <ul> <li> <p>Create a stateful session by specifying the value <code>NEW_SESSION</code>.</p> </li> <li> <p>Send your request to an existing stateful session by specifying the ID of that session.</p> </li> </ul> <p>With a stateful session, you can send multiple requests to a stateful model. When you create a session with a stateful model, the model must create the session ID and set the expiration time. The model must also provide that information in the response to your request. You can get the ID and timestamp from the <code>NewSessionId</code> response parameter. For any subsequent request where you specify that session ID, SageMaker AI routes the request to the same instance that supports the session.</p>
            prefix_aware_id: <p>An optional, stable identifier that serves as a routing hint for prefix-aware routing. The service routes requests with the same prefix and the same identifier to the same instance. If requests from different applications might have the same prompt prefix, set a different identifier for each application to differentiate their routing decisions.</p> <p>Applies only to endpoints configured with a <code>RoutingStrategy</code> of <code>PREFIX_AWARE</code>.</p>

        Raises:
            capo_sagemaker_runtime.errors.internal_dependency_exception.InternalDependencyException: <p>Your request caused an exception with an internal dependency. Contact customer support. </p>
            capo_sagemaker_runtime.errors.internal_failure.InternalFailure: <p> An internal failure occurred. </p>
            capo_sagemaker_runtime.errors.model_error.ModelError: <p> Model (owned by the customer in the container) returned 4xx or 5xx error code. </p>
            capo_sagemaker_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>Either a serverless endpoint variant's resources are still being provisioned, or a multi-model endpoint is still downloading or loading the target model. Wait and try your request again.</p>
            capo_sagemaker_runtime.errors.service_unavailable.ServiceUnavailable: <p> The service is unavailable. Try your call again. </p>
            capo_sagemaker_runtime.errors.validation_error.ValidationError: <p> Inspect your request and try again. </p>
            capo_sagemaker_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_runtime.types.invoke_endpoint_input.InvokeEndpointInput]",
        ) -> OperationResponse[
            "capo_sagemaker_runtime.types.invoke_endpoint_output.InvokeEndpointOutput"
        ]:
            import capo_sagemaker_runtime._operations.amazon_sage_maker_runtime.invoke_endpoint

            output, http_response = (
                capo_sagemaker_runtime._operations.amazon_sage_maker_runtime.invoke_endpoint.invoke_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_runtime.types.invoke_endpoint_input.InvokeEndpointInput = {
            "endpoint_name": endpoint_name
        }
        if body is not None:
            input_["body"] = body
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if custom_attributes is not None:
            input_["custom_attributes"] = custom_attributes
        if target_model is not None:
            input_["target_model"] = target_model
        if target_variant is not None:
            input_["target_variant"] = target_variant
        if target_container_hostname is not None:
            input_["target_container_hostname"] = target_container_hostname
        if inference_id is not None:
            input_["inference_id"] = inference_id
        if enable_explanations is not None:
            input_["enable_explanations"] = enable_explanations
        if inference_component_name is not None:
            input_["inference_component_name"] = inference_component_name
        if session_id is not None:
            input_["session_id"] = session_id
        if prefix_aware_id is not None:
            input_["prefix_aware_id"] = prefix_aware_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def invoke_endpoint_async(
        self,
        endpoint_name: "capo_sagemaker_runtime.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[SageMakerRuntimeClientConfig] = None,
        content_type: Optional["capo_sagemaker_runtime.types.header.Header"] = None,
        accept: Optional["capo_sagemaker_runtime.types.header.Header"] = None,
        custom_attributes: Optional[
            "capo_sagemaker_runtime.types.custom_attributes_header.CustomAttributesHeader"
        ] = None,
        inference_id: Optional[
            "capo_sagemaker_runtime.types.inference_id.InferenceId"
        ] = None,
        input_location: Optional[
            "capo_sagemaker_runtime.types.input_location_header.InputLocationHeader"
        ] = None,
        s3_output_path_extension: Optional[
            "capo_sagemaker_runtime.types.s3_output_path_extension_header.S3OutputPathExtensionHeader"
        ] = None,
        filename: Optional[
            "capo_sagemaker_runtime.types.filename_header.FilenameHeader"
        ] = None,
        request_ttl_seconds: Optional[
            "capo_sagemaker_runtime.types.request_ttl_seconds_header.RequestTTLSecondsHeader"
        ] = None,
        invocation_timeout_seconds: Optional[
            "capo_sagemaker_runtime.types.invocation_timeout_seconds_header.InvocationTimeoutSecondsHeader"
        ] = None,
        body: Optional[
            "capo_sagemaker_runtime.types.async_body_blob.AsyncBodyBlob"
        ] = None,
    ) -> "capo_sagemaker_runtime.types.invoke_endpoint_async_output.InvokeEndpointAsyncOutput":
        """<p>After you deploy a model into production using Amazon SageMaker AI hosting services, your client applications use this API to get inferences from the model hosted at the specified endpoint in an asynchronous manner.</p> <p>Inference requests sent to this API are enqueued for asynchronous processing. The processing of the inference request may or may not complete before you receive a response from this API. The response from this API will not contain the result of the inference request but contain information about where you can locate it.</p> <p>Amazon SageMaker AI strips all POST headers except those supported by the API. Amazon SageMaker AI might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax. </p> <p>Calls to <code>InvokeEndpointAsync</code> are authenticated by using Amazon Web Services Signature Version 4. For information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon S3 API Reference</i>.</p>

        Args:
            endpoint_name: <p>The name of the endpoint that you specified when you created the endpoint using the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html">CreateEndpoint</a> API.</p>
            content_type: <p>The MIME type of the input data in the request body.</p>
            accept: <p>The desired MIME type of the inference response from the model container.</p>
            custom_attributes: <p>Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker AI endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in <a href="https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6">Section 3.3.6. Field Value Components</a> of the Hypertext Transfer Protocol (HTTP/1.1). </p> <p>The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with <code>Trace ID:</code> in your post-processing function. </p> <p>This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker AI Python SDK. </p>
            inference_id: <p>The identifier for the inference request. Amazon SageMaker AI will generate an identifier for you if none is specified. </p>
            input_location: <p>The Amazon S3 URI where the inference request payload is stored.</p>
            s3_output_path_extension: <p>The path extension that is appended to the Amazon S3 output path where the inference response payload is stored.</p>
            filename: <p>The filename for the inference response payload stored in Amazon S3. If not specified, Amazon SageMaker AI generates a filename based on the inference ID.</p>
            request_ttl_seconds: <p>Maximum age in seconds a request can be in the queue before it is marked as expired. The default is 6 hours, or 21,600 seconds.</p>
            invocation_timeout_seconds: <p>Maximum amount of time in seconds a request can be processed before it is marked as expired. The default is 15 minutes, or 900 seconds.</p>
            body: <p>Provides inline input data for the inference request, in the format specified in the <code>ContentType</code> request header. Use this parameter to send the request payload directly in the API call instead of uploading it to Amazon S3 and referencing it with <code>InputLocation</code>. The inline payload can be up to 128,000 bytes.</p> <p> <code>Body</code> and <code>InputLocation</code> are mutually exclusive. Provide exactly one of them.</p> <p>For information about the format of the request body, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html">Common Data Formats-Inference</a>.</p>

        Raises:
            capo_sagemaker_runtime.errors.internal_failure.InternalFailure: <p> An internal failure occurred. </p>
            capo_sagemaker_runtime.errors.service_unavailable.ServiceUnavailable: <p> The service is unavailable. Try your call again. </p>
            capo_sagemaker_runtime.errors.validation_error.ValidationError: <p> Inspect your request and try again. </p>
            capo_sagemaker_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_runtime.types.invoke_endpoint_async_input.InvokeEndpointAsyncInput]",
        ) -> OperationResponse[
            "capo_sagemaker_runtime.types.invoke_endpoint_async_output.InvokeEndpointAsyncOutput"
        ]:
            import capo_sagemaker_runtime._operations.amazon_sage_maker_runtime.invoke_endpoint_async

            output, http_response = (
                capo_sagemaker_runtime._operations.amazon_sage_maker_runtime.invoke_endpoint_async.invoke_endpoint_async(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_runtime.types.invoke_endpoint_async_input.InvokeEndpointAsyncInput = {
            "endpoint_name": endpoint_name
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if custom_attributes is not None:
            input_["custom_attributes"] = custom_attributes
        if inference_id is not None:
            input_["inference_id"] = inference_id
        if input_location is not None:
            input_["input_location"] = input_location
        if s3_output_path_extension is not None:
            input_["s3_output_path_extension"] = s3_output_path_extension
        if filename is not None:
            input_["filename"] = filename
        if request_ttl_seconds is not None:
            input_["request_ttl_seconds"] = request_ttl_seconds
        if invocation_timeout_seconds is not None:
            input_["invocation_timeout_seconds"] = invocation_timeout_seconds
        if body is not None:
            input_["body"] = body

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def invoke_endpoint_with_response_stream(
        self,
        endpoint_name: "capo_sagemaker_runtime.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[SageMakerRuntimeClientConfig] = None,
        body: Optional["capo_sagemaker_runtime.types.body_blob.BodyBlob"] = None,
        content_type: Optional["capo_sagemaker_runtime.types.header.Header"] = None,
        accept: Optional["capo_sagemaker_runtime.types.header.Header"] = None,
        custom_attributes: Optional[
            "capo_sagemaker_runtime.types.custom_attributes_header.CustomAttributesHeader"
        ] = None,
        target_variant: Optional[
            "capo_sagemaker_runtime.types.target_variant_header.TargetVariantHeader"
        ] = None,
        target_container_hostname: Optional[
            "capo_sagemaker_runtime.types.target_container_hostname_header.TargetContainerHostnameHeader"
        ] = None,
        inference_id: Optional[
            "capo_sagemaker_runtime.types.inference_id.InferenceId"
        ] = None,
        inference_component_name: Optional[
            "capo_sagemaker_runtime.types.inference_component_header.InferenceComponentHeader"
        ] = None,
        session_id: Optional[
            "capo_sagemaker_runtime.types.session_id_header.SessionIdHeader"
        ] = None,
        prefix_aware_id: Optional[
            "capo_sagemaker_runtime.types.prefix_aware_id_header.PrefixAwareIdHeader"
        ] = None,
    ) -> "Generator[capo_sagemaker_runtime.types.invoke_endpoint_with_response_stream_output.InvokeEndpointWithResponseStreamOutput]":
        """<p>Invokes a model at the specified endpoint to return the inference response as a stream. The inference stream provides the response payload incrementally as a series of parts. Before you can get an inference stream, you must have access to a model that's deployed using Amazon SageMaker AI hosting services, and the container for that model must support inference streaming.</p> <p>For more information that can help you use this API, see the following sections in the <i>Amazon SageMaker AI Developer Guide</i>:</p> <ul> <li> <p>For information about how to add streaming support to a model, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-code-how-containe-serves-requests">How Containers Serve Requests</a>.</p> </li> <li> <p>For information about how to process the streaming response, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-test-endpoints.html">Invoke real-time endpoints</a>.</p> </li> </ul> <p>Before you can use this operation, your IAM permissions must allow the <code>sagemaker:InvokeEndpoint</code> action. For more information about Amazon SageMaker AI actions for IAM policies, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemaker.html">Actions, resources, and condition keys for Amazon SageMaker AI</a> in the <i>IAM Service Authorization Reference</i>.</p> <p>Amazon SageMaker AI strips all POST headers except those supported by the API. Amazon SageMaker AI might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax. </p> <p>Calls to <code>InvokeEndpointWithResponseStream</code> are authenticated by using Amazon Web Services Signature Version 4. For information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon S3 API Reference</i>.</p>

        Args:
            endpoint_name: <p>The name of the endpoint that you specified when you created the endpoint using the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html">CreateEndpoint</a> API.</p>
            body: <p>Provides input data, in the format specified in the <code>ContentType</code> request header. Amazon SageMaker AI passes all of the data in the body to the model. </p> <p>For information about the format of the request body, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html">Common Data Formats-Inference</a>.</p>
            content_type: <p>The MIME type of the input data in the request body.</p>
            accept: <p>The desired MIME type of the inference response from the model container.</p>
            custom_attributes: <p>Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker AI endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in <a href="https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6">Section 3.3.6. Field Value Components</a> of the Hypertext Transfer Protocol (HTTP/1.1). </p> <p>The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with <code>Trace ID:</code> in your post-processing function. </p> <p>This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker AI Python SDK. </p>
            target_variant: <p>Specify the production variant to send the inference request to when invoking an endpoint that is running two or more variants. Note that this parameter overrides the default behavior for the endpoint, which is to distribute the invocation traffic based on the variant weights.</p> <p>For information about how to use variant targeting to perform a/b testing, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html">Test models in production</a> </p>
            target_container_hostname: <p>If the endpoint hosts multiple containers and is configured to use direct invocation, this parameter specifies the host name of the container to invoke.</p>
            inference_id: <p>An identifier that you assign to your request.</p>
            inference_component_name: <p>If the endpoint hosts one or more inference components, this parameter specifies the name of inference component to invoke for a streaming response.</p>
            session_id: <p>The ID of a stateful session to handle your request.</p> <p>You can't create a stateful session by using the <code>InvokeEndpointWithResponseStream</code> action. Instead, you can create one by using the <code> <a>InvokeEndpoint</a> </code> action. In your request, you specify <code>NEW_SESSION</code> for the <code>SessionId</code> request parameter. The response to that request provides the session ID for the <code>NewSessionId</code> response parameter.</p>
            prefix_aware_id: <p>An optional, stable identifier that serves as a routing hint for prefix-aware routing. The service routes requests with the same prefix and the same identifier to the same instance. If requests from different applications might have the same prompt prefix, set a different identifier for each application to differentiate their routing decisions.</p> <p>Applies only to endpoints configured with a <code>RoutingStrategy</code> of <code>PREFIX_AWARE</code>.</p>

        Raises:
            capo_sagemaker_runtime.errors.internal_failure.InternalFailure: <p> An internal failure occurred. </p>
            capo_sagemaker_runtime.errors.internal_stream_failure.InternalStreamFailure: <p>The stream processing failed because of an unknown error, exception or failure. Try your request again.</p>
            capo_sagemaker_runtime.errors.model_error.ModelError: <p> Model (owned by the customer in the container) returned 4xx or 5xx error code. </p>
            capo_sagemaker_runtime.errors.model_stream_error.ModelStreamError: <p> An error occurred while streaming the response body. This error can have the following error codes:</p> <dl> <dt>ModelInvocationTimeExceeded</dt> <dd> <p>The model failed to finish sending the response within the timeout period allowed by Amazon SageMaker AI.</p> </dd> <dt>StreamBroken</dt> <dd> <p>The Transmission Control Protocol (TCP) connection between the client and the model was reset or closed.</p> </dd> </dl>
            capo_sagemaker_runtime.errors.service_unavailable.ServiceUnavailable: <p> The service is unavailable. Try your call again. </p>
            capo_sagemaker_runtime.errors.validation_error.ValidationError: <p> Inspect your request and try again. </p>
            capo_sagemaker_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_runtime.types.invoke_endpoint_with_response_stream_input.InvokeEndpointWithResponseStreamInput]",
        ) -> OperationResponse[
            "capo_sagemaker_runtime.types.invoke_endpoint_with_response_stream_output.InvokeEndpointWithResponseStreamOutput"
        ]:
            import capo_sagemaker_runtime._operations.amazon_sage_maker_runtime.invoke_endpoint_with_response_stream

            output, http_response = (
                capo_sagemaker_runtime._operations.amazon_sage_maker_runtime.invoke_endpoint_with_response_stream.invoke_endpoint_with_response_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_runtime.types.invoke_endpoint_with_response_stream_input.InvokeEndpointWithResponseStreamInput = {
            "endpoint_name": endpoint_name
        }
        if body is not None:
            input_["body"] = body
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if custom_attributes is not None:
            input_["custom_attributes"] = custom_attributes
        if target_variant is not None:
            input_["target_variant"] = target_variant
        if target_container_hostname is not None:
            input_["target_container_hostname"] = target_container_hostname
        if inference_id is not None:
            input_["inference_id"] = inference_id
        if inference_component_name is not None:
            input_["inference_component_name"] = inference_component_name
        if session_id is not None:
            input_["session_id"] = session_id
        if prefix_aware_id is not None:
            input_["prefix_aware_id"] = prefix_aware_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
