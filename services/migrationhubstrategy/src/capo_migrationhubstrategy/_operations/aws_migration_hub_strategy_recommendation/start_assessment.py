"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#StartAssessment``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_migrationhubstrategy._auth._signers
import capo_migrationhubstrategy._auth._sigv4
import capo_migrationhubstrategy._protocol.eventstream
import capo_migrationhubstrategy.errors.access_denied_exception
import capo_migrationhubstrategy.errors.internal_server_exception
import capo_migrationhubstrategy.errors.service_quota_exceeded_exception
import capo_migrationhubstrategy.errors.throttling_exception
import capo_migrationhubstrategy.types.assessment_targets
import capo_migrationhubstrategy.types.start_assessment_request
import capo_migrationhubstrategy.types.start_assessment_response
from capo_migrationhubstrategy._protocol.errors import parse_error_metadata_json
from capo_migrationhubstrategy._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_migrationhubstrategy._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_migrationhubstrategy.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException.from_json(
                data, message
            )
        case "InternalServerException":
            raise capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException.from_json(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_migrationhubstrategy.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data, message
            )
        case "ThrottlingException":
            raise capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_migrationhubstrategy.types.start_assessment_response.StartAssessmentResponse:
    out: capo_migrationhubstrategy.types.start_assessment_response.StartAssessmentResponse = capo_migrationhubstrategy.types.start_assessment_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_migrationhubstrategy.types.start_assessment_response.StartAssessmentResponse:
    out: capo_migrationhubstrategy.types.start_assessment_response.StartAssessmentResponse = capo_migrationhubstrategy.types.start_assessment_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_migrationhubstrategy._auth._signers.Signer | None:
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
                capo_migrationhubstrategy._auth._sigv4.build_sigv4_auth_scheme(
                    "migrationhub-strategy", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_migrationhubstrategy._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_migrationhubstrategy.types.start_assessment_request.StartAssessmentRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/start-assessment"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_migrationhubstrategy.types.start_assessment_request.serialize_json(input_),
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
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def start_assessment(
    options: OperationOptions,
    input_: capo_migrationhubstrategy.types.start_assessment_request.StartAssessmentRequest,
) -> tuple[
    capo_migrationhubstrategy.types.start_assessment_response.StartAssessmentResponse,
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


async def async_start_assessment(
    options: AsyncOperationOptions,
    input_: capo_migrationhubstrategy.types.start_assessment_request.StartAssessmentRequest,
) -> tuple[
    capo_migrationhubstrategy.types.start_assessment_response.StartAssessmentResponse,
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
