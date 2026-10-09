"""Generated from Smithy shape ``com.amazonaws.signer#ListSigningJobs``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_signer._auth._signers
import capo_signer._auth._sigv4
import capo_signer._protocol.eventstream
import capo_signer.errors.access_denied_exception
import capo_signer.errors.internal_service_error_exception
import capo_signer.errors.too_many_requests_exception
import capo_signer.errors.validation_exception
import capo_signer.types.list_signing_jobs_request
import capo_signer.types.list_signing_jobs_response
import capo_signer.types.signing_jobs
import capo_signer.types.signing_status
import capo_signer.types.timestamp
from capo_signer._protocol.errors import parse_error_metadata_json
from capo_signer._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_signer._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_signer.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_signer.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServiceErrorException":
            raise capo_signer.errors.internal_service_error_exception.InternalServiceErrorException.from_json(
                data, message
            )
        case "TooManyRequestsException":
            raise capo_signer.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_signer.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_signer.types.list_signing_jobs_response.ListSigningJobsResponse:
    out: capo_signer.types.list_signing_jobs_response.ListSigningJobsResponse = (
        capo_signer.types.list_signing_jobs_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_signer.types.list_signing_jobs_response.ListSigningJobsResponse:
    out: capo_signer.types.list_signing_jobs_response.ListSigningJobsResponse = (
        capo_signer.types.list_signing_jobs_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_signer._auth._signers.Signer | None:
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
            sigv4_config = capo_signer._auth._sigv4.build_sigv4_auth_scheme(
                "signer", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_signer._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_signer.types.list_signing_jobs_request.ListSigningJobsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_signer._protocol.serialize
    import capo_signer.types.signing_status

    url = endpoint.url.rstrip("/") + "/signing-jobs"
    params: list[tuple[str, str]] = []
    if "status" in input_:
        params.append(
            (
                "status",
                capo_signer.types.signing_status.serialize_json(input_["status"]),
            )
        )
    if "platform_id" in input_:
        params.append(("platformId", input_["platform_id"]))
    if "requested_by" in input_:
        params.append(("requestedBy", input_["requested_by"]))
    if "max_results" in input_:
        params.append(("maxResults", str(input_["max_results"])))
    if "next_token" in input_:
        params.append(("nextToken", input_["next_token"]))
    params.append(("isRevoked", "true" if input_.get("is_revoked", False) else "false"))
    if "signature_expires_before" in input_:
        params.append(
            (
                "signatureExpiresBefore",
                capo_signer._protocol.serialize.fmt_date_time(
                    input_["signature_expires_before"]
                ),
            )
        )
    if "signature_expires_after" in input_:
        params.append(
            (
                "signatureExpiresAfter",
                capo_signer._protocol.serialize.fmt_date_time(
                    input_["signature_expires_after"]
                ),
            )
        )
    if "job_invoker" in input_:
        params.append(("jobInvoker", input_["job_invoker"]))
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


def list_signing_jobs(
    options: OperationOptions,
    input_: capo_signer.types.list_signing_jobs_request.ListSigningJobsRequest,
) -> tuple[
    capo_signer.types.list_signing_jobs_response.ListSigningJobsResponse,
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


async def async_list_signing_jobs(
    options: AsyncOperationOptions,
    input_: capo_signer.types.list_signing_jobs_request.ListSigningJobsRequest,
) -> tuple[
    capo_signer.types.list_signing_jobs_response.ListSigningJobsResponse,
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
