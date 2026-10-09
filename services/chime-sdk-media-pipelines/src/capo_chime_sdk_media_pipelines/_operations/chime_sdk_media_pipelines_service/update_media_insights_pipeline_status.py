"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#UpdateMediaInsightsPipelineStatus``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_chime_sdk_media_pipelines._auth._signers
import capo_chime_sdk_media_pipelines._auth._sigv4
import capo_chime_sdk_media_pipelines._protocol.eventstream
import capo_chime_sdk_media_pipelines.errors.bad_request_exception
import capo_chime_sdk_media_pipelines.errors.conflict_exception
import capo_chime_sdk_media_pipelines.errors.forbidden_exception
import capo_chime_sdk_media_pipelines.errors.not_found_exception
import capo_chime_sdk_media_pipelines.errors.service_failure_exception
import capo_chime_sdk_media_pipelines.errors.service_unavailable_exception
import capo_chime_sdk_media_pipelines.errors.throttled_client_exception
import capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception
import capo_chime_sdk_media_pipelines.types.media_pipeline_status_update
import capo_chime_sdk_media_pipelines.types.update_media_insights_pipeline_status_request
from capo_chime_sdk_media_pipelines._protocol.errors import parse_error_metadata_json
from capo_chime_sdk_media_pipelines._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_chime_sdk_media_pipelines._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_chime_sdk_media_pipelines.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException.from_json(
                data, message
            )
        case "ConflictException":
            raise capo_chime_sdk_media_pipelines.errors.conflict_exception.ConflictException.from_json(
                data, message
            )
        case "ForbiddenException":
            raise capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException.from_json(
                data, message
            )
        case "NotFoundException":
            raise capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException.from_json(
                data, message
            )
        case "ServiceFailureException":
            raise capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException.from_json(
                data, message
            )
        case "ServiceUnavailableException":
            raise capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data, message
            )
        case "ThrottledClientException":
            raise capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException.from_json(
                data, message
            )
        case "UnauthorizedClientException":
            raise capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_chime_sdk_media_pipelines._auth._signers.Signer | None:
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
                capo_chime_sdk_media_pipelines._auth._sigv4.build_sigv4_auth_scheme(
                    "chime", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_chime_sdk_media_pipelines._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_chime_sdk_media_pipelines.types.update_media_insights_pipeline_status_request.UpdateMediaInsightsPipelineStatusRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/media-insights-pipeline-status/{Identifier}"
    url = url.replace("{Identifier}", quote(input_["identifier"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_chime_sdk_media_pipelines.types.update_media_insights_pipeline_status_request.serialize_json(
            input_
        ),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/json"
    signer = (
        None
        if options.anonymous
        else get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    )
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def update_media_insights_pipeline_status(
    options: OperationOptions,
    input_: capo_chime_sdk_media_pipelines.types.update_media_insights_pipeline_status_request.UpdateMediaInsightsPipelineStatusRequest,
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


async def async_update_media_insights_pipeline_status(
    options: AsyncOperationOptions,
    input_: capo_chime_sdk_media_pipelines.types.update_media_insights_pipeline_status_request.UpdateMediaInsightsPipelineStatusRequest,
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
