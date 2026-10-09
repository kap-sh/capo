"""Generated from Smithy shape ``com.amazonaws.servicediscovery#UpdateHttpNamespace``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_servicediscovery._auth._signers
import capo_servicediscovery._auth._sigv4
import capo_servicediscovery._protocol.eventstream
import capo_servicediscovery.errors.duplicate_request
import capo_servicediscovery.errors.invalid_input
import capo_servicediscovery.errors.namespace_not_found
import capo_servicediscovery.errors.resource_in_use
import capo_servicediscovery.types.http_namespace_change
import capo_servicediscovery.types.update_http_namespace_request
import capo_servicediscovery.types.update_http_namespace_response
from capo_servicediscovery._protocol.errors import parse_error_metadata_json
from capo_servicediscovery._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_servicediscovery._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_servicediscovery.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "DuplicateRequest":
            raise capo_servicediscovery.errors.duplicate_request.DuplicateRequest.from_aws_json_1_1(
                data, message
            )
        case "InvalidInput":
            raise capo_servicediscovery.errors.invalid_input.InvalidInput.from_aws_json_1_1(
                data, message
            )
        case "NamespaceNotFound":
            raise capo_servicediscovery.errors.namespace_not_found.NamespaceNotFound.from_aws_json_1_1(
                data, message
            )
        case "ResourceInUse":
            raise capo_servicediscovery.errors.resource_in_use.ResourceInUse.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_servicediscovery.types.update_http_namespace_response.UpdateHttpNamespaceResponse:
    out: capo_servicediscovery.types.update_http_namespace_response.UpdateHttpNamespaceResponse = capo_servicediscovery.types.update_http_namespace_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_servicediscovery.types.update_http_namespace_response.UpdateHttpNamespaceResponse:
    out: capo_servicediscovery.types.update_http_namespace_response.UpdateHttpNamespaceResponse = capo_servicediscovery.types.update_http_namespace_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_servicediscovery._auth._signers.Signer | None:
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
            sigv4_config = capo_servicediscovery._auth._sigv4.build_sigv4_auth_scheme(
                "servicediscovery", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_servicediscovery._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_servicediscovery.types.update_http_namespace_request.UpdateHttpNamespaceRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "Route53AutoNaming_v20170314.UpdateHttpNamespace"
    body: bytes | None = json.dumps(
        capo_servicediscovery.types.update_http_namespace_request.serialize_aws_json_1_1(
            input_
        ),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
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


def update_http_namespace(
    options: OperationOptions,
    input_: capo_servicediscovery.types.update_http_namespace_request.UpdateHttpNamespaceRequest,
) -> tuple[
    capo_servicediscovery.types.update_http_namespace_response.UpdateHttpNamespaceResponse,
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


async def async_update_http_namespace(
    options: AsyncOperationOptions,
    input_: capo_servicediscovery.types.update_http_namespace_request.UpdateHttpNamespaceRequest,
) -> tuple[
    capo_servicediscovery.types.update_http_namespace_response.UpdateHttpNamespaceResponse,
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
