"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeAgentRuntime``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_bedrock_agentcore._auth._signers
import capo_bedrock_agentcore._auth._sigv4
import capo_bedrock_agentcore._protocol.eventstream
import capo_bedrock_agentcore.errors.access_denied_exception
import capo_bedrock_agentcore.errors.internal_server_exception
import capo_bedrock_agentcore.errors.resource_not_found_exception
import capo_bedrock_agentcore.errors.retryable_conflict_exception
import capo_bedrock_agentcore.errors.runtime_client_error
import capo_bedrock_agentcore.errors.service_quota_exceeded_exception
import capo_bedrock_agentcore.errors.throttling_exception
import capo_bedrock_agentcore.errors.validation_exception
import capo_bedrock_agentcore.types.body
import capo_bedrock_agentcore.types.invoke_agent_runtime_request
import capo_bedrock_agentcore.types.invoke_agent_runtime_response
import capo_bedrock_agentcore.types.response_stream
from capo_bedrock_agentcore._protocol.errors import parse_error_metadata_json
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
        case "RetryableConflictException":
            raise capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException.from_json(
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
) -> capo_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse:
    _iter = cast(Any, response.iter_raw())
    out: capo_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse = {
        "response": _iter
    }  # type: ignore[reportAssignmentType]
    if "X-Amzn-Bedrock-AgentCore-Runtime-Session-Id" in response.headers:
        out["runtime_session_id"] = response.headers[
            "X-Amzn-Bedrock-AgentCore-Runtime-Session-Id"
        ]
    if "Mcp-Session-Id" in response.headers:
        out["mcp_session_id"] = response.headers["Mcp-Session-Id"]
    if "Mcp-Protocol-Version" in response.headers:
        out["mcp_protocol_version"] = response.headers["Mcp-Protocol-Version"]
    if "X-Amzn-Trace-Id" in response.headers:
        out["trace_id"] = response.headers["X-Amzn-Trace-Id"]
    if "traceparent" in response.headers:
        out["trace_parent"] = response.headers["traceparent"]
    if "tracestate" in response.headers:
        out["trace_state"] = response.headers["tracestate"]
    if "baggage" in response.headers:
        out["baggage"] = response.headers["baggage"]
    out["content_type"] = response.headers["Content-Type"]
    out["status_code"] = response.status
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse:
    _iter = cast(Any, response.async_iter_raw())
    out: capo_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse = {
        "response": _iter
    }  # type: ignore[reportAssignmentType]
    if "X-Amzn-Bedrock-AgentCore-Runtime-Session-Id" in response.headers:
        out["runtime_session_id"] = response.headers[
            "X-Amzn-Bedrock-AgentCore-Runtime-Session-Id"
        ]
    if "Mcp-Session-Id" in response.headers:
        out["mcp_session_id"] = response.headers["Mcp-Session-Id"]
    if "Mcp-Protocol-Version" in response.headers:
        out["mcp_protocol_version"] = response.headers["Mcp-Protocol-Version"]
    if "X-Amzn-Trace-Id" in response.headers:
        out["trace_id"] = response.headers["X-Amzn-Trace-Id"]
    if "traceparent" in response.headers:
        out["trace_parent"] = response.headers["traceparent"]
    if "tracestate" in response.headers:
        out["trace_state"] = response.headers["tracestate"]
    if "baggage" in response.headers:
        out["baggage"] = response.headers["baggage"]
    out["content_type"] = response.headers["Content-Type"]
    out["status_code"] = response.status
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
    input_: capo_bedrock_agentcore.types.invoke_agent_runtime_request.InvokeAgentRuntimeRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/runtimes/{agentRuntimeArn}/invocations"
    url = url.replace("{agentRuntimeArn}", quote(input_["agent_runtime_arn"], safe=""))
    params: list[tuple[str, str]] = []
    if "qualifier" in input_:
        params.append(("qualifier", input_["qualifier"]))
    if "account_id" in input_:
        params.append(("accountId", input_["account_id"]))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "content_type" in input_:
        headers["Content-Type"] = input_["content_type"]
    if "accept" in input_:
        headers["Accept"] = input_["accept"]
    if "mcp_session_id" in input_:
        headers["Mcp-Session-Id"] = input_["mcp_session_id"]
    if "runtime_session_id" in input_:
        headers["X-Amzn-Bedrock-AgentCore-Runtime-Session-Id"] = input_[
            "runtime_session_id"
        ]
    if "mcp_protocol_version" in input_:
        headers["Mcp-Protocol-Version"] = input_["mcp_protocol_version"]
    if "mcp_method" in input_:
        headers["Mcp-Method"] = input_["mcp_method"]
    if "mcp_name" in input_:
        headers["Mcp-Name"] = input_["mcp_name"]
    if "runtime_user_id" in input_:
        headers["X-Amzn-Bedrock-AgentCore-Runtime-User-Id"] = input_["runtime_user_id"]
    if "trace_id" in input_:
        headers["X-Amzn-Trace-Id"] = input_["trace_id"]
    if "trace_parent" in input_:
        headers["traceparent"] = input_["trace_parent"]
    if "trace_state" in input_:
        headers["tracestate"] = input_["trace_state"]
    if "baggage" in input_:
        headers["baggage"] = input_["baggage"]
    body: bytes | None = input_["payload"]
    headers["content-type"] = "application/octet-stream"
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


def invoke_agent_runtime(
    options: OperationOptions,
    input_: capo_bedrock_agentcore.types.invoke_agent_runtime_request.InvokeAgentRuntimeRequest,
) -> tuple[
    capo_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse,
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


async def async_invoke_agent_runtime(
    options: AsyncOperationOptions,
    input_: capo_bedrock_agentcore.types.invoke_agent_runtime_request.InvokeAgentRuntimeRequest,
) -> tuple[
    capo_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse,
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
