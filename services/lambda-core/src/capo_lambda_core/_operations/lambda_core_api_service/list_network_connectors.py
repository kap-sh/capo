"""Generated from Smithy shape ``com.amazonaws.lambdacore#ListNetworkConnectors``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_lambda_core._auth._signers
import capo_lambda_core._auth._sigv4
import capo_lambda_core._protocol.eventstream
import capo_lambda_core.errors.invalid_parameter_value_exception
import capo_lambda_core.errors.service_exception
import capo_lambda_core.errors.too_many_requests_exception
import capo_lambda_core.types.list_network_connectors_request
import capo_lambda_core.types.list_network_connectors_response
import capo_lambda_core.types.network_connector_state
import capo_lambda_core.types.network_connectors_list
from capo_lambda_core._protocol.errors import parse_error_metadata_json
from capo_lambda_core._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_lambda_core._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_lambda_core.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            raise capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data, message
            )
        case "ServiceException":
            raise capo_lambda_core.errors.service_exception.ServiceException.from_json(
                data, message
            )
        case "TooManyRequestsException":
            raise capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_lambda_core.types.list_network_connectors_response.ListNetworkConnectorsResponse:
    out: capo_lambda_core.types.list_network_connectors_response.ListNetworkConnectorsResponse = capo_lambda_core.types.list_network_connectors_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_lambda_core.types.list_network_connectors_response.ListNetworkConnectorsResponse:
    out: capo_lambda_core.types.list_network_connectors_response.ListNetworkConnectorsResponse = capo_lambda_core.types.list_network_connectors_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_lambda_core._auth._signers.Signer | None:
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
            sigv4_config = capo_lambda_core._auth._sigv4.build_sigv4_auth_scheme(
                "lambda", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_lambda_core._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_lambda_core.types.list_network_connectors_request.ListNetworkConnectorsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_lambda_core.types.network_connector_state

    url = endpoint.url.rstrip("/") + "/2026-04-04/network-connectors"
    params: list[tuple[str, str]] = []
    if "state" in input_:
        params.append(
            (
                "State",
                capo_lambda_core.types.network_connector_state.serialize_json(
                    input_["state"]
                ),
            )
        )
    if "marker" in input_:
        params.append(("Marker", input_["marker"]))
    if "max_items" in input_:
        params.append(("MaxItems", str(input_["max_items"])))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_network_connectors(
    options: OperationOptions,
    input_: capo_lambda_core.types.list_network_connectors_request.ListNetworkConnectorsRequest,
) -> tuple[
    capo_lambda_core.types.list_network_connectors_response.ListNetworkConnectorsResponse,
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


async def async_list_network_connectors(
    options: AsyncOperationOptions,
    input_: capo_lambda_core.types.list_network_connectors_request.ListNetworkConnectorsRequest,
) -> tuple[
    capo_lambda_core.types.list_network_connectors_response.ListNetworkConnectorsResponse,
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
