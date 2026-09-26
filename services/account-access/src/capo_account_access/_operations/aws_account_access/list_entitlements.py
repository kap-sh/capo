"""Generated from Smithy shape ``com.amazonaws.accountaccess#ListEntitlements``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_account_access._auth._signers
import capo_account_access._auth._sigv4
import capo_account_access._protocol.eventstream
import capo_account_access.errors.access_denied_exception
import capo_account_access.errors.internal_server_exception
import capo_account_access.errors.resource_not_found_exception
import capo_account_access.errors.throttling_exception
import capo_account_access.errors.validation_exception
import capo_account_access.types.entitlement_filter
import capo_account_access.types.entitlements_list
import capo_account_access.types.list_entitlements_request
import capo_account_access.types.list_entitlements_response
from capo_account_access._protocol.errors import parse_error_metadata_json
from capo_account_access._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_account_access._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_account_access.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_account_access.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_account_access.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_account_access.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_account_access.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_account_access.types.list_entitlements_response.ListEntitlementsResponse:
    out: capo_account_access.types.list_entitlements_response.ListEntitlementsResponse = capo_account_access.types.list_entitlements_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_account_access.types.list_entitlements_response.ListEntitlementsResponse:
    out: capo_account_access.types.list_entitlements_response.ListEntitlementsResponse = capo_account_access.types.list_entitlements_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_account_access._auth._signers.Signer | None:
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
            sigv4_config = capo_account_access._auth._sigv4.build_sigv4_auth_scheme(
                "account-access", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_account_access._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_account_access.types.list_entitlements_request.ListEntitlementsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/entitlements-list"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_account_access.types.list_entitlements_request.serialize_json(input_),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def list_entitlements(
    options: OperationOptions,
    input_: capo_account_access.types.list_entitlements_request.ListEntitlementsRequest,
) -> tuple[
    capo_account_access.types.list_entitlements_response.ListEntitlementsResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_list_entitlements(
    options: AsyncOperationOptions,
    input_: capo_account_access.types.list_entitlements_request.ListEntitlementsRequest,
) -> tuple[
    capo_account_access.types.list_entitlements_response.ListEntitlementsResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
