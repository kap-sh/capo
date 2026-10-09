"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DescribeEventBus``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_eventbridgev2._auth._signers
import capo_eventbridgev2._auth._sigv4
import capo_eventbridgev2._protocol.eventstream
import capo_eventbridgev2.errors.access_denied_exception
import capo_eventbridgev2.errors.internal_exception
import capo_eventbridgev2.errors.invalid_input_exception
import capo_eventbridgev2.errors.resource_not_found_exception
import capo_eventbridgev2.errors.throttling_exception
import capo_eventbridgev2.types.bus_state
import capo_eventbridgev2.types.describe_event_bus_request
import capo_eventbridgev2.types.describe_event_bus_response
import capo_eventbridgev2.types.encryption_configuration
import capo_eventbridgev2.types.storage_configuration_output
import capo_eventbridgev2.types.timestamp
from capo_eventbridgev2._protocol import cbor
from capo_eventbridgev2._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_eventbridgev2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_eventbridgev2.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data, code, message = cbor.parse_error(response)
    match code:
        case "AccessDeniedException":
            raise capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException.from_cbor(
                data, message
            )
        case "InternalException":
            raise capo_eventbridgev2.errors.internal_exception.InternalException.from_cbor(
                data, message
            )
        case "InvalidInputException":
            raise capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException.from_cbor(
                data, message
            )
        case "ThrottlingException":
            raise capo_eventbridgev2.errors.throttling_exception.ThrottlingException.from_cbor(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException.from_cbor(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_eventbridgev2.types.describe_event_bus_response.DescribeEventBusResponse:
    out: capo_eventbridgev2.types.describe_event_bus_response.DescribeEventBusResponse = capo_eventbridgev2.types.describe_event_bus_response.deserialize_cbor(
        cbor.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_eventbridgev2.types.describe_event_bus_response.DescribeEventBusResponse:
    out: capo_eventbridgev2.types.describe_event_bus_response.DescribeEventBusResponse = capo_eventbridgev2.types.describe_event_bus_response.deserialize_cbor(
        cbor.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_eventbridgev2._auth._signers.Signer | None:
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
            sigv4_config = capo_eventbridgev2._auth._sigv4.build_sigv4_auth_scheme(
                "events", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_eventbridgev2._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_eventbridgev2.types.describe_event_bus_request.DescribeEventBusRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            Endpoint=options.endpoint,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            AccountId=options.account_id,
            EventBusArn=input_.get("event_bus_arn"),
            AccountIdEndpointMode=options.account_id_endpoint_mode,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/service/AWSEventsV2/operation/DescribeEventBus"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["smithy-protocol"] = "rpc-v2-cbor"
    headers["accept"] = "application/cbor"
    body: bytes | None = cbor.dumps(
        capo_eventbridgev2.types.describe_event_bus_request.serialize_cbor(input_)
    )
    headers["content-type"] = "application/cbor"
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


def describe_event_bus(
    options: OperationOptions,
    input_: capo_eventbridgev2.types.describe_event_bus_request.DescribeEventBusRequest,
) -> tuple[
    capo_eventbridgev2.types.describe_event_bus_response.DescribeEventBusResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if (
            response.status != 200
            or response.headers.get("smithy-protocol") != "rpc-v2-cbor"
        ):
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_describe_event_bus(
    options: AsyncOperationOptions,
    input_: capo_eventbridgev2.types.describe_event_bus_request.DescribeEventBusRequest,
) -> tuple[
    capo_eventbridgev2.types.describe_event_bus_response.DescribeEventBusResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if (
            response.status != 200
            or response.headers.get("smithy-protocol") != "rpc-v2-cbor"
        ):
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
