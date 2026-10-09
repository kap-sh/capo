"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListEnrichmentJobs``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_iotsitewise._auth._signers
import capo_iotsitewise._auth._sigv4
import capo_iotsitewise._protocol.eventstream
import capo_iotsitewise.errors.access_denied_exception
import capo_iotsitewise.errors.conflicting_operation_exception
import capo_iotsitewise.errors.internal_failure_exception
import capo_iotsitewise.errors.invalid_request_exception
import capo_iotsitewise.errors.limit_exceeded_exception
import capo_iotsitewise.errors.resource_not_found_exception
import capo_iotsitewise.errors.throttling_exception
import capo_iotsitewise.types.enrichment_job_status
import capo_iotsitewise.types.enrichment_job_summaries
import capo_iotsitewise.types.job_type
import capo_iotsitewise.types.list_enrichment_jobs_request
import capo_iotsitewise.types.list_enrichment_jobs_response
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
        case "AccessDeniedException":
            raise capo_iotsitewise.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "ConflictingOperationException":
            raise capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException.from_json(
                data, message
            )
        case "InternalFailureException":
            raise capo_iotsitewise.errors.internal_failure_exception.InternalFailureException.from_json(
                data, message
            )
        case "InvalidRequestException":
            raise capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException.from_json(
                data, message
            )
        case "LimitExceededException":
            raise capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
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
) -> capo_iotsitewise.types.list_enrichment_jobs_response.ListEnrichmentJobsResponse:
    out: capo_iotsitewise.types.list_enrichment_jobs_response.ListEnrichmentJobsResponse = capo_iotsitewise.types.list_enrichment_jobs_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_iotsitewise.types.list_enrichment_jobs_response.ListEnrichmentJobsResponse:
    out: capo_iotsitewise.types.list_enrichment_jobs_response.ListEnrichmentJobsResponse = capo_iotsitewise.types.list_enrichment_jobs_response.deserialize_json(
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
    input_: capo_iotsitewise.types.list_enrichment_jobs_request.ListEnrichmentJobsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_iotsitewise._protocol.serialize
    import capo_iotsitewise.types.enrichment_job_status
    import capo_iotsitewise.types.job_type

    url = endpoint.url.rstrip("/") + "/workspaces/{workspaceName}/enrichment-jobs"
    url = url.replace("{workspaceName}", quote(input_["workspace_name"], safe=""))
    params: list[tuple[str, str]] = []
    if "dataset_id" in input_:
        params.append(("datasetId", input_["dataset_id"]))
    if "property_alias" in input_:
        params.append(("propertyAlias", input_["property_alias"]))
    if "time_series_id" in input_:
        params.append(("timeSeriesId", input_["time_series_id"]))
    if "status" in input_:
        params.append(
            (
                "status",
                capo_iotsitewise.types.enrichment_job_status.serialize_json(
                    input_["status"]
                ),
            )
        )
    if "job_type" in input_:
        params.append(
            (
                "jobType",
                capo_iotsitewise.types.job_type.serialize_json(input_["job_type"]),
            )
        )
    if "start_date" in input_:
        params.append(
            (
                "startDate",
                capo_iotsitewise._protocol.serialize.fmt_date_time(
                    input_["start_date"]
                ),
            )
        )
    if "end_date" in input_:
        params.append(
            (
                "endDate",
                capo_iotsitewise._protocol.serialize.fmt_date_time(input_["end_date"]),
            )
        )
    if "max_results" in input_:
        params.append(("maxResults", str(input_["max_results"])))
    if "next_token" in input_:
        params.append(("nextToken", input_["next_token"]))
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


def list_enrichment_jobs(
    options: OperationOptions,
    input_: capo_iotsitewise.types.list_enrichment_jobs_request.ListEnrichmentJobsRequest,
) -> tuple[
    capo_iotsitewise.types.list_enrichment_jobs_response.ListEnrichmentJobsResponse,
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


async def async_list_enrichment_jobs(
    options: AsyncOperationOptions,
    input_: capo_iotsitewise.types.list_enrichment_jobs_request.ListEnrichmentJobsRequest,
) -> tuple[
    capo_iotsitewise.types.list_enrichment_jobs_response.ListEnrichmentJobsResponse,
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
