"""Generated from Smithy shape ``com.amazonaws.route53#UpdateHealthCheck``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_route_53._auth._signers
import capo_route_53._auth._sigv4
import capo_route_53._protocol.eventstream
import capo_route_53.errors.health_check_version_mismatch
import capo_route_53.errors.invalid_input
import capo_route_53.errors.no_such_health_check
import capo_route_53.types.alarm_identifier
import capo_route_53.types.child_health_check_list
import capo_route_53.types.health_check
import capo_route_53.types.health_check_region_list
import capo_route_53.types.insufficient_data_health_status
import capo_route_53.types.resettable_element_name_list
import capo_route_53.types.update_health_check_request
import capo_route_53.types.update_health_check_response
from capo_route_53._protocol.errors import find_error_element, parse_error_metadata
from capo_route_53._protocol.xml import Element, SubElement, fromstring, tostring
from capo_route_53._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_route_53._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_route_53.errors import UnknownServiceError

STATUS_CODE_TO_CODE = {
    400: "InvalidInput",
    404: "NoSuchHealthCheck",
    409: "HealthCheckVersionMismatch",
}


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
        case "HealthCheckVersionMismatch":
            raise capo_route_53.errors.health_check_version_mismatch.HealthCheckVersionMismatch.from_xml(
                error_el, message
            )
        case "InvalidInput":
            raise capo_route_53.errors.invalid_input.InvalidInput.from_xml(
                error_el, message
            )
        case "NoSuchHealthCheck":
            raise capo_route_53.errors.no_such_health_check.NoSuchHealthCheck.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_route_53.types.update_health_check_response.UpdateHealthCheckResponse:
    out: capo_route_53.types.update_health_check_response.UpdateHealthCheckResponse = (
        capo_route_53.types.update_health_check_response.deserialize_xml(
            fromstring(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_route_53.types.update_health_check_response.UpdateHealthCheckResponse:
    out: capo_route_53.types.update_health_check_response.UpdateHealthCheckResponse = (
        capo_route_53.types.update_health_check_response.deserialize_xml(
            fromstring(await response.aread())
        )
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
    input_: capo_route_53.types.update_health_check_request.UpdateHealthCheckRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2013-04-01/healthcheck/{HealthCheckId}"
    url = url.replace("{HealthCheckId}", quote(input_["health_check_id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import capo_route_53.types.alarm_identifier
    import capo_route_53.types.child_health_check_list
    import capo_route_53.types.health_check_region_list
    import capo_route_53.types.insufficient_data_health_status
    import capo_route_53.types.resettable_element_name_list

    root = Element("UpdateHealthCheckRequest")
    if "health_check_version" in input_:
        SubElement(root, "HealthCheckVersion").text = str(
            input_["health_check_version"]
        )
    if "ip_address" in input_:
        SubElement(root, "IPAddress").text = input_["ip_address"]
    if "port" in input_:
        SubElement(root, "Port").text = str(input_["port"])
    if "resource_path" in input_:
        SubElement(root, "ResourcePath").text = input_["resource_path"]
    if "fully_qualified_domain_name" in input_:
        SubElement(root, "FullyQualifiedDomainName").text = input_[
            "fully_qualified_domain_name"
        ]
    if "search_string" in input_:
        SubElement(root, "SearchString").text = input_["search_string"]
    if "failure_threshold" in input_:
        SubElement(root, "FailureThreshold").text = str(input_["failure_threshold"])
    if "inverted" in input_:
        SubElement(root, "Inverted").text = "true" if input_["inverted"] else "false"
    if "disabled" in input_:
        SubElement(root, "Disabled").text = "true" if input_["disabled"] else "false"
    if "health_threshold" in input_:
        SubElement(root, "HealthThreshold").text = str(input_["health_threshold"])
    if "child_health_checks" in input_:
        capo_route_53.types.child_health_check_list.serialize_xml(
            input_["child_health_checks"], root, "ChildHealthChecks"
        )
    if "enable_sni" in input_:
        SubElement(root, "EnableSNI").text = "true" if input_["enable_sni"] else "false"
    if "regions" in input_:
        capo_route_53.types.health_check_region_list.serialize_xml(
            input_["regions"], root, "Regions"
        )
    if "alarm_identifier" in input_:
        capo_route_53.types.alarm_identifier.serialize_xml(
            input_["alarm_identifier"], root, "AlarmIdentifier"
        )
    if "insufficient_data_health_status" in input_:
        capo_route_53.types.insufficient_data_health_status.serialize_xml(
            input_["insufficient_data_health_status"],
            root,
            "InsufficientDataHealthStatus",
        )
    if "reset_elements" in input_:
        capo_route_53.types.resettable_element_name_list.serialize_xml(
            input_["reset_elements"], root, "ResetElements"
        )
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


def update_health_check(
    options: OperationOptions,
    input_: capo_route_53.types.update_health_check_request.UpdateHealthCheckRequest,
) -> tuple[
    capo_route_53.types.update_health_check_response.UpdateHealthCheckResponse,
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


async def async_update_health_check(
    options: AsyncOperationOptions,
    input_: capo_route_53.types.update_health_check_request.UpdateHealthCheckRequest,
) -> tuple[
    capo_route_53.types.update_health_check_response.UpdateHealthCheckResponse,
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
