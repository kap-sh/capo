"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithBidirectionalStream``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_bedrock_runtime._auth._signers
import capo_bedrock_runtime._auth._sigv4
import capo_bedrock_runtime._iter
import capo_bedrock_runtime._protocol.eventstream
import capo_bedrock_runtime.errors.access_denied_exception
import capo_bedrock_runtime.errors.internal_server_exception
import capo_bedrock_runtime.errors.model_error_exception
import capo_bedrock_runtime.errors.model_not_ready_exception
import capo_bedrock_runtime.errors.model_stream_error_exception
import capo_bedrock_runtime.errors.model_timeout_exception
import capo_bedrock_runtime.errors.resource_not_found_exception
import capo_bedrock_runtime.errors.service_quota_exceeded_exception
import capo_bedrock_runtime.errors.service_unavailable_exception
import capo_bedrock_runtime.errors.throttling_exception
import capo_bedrock_runtime.errors.validation_exception
import capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input
import capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_output
import capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request
import capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response
from capo_bedrock_runtime._protocol.errors import parse_error_metadata_json
from capo_bedrock_runtime._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from capo_bedrock_runtime._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_bedrock_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
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
        case "ModelStreamErrorException":
            raise capo_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException.from_json(
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
) -> capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse:
    _message_decoder = MessageDecoder()
    _union_deser = capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_output.deserialize_event_json
    _iter = cast(Any, response.iter_bytes())
    out: capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse = {
        "body": cast(Any, raw_stream_to_events(_iter, _message_decoder, _union_deser))
    }  # type: ignore[reportAssignmentType]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse:
    _message_decoder = MessageDecoder()
    _union_deser = capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_output.deserialize_event_json
    _iter = cast(Any, response.async_iter_bytes())
    out: capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse = {
        "body": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
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
                    options.credentials_provider,
                    auth_scheme=sigv4_config,
                    event_stream=True,
                )
    if options.bearer_provider is not None:
        return capo_bedrock_runtime._auth._signers.HttpBearerSigner(
            options.bearer_provider
        )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/model/{modelId}/invoke-with-bidirectional-stream"
    url = url.replace("{modelId}", quote(input_["model_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}

    body = capo_bedrock_runtime._iter.map_sync_iterator(
        input_["body"],
        capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input.serialize_event_json,
    )

    headers["content-type"] = "application/vnd.amazon-eventstream"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def async_build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/model/{modelId}/invoke-with-bidirectional-stream"
    url = url.replace("{modelId}", quote(input_["model_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}

    body = capo_bedrock_runtime._iter.map_async_iterator(
        input_["body"],
        capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input.serialize_event_json,
    )

    headers["content-type"] = "application/vnd.amazon-eventstream"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def invoke_model_with_bidirectional_stream(
    options: OperationOptions,
    input_: capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest,
) -> tuple[
    capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_invoke_model_with_bidirectional_stream(
    options: AsyncOperationOptions,
    input_: capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest,
) -> tuple[
    capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(
        async_build_request(options, input_)
    )
    try:
        if response.status >= 300:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
