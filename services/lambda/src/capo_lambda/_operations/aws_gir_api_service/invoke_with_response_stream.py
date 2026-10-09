"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeWithResponseStream``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
import capo_lambda._protocol.eventstream
import capo_lambda.errors.code_artifact_user_deleted_exception
import capo_lambda.errors.code_artifact_user_failed_exception
import capo_lambda.errors.code_artifact_user_pending_exception
import capo_lambda.errors.ec2_access_denied_exception
import capo_lambda.errors.ec2_throttled_exception
import capo_lambda.errors.ec2_unexpected_exception
import capo_lambda.errors.efs_mount_connectivity_exception
import capo_lambda.errors.efs_mount_failure_exception
import capo_lambda.errors.efs_mount_timeout_exception
import capo_lambda.errors.efsio_exception
import capo_lambda.errors.eni_limit_reached_exception
import capo_lambda.errors.invalid_parameter_value_exception
import capo_lambda.errors.invalid_request_content_exception
import capo_lambda.errors.invalid_runtime_exception
import capo_lambda.errors.invalid_security_group_id_exception
import capo_lambda.errors.invalid_subnet_id_exception
import capo_lambda.errors.invalid_zip_file_exception
import capo_lambda.errors.kms_access_denied_exception
import capo_lambda.errors.kms_disabled_exception
import capo_lambda.errors.kms_invalid_state_exception
import capo_lambda.errors.kms_not_found_exception
import capo_lambda.errors.no_published_version_exception
import capo_lambda.errors.recursive_invocation_exception
import capo_lambda.errors.request_too_large_exception
import capo_lambda.errors.resource_conflict_exception
import capo_lambda.errors.resource_not_found_exception
import capo_lambda.errors.resource_not_ready_exception
import capo_lambda.errors.s3_files_mount_connectivity_exception
import capo_lambda.errors.s3_files_mount_failure_exception
import capo_lambda.errors.s3_files_mount_timeout_exception
import capo_lambda.errors.serialized_request_entity_too_large_exception
import capo_lambda.errors.service_exception
import capo_lambda.errors.service_quota_exceeded_exception
import capo_lambda.errors.snap_start_exception
import capo_lambda.errors.snap_start_not_ready_exception
import capo_lambda.errors.snap_start_regeneration_failure_exception
import capo_lambda.errors.snap_start_timeout_exception
import capo_lambda.errors.subnet_ip_address_limit_reached_exception
import capo_lambda.errors.too_many_requests_exception
import capo_lambda.errors.unsupported_media_type_exception
import capo_lambda.types.blob
import capo_lambda.types.invoke_with_response_stream_request
import capo_lambda.types.invoke_with_response_stream_response
import capo_lambda.types.invoke_with_response_stream_response_event
import capo_lambda.types.log_type
import capo_lambda.types.response_streaming_invocation_type
from capo_lambda._protocol.errors import parse_error_metadata_json
from capo_lambda._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from capo_lambda._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_lambda._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_lambda.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CodeArtifactUserDeletedException":
            raise capo_lambda.errors.code_artifact_user_deleted_exception.CodeArtifactUserDeletedException.from_json(
                data, message
            )
        case "CodeArtifactUserFailedException":
            raise capo_lambda.errors.code_artifact_user_failed_exception.CodeArtifactUserFailedException.from_json(
                data, message
            )
        case "CodeArtifactUserPendingException":
            raise capo_lambda.errors.code_artifact_user_pending_exception.CodeArtifactUserPendingException.from_json(
                data, message
            )
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
        case "InvalidParameterValueException":
            raise capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
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
        case "InvalidZipFileException":
            raise capo_lambda.errors.invalid_zip_file_exception.InvalidZipFileException.from_json(
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
        case "NoPublishedVersionException":
            raise capo_lambda.errors.no_published_version_exception.NoPublishedVersionException.from_json(
                data, message
            )
        case "RecursiveInvocationException":
            raise capo_lambda.errors.recursive_invocation_exception.RecursiveInvocationException.from_json(
                data, message
            )
        case "RequestTooLargeException":
            raise capo_lambda.errors.request_too_large_exception.RequestTooLargeException.from_json(
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
        case "ResourceNotReadyException":
            raise capo_lambda.errors.resource_not_ready_exception.ResourceNotReadyException.from_json(
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
        case "SerializedRequestEntityTooLargeException":
            raise capo_lambda.errors.serialized_request_entity_too_large_exception.SerializedRequestEntityTooLargeException.from_json(
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
        case "TooManyRequestsException":
            raise capo_lambda.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data, message
            )
        case "UnsupportedMediaTypeException":
            raise capo_lambda.errors.unsupported_media_type_exception.UnsupportedMediaTypeException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse:
    _message_decoder = MessageDecoder()
    _union_deser = capo_lambda.types.invoke_with_response_stream_response_event.deserialize_event_json
    _iter = cast(Any, response.iter_bytes())
    out: capo_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse = {
        "event_stream": cast(
            Any, raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "X-Amz-Executed-Version" in response.headers:
        out["executed_version"] = response.headers["X-Amz-Executed-Version"]
    if "Content-Type" in response.headers:
        out["response_stream_content_type"] = response.headers["Content-Type"]
    out["status_code"] = response.status
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse:
    _message_decoder = MessageDecoder()
    _union_deser = capo_lambda.types.invoke_with_response_stream_response_event.deserialize_event_json
    _iter = cast(Any, response.async_iter_bytes())
    out: capo_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse = {
        "event_stream": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "X-Amz-Executed-Version" in response.headers:
        out["executed_version"] = response.headers["X-Amz-Executed-Version"]
    if "Content-Type" in response.headers:
        out["response_stream_content_type"] = response.headers["Content-Type"]
    out["status_code"] = response.status
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
    input_: capo_lambda.types.invoke_with_response_stream_request.InvokeWithResponseStreamRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_lambda.types.log_type
    import capo_lambda.types.response_streaming_invocation_type

    url = (
        endpoint.url.rstrip("/")
        + "/2021-11-15/functions/{FunctionName}/response-streaming-invocations"
    )
    url = url.replace("{FunctionName}", quote(input_["function_name"], safe=""))
    params: list[tuple[str, str]] = []
    if "qualifier" in input_:
        params.append(("Qualifier", input_["qualifier"]))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "log_type" in input_:
        headers["X-Amz-Log-Type"] = capo_lambda.types.log_type.serialize_json(
            input_["log_type"]
        )
    if "client_context" in input_:
        headers["X-Amz-Client-Context"] = input_["client_context"]
    if "tenant_id" in input_:
        headers["X-Amz-Tenant-Id"] = input_["tenant_id"]
    if "invocation_type" in input_:
        headers["X-Amz-Invocation-Type"] = (
            capo_lambda.types.response_streaming_invocation_type.serialize_json(
                input_["invocation_type"]
            )
        )
    if "payload" in input_:
        body: bytes | None = input_["payload"]
        headers["content-type"] = "application/octet-stream"
    else:
        body = b""
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


def invoke_with_response_stream(
    options: OperationOptions,
    input_: capo_lambda.types.invoke_with_response_stream_request.InvokeWithResponseStreamRequest,
) -> tuple[
    capo_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse,
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


async def async_invoke_with_response_stream(
    options: AsyncOperationOptions,
    input_: capo_lambda.types.invoke_with_response_stream_request.InvokeWithResponseStreamRequest,
) -> tuple[
    capo_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse,
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
