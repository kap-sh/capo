"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpdateElasticsearchDomainConfig``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_elasticsearch_service._auth._signers
import capo_elasticsearch_service._auth._sigv4
import capo_elasticsearch_service._protocol.eventstream
import capo_elasticsearch_service.errors.base_exception
import capo_elasticsearch_service.errors.internal_exception
import capo_elasticsearch_service.errors.invalid_type_exception
import capo_elasticsearch_service.errors.limit_exceeded_exception
import capo_elasticsearch_service.errors.resource_not_found_exception
import capo_elasticsearch_service.errors.validation_exception
import capo_elasticsearch_service.types.advanced_options
import capo_elasticsearch_service.types.advanced_security_options_input
import capo_elasticsearch_service.types.auto_tune_options
import capo_elasticsearch_service.types.automated_snapshot_pause_request_options
import capo_elasticsearch_service.types.cognito_options
import capo_elasticsearch_service.types.deployment_strategy_options
import capo_elasticsearch_service.types.domain_endpoint_options
import capo_elasticsearch_service.types.domain_engine_mode
import capo_elasticsearch_service.types.domain_use_case
import capo_elasticsearch_service.types.dry_run_results
import capo_elasticsearch_service.types.ebs_options
import capo_elasticsearch_service.types.elasticsearch_cluster_config
import capo_elasticsearch_service.types.elasticsearch_domain_config
import capo_elasticsearch_service.types.encryption_at_rest_options
import capo_elasticsearch_service.types.log_publishing_options
import capo_elasticsearch_service.types.node_to_node_encryption_options
import capo_elasticsearch_service.types.snapshot_options
import capo_elasticsearch_service.types.update_elasticsearch_domain_config_request
import capo_elasticsearch_service.types.update_elasticsearch_domain_config_response
import capo_elasticsearch_service.types.vpc_options
from capo_elasticsearch_service._protocol.errors import parse_error_metadata_json
from capo_elasticsearch_service._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_elasticsearch_service._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_elasticsearch_service.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BaseException":
            raise capo_elasticsearch_service.errors.base_exception.BaseException.from_json(
                data, message
            )
        case "InternalException":
            raise capo_elasticsearch_service.errors.internal_exception.InternalException.from_json(
                data, message
            )
        case "InvalidTypeException":
            raise capo_elasticsearch_service.errors.invalid_type_exception.InvalidTypeException.from_json(
                data, message
            )
        case "LimitExceededException":
            raise capo_elasticsearch_service.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data, message
            )
        case "ResourceNotFoundException":
            raise capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data, message
            )
        case "ValidationException":
            raise capo_elasticsearch_service.errors.validation_exception.ValidationException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_elasticsearch_service.types.update_elasticsearch_domain_config_response.UpdateElasticsearchDomainConfigResponse:
    out: capo_elasticsearch_service.types.update_elasticsearch_domain_config_response.UpdateElasticsearchDomainConfigResponse = capo_elasticsearch_service.types.update_elasticsearch_domain_config_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_elasticsearch_service.types.update_elasticsearch_domain_config_response.UpdateElasticsearchDomainConfigResponse:
    out: capo_elasticsearch_service.types.update_elasticsearch_domain_config_response.UpdateElasticsearchDomainConfigResponse = capo_elasticsearch_service.types.update_elasticsearch_domain_config_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_elasticsearch_service._auth._signers.Signer | None:
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
                capo_elasticsearch_service._auth._sigv4.build_sigv4_auth_scheme(
                    "es", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_elasticsearch_service._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_elasticsearch_service.types.update_elasticsearch_domain_config_request.UpdateElasticsearchDomainConfigRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2015-01-01/es/domain/{DomainName}/config"
    url = url.replace("{DomainName}", quote(input_["domain_name"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_elasticsearch_service.types.update_elasticsearch_domain_config_request.serialize_json(
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
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def update_elasticsearch_domain_config(
    options: OperationOptions,
    input_: capo_elasticsearch_service.types.update_elasticsearch_domain_config_request.UpdateElasticsearchDomainConfigRequest,
) -> tuple[
    capo_elasticsearch_service.types.update_elasticsearch_domain_config_response.UpdateElasticsearchDomainConfigResponse,
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


async def async_update_elasticsearch_domain_config(
    options: AsyncOperationOptions,
    input_: capo_elasticsearch_service.types.update_elasticsearch_domain_config_request.UpdateElasticsearchDomainConfigRequest,
) -> tuple[
    capo_elasticsearch_service.types.update_elasticsearch_domain_config_response.UpdateElasticsearchDomainConfigResponse,
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
