"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DeleteAccessToken``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_codecatalyst._auth._signers
import capo_codecatalyst._auth._sigv4
import capo_codecatalyst._protocol.eventstream
import capo_codecatalyst.errors.access_denied_exception
import capo_codecatalyst.errors.conflict_exception
import capo_codecatalyst.errors.resource_not_found_exception
import capo_codecatalyst.errors.service_quota_exceeded_exception
import capo_codecatalyst.errors.throttling_exception
import capo_codecatalyst.errors.validation_exception
import capo_codecatalyst.types.delete_access_token_request
import capo_codecatalyst.types.delete_access_token_response
from capo_codecatalyst._protocol.errors import parse_error_metadata_json
from capo_codecatalyst._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_codecatalyst._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_codecatalyst.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_codecatalyst.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "ConflictException":
            raise capo_codecatalyst.errors.conflict_exception.ConflictException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_codecatalyst.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_codecatalyst.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_codecatalyst.types.delete_access_token_response.DeleteAccessTokenResponse:
    out: capo_codecatalyst.types.delete_access_token_response.DeleteAccessTokenResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_codecatalyst.types.delete_access_token_response.DeleteAccessTokenResponse:
    out: capo_codecatalyst.types.delete_access_token_response.DeleteAccessTokenResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_codecatalyst._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.bearer_provider is not None:
        return capo_codecatalyst._auth._signers.HttpBearerSigner(
            options.bearer_provider
        )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_codecatalyst.types.delete_access_token_request.DeleteAccessTokenRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Region=options.region, Endpoint=options.endpoint
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/accessTokens/{id}"
    url = url.replace("{id}", quote(input_["id"], safe=""))
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
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_access_token(
    options: OperationOptions,
    input_: capo_codecatalyst.types.delete_access_token_request.DeleteAccessTokenRequest,
) -> tuple[
    capo_codecatalyst.types.delete_access_token_response.DeleteAccessTokenResponse,
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


async def async_delete_access_token(
    options: AsyncOperationOptions,
    input_: capo_codecatalyst.types.delete_access_token_request.DeleteAccessTokenRequest,
) -> tuple[
    capo_codecatalyst.types.delete_access_token_response.DeleteAccessTokenResponse,
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
