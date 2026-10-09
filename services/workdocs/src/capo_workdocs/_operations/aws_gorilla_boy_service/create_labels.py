"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateLabels``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_workdocs._auth._signers
import capo_workdocs._auth._sigv4
import capo_workdocs._protocol.eventstream
import capo_workdocs.errors.entity_not_exists_exception
import capo_workdocs.errors.failed_dependency_exception
import capo_workdocs.errors.service_unavailable_exception
import capo_workdocs.errors.too_many_labels_exception
import capo_workdocs.errors.unauthorized_operation_exception
import capo_workdocs.errors.unauthorized_resource_access_exception
import capo_workdocs.types.create_labels_request
import capo_workdocs.types.create_labels_response
import capo_workdocs.types.shared_labels
from capo_workdocs._protocol.errors import parse_error_metadata_json
from capo_workdocs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_workdocs._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_workdocs.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "EntityNotExistsException":
            raise capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException.from_json(
                data, message
            )
        case "FailedDependencyException":
            raise capo_workdocs.errors.failed_dependency_exception.FailedDependencyException.from_json(
                data, message
            )
        case "ServiceUnavailableException":
            raise capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message
            )
        case "TooManyLabelsException":
            raise capo_workdocs.errors.too_many_labels_exception.TooManyLabelsException.from_json(
                data, message
            )
        case "UnauthorizedOperationException":
            raise capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException.from_json(
                data, message
            )
        case "UnauthorizedResourceAccessException":
            raise capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_workdocs.types.create_labels_response.CreateLabelsResponse:
    out: capo_workdocs.types.create_labels_response.CreateLabelsResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_workdocs.types.create_labels_response.CreateLabelsResponse:
    out: capo_workdocs.types.create_labels_response.CreateLabelsResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_workdocs._auth._signers.Signer | None:
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
            sigv4_config = capo_workdocs._auth._sigv4.build_sigv4_auth_scheme(
                "workdocs", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_workdocs._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_workdocs.types.create_labels_request.CreateLabelsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/api/v1/resources/{ResourceId}/labels"
    url = url.replace("{ResourceId}", quote(input_["resource_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "authentication_token" in input_:
        headers["Authentication"] = input_["authentication_token"]
    body: bytes | None = json.dumps(
        capo_workdocs.types.create_labels_request.serialize_json(input_),
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
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def create_labels(
    options: OperationOptions,
    input_: capo_workdocs.types.create_labels_request.CreateLabelsRequest,
) -> tuple[
    capo_workdocs.types.create_labels_response.CreateLabelsResponse, zapros.Response
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


async def async_create_labels(
    options: AsyncOperationOptions,
    input_: capo_workdocs.types.create_labels_request.CreateLabelsRequest,
) -> tuple[
    capo_workdocs.types.create_labels_response.CreateLabelsResponse, zapros.Response
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
