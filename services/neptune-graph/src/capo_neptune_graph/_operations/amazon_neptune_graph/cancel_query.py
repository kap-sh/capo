"""Generated from Smithy shape ``com.amazonaws.neptunegraph#CancelQuery``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_neptune_graph._auth._signers
import capo_neptune_graph._auth._sigv4
import capo_neptune_graph._protocol.eventstream
import capo_neptune_graph.errors.access_denied_exception
import capo_neptune_graph.errors.internal_server_exception
import capo_neptune_graph.errors.resource_not_found_exception
import capo_neptune_graph.errors.throttling_exception
import capo_neptune_graph.errors.validation_exception
import capo_neptune_graph.types.cancel_query_input
from capo_neptune_graph._protocol.errors import parse_error_metadata_json
from capo_neptune_graph._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_neptune_graph._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_neptune_graph.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_neptune_graph.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_neptune_graph.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_neptune_graph.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_neptune_graph.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_neptune_graph._auth._signers.Signer | None:
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
            sigv4_config = capo_neptune_graph._auth._sigv4.build_sigv4_auth_scheme(
                "neptune-graph", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_neptune_graph._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_neptune_graph.types.cancel_query_input.CancelQueryInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
            ApiType="DataPlane",
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/queries/{queryId}"
    url = url.replace("{queryId}", quote(input_["query_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "graph_identifier" in input_:
        headers["graphIdentifier"] = input_["graph_identifier"]
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


def cancel_query(
    options: OperationOptions,
    input_: capo_neptune_graph.types.cancel_query_input.CancelQueryInput,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_cancel_query(
    options: AsyncOperationOptions,
    input_: capo_neptune_graph.types.cancel_query_input.CancelQueryInput,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return None, response
    except BaseException:
        await response.aclose()
        raise
