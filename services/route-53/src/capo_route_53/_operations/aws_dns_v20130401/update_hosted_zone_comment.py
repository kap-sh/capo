"""Generated from Smithy shape ``com.amazonaws.route53#UpdateHostedZoneComment``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_route_53._auth._signers
import capo_route_53._auth._sigv4
import capo_route_53._protocol.eventstream
import capo_route_53.errors.invalid_input
import capo_route_53.errors.no_such_hosted_zone
import capo_route_53.errors.prior_request_not_complete
import capo_route_53.types.hosted_zone
import capo_route_53.types.update_hosted_zone_comment_request
import capo_route_53.types.update_hosted_zone_comment_response
from capo_route_53._protocol.errors import find_error_element, parse_error_metadata
from capo_route_53._protocol.xml import Element, SubElement, fromstring, tostring
from capo_route_53._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_route_53._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_route_53.errors import UnknownServiceError

STATUS_CODE_TO_CODE = {404: "NoSuchHostedZone"}


def handle_error(response: zapros.Response) -> Never:
    body = response.read()
    if body:
        root = fromstring(body)
        code, message = parse_error_metadata(root)
        error_el = find_error_element(root)
    else:
        code = STATUS_CODE_TO_CODE.get(response.status)
        message = None
        error_el = Element("Error")
    match code:
        case "InvalidInput":
            raise capo_route_53.errors.invalid_input.InvalidInput.from_xml(
                error_el, message
            )
        case "NoSuchHostedZone":
            raise capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone.from_xml(
                error_el, message
            )
        case "PriorRequestNotComplete":
            raise capo_route_53.errors.prior_request_not_complete.PriorRequestNotComplete.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_route_53.types.update_hosted_zone_comment_response.UpdateHostedZoneCommentResponse:
    out: capo_route_53.types.update_hosted_zone_comment_response.UpdateHostedZoneCommentResponse = capo_route_53.types.update_hosted_zone_comment_response.deserialize_xml(
        fromstring(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_route_53.types.update_hosted_zone_comment_response.UpdateHostedZoneCommentResponse:
    out: capo_route_53.types.update_hosted_zone_comment_response.UpdateHostedZoneCommentResponse = capo_route_53.types.update_hosted_zone_comment_response.deserialize_xml(
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
    input_: capo_route_53.types.update_hosted_zone_comment_request.UpdateHostedZoneCommentRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2013-04-01/hostedzone/{Id}"
    url = url.replace("{Id}", quote(input_["id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    root = Element("UpdateHostedZoneCommentRequest")
    if "comment" in input_:
        SubElement(root, "Comment").text = input_["comment"]
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
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


def update_hosted_zone_comment(
    options: OperationOptions,
    input_: capo_route_53.types.update_hosted_zone_comment_request.UpdateHostedZoneCommentRequest,
) -> tuple[
    capo_route_53.types.update_hosted_zone_comment_response.UpdateHostedZoneCommentResponse,
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


async def async_update_hosted_zone_comment(
    options: AsyncOperationOptions,
    input_: capo_route_53.types.update_hosted_zone_comment_request.UpdateHostedZoneCommentRequest,
) -> tuple[
    capo_route_53.types.update_hosted_zone_comment_response.UpdateHostedZoneCommentResponse,
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
