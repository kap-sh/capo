"""Generated from Smithy shape ``com.amazonaws.geomaps#GetStaticMap``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_geo_maps._auth._signers
import capo_geo_maps._auth._sigv4
import capo_geo_maps._protocol.eventstream
import capo_geo_maps.errors.access_denied_exception
import capo_geo_maps.errors.internal_server_exception
import capo_geo_maps.errors.throttling_exception
import capo_geo_maps.errors.validation_exception
import capo_geo_maps.types.color_scheme
import capo_geo_maps.types.get_static_map_request
import capo_geo_maps.types.get_static_map_response
import capo_geo_maps.types.label_size
import capo_geo_maps.types.map_feature_mode
import capo_geo_maps.types.scale_bar_unit
import capo_geo_maps.types.static_map_style
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
        case "AccessDeniedException":
            raise capo_geo_maps.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_geo_maps.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_geo_maps.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_geo_maps.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_geo_maps.types.get_static_map_response.GetStaticMapResponse:
    out: capo_geo_maps.types.get_static_map_response.GetStaticMapResponse = {
        "blob": b"".join(response.iter_raw())
    }  # type: ignore[typeddict-item]
    if "Content-Type" in response.headers:
        out["content_type"] = response.headers["Content-Type"]
    if "Cache-Control" in response.headers:
        out["cache_control"] = response.headers["Cache-Control"]
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    out["pricing_bucket"] = response.headers["x-amz-geo-pricing-bucket"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_geo_maps.types.get_static_map_response.GetStaticMapResponse:
    out: capo_geo_maps.types.get_static_map_response.GetStaticMapResponse = {
        "blob": b"".join([chunk async for chunk in response.async_iter_raw()])
    }  # type: ignore[typeddict-item]
    if "Content-Type" in response.headers:
        out["content_type"] = response.headers["Content-Type"]
    if "Cache-Control" in response.headers:
        out["cache_control"] = response.headers["Cache-Control"]
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    out["pricing_bucket"] = response.headers["x-amz-geo-pricing-bucket"]
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
    input_: capo_geo_maps.types.get_static_map_request.GetStaticMapRequest,
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
    import capo_geo_maps.types.label_size
    import capo_geo_maps.types.map_feature_mode
    import capo_geo_maps.types.scale_bar_unit
    import capo_geo_maps.types.static_map_style

    url = endpoint.url.rstrip("/") + "/v2/static/{FileName}"
    url = url.replace("{FileName}", quote(input_["file_name"], safe=""))
    params: list[tuple[str, str]] = []
    if "bounding_box" in input_:
        params.append(("bounding-box", input_["bounding_box"]))
    if "bounded_positions" in input_:
        params.append(("bounded-positions", input_["bounded_positions"]))
    if "center" in input_:
        params.append(("center", input_["center"]))
    if "color_scheme" in input_:
        params.append(
            (
                "color-scheme",
                capo_geo_maps.types.color_scheme.serialize_json(input_["color_scheme"]),
            )
        )
    if "compact_overlay" in input_:
        params.append(("compact-overlay", input_["compact_overlay"]))
    if "crop_labels" in input_:
        params.append(("crop-labels", "true" if input_["crop_labels"] else "false"))
    if "geo_json_overlay" in input_:
        params.append(("geojson-overlay", input_["geo_json_overlay"]))
    if "height" in input_:
        params.append(("height", str(input_["height"])))
    if "key" in input_:
        params.append(("key", input_["key"]))
    if "label_size" in input_:
        params.append(
            (
                "label-size",
                capo_geo_maps.types.label_size.serialize_json(input_["label_size"]),
            )
        )
    if "language" in input_:
        params.append(("lang", input_["language"]))
    if "padding" in input_:
        params.append(("padding", str(input_["padding"])))
    if "political_view" in input_:
        params.append(("political-view", input_["political_view"]))
    if "points_of_interests" in input_:
        params.append(
            (
                "pois",
                capo_geo_maps.types.map_feature_mode.serialize_json(
                    input_["points_of_interests"]
                ),
            )
        )
    if "radius" in input_:
        params.append(("radius", str(input_["radius"])))
    if "scale_bar_unit" in input_:
        params.append(
            (
                "scale-unit",
                capo_geo_maps.types.scale_bar_unit.serialize_json(
                    input_["scale_bar_unit"]
                ),
            )
        )
    if "style" in input_:
        params.append(
            (
                "style",
                capo_geo_maps.types.static_map_style.serialize_json(input_["style"]),
            )
        )
    if "width" in input_:
        params.append(("width", str(input_["width"])))
    if "zoom" in input_:
        params.append(("zoom", str(input_["zoom"])))
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


def get_static_map(
    options: OperationOptions,
    input_: capo_geo_maps.types.get_static_map_request.GetStaticMapRequest,
) -> tuple[
    capo_geo_maps.types.get_static_map_response.GetStaticMapResponse, zapros.Response
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


async def async_get_static_map(
    options: AsyncOperationOptions,
    input_: capo_geo_maps.types.get_static_map_request.GetStaticMapRequest,
) -> tuple[
    capo_geo_maps.types.get_static_map_response.GetStaticMapResponse, zapros.Response
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
