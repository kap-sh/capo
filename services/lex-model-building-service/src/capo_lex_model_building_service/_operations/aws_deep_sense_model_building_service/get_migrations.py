"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetMigrations``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_lex_model_building_service._auth._signers
import capo_lex_model_building_service._auth._sigv4
import capo_lex_model_building_service._protocol.eventstream
import capo_lex_model_building_service.errors.bad_request_exception
import capo_lex_model_building_service.errors.internal_failure_exception
import capo_lex_model_building_service.errors.limit_exceeded_exception
import capo_lex_model_building_service.types.get_migrations_request
import capo_lex_model_building_service.types.get_migrations_response
import capo_lex_model_building_service.types.migration_sort_attribute
import capo_lex_model_building_service.types.migration_status
import capo_lex_model_building_service.types.migration_summary_list
import capo_lex_model_building_service.types.sort_order
from capo_lex_model_building_service._protocol.errors import parse_error_metadata_json
from capo_lex_model_building_service._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_lex_model_building_service._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_lex_model_building_service.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise capo_lex_model_building_service.errors.bad_request_exception.BadRequestException.from_json(
                data, message
            )
        case "InternalFailureException":
            raise capo_lex_model_building_service.errors.internal_failure_exception.InternalFailureException.from_json(
                data, message
            )
        case "LimitExceededException":
            raise capo_lex_model_building_service.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    capo_lex_model_building_service.types.get_migrations_response.GetMigrationsResponse
):
    out: capo_lex_model_building_service.types.get_migrations_response.GetMigrationsResponse = capo_lex_model_building_service.types.get_migrations_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    capo_lex_model_building_service.types.get_migrations_response.GetMigrationsResponse
):
    out: capo_lex_model_building_service.types.get_migrations_response.GetMigrationsResponse = capo_lex_model_building_service.types.get_migrations_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_lex_model_building_service._auth._signers.Signer | None:
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
                capo_lex_model_building_service._auth._sigv4.build_sigv4_auth_scheme(
                    "lex", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_lex_model_building_service._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_lex_model_building_service.types.get_migrations_request.GetMigrationsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_lex_model_building_service.types.migration_sort_attribute
    import capo_lex_model_building_service.types.migration_status
    import capo_lex_model_building_service.types.sort_order

    url = endpoint.url.rstrip("/") + "/migrations"
    params: list[tuple[str, str]] = []
    if "sort_by_attribute" in input_:
        params.append(
            (
                "sortByAttribute",
                capo_lex_model_building_service.types.migration_sort_attribute.serialize_json(
                    input_["sort_by_attribute"]
                ),
            )
        )
    if "sort_by_order" in input_:
        params.append(
            (
                "sortByOrder",
                capo_lex_model_building_service.types.sort_order.serialize_json(
                    input_["sort_by_order"]
                ),
            )
        )
    if "v1_bot_name_contains" in input_:
        params.append(("v1BotNameContains", input_["v1_bot_name_contains"]))
    if "migration_status_equals" in input_:
        params.append(
            (
                "migrationStatusEquals",
                capo_lex_model_building_service.types.migration_status.serialize_json(
                    input_["migration_status_equals"]
                ),
            )
        )
    if "max_results" in input_:
        params.append(("maxResults", str(input_["max_results"])))
    if "next_token" in input_:
        params.append(("nextToken", input_["next_token"]))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
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


def get_migrations(
    options: OperationOptions,
    input_: capo_lex_model_building_service.types.get_migrations_request.GetMigrationsRequest,
) -> tuple[
    capo_lex_model_building_service.types.get_migrations_response.GetMigrationsResponse,
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


async def async_get_migrations(
    options: AsyncOperationOptions,
    input_: capo_lex_model_building_service.types.get_migrations_request.GetMigrationsRequest,
) -> tuple[
    capo_lex_model_building_service.types.get_migrations_response.GetMigrationsResponse,
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
