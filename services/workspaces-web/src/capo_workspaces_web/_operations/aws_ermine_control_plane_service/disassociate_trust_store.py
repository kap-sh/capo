"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DisassociateTrustStore``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_workspaces_web._auth._signers
import capo_workspaces_web._auth._sigv4
import capo_workspaces_web._protocol.eventstream
import capo_workspaces_web.errors.access_denied_exception
import capo_workspaces_web.errors.conflict_exception
import capo_workspaces_web.errors.internal_server_exception
import capo_workspaces_web.errors.resource_not_found_exception
import capo_workspaces_web.errors.throttling_exception
import capo_workspaces_web.errors.validation_exception
import capo_workspaces_web.types.disassociate_trust_store_request
import capo_workspaces_web.types.disassociate_trust_store_response
from capo_workspaces_web._protocol.errors import parse_error_metadata_json
from capo_workspaces_web._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_workspaces_web._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_workspaces_web.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_workspaces_web.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "ConflictException":
            raise capo_workspaces_web.errors.conflict_exception.ConflictException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_workspaces_web.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_workspaces_web.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_workspaces_web.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_workspaces_web.types.disassociate_trust_store_response.DisassociateTrustStoreResponse:
    out: capo_workspaces_web.types.disassociate_trust_store_response.DisassociateTrustStoreResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_workspaces_web.types.disassociate_trust_store_response.DisassociateTrustStoreResponse:
    out: capo_workspaces_web.types.disassociate_trust_store_response.DisassociateTrustStoreResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_workspaces_web._auth._signers.Signer | None:
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
            sigv4_config = capo_workspaces_web._auth._sigv4.build_sigv4_auth_scheme(
                "workspaces-web", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_workspaces_web._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_workspaces_web.types.disassociate_trust_store_request.DisassociateTrustStoreRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/portals/{portalArn+}/trustStores"
    url = url.replace("{portalArn+}", quote(input_["portal_arn"], safe="/"))
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


def disassociate_trust_store(
    options: OperationOptions,
    input_: capo_workspaces_web.types.disassociate_trust_store_request.DisassociateTrustStoreRequest,
) -> tuple[
    capo_workspaces_web.types.disassociate_trust_store_response.DisassociateTrustStoreResponse,
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


async def async_disassociate_trust_store(
    options: AsyncOperationOptions,
    input_: capo_workspaces_web.types.disassociate_trust_store_request.DisassociateTrustStoreRequest,
) -> tuple[
    capo_workspaces_web.types.disassociate_trust_store_response.DisassociateTrustStoreResponse,
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
