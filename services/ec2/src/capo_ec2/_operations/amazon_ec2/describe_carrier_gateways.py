"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCarrierGateways``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_ec2._auth._signers
import capo_ec2._auth._sigv4
import capo_ec2._protocol.eventstream
import capo_ec2.types.carrier_gateway_id_set
import capo_ec2.types.carrier_gateway_set
import capo_ec2.types.describe_carrier_gateways_request
import capo_ec2.types.describe_carrier_gateways_result
import capo_ec2.types.filter_list
from capo_ec2._protocol.errors import parse_error_metadata
from capo_ec2._protocol.xml import fromstring
from capo_ec2._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_ec2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_ec2.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_ec2.types.describe_carrier_gateways_result.DescribeCarrierGatewaysResult:
    out: capo_ec2.types.describe_carrier_gateways_result.DescribeCarrierGatewaysResult = capo_ec2.types.describe_carrier_gateways_result.deserialize_ec2_query(
        fromstring(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_ec2.types.describe_carrier_gateways_result.DescribeCarrierGatewaysResult:
    out: capo_ec2.types.describe_carrier_gateways_result.DescribeCarrierGatewaysResult = capo_ec2.types.describe_carrier_gateways_result.deserialize_ec2_query(
        fromstring(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_ec2._auth._signers.Signer | None:
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
            sigv4_config = capo_ec2._auth._sigv4.build_sigv4_auth_scheme(
                "ec2", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_ec2._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_ec2.types.describe_carrier_gateways_request.DescribeCarrierGatewaysRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "DescribeCarrierGateways"))
    pairs.append(("Version", "2016-11-15"))
    capo_ec2.types.describe_carrier_gateways_request.serialize_ec2_query(
        input_, pairs, ""
    )
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
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


def describe_carrier_gateways(
    options: OperationOptions,
    input_: capo_ec2.types.describe_carrier_gateways_request.DescribeCarrierGatewaysRequest,
) -> tuple[
    capo_ec2.types.describe_carrier_gateways_result.DescribeCarrierGatewaysResult,
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


async def async_describe_carrier_gateways(
    options: AsyncOperationOptions,
    input_: capo_ec2.types.describe_carrier_gateways_request.DescribeCarrierGatewaysRequest,
) -> tuple[
    capo_ec2.types.describe_carrier_gateways_result.DescribeCarrierGatewaysResult,
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
