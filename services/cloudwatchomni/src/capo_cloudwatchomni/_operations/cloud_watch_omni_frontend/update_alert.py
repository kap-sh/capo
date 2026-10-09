"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#UpdateAlert``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudwatchomni._auth._signers
import capo_cloudwatchomni._auth._sigv4
import capo_cloudwatchomni._protocol.eventstream
import capo_cloudwatchomni.errors.access_denied_exception
import capo_cloudwatchomni.errors.conflict_exception
import capo_cloudwatchomni.errors.internal_server_exception
import capo_cloudwatchomni.errors.resource_not_found_exception
import capo_cloudwatchomni.errors.throttling_exception
import capo_cloudwatchomni.errors.validation_exception
import capo_cloudwatchomni.types.notification_rule_list
import capo_cloudwatchomni.types.rule
import capo_cloudwatchomni.types.update_alert_input
import capo_cloudwatchomni.types.update_alert_output
from capo_cloudwatchomni._protocol import cbor
from capo_cloudwatchomni._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudwatchomni._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cloudwatchomni.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data, code, message = cbor.parse_error(response)
    match code:
        case "AccessDeniedException":
            raise capo_cloudwatchomni.errors.access_denied_exception.AccessDeniedException.from_cbor(
                data, message
            )
        case "ConflictException":
            raise capo_cloudwatchomni.errors.conflict_exception.ConflictException.from_cbor(
                data, message
            )
        case "InternalServerException":
            raise capo_cloudwatchomni.errors.internal_server_exception.InternalServerException.from_cbor(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_cloudwatchomni.errors.resource_not_found_exception.ResourceNotFoundException.from_cbor(
                data, message
            )
        case "ThrottlingException":
            raise capo_cloudwatchomni.errors.throttling_exception.ThrottlingException.from_cbor(
                data, message
            )
        case "ValidationException":
            raise capo_cloudwatchomni.errors.validation_exception.ValidationException.from_cbor(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudwatchomni.types.update_alert_output.UpdateAlertOutput:
    out: capo_cloudwatchomni.types.update_alert_output.UpdateAlertOutput = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudwatchomni.types.update_alert_output.UpdateAlertOutput:
    out: capo_cloudwatchomni.types.update_alert_output.UpdateAlertOutput = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudwatchomni._auth._signers.Signer | None:
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
            sigv4_config = capo_cloudwatchomni._auth._sigv4.build_sigv4_auth_scheme(
                "cloudwatch", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_cloudwatchomni._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudwatchomni.types.update_alert_input.UpdateAlertInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/service/CloudWatchOmniFrontend/operation/UpdateAlert"
    )
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["smithy-protocol"] = "rpc-v2-cbor"
    headers["accept"] = "application/cbor"
    body: bytes | None = cbor.dumps(
        capo_cloudwatchomni.types.update_alert_input.serialize_cbor(input_)
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


def update_alert(
    options: OperationOptions,
    input_: capo_cloudwatchomni.types.update_alert_input.UpdateAlertInput,
) -> tuple[
    capo_cloudwatchomni.types.update_alert_output.UpdateAlertOutput, zapros.Response
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


async def async_update_alert(
    options: AsyncOperationOptions,
    input_: capo_cloudwatchomni.types.update_alert_input.UpdateAlertInput,
) -> tuple[
    capo_cloudwatchomni.types.update_alert_output.UpdateAlertOutput, zapros.Response
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
