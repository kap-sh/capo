"""Generated from Smithy shape ``com.amazonaws.ssm#SendCommand``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_ssm._auth._signers
import capo_ssm._auth._sigv4
import capo_ssm._protocol.eventstream
import capo_ssm.errors.duplicate_instance_id
import capo_ssm.errors.internal_server_error
import capo_ssm.errors.invalid_document
import capo_ssm.errors.invalid_document_version
import capo_ssm.errors.invalid_instance_id
import capo_ssm.errors.invalid_notification_config
import capo_ssm.errors.invalid_output_folder
import capo_ssm.errors.invalid_parameters
import capo_ssm.errors.invalid_role
import capo_ssm.errors.max_document_size_exceeded
import capo_ssm.errors.unsupported_platform_type
import capo_ssm.types.alarm_configuration
import capo_ssm.types.cloud_watch_output_config
import capo_ssm.types.command
import capo_ssm.types.document_hash_type
import capo_ssm.types.instance_id_list
import capo_ssm.types.notification_config
import capo_ssm.types.parameters
import capo_ssm.types.send_command_request
import capo_ssm.types.send_command_result
import capo_ssm.types.targets
from capo_ssm._protocol.errors import parse_error_metadata_json
from capo_ssm._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_ssm._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_ssm.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "DuplicateInstanceId":
            raise capo_ssm.errors.duplicate_instance_id.DuplicateInstanceId.from_aws_json_1_1(
                data, message
            )
        case "InternalServerError":
            raise capo_ssm.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data, message
            )
        case "InvalidDocument":
            raise capo_ssm.errors.invalid_document.InvalidDocument.from_aws_json_1_1(
                data, message
            )
        case "InvalidDocumentVersion":
            raise capo_ssm.errors.invalid_document_version.InvalidDocumentVersion.from_aws_json_1_1(
                data, message
            )
        case "InvalidInstanceId":
            raise capo_ssm.errors.invalid_instance_id.InvalidInstanceId.from_aws_json_1_1(
                data, message
            )
        case "InvalidNotificationConfig":
            raise capo_ssm.errors.invalid_notification_config.InvalidNotificationConfig.from_aws_json_1_1(
                data, message
            )
        case "InvalidOutputFolder":
            raise capo_ssm.errors.invalid_output_folder.InvalidOutputFolder.from_aws_json_1_1(
                data, message
            )
        case "InvalidParameters":
            raise capo_ssm.errors.invalid_parameters.InvalidParameters.from_aws_json_1_1(
                data, message
            )
        case "InvalidRole":
            raise capo_ssm.errors.invalid_role.InvalidRole.from_aws_json_1_1(
                data, message
            )
        case "MaxDocumentSizeExceeded":
            raise capo_ssm.errors.max_document_size_exceeded.MaxDocumentSizeExceeded.from_aws_json_1_1(
                data, message
            )
        case "UnsupportedPlatformType":
            raise capo_ssm.errors.unsupported_platform_type.UnsupportedPlatformType.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_ssm.types.send_command_result.SendCommandResult:
    out: capo_ssm.types.send_command_result.SendCommandResult = (
        capo_ssm.types.send_command_result.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_ssm.types.send_command_result.SendCommandResult:
    out: capo_ssm.types.send_command_result.SendCommandResult = (
        capo_ssm.types.send_command_result.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_ssm._auth._signers.Signer | None:
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
            sigv4_config = capo_ssm._auth._sigv4.build_sigv4_auth_scheme(
                "ssm", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_ssm._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_ssm.types.send_command_request.SendCommandRequest,
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
    headers["X-Amz-Target"] = "AmazonSSM.SendCommand"
    body: bytes | None = json.dumps(
        capo_ssm.types.send_command_request.serialize_aws_json_1_1(input_),
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


def send_command(
    options: OperationOptions,
    input_: capo_ssm.types.send_command_request.SendCommandRequest,
) -> tuple[capo_ssm.types.send_command_result.SendCommandResult, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_send_command(
    options: AsyncOperationOptions,
    input_: capo_ssm.types.send_command_request.SendCommandRequest,
) -> tuple[capo_ssm.types.send_command_result.SendCommandResult, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
