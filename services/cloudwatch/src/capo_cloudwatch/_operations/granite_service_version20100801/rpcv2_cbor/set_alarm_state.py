"""Generated from Smithy shape ``com.amazonaws.cloudwatch#SetAlarmState``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudwatch._auth._signers
import capo_cloudwatch._auth._sigv4
import capo_cloudwatch._protocol.eventstream
import capo_cloudwatch.errors.invalid_format_fault
import capo_cloudwatch.errors.resource_not_found
import capo_cloudwatch.types.set_alarm_state_input
import capo_cloudwatch.types.state_value
from capo_cloudwatch._protocol import cbor
from capo_cloudwatch._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudwatch._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cloudwatch.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data, code, message = cbor.parse_error(response)
    match code:
        case "InvalidFormatFault":
            raise capo_cloudwatch.errors.invalid_format_fault.InvalidFormatFault.from_cbor(
                data, message, response=response
            )
        case "ResourceNotFound":
            raise capo_cloudwatch.errors.resource_not_found.ResourceNotFound.from_cbor(
                data, message, response=response
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudwatch._auth._signers.Signer | None:
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
            sigv4_config = capo_cloudwatch._auth._sigv4.build_sigv4_auth_scheme(
                "monitoring", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_cloudwatch._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudwatch.types.set_alarm_state_input.SetAlarmStateInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/service/GraniteServiceVersion20100801/operation/SetAlarmState"
    )
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["smithy-protocol"] = "rpc-v2-cbor"
    headers["accept"] = "application/cbor"
    body: bytes | None = cbor.dumps(
        capo_cloudwatch.types.set_alarm_state_input.serialize_cbor(input_)
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


def set_alarm_state(
    options: OperationOptions,
    input_: capo_cloudwatch.types.set_alarm_state_input.SetAlarmStateInput,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if (
            response.status != 200
            or response.headers.get("smithy-protocol") != "rpc-v2-cbor"
        ):
            response.read()
            raise_error(response, handle_error)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_set_alarm_state(
    options: AsyncOperationOptions,
    input_: capo_cloudwatch.types.set_alarm_state_input.SetAlarmStateInput,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if (
            response.status != 200
            or response.headers.get("smithy-protocol") != "rpc-v2-cbor"
        ):
            await response.aread()
            raise_error(response, handle_error)
        return None, response
    except BaseException:
        await response.aclose()
        raise
