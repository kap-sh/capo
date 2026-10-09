"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionPackage``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_tnb._auth._signers
import capo_tnb._auth._sigv4
import capo_tnb._protocol.eventstream
import capo_tnb.errors.access_denied_exception
import capo_tnb.errors.internal_server_exception
import capo_tnb.errors.resource_not_found_exception
import capo_tnb.errors.throttling_exception
import capo_tnb.errors.validation_exception
import capo_tnb.types.get_sol_function_package_input
import capo_tnb.types.get_sol_function_package_metadata
import capo_tnb.types.get_sol_function_package_output
import capo_tnb.types.onboarding_state
import capo_tnb.types.operational_state
import capo_tnb.types.tag_map
import capo_tnb.types.usage_state
from capo_tnb._protocol.errors import parse_error_metadata_json
from capo_tnb._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_tnb._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_tnb.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_tnb.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_tnb.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_tnb.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_tnb.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_tnb.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_tnb.types.get_sol_function_package_output.GetSolFunctionPackageOutput:
    out: capo_tnb.types.get_sol_function_package_output.GetSolFunctionPackageOutput = (
        capo_tnb.types.get_sol_function_package_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_tnb.types.get_sol_function_package_output.GetSolFunctionPackageOutput:
    out: capo_tnb.types.get_sol_function_package_output.GetSolFunctionPackageOutput = (
        capo_tnb.types.get_sol_function_package_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_tnb._auth._signers.Signer | None:
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
            sigv4_config = capo_tnb._auth._sigv4.build_sigv4_auth_scheme(
                "tnb", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_tnb._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_tnb.types.get_sol_function_package_input.GetSolFunctionPackageInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/sol/vnfpkgm/v1/vnf_packages/{vnfPkgId}"
    url = url.replace("{vnfPkgId}", quote(input_["vnf_pkg_id"], safe=""))
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


def get_sol_function_package(
    options: OperationOptions,
    input_: capo_tnb.types.get_sol_function_package_input.GetSolFunctionPackageInput,
) -> tuple[
    capo_tnb.types.get_sol_function_package_output.GetSolFunctionPackageOutput,
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


async def async_get_sol_function_package(
    options: AsyncOperationOptions,
    input_: capo_tnb.types.get_sol_function_package_input.GetSolFunctionPackageInput,
) -> tuple[
    capo_tnb.types.get_sol_function_package_output.GetSolFunctionPackageOutput,
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
