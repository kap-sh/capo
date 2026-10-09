"""Generated from Smithy shape ``com.amazonaws.efs#DescribeBackupPolicy``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_efs._auth._signers
import capo_efs._auth._sigv4
import capo_efs._protocol.eventstream
import capo_efs.errors.bad_request
import capo_efs.errors.file_system_not_found
import capo_efs.errors.internal_server_error
import capo_efs.errors.policy_not_found
import capo_efs.errors.validation_exception
import capo_efs.types.backup_policy
import capo_efs.types.backup_policy_description
import capo_efs.types.describe_backup_policy_request
from capo_efs._protocol.errors import parse_error_metadata_json
from capo_efs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_efs._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_efs.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequest":
            raise capo_efs.errors.bad_request.BadRequest.from_json(data, message)
        case "FileSystemNotFound":
            raise capo_efs.errors.file_system_not_found.FileSystemNotFound.from_json(
                data, message
            )
        case "InternalServerError":
            raise capo_efs.errors.internal_server_error.InternalServerError.from_json(
                data, message
            )
        case "PolicyNotFound":
            raise capo_efs.errors.policy_not_found.PolicyNotFound.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_efs.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_efs.types.backup_policy_description.BackupPolicyDescription:
    out: capo_efs.types.backup_policy_description.BackupPolicyDescription = (
        capo_efs.types.backup_policy_description.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_efs.types.backup_policy_description.BackupPolicyDescription:
    out: capo_efs.types.backup_policy_description.BackupPolicyDescription = (
        capo_efs.types.backup_policy_description.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_efs._auth._signers.Signer | None:
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
            sigv4_config = capo_efs._auth._sigv4.build_sigv4_auth_scheme(
                "elasticfilesystem", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_efs._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_efs.types.describe_backup_policy_request.DescribeBackupPolicyRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/2015-02-01/file-systems/{FileSystemId}/backup-policy"
    )
    url = url.replace("{FileSystemId}", quote(input_["file_system_id"], safe=""))
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


def describe_backup_policy(
    options: OperationOptions,
    input_: capo_efs.types.describe_backup_policy_request.DescribeBackupPolicyRequest,
) -> tuple[
    capo_efs.types.backup_policy_description.BackupPolicyDescription, zapros.Response
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


async def async_describe_backup_policy(
    options: AsyncOperationOptions,
    input_: capo_efs.types.describe_backup_policy_request.DescribeBackupPolicyRequest,
) -> tuple[
    capo_efs.types.backup_policy_description.BackupPolicyDescription, zapros.Response
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
