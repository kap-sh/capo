"""Generated from Smithy shape ``com.amazonaws.sagemakerinferencerouterruntime#InvokeInferenceRouterAsync``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_sagemaker_inference_router_runtime._auth._signers
import capo_sagemaker_inference_router_runtime._auth._sigv4
import capo_sagemaker_inference_router_runtime._protocol.eventstream
import capo_sagemaker_inference_router_runtime.errors.access_denied_exception
import capo_sagemaker_inference_router_runtime.errors.internal_failure
import capo_sagemaker_inference_router_runtime.errors.request_timeout_exception
import capo_sagemaker_inference_router_runtime.errors.service_unavailable_exception
import capo_sagemaker_inference_router_runtime.errors.throttling_exception
import capo_sagemaker_inference_router_runtime.errors.validation_exception
import capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_input
import capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_output
from capo_sagemaker_inference_router_runtime._protocol.errors import (
    parse_error_metadata_json,
)
from capo_sagemaker_inference_router_runtime._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_sagemaker_inference_router_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_sagemaker_inference_router_runtime.errors import (
    UnknownServiceError,
)


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_sagemaker_inference_router_runtime.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message, response=response
            )
        case "InternalFailure":
            raise capo_sagemaker_inference_router_runtime.errors.internal_failure.InternalFailure.from_json(
                data, message, response=response
            )
        case "RequestTimeoutException":
            raise capo_sagemaker_inference_router_runtime.errors.request_timeout_exception.RequestTimeoutException.from_json(
                data, message, response=response
            )
        case "ServiceUnavailableException":
            raise capo_sagemaker_inference_router_runtime.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message, response=response
            )
        case "ThrottlingException":
            raise capo_sagemaker_inference_router_runtime.errors.throttling_exception.ThrottlingException.from_json(
                data, message, response=response
            )
        case "ValidationException":
            raise capo_sagemaker_inference_router_runtime.errors.validation_exception.ValidationException.from_json(
                data, message, response=response
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_output.InvokeInferenceRouterAsyncOutput:
    out: capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_output.InvokeInferenceRouterAsyncOutput = capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_output.deserialize_json(
        json.loads(response.read())
    )
    if "X-Amzn-SageMaker-OutputLocation" in response.headers:
        out["output_location"] = response.headers["X-Amzn-SageMaker-OutputLocation"]
    if "X-Amzn-SageMaker-FailureLocation" in response.headers:
        out["failure_location"] = response.headers["X-Amzn-SageMaker-FailureLocation"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_output.InvokeInferenceRouterAsyncOutput:
    out: capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_output.InvokeInferenceRouterAsyncOutput = capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_output.deserialize_json(
        json.loads(await response.aread())
    )
    if "X-Amzn-SageMaker-OutputLocation" in response.headers:
        out["output_location"] = response.headers["X-Amzn-SageMaker-OutputLocation"]
    if "X-Amzn-SageMaker-FailureLocation" in response.headers:
        out["failure_location"] = response.headers["X-Amzn-SageMaker-FailureLocation"]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_sagemaker_inference_router_runtime._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if (
        options.credentials_provider is not None
        and name_to_schema
        and not name_to_schema.keys() & {"sigv4", "sigv4-s3express"}
    ):
        raise RuntimeError(
            "Endpoint requires an unsupported auth scheme: " + ", ".join(name_to_schema)
        )
    if options.credentials_provider is not None:
        endpoint_scheme = name_to_schema.get("sigv4") or name_to_schema.get(
            "sigv4-s3express"
        )
        if endpoint_scheme is not None or not name_to_schema:
            sigv4_config = capo_sagemaker_inference_router_runtime._auth._sigv4.build_sigv4_auth_scheme(
                "sagemaker", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return (
                    capo_sagemaker_inference_router_runtime._auth._signers.SigV4Signer(
                        options.credentials_provider, auth_scheme=sigv4_config
                    )
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_input.InvokeInferenceRouterAsyncInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/inference-routers/{InferenceRouterName}/async-invocations"
    )
    url = url.replace(
        "{InferenceRouterName}", quote(input_["inference_router_name"], safe="")
    )
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "routing_target_name" in input_:
        headers["X-Amzn-SageMaker-Routing-Target-Name"] = input_["routing_target_name"]
    if "content_type" in input_:
        headers["X-Amzn-SageMaker-Content-Type"] = input_["content_type"]
    if "accept" in input_:
        headers["X-Amzn-SageMaker-Accept"] = input_["accept"]
    if "custom_attributes" in input_:
        headers["X-Amzn-SageMaker-Custom-Attributes"] = input_["custom_attributes"]
    if "inference_id" in input_:
        headers["X-Amzn-SageMaker-Inference-Id"] = input_["inference_id"]
    if "input_location" in input_:
        headers["X-Amzn-SageMaker-InputLocation"] = input_["input_location"]
    if "s3_output_path_extension" in input_:
        headers["X-Amzn-SageMaker-S3OutputPathExtension"] = input_[
            "s3_output_path_extension"
        ]
    if "filename" in input_:
        headers["X-Amzn-SageMaker-Filename"] = input_["filename"]
    if "request_ttl_seconds" in input_:
        headers["X-Amzn-SageMaker-RequestTTLSeconds"] = str(
            input_["request_ttl_seconds"]
        )
    if "invocation_timeout_seconds" in input_:
        headers["X-Amzn-SageMaker-InvocationTimeoutSeconds"] = str(
            input_["invocation_timeout_seconds"]
        )
    body: bytes | None = b""
    signer = (
        None
        if options.anonymous
        else get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    )
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def invoke_inference_router_async(
    options: OperationOptions,
    input_: capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_input.InvokeInferenceRouterAsyncInput,
) -> tuple[
    capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_output.InvokeInferenceRouterAsyncOutput,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_invoke_inference_router_async(
    options: AsyncOperationOptions,
    input_: capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_input.InvokeInferenceRouterAsyncInput,
) -> tuple[
    capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_output.InvokeInferenceRouterAsyncOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
