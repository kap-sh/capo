"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateStream``."""

from __future__ import annotations

import json
from typing import Any, cast

import zapros
from typing_extensions import Never

import capo_bedrock_agent_runtime._auth._signers
import capo_bedrock_agent_runtime._auth._sigv4
import capo_bedrock_agent_runtime._protocol.eventstream
import capo_bedrock_agent_runtime.errors.access_denied_exception
import capo_bedrock_agent_runtime.errors.bad_gateway_exception
import capo_bedrock_agent_runtime.errors.conflict_exception
import capo_bedrock_agent_runtime.errors.dependency_failed_exception
import capo_bedrock_agent_runtime.errors.internal_server_exception
import capo_bedrock_agent_runtime.errors.resource_not_found_exception
import capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception
import capo_bedrock_agent_runtime.errors.throttling_exception
import capo_bedrock_agent_runtime.errors.validation_exception
import capo_bedrock_agent_runtime.types.retrieve_and_generate_configuration
import capo_bedrock_agent_runtime.types.retrieve_and_generate_input
import capo_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration
import capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_request
import capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response
import capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response_output
import capo_bedrock_agent_runtime.types.user_context
from capo_bedrock_agent_runtime._protocol.errors import parse_error_metadata_json
from capo_bedrock_agent_runtime._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from capo_bedrock_agent_runtime._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_bedrock_agent_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_bedrock_agent_runtime.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "BadGatewayException":
            raise capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException.from_json(
                data, message
            )
        case "ConflictException":
            raise capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException.from_json(
                data, message
            )
        case "DependencyFailedException":
            raise capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_bedrock_agent_runtime.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response.RetrieveAndGenerateStreamResponse:
    _message_decoder = MessageDecoder()
    _union_deser = capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response_output.deserialize_event_json
    _iter = cast(Any, response.iter_bytes())
    out: capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response.RetrieveAndGenerateStreamResponse = {
        "stream": cast(Any, raw_stream_to_events(_iter, _message_decoder, _union_deser))
    }  # type: ignore[reportAssignmentType]
    out["session_id"] = response.headers["x-amzn-bedrock-knowledge-base-session-id"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response.RetrieveAndGenerateStreamResponse:
    _message_decoder = MessageDecoder()
    _union_deser = capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response_output.deserialize_event_json
    _iter = cast(Any, response.async_iter_bytes())
    out: capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response.RetrieveAndGenerateStreamResponse = {
        "stream": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    out["session_id"] = response.headers["x-amzn-bedrock-knowledge-base-session-id"]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_bedrock_agent_runtime._auth._signers.Signer | None:
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
            sigv4_config = (
                capo_bedrock_agent_runtime._auth._sigv4.build_sigv4_auth_scheme(
                    "bedrock", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_bedrock_agent_runtime._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_request.RetrieveAndGenerateStreamRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/retrieveAndGenerateStream"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_request.serialize_json(
            input_
        ),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/json"
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


def retrieve_and_generate_stream(
    options: OperationOptions,
    input_: capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_request.RetrieveAndGenerateStreamRequest,
) -> tuple[
    capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response.RetrieveAndGenerateStreamResponse,
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


async def async_retrieve_and_generate_stream(
    options: AsyncOperationOptions,
    input_: capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_request.RetrieveAndGenerateStreamRequest,
) -> tuple[
    capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response.RetrieveAndGenerateStreamResponse,
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
