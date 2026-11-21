"""Generated from Smithy shape ``com.amazonaws.ssooidc#StartDeviceAuthorization``."""

from __future__ import annotations

import json

import zapros
from typing_extensions import Never

import capo_sso_oidc._auth._signers
import capo_sso_oidc._auth._sigv4
import capo_sso_oidc._protocol.eventstream
import capo_sso_oidc.errors.internal_server_exception
import capo_sso_oidc.errors.invalid_client_exception
import capo_sso_oidc.errors.invalid_request_exception
import capo_sso_oidc.errors.slow_down_exception
import capo_sso_oidc.errors.unauthorized_client_exception
import capo_sso_oidc.types.start_device_authorization_request
import capo_sso_oidc.types.start_device_authorization_response
from capo_sso_oidc._protocol.errors import parse_error_metadata_json
from capo_sso_oidc._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_sso_oidc._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_sso_oidc.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            raise capo_sso_oidc.errors.internal_server_exception.InternalServerException.from_json(
                data, message, response=response
            )
        case "InvalidClientException":
            raise capo_sso_oidc.errors.invalid_client_exception.InvalidClientException.from_json(
                data, message, response=response
            )
        case "InvalidRequestException":
            raise capo_sso_oidc.errors.invalid_request_exception.InvalidRequestException.from_json(
                data, message, response=response
            )
        case "SlowDownException":
            raise capo_sso_oidc.errors.slow_down_exception.SlowDownException.from_json(
                data, message, response=response
            )
        case "UnauthorizedClientException":
            raise capo_sso_oidc.errors.unauthorized_client_exception.UnauthorizedClientException.from_json(
                data, message, response=response
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_sso_oidc.types.start_device_authorization_response.StartDeviceAuthorizationResponse:
    out: capo_sso_oidc.types.start_device_authorization_response.StartDeviceAuthorizationResponse = capo_sso_oidc.types.start_device_authorization_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_sso_oidc.types.start_device_authorization_response.StartDeviceAuthorizationResponse:
    out: capo_sso_oidc.types.start_device_authorization_response.StartDeviceAuthorizationResponse = capo_sso_oidc.types.start_device_authorization_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_sso_oidc.types.start_device_authorization_request.StartDeviceAuthorizationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/device_authorization"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_sso_oidc.types.start_device_authorization_request.serialize_json(input_),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/json"
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(normalized_url, "POST", headers=headers, body=body)


def start_device_authorization(
    options: OperationOptions,
    input_: capo_sso_oidc.types.start_device_authorization_request.StartDeviceAuthorizationRequest,
) -> tuple[
    capo_sso_oidc.types.start_device_authorization_response.StartDeviceAuthorizationResponse,
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


async def async_start_device_authorization(
    options: AsyncOperationOptions,
    input_: capo_sso_oidc.types.start_device_authorization_request.StartDeviceAuthorizationRequest,
) -> tuple[
    capo_sso_oidc.types.start_device_authorization_response.StartDeviceAuthorizationResponse,
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
