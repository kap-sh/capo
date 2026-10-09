"""Generated from Smithy shape ``com.amazonaws.route53#ListHostedZonesByVPC``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_route_53._auth._signers
import capo_route_53._auth._sigv4
import capo_route_53._protocol.eventstream
import capo_route_53.errors.invalid_input
import capo_route_53.errors.invalid_pagination_token
import capo_route_53.types.hosted_zone_summaries
import capo_route_53.types.list_hosted_zones_by_vpc_request
import capo_route_53.types.list_hosted_zones_by_vpc_response
import capo_route_53.types.vpc_region
from capo_route_53._protocol.errors import find_error_element, parse_error_metadata
from capo_route_53._protocol.xml import fromstring
from capo_route_53._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_route_53._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_route_53.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    body = response.read()
    if not body:
        raise UnknownServiceError(code=None, message=None, response=response)
    root = fromstring(body)
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "InvalidInput":
            raise capo_route_53.errors.invalid_input.InvalidInput.from_xml(
                error_el, message
            )
        case "InvalidPaginationToken":
            raise capo_route_53.errors.invalid_pagination_token.InvalidPaginationToken.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_route_53.types.list_hosted_zones_by_vpc_response.ListHostedZonesByVPCResponse:
    out: capo_route_53.types.list_hosted_zones_by_vpc_response.ListHostedZonesByVPCResponse = capo_route_53.types.list_hosted_zones_by_vpc_response.deserialize_xml(
        fromstring(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_route_53.types.list_hosted_zones_by_vpc_response.ListHostedZonesByVPCResponse:
    out: capo_route_53.types.list_hosted_zones_by_vpc_response.ListHostedZonesByVPCResponse = capo_route_53.types.list_hosted_zones_by_vpc_response.deserialize_xml(
        fromstring(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_route_53._auth._signers.Signer | None:
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
            sigv4_config = capo_route_53._auth._sigv4.build_sigv4_auth_scheme(
                "route53", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_route_53._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_route_53.types.list_hosted_zones_by_vpc_request.ListHostedZonesByVPCRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    import capo_route_53.types.vpc_region

    url = endpoint.url.rstrip("/") + "/2013-04-01/hostedzonesbyvpc"
    params: list[tuple[str, str]] = []
    if "vpc_id" in input_:
        params.append(("vpcid", input_["vpc_id"]))
    if "vpc_region" in input_:
        params.append(
            (
                "vpcregion",
                capo_route_53.types.vpc_region.to_xml_text(input_["vpc_region"]),
            )
        )
    if "max_items" in input_:
        params.append(("maxitems", str(input_["max_items"])))
    if "next_token" in input_:
        params.append(("nexttoken", input_["next_token"]))
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


def list_hosted_zones_by_vpc(
    options: OperationOptions,
    input_: capo_route_53.types.list_hosted_zones_by_vpc_request.ListHostedZonesByVPCRequest,
) -> tuple[
    capo_route_53.types.list_hosted_zones_by_vpc_response.ListHostedZonesByVPCResponse,
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


async def async_list_hosted_zones_by_vpc(
    options: AsyncOperationOptions,
    input_: capo_route_53.types.list_hosted_zones_by_vpc_request.ListHostedZonesByVPCRequest,
) -> tuple[
    capo_route_53.types.list_hosted_zones_by_vpc_response.ListHostedZonesByVPCResponse,
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
