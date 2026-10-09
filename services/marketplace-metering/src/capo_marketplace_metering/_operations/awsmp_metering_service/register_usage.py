"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#RegisterUsage``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_marketplace_metering._auth._signers
import capo_marketplace_metering._auth._sigv4
import capo_marketplace_metering._protocol.eventstream
import capo_marketplace_metering.errors.customer_not_entitled_exception
import capo_marketplace_metering.errors.disabled_api_exception
import capo_marketplace_metering.errors.internal_service_error_exception
import capo_marketplace_metering.errors.invalid_product_code_exception
import capo_marketplace_metering.errors.invalid_public_key_version_exception
import capo_marketplace_metering.errors.invalid_region_exception
import capo_marketplace_metering.errors.platform_not_supported_exception
import capo_marketplace_metering.errors.throttling_exception
import capo_marketplace_metering.types.register_usage_request
import capo_marketplace_metering.types.register_usage_result
import capo_marketplace_metering.types.timestamp
from capo_marketplace_metering._protocol.errors import parse_error_metadata_json
from capo_marketplace_metering._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_marketplace_metering._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_marketplace_metering.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CustomerNotEntitledException":
            raise capo_marketplace_metering.errors.customer_not_entitled_exception.CustomerNotEntitledException.from_aws_json_1_1(
                data, message
            )
        case "DisabledApiException":
            raise capo_marketplace_metering.errors.disabled_api_exception.DisabledApiException.from_aws_json_1_1(
                data, message
            )
        case "InternalServiceErrorException":
            raise capo_marketplace_metering.errors.internal_service_error_exception.InternalServiceErrorException.from_aws_json_1_1(
                data, message
            )
        case "InvalidProductCodeException":
            raise capo_marketplace_metering.errors.invalid_product_code_exception.InvalidProductCodeException.from_aws_json_1_1(
                data, message
            )
        case "InvalidPublicKeyVersionException":
            raise capo_marketplace_metering.errors.invalid_public_key_version_exception.InvalidPublicKeyVersionException.from_aws_json_1_1(
                data, message
            )
        case "InvalidRegionException":
            raise capo_marketplace_metering.errors.invalid_region_exception.InvalidRegionException.from_aws_json_1_1(
                data, message
            )
        case "PlatformNotSupportedException":
            raise capo_marketplace_metering.errors.platform_not_supported_exception.PlatformNotSupportedException.from_aws_json_1_1(
                data, message
            )
        case "ThrottlingException":
            raise capo_marketplace_metering.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_marketplace_metering.types.register_usage_result.RegisterUsageResult:
    out: capo_marketplace_metering.types.register_usage_result.RegisterUsageResult = (
        capo_marketplace_metering.types.register_usage_result.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_marketplace_metering.types.register_usage_result.RegisterUsageResult:
    out: capo_marketplace_metering.types.register_usage_result.RegisterUsageResult = (
        capo_marketplace_metering.types.register_usage_result.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_marketplace_metering._auth._signers.Signer | None:
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
            sigv4_config = (
                capo_marketplace_metering._auth._sigv4.build_sigv4_auth_scheme(
                    "aws-marketplace", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_marketplace_metering._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_marketplace_metering.types.register_usage_request.RegisterUsageRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSMPMeteringService.RegisterUsage"
    body: bytes | None = json.dumps(
        capo_marketplace_metering.types.register_usage_request.serialize_aws_json_1_1(
            input_
        ),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
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


def register_usage(
    options: OperationOptions,
    input_: capo_marketplace_metering.types.register_usage_request.RegisterUsageRequest,
) -> tuple[
    capo_marketplace_metering.types.register_usage_result.RegisterUsageResult,
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


async def async_register_usage(
    options: AsyncOperationOptions,
    input_: capo_marketplace_metering.types.register_usage_request.RegisterUsageRequest,
) -> tuple[
    capo_marketplace_metering.types.register_usage_result.RegisterUsageResult,
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
