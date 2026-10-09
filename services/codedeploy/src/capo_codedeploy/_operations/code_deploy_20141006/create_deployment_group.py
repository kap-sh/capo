"""Generated from Smithy shape ``com.amazonaws.codedeploy#CreateDeploymentGroup``."""

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
import capo_codedeploy.errors.deployment_group_already_exists_exception
import capo_codedeploy.errors.deployment_group_limit_exceeded_exception
import capo_codedeploy.errors.deployment_group_name_required_exception
import capo_codedeploy.errors.ecs_service_mapping_limit_exceeded_exception
import capo_codedeploy.errors.invalid_alarm_config_exception
import capo_codedeploy.errors.invalid_application_name_exception
import capo_codedeploy.errors.invalid_auto_rollback_config_exception
import capo_codedeploy.errors.invalid_auto_scaling_group_exception
import capo_codedeploy.errors.invalid_blue_green_deployment_configuration_exception
import capo_codedeploy.errors.invalid_deployment_config_name_exception
import capo_codedeploy.errors.invalid_deployment_group_name_exception
import capo_codedeploy.errors.invalid_deployment_style_exception
import capo_codedeploy.errors.invalid_ec2_tag_combination_exception
import capo_codedeploy.errors.invalid_ec2_tag_exception
import capo_codedeploy.errors.invalid_ecs_service_exception
import capo_codedeploy.errors.invalid_input_exception
import capo_codedeploy.errors.invalid_load_balancer_info_exception
import capo_codedeploy.errors.invalid_on_premises_tag_combination_exception
import capo_codedeploy.errors.invalid_role_exception
import capo_codedeploy.errors.invalid_tag_exception
import capo_codedeploy.errors.invalid_tags_to_add_exception
import capo_codedeploy.errors.invalid_target_group_pair_exception
import capo_codedeploy.errors.invalid_traffic_routing_configuration_exception
import capo_codedeploy.errors.invalid_trigger_config_exception
import capo_codedeploy.errors.lifecycle_hook_limit_exceeded_exception
import capo_codedeploy.errors.role_required_exception
import capo_codedeploy.errors.tag_set_list_limit_exceeded_exception
import capo_codedeploy.errors.throttling_exception
import capo_codedeploy.errors.trigger_targets_limit_exceeded_exception
import capo_codedeploy.types.alarm_configuration
import capo_codedeploy.types.auto_rollback_configuration
import capo_codedeploy.types.auto_scaling_group_name_list
import capo_codedeploy.types.blue_green_deployment_configuration
import capo_codedeploy.types.create_deployment_group_input
import capo_codedeploy.types.create_deployment_group_output
import capo_codedeploy.types.deployment_style
import capo_codedeploy.types.ec2_tag_filter_list
import capo_codedeploy.types.ec2_tag_set
import capo_codedeploy.types.ecs_service_list
import capo_codedeploy.types.load_balancer_info
import capo_codedeploy.types.on_premises_tag_set
import capo_codedeploy.types.outdated_instances_strategy
import capo_codedeploy.types.tag_filter_list
import capo_codedeploy.types.tag_list
import capo_codedeploy.types.trigger_config_list
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
        case "DeploymentGroupAlreadyExistsException":
            raise capo_codedeploy.errors.deployment_group_already_exists_exception.DeploymentGroupAlreadyExistsException.from_aws_json_1_1(
                data, message
            )
        case "DeploymentGroupLimitExceededException":
            raise capo_codedeploy.errors.deployment_group_limit_exceeded_exception.DeploymentGroupLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "DeploymentGroupNameRequiredException":
            raise capo_codedeploy.errors.deployment_group_name_required_exception.DeploymentGroupNameRequiredException.from_aws_json_1_1(
                data, message
            )
        case "ECSServiceMappingLimitExceededException":
            raise capo_codedeploy.errors.ecs_service_mapping_limit_exceeded_exception.ECSServiceMappingLimitExceededException.from_aws_json_1_1(
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
        case "InvalidBlueGreenDeploymentConfigurationException":
            raise capo_codedeploy.errors.invalid_blue_green_deployment_configuration_exception.InvalidBlueGreenDeploymentConfigurationException.from_aws_json_1_1(
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
        case "InvalidDeploymentStyleException":
            raise capo_codedeploy.errors.invalid_deployment_style_exception.InvalidDeploymentStyleException.from_aws_json_1_1(
                data, message
            )
        case "InvalidEC2TagCombinationException":
            raise capo_codedeploy.errors.invalid_ec2_tag_combination_exception.InvalidEC2TagCombinationException.from_aws_json_1_1(
                data, message
            )
        case "InvalidEC2TagException":
            raise capo_codedeploy.errors.invalid_ec2_tag_exception.InvalidEC2TagException.from_aws_json_1_1(
                data, message
            )
        case "InvalidECSServiceException":
            raise capo_codedeploy.errors.invalid_ecs_service_exception.InvalidECSServiceException.from_aws_json_1_1(
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
        case "InvalidOnPremisesTagCombinationException":
            raise capo_codedeploy.errors.invalid_on_premises_tag_combination_exception.InvalidOnPremisesTagCombinationException.from_aws_json_1_1(
                data, message
            )
        case "InvalidRoleException":
            raise capo_codedeploy.errors.invalid_role_exception.InvalidRoleException.from_aws_json_1_1(
                data, message
            )
        case "InvalidTagException":
            raise capo_codedeploy.errors.invalid_tag_exception.InvalidTagException.from_aws_json_1_1(
                data, message
            )
        case "InvalidTagsToAddException":
            raise capo_codedeploy.errors.invalid_tags_to_add_exception.InvalidTagsToAddException.from_aws_json_1_1(
                data, message
            )
        case "InvalidTargetGroupPairException":
            raise capo_codedeploy.errors.invalid_target_group_pair_exception.InvalidTargetGroupPairException.from_aws_json_1_1(
                data, message
            )
        case "InvalidTrafficRoutingConfigurationException":
            raise capo_codedeploy.errors.invalid_traffic_routing_configuration_exception.InvalidTrafficRoutingConfigurationException.from_aws_json_1_1(
                data, message
            )
        case "InvalidTriggerConfigException":
            raise capo_codedeploy.errors.invalid_trigger_config_exception.InvalidTriggerConfigException.from_aws_json_1_1(
                data, message
            )
        case "LifecycleHookLimitExceededException":
            raise capo_codedeploy.errors.lifecycle_hook_limit_exceeded_exception.LifecycleHookLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "RoleRequiredException":
            raise capo_codedeploy.errors.role_required_exception.RoleRequiredException.from_aws_json_1_1(
                data, message
            )
        case "TagSetListLimitExceededException":
            raise capo_codedeploy.errors.tag_set_list_limit_exceeded_exception.TagSetListLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "ThrottlingException":
            raise capo_codedeploy.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data, message
            )
        case "TriggerTargetsLimitExceededException":
            raise capo_codedeploy.errors.trigger_targets_limit_exceeded_exception.TriggerTargetsLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_codedeploy.types.create_deployment_group_output.CreateDeploymentGroupOutput:
    out: capo_codedeploy.types.create_deployment_group_output.CreateDeploymentGroupOutput = capo_codedeploy.types.create_deployment_group_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_codedeploy.types.create_deployment_group_output.CreateDeploymentGroupOutput:
    out: capo_codedeploy.types.create_deployment_group_output.CreateDeploymentGroupOutput = capo_codedeploy.types.create_deployment_group_output.deserialize_aws_json_1_1(
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
    input_: capo_codedeploy.types.create_deployment_group_input.CreateDeploymentGroupInput,
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
    headers["X-Amz-Target"] = "CodeDeploy_20141006.CreateDeploymentGroup"
    body: bytes | None = json.dumps(
        capo_codedeploy.types.create_deployment_group_input.serialize_aws_json_1_1(
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


def create_deployment_group(
    options: OperationOptions,
    input_: capo_codedeploy.types.create_deployment_group_input.CreateDeploymentGroupInput,
) -> tuple[
    capo_codedeploy.types.create_deployment_group_output.CreateDeploymentGroupOutput,
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


async def async_create_deployment_group(
    options: AsyncOperationOptions,
    input_: capo_codedeploy.types.create_deployment_group_input.CreateDeploymentGroupInput,
) -> tuple[
    capo_codedeploy.types.create_deployment_group_output.CreateDeploymentGroupOutput,
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
