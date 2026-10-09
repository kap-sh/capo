"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeHarness``."""

from __future__ import annotations

import json
from typing import Any, cast

import zapros
from typing_extensions import Never

import capo_bedrock_agentcore._auth._signers
import capo_bedrock_agentcore._auth._sigv4
import capo_bedrock_agentcore._protocol.eventstream
import capo_bedrock_agentcore.errors.access_denied_exception
import capo_bedrock_agentcore.errors.internal_server_exception
import capo_bedrock_agentcore.errors.resource_not_found_exception
import capo_bedrock_agentcore.errors.runtime_client_error
import capo_bedrock_agentcore.errors.service_quota_exceeded_exception
import capo_bedrock_agentcore.errors.throttling_exception
import capo_bedrock_agentcore.errors.validation_exception
import capo_bedrock_agentcore.types.harness_allowed_tools
import capo_bedrock_agentcore.types.harness_messages
import capo_bedrock_agentcore.types.harness_model_configuration
import capo_bedrock_agentcore.types.harness_skills
import capo_bedrock_agentcore.types.harness_system_prompt
import capo_bedrock_agentcore.types.harness_tools
import capo_bedrock_agentcore.types.invoke_harness_request
import capo_bedrock_agentcore.types.invoke_harness_response
import capo_bedrock_agentcore.types.invoke_harness_stream_output
from capo_bedrock_agentcore._protocol.errors import parse_error_metadata_json
from capo_bedrock_agentcore._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from capo_bedrock_agentcore._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_bedrock_agentcore._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_bedrock_agentcore.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "RuntimeClientError":
            raise capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError.from_json(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_bedrock_agentcore.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse:
    _message_decoder = MessageDecoder()
    _union_deser = (
        capo_bedrock_agentcore.types.invoke_harness_stream_output.deserialize_event_json
    )
    _iter = cast(Any, response.iter_bytes())
    out: capo_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse = {
        "stream": cast(Any, raw_stream_to_events(_iter, _message_decoder, _union_deser))
    }  # type: ignore[reportAssignmentType]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse:
    _message_decoder = MessageDecoder()
    _union_deser = (
        capo_bedrock_agentcore.types.invoke_harness_stream_output.deserialize_event_json
    )
    _iter = cast(Any, response.async_iter_bytes())
    out: capo_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse = {
        "stream": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_bedrock_agentcore._auth._signers.Signer | None:
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
            sigv4_config = capo_bedrock_agentcore._auth._sigv4.build_sigv4_auth_scheme(
                "bedrock-agentcore", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_bedrock_agentcore._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_bedrock_agentcore.types.invoke_harness_request.InvokeHarnessRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/harnesses/invoke"
    params: list[tuple[str, str]] = []
    if "harness_arn" in input_:
        params.append(("harnessArn", input_["harness_arn"]))
    if "qualifier" in input_:
        params.append(("qualifier", input_["qualifier"]))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "runtime_session_id" in input_:
        headers["X-Amzn-Bedrock-AgentCore-Runtime-Session-Id"] = input_[
            "runtime_session_id"
        ]
    if "runtime_user_id" in input_:
        headers["X-Amzn-Bedrock-AgentCore-Runtime-User-Id"] = input_["runtime_user_id"]
    if "trace_parent" in input_:
        headers["traceparent"] = input_["trace_parent"]
    if "trace_state" in input_:
        headers["tracestate"] = input_["trace_state"]
    if "trace_id" in input_:
        headers["X-Amzn-Trace-Id"] = input_["trace_id"]
    if "baggage" in input_:
        headers["baggage"] = input_["baggage"]
    body: bytes | None = json.dumps(
        capo_bedrock_agentcore.types.invoke_harness_request.serialize_json(input_),
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


def invoke_harness(
    options: OperationOptions,
    input_: capo_bedrock_agentcore.types.invoke_harness_request.InvokeHarnessRequest,
) -> tuple[
    capo_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse,
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


async def async_invoke_harness(
    options: AsyncOperationOptions,
    input_: capo_bedrock_agentcore.types.invoke_harness_request.InvokeHarnessRequest,
) -> tuple[
    capo_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse,
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
