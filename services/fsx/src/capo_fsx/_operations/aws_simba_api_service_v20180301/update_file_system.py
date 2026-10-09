"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateFileSystem``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_fsx._auth._signers
import capo_fsx._auth._sigv4
import capo_fsx._protocol.eventstream
import capo_fsx.errors.bad_request
import capo_fsx.errors.file_system_not_found
import capo_fsx.errors.incompatible_parameter_error
import capo_fsx.errors.internal_server_error
import capo_fsx.errors.invalid_network_settings
import capo_fsx.errors.missing_file_system_configuration
import capo_fsx.errors.service_limit_exceeded
import capo_fsx.errors.unsupported_operation
import capo_fsx.types.file_system
import capo_fsx.types.network_type
import capo_fsx.types.storage_type
import capo_fsx.types.update_file_system_lustre_configuration
import capo_fsx.types.update_file_system_ontap_configuration
import capo_fsx.types.update_file_system_open_zfs_configuration
import capo_fsx.types.update_file_system_request
import capo_fsx.types.update_file_system_response
import capo_fsx.types.update_file_system_windows_configuration
from capo_fsx._protocol.errors import parse_error_metadata_json
from capo_fsx._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_fsx._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_fsx.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequest":
            raise capo_fsx.errors.bad_request.BadRequest.from_aws_json_1_1(
                data, message
            )
        case "FileSystemNotFound":
            raise capo_fsx.errors.file_system_not_found.FileSystemNotFound.from_aws_json_1_1(
                data, message
            )
        case "IncompatibleParameterError":
            raise capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError.from_aws_json_1_1(
                data, message
            )
        case "InternalServerError":
            raise capo_fsx.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data, message
            )
        case "InvalidNetworkSettings":
            raise capo_fsx.errors.invalid_network_settings.InvalidNetworkSettings.from_aws_json_1_1(
                data, message
            )
        case "MissingFileSystemConfiguration":
            raise capo_fsx.errors.missing_file_system_configuration.MissingFileSystemConfiguration.from_aws_json_1_1(
                data, message
            )
        case "ServiceLimitExceeded":
            raise capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded.from_aws_json_1_1(
                data, message
            )
        case "UnsupportedOperation":
            raise capo_fsx.errors.unsupported_operation.UnsupportedOperation.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_fsx.types.update_file_system_response.UpdateFileSystemResponse:
    out: capo_fsx.types.update_file_system_response.UpdateFileSystemResponse = (
        capo_fsx.types.update_file_system_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_fsx.types.update_file_system_response.UpdateFileSystemResponse:
    out: capo_fsx.types.update_file_system_response.UpdateFileSystemResponse = (
        capo_fsx.types.update_file_system_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_fsx._auth._signers.Signer | None:
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
            sigv4_config = capo_fsx._auth._sigv4.build_sigv4_auth_scheme(
                "fsx", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_fsx._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_fsx.types.update_file_system_request.UpdateFileSystemRequest,
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
    headers["X-Amz-Target"] = "AWSSimbaAPIService_v20180301.UpdateFileSystem"
    body: bytes | None = json.dumps(
        capo_fsx.types.update_file_system_request.serialize_aws_json_1_1(input_),
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


def update_file_system(
    options: OperationOptions,
    input_: capo_fsx.types.update_file_system_request.UpdateFileSystemRequest,
) -> tuple[
    capo_fsx.types.update_file_system_response.UpdateFileSystemResponse, zapros.Response
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


async def async_update_file_system(
    options: AsyncOperationOptions,
    input_: capo_fsx.types.update_file_system_request.UpdateFileSystemRequest,
) -> tuple[
    capo_fsx.types.update_file_system_response.UpdateFileSystemResponse, zapros.Response
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
