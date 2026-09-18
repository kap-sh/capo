"""Generated from Smithy shape ``com.amazonaws.s3#WriteGetObjectResponse``."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import Any, cast

import zapros
from typing_extensions import Never

import capo_s3._auth._signers
import capo_s3._auth._sigv4
import capo_s3._body
import capo_s3._protocol.eventstream
import capo_s3.types.last_modified
import capo_s3.types.metadata
import capo_s3.types.object_lock_legal_hold_status
import capo_s3.types.object_lock_mode
import capo_s3.types.object_lock_retain_until_date
import capo_s3.types.replication_status
import capo_s3.types.request_charged
import capo_s3.types.server_side_encryption
import capo_s3.types.storage_class
import capo_s3.types.streaming_blob
import capo_s3.types.write_get_object_response_request
from capo_s3._protocol.errors import parse_error_metadata
from capo_s3._protocol.xml import fromstring
from capo_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_s3.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    body = response.read()
    if not body:
        raise UnknownServiceError(code=None, message=None, response=response)
    root = fromstring(body)
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


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
    input_: capo_s3.types.write_get_object_response_request.WriteGetObjectResponseRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Bucket=options.bucket,
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
            ForcePathStyle=options.force_path_style,
            Accelerate=options.accelerate,
            UseGlobalEndpoint=options.use_global_endpoint,
            UseObjectLambdaEndpoint=True,
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
    import capo_s3._protocol.serialize
    import capo_s3.types.object_lock_legal_hold_status
    import capo_s3.types.object_lock_mode
    import capo_s3.types.replication_status
    import capo_s3.types.request_charged
    import capo_s3.types.server_side_encryption
    import capo_s3.types.storage_class

    url = endpoint.url.rstrip("/") + "/WriteGetObjectResponse"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "request_route" in input_:
        headers["x-amz-request-route"] = input_["request_route"]
    if "request_token" in input_:
        headers["x-amz-request-token"] = input_["request_token"]
    if "status_code" in input_:
        headers["x-amz-fwd-status"] = str(input_["status_code"])
    if "error_code" in input_:
        headers["x-amz-fwd-error-code"] = input_["error_code"]
    if "error_message" in input_:
        headers["x-amz-fwd-error-message"] = input_["error_message"]
    if "accept_ranges" in input_:
        headers["x-amz-fwd-header-accept-ranges"] = input_["accept_ranges"]
    if "cache_control" in input_:
        headers["x-amz-fwd-header-Cache-Control"] = input_["cache_control"]
    if "content_disposition" in input_:
        headers["x-amz-fwd-header-Content-Disposition"] = input_["content_disposition"]
    if "content_encoding" in input_:
        headers["x-amz-fwd-header-Content-Encoding"] = input_["content_encoding"]
    if "content_language" in input_:
        headers["x-amz-fwd-header-Content-Language"] = input_["content_language"]
    if "content_length" in input_:
        headers["Content-Length"] = str(input_["content_length"])
    if "content_range" in input_:
        headers["x-amz-fwd-header-Content-Range"] = input_["content_range"]
    if "content_type" in input_:
        headers["x-amz-fwd-header-Content-Type"] = input_["content_type"]
    if "checksum_crc32" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-crc32"] = input_["checksum_crc32"]
    if "checksum_crc32_c" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-crc32c"] = input_["checksum_crc32_c"]
    if "checksum_crc64_nvme" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-crc64nvme"] = input_[
            "checksum_crc64_nvme"
        ]
    if "checksum_sha1" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-sha1"] = input_["checksum_sha1"]
    if "checksum_sha256" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-sha256"] = input_["checksum_sha256"]
    if "checksum_sha512" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-sha512"] = input_["checksum_sha512"]
    if "checksum_md5" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-md5"] = input_["checksum_md5"]
    if "checksum_xxhash64" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-xxhash64"] = input_[
            "checksum_xxhash64"
        ]
    if "checksum_xxhash3" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-xxhash3"] = input_["checksum_xxhash3"]
    if "checksum_xxhash128" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-xxhash128"] = input_[
            "checksum_xxhash128"
        ]
    if "delete_marker" in input_:
        headers["x-amz-fwd-header-x-amz-delete-marker"] = (
            "true" if input_["delete_marker"] else "false"
        )
    if "e_tag" in input_:
        headers["x-amz-fwd-header-ETag"] = input_["e_tag"]
    if "expires" in input_:
        headers["x-amz-fwd-header-Expires"] = input_["expires"]
    if "expiration" in input_:
        headers["x-amz-fwd-header-x-amz-expiration"] = input_["expiration"]
    if "last_modified" in input_:
        headers["x-amz-fwd-header-Last-Modified"] = (
            capo_s3._protocol.serialize.fmt_http_date(input_["last_modified"])
        )
    if "missing_meta" in input_:
        headers["x-amz-fwd-header-x-amz-missing-meta"] = str(input_["missing_meta"])
    if "object_lock_mode" in input_:
        headers["x-amz-fwd-header-x-amz-object-lock-mode"] = (
            capo_s3.types.object_lock_mode.to_xml_text(input_["object_lock_mode"])
        )
    if "object_lock_legal_hold_status" in input_:
        headers["x-amz-fwd-header-x-amz-object-lock-legal-hold"] = (
            capo_s3.types.object_lock_legal_hold_status.to_xml_text(
                input_["object_lock_legal_hold_status"]
            )
        )
    if "object_lock_retain_until_date" in input_:
        headers["x-amz-fwd-header-x-amz-object-lock-retain-until-date"] = (
            capo_s3._protocol.serialize.fmt_date_time(
                input_["object_lock_retain_until_date"]
            )
        )
    if "parts_count" in input_:
        headers["x-amz-fwd-header-x-amz-mp-parts-count"] = str(input_["parts_count"])
    if "replication_status" in input_:
        headers["x-amz-fwd-header-x-amz-replication-status"] = (
            capo_s3.types.replication_status.to_xml_text(input_["replication_status"])
        )
    if "request_charged" in input_:
        headers["x-amz-fwd-header-x-amz-request-charged"] = (
            capo_s3.types.request_charged.to_xml_text(input_["request_charged"])
        )
    if "restore" in input_:
        headers["x-amz-fwd-header-x-amz-restore"] = input_["restore"]
    if "server_side_encryption" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption"] = (
            capo_s3.types.server_side_encryption.to_xml_text(
                input_["server_side_encryption"]
            )
        )
    if "sse_customer_algorithm" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption-customer-algorithm"] = (
            input_["sse_customer_algorithm"]
        )
    if "ssekms_key_id" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption-aws-kms-key-id"] = (
            input_["ssekms_key_id"]
        )
    if "sse_customer_key_md5" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption-customer-key-MD5"] = (
            input_["sse_customer_key_md5"]
        )
    if "storage_class" in input_:
        headers["x-amz-fwd-header-x-amz-storage-class"] = (
            capo_s3.types.storage_class.to_xml_text(input_["storage_class"])
        )
    if "tag_count" in input_:
        headers["x-amz-fwd-header-x-amz-tagging-count"] = str(input_["tag_count"])
    if "version_id" in input_:
        headers["x-amz-fwd-header-x-amz-version-id"] = input_["version_id"]
    if "bucket_key_enabled" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption-bucket-key-enabled"] = (
            "true" if input_["bucket_key_enabled"] else "false"
        )
    if "metadata" in input_:
        for k, v in input_["metadata"].items():
            headers["x-amz-meta-" + k] = v
    body = input_["body"]
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
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


async def async_build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_s3.types.write_get_object_response_request.WriteGetObjectResponseRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Bucket=options.bucket,
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
            ForcePathStyle=options.force_path_style,
            Accelerate=options.accelerate,
            UseGlobalEndpoint=options.use_global_endpoint,
            UseObjectLambdaEndpoint=True,
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
    import capo_s3._protocol.serialize
    import capo_s3.types.object_lock_legal_hold_status
    import capo_s3.types.object_lock_mode
    import capo_s3.types.replication_status
    import capo_s3.types.request_charged
    import capo_s3.types.server_side_encryption
    import capo_s3.types.storage_class

    url = endpoint.url.rstrip("/") + "/WriteGetObjectResponse"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "request_route" in input_:
        headers["x-amz-request-route"] = input_["request_route"]
    if "request_token" in input_:
        headers["x-amz-request-token"] = input_["request_token"]
    if "status_code" in input_:
        headers["x-amz-fwd-status"] = str(input_["status_code"])
    if "error_code" in input_:
        headers["x-amz-fwd-error-code"] = input_["error_code"]
    if "error_message" in input_:
        headers["x-amz-fwd-error-message"] = input_["error_message"]
    if "accept_ranges" in input_:
        headers["x-amz-fwd-header-accept-ranges"] = input_["accept_ranges"]
    if "cache_control" in input_:
        headers["x-amz-fwd-header-Cache-Control"] = input_["cache_control"]
    if "content_disposition" in input_:
        headers["x-amz-fwd-header-Content-Disposition"] = input_["content_disposition"]
    if "content_encoding" in input_:
        headers["x-amz-fwd-header-Content-Encoding"] = input_["content_encoding"]
    if "content_language" in input_:
        headers["x-amz-fwd-header-Content-Language"] = input_["content_language"]
    if "content_length" in input_:
        headers["Content-Length"] = str(input_["content_length"])
    if "content_range" in input_:
        headers["x-amz-fwd-header-Content-Range"] = input_["content_range"]
    if "content_type" in input_:
        headers["x-amz-fwd-header-Content-Type"] = input_["content_type"]
    if "checksum_crc32" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-crc32"] = input_["checksum_crc32"]
    if "checksum_crc32_c" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-crc32c"] = input_["checksum_crc32_c"]
    if "checksum_crc64_nvme" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-crc64nvme"] = input_[
            "checksum_crc64_nvme"
        ]
    if "checksum_sha1" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-sha1"] = input_["checksum_sha1"]
    if "checksum_sha256" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-sha256"] = input_["checksum_sha256"]
    if "checksum_sha512" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-sha512"] = input_["checksum_sha512"]
    if "checksum_md5" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-md5"] = input_["checksum_md5"]
    if "checksum_xxhash64" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-xxhash64"] = input_[
            "checksum_xxhash64"
        ]
    if "checksum_xxhash3" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-xxhash3"] = input_["checksum_xxhash3"]
    if "checksum_xxhash128" in input_:
        headers["x-amz-fwd-header-x-amz-checksum-xxhash128"] = input_[
            "checksum_xxhash128"
        ]
    if "delete_marker" in input_:
        headers["x-amz-fwd-header-x-amz-delete-marker"] = (
            "true" if input_["delete_marker"] else "false"
        )
    if "e_tag" in input_:
        headers["x-amz-fwd-header-ETag"] = input_["e_tag"]
    if "expires" in input_:
        headers["x-amz-fwd-header-Expires"] = input_["expires"]
    if "expiration" in input_:
        headers["x-amz-fwd-header-x-amz-expiration"] = input_["expiration"]
    if "last_modified" in input_:
        headers["x-amz-fwd-header-Last-Modified"] = (
            capo_s3._protocol.serialize.fmt_http_date(input_["last_modified"])
        )
    if "missing_meta" in input_:
        headers["x-amz-fwd-header-x-amz-missing-meta"] = str(input_["missing_meta"])
    if "object_lock_mode" in input_:
        headers["x-amz-fwd-header-x-amz-object-lock-mode"] = (
            capo_s3.types.object_lock_mode.to_xml_text(input_["object_lock_mode"])
        )
    if "object_lock_legal_hold_status" in input_:
        headers["x-amz-fwd-header-x-amz-object-lock-legal-hold"] = (
            capo_s3.types.object_lock_legal_hold_status.to_xml_text(
                input_["object_lock_legal_hold_status"]
            )
        )
    if "object_lock_retain_until_date" in input_:
        headers["x-amz-fwd-header-x-amz-object-lock-retain-until-date"] = (
            capo_s3._protocol.serialize.fmt_date_time(
                input_["object_lock_retain_until_date"]
            )
        )
    if "parts_count" in input_:
        headers["x-amz-fwd-header-x-amz-mp-parts-count"] = str(input_["parts_count"])
    if "replication_status" in input_:
        headers["x-amz-fwd-header-x-amz-replication-status"] = (
            capo_s3.types.replication_status.to_xml_text(input_["replication_status"])
        )
    if "request_charged" in input_:
        headers["x-amz-fwd-header-x-amz-request-charged"] = (
            capo_s3.types.request_charged.to_xml_text(input_["request_charged"])
        )
    if "restore" in input_:
        headers["x-amz-fwd-header-x-amz-restore"] = input_["restore"]
    if "server_side_encryption" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption"] = (
            capo_s3.types.server_side_encryption.to_xml_text(
                input_["server_side_encryption"]
            )
        )
    if "sse_customer_algorithm" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption-customer-algorithm"] = (
            input_["sse_customer_algorithm"]
        )
    if "ssekms_key_id" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption-aws-kms-key-id"] = (
            input_["ssekms_key_id"]
        )
    if "sse_customer_key_md5" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption-customer-key-MD5"] = (
            input_["sse_customer_key_md5"]
        )
    if "storage_class" in input_:
        headers["x-amz-fwd-header-x-amz-storage-class"] = (
            capo_s3.types.storage_class.to_xml_text(input_["storage_class"])
        )
    if "tag_count" in input_:
        headers["x-amz-fwd-header-x-amz-tagging-count"] = str(input_["tag_count"])
    if "version_id" in input_:
        headers["x-amz-fwd-header-x-amz-version-id"] = input_["version_id"]
    if "bucket_key_enabled" in input_:
        headers["x-amz-fwd-header-x-amz-server-side-encryption-bucket-key-enabled"] = (
            "true" if input_["bucket_key_enabled"] else "false"
        )
    if "metadata" in input_:
        for k, v in input_["metadata"].items():
            headers["x-amz-meta-" + k] = v
    body = input_["body"]
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
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def write_get_object_response(
    options: OperationOptions,
    input_: capo_s3.types.write_get_object_response_request.WriteGetObjectResponseRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 300:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_write_get_object_response(
    options: AsyncOperationOptions,
    input_: capo_s3.types.write_get_object_response_request.WriteGetObjectResponseRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(
        await async_build_request(options, input_)
    )
    try:
        if response.status >= 300:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
