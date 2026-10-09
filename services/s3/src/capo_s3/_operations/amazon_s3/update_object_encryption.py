"""Generated from Smithy shape ``com.amazonaws.s3#UpdateObjectEncryption``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_s3._auth._signers
import capo_s3._auth._sigv4
import capo_s3._checksums
import capo_s3._protocol.eventstream
import capo_s3.errors.access_denied
import capo_s3.errors.invalid_request
import capo_s3.errors.no_such_key
import capo_s3.types.checksum_algorithm
import capo_s3.types.object_encryption
import capo_s3.types.request_charged
import capo_s3.types.request_payer
import capo_s3.types.update_object_encryption_request
import capo_s3.types.update_object_encryption_response
from capo_s3._protocol.errors import find_error_element, parse_error_metadata
from capo_s3._protocol.xml import Element, fromstring, tostring
from capo_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_s3.errors import UnknownServiceError

STATUS_CODE_TO_CODE = {400: "InvalidRequest", 403: "AccessDenied", 404: "NoSuchKey"}


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
        case "AccessDenied":
            raise capo_s3.errors.access_denied.AccessDenied.from_xml(error_el, message)
        case "InvalidRequest":
            raise capo_s3.errors.invalid_request.InvalidRequest.from_xml(
                error_el, message
            )
        case "NoSuchKey":
            raise capo_s3.errors.no_such_key.NoSuchKey.from_xml(error_el, message)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_s3.types.update_object_encryption_response.UpdateObjectEncryptionResponse:
    out: capo_s3.types.update_object_encryption_response.UpdateObjectEncryptionResponse = {}  # type: ignore[typeddict-item]
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = capo_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3.types.update_object_encryption_response.UpdateObjectEncryptionResponse:
    out: capo_s3.types.update_object_encryption_response.UpdateObjectEncryptionResponse = {}  # type: ignore[typeddict-item]
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = capo_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
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
    input_: capo_s3.types.update_object_encryption_request.UpdateObjectEncryptionRequest,
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
            Key=options.key,
            Prefix=options.prefix,
            CopySource=options.copy_source,
            DisableAccessPoints=options.disable_access_points,
            DisableMultiRegionAccessPoints=options.disable_multi_region_access_points,
            UseArnRegion=options.use_arn_region,
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
            DisableS3ExpressSessionAuth=options.disable_s3_express_session_auth,
        )
    )  # noqa: F841
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.request_payer

    url = endpoint.url.rstrip("/") + "/{Key+}?encryption"
    url = url.replace("{Key+}", quote(input_["key"], safe="/"))
    params: list[tuple[str, str]] = []
    if "version_id" in input_:
        params.append(("versionId", input_["version_id"]))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "request_payer" in input_:
        headers["x-amz-request-payer"] = capo_s3.types.request_payer.to_xml_text(
            input_["request_payer"]
        )
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = input_["expected_bucket_owner"]
    if "content_md5" in input_:
        headers["Content-MD5"] = input_["content_md5"]
    if "checksum_algorithm" in input_:
        headers["x-amz-sdk-checksum-algorithm"] = (
            capo_s3.types.checksum_algorithm.to_xml_text(input_["checksum_algorithm"])
        )
    payload_root = Element("_")
    capo_s3.types.object_encryption.serialize_xml(
        input_["object_encryption"], payload_root, "ObjectEncryption"
    )
    body: bytes | None = tostring(payload_root[0])
    headers["content-type"] = "application/xml"
    capo_s3._checksums.set_request_checksum(
        headers, body, input_.get("checksum_algorithm")
    )
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


def update_object_encryption(
    options: OperationOptions,
    input_: capo_s3.types.update_object_encryption_request.UpdateObjectEncryptionRequest,
) -> tuple[
    capo_s3.types.update_object_encryption_response.UpdateObjectEncryptionResponse,
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


async def async_update_object_encryption(
    options: AsyncOperationOptions,
    input_: capo_s3.types.update_object_encryption_request.UpdateObjectEncryptionRequest,
) -> tuple[
    capo_s3.types.update_object_encryption_response.UpdateObjectEncryptionResponse,
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
