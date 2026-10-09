"""Generated from Smithy shape ``com.amazonaws.cognitosync#ListRecords``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_cognito_sync._auth._signers
import capo_cognito_sync._auth._sigv4
import capo_cognito_sync._protocol.eventstream
import capo_cognito_sync.errors.internal_error_exception
import capo_cognito_sync.errors.invalid_parameter_exception
import capo_cognito_sync.errors.not_authorized_exception
import capo_cognito_sync.errors.too_many_requests_exception
import capo_cognito_sync.types.list_records_request
import capo_cognito_sync.types.list_records_response
import capo_cognito_sync.types.merged_dataset_name_list
import capo_cognito_sync.types.record_list
from capo_cognito_sync._protocol.errors import parse_error_metadata_json
from capo_cognito_sync._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cognito_sync._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cognito_sync.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalErrorException":
            raise capo_cognito_sync.errors.internal_error_exception.InternalErrorException.from_json(
                data, message
            )
        case "InvalidParameterException":
            raise capo_cognito_sync.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data, message
            )
        case "NotAuthorizedException":
            raise capo_cognito_sync.errors.not_authorized_exception.NotAuthorizedException.from_json(
                data, message
            )
        case "TooManyRequestsException":
            raise capo_cognito_sync.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cognito_sync.types.list_records_response.ListRecordsResponse:
    out: capo_cognito_sync.types.list_records_response.ListRecordsResponse = (
        capo_cognito_sync.types.list_records_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cognito_sync.types.list_records_response.ListRecordsResponse:
    out: capo_cognito_sync.types.list_records_response.ListRecordsResponse = (
        capo_cognito_sync.types.list_records_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cognito_sync._auth._signers.Signer | None:
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
            sigv4_config = capo_cognito_sync._auth._sigv4.build_sigv4_auth_scheme(
                "cognito-sync", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_cognito_sync._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cognito_sync.types.list_records_request.ListRecordsRequest,
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
        + "/identitypools/{IdentityPoolId}/identities/{IdentityId}/datasets/{DatasetName}/records"
    )
    url = url.replace("{IdentityPoolId}", quote(input_["identity_pool_id"], safe=""))
    url = url.replace("{IdentityId}", quote(input_["identity_id"], safe=""))
    url = url.replace("{DatasetName}", quote(input_["dataset_name"], safe=""))
    params: list[tuple[str, str]] = []
    if "last_sync_count" in input_:
        params.append(("lastSyncCount", str(input_["last_sync_count"])))
    if "next_token" in input_:
        params.append(("nextToken", input_["next_token"]))
    if "max_results" in input_:
        params.append(("maxResults", str(input_["max_results"])))
    if "sync_session_token" in input_:
        params.append(("syncSessionToken", input_["sync_session_token"]))
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


def list_records(
    options: OperationOptions,
    input_: capo_cognito_sync.types.list_records_request.ListRecordsRequest,
) -> tuple[
    capo_cognito_sync.types.list_records_response.ListRecordsResponse, zapros.Response
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


async def async_list_records(
    options: AsyncOperationOptions,
    input_: capo_cognito_sync.types.list_records_request.ListRecordsRequest,
) -> tuple[
    capo_cognito_sync.types.list_records_response.ListRecordsResponse, zapros.Response
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
