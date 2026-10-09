"""Generated from Smithy shape ``com.amazonaws.iotdataplane#Publish``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_iot_data_plane._auth._signers
import capo_iot_data_plane._auth._sigv4
import capo_iot_data_plane._protocol.eventstream
import capo_iot_data_plane.errors.internal_failure_exception
import capo_iot_data_plane.errors.invalid_request_exception
import capo_iot_data_plane.errors.method_not_allowed_exception
import capo_iot_data_plane.errors.throttling_exception
import capo_iot_data_plane.errors.unauthorized_exception
import capo_iot_data_plane.types.payload
import capo_iot_data_plane.types.payload_format_indicator
import capo_iot_data_plane.types.publish_request
from capo_iot_data_plane._protocol.errors import parse_error_metadata_json
from capo_iot_data_plane._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_iot_data_plane._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_iot_data_plane.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalFailureException":
            raise capo_iot_data_plane.errors.internal_failure_exception.InternalFailureException.from_json(
                data, message
            )
        case "InvalidRequestException":
            raise capo_iot_data_plane.errors.invalid_request_exception.InvalidRequestException.from_json(
                data, message
            )
        case "MethodNotAllowedException":
            raise capo_iot_data_plane.errors.method_not_allowed_exception.MethodNotAllowedException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_iot_data_plane.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case "UnauthorizedException":
            raise capo_iot_data_plane.errors.unauthorized_exception.UnauthorizedException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_iot_data_plane._auth._signers.Signer | None:
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
            sigv4_config = capo_iot_data_plane._auth._sigv4.build_sigv4_auth_scheme(
                "iotdata", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_iot_data_plane._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_iot_data_plane.types.publish_request.PublishRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_iot_data_plane.types.payload_format_indicator

    url = endpoint.url.rstrip("/") + "/topics/{topic}"
    url = url.replace("{topic}", quote(input_["topic"], safe=""))
    params: list[tuple[str, str]] = []
    params.append(("qos", str(input_.get("qos", 0))))
    params.append(("retain", "true" if input_.get("retain", False) else "false"))
    if "content_type" in input_:
        params.append(("contentType", input_["content_type"]))
    if "response_topic" in input_:
        params.append(("responseTopic", input_["response_topic"]))
    params.append(("messageExpiry", str(input_.get("message_expiry", 0))))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "user_properties" in input_:
        headers["x-amz-mqtt5-user-properties"] = input_["user_properties"]
    if "payload_format_indicator" in input_:
        headers["x-amz-mqtt5-payload-format-indicator"] = (
            capo_iot_data_plane.types.payload_format_indicator.serialize_json(
                input_["payload_format_indicator"]
            )
        )
    if "correlation_data" in input_:
        headers["x-amz-mqtt5-correlation-data"] = input_["correlation_data"]
    if "payload" in input_:
        body: bytes | None = input_["payload"]
        headers["content-type"] = "application/octet-stream"
    else:
        body = b""
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


def publish(
    options: OperationOptions,
    input_: capo_iot_data_plane.types.publish_request.PublishRequest,
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


async def async_publish(
    options: AsyncOperationOptions,
    input_: capo_iot_data_plane.types.publish_request.PublishRequest,
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
