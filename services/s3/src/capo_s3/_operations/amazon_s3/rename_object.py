"""Generated from Smithy shape ``com.amazonaws.s3#RenameObject``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_s3._auth._signers
import capo_s3._auth._sigv4
import capo_s3._protocol.eventstream
import capo_s3.errors.idempotency_parameter_mismatch
import capo_s3.types.if_modified_since
import capo_s3.types.if_unmodified_since
import capo_s3.types.rename_object_output
import capo_s3.types.rename_object_request
import capo_s3.types.rename_source_if_modified_since
import capo_s3.types.rename_source_if_unmodified_since
from capo_s3._protocol.errors import find_error_element, parse_error_metadata
from capo_s3._protocol.xml import Element, fromstring
from capo_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_s3.errors import UnknownServiceError

STATUS_CODE_TO_CODE = {400: "IdempotencyParameterMismatch"}


def handle_error(response: zapros.Response) -> Never:
    body = response.read()
    if body:
        root = fromstring(body)
        code, message = parse_error_metadata(root)
        error_el = find_error_element(root)
    else:
        code = STATUS_CODE_TO_CODE.get(response.status)
        message = None
        error_el = Element("Error")
    match code:
        case "IdempotencyParameterMismatch":
            raise capo_s3.errors.idempotency_parameter_mismatch.IdempotencyParameterMismatch.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_s3.types.rename_object_output.RenameObjectOutput:
    out: capo_s3.types.rename_object_output.RenameObjectOutput = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3.types.rename_object_output.RenameObjectOutput:
    out: capo_s3.types.rename_object_output.RenameObjectOutput = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_s3._auth._signers.Signer | None:
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
            sigv4_config = capo_s3._auth._sigv4.build_sigv4_auth_scheme(
                "s3", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_s3._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_s3.types.rename_object_request.RenameObjectRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Bucket=input_.get("bucket"),
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
            ForcePathStyle=options.force_path_style,
            Accelerate=options.accelerate,
            UseGlobalEndpoint=options.use_global_endpoint,
            UseObjectLambdaEndpoint=options.use_object_lambda_endpoint,
            Key=input_.get("key"),
            Prefix=options.prefix,
            CopySource=options.copy_source,
            DisableAccessPoints=options.disable_access_points,
            DisableMultiRegionAccessPoints=options.disable_multi_region_access_points,
            UseArnRegion=options.use_arn_region,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
            DisableS3ExpressSessionAuth=options.disable_s3_express_session_auth,
        )
    )  # noqa: F841
    import capo_s3._protocol.serialize

    url = endpoint.url.rstrip("/") + "/{Key+}?renameObject"
    url = url.replace("{Key+}", quote(input_["key"], safe="/"))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "rename_source" in input_:
        headers["x-amz-rename-source"] = input_["rename_source"]
    if "destination_if_match" in input_:
        headers["If-Match"] = input_["destination_if_match"]
    if "destination_if_none_match" in input_:
        headers["If-None-Match"] = input_["destination_if_none_match"]
    if "destination_if_modified_since" in input_:
        headers["If-Modified-Since"] = capo_s3._protocol.serialize.fmt_http_date(
            input_["destination_if_modified_since"]
        )
    if "destination_if_unmodified_since" in input_:
        headers["If-Unmodified-Since"] = capo_s3._protocol.serialize.fmt_http_date(
            input_["destination_if_unmodified_since"]
        )
    if "source_if_match" in input_:
        headers["x-amz-rename-source-if-match"] = input_["source_if_match"]
    if "source_if_none_match" in input_:
        headers["x-amz-rename-source-if-none-match"] = input_["source_if_none_match"]
    if "source_if_modified_since" in input_:
        headers["x-amz-rename-source-if-modified-since"] = (
            capo_s3._protocol.serialize.fmt_http_date(
                input_["source_if_modified_since"]
            )
        )
    if "source_if_unmodified_since" in input_:
        headers["x-amz-rename-source-if-unmodified-since"] = (
            capo_s3._protocol.serialize.fmt_http_date(
                input_["source_if_unmodified_since"]
            )
        )
    if "client_token" in input_:
        headers["x-amz-client-token"] = input_["client_token"]
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
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def rename_object(
    options: OperationOptions,
    input_: capo_s3.types.rename_object_request.RenameObjectRequest,
) -> tuple[capo_s3.types.rename_object_output.RenameObjectOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            raise_error(response, handle_error)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_rename_object(
    options: AsyncOperationOptions,
    input_: capo_s3.types.rename_object_request.RenameObjectRequest,
) -> tuple[capo_s3.types.rename_object_output.RenameObjectOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 300:
            await response.aread()
            raise_error(response, handle_error)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
