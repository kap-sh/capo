"""Generated from Smithy shape ``com.amazonaws.accountaccessruntime#ListRoles``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_account_access_runtime._auth._signers
import capo_account_access_runtime._auth._sigv4
import capo_account_access_runtime._protocol.eventstream
import capo_account_access_runtime.errors.internal_server_exception
import capo_account_access_runtime.errors.throttling_exception
import capo_account_access_runtime.errors.unauthorized_exception
import capo_account_access_runtime.errors.validation_exception
import capo_account_access_runtime.types.access_details_list
import capo_account_access_runtime.types.list_roles_request
import capo_account_access_runtime.types.list_roles_response
from capo_account_access_runtime._protocol.errors import parse_error_metadata_json
from capo_account_access_runtime._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_account_access_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_account_access_runtime.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            raise capo_account_access_runtime.errors.internal_server_exception.InternalServerException.from_json(
                data, message, response=response
            )
        case "ThrottlingException":
            raise capo_account_access_runtime.errors.throttling_exception.ThrottlingException.from_json(
                data, message, response=response
            )
        case "UnauthorizedException":
            raise capo_account_access_runtime.errors.unauthorized_exception.UnauthorizedException.from_json(
                data, message, response=response
            )
        case "ValidationException":
            raise capo_account_access_runtime.errors.validation_exception.ValidationException.from_json(
                data, message, response=response
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_account_access_runtime.types.list_roles_response.ListRolesResponse:
    out: capo_account_access_runtime.types.list_roles_response.ListRolesResponse = (
        capo_account_access_runtime.types.list_roles_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_account_access_runtime.types.list_roles_response.ListRolesResponse:
    out: capo_account_access_runtime.types.list_roles_response.ListRolesResponse = (
        capo_account_access_runtime.types.list_roles_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_account_access_runtime._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.bearer_provider is not None:
        return capo_account_access_runtime._auth._signers.HttpBearerSigner(
            options.bearer_provider
        )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_account_access_runtime.types.list_roles_request.ListRolesRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/access"
    params: list[tuple[str, str]] = []
    if "tenant_id" in input_:
        params.append(("tenantId", input_["tenant_id"]))
    if "max_results" in input_:
        params.append(("maxResults", str(input_["max_results"])))
    if "next_token" in input_:
        params.append(("nextToken", input_["next_token"]))
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


def list_roles(
    options: OperationOptions,
    input_: capo_account_access_runtime.types.list_roles_request.ListRolesRequest,
) -> tuple[
    capo_account_access_runtime.types.list_roles_response.ListRolesResponse,
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


async def async_list_roles(
    options: AsyncOperationOptions,
    input_: capo_account_access_runtime.types.list_roles_request.ListRolesRequest,
) -> tuple[
    capo_account_access_runtime.types.list_roles_response.ListRolesResponse,
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
