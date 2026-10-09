"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelModeratedByAppInstanceUser``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_chime_sdk_messaging._auth._signers
import capo_chime_sdk_messaging._auth._sigv4
import capo_chime_sdk_messaging._protocol.eventstream
import capo_chime_sdk_messaging.errors.bad_request_exception
import capo_chime_sdk_messaging.errors.forbidden_exception
import capo_chime_sdk_messaging.errors.service_failure_exception
import capo_chime_sdk_messaging.errors.service_unavailable_exception
import capo_chime_sdk_messaging.errors.throttled_client_exception
import capo_chime_sdk_messaging.errors.unauthorized_client_exception
import capo_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary
import capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_request
import capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response
from capo_chime_sdk_messaging._protocol.errors import parse_error_metadata_json
from capo_chime_sdk_messaging._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_chime_sdk_messaging._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_chime_sdk_messaging.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException.from_json(
                data, message
            )
        case "ForbiddenException":
            raise capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException.from_json(
                data, message
            )
        case "ServiceFailureException":
            raise capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException.from_json(
                data, message
            )
        case "ServiceUnavailableException":
            raise capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message
            )
        case "ThrottledClientException":
            raise capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException.from_json(
                data, message
            )
        case "UnauthorizedClientException":
            raise capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response.DescribeChannelModeratedByAppInstanceUserResponse:
    out: capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response.DescribeChannelModeratedByAppInstanceUserResponse = capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response.DescribeChannelModeratedByAppInstanceUserResponse:
    out: capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response.DescribeChannelModeratedByAppInstanceUserResponse = capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_chime_sdk_messaging._auth._signers.Signer | None:
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
            sigv4_config = (
                capo_chime_sdk_messaging._auth._sigv4.build_sigv4_auth_scheme(
                    "chime", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_chime_sdk_messaging._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_request.DescribeChannelModeratedByAppInstanceUserRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/channels/{ChannelArn}?scope=app-instance-user-moderated-channel"
    )
    url = url.replace("{ChannelArn}", quote(input_["channel_arn"], safe=""))
    params: list[tuple[str, str]] = []
    if "app_instance_user_arn" in input_:
        params.append(("app-instance-user-arn", input_["app_instance_user_arn"]))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "chime_bearer" in input_:
        headers["x-amz-chime-bearer"] = input_["chime_bearer"]
    body: bytes | None = b""
    signer = (
        None
        if options.anonymous
        else get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    )
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def describe_channel_moderated_by_app_instance_user(
    options: OperationOptions,
    input_: capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_request.DescribeChannelModeratedByAppInstanceUserRequest,
) -> tuple[
    capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response.DescribeChannelModeratedByAppInstanceUserResponse,
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


async def async_describe_channel_moderated_by_app_instance_user(
    options: AsyncOperationOptions,
    input_: capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_request.DescribeChannelModeratedByAppInstanceUserRequest,
) -> tuple[
    capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response.DescribeChannelModeratedByAppInstanceUserResponse,
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
