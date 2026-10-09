"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupJobs``."""

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
import capo_backup.types.backup_job_state
import capo_backup.types.backup_jobs_list
import capo_backup.types.list_backup_jobs_input
import capo_backup.types.list_backup_jobs_output
import capo_backup.types.timestamp
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
) -> capo_backup.types.list_backup_jobs_output.ListBackupJobsOutput:
    out: capo_backup.types.list_backup_jobs_output.ListBackupJobsOutput = (
        capo_backup.types.list_backup_jobs_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_backup.types.list_backup_jobs_output.ListBackupJobsOutput:
    out: capo_backup.types.list_backup_jobs_output.ListBackupJobsOutput = (
        capo_backup.types.list_backup_jobs_output.deserialize_json(
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
    input_: capo_backup.types.list_backup_jobs_input.ListBackupJobsInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_backup._protocol.serialize
    import capo_backup.types.backup_job_state

    url = endpoint.url.rstrip("/") + "/backup-jobs"
    params: list[tuple[str, str]] = []
    if "next_token" in input_:
        params.append(("nextToken", input_["next_token"]))
    if "max_results" in input_:
        params.append(("maxResults", str(input_["max_results"])))
    if "by_resource_arn" in input_:
        params.append(("resourceArn", input_["by_resource_arn"]))
    if "by_state" in input_:
        params.append(
            (
                "state",
                capo_backup.types.backup_job_state.serialize_json(input_["by_state"]),
            )
        )
    if "by_backup_vault_name" in input_:
        params.append(("backupVaultName", input_["by_backup_vault_name"]))
    if "by_created_before" in input_:
        params.append(
            (
                "createdBefore",
                capo_backup._protocol.serialize.fmt_date_time(
                    input_["by_created_before"]
                ),
            )
        )
    if "by_created_after" in input_:
        params.append(
            (
                "createdAfter",
                capo_backup._protocol.serialize.fmt_date_time(
                    input_["by_created_after"]
                ),
            )
        )
    if "by_resource_type" in input_:
        params.append(("resourceType", input_["by_resource_type"]))
    if "by_account_id" in input_:
        params.append(("accountId", input_["by_account_id"]))
    if "by_complete_after" in input_:
        params.append(
            (
                "completeAfter",
                capo_backup._protocol.serialize.fmt_date_time(
                    input_["by_complete_after"]
                ),
            )
        )
    if "by_complete_before" in input_:
        params.append(
            (
                "completeBefore",
                capo_backup._protocol.serialize.fmt_date_time(
                    input_["by_complete_before"]
                ),
            )
        )
    if "by_parent_job_id" in input_:
        params.append(("parentJobId", input_["by_parent_job_id"]))
    if "by_message_category" in input_:
        params.append(("messageCategory", input_["by_message_category"]))
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


def list_backup_jobs(
    options: OperationOptions,
    input_: capo_backup.types.list_backup_jobs_input.ListBackupJobsInput,
) -> tuple[
    capo_backup.types.list_backup_jobs_output.ListBackupJobsOutput, zapros.Response
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


async def async_list_backup_jobs(
    options: AsyncOperationOptions,
    input_: capo_backup.types.list_backup_jobs_input.ListBackupJobsInput,
) -> tuple[
    capo_backup.types.list_backup_jobs_output.ListBackupJobsOutput, zapros.Response
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
