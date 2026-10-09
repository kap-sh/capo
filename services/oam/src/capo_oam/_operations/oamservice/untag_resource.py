"""Generated from Smithy shape ``com.amazonaws.oam#UntagResource``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_oam._auth._signers
import capo_oam._auth._sigv4
import capo_oam._protocol.eventstream
import capo_oam.errors.resource_not_found_exception
import capo_oam.errors.validation_exception
import capo_oam.types.tag_keys
import capo_oam.types.untag_resource_input
import capo_oam.types.untag_resource_output
from capo_oam._protocol.errors import parse_error_metadata_json
from capo_oam._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_oam._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_oam.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ResourceNotFoundException":
            raise capo_oam.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_oam.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_oam.types.untag_resource_output.UntagResourceOutput:
    out: capo_oam.types.untag_resource_output.UntagResourceOutput = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_oam.types.untag_resource_output.UntagResourceOutput:
    out: capo_oam.types.untag_resource_output.UntagResourceOutput = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_oam._auth._signers.Signer | None:
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
            sigv4_config = capo_oam._auth._sigv4.build_sigv4_auth_scheme(
                "oam", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_oam._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_oam.types.untag_resource_input.UntagResourceInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/tags/{ResourceArn}"
    url = url.replace("{ResourceArn}", quote(input_["resource_arn"], safe=""))
    params: list[tuple[str, str]] = []
    for item in input_["tag_keys"]:
        params.append(("tagKeys", item))
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
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def untag_resource(
    options: OperationOptions,
    input_: capo_oam.types.untag_resource_input.UntagResourceInput,
) -> tuple[capo_oam.types.untag_resource_output.UntagResourceOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_untag_resource(
    options: AsyncOperationOptions,
    input_: capo_oam.types.untag_resource_input.UntagResourceInput,
) -> tuple[capo_oam.types.untag_resource_output.UntagResourceOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
