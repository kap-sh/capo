"""Generated from Smithy shape ``com.amazonaws.ssooidc#RegisterClient``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_sso_oidc._auth._signers
import capo_sso_oidc._auth._sigv4
import capo_sso_oidc._protocol.eventstream
import capo_sso_oidc.errors.internal_server_exception
import capo_sso_oidc.errors.invalid_client_metadata_exception
import capo_sso_oidc.errors.invalid_redirect_uri_exception
import capo_sso_oidc.errors.invalid_request_exception
import capo_sso_oidc.errors.invalid_scope_exception
import capo_sso_oidc.errors.slow_down_exception
import capo_sso_oidc.errors.unsupported_grant_type_exception
import capo_sso_oidc.types.grant_types
import capo_sso_oidc.types.redirect_uris
import capo_sso_oidc.types.register_client_request
import capo_sso_oidc.types.register_client_response
import capo_sso_oidc.types.scopes
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
                data, message
            )
        case "InvalidClientMetadataException":
            raise capo_sso_oidc.errors.invalid_client_metadata_exception.InvalidClientMetadataException.from_json(
                data, message
            )
        case "InvalidRedirectUriException":
            raise capo_sso_oidc.errors.invalid_redirect_uri_exception.InvalidRedirectUriException.from_json(
                data, message
            )
        case "InvalidRequestException":
            raise capo_sso_oidc.errors.invalid_request_exception.InvalidRequestException.from_json(
                data, message
            )
        case "InvalidScopeException":
            raise capo_sso_oidc.errors.invalid_scope_exception.InvalidScopeException.from_json(
                data, message
            )
        case "SlowDownException":
            raise capo_sso_oidc.errors.slow_down_exception.SlowDownException.from_json(
                data, message
            )
        case "UnsupportedGrantTypeException":
            raise capo_sso_oidc.errors.unsupported_grant_type_exception.UnsupportedGrantTypeException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_sso_oidc.types.register_client_response.RegisterClientResponse:
    out: capo_sso_oidc.types.register_client_response.RegisterClientResponse = (
        capo_sso_oidc.types.register_client_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_sso_oidc.types.register_client_response.RegisterClientResponse:
    out: capo_sso_oidc.types.register_client_response.RegisterClientResponse = (
        capo_sso_oidc.types.register_client_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_sso_oidc._auth._signers.Signer | None:
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
            sigv4_config = capo_sso_oidc._auth._sigv4.build_sigv4_auth_scheme(
                "sso-oauth", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_sso_oidc._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    return None


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_sso_oidc.types.register_client_request.RegisterClientRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/client/register"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_sso_oidc.types.register_client_request.serialize_json(input_),
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


def register_client(
    options: OperationOptions,
    input_: capo_sso_oidc.types.register_client_request.RegisterClientRequest,
) -> tuple[
    capo_sso_oidc.types.register_client_response.RegisterClientResponse, zapros.Response
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


async def async_register_client(
    options: AsyncOperationOptions,
    input_: capo_sso_oidc.types.register_client_request.RegisterClientRequest,
) -> tuple[
    capo_sso_oidc.types.register_client_response.RegisterClientResponse, zapros.Response
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
