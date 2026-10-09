"""Generated from Smithy shape ``com.amazonaws.sesv2#PutConfigurationSetDeliveryOptions``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_sesv2._auth._signers
import capo_sesv2._auth._sigv4
import capo_sesv2._protocol.eventstream
import capo_sesv2.errors.bad_request_exception
import capo_sesv2.errors.not_found_exception
import capo_sesv2.errors.too_many_requests_exception
import capo_sesv2.types.put_configuration_set_delivery_options_request
import capo_sesv2.types.put_configuration_set_delivery_options_response
import capo_sesv2.types.tls_policy
from capo_sesv2._protocol.errors import parse_error_metadata_json
from capo_sesv2._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_sesv2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_sesv2.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise capo_sesv2.errors.bad_request_exception.BadRequestException.from_json(
                data, message
            )
        case "NotFoundException":
            raise capo_sesv2.errors.not_found_exception.NotFoundException.from_json(
                data, message
            )
        case "TooManyRequestsException":
            raise capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_sesv2.types.put_configuration_set_delivery_options_response.PutConfigurationSetDeliveryOptionsResponse:
    out: capo_sesv2.types.put_configuration_set_delivery_options_response.PutConfigurationSetDeliveryOptionsResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_sesv2.types.put_configuration_set_delivery_options_response.PutConfigurationSetDeliveryOptionsResponse:
    out: capo_sesv2.types.put_configuration_set_delivery_options_response.PutConfigurationSetDeliveryOptionsResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_sesv2._auth._signers.Signer | None:
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
            sigv4_config = capo_sesv2._auth._sigv4.build_sigv4_auth_scheme(
                "ses", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_sesv2._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_sesv2.types.put_configuration_set_delivery_options_request.PutConfigurationSetDeliveryOptionsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            EndpointId=options.endpoint_id,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/v2/email/configuration-sets/{ConfigurationSetName}/delivery-options"
    )
    url = url.replace(
        "{ConfigurationSetName}", quote(input_["configuration_set_name"], safe="")
    )
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_sesv2.types.put_configuration_set_delivery_options_request.serialize_json(
            input_
        ),
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


def put_configuration_set_delivery_options(
    options: OperationOptions,
    input_: capo_sesv2.types.put_configuration_set_delivery_options_request.PutConfigurationSetDeliveryOptionsRequest,
) -> tuple[
    capo_sesv2.types.put_configuration_set_delivery_options_response.PutConfigurationSetDeliveryOptionsResponse,
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


async def async_put_configuration_set_delivery_options(
    options: AsyncOperationOptions,
    input_: capo_sesv2.types.put_configuration_set_delivery_options_request.PutConfigurationSetDeliveryOptionsRequest,
) -> tuple[
    capo_sesv2.types.put_configuration_set_delivery_options_response.PutConfigurationSetDeliveryOptionsResponse,
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
