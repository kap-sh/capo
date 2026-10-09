"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeDataset``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_databrew._auth._signers
import capo_databrew._auth._sigv4
import capo_databrew._protocol.eventstream
import capo_databrew.errors.resource_not_found_exception
import capo_databrew.errors.validation_exception
import capo_databrew.types.date
import capo_databrew.types.describe_dataset_request
import capo_databrew.types.describe_dataset_response
import capo_databrew.types.format_options
import capo_databrew.types.input
import capo_databrew.types.input_format
import capo_databrew.types.path_options
import capo_databrew.types.source
import capo_databrew.types.tag_map
from capo_databrew._protocol.errors import parse_error_metadata_json
from capo_databrew._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_databrew._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_databrew.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ResourceNotFoundException":
            raise capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_databrew.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_databrew.types.describe_dataset_response.DescribeDatasetResponse:
    out: capo_databrew.types.describe_dataset_response.DescribeDatasetResponse = (
        capo_databrew.types.describe_dataset_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_databrew.types.describe_dataset_response.DescribeDatasetResponse:
    out: capo_databrew.types.describe_dataset_response.DescribeDatasetResponse = (
        capo_databrew.types.describe_dataset_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_databrew._auth._signers.Signer | None:
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
            sigv4_config = capo_databrew._auth._sigv4.build_sigv4_auth_scheme(
                "databrew", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_databrew._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_databrew.types.describe_dataset_request.DescribeDatasetRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/datasets/{Name}"
    url = url.replace("{Name}", quote(input_["name"], safe=""))
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


def describe_dataset(
    options: OperationOptions,
    input_: capo_databrew.types.describe_dataset_request.DescribeDatasetRequest,
) -> tuple[
    capo_databrew.types.describe_dataset_response.DescribeDatasetResponse,
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


async def async_describe_dataset(
    options: AsyncOperationOptions,
    input_: capo_databrew.types.describe_dataset_request.DescribeDatasetRequest,
) -> tuple[
    capo_databrew.types.describe_dataset_response.DescribeDatasetResponse,
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
