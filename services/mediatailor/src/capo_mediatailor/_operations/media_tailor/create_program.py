"""Generated from Smithy shape ``com.amazonaws.mediatailor#CreateProgram``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_mediatailor._auth._signers
import capo_mediatailor._auth._sigv4
import capo_mediatailor._protocol.eventstream
import capo_mediatailor.types.__list_of_ad_break
import capo_mediatailor.types.__list_of_audience_media
import capo_mediatailor.types.__map_of__string
import capo_mediatailor.types.__timestamp_unix
import capo_mediatailor.types.clip_range
import capo_mediatailor.types.create_program_request
import capo_mediatailor.types.create_program_response
import capo_mediatailor.types.schedule_configuration
from capo_mediatailor._protocol.errors import parse_error_metadata_json
from capo_mediatailor._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_mediatailor._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_mediatailor.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_mediatailor.types.create_program_response.CreateProgramResponse:
    out: capo_mediatailor.types.create_program_response.CreateProgramResponse = (
        capo_mediatailor.types.create_program_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_mediatailor.types.create_program_response.CreateProgramResponse:
    out: capo_mediatailor.types.create_program_response.CreateProgramResponse = (
        capo_mediatailor.types.create_program_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_mediatailor._auth._signers.Signer | None:
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
            sigv4_config = capo_mediatailor._auth._sigv4.build_sigv4_auth_scheme(
                "mediatailor", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_mediatailor._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_mediatailor.types.create_program_request.CreateProgramRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/channel/{ChannelName}/program/{ProgramName}"
    url = url.replace("{ChannelName}", quote(input_["channel_name"], safe=""))
    url = url.replace("{ProgramName}", quote(input_["program_name"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_mediatailor.types.create_program_request.serialize_json(input_),
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


def create_program(
    options: OperationOptions,
    input_: capo_mediatailor.types.create_program_request.CreateProgramRequest,
) -> tuple[
    capo_mediatailor.types.create_program_response.CreateProgramResponse,
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


async def async_create_program(
    options: AsyncOperationOptions,
    input_: capo_mediatailor.types.create_program_request.CreateProgramRequest,
) -> tuple[
    capo_mediatailor.types.create_program_response.CreateProgramResponse,
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
