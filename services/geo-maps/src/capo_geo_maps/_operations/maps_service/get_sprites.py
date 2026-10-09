"""Generated from Smithy shape ``com.amazonaws.geomaps#GetSprites``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_geo_maps._auth._signers
import capo_geo_maps._auth._sigv4
import capo_geo_maps._protocol.eventstream
import capo_geo_maps.types.color_scheme
import capo_geo_maps.types.get_sprites_request
import capo_geo_maps.types.get_sprites_response
import capo_geo_maps.types.map_style
import capo_geo_maps.types.variant
from capo_geo_maps._protocol.errors import parse_error_metadata_json
from capo_geo_maps._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_geo_maps._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_geo_maps.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_geo_maps.types.get_sprites_response.GetSpritesResponse:
    out: capo_geo_maps.types.get_sprites_response.GetSpritesResponse = {
        "blob": b"".join(response.iter_raw())
    }  # type: ignore[typeddict-item]
    if "Content-Type" in response.headers:
        out["content_type"] = response.headers["Content-Type"]
    if "Cache-Control" in response.headers:
        out["cache_control"] = response.headers["Cache-Control"]
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_geo_maps.types.get_sprites_response.GetSpritesResponse:
    out: capo_geo_maps.types.get_sprites_response.GetSpritesResponse = {
        "blob": b"".join([chunk async for chunk in response.async_iter_raw()])
    }  # type: ignore[typeddict-item]
    if "Content-Type" in response.headers:
        out["content_type"] = response.headers["Content-Type"]
    if "Cache-Control" in response.headers:
        out["cache_control"] = response.headers["Cache-Control"]
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_geo_maps._auth._signers.Signer | None:
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
            sigv4_config = capo_geo_maps._auth._sigv4.build_sigv4_auth_scheme(
                "geo-maps", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_geo_maps._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_geo_maps.types.get_sprites_request.GetSpritesRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    import capo_geo_maps.types.color_scheme
    import capo_geo_maps.types.map_style
    import capo_geo_maps.types.variant

    url = (
        endpoint.url.rstrip("/")
        + "/v2/styles/{Style}/{ColorScheme}/{Variant}/sprites/{FileName}"
    )
    url = url.replace("{FileName}", quote(input_["file_name"], safe=""))
    url = url.replace(
        "{Style}",
        quote(capo_geo_maps.types.map_style.serialize_json(input_["style"]), safe=""),
    )
    url = url.replace(
        "{ColorScheme}",
        quote(
            capo_geo_maps.types.color_scheme.serialize_json(input_["color_scheme"]),
            safe="",
        ),
    )
    url = url.replace(
        "{Variant}",
        quote(capo_geo_maps.types.variant.serialize_json(input_["variant"]), safe=""),
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


def get_sprites(
    options: OperationOptions,
    input_: capo_geo_maps.types.get_sprites_request.GetSpritesRequest,
) -> tuple[
    capo_geo_maps.types.get_sprites_response.GetSpritesResponse, zapros.Response
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


async def async_get_sprites(
    options: AsyncOperationOptions,
    input_: capo_geo_maps.types.get_sprites_request.GetSpritesRequest,
) -> tuple[
    capo_geo_maps.types.get_sprites_response.GetSpritesResponse, zapros.Response
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
