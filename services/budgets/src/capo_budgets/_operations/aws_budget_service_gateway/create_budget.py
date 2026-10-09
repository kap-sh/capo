"""Generated from Smithy shape ``com.amazonaws.budgets#CreateBudget``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_budgets._auth._signers
import capo_budgets._auth._sigv4
import capo_budgets._protocol.eventstream
import capo_budgets.errors.access_denied_exception
import capo_budgets.errors.billing_view_health_status_exception
import capo_budgets.errors.creation_limit_exceeded_exception
import capo_budgets.errors.duplicate_record_exception
import capo_budgets.errors.internal_error_exception
import capo_budgets.errors.invalid_parameter_exception
import capo_budgets.errors.not_found_exception
import capo_budgets.errors.service_quota_exceeded_exception
import capo_budgets.errors.throttling_exception
import capo_budgets.types.budget
import capo_budgets.types.create_budget_request
import capo_budgets.types.create_budget_response
import capo_budgets.types.notification_with_subscribers_list
import capo_budgets.types.resource_tag_list
from capo_budgets._protocol.errors import parse_error_metadata_json
from capo_budgets._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_budgets._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_budgets.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_budgets.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data, message
            )
        case "BillingViewHealthStatusException":
            raise capo_budgets.errors.billing_view_health_status_exception.BillingViewHealthStatusException.from_aws_json_1_1(
                data, message
            )
        case "CreationLimitExceededException":
            raise capo_budgets.errors.creation_limit_exceeded_exception.CreationLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "DuplicateRecordException":
            raise capo_budgets.errors.duplicate_record_exception.DuplicateRecordException.from_aws_json_1_1(
                data, message
            )
        case "InternalErrorException":
            raise capo_budgets.errors.internal_error_exception.InternalErrorException.from_aws_json_1_1(
                data, message
            )
        case "InvalidParameterException":
            raise capo_budgets.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data, message
            )
        case "NotFoundException":
            raise capo_budgets.errors.not_found_exception.NotFoundException.from_aws_json_1_1(
                data, message
            )
        case "ServiceQuotaExceededException":
            raise capo_budgets.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_aws_json_1_1(
                data, message
            )
        case "ThrottlingException":
            raise capo_budgets.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_budgets.types.create_budget_response.CreateBudgetResponse:
    out: capo_budgets.types.create_budget_response.CreateBudgetResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_budgets.types.create_budget_response.CreateBudgetResponse:
    out: capo_budgets.types.create_budget_response.CreateBudgetResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_budgets._auth._signers.Signer | None:
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
            sigv4_config = capo_budgets._auth._sigv4.build_sigv4_auth_scheme(
                "budgets", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_budgets._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_budgets.types.create_budget_request.CreateBudgetRequest,
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
    headers["X-Amz-Target"] = "AWSBudgetServiceGateway.CreateBudget"
    body: bytes | None = json.dumps(
        capo_budgets.types.create_budget_request.serialize_aws_json_1_1(input_),
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


def create_budget(
    options: OperationOptions,
    input_: capo_budgets.types.create_budget_request.CreateBudgetRequest,
) -> tuple[
    capo_budgets.types.create_budget_response.CreateBudgetResponse, zapros.Response
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


async def async_create_budget(
    options: AsyncOperationOptions,
    input_: capo_budgets.types.create_budget_request.CreateBudgetRequest,
) -> tuple[
    capo_budgets.types.create_budget_response.CreateBudgetResponse, zapros.Response
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
