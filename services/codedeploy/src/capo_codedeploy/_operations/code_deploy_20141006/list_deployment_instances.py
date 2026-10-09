"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListDeploymentInstances``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_codedeploy._auth._signers
import capo_codedeploy._auth._sigv4
import capo_codedeploy._protocol.eventstream
import capo_codedeploy.errors.application_does_not_exist_exception
import capo_codedeploy.errors.deployment_does_not_exist_exception
import capo_codedeploy.errors.deployment_group_does_not_exist_exception
import capo_codedeploy.errors.deployment_id_required_exception
import capo_codedeploy.errors.deployment_not_started_exception
import capo_codedeploy.errors.invalid_compute_platform_exception
import capo_codedeploy.errors.invalid_deployment_id_exception
import capo_codedeploy.errors.invalid_deployment_instance_type_exception
import capo_codedeploy.errors.invalid_instance_status_exception
import capo_codedeploy.errors.invalid_instance_type_exception
import capo_codedeploy.errors.invalid_next_token_exception
import capo_codedeploy.errors.invalid_target_filter_name_exception
import capo_codedeploy.types.instance_status_list
import capo_codedeploy.types.instance_type_list
import capo_codedeploy.types.instances_list
import capo_codedeploy.types.list_deployment_instances_input
import capo_codedeploy.types.list_deployment_instances_output
from capo_codedeploy._protocol.errors import parse_error_metadata_json
from capo_codedeploy._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_codedeploy._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_codedeploy.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ApplicationDoesNotExistException":
            raise capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException.from_aws_json_1_1(
                data, message
            )
        case "DeploymentDoesNotExistException":
            raise capo_codedeploy.errors.deployment_does_not_exist_exception.DeploymentDoesNotExistException.from_aws_json_1_1(
                data, message
            )
        case "DeploymentGroupDoesNotExistException":
            raise capo_codedeploy.errors.deployment_group_does_not_exist_exception.DeploymentGroupDoesNotExistException.from_aws_json_1_1(
                data, message
            )
        case "DeploymentIdRequiredException":
            raise capo_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException.from_aws_json_1_1(
                data, message
            )
        case "DeploymentNotStartedException":
            raise capo_codedeploy.errors.deployment_not_started_exception.DeploymentNotStartedException.from_aws_json_1_1(
                data, message
            )
        case "InvalidComputePlatformException":
            raise capo_codedeploy.errors.invalid_compute_platform_exception.InvalidComputePlatformException.from_aws_json_1_1(
                data, message
            )
        case "InvalidDeploymentIdException":
            raise capo_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException.from_aws_json_1_1(
                data, message
            )
        case "InvalidDeploymentInstanceTypeException":
            raise capo_codedeploy.errors.invalid_deployment_instance_type_exception.InvalidDeploymentInstanceTypeException.from_aws_json_1_1(
                data, message
            )
        case "InvalidInstanceStatusException":
            raise capo_codedeploy.errors.invalid_instance_status_exception.InvalidInstanceStatusException.from_aws_json_1_1(
                data, message
            )
        case "InvalidInstanceTypeException":
            raise capo_codedeploy.errors.invalid_instance_type_exception.InvalidInstanceTypeException.from_aws_json_1_1(
                data, message
            )
        case "InvalidNextTokenException":
            raise capo_codedeploy.errors.invalid_next_token_exception.InvalidNextTokenException.from_aws_json_1_1(
                data, message
            )
        case "InvalidTargetFilterNameException":
            raise capo_codedeploy.errors.invalid_target_filter_name_exception.InvalidTargetFilterNameException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    capo_codedeploy.types.list_deployment_instances_output.ListDeploymentInstancesOutput
):
    out: capo_codedeploy.types.list_deployment_instances_output.ListDeploymentInstancesOutput = capo_codedeploy.types.list_deployment_instances_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    capo_codedeploy.types.list_deployment_instances_output.ListDeploymentInstancesOutput
):
    out: capo_codedeploy.types.list_deployment_instances_output.ListDeploymentInstancesOutput = capo_codedeploy.types.list_deployment_instances_output.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_codedeploy._auth._signers.Signer | None:
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
            sigv4_config = capo_codedeploy._auth._sigv4.build_sigv4_auth_scheme(
                "codedeploy", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_codedeploy._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_codedeploy.types.list_deployment_instances_input.ListDeploymentInstancesInput,
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
    headers["X-Amz-Target"] = "CodeDeploy_20141006.ListDeploymentInstances"
    body: bytes | None = json.dumps(
        capo_codedeploy.types.list_deployment_instances_input.serialize_aws_json_1_1(
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


def list_deployment_instances(
    options: OperationOptions,
    input_: capo_codedeploy.types.list_deployment_instances_input.ListDeploymentInstancesInput,
) -> tuple[
    capo_codedeploy.types.list_deployment_instances_output.ListDeploymentInstancesOutput,
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


async def async_list_deployment_instances(
    options: AsyncOperationOptions,
    input_: capo_codedeploy.types.list_deployment_instances_input.ListDeploymentInstancesInput,
) -> tuple[
    capo_codedeploy.types.list_deployment_instances_output.ListDeploymentInstancesOutput,
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
