"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetMetricData``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_cloudwatch._auth._signers
import capo_cloudwatch._auth._sigv4
import capo_cloudwatch._protocol.eventstream
import capo_cloudwatch.errors.invalid_next_token
import capo_cloudwatch.types.get_metric_data_input
import capo_cloudwatch.types.get_metric_data_output
import capo_cloudwatch.types.label_options
import capo_cloudwatch.types.metric_data_queries
import capo_cloudwatch.types.metric_data_result_messages
import capo_cloudwatch.types.metric_data_results
import capo_cloudwatch.types.scan_by
import capo_cloudwatch.types.timestamp
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
        case "InvalidNextToken":
            raise capo_cloudwatch.errors.invalid_next_token.InvalidNextToken.from_aws_json_1_0(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudwatch.types.get_metric_data_output.GetMetricDataOutput:
    out: capo_cloudwatch.types.get_metric_data_output.GetMetricDataOutput = (
        capo_cloudwatch.types.get_metric_data_output.deserialize_aws_json_1_0(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudwatch.types.get_metric_data_output.GetMetricDataOutput:
    out: capo_cloudwatch.types.get_metric_data_output.GetMetricDataOutput = (
        capo_cloudwatch.types.get_metric_data_output.deserialize_aws_json_1_0(
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
    input_: capo_cloudwatch.types.get_metric_data_input.GetMetricDataInput,
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
    headers["X-Amz-Target"] = "GraniteServiceVersion20100801.GetMetricData"
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "GetMetricData"))
    pairs.append(("Version", "2010-08-01"))
    capo_cloudwatch.types.get_metric_data_input.serialize_query(input_, pairs, "")
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


def get_metric_data(
    options: OperationOptions,
    input_: capo_cloudwatch.types.get_metric_data_input.GetMetricDataInput,
) -> tuple[
    capo_cloudwatch.types.get_metric_data_output.GetMetricDataOutput, zapros.Response
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


async def async_get_metric_data(
    options: AsyncOperationOptions,
    input_: capo_cloudwatch.types.get_metric_data_input.GetMetricDataInput,
) -> tuple[
    capo_cloudwatch.types.get_metric_data_output.GetMetricDataOutput, zapros.Response
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
