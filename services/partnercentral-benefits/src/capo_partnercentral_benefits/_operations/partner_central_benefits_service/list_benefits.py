"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ListBenefits``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_partnercentral_benefits._auth._signers
import capo_partnercentral_benefits._auth._sigv4
import capo_partnercentral_benefits._protocol.eventstream
import capo_partnercentral_benefits.errors.access_denied_exception
import capo_partnercentral_benefits.errors.internal_server_exception
import capo_partnercentral_benefits.errors.resource_not_found_exception
import capo_partnercentral_benefits.errors.throttling_exception
import capo_partnercentral_benefits.errors.validation_exception
import capo_partnercentral_benefits.types.benefit_statuses
import capo_partnercentral_benefits.types.benefit_summaries
import capo_partnercentral_benefits.types.fulfillment_types
import capo_partnercentral_benefits.types.list_benefits_input
import capo_partnercentral_benefits.types.list_benefits_output
import capo_partnercentral_benefits.types.programs
from capo_partnercentral_benefits._protocol.errors import parse_error_metadata_json
from capo_partnercentral_benefits._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_partnercentral_benefits._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_partnercentral_benefits.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_partnercentral_benefits.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_0(
                data, message
            )
        case "InternalServerException":
            raise capo_partnercentral_benefits.errors.internal_server_exception.InternalServerException.from_aws_json_1_0(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_partnercentral_benefits.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data, message
            )
        case "ThrottlingException":
            raise capo_partnercentral_benefits.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data, message
            )
        case "ValidationException":
            raise capo_partnercentral_benefits.errors.validation_exception.ValidationException.from_aws_json_1_0(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_partnercentral_benefits.types.list_benefits_output.ListBenefitsOutput:
    out: capo_partnercentral_benefits.types.list_benefits_output.ListBenefitsOutput = capo_partnercentral_benefits.types.list_benefits_output.deserialize_aws_json_1_0(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_partnercentral_benefits.types.list_benefits_output.ListBenefitsOutput:
    out: capo_partnercentral_benefits.types.list_benefits_output.ListBenefitsOutput = capo_partnercentral_benefits.types.list_benefits_output.deserialize_aws_json_1_0(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_partnercentral_benefits._auth._signers.Signer | None:
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
                capo_partnercentral_benefits._auth._sigv4.build_sigv4_auth_scheme(
                    "partnercentral-benefits", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_partnercentral_benefits._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_partnercentral_benefits.types.list_benefits_input.ListBenefitsInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/ListBenefits"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "PartnerCentralBenefitsService.ListBenefits"
    body: bytes | None = json.dumps(
        capo_partnercentral_benefits.types.list_benefits_input.serialize_aws_json_1_0(
            input_
        ),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
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


def list_benefits(
    options: OperationOptions,
    input_: capo_partnercentral_benefits.types.list_benefits_input.ListBenefitsInput,
) -> tuple[
    capo_partnercentral_benefits.types.list_benefits_output.ListBenefitsOutput,
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


async def async_list_benefits(
    options: AsyncOperationOptions,
    input_: capo_partnercentral_benefits.types.list_benefits_input.ListBenefitsInput,
) -> tuple[
    capo_partnercentral_benefits.types.list_benefits_output.ListBenefitsOutput,
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
