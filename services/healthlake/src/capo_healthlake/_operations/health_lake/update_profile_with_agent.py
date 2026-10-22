"""Generated from Smithy shape ``com.amazonaws.healthlake#UpdateProfileWithAgent``."""

from __future__ import annotations

import functools
import json
from typing import Any, cast

import zapros
from typing_extensions import Never

import capo_healthlake._auth._signers
import capo_healthlake._auth._sigv4
import capo_healthlake._iter
import capo_healthlake._protocol.eventstream
import capo_healthlake.errors.access_denied_exception
import capo_healthlake.errors.internal_server_exception
import capo_healthlake.errors.resource_not_found_exception
import capo_healthlake.errors.throttling_exception
import capo_healthlake.errors.validation_exception
import capo_healthlake.types.agent_input_message
import capo_healthlake.types.agent_output_message_stream
import capo_healthlake.types.update_profile_with_agent_request
import capo_healthlake.types.update_profile_with_agent_response
from capo_healthlake._protocol.errors import parse_error_metadata_json
from capo_healthlake._protocol.eventstream import (
    MessageDecoder,
    async_read_messages,
    read_messages,
)
from capo_healthlake._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_healthlake._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_healthlake.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_healthlake.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_0(
                data, message, response=response
            )
        case "InternalServerException":
            raise capo_healthlake.errors.internal_server_exception.InternalServerException.from_aws_json_1_0(
                data, message, response=response
            )
        case "ResourceNotFoundException":
            raise capo_healthlake.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data, message, response=response
            )
        case "ThrottlingException":
            raise capo_healthlake.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data, message, response=response
            )
        case "ValidationException":
            raise capo_healthlake.errors.validation_exception.ValidationException.from_aws_json_1_0(
                data, message, response=response
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_healthlake.types.update_profile_with_agent_response.UpdateProfileWithAgentResponse:
    _decoder = MessageDecoder()
    _messages = read_messages(response.iter_bytes(), _decoder)
    out: capo_healthlake.types.update_profile_with_agent_response.UpdateProfileWithAgentResponse = {}  # type: ignore[typeddict-item]
    out["agent_response"] = cast(
        Any,
        capo_healthlake._iter.map_sync_iterator(
            _messages,
            functools.partial(
                capo_healthlake.types.agent_output_message_stream.deserialize_event_aws_json_1_0,
                response=response,
            ),
        ),
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_healthlake.types.update_profile_with_agent_response.UpdateProfileWithAgentResponse:
    _decoder = MessageDecoder()
    _messages = async_read_messages(response.async_iter_bytes(), _decoder)
    out: capo_healthlake.types.update_profile_with_agent_response.UpdateProfileWithAgentResponse = {}  # type: ignore[typeddict-item]
    out["agent_response"] = cast(
        Any,
        capo_healthlake._iter.map_async_iterator(
            _messages,
            functools.partial(
                capo_healthlake.types.agent_output_message_stream.deserialize_event_aws_json_1_0,
                response=response,
            ),
        ),
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_healthlake._auth._signers.Signer | None:
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
            sigv4_config = capo_healthlake._auth._sigv4.build_sigv4_auth_scheme(
                "healthlake", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_healthlake._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_healthlake.types.update_profile_with_agent_request.UpdateProfileWithAgentRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/update-profile-with-agent"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "HealthLake.UpdateProfileWithAgent"
    body: bytes | None = json.dumps(
        capo_healthlake.types.update_profile_with_agent_request.serialize_aws_json_1_0(
            input_
        ),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
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


def update_profile_with_agent(
    options: OperationOptions,
    input_: capo_healthlake.types.update_profile_with_agent_request.UpdateProfileWithAgentRequest,
) -> tuple[
    capo_healthlake.types.update_profile_with_agent_response.UpdateProfileWithAgentResponse,
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


async def async_update_profile_with_agent(
    options: AsyncOperationOptions,
    input_: capo_healthlake.types.update_profile_with_agent_request.UpdateProfileWithAgentRequest,
) -> tuple[
    capo_healthlake.types.update_profile_with_agent_response.UpdateProfileWithAgentResponse,
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
