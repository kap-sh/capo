"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetInterpolatedAssetPropertyValues``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_iotsitewise._auth._signers
import capo_iotsitewise._auth._sigv4
import capo_iotsitewise._protocol.eventstream
import capo_iotsitewise.errors.internal_failure_exception
import capo_iotsitewise.errors.invalid_request_exception
import capo_iotsitewise.errors.resource_not_found_exception
import capo_iotsitewise.errors.service_unavailable_exception
import capo_iotsitewise.errors.throttling_exception
import capo_iotsitewise.types.get_interpolated_asset_property_values_request
import capo_iotsitewise.types.get_interpolated_asset_property_values_response
import capo_iotsitewise.types.interpolated_asset_property_values
import capo_iotsitewise.types.quality
from capo_iotsitewise._protocol.errors import parse_error_metadata_json
from capo_iotsitewise._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_iotsitewise._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_iotsitewise.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalFailureException":
            raise capo_iotsitewise.errors.internal_failure_exception.InternalFailureException.from_json(
                data, message
            )
        case "InvalidRequestException":
            raise capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ServiceUnavailableException":
            raise capo_iotsitewise.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_iotsitewise.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_iotsitewise.types.get_interpolated_asset_property_values_response.GetInterpolatedAssetPropertyValuesResponse:
    out: capo_iotsitewise.types.get_interpolated_asset_property_values_response.GetInterpolatedAssetPropertyValuesResponse = capo_iotsitewise.types.get_interpolated_asset_property_values_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_iotsitewise.types.get_interpolated_asset_property_values_response.GetInterpolatedAssetPropertyValuesResponse:
    out: capo_iotsitewise.types.get_interpolated_asset_property_values_response.GetInterpolatedAssetPropertyValuesResponse = capo_iotsitewise.types.get_interpolated_asset_property_values_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_iotsitewise._auth._signers.Signer | None:
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
            sigv4_config = capo_iotsitewise._auth._sigv4.build_sigv4_auth_scheme(
                "iotsitewise", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_iotsitewise._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_iotsitewise.types.get_interpolated_asset_property_values_request.GetInterpolatedAssetPropertyValuesRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_iotsitewise.types.quality

    url = endpoint.url.rstrip("/") + "/properties/interpolated"
    params: list[tuple[str, str]] = []
    if "asset_id" in input_:
        params.append(("assetId", input_["asset_id"]))
    if "property_id" in input_:
        params.append(("propertyId", input_["property_id"]))
    if "property_alias" in input_:
        params.append(("propertyAlias", input_["property_alias"]))
    if "start_time_in_seconds" in input_:
        params.append(("startTimeInSeconds", str(input_["start_time_in_seconds"])))
    if "start_time_offset_in_nanos" in input_:
        params.append(
            ("startTimeOffsetInNanos", str(input_["start_time_offset_in_nanos"]))
        )
    if "end_time_in_seconds" in input_:
        params.append(("endTimeInSeconds", str(input_["end_time_in_seconds"])))
    if "end_time_offset_in_nanos" in input_:
        params.append(("endTimeOffsetInNanos", str(input_["end_time_offset_in_nanos"])))
    if "quality" in input_:
        params.append(
            (
                "quality",
                capo_iotsitewise.types.quality.serialize_json(input_["quality"]),
            )
        )
    if "interval_in_seconds" in input_:
        params.append(("intervalInSeconds", str(input_["interval_in_seconds"])))
    if "next_token" in input_:
        params.append(("nextToken", input_["next_token"]))
    if "max_results" in input_:
        params.append(("maxResults", str(input_["max_results"])))
    if "type" in input_:
        params.append(("type", input_["type"]))
    if "interval_window_in_seconds" in input_:
        params.append(
            ("intervalWindowInSeconds", str(input_["interval_window_in_seconds"]))
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


def get_interpolated_asset_property_values(
    options: OperationOptions,
    input_: capo_iotsitewise.types.get_interpolated_asset_property_values_request.GetInterpolatedAssetPropertyValuesRequest,
) -> tuple[
    capo_iotsitewise.types.get_interpolated_asset_property_values_response.GetInterpolatedAssetPropertyValuesResponse,
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


async def async_get_interpolated_asset_property_values(
    options: AsyncOperationOptions,
    input_: capo_iotsitewise.types.get_interpolated_asset_property_values_request.GetInterpolatedAssetPropertyValuesRequest,
) -> tuple[
    capo_iotsitewise.types.get_interpolated_asset_property_values_response.GetInterpolatedAssetPropertyValuesResponse,
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
