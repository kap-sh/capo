"""Generated from Smithy shape ``com.amazonaws.configservice#PutDeliveryChannel``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_config_service._auth._signers
import capo_config_service._auth._sigv4
import capo_config_service._protocol.eventstream
import capo_config_service.errors.insufficient_delivery_policy_exception
import capo_config_service.errors.invalid_delivery_channel_name_exception
import capo_config_service.errors.invalid_s3_key_prefix_exception
import capo_config_service.errors.invalid_s3_kms_key_arn_exception
import capo_config_service.errors.invalid_sns_topic_arn_exception
import capo_config_service.errors.max_number_of_delivery_channels_exceeded_exception
import capo_config_service.errors.no_available_configuration_recorder_exception
import capo_config_service.errors.no_such_bucket_exception
import capo_config_service.types.delivery_channel
import capo_config_service.types.put_delivery_channel_request
from capo_config_service._protocol.errors import parse_error_metadata_json
from capo_config_service._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_config_service._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_config_service.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InsufficientDeliveryPolicyException":
            raise capo_config_service.errors.insufficient_delivery_policy_exception.InsufficientDeliveryPolicyException.from_aws_json_1_1(
                data, message
            )
        case "InvalidDeliveryChannelNameException":
            raise capo_config_service.errors.invalid_delivery_channel_name_exception.InvalidDeliveryChannelNameException.from_aws_json_1_1(
                data, message
            )
        case "InvalidS3KeyPrefixException":
            raise capo_config_service.errors.invalid_s3_key_prefix_exception.InvalidS3KeyPrefixException.from_aws_json_1_1(
                data, message
            )
        case "InvalidS3KmsKeyArnException":
            raise capo_config_service.errors.invalid_s3_kms_key_arn_exception.InvalidS3KmsKeyArnException.from_aws_json_1_1(
                data, message
            )
        case "InvalidSNSTopicARNException":
            raise capo_config_service.errors.invalid_sns_topic_arn_exception.InvalidSNSTopicARNException.from_aws_json_1_1(
                data, message
            )
        case "MaxNumberOfDeliveryChannelsExceededException":
            raise capo_config_service.errors.max_number_of_delivery_channels_exceeded_exception.MaxNumberOfDeliveryChannelsExceededException.from_aws_json_1_1(
                data, message
            )
        case "NoAvailableConfigurationRecorderException":
            raise capo_config_service.errors.no_available_configuration_recorder_exception.NoAvailableConfigurationRecorderException.from_aws_json_1_1(
                data, message
            )
        case "NoSuchBucketException":
            raise capo_config_service.errors.no_such_bucket_exception.NoSuchBucketException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_config_service._auth._signers.Signer | None:
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
            sigv4_config = capo_config_service._auth._sigv4.build_sigv4_auth_scheme(
                "config", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_config_service._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_config_service.types.put_delivery_channel_request.PutDeliveryChannelRequest,
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
    headers["X-Amz-Target"] = "StarlingDoveService.PutDeliveryChannel"
    body: bytes | None = json.dumps(
        capo_config_service.types.put_delivery_channel_request.serialize_aws_json_1_1(
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


def put_delivery_channel(
    options: OperationOptions,
    input_: capo_config_service.types.put_delivery_channel_request.PutDeliveryChannelRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_put_delivery_channel(
    options: AsyncOperationOptions,
    input_: capo_config_service.types.put_delivery_channel_request.PutDeliveryChannelRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return None, response
    except BaseException:
        await response.aclose()
        raise
