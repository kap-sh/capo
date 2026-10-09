"""Generated from Smithy shape ``com.amazonaws.snowball#ListJobs``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_snowball._auth._signers
import capo_snowball._auth._sigv4
import capo_snowball._protocol.eventstream
import capo_snowball.errors.invalid_next_token_exception
import capo_snowball.types.job_list_entry_list
import capo_snowball.types.list_jobs_request
import capo_snowball.types.list_jobs_result
from capo_snowball._protocol.errors import parse_error_metadata_json
from capo_snowball._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_snowball._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_snowball.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidNextTokenException":
            raise capo_snowball.errors.invalid_next_token_exception.InvalidNextTokenException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_snowball.types.list_jobs_result.ListJobsResult:
    out: capo_snowball.types.list_jobs_result.ListJobsResult = (
        capo_snowball.types.list_jobs_result.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_snowball.types.list_jobs_result.ListJobsResult:
    out: capo_snowball.types.list_jobs_result.ListJobsResult = (
        capo_snowball.types.list_jobs_result.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_snowball._auth._signers.Signer | None:
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
            sigv4_config = capo_snowball._auth._sigv4.build_sigv4_auth_scheme(
                "snowball", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_snowball._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_snowball.types.list_jobs_request.ListJobsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSIESnowballJobManagementService.ListJobs"
    body: bytes | None = json.dumps(
        capo_snowball.types.list_jobs_request.serialize_aws_json_1_1(input_),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
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


def list_jobs(
    options: OperationOptions,
    input_: capo_snowball.types.list_jobs_request.ListJobsRequest,
) -> tuple[capo_snowball.types.list_jobs_result.ListJobsResult, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_list_jobs(
    options: AsyncOperationOptions,
    input_: capo_snowball.types.list_jobs_request.ListJobsRequest,
) -> tuple[capo_snowball.types.list_jobs_result.ListJobsResult, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
