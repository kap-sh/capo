"""Generated from Smithy shape ``com.amazonaws.signin#CreateOAuth2TokenWithTokenExchange``."""

from __future__ import annotations

import json

import zapros
from typing_extensions import Never

import capo_signin._auth._signers
import capo_signin._auth._sigv4
import capo_signin._protocol.eventstream
import capo_signin.errors.internal_server_exception
import capo_signin.errors.invalid_grant_exception
import capo_signin.errors.invalid_scope_exception
import capo_signin.errors.service_unavailable_exception
import capo_signin.errors.too_many_requests_error
import capo_signin.errors.validation_exception
import capo_signin.types.create_o_auth2_token_with_token_exchange_request
import capo_signin.types.create_o_auth2_token_with_token_exchange_response
from capo_signin._protocol.errors import parse_error_metadata_json
from capo_signin._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_signin._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_signin.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            raise capo_signin.errors.internal_server_exception.InternalServerException.from_json(
                data, message, response=response
            )
        case "InvalidGrantException":
            raise capo_signin.errors.invalid_grant_exception.InvalidGrantException.from_json(
                data, message, response=response
            )
        case "InvalidScopeException":
            raise capo_signin.errors.invalid_scope_exception.InvalidScopeException.from_json(
                data, message, response=response
            )
        case "ServiceUnavailableException":
            raise capo_signin.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message, response=response
            )
        case "TooManyRequestsError":
            raise capo_signin.errors.too_many_requests_error.TooManyRequestsError.from_json(
                data, message, response=response
            )
        case "ValidationException":
            raise capo_signin.errors.validation_exception.ValidationException.from_json(
                data, message, response=response
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_signin.types.create_o_auth2_token_with_token_exchange_response.CreateOAuth2TokenWithTokenExchangeResponse:
    out: capo_signin.types.create_o_auth2_token_with_token_exchange_response.CreateOAuth2TokenWithTokenExchangeResponse = capo_signin.types.create_o_auth2_token_with_token_exchange_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_signin.types.create_o_auth2_token_with_token_exchange_response.CreateOAuth2TokenWithTokenExchangeResponse:
    out: capo_signin.types.create_o_auth2_token_with_token_exchange_response.CreateOAuth2TokenWithTokenExchangeResponse = capo_signin.types.create_o_auth2_token_with_token_exchange_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_signin.types.create_o_auth2_token_with_token_exchange_request.CreateOAuth2TokenWithTokenExchangeRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
            IsControlPlane=options.is_control_plane,
            IsOAuthEndpoint=True,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/token?x-amz-oauth-token-method=token-exchange"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_signin.types.create_o_auth2_token_with_token_exchange_request.serialize_json(
            input_
        ),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/json"
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(normalized_url, "POST", headers=headers, body=body)


def create_o_auth2_token_with_token_exchange(
    options: OperationOptions,
    input_: capo_signin.types.create_o_auth2_token_with_token_exchange_request.CreateOAuth2TokenWithTokenExchangeRequest,
) -> tuple[
    capo_signin.types.create_o_auth2_token_with_token_exchange_response.CreateOAuth2TokenWithTokenExchangeResponse,
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


async def async_create_o_auth2_token_with_token_exchange(
    options: AsyncOperationOptions,
    input_: capo_signin.types.create_o_auth2_token_with_token_exchange_request.CreateOAuth2TokenWithTokenExchangeRequest,
) -> tuple[
    capo_signin.types.create_o_auth2_token_with_token_exchange_response.CreateOAuth2TokenWithTokenExchangeResponse,
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
