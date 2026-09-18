"""Generated from Smithy shape ``com.amazonaws.s3#PutObjectAnnotation``."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_s3._auth._signers
import capo_s3._auth._sigv4
import capo_s3._body
import capo_s3._checksums
import capo_s3._protocol.eventstream
import capo_s3.errors.annotation_limit_exceeded
import capo_s3.errors.annotation_name_too_long
import capo_s3.errors.invalid_annotation_name
import capo_s3.errors.invalid_request
import capo_s3.errors.no_such_bucket
import capo_s3.errors.no_such_key
import capo_s3.errors.unsupported_media_type
import capo_s3.types.checksum_algorithm
import capo_s3.types.checksum_type
import capo_s3.types.put_object_annotation_output
import capo_s3.types.put_object_annotation_request
import capo_s3.types.request_charged
import capo_s3.types.request_payer
import capo_s3.types.server_side_encryption
import capo_s3.types.streaming_blob
from capo_s3._protocol.errors import find_error_element, parse_error_metadata
from capo_s3._protocol.xml import Element, fromstring
from capo_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_s3.errors import UnknownServiceError

STATUS_CODE_TO_CODE = {415: "UnsupportedMediaType"}


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
        case "AnnotationLimitExceeded":
            raise capo_s3.errors.annotation_limit_exceeded.AnnotationLimitExceeded.from_xml(
                error_el, message
            )
        case "AnnotationNameTooLong":
            raise capo_s3.errors.annotation_name_too_long.AnnotationNameTooLong.from_xml(
                error_el, message
            )
        case "InvalidAnnotationName":
            raise capo_s3.errors.invalid_annotation_name.InvalidAnnotationName.from_xml(
                error_el, message
            )
        case "InvalidRequest":
            raise capo_s3.errors.invalid_request.InvalidRequest.from_xml(
                error_el, message
            )
        case "NoSuchBucket":
            raise capo_s3.errors.no_such_bucket.NoSuchBucket.from_xml(error_el, message)
        case "NoSuchKey":
            raise capo_s3.errors.no_such_key.NoSuchKey.from_xml(error_el, message)
        case "UnsupportedMediaType":
            raise capo_s3.errors.unsupported_media_type.UnsupportedMediaType.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_s3.types.put_object_annotation_output.PutObjectAnnotationOutput:
    out: capo_s3.types.put_object_annotation_output.PutObjectAnnotationOutput = (
        capo_s3.types.put_object_annotation_output.deserialize_xml(
            fromstring(response.read())
        )
    )
    if "x-amz-object-version-id" in response.headers:
        out["object_version_id"] = response.headers["x-amz-object-version-id"]
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
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3.types.put_object_annotation_output.PutObjectAnnotationOutput:
    out: capo_s3.types.put_object_annotation_output.PutObjectAnnotationOutput = (
        capo_s3.types.put_object_annotation_output.deserialize_xml(
            fromstring(await response.aread())
        )
    )
    if "x-amz-object-version-id" in response.headers:
        out["object_version_id"] = response.headers["x-amz-object-version-id"]
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
    input_: capo_s3.types.put_object_annotation_request.PutObjectAnnotationRequest,
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
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.request_payer

    url = endpoint.url.rstrip("/") + "/{Key+}?annotation"
    url = url.replace("{Key+}", quote(input_["key"], safe="/"))
    params: list[tuple[str, str]] = []
    if "version_id" in input_:
        params.append(("versionId", input_["version_id"]))
    if "annotation_name" in input_:
        params.append(("annotationName", input_["annotation_name"]))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "object_if_match" in input_:
        headers["x-amz-object-if-match"] = input_["object_if_match"]
    if "checksum_algorithm" in input_:
        headers["x-amz-sdk-checksum-algorithm"] = (
            capo_s3.types.checksum_algorithm.to_xml_text(input_["checksum_algorithm"])
        )
    if "checksum_crc32" in input_:
        headers["x-amz-checksum-crc32"] = input_["checksum_crc32"]
    if "checksum_crc32_c" in input_:
        headers["x-amz-checksum-crc32c"] = input_["checksum_crc32_c"]
    if "checksum_crc64_nvme" in input_:
        headers["x-amz-checksum-crc64nvme"] = input_["checksum_crc64_nvme"]
    if "checksum_sha1" in input_:
        headers["x-amz-checksum-sha1"] = input_["checksum_sha1"]
    if "checksum_sha256" in input_:
        headers["x-amz-checksum-sha256"] = input_["checksum_sha256"]
    if "checksum_sha512" in input_:
        headers["x-amz-checksum-sha512"] = input_["checksum_sha512"]
    if "checksum_md5" in input_:
        headers["x-amz-checksum-md5"] = input_["checksum_md5"]
    if "checksum_xxhash64" in input_:
        headers["x-amz-checksum-xxhash64"] = input_["checksum_xxhash64"]
    if "checksum_xxhash3" in input_:
        headers["x-amz-checksum-xxhash3"] = input_["checksum_xxhash3"]
    if "checksum_xxhash128" in input_:
        headers["x-amz-checksum-xxhash128"] = input_["checksum_xxhash128"]
    if "content_md5" in input_:
        headers["Content-MD5"] = input_["content_md5"]
    if "request_payer" in input_:
        headers["x-amz-request-payer"] = capo_s3.types.request_payer.to_xml_text(
            input_["request_payer"]
        )
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = input_["expected_bucket_owner"]
    body = input_["annotation_payload"]
    if isinstance(body, capo_s3._body.Body):
        body = cast(capo_s3._body.Body[Iterator[bytes]], body)
        stream = body.stream
        if stream is None:
            rebuilt = body.rebuild()
            if rebuilt is None:
                raise RuntimeError("streaming body could not be rebuilt")
            stream, _ = rebuilt
        if "content-length" not in [header.lower() for header in headers]:
            headers["Content-Length"] = str(body.length)
        body = stream
    if isinstance(body, capo_s3._iter.StaticAnyIterator):
        body = cast(bytes, body.content)
    if not isinstance(body, bytes) and "content-length" not in [
        header.lower() for header in headers
    ]:
        raise ValueError("Content-Length is required for streaming input")
    if "checksum_algorithm" in input_:
        if not capo_s3._checksums.set_request_checksum(
            headers, body, input_.get("checksum_algorithm")
        ):
            body = capo_s3._checksums.trailing_checksum(
                headers, cast(Iterator[bytes], body), input_.get("checksum_algorithm")
            )
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


async def async_build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_s3.types.put_object_annotation_request.PutObjectAnnotationRequest,
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
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.request_payer

    url = endpoint.url.rstrip("/") + "/{Key+}?annotation"
    url = url.replace("{Key+}", quote(input_["key"], safe="/"))
    params: list[tuple[str, str]] = []
    if "version_id" in input_:
        params.append(("versionId", input_["version_id"]))
    if "annotation_name" in input_:
        params.append(("annotationName", input_["annotation_name"]))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "object_if_match" in input_:
        headers["x-amz-object-if-match"] = input_["object_if_match"]
    if "checksum_algorithm" in input_:
        headers["x-amz-sdk-checksum-algorithm"] = (
            capo_s3.types.checksum_algorithm.to_xml_text(input_["checksum_algorithm"])
        )
    if "checksum_crc32" in input_:
        headers["x-amz-checksum-crc32"] = input_["checksum_crc32"]
    if "checksum_crc32_c" in input_:
        headers["x-amz-checksum-crc32c"] = input_["checksum_crc32_c"]
    if "checksum_crc64_nvme" in input_:
        headers["x-amz-checksum-crc64nvme"] = input_["checksum_crc64_nvme"]
    if "checksum_sha1" in input_:
        headers["x-amz-checksum-sha1"] = input_["checksum_sha1"]
    if "checksum_sha256" in input_:
        headers["x-amz-checksum-sha256"] = input_["checksum_sha256"]
    if "checksum_sha512" in input_:
        headers["x-amz-checksum-sha512"] = input_["checksum_sha512"]
    if "checksum_md5" in input_:
        headers["x-amz-checksum-md5"] = input_["checksum_md5"]
    if "checksum_xxhash64" in input_:
        headers["x-amz-checksum-xxhash64"] = input_["checksum_xxhash64"]
    if "checksum_xxhash3" in input_:
        headers["x-amz-checksum-xxhash3"] = input_["checksum_xxhash3"]
    if "checksum_xxhash128" in input_:
        headers["x-amz-checksum-xxhash128"] = input_["checksum_xxhash128"]
    if "content_md5" in input_:
        headers["Content-MD5"] = input_["content_md5"]
    if "request_payer" in input_:
        headers["x-amz-request-payer"] = capo_s3.types.request_payer.to_xml_text(
            input_["request_payer"]
        )
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = input_["expected_bucket_owner"]
    body = input_["annotation_payload"]
    if isinstance(body, capo_s3._body.Body):
        body = cast(capo_s3._body.Body[AsyncIterator[bytes]], body)
        stream = body.stream
        if stream is None:
            rebuilt = await body.arebuild()
            if rebuilt is None:
                raise RuntimeError("streaming body could not be rebuilt")
            stream, _ = rebuilt
        if "content-length" not in [header.lower() for header in headers]:
            headers["Content-Length"] = str(body.length)
        body = stream
    if isinstance(body, capo_s3._iter.StaticAnyIterator):
        body = cast(bytes, body.content)
    if not isinstance(body, bytes) and "content-length" not in [
        header.lower() for header in headers
    ]:
        raise ValueError("Content-Length is required for streaming input")
    if "checksum_algorithm" in input_:
        if not capo_s3._checksums.set_request_checksum(
            headers, body, input_.get("checksum_algorithm")
        ):
            body = capo_s3._checksums.trailing_checksum(
                headers,
                cast(AsyncIterator[bytes], body),
                input_.get("checksum_algorithm"),
            )
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def put_object_annotation(
    options: OperationOptions,
    input_: capo_s3.types.put_object_annotation_request.PutObjectAnnotationRequest,
) -> tuple[
    capo_s3.types.put_object_annotation_output.PutObjectAnnotationOutput,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_put_object_annotation(
    options: AsyncOperationOptions,
    input_: capo_s3.types.put_object_annotation_request.PutObjectAnnotationRequest,
) -> tuple[
    capo_s3.types.put_object_annotation_output.PutObjectAnnotationOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(
        await async_build_request(options, input_)
    )
    try:
        if response.status >= 300:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
