"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#CreateIngestConfiguration``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_ivs_realtime._auth._signers
import capo_ivs_realtime._auth._sigv4
import capo_ivs_realtime._protocol.eventstream
import capo_ivs_realtime.errors.access_denied_exception
import capo_ivs_realtime.errors.pending_verification
import capo_ivs_realtime.errors.service_quota_exceeded_exception
import capo_ivs_realtime.errors.validation_exception
import capo_ivs_realtime.types.create_ingest_configuration_request
import capo_ivs_realtime.types.create_ingest_configuration_response
import capo_ivs_realtime.types.ingest_configuration
import capo_ivs_realtime.types.ingest_protocol
import capo_ivs_realtime.types.participant_attributes
import capo_ivs_realtime.types.tags
from capo_ivs_realtime._protocol.errors import parse_error_metadata_json
from capo_ivs_realtime._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_ivs_realtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_ivs_realtime.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "PendingVerification":
            raise capo_ivs_realtime.errors.pending_verification.PendingVerification.from_json(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_ivs_realtime.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_ivs_realtime.types.create_ingest_configuration_response.CreateIngestConfigurationResponse:
    out: capo_ivs_realtime.types.create_ingest_configuration_response.CreateIngestConfigurationResponse = capo_ivs_realtime.types.create_ingest_configuration_response.deserialize_json(
        json.loads(response.read())
    )
    if "Access-Control-Allow-Origin" in response.headers:
        out["access_control_allow_origin"] = response.headers[
            "Access-Control-Allow-Origin"
        ]
    if "Access-Control-Expose-Headers" in response.headers:
        out["access_control_expose_headers"] = response.headers[
            "Access-Control-Expose-Headers"
        ]
    if "Cache-Control" in response.headers:
        out["cache_control"] = response.headers["Cache-Control"]
    if "Content-Security-Policy" in response.headers:
        out["content_security_policy"] = response.headers["Content-Security-Policy"]
    if "Strict-Transport-Security" in response.headers:
        out["strict_transport_security"] = response.headers["Strict-Transport-Security"]
    if "X-Content-Type-Options" in response.headers:
        out["x_content_type_options"] = response.headers["X-Content-Type-Options"]
    if "X-Frame-Options" in response.headers:
        out["x_frame_options"] = response.headers["X-Frame-Options"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_ivs_realtime.types.create_ingest_configuration_response.CreateIngestConfigurationResponse:
    out: capo_ivs_realtime.types.create_ingest_configuration_response.CreateIngestConfigurationResponse = capo_ivs_realtime.types.create_ingest_configuration_response.deserialize_json(
        json.loads(await response.aread())
    )
    if "Access-Control-Allow-Origin" in response.headers:
        out["access_control_allow_origin"] = response.headers[
            "Access-Control-Allow-Origin"
        ]
    if "Access-Control-Expose-Headers" in response.headers:
        out["access_control_expose_headers"] = response.headers[
            "Access-Control-Expose-Headers"
        ]
    if "Cache-Control" in response.headers:
        out["cache_control"] = response.headers["Cache-Control"]
    if "Content-Security-Policy" in response.headers:
        out["content_security_policy"] = response.headers["Content-Security-Policy"]
    if "Strict-Transport-Security" in response.headers:
        out["strict_transport_security"] = response.headers["Strict-Transport-Security"]
    if "X-Content-Type-Options" in response.headers:
        out["x_content_type_options"] = response.headers["X-Content-Type-Options"]
    if "X-Frame-Options" in response.headers:
        out["x_frame_options"] = response.headers["X-Frame-Options"]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_ivs_realtime._auth._signers.Signer | None:
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
            sigv4_config = capo_ivs_realtime._auth._sigv4.build_sigv4_auth_scheme(
                "ivs", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_ivs_realtime._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_ivs_realtime.types.create_ingest_configuration_request.CreateIngestConfigurationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/CreateIngestConfiguration"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_ivs_realtime.types.create_ingest_configuration_request.serialize_json(
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
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_ingest_configuration(
    options: OperationOptions,
    input_: capo_ivs_realtime.types.create_ingest_configuration_request.CreateIngestConfigurationRequest,
) -> tuple[
    capo_ivs_realtime.types.create_ingest_configuration_response.CreateIngestConfigurationResponse,
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


async def async_create_ingest_configuration(
    options: AsyncOperationOptions,
    input_: capo_ivs_realtime.types.create_ingest_configuration_request.CreateIngestConfigurationRequest,
) -> tuple[
    capo_ivs_realtime.types.create_ingest_configuration_response.CreateIngestConfigurationResponse,
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
