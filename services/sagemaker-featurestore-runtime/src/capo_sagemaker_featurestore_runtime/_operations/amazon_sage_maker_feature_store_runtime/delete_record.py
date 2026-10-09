"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#DeleteRecord``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_sagemaker_featurestore_runtime._auth._signers
import capo_sagemaker_featurestore_runtime._auth._sigv4
import capo_sagemaker_featurestore_runtime._protocol.eventstream
import capo_sagemaker_featurestore_runtime.errors.access_forbidden
import capo_sagemaker_featurestore_runtime.errors.internal_failure
import capo_sagemaker_featurestore_runtime.errors.service_unavailable
import capo_sagemaker_featurestore_runtime.errors.validation_error
import capo_sagemaker_featurestore_runtime.types.delete_record_request
import capo_sagemaker_featurestore_runtime.types.deletion_mode
import capo_sagemaker_featurestore_runtime.types.target_stores
from capo_sagemaker_featurestore_runtime._protocol.errors import (
    parse_error_metadata_json,
)
from capo_sagemaker_featurestore_runtime._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_sagemaker_featurestore_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_sagemaker_featurestore_runtime.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessForbidden":
            raise capo_sagemaker_featurestore_runtime.errors.access_forbidden.AccessForbidden.from_json(
                data, message
            )
        case "InternalFailure":
            raise capo_sagemaker_featurestore_runtime.errors.internal_failure.InternalFailure.from_json(
                data, message
            )
        case "ServiceUnavailable":
            raise capo_sagemaker_featurestore_runtime.errors.service_unavailable.ServiceUnavailable.from_json(
                data, message
            )
        case "ValidationError":
            raise capo_sagemaker_featurestore_runtime.errors.validation_error.ValidationError.from_json(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_sagemaker_featurestore_runtime._auth._signers.Signer | None:
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
            sigv4_config = capo_sagemaker_featurestore_runtime._auth._sigv4.build_sigv4_auth_scheme(
                "sagemaker", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_sagemaker_featurestore_runtime._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_sagemaker_featurestore_runtime.types.delete_record_request.DeleteRecordRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    import capo_sagemaker_featurestore_runtime.types.deletion_mode
    import capo_sagemaker_featurestore_runtime.types.target_store

    url = endpoint.url.rstrip("/") + "/FeatureGroup/{FeatureGroupName}"
    url = url.replace(
        "{FeatureGroupName}", quote(input_["feature_group_name"], safe="")
    )
    params: list[tuple[str, str]] = []
    if "record_identifier_value_as_string" in input_:
        params.append(
            (
                "RecordIdentifierValueAsString",
                input_["record_identifier_value_as_string"],
            )
        )
    if "event_time" in input_:
        params.append(("EventTime", input_["event_time"]))
    if "target_stores" in input_:
        for item in input_["target_stores"]:
            params.append(
                (
                    "TargetStores",
                    capo_sagemaker_featurestore_runtime.types.target_store.serialize_json(
                        item
                    ),
                )
            )
    if "deletion_mode" in input_:
        params.append(
            (
                "DeletionMode",
                capo_sagemaker_featurestore_runtime.types.deletion_mode.serialize_json(
                    input_["deletion_mode"]
                ),
            )
        )
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
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_record(
    options: OperationOptions,
    input_: capo_sagemaker_featurestore_runtime.types.delete_record_request.DeleteRecordRequest,
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


async def async_delete_record(
    options: AsyncOperationOptions,
    input_: capo_sagemaker_featurestore_runtime.types.delete_record_request.DeleteRecordRequest,
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
