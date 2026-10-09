"""Generated from Smithy shape ``com.amazonaws.codedeploy#CreateDeployment``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_codedeploy._auth._signers
import capo_codedeploy._auth._sigv4
import capo_codedeploy._protocol.eventstream
import capo_codedeploy.errors.alarms_limit_exceeded_exception
import capo_codedeploy.errors.application_does_not_exist_exception
import capo_codedeploy.errors.application_name_required_exception
import capo_codedeploy.errors.deployment_config_does_not_exist_exception
import capo_codedeploy.errors.deployment_group_does_not_exist_exception
import capo_codedeploy.errors.deployment_group_name_required_exception
import capo_codedeploy.errors.deployment_limit_exceeded_exception
import capo_codedeploy.errors.description_too_long_exception
import capo_codedeploy.errors.invalid_alarm_config_exception
import capo_codedeploy.errors.invalid_application_name_exception
import capo_codedeploy.errors.invalid_auto_rollback_config_exception
import capo_codedeploy.errors.invalid_auto_scaling_group_exception
import capo_codedeploy.errors.invalid_compute_platform_exception
import capo_codedeploy.errors.invalid_deployment_config_name_exception
import capo_codedeploy.errors.invalid_deployment_group_name_exception
import capo_codedeploy.errors.invalid_ecs_service_exception
import capo_codedeploy.errors.invalid_file_exists_behavior_exception
import capo_codedeploy.errors.invalid_git_hub_account_token_exception
import capo_codedeploy.errors.invalid_ignore_application_stop_failures_value_exception
import capo_codedeploy.errors.invalid_input_exception
import capo_codedeploy.errors.invalid_load_balancer_info_exception
import capo_codedeploy.errors.invalid_revision_exception
import capo_codedeploy.errors.invalid_role_exception
import capo_codedeploy.errors.invalid_target_instances_exception
import capo_codedeploy.errors.invalid_traffic_routing_configuration_exception
import capo_codedeploy.errors.invalid_update_outdated_instances_only_value_exception
import capo_codedeploy.errors.revision_does_not_exist_exception
import capo_codedeploy.errors.revision_required_exception
import capo_codedeploy.errors.throttling_exception
import capo_codedeploy.types.alarm_configuration
import capo_codedeploy.types.auto_rollback_configuration
import capo_codedeploy.types.create_deployment_input
import capo_codedeploy.types.create_deployment_output
import capo_codedeploy.types.deployment_mode
import capo_codedeploy.types.file_exists_behavior
import capo_codedeploy.types.revision_location
import capo_codedeploy.types.target_instances
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
        case "AlarmsLimitExceededException":
            raise capo_codedeploy.errors.alarms_limit_exceeded_exception.AlarmsLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "ApplicationDoesNotExistException":
            raise capo_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException.from_aws_json_1_1(
                data, message
            )
        case "ApplicationNameRequiredException":
            raise capo_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException.from_aws_json_1_1(
                data, message
            )
        case "DeploymentConfigDoesNotExistException":
            raise capo_codedeploy.errors.deployment_config_does_not_exist_exception.DeploymentConfigDoesNotExistException.from_aws_json_1_1(
                data, message
            )
        case "DeploymentGroupDoesNotExistException":
            raise capo_codedeploy.errors.deployment_group_does_not_exist_exception.DeploymentGroupDoesNotExistException.from_aws_json_1_1(
                data, message
            )
        case "DeploymentGroupNameRequiredException":
            raise capo_codedeploy.errors.deployment_group_name_required_exception.DeploymentGroupNameRequiredException.from_aws_json_1_1(
                data, message
            )
        case "DeploymentLimitExceededException":
            raise capo_codedeploy.errors.deployment_limit_exceeded_exception.DeploymentLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "DescriptionTooLongException":
            raise capo_codedeploy.errors.description_too_long_exception.DescriptionTooLongException.from_aws_json_1_1(
                data, message
            )
        case "InvalidAlarmConfigException":
            raise capo_codedeploy.errors.invalid_alarm_config_exception.InvalidAlarmConfigException.from_aws_json_1_1(
                data, message
            )
        case "InvalidApplicationNameException":
            raise capo_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException.from_aws_json_1_1(
                data, message
            )
        case "InvalidAutoRollbackConfigException":
            raise capo_codedeploy.errors.invalid_auto_rollback_config_exception.InvalidAutoRollbackConfigException.from_aws_json_1_1(
                data, message
            )
        case "InvalidAutoScalingGroupException":
            raise capo_codedeploy.errors.invalid_auto_scaling_group_exception.InvalidAutoScalingGroupException.from_aws_json_1_1(
                data, message
            )
        case "InvalidComputePlatformException":
            raise capo_codedeploy.errors.invalid_compute_platform_exception.InvalidComputePlatformException.from_aws_json_1_1(
                data, message
            )
        case "InvalidDeploymentConfigNameException":
            raise capo_codedeploy.errors.invalid_deployment_config_name_exception.InvalidDeploymentConfigNameException.from_aws_json_1_1(
                data, message
            )
        case "InvalidDeploymentGroupNameException":
            raise capo_codedeploy.errors.invalid_deployment_group_name_exception.InvalidDeploymentGroupNameException.from_aws_json_1_1(
                data, message
            )
        case "InvalidECSServiceException":
            raise capo_codedeploy.errors.invalid_ecs_service_exception.InvalidECSServiceException.from_aws_json_1_1(
                data, message
            )
        case "InvalidFileExistsBehaviorException":
            raise capo_codedeploy.errors.invalid_file_exists_behavior_exception.InvalidFileExistsBehaviorException.from_aws_json_1_1(
                data, message
            )
        case "InvalidGitHubAccountTokenException":
            raise capo_codedeploy.errors.invalid_git_hub_account_token_exception.InvalidGitHubAccountTokenException.from_aws_json_1_1(
                data, message
            )
        case "InvalidIgnoreApplicationStopFailuresValueException":
            raise capo_codedeploy.errors.invalid_ignore_application_stop_failures_value_exception.InvalidIgnoreApplicationStopFailuresValueException.from_aws_json_1_1(
                data, message
            )
        case "InvalidInputException":
            raise capo_codedeploy.errors.invalid_input_exception.InvalidInputException.from_aws_json_1_1(
                data, message
            )
        case "InvalidLoadBalancerInfoException":
            raise capo_codedeploy.errors.invalid_load_balancer_info_exception.InvalidLoadBalancerInfoException.from_aws_json_1_1(
                data, message
            )
        case "InvalidRevisionException":
            raise capo_codedeploy.errors.invalid_revision_exception.InvalidRevisionException.from_aws_json_1_1(
                data, message
            )
        case "InvalidRoleException":
            raise capo_codedeploy.errors.invalid_role_exception.InvalidRoleException.from_aws_json_1_1(
                data, message
            )
        case "InvalidTargetInstancesException":
            raise capo_codedeploy.errors.invalid_target_instances_exception.InvalidTargetInstancesException.from_aws_json_1_1(
                data, message
            )
        case "InvalidTrafficRoutingConfigurationException":
            raise capo_codedeploy.errors.invalid_traffic_routing_configuration_exception.InvalidTrafficRoutingConfigurationException.from_aws_json_1_1(
                data, message
            )
        case "InvalidUpdateOutdatedInstancesOnlyValueException":
            raise capo_codedeploy.errors.invalid_update_outdated_instances_only_value_exception.InvalidUpdateOutdatedInstancesOnlyValueException.from_aws_json_1_1(
                data, message
            )
        case "RevisionDoesNotExistException":
            raise capo_codedeploy.errors.revision_does_not_exist_exception.RevisionDoesNotExistException.from_aws_json_1_1(
                data, message
            )
        case "RevisionRequiredException":
            raise capo_codedeploy.errors.revision_required_exception.RevisionRequiredException.from_aws_json_1_1(
                data, message
            )
        case "ThrottlingException":
            raise capo_codedeploy.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_codedeploy.types.create_deployment_output.CreateDeploymentOutput:
    out: capo_codedeploy.types.create_deployment_output.CreateDeploymentOutput = (
        capo_codedeploy.types.create_deployment_output.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_codedeploy.types.create_deployment_output.CreateDeploymentOutput:
    out: capo_codedeploy.types.create_deployment_output.CreateDeploymentOutput = (
        capo_codedeploy.types.create_deployment_output.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
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
    input_: capo_codedeploy.types.create_deployment_input.CreateDeploymentInput,
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
    headers["X-Amz-Target"] = "CodeDeploy_20141006.CreateDeployment"
    body: bytes | None = json.dumps(
        capo_codedeploy.types.create_deployment_input.serialize_aws_json_1_1(input_),
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


def create_deployment(
    options: OperationOptions,
    input_: capo_codedeploy.types.create_deployment_input.CreateDeploymentInput,
) -> tuple[
    capo_codedeploy.types.create_deployment_output.CreateDeploymentOutput,
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


async def async_create_deployment(
    options: AsyncOperationOptions,
    input_: capo_codedeploy.types.create_deployment_input.CreateDeploymentInput,
) -> tuple[
    capo_codedeploy.types.create_deployment_output.CreateDeploymentOutput,
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
