"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModel``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_bedrock_runtime._auth._signers
import capo_bedrock_runtime._auth._sigv4
import capo_bedrock_runtime._protocol.eventstream
import capo_bedrock_runtime.errors.access_denied_exception
import capo_bedrock_runtime.errors.internal_server_exception
import capo_bedrock_runtime.errors.model_error_exception
import capo_bedrock_runtime.errors.model_not_ready_exception
import capo_bedrock_runtime.errors.model_timeout_exception
import capo_bedrock_runtime.errors.resource_not_found_exception
import capo_bedrock_runtime.errors.service_quota_exceeded_exception
import capo_bedrock_runtime.errors.service_unavailable_exception
import capo_bedrock_runtime.errors.throttling_exception
import capo_bedrock_runtime.errors.validation_exception
import capo_bedrock_runtime.types.body
import capo_bedrock_runtime.types.invoke_model_request
import capo_bedrock_runtime.types.invoke_model_response
import capo_bedrock_runtime.types.performance_config_latency
import capo_bedrock_runtime.types.service_tier_type
import capo_bedrock_runtime.types.trace
from capo_bedrock_runtime._protocol.errors import parse_error_metadata_json
from capo_bedrock_runtime._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_bedrock_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_bedrock_runtime.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_bedrock_runtime.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ModelErrorException":
            raise capo_bedrock_runtime.errors.model_error_exception.ModelErrorException.from_json(
                data, message
            )
        case "ModelNotReadyException":
            raise capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException.from_json(
                data, message
            )
        case "ModelTimeoutException":
            raise capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data, message
            )
        case "ServiceUnavailableException":
            raise capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_bedrock_runtime.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_bedrock_runtime.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_bedrock_runtime.types.invoke_model_response.InvokeModelResponse:
    out: capo_bedrock_runtime.types.invoke_model_response.InvokeModelResponse = {
        "body": b"".join(response.iter_raw())
    }  # type: ignore[typeddict-item]
    out["content_type"] = response.headers["Content-Type"]
    if "X-Amzn-Bedrock-PerformanceConfig-Latency" in response.headers:
        out["performance_config_latency"] = (
            capo_bedrock_runtime.types.performance_config_latency.deserialize_json(
                response.headers["X-Amzn-Bedrock-PerformanceConfig-Latency"]
            )
        )
    if "X-Amzn-Bedrock-Service-Tier" in response.headers:
        out["service_tier"] = (
            capo_bedrock_runtime.types.service_tier_type.deserialize_json(
                response.headers["X-Amzn-Bedrock-Service-Tier"]
            )
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_bedrock_runtime.types.invoke_model_response.InvokeModelResponse:
    out: capo_bedrock_runtime.types.invoke_model_response.InvokeModelResponse = {
        "body": b"".join([chunk async for chunk in response.async_iter_raw()])
    }  # type: ignore[typeddict-item]
    out["content_type"] = response.headers["Content-Type"]
    if "X-Amzn-Bedrock-PerformanceConfig-Latency" in response.headers:
        out["performance_config_latency"] = (
            capo_bedrock_runtime.types.performance_config_latency.deserialize_json(
                response.headers["X-Amzn-Bedrock-PerformanceConfig-Latency"]
            )
        )
    if "X-Amzn-Bedrock-Service-Tier" in response.headers:
        out["service_tier"] = (
            capo_bedrock_runtime.types.service_tier_type.deserialize_json(
                response.headers["X-Amzn-Bedrock-Service-Tier"]
            )
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_bedrock_runtime._auth._signers.Signer | None:
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
            sigv4_config = capo_bedrock_runtime._auth._sigv4.build_sigv4_auth_scheme(
                "bedrock", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_bedrock_runtime._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    if options.bearer_provider is not None:
        return capo_bedrock_runtime._auth._signers.HttpBearerSigner(
            options.bearer_provider
        )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_bedrock_runtime.types.invoke_model_request.InvokeModelRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_bedrock_runtime.types.performance_config_latency
    import capo_bedrock_runtime.types.service_tier_type
    import capo_bedrock_runtime.types.trace

    url = endpoint.url.rstrip("/") + "/model/{modelId}/invoke"
    url = url.replace("{modelId}", quote(input_["model_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "content_type" in input_:
        headers["Content-Type"] = input_["content_type"]
    if "accept" in input_:
        headers["Accept"] = input_["accept"]
    if "trace" in input_:
        headers["X-Amzn-Bedrock-Trace"] = (
            capo_bedrock_runtime.types.trace.serialize_json(input_["trace"])
        )
    if "guardrail_identifier" in input_:
        headers["X-Amzn-Bedrock-GuardrailIdentifier"] = input_["guardrail_identifier"]
    if "guardrail_version" in input_:
        headers["X-Amzn-Bedrock-GuardrailVersion"] = input_["guardrail_version"]
    headers["X-Amzn-Bedrock-PerformanceConfig-Latency"] = (
        capo_bedrock_runtime.types.performance_config_latency.serialize_json(
            input_.get("performance_config_latency", "standard")
        )
    )
    if "service_tier" in input_:
        headers["X-Amzn-Bedrock-Service-Tier"] = (
            capo_bedrock_runtime.types.service_tier_type.serialize_json(
                input_["service_tier"]
            )
        )
    if "request_metadata" in input_:
        headers["X-Amzn-Bedrock-Request-Metadata"] = input_["request_metadata"]
    if "body" in input_:
        body: bytes | None = input_["body"]
        headers["content-type"] = "application/octet-stream"
    else:
        body = b""
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


def invoke_model(
    options: OperationOptions,
    input_: capo_bedrock_runtime.types.invoke_model_request.InvokeModelRequest,
) -> tuple[
    capo_bedrock_runtime.types.invoke_model_response.InvokeModelResponse,
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


async def async_invoke_model(
    options: AsyncOperationOptions,
    input_: capo_bedrock_runtime.types.invoke_model_request.InvokeModelRequest,
) -> tuple[
    capo_bedrock_runtime.types.invoke_model_response.InvokeModelResponse,
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
