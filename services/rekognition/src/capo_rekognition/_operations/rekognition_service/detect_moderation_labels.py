"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectModerationLabels``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_rekognition._auth._signers
import capo_rekognition._auth._sigv4
import capo_rekognition._protocol.eventstream
import capo_rekognition.errors.access_denied_exception
import capo_rekognition.errors.human_loop_quota_exceeded_exception
import capo_rekognition.errors.image_too_large_exception
import capo_rekognition.errors.internal_server_error
import capo_rekognition.errors.invalid_image_format_exception
import capo_rekognition.errors.invalid_parameter_exception
import capo_rekognition.errors.invalid_s3_object_exception
import capo_rekognition.errors.provisioned_throughput_exceeded_exception
import capo_rekognition.errors.resource_not_found_exception
import capo_rekognition.errors.resource_not_ready_exception
import capo_rekognition.errors.throttling_exception
import capo_rekognition.types.content_types
import capo_rekognition.types.detect_moderation_labels_request
import capo_rekognition.types.detect_moderation_labels_response
import capo_rekognition.types.human_loop_activation_output
import capo_rekognition.types.human_loop_config
import capo_rekognition.types.image
import capo_rekognition.types.moderation_labels
from capo_rekognition._protocol.errors import parse_error_metadata_json
from capo_rekognition._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_rekognition._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_rekognition.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_rekognition.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data, message
            )
        case "HumanLoopQuotaExceededException":
            raise capo_rekognition.errors.human_loop_quota_exceeded_exception.HumanLoopQuotaExceededException.from_aws_json_1_1(
                data, message
            )
        case "ImageTooLargeException":
            raise capo_rekognition.errors.image_too_large_exception.ImageTooLargeException.from_aws_json_1_1(
                data, message
            )
        case "InternalServerError":
            raise capo_rekognition.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data, message
            )
        case "InvalidImageFormatException":
            raise capo_rekognition.errors.invalid_image_format_exception.InvalidImageFormatException.from_aws_json_1_1(
                data, message
            )
        case "InvalidParameterException":
            raise capo_rekognition.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data, message
            )
        case "InvalidS3ObjectException":
            raise capo_rekognition.errors.invalid_s3_object_exception.InvalidS3ObjectException.from_aws_json_1_1(
                data, message
            )
        case "ProvisionedThroughputExceededException":
            raise capo_rekognition.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException.from_aws_json_1_1(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_rekognition.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data, message
            )
        case "ResourceNotReadyException":
            raise capo_rekognition.errors.resource_not_ready_exception.ResourceNotReadyException.from_aws_json_1_1(
                data, message
            )
        case "ThrottlingException":
            raise capo_rekognition.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_rekognition.types.detect_moderation_labels_response.DetectModerationLabelsResponse:
    out: capo_rekognition.types.detect_moderation_labels_response.DetectModerationLabelsResponse = capo_rekognition.types.detect_moderation_labels_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_rekognition.types.detect_moderation_labels_response.DetectModerationLabelsResponse:
    out: capo_rekognition.types.detect_moderation_labels_response.DetectModerationLabelsResponse = capo_rekognition.types.detect_moderation_labels_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_rekognition._auth._signers.Signer | None:
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
            sigv4_config = capo_rekognition._auth._sigv4.build_sigv4_auth_scheme(
                "rekognition", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_rekognition._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_rekognition.types.detect_moderation_labels_request.DetectModerationLabelsRequest,
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
    headers["X-Amz-Target"] = "RekognitionService.DetectModerationLabels"
    body: bytes | None = json.dumps(
        capo_rekognition.types.detect_moderation_labels_request.serialize_aws_json_1_1(
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


def detect_moderation_labels(
    options: OperationOptions,
    input_: capo_rekognition.types.detect_moderation_labels_request.DetectModerationLabelsRequest,
) -> tuple[
    capo_rekognition.types.detect_moderation_labels_response.DetectModerationLabelsResponse,
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


async def async_detect_moderation_labels(
    options: AsyncOperationOptions,
    input_: capo_rekognition.types.detect_moderation_labels_request.DetectModerationLabelsRequest,
) -> tuple[
    capo_rekognition.types.detect_moderation_labels_response.DetectModerationLabelsResponse,
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
