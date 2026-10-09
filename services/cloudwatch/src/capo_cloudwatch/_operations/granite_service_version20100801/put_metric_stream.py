"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutMetricStream``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_cloudwatch._auth._signers
import capo_cloudwatch._auth._sigv4
import capo_cloudwatch._protocol.eventstream
import capo_cloudwatch.errors.concurrent_modification_exception
import capo_cloudwatch.errors.internal_service_fault
import capo_cloudwatch.errors.invalid_parameter_combination_exception
import capo_cloudwatch.errors.invalid_parameter_value_exception
import capo_cloudwatch.errors.missing_required_parameter_exception
import capo_cloudwatch.types.metric_stream_filters
import capo_cloudwatch.types.metric_stream_output_format
import capo_cloudwatch.types.metric_stream_statistics_configurations
import capo_cloudwatch.types.put_metric_stream_input
import capo_cloudwatch.types.put_metric_stream_output
import capo_cloudwatch.types.tag_list
from capo_cloudwatch._protocol.errors import parse_error_metadata_json
from capo_cloudwatch._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudwatch._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cloudwatch.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConcurrentModificationException":
            raise capo_cloudwatch.errors.concurrent_modification_exception.ConcurrentModificationException.from_aws_json_1_0(
                data, message
            )
        case "InternalServiceFault":
            raise capo_cloudwatch.errors.internal_service_fault.InternalServiceFault.from_aws_json_1_0(
                data, message
            )
        case "InvalidParameterCombinationException":
            raise capo_cloudwatch.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException.from_aws_json_1_0(
                data, message
            )
        case "InvalidParameterValueException":
            raise capo_cloudwatch.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_aws_json_1_0(
                data, message
            )
        case "MissingRequiredParameterException":
            raise capo_cloudwatch.errors.missing_required_parameter_exception.MissingRequiredParameterException.from_aws_json_1_0(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudwatch.types.put_metric_stream_output.PutMetricStreamOutput:
    out: capo_cloudwatch.types.put_metric_stream_output.PutMetricStreamOutput = (
        capo_cloudwatch.types.put_metric_stream_output.deserialize_aws_json_1_0(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudwatch.types.put_metric_stream_output.PutMetricStreamOutput:
    out: capo_cloudwatch.types.put_metric_stream_output.PutMetricStreamOutput = (
        capo_cloudwatch.types.put_metric_stream_output.deserialize_aws_json_1_0(
            json.loads(await response.aread())
        )
    )
    return out


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
    input_: capo_cloudwatch.types.put_metric_stream_input.PutMetricStreamInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "GraniteServiceVersion20100801.PutMetricStream"
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "PutMetricStream"))
    pairs.append(("Version", "2010-08-01"))
    capo_cloudwatch.types.put_metric_stream_input.serialize_query(input_, pairs, "")
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
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


def put_metric_stream(
    options: OperationOptions,
    input_: capo_cloudwatch.types.put_metric_stream_input.PutMetricStreamInput,
) -> tuple[
    capo_cloudwatch.types.put_metric_stream_output.PutMetricStreamOutput,
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


async def async_put_metric_stream(
    options: AsyncOperationOptions,
    input_: capo_cloudwatch.types.put_metric_stream_input.PutMetricStreamInput,
) -> tuple[
    capo_cloudwatch.types.put_metric_stream_output.PutMetricStreamOutput,
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
