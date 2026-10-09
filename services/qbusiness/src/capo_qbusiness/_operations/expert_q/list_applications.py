"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListApplications``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_qbusiness._auth._signers
import capo_qbusiness._auth._sigv4
import capo_qbusiness._protocol.eventstream
import capo_qbusiness.errors.access_denied_exception
import capo_qbusiness.errors.internal_server_exception
import capo_qbusiness.errors.throttling_exception
import capo_qbusiness.errors.validation_exception
import capo_qbusiness.types.applications
import capo_qbusiness.types.list_applications_request
import capo_qbusiness.types.list_applications_response
from capo_qbusiness._protocol.errors import parse_error_metadata_json
from capo_qbusiness._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_qbusiness._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_qbusiness.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_qbusiness.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_qbusiness.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_qbusiness.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_qbusiness.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_qbusiness.types.list_applications_response.ListApplicationsResponse:
    out: capo_qbusiness.types.list_applications_response.ListApplicationsResponse = (
        capo_qbusiness.types.list_applications_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_qbusiness.types.list_applications_response.ListApplicationsResponse:
    out: capo_qbusiness.types.list_applications_response.ListApplicationsResponse = (
        capo_qbusiness.types.list_applications_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_qbusiness._auth._signers.Signer | None:
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
            sigv4_config = capo_qbusiness._auth._sigv4.build_sigv4_auth_scheme(
                "qbusiness", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_qbusiness._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_qbusiness.types.list_applications_request.ListApplicationsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region, UseFIPS=options.use_fips, Endpoint=options.endpoint
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/applications"
    params: list[tuple[str, str]] = []
    if "next_token" in input_:
        params.append(("nextToken", input_["next_token"]))
    if "max_results" in input_:
        params.append(("maxResults", str(input_["max_results"])))
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


def list_applications(
    options: OperationOptions,
    input_: capo_qbusiness.types.list_applications_request.ListApplicationsRequest,
) -> tuple[
    capo_qbusiness.types.list_applications_response.ListApplicationsResponse,
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


async def async_list_applications(
    options: AsyncOperationOptions,
    input_: capo_qbusiness.types.list_applications_request.ListApplicationsRequest,
) -> tuple[
    capo_qbusiness.types.list_applications_response.ListApplicationsResponse,
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
