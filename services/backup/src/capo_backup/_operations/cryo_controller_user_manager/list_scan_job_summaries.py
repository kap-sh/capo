"""Generated from Smithy shape ``com.amazonaws.backup#ListScanJobSummaries``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_backup._auth._signers
import capo_backup._auth._sigv4
import capo_backup._protocol.eventstream
import capo_backup.errors.invalid_parameter_value_exception
import capo_backup.errors.service_unavailable_exception
import capo_backup.types.aggregation_period
import capo_backup.types.list_scan_job_summaries_input
import capo_backup.types.list_scan_job_summaries_output
import capo_backup.types.malware_scanner
import capo_backup.types.scan_job_status
import capo_backup.types.scan_job_summary_list
import capo_backup.types.scan_result_status
from capo_backup._protocol.errors import parse_error_metadata_json
from capo_backup._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_backup._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_backup.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            raise capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data, message
            )
        case "ServiceUnavailableException":
            raise capo_backup.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_backup.types.list_scan_job_summaries_output.ListScanJobSummariesOutput:
    out: capo_backup.types.list_scan_job_summaries_output.ListScanJobSummariesOutput = (
        capo_backup.types.list_scan_job_summaries_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_backup.types.list_scan_job_summaries_output.ListScanJobSummariesOutput:
    out: capo_backup.types.list_scan_job_summaries_output.ListScanJobSummariesOutput = (
        capo_backup.types.list_scan_job_summaries_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_backup._auth._signers.Signer | None:
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
            sigv4_config = capo_backup._auth._sigv4.build_sigv4_auth_scheme(
                "backup", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_backup._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_backup.types.list_scan_job_summaries_input.ListScanJobSummariesInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_backup.types.aggregation_period
    import capo_backup.types.malware_scanner
    import capo_backup.types.scan_job_status
    import capo_backup.types.scan_result_status

    url = endpoint.url.rstrip("/") + "/audit/scan-job-summaries"
    params: list[tuple[str, str]] = []
    if "account_id" in input_:
        params.append(("AccountId", input_["account_id"]))
    if "resource_type" in input_:
        params.append(("ResourceType", input_["resource_type"]))
    if "malware_scanner" in input_:
        params.append(
            (
                "MalwareScanner",
                capo_backup.types.malware_scanner.serialize_json(
                    input_["malware_scanner"]
                ),
            )
        )
    if "scan_result_status" in input_:
        params.append(
            (
                "ScanResultStatus",
                capo_backup.types.scan_result_status.serialize_json(
                    input_["scan_result_status"]
                ),
            )
        )
    if "state" in input_:
        params.append(
            ("State", capo_backup.types.scan_job_status.serialize_json(input_["state"]))
        )
    if "aggregation_period" in input_:
        params.append(
            (
                "AggregationPeriod",
                capo_backup.types.aggregation_period.serialize_json(
                    input_["aggregation_period"]
                ),
            )
        )
    if "max_results" in input_:
        params.append(("MaxResults", str(input_["max_results"])))
    if "next_token" in input_:
        params.append(("NextToken", input_["next_token"]))
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


def list_scan_job_summaries(
    options: OperationOptions,
    input_: capo_backup.types.list_scan_job_summaries_input.ListScanJobSummariesInput,
) -> tuple[
    capo_backup.types.list_scan_job_summaries_output.ListScanJobSummariesOutput,
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


async def async_list_scan_job_summaries(
    options: AsyncOperationOptions,
    input_: capo_backup.types.list_scan_job_summaries_input.ListScanJobSummariesInput,
) -> tuple[
    capo_backup.types.list_scan_job_summaries_output.ListScanJobSummariesOutput,
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
