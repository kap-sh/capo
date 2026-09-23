"""Generated from Smithy shape ``com.amazonaws.s3#CompleteMultipartUpload``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_s3._auth._signers
import capo_s3._auth._sigv4
import capo_s3._protocol.eventstream
import capo_s3.types.checksum_type
import capo_s3.types.complete_multipart_upload_output
import capo_s3.types.complete_multipart_upload_request
import capo_s3.types.completed_multipart_upload
import capo_s3.types.request_charged
import capo_s3.types.request_payer
import capo_s3.types.server_side_encryption
from capo_s3._protocol.errors import is_xml_error_body, parse_error_metadata
from capo_s3._protocol.xml import Element, fromstring, tostring
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


def handle_response(
    response: zapros.Response,
) -> capo_s3.types.complete_multipart_upload_output.CompleteMultipartUploadOutput:
    out: capo_s3.types.complete_multipart_upload_output.CompleteMultipartUploadOutput = capo_s3.types.complete_multipart_upload_output.deserialize_xml(
        fromstring(response.read())
    )
    if "x-amz-expiration" in response.headers:
        out["expiration"] = response.headers["x-amz-expiration"]
    if "x-amz-server-side-encryption" in response.headers:
        out["server_side_encryption"] = (
            capo_s3.types.server_side_encryption.from_xml_text(
                response.headers["x-amz-server-side-encryption"]
            )
        )
    if "x-amz-version-id" in response.headers:
        out["version_id"] = response.headers["x-amz-version-id"]
    if "x-amz-server-side-encryption-aws-kms-key-id" in response.headers:
        out["ssekms_key_id"] = response.headers[
            "x-amz-server-side-encryption-aws-kms-key-id"
        ]
    if "x-amz-server-side-encryption-bucket-key-enabled" in response.headers:
        out["bucket_key_enabled"] = (
            response.headers["x-amz-server-side-encryption-bucket-key-enabled"].lower()
            == "true"
        )
    if "x-amz-request-charged" in response.headers:
        out["request_charged"] = capo_s3.types.request_charged.from_xml_text(
            response.headers["x-amz-request-charged"]
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3.types.complete_multipart_upload_output.CompleteMultipartUploadOutput:
    out: capo_s3.types.complete_multipart_upload_output.CompleteMultipartUploadOutput = capo_s3.types.complete_multipart_upload_output.deserialize_xml(
        fromstring(await response.aread())
    )
    if "x-amz-expiration" in response.headers:
        out["expiration"] = response.headers["x-amz-expiration"]
    if "x-amz-server-side-encryption" in response.headers:
        out["server_side_encryption"] = (
            capo_s3.types.server_side_encryption.from_xml_text(
                response.headers["x-amz-server-side-encryption"]
            )
        )
    if "x-amz-version-id" in response.headers:
        out["version_id"] = response.headers["x-amz-version-id"]
    if "x-amz-server-side-encryption-aws-kms-key-id" in response.headers:
        out["ssekms_key_id"] = response.headers[
            "x-amz-server-side-encryption-aws-kms-key-id"
        ]
    if "x-amz-server-side-encryption-bucket-key-enabled" in response.headers:
        out["bucket_key_enabled"] = (
            response.headers["x-amz-server-side-encryption-bucket-key-enabled"].lower()
            == "true"
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
    input_: capo_s3.types.complete_multipart_upload_request.CompleteMultipartUploadRequest,
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
    import capo_s3.types.checksum_type
    import capo_s3.types.request_payer

    url = endpoint.url.rstrip("/") + "/{Key+}"
    url = url.replace("{Key+}", quote(input_["key"], safe="/"))
    params: list[tuple[str, str]] = []
    if "upload_id" in input_:
        params.append(("uploadId", input_["upload_id"]))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
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
    if "checksum_type" in input_:
        headers["x-amz-checksum-type"] = capo_s3.types.checksum_type.to_xml_text(
            input_["checksum_type"]
        )
    if "mpu_object_size" in input_:
        headers["x-amz-mp-object-size"] = str(input_["mpu_object_size"])
    if "request_payer" in input_:
        headers["x-amz-request-payer"] = capo_s3.types.request_payer.to_xml_text(
            input_["request_payer"]
        )
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = input_["expected_bucket_owner"]
    if "if_match" in input_:
        headers["If-Match"] = input_["if_match"]
    if "if_none_match" in input_:
        headers["If-None-Match"] = input_["if_none_match"]
    if "sse_customer_algorithm" in input_:
        headers["x-amz-server-side-encryption-customer-algorithm"] = input_[
            "sse_customer_algorithm"
        ]
    if "sse_customer_key" in input_:
        headers["x-amz-server-side-encryption-customer-key"] = input_[
            "sse_customer_key"
        ]
    if "sse_customer_key_md5" in input_:
        headers["x-amz-server-side-encryption-customer-key-MD5"] = input_[
            "sse_customer_key_md5"
        ]
    if "multipart_upload" in input_:
        payload_root = Element("_")
        capo_s3.types.completed_multipart_upload.serialize_xml(
            input_["multipart_upload"], payload_root, "CompleteMultipartUpload"
        )
        body: bytes | None = tostring(payload_root[0])
        headers["content-type"] = "application/xml"
    else:
        body = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def complete_multipart_upload(
    options: OperationOptions,
    input_: capo_s3.types.complete_multipart_upload_request.CompleteMultipartUploadRequest,
) -> tuple[
    capo_s3.types.complete_multipart_upload_output.CompleteMultipartUploadOutput,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        body = response.read()
        if response.status >= 300 or is_xml_error_body(body):
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_complete_multipart_upload(
    options: AsyncOperationOptions,
    input_: capo_s3.types.complete_multipart_upload_request.CompleteMultipartUploadRequest,
) -> tuple[
    capo_s3.types.complete_multipart_upload_output.CompleteMultipartUploadOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        body = await response.aread()
        if response.status >= 300 or is_xml_error_body(body):
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
