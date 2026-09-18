"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeAsync``."""

from __future__ import annotations

import json
from collections.abc import AsyncIterator, Iterator
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
import capo_lambda._body
import capo_lambda._protocol.eventstream
import capo_lambda.errors.ec2_access_denied_exception
import capo_lambda.errors.ec2_throttled_exception
import capo_lambda.errors.ec2_unexpected_exception
import capo_lambda.errors.efs_mount_connectivity_exception
import capo_lambda.errors.efs_mount_failure_exception
import capo_lambda.errors.efs_mount_timeout_exception
import capo_lambda.errors.efsio_exception
import capo_lambda.errors.eni_limit_reached_exception
import capo_lambda.errors.invalid_request_content_exception
import capo_lambda.errors.invalid_runtime_exception
import capo_lambda.errors.invalid_security_group_id_exception
import capo_lambda.errors.invalid_subnet_id_exception
import capo_lambda.errors.kms_access_denied_exception
import capo_lambda.errors.kms_disabled_exception
import capo_lambda.errors.kms_invalid_state_exception
import capo_lambda.errors.kms_not_found_exception
import capo_lambda.errors.mode_not_supported_exception
import capo_lambda.errors.resource_conflict_exception
import capo_lambda.errors.resource_not_found_exception
import capo_lambda.errors.s3_files_mount_connectivity_exception
import capo_lambda.errors.s3_files_mount_failure_exception
import capo_lambda.errors.s3_files_mount_timeout_exception
import capo_lambda.errors.service_exception
import capo_lambda.errors.service_quota_exceeded_exception
import capo_lambda.errors.snap_start_exception
import capo_lambda.errors.snap_start_not_ready_exception
import capo_lambda.errors.snap_start_regeneration_failure_exception
import capo_lambda.errors.snap_start_timeout_exception
import capo_lambda.errors.subnet_ip_address_limit_reached_exception
import capo_lambda.types.blob_stream
import capo_lambda.types.invoke_async_request
import capo_lambda.types.invoke_async_response
from capo_lambda._protocol.errors import parse_error_metadata_json
from capo_lambda._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_lambda._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_lambda.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "EC2AccessDeniedException":
            raise capo_lambda.errors.ec2_access_denied_exception.EC2AccessDeniedException.from_json(
                data, message
            )
        case "EC2ThrottledException":
            raise capo_lambda.errors.ec2_throttled_exception.EC2ThrottledException.from_json(
                data, message
            )
        case "EC2UnexpectedException":
            raise capo_lambda.errors.ec2_unexpected_exception.EC2UnexpectedException.from_json(
                data, message
            )
        case "EFSIOException":
            raise capo_lambda.errors.efsio_exception.EFSIOException.from_json(
                data, message
            )
        case "EFSMountConnectivityException":
            raise capo_lambda.errors.efs_mount_connectivity_exception.EFSMountConnectivityException.from_json(
                data, message
            )
        case "EFSMountFailureException":
            raise capo_lambda.errors.efs_mount_failure_exception.EFSMountFailureException.from_json(
                data, message
            )
        case "EFSMountTimeoutException":
            raise capo_lambda.errors.efs_mount_timeout_exception.EFSMountTimeoutException.from_json(
                data, message
            )
        case "ENILimitReachedException":
            raise capo_lambda.errors.eni_limit_reached_exception.ENILimitReachedException.from_json(
                data, message
            )
        case "InvalidRequestContentException":
            raise capo_lambda.errors.invalid_request_content_exception.InvalidRequestContentException.from_json(
                data, message
            )
        case "InvalidRuntimeException":
            raise capo_lambda.errors.invalid_runtime_exception.InvalidRuntimeException.from_json(
                data, message
            )
        case "InvalidSecurityGroupIDException":
            raise capo_lambda.errors.invalid_security_group_id_exception.InvalidSecurityGroupIDException.from_json(
                data, message
            )
        case "InvalidSubnetIDException":
            raise capo_lambda.errors.invalid_subnet_id_exception.InvalidSubnetIDException.from_json(
                data, message
            )
        case "KMSAccessDeniedException":
            raise capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException.from_json(
                data, message
            )
        case "KMSDisabledException":
            raise capo_lambda.errors.kms_disabled_exception.KMSDisabledException.from_json(
                data, message
            )
        case "KMSInvalidStateException":
            raise capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException.from_json(
                data, message
            )
        case "KMSNotFoundException":
            raise capo_lambda.errors.kms_not_found_exception.KMSNotFoundException.from_json(
                data, message
            )
        case "ModeNotSupportedException":
            raise capo_lambda.errors.mode_not_supported_exception.ModeNotSupportedException.from_json(
                data, message
            )
        case "ResourceConflictException":
            raise capo_lambda.errors.resource_conflict_exception.ResourceConflictException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "S3FilesMountConnectivityException":
            raise capo_lambda.errors.s3_files_mount_connectivity_exception.S3FilesMountConnectivityException.from_json(
                data, message
            )
        case "S3FilesMountFailureException":
            raise capo_lambda.errors.s3_files_mount_failure_exception.S3FilesMountFailureException.from_json(
                data, message
            )
        case "S3FilesMountTimeoutException":
            raise capo_lambda.errors.s3_files_mount_timeout_exception.S3FilesMountTimeoutException.from_json(
                data, message
            )
        case "ServiceException":
            raise capo_lambda.errors.service_exception.ServiceException.from_json(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_lambda.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data, message
            )
        case "SnapStartException":
            raise capo_lambda.errors.snap_start_exception.SnapStartException.from_json(
                data, message
            )
        case "SnapStartNotReadyException":
            raise capo_lambda.errors.snap_start_not_ready_exception.SnapStartNotReadyException.from_json(
                data, message
            )
        case "SnapStartRegenerationFailureException":
            raise capo_lambda.errors.snap_start_regeneration_failure_exception.SnapStartRegenerationFailureException.from_json(
                data, message
            )
        case "SnapStartTimeoutException":
            raise capo_lambda.errors.snap_start_timeout_exception.SnapStartTimeoutException.from_json(
                data, message
            )
        case "SubnetIPAddressLimitReachedException":
            raise capo_lambda.errors.subnet_ip_address_limit_reached_exception.SubnetIPAddressLimitReachedException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_lambda.types.invoke_async_response.InvokeAsyncResponse:
    out: capo_lambda.types.invoke_async_response.InvokeAsyncResponse = {}  # type: ignore[typeddict-item]
    out["status"] = response.status
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_lambda.types.invoke_async_response.InvokeAsyncResponse:
    out: capo_lambda.types.invoke_async_response.InvokeAsyncResponse = {}  # type: ignore[typeddict-item]
    out["status"] = response.status
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_lambda._auth._signers.Signer | None:
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
            sigv4_config = capo_lambda._auth._sigv4.build_sigv4_auth_scheme(
                "lambda", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_lambda._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_lambda.types.invoke_async_request.InvokeAsyncRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2014-11-13/functions/{FunctionName}/invoke-async"
    url = url.replace("{FunctionName}", quote(input_["function_name"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body = input_["invoke_args"]
    if isinstance(body, capo_lambda._body.Body):
        body = cast(capo_lambda._body.Body[Iterator[bytes]], body)
        stream = body.stream
        if stream is None:
            rebuilt = body.rebuild()
            if rebuilt is None:
                raise RuntimeError("streaming body could not be rebuilt")
            stream, _ = rebuilt
        if "content-length" not in [header.lower() for header in headers]:
            headers["Content-Length"] = str(body.length)
        body = stream
    if isinstance(body, capo_lambda._iter.StaticAnyIterator):
        body = cast(bytes, body.content)
    if not isinstance(body, bytes) and "content-length" not in [
        header.lower() for header in headers
    ]:
        raise ValueError("Content-Length is required for streaming input")
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


async def async_build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_lambda.types.invoke_async_request.InvokeAsyncRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2014-11-13/functions/{FunctionName}/invoke-async"
    url = url.replace("{FunctionName}", quote(input_["function_name"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body = input_["invoke_args"]
    if isinstance(body, capo_lambda._body.Body):
        body = cast(capo_lambda._body.Body[AsyncIterator[bytes]], body)
        stream = body.stream
        if stream is None:
            rebuilt = await body.arebuild()
            if rebuilt is None:
                raise RuntimeError("streaming body could not be rebuilt")
            stream, _ = rebuilt
        if "content-length" not in [header.lower() for header in headers]:
            headers["Content-Length"] = str(body.length)
        body = stream
    if isinstance(body, capo_lambda._iter.StaticAnyIterator):
        body = cast(bytes, body.content)
    if not isinstance(body, bytes) and "content-length" not in [
        header.lower() for header in headers
    ]:
        raise ValueError("Content-Length is required for streaming input")
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def invoke_async(
    options: OperationOptions,
    input_: capo_lambda.types.invoke_async_request.InvokeAsyncRequest,
) -> tuple[
    capo_lambda.types.invoke_async_response.InvokeAsyncResponse, zapros.Response
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_invoke_async(
    options: AsyncOperationOptions,
    input_: capo_lambda.types.invoke_async_request.InvokeAsyncRequest,
) -> tuple[
    capo_lambda.types.invoke_async_response.InvokeAsyncResponse, zapros.Response
]:
    response = await options.client.handler.ahandle(
        await async_build_request(options, input_)
    )
    try:
        if response.status >= 300:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
