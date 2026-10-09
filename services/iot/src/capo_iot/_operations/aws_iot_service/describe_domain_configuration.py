"""Generated from Smithy shape ``com.amazonaws.iot#DescribeDomainConfiguration``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_iot._auth._signers
import capo_iot._auth._sigv4
import capo_iot._protocol.eventstream
import capo_iot.errors.internal_failure_exception
import capo_iot.errors.invalid_request_exception
import capo_iot.errors.resource_not_found_exception
import capo_iot.errors.service_unavailable_exception
import capo_iot.errors.throttling_exception
import capo_iot.errors.unauthorized_exception
import capo_iot.types.application_protocol
import capo_iot.types.authentication_type
import capo_iot.types.authorizer_config
import capo_iot.types.client_certificate_config
import capo_iot.types.date_type
import capo_iot.types.describe_domain_configuration_request
import capo_iot.types.describe_domain_configuration_response
import capo_iot.types.domain_configuration_status
import capo_iot.types.domain_type
import capo_iot.types.server_certificate_config
import capo_iot.types.server_certificates
import capo_iot.types.service_type
import capo_iot.types.tls_config
from capo_iot._protocol.errors import parse_error_metadata_json
from capo_iot._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_iot._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_iot.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalFailureException":
            raise capo_iot.errors.internal_failure_exception.InternalFailureException.from_json(
                data, message
            )
        case "InvalidRequestException":
            raise capo_iot.errors.invalid_request_exception.InvalidRequestException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_iot.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ServiceUnavailableException":
            raise capo_iot.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_iot.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "UnauthorizedException":
            raise capo_iot.errors.unauthorized_exception.UnauthorizedException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_iot.types.describe_domain_configuration_response.DescribeDomainConfigurationResponse:
    out: capo_iot.types.describe_domain_configuration_response.DescribeDomainConfigurationResponse = capo_iot.types.describe_domain_configuration_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_iot.types.describe_domain_configuration_response.DescribeDomainConfigurationResponse:
    out: capo_iot.types.describe_domain_configuration_response.DescribeDomainConfigurationResponse = capo_iot.types.describe_domain_configuration_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_iot._auth._signers.Signer | None:
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
            sigv4_config = capo_iot._auth._sigv4.build_sigv4_auth_scheme(
                "iot", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_iot._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_iot.types.describe_domain_configuration_request.DescribeDomainConfigurationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/domainConfigurations/{domainConfigurationName}"
    url = url.replace(
        "{domainConfigurationName}", quote(input_["domain_configuration_name"], safe="")
    )
    params: list[tuple[str, str]] = []
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


def describe_domain_configuration(
    options: OperationOptions,
    input_: capo_iot.types.describe_domain_configuration_request.DescribeDomainConfigurationRequest,
) -> tuple[
    capo_iot.types.describe_domain_configuration_response.DescribeDomainConfigurationResponse,
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


async def async_describe_domain_configuration(
    options: AsyncOperationOptions,
    input_: capo_iot.types.describe_domain_configuration_request.DescribeDomainConfigurationRequest,
) -> tuple[
    capo_iot.types.describe_domain_configuration_response.DescribeDomainConfigurationResponse,
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
