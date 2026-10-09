"""Generated from Smithy shape ``com.amazonaws.s3#GetObjectAnnotation``."""

from __future__ import annotations

from email.utils import parsedate_to_datetime as _parse_http_date
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_s3._auth._signers
import capo_s3._auth._sigv4
import capo_s3._protocol.eventstream
import capo_s3.errors.no_such_annotation
import capo_s3.errors.no_such_bucket
import capo_s3.errors.no_such_key
import capo_s3.types.checksum_mode
import capo_s3.types.checksum_type
import capo_s3.types.get_object_annotation_output
import capo_s3.types.get_object_annotation_request
import capo_s3.types.last_modified
import capo_s3.types.replication_status
import capo_s3.types.request_charged
import capo_s3.types.request_payer
import capo_s3.types.server_side_encryption
import capo_s3.types.streaming_blob
from capo_s3._protocol.errors import find_error_element, parse_error_metadata
from capo_s3._protocol.xml import fromstring
from capo_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_s3.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    body = response.read()
    if not body:
        raise UnknownServiceError(code=None, message=None, response=response)
    root = fromstring(body)
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "NoSuchAnnotation":
            raise capo_s3.errors.no_such_annotation.NoSuchAnnotation.from_xml(
                error_el, message
            )
        case "NoSuchBucket":
            raise capo_s3.errors.no_such_bucket.NoSuchBucket.from_xml(error_el, message)
        case "NoSuchKey":
            raise capo_s3.errors.no_such_key.NoSuchKey.from_xml(error_el, message)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_s3.types.get_object_annotation_output.GetObjectAnnotationOutput:
    _iter = cast(Any, response.iter_raw())
    out: capo_s3.types.get_object_annotation_output.GetObjectAnnotationOutput = {
        "annotation_payload": _iter
    }  # type: ignore[reportAssignmentType]
    if "x-amz-object-version-id" in response.headers:
        out["object_version_id"] = response.headers["x-amz-object-version-id"]
    if "Last-Modified" in response.headers:
        out["last_modified"] = _parse_http_date(response.headers["Last-Modified"])
    if "Content-Length" in response.headers:
        out["content_length"] = int(response.headers["Content-Length"])
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    if "x-amz-checksum-crc32" in response.headers:
        out["checksum_crc32"] = response.headers["x-amz-checksum-crc32"]
    if "x-amz-checksum-crc32c" in response.headers:
        out["checksum_crc32_c"] = response.headers["x-amz-checksum-crc32c"]
    if "x-amz-checksum-crc64nvme" in response.headers:
        out["checksum_crc64_nvme"] = response.headers["x-amz-checksum-crc64nvme"]
    if "x-amz-checksum-sha1" in response.headers:
        out["checksum_sha1"] = response.headers["x-amz-checksum-sha1"]
    if "x-amz-checksum-sha256" in response.headers:
        out["checksum_sha256"] = response.headers["x-amz-checksum-sha256"]
    if "x-amz-checksum-sha512" in response.headers:
        out["checksum_sha512"] = response.headers["x-amz-checksum-sha512"]
    if "x-amz-checksum-md5" in response.headers:
        out["checksum_md5"] = response.headers["x-amz-checksum-md5"]
    if "x-amz-checksum-xxhash64" in response.headers:
        out["checksum_xxhash64"] = response.headers["x-amz-checksum-xxhash64"]
    if "x-amz-checksum-xxhash3" in response.headers:
        out["checksum_xxhash3"] = response.headers["x-amz-checksum-xxhash3"]
    if "x-amz-checksum-xxhash128" in response.headers:
        out["checksum_xxhash128"] = response.headers["x-amz-checksum-xxhash128"]
    if "x-amz-checksum-type" in response.headers:
        out["checksum_type"] = capo_s3.types.checksum_type.from_xml_text(
            response.headers["x-amz-checksum-type"]
        )
    if "x-amz-server-side-encryption" in response.headers:
        out["server_side_encryption"] = (
            capo_s3.types.server_side_encryption.from_xml_text(
                response.headers["x-amz-server-side-encryption"]
            )
        )
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = capo_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    if "x-amz-replication-status" in response.headers:
        out["replication_status"] = capo_s3.types.replication_status.from_xml_text(
            response.headers["x-amz-replication-status"]
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3.types.get_object_annotation_output.GetObjectAnnotationOutput:
    _iter = cast(Any, response.async_iter_raw())
    out: capo_s3.types.get_object_annotation_output.GetObjectAnnotationOutput = {
        "annotation_payload": _iter
    }  # type: ignore[reportAssignmentType]
    if "x-amz-object-version-id" in response.headers:
        out["object_version_id"] = response.headers["x-amz-object-version-id"]
    if "Last-Modified" in response.headers:
        out["last_modified"] = _parse_http_date(response.headers["Last-Modified"])
    if "Content-Length" in response.headers:
        out["content_length"] = int(response.headers["Content-Length"])
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    if "x-amz-checksum-crc32" in response.headers:
        out["checksum_crc32"] = response.headers["x-amz-checksum-crc32"]
    if "x-amz-checksum-crc32c" in response.headers:
        out["checksum_crc32_c"] = response.headers["x-amz-checksum-crc32c"]
    if "x-amz-checksum-crc64nvme" in response.headers:
        out["checksum_crc64_nvme"] = response.headers["x-amz-checksum-crc64nvme"]
    if "x-amz-checksum-sha1" in response.headers:
        out["checksum_sha1"] = response.headers["x-amz-checksum-sha1"]
    if "x-amz-checksum-sha256" in response.headers:
        out["checksum_sha256"] = response.headers["x-amz-checksum-sha256"]
    if "x-amz-checksum-sha512" in response.headers:
        out["checksum_sha512"] = response.headers["x-amz-checksum-sha512"]
    if "x-amz-checksum-md5" in response.headers:
        out["checksum_md5"] = response.headers["x-amz-checksum-md5"]
    if "x-amz-checksum-xxhash64" in response.headers:
        out["checksum_xxhash64"] = response.headers["x-amz-checksum-xxhash64"]
    if "x-amz-checksum-xxhash3" in response.headers:
        out["checksum_xxhash3"] = response.headers["x-amz-checksum-xxhash3"]
    if "x-amz-checksum-xxhash128" in response.headers:
        out["checksum_xxhash128"] = response.headers["x-amz-checksum-xxhash128"]
    if "x-amz-checksum-type" in response.headers:
        out["checksum_type"] = capo_s3.types.checksum_type.from_xml_text(
            response.headers["x-amz-checksum-type"]
        )
    if "x-amz-server-side-encryption" in response.headers:
        out["server_side_encryption"] = (
            capo_s3.types.server_side_encryption.from_xml_text(
                response.headers["x-amz-server-side-encryption"]
            )
        )
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = capo_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    if "x-amz-replication-status" in response.headers:
        out["replication_status"] = capo_s3.types.replication_status.from_xml_text(
            response.headers["x-amz-replication-status"]
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


RESPONSE_CHECKSUM_ALGORITHMS = (
    "CRC64NVME",
    "CRC32",
    "CRC32C",
    "SHA256",
    "SHA1",
    "SHA512",
    "MD5",
    "XXHASH64",
    "XXHASH3",
    "XXHASH128",
)


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_s3.types.get_object_annotation_request.GetObjectAnnotationRequest,
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
    import capo_s3.types.checksum_mode
    import capo_s3.types.request_payer

    url = endpoint.url.rstrip("/") + "/{Key+}?annotation&x-id=GetObjectAnnotation"
    url = url.replace("{Key+}", quote(input_["key"], safe="/"))
    params: list[tuple[str, str]] = []
    if "annotation_name" in input_:
        params.append(("annotationName", input_["annotation_name"]))
    if "version_id" in input_:
        params.append(("versionId", input_["version_id"]))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "request_payer" in input_:
        headers["x-amz-request-payer"] = capo_s3.types.request_payer.to_xml_text(
            input_["request_payer"]
        )
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = input_["expected_bucket_owner"]
    if "checksum_mode" in input_:
        headers["x-amz-checksum-mode"] = capo_s3.types.checksum_mode.to_xml_text(
            input_["checksum_mode"]
        )
    body: bytes | None = b""
    signer = (
        None
        if options.anonymous
        else get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    )
    context: zapros.RequestContext = {"signer": signer}
    if input_.get("checksum_mode") == "ENABLED":
        context["checksum_algorithms"] = RESPONSE_CHECKSUM_ALGORITHMS
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context=context
    )


def get_object_annotation(
    options: OperationOptions,
    input_: capo_s3.types.get_object_annotation_request.GetObjectAnnotationRequest,
) -> tuple[
    capo_s3.types.get_object_annotation_output.GetObjectAnnotationOutput,
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


async def async_get_object_annotation(
    options: AsyncOperationOptions,
    input_: capo_s3.types.get_object_annotation_request.GetObjectAnnotationRequest,
) -> tuple[
    capo_s3.types.get_object_annotation_output.GetObjectAnnotationOutput,
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
