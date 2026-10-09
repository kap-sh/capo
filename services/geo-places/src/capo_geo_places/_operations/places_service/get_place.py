"""Generated from Smithy shape ``com.amazonaws.geoplaces#GetPlace``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_geo_places._auth._signers
import capo_geo_places._auth._sigv4
import capo_geo_places._protocol.eventstream
import capo_geo_places.errors.access_denied_exception
import capo_geo_places.errors.internal_server_exception
import capo_geo_places.errors.throttling_exception
import capo_geo_places.errors.validation_exception
import capo_geo_places.types.access_point_list
import capo_geo_places.types.access_restriction_list
import capo_geo_places.types.address
import capo_geo_places.types.bounding_box
import capo_geo_places.types.business_chain_list
import capo_geo_places.types.category_list
import capo_geo_places.types.contacts
import capo_geo_places.types.cross_reference_list
import capo_geo_places.types.food_type_list
import capo_geo_places.types.get_place_additional_feature_list
import capo_geo_places.types.get_place_address_names_mode
import capo_geo_places.types.get_place_intended_use
import capo_geo_places.types.get_place_request
import capo_geo_places.types.get_place_response
import capo_geo_places.types.opening_hours_list
import capo_geo_places.types.phoneme_details
import capo_geo_places.types.place_attribute_list
import capo_geo_places.types.place_type
import capo_geo_places.types.position
import capo_geo_places.types.postal_code_details_list
import capo_geo_places.types.related_place
import capo_geo_places.types.related_place_list
import capo_geo_places.types.time_zone
from capo_geo_places._protocol.errors import parse_error_metadata_json
from capo_geo_places._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_geo_places._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_geo_places.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_geo_places.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_geo_places.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_geo_places.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_geo_places.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_geo_places.types.get_place_response.GetPlaceResponse:
    out: capo_geo_places.types.get_place_response.GetPlaceResponse = (
        capo_geo_places.types.get_place_response.deserialize_json(
            json.loads(response.read())
        )
    )
    out["pricing_bucket"] = response.headers["x-amz-geo-pricing-bucket"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_geo_places.types.get_place_response.GetPlaceResponse:
    out: capo_geo_places.types.get_place_response.GetPlaceResponse = (
        capo_geo_places.types.get_place_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    out["pricing_bucket"] = response.headers["x-amz-geo-pricing-bucket"]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_geo_places._auth._signers.Signer | None:
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
            sigv4_config = capo_geo_places._auth._sigv4.build_sigv4_auth_scheme(
                "geo-places", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_geo_places._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_geo_places.types.get_place_request.GetPlaceRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    import capo_geo_places.types.get_place_additional_feature
    import capo_geo_places.types.get_place_address_names_mode
    import capo_geo_places.types.get_place_intended_use

    url = endpoint.url.rstrip("/") + "/v2/place/{PlaceId}"
    url = url.replace("{PlaceId}", quote(input_["place_id"], safe=""))
    params: list[tuple[str, str]] = []
    if "additional_features" in input_:
        for item in input_["additional_features"]:
            params.append(
                (
                    "additional-features",
                    capo_geo_places.types.get_place_additional_feature.serialize_json(
                        item
                    ),
                )
            )
    if "language" in input_:
        params.append(("language", input_["language"]))
    if "political_view" in input_:
        params.append(("political-view", input_["political_view"]))
    if "intended_use" in input_:
        params.append(
            (
                "intended-use",
                capo_geo_places.types.get_place_intended_use.serialize_json(
                    input_["intended_use"]
                ),
            )
        )
    if "key" in input_:
        params.append(("key", input_["key"]))
    if "address_names_mode" in input_:
        params.append(
            (
                "address-names-mode",
                capo_geo_places.types.get_place_address_names_mode.serialize_json(
                    input_["address_names_mode"]
                ),
            )
        )
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


def get_place(
    options: OperationOptions,
    input_: capo_geo_places.types.get_place_request.GetPlaceRequest,
) -> tuple[capo_geo_places.types.get_place_response.GetPlaceResponse, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_get_place(
    options: AsyncOperationOptions,
    input_: capo_geo_places.types.get_place_request.GetPlaceRequest,
) -> tuple[capo_geo_places.types.get_place_response.GetPlaceResponse, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
