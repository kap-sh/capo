"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CreateTrail``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudtrail._auth._signers
import capo_cloudtrail._auth._sigv4
import capo_cloudtrail._protocol.eventstream
import capo_cloudtrail.errors.cloud_trail_access_not_enabled_exception
import capo_cloudtrail.errors.cloud_trail_invalid_client_token_id_exception
import capo_cloudtrail.errors.cloud_watch_logs_delivery_unavailable_exception
import capo_cloudtrail.errors.conflict_exception
import capo_cloudtrail.errors.insufficient_dependency_service_access_permission_exception
import capo_cloudtrail.errors.insufficient_encryption_policy_exception
import capo_cloudtrail.errors.insufficient_s3_bucket_policy_exception
import capo_cloudtrail.errors.insufficient_sns_topic_policy_exception
import capo_cloudtrail.errors.invalid_cloud_watch_logs_log_group_arn_exception
import capo_cloudtrail.errors.invalid_cloud_watch_logs_role_arn_exception
import capo_cloudtrail.errors.invalid_kms_key_id_exception
import capo_cloudtrail.errors.invalid_parameter_combination_exception
import capo_cloudtrail.errors.invalid_parameter_exception
import capo_cloudtrail.errors.invalid_s3_bucket_name_exception
import capo_cloudtrail.errors.invalid_s3_prefix_exception
import capo_cloudtrail.errors.invalid_sns_topic_name_exception
import capo_cloudtrail.errors.invalid_tag_parameter_exception
import capo_cloudtrail.errors.invalid_trail_name_exception
import capo_cloudtrail.errors.kms_exception
import capo_cloudtrail.errors.kms_key_disabled_exception
import capo_cloudtrail.errors.kms_key_not_found_exception
import capo_cloudtrail.errors.maximum_number_of_trails_exceeded_exception
import capo_cloudtrail.errors.no_management_account_slr_exists_exception
import capo_cloudtrail.errors.not_organization_master_account_exception
import capo_cloudtrail.errors.operation_not_permitted_exception
import capo_cloudtrail.errors.organization_not_in_all_features_mode_exception
import capo_cloudtrail.errors.organizations_not_in_use_exception
import capo_cloudtrail.errors.s3_bucket_does_not_exist_exception
import capo_cloudtrail.errors.tags_limit_exceeded_exception
import capo_cloudtrail.errors.throttling_exception
import capo_cloudtrail.errors.trail_already_exists_exception
import capo_cloudtrail.errors.trail_not_provided_exception
import capo_cloudtrail.errors.unsupported_operation_exception
import capo_cloudtrail.types.create_trail_request
import capo_cloudtrail.types.create_trail_response
import capo_cloudtrail.types.tags_list
from capo_cloudtrail._protocol.errors import parse_error_metadata_json
from capo_cloudtrail._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudtrail._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cloudtrail.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CloudTrailAccessNotEnabledException":
            raise capo_cloudtrail.errors.cloud_trail_access_not_enabled_exception.CloudTrailAccessNotEnabledException.from_aws_json_1_1(
                data, message
            )
        case "CloudTrailInvalidClientTokenIdException":
            raise capo_cloudtrail.errors.cloud_trail_invalid_client_token_id_exception.CloudTrailInvalidClientTokenIdException.from_aws_json_1_1(
                data, message
            )
        case "CloudWatchLogsDeliveryUnavailableException":
            raise capo_cloudtrail.errors.cloud_watch_logs_delivery_unavailable_exception.CloudWatchLogsDeliveryUnavailableException.from_aws_json_1_1(
                data, message
            )
        case "ConflictException":
            raise capo_cloudtrail.errors.conflict_exception.ConflictException.from_aws_json_1_1(
                data, message
            )
        case "InsufficientDependencyServiceAccessPermissionException":
            raise capo_cloudtrail.errors.insufficient_dependency_service_access_permission_exception.InsufficientDependencyServiceAccessPermissionException.from_aws_json_1_1(
                data, message
            )
        case "InsufficientEncryptionPolicyException":
            raise capo_cloudtrail.errors.insufficient_encryption_policy_exception.InsufficientEncryptionPolicyException.from_aws_json_1_1(
                data, message
            )
        case "InsufficientS3BucketPolicyException":
            raise capo_cloudtrail.errors.insufficient_s3_bucket_policy_exception.InsufficientS3BucketPolicyException.from_aws_json_1_1(
                data, message
            )
        case "InsufficientSnsTopicPolicyException":
            raise capo_cloudtrail.errors.insufficient_sns_topic_policy_exception.InsufficientSnsTopicPolicyException.from_aws_json_1_1(
                data, message
            )
        case "InvalidCloudWatchLogsLogGroupArnException":
            raise capo_cloudtrail.errors.invalid_cloud_watch_logs_log_group_arn_exception.InvalidCloudWatchLogsLogGroupArnException.from_aws_json_1_1(
                data, message
            )
        case "InvalidCloudWatchLogsRoleArnException":
            raise capo_cloudtrail.errors.invalid_cloud_watch_logs_role_arn_exception.InvalidCloudWatchLogsRoleArnException.from_aws_json_1_1(
                data, message
            )
        case "InvalidKmsKeyIdException":
            raise capo_cloudtrail.errors.invalid_kms_key_id_exception.InvalidKmsKeyIdException.from_aws_json_1_1(
                data, message
            )
        case "InvalidParameterCombinationException":
            raise capo_cloudtrail.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException.from_aws_json_1_1(
                data, message
            )
        case "InvalidParameterException":
            raise capo_cloudtrail.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data, message
            )
        case "InvalidS3BucketNameException":
            raise capo_cloudtrail.errors.invalid_s3_bucket_name_exception.InvalidS3BucketNameException.from_aws_json_1_1(
                data, message
            )
        case "InvalidS3PrefixException":
            raise capo_cloudtrail.errors.invalid_s3_prefix_exception.InvalidS3PrefixException.from_aws_json_1_1(
                data, message
            )
        case "InvalidSnsTopicNameException":
            raise capo_cloudtrail.errors.invalid_sns_topic_name_exception.InvalidSnsTopicNameException.from_aws_json_1_1(
                data, message
            )
        case "InvalidTagParameterException":
            raise capo_cloudtrail.errors.invalid_tag_parameter_exception.InvalidTagParameterException.from_aws_json_1_1(
                data, message
            )
        case "InvalidTrailNameException":
            raise capo_cloudtrail.errors.invalid_trail_name_exception.InvalidTrailNameException.from_aws_json_1_1(
                data, message
            )
        case "KmsException":
            raise capo_cloudtrail.errors.kms_exception.KmsException.from_aws_json_1_1(
                data, message
            )
        case "KmsKeyDisabledException":
            raise capo_cloudtrail.errors.kms_key_disabled_exception.KmsKeyDisabledException.from_aws_json_1_1(
                data, message
            )
        case "KmsKeyNotFoundException":
            raise capo_cloudtrail.errors.kms_key_not_found_exception.KmsKeyNotFoundException.from_aws_json_1_1(
                data, message
            )
        case "MaximumNumberOfTrailsExceededException":
            raise capo_cloudtrail.errors.maximum_number_of_trails_exceeded_exception.MaximumNumberOfTrailsExceededException.from_aws_json_1_1(
                data, message
            )
        case "NoManagementAccountSLRExistsException":
            raise capo_cloudtrail.errors.no_management_account_slr_exists_exception.NoManagementAccountSLRExistsException.from_aws_json_1_1(
                data, message
            )
        case "NotOrganizationMasterAccountException":
            raise capo_cloudtrail.errors.not_organization_master_account_exception.NotOrganizationMasterAccountException.from_aws_json_1_1(
                data, message
            )
        case "OperationNotPermittedException":
            raise capo_cloudtrail.errors.operation_not_permitted_exception.OperationNotPermittedException.from_aws_json_1_1(
                data, message
            )
        case "OrganizationNotInAllFeaturesModeException":
            raise capo_cloudtrail.errors.organization_not_in_all_features_mode_exception.OrganizationNotInAllFeaturesModeException.from_aws_json_1_1(
                data, message
            )
        case "OrganizationsNotInUseException":
            raise capo_cloudtrail.errors.organizations_not_in_use_exception.OrganizationsNotInUseException.from_aws_json_1_1(
                data, message
            )
        case "S3BucketDoesNotExistException":
            raise capo_cloudtrail.errors.s3_bucket_does_not_exist_exception.S3BucketDoesNotExistException.from_aws_json_1_1(
                data, message
            )
        case "TagsLimitExceededException":
            raise capo_cloudtrail.errors.tags_limit_exceeded_exception.TagsLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "ThrottlingException":
            raise capo_cloudtrail.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data, message
            )
        case "TrailAlreadyExistsException":
            raise capo_cloudtrail.errors.trail_already_exists_exception.TrailAlreadyExistsException.from_aws_json_1_1(
                data, message
            )
        case "TrailNotProvidedException":
            raise capo_cloudtrail.errors.trail_not_provided_exception.TrailNotProvidedException.from_aws_json_1_1(
                data, message
            )
        case "UnsupportedOperationException":
            raise capo_cloudtrail.errors.unsupported_operation_exception.UnsupportedOperationException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudtrail.types.create_trail_response.CreateTrailResponse:
    out: capo_cloudtrail.types.create_trail_response.CreateTrailResponse = (
        capo_cloudtrail.types.create_trail_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudtrail.types.create_trail_response.CreateTrailResponse:
    out: capo_cloudtrail.types.create_trail_response.CreateTrailResponse = (
        capo_cloudtrail.types.create_trail_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudtrail._auth._signers.Signer | None:
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
            sigv4_config = capo_cloudtrail._auth._sigv4.build_sigv4_auth_scheme(
                "cloudtrail", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_cloudtrail._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudtrail.types.create_trail_request.CreateTrailRequest,
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
    headers["X-Amz-Target"] = "CloudTrail_20131101.CreateTrail"
    body: bytes | None = json.dumps(
        capo_cloudtrail.types.create_trail_request.serialize_aws_json_1_1(input_),
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


def create_trail(
    options: OperationOptions,
    input_: capo_cloudtrail.types.create_trail_request.CreateTrailRequest,
) -> tuple[
    capo_cloudtrail.types.create_trail_response.CreateTrailResponse, zapros.Response
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


async def async_create_trail(
    options: AsyncOperationOptions,
    input_: capo_cloudtrail.types.create_trail_request.CreateTrailRequest,
) -> tuple[
    capo_cloudtrail.types.create_trail_response.CreateTrailResponse, zapros.Response
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
