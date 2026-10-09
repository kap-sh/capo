"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetEvent``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_bedrock_agentcore._auth._signers
import capo_bedrock_agentcore._auth._sigv4
import capo_bedrock_agentcore._protocol.eventstream
import capo_bedrock_agentcore.errors.access_denied_exception
import capo_bedrock_agentcore.errors.invalid_input_exception
import capo_bedrock_agentcore.errors.resource_not_found_exception
import capo_bedrock_agentcore.errors.service_exception
import capo_bedrock_agentcore.errors.service_quota_exceeded_exception
import capo_bedrock_agentcore.errors.throttled_exception
import capo_bedrock_agentcore.errors.validation_exception
import capo_bedrock_agentcore.types.event
import capo_bedrock_agentcore.types.get_event_input
import capo_bedrock_agentcore.types.get_event_output
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
        case "InvalidInputException":
            raise capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ServiceException":
            raise capo_bedrock_agentcore.errors.service_exception.ServiceException.from_json(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data, message
            )
        case "ThrottledException":
            raise capo_bedrock_agentcore.errors.throttled_exception.ThrottledException.from_json(
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
) -> capo_bedrock_agentcore.types.get_event_output.GetEventOutput:
    out: capo_bedrock_agentcore.types.get_event_output.GetEventOutput = (
        capo_bedrock_agentcore.types.get_event_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_bedrock_agentcore.types.get_event_output.GetEventOutput:
    out: capo_bedrock_agentcore.types.get_event_output.GetEventOutput = (
        capo_bedrock_agentcore.types.get_event_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
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
    input_: capo_bedrock_agentcore.types.get_event_input.GetEventInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/memories/{memoryId}/actor/{actorId}/sessions/{sessionId}/events/{eventId}"
    )
    url = url.replace("{memoryId}", quote(input_["memory_id"], safe=""))
    url = url.replace("{sessionId}", quote(input_["session_id"], safe=""))
    url = url.replace("{actorId}", quote(input_["actor_id"], safe=""))
    url = url.replace("{eventId}", quote(input_["event_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
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
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_event(
    options: OperationOptions,
    input_: capo_bedrock_agentcore.types.get_event_input.GetEventInput,
) -> tuple[
    capo_bedrock_agentcore.types.get_event_output.GetEventOutput, zapros.Response
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


async def async_get_event(
    options: AsyncOperationOptions,
    input_: capo_bedrock_agentcore.types.get_event_input.GetEventInput,
) -> tuple[
    capo_bedrock_agentcore.types.get_event_output.GetEventOutput, zapros.Response
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
