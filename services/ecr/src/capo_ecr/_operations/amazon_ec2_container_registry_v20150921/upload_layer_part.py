"""Generated from Smithy shape ``com.amazonaws.ecr#UploadLayerPart``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_ecr._auth._signers
import capo_ecr._auth._sigv4
import capo_ecr._protocol.eventstream
import capo_ecr.errors.invalid_layer_part_exception
import capo_ecr.errors.invalid_parameter_exception
import capo_ecr.errors.kms_exception
import capo_ecr.errors.limit_exceeded_exception
import capo_ecr.errors.repository_not_found_exception
import capo_ecr.errors.server_exception
import capo_ecr.errors.upload_not_found_exception
import capo_ecr.types.layer_part_blob
import capo_ecr.types.upload_layer_part_request
import capo_ecr.types.upload_layer_part_response
from capo_ecr._protocol.errors import parse_error_metadata_json
from capo_ecr._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_ecr._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_ecr.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidLayerPartException":
            raise capo_ecr.errors.invalid_layer_part_exception.InvalidLayerPartException.from_aws_json_1_1(
                data, message
            )
        case "InvalidParameterException":
            raise capo_ecr.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data, message
            )
        case "KmsException":
            raise capo_ecr.errors.kms_exception.KmsException.from_aws_json_1_1(
                data, message
            )
        case "LimitExceededException":
            raise capo_ecr.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "RepositoryNotFoundException":
            raise capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException.from_aws_json_1_1(
                data, message
            )
        case "ServerException":
            raise capo_ecr.errors.server_exception.ServerException.from_aws_json_1_1(
                data, message
            )
        case "UploadNotFoundException":
            raise capo_ecr.errors.upload_not_found_exception.UploadNotFoundException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_ecr.types.upload_layer_part_response.UploadLayerPartResponse:
    out: capo_ecr.types.upload_layer_part_response.UploadLayerPartResponse = (
        capo_ecr.types.upload_layer_part_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_ecr.types.upload_layer_part_response.UploadLayerPartResponse:
    out: capo_ecr.types.upload_layer_part_response.UploadLayerPartResponse = (
        capo_ecr.types.upload_layer_part_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_ecr._auth._signers.Signer | None:
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
            sigv4_config = capo_ecr._auth._sigv4.build_sigv4_auth_scheme(
                "ecr", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_ecr._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_ecr.types.upload_layer_part_request.UploadLayerPartRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AmazonEC2ContainerRegistry_V20150921.UploadLayerPart"
    body: bytes | None = json.dumps(
        capo_ecr.types.upload_layer_part_request.serialize_aws_json_1_1(input_),
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


def upload_layer_part(
    options: OperationOptions,
    input_: capo_ecr.types.upload_layer_part_request.UploadLayerPartRequest,
) -> tuple[
    capo_ecr.types.upload_layer_part_response.UploadLayerPartResponse, zapros.Response
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


async def async_upload_layer_part(
    options: AsyncOperationOptions,
    input_: capo_ecr.types.upload_layer_part_request.UploadLayerPartRequest,
) -> tuple[
    capo_ecr.types.upload_layer_part_response.UploadLayerPartResponse, zapros.Response
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
