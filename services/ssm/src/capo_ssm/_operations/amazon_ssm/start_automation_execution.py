"""Generated from Smithy shape ``com.amazonaws.ssm#StartAutomationExecution``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_ssm._auth._signers
import capo_ssm._auth._sigv4
import capo_ssm._protocol.eventstream
import capo_ssm.errors.automation_definition_not_found_exception
import capo_ssm.errors.automation_definition_version_not_found_exception
import capo_ssm.errors.automation_execution_limit_exceeded_exception
import capo_ssm.errors.idempotent_parameter_mismatch
import capo_ssm.errors.internal_server_error
import capo_ssm.errors.invalid_automation_execution_parameters_exception
import capo_ssm.errors.invalid_target
import capo_ssm.types.alarm_configuration
import capo_ssm.types.automation_parameter_map
import capo_ssm.types.automation_targets
import capo_ssm.types.execution_mode
import capo_ssm.types.start_automation_execution_request
import capo_ssm.types.start_automation_execution_result
import capo_ssm.types.tag_list
import capo_ssm.types.target_locations
import capo_ssm.types.target_maps
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
        case "AutomationDefinitionNotFoundException":
            raise capo_ssm.errors.automation_definition_not_found_exception.AutomationDefinitionNotFoundException.from_aws_json_1_1(
                data, message
            )
        case "AutomationDefinitionVersionNotFoundException":
            raise capo_ssm.errors.automation_definition_version_not_found_exception.AutomationDefinitionVersionNotFoundException.from_aws_json_1_1(
                data, message
            )
        case "AutomationExecutionLimitExceededException":
            raise capo_ssm.errors.automation_execution_limit_exceeded_exception.AutomationExecutionLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "IdempotentParameterMismatch":
            raise capo_ssm.errors.idempotent_parameter_mismatch.IdempotentParameterMismatch.from_aws_json_1_1(
                data, message
            )
        case "InternalServerError":
            raise capo_ssm.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data, message
            )
        case "InvalidAutomationExecutionParametersException":
            raise capo_ssm.errors.invalid_automation_execution_parameters_exception.InvalidAutomationExecutionParametersException.from_aws_json_1_1(
                data, message
            )
        case "InvalidTarget":
            raise capo_ssm.errors.invalid_target.InvalidTarget.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_ssm.types.start_automation_execution_result.StartAutomationExecutionResult:
    out: capo_ssm.types.start_automation_execution_result.StartAutomationExecutionResult = capo_ssm.types.start_automation_execution_result.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_ssm.types.start_automation_execution_result.StartAutomationExecutionResult:
    out: capo_ssm.types.start_automation_execution_result.StartAutomationExecutionResult = capo_ssm.types.start_automation_execution_result.deserialize_aws_json_1_1(
        json.loads(await response.aread())
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
    input_: capo_ssm.types.start_automation_execution_request.StartAutomationExecutionRequest,
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
    headers["X-Amz-Target"] = "AmazonSSM.StartAutomationExecution"
    body: bytes | None = json.dumps(
        capo_ssm.types.start_automation_execution_request.serialize_aws_json_1_1(
            input_
        ),
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


def start_automation_execution(
    options: OperationOptions,
    input_: capo_ssm.types.start_automation_execution_request.StartAutomationExecutionRequest,
) -> tuple[
    capo_ssm.types.start_automation_execution_result.StartAutomationExecutionResult,
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


async def async_start_automation_execution(
    options: AsyncOperationOptions,
    input_: capo_ssm.types.start_automation_execution_request.StartAutomationExecutionRequest,
) -> tuple[
    capo_ssm.types.start_automation_execution_result.StartAutomationExecutionResult,
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
