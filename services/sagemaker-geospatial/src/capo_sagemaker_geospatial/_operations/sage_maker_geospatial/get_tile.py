"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GetTile``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_sagemaker_geospatial._auth._signers
import capo_sagemaker_geospatial._auth._sigv4
import capo_sagemaker_geospatial._protocol.eventstream
import capo_sagemaker_geospatial.errors.access_denied_exception
import capo_sagemaker_geospatial.errors.internal_server_exception
import capo_sagemaker_geospatial.errors.resource_not_found_exception
import capo_sagemaker_geospatial.errors.throttling_exception
import capo_sagemaker_geospatial.errors.validation_exception
import capo_sagemaker_geospatial.types.binary_file
import capo_sagemaker_geospatial.types.get_tile_input
import capo_sagemaker_geospatial.types.get_tile_output
import capo_sagemaker_geospatial.types.string_list_input
from capo_sagemaker_geospatial._protocol.errors import parse_error_metadata_json
from capo_sagemaker_geospatial._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_sagemaker_geospatial._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_sagemaker_geospatial.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_sagemaker_geospatial.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_sagemaker_geospatial.types.get_tile_output.GetTileOutput:
    _iter = cast(Any, response.iter_raw())
    out: capo_sagemaker_geospatial.types.get_tile_output.GetTileOutput = {
        "binary_file": _iter
    }  # type: ignore[reportAssignmentType]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_sagemaker_geospatial.types.get_tile_output.GetTileOutput:
    _iter = cast(Any, response.async_iter_raw())
    out: capo_sagemaker_geospatial.types.get_tile_output.GetTileOutput = {
        "binary_file": _iter
    }  # type: ignore[reportAssignmentType]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_sagemaker_geospatial._auth._signers.Signer | None:
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
                capo_sagemaker_geospatial._auth._sigv4.build_sigv4_auth_scheme(
                    "sagemaker-geospatial", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_sagemaker_geospatial._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_sagemaker_geospatial.types.get_tile_input.GetTileInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/tile/{z}/{x}/{y}"
    url = url.replace("{x}", quote(str(input_["x"]), safe=""))
    url = url.replace("{y}", quote(str(input_["y"]), safe=""))
    url = url.replace("{z}", quote(str(input_["z"]), safe=""))
    params: list[tuple[str, str]] = []
    for item in input_["image_assets"]:
        params.append(("ImageAssets", item))
    if "target" in input_:
        params.append(("Target", input_["target"]))
    if "arn" in input_:
        params.append(("Arn", input_["arn"]))
    if "image_mask" in input_:
        params.append(("ImageMask", "true" if input_["image_mask"] else "false"))
    if "output_format" in input_:
        params.append(("OutputFormat", input_["output_format"]))
    if "time_range_filter" in input_:
        params.append(("TimeRangeFilter", input_["time_range_filter"]))
    if "property_filters" in input_:
        params.append(("PropertyFilters", input_["property_filters"]))
    if "output_data_type" in input_:
        params.append(("OutputDataType", input_["output_data_type"]))
    if "execution_role_arn" in input_:
        params.append(("ExecutionRoleArn", input_["execution_role_arn"]))
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


def get_tile(
    options: OperationOptions,
    input_: capo_sagemaker_geospatial.types.get_tile_input.GetTileInput,
) -> tuple[
    capo_sagemaker_geospatial.types.get_tile_output.GetTileOutput, zapros.Response
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


async def async_get_tile(
    options: AsyncOperationOptions,
    input_: capo_sagemaker_geospatial.types.get_tile_input.GetTileInput,
) -> tuple[
    capo_sagemaker_geospatial.types.get_tile_output.GetTileOutput, zapros.Response
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
