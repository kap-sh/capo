"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateFieldLevelEncryptionConfig``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudfront._auth._signers
import capo_cloudfront._auth._sigv4
import capo_cloudfront._protocol.eventstream
import capo_cloudfront.errors.field_level_encryption_config_already_exists
import capo_cloudfront.errors.inconsistent_quantities
import capo_cloudfront.errors.invalid_argument
import capo_cloudfront.errors.no_such_field_level_encryption_profile
import capo_cloudfront.errors.query_arg_profile_empty
import capo_cloudfront.errors.too_many_field_level_encryption_configs
import capo_cloudfront.errors.too_many_field_level_encryption_content_type_profiles
import capo_cloudfront.errors.too_many_field_level_encryption_query_arg_profiles
import capo_cloudfront.types.create_field_level_encryption_config_request
import capo_cloudfront.types.create_field_level_encryption_config_result
import capo_cloudfront.types.field_level_encryption
import capo_cloudfront.types.field_level_encryption_config
from capo_cloudfront._protocol.errors import find_error_element, parse_error_metadata
from capo_cloudfront._protocol.xml import Element, fromstring, tostring
from capo_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudfront._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cloudfront.errors import UnknownServiceError

STATUS_CODE_TO_CODE = {
    404: "NoSuchFieldLevelEncryptionProfile",
    409: "FieldLevelEncryptionConfigAlreadyExists",
}


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
        case "FieldLevelEncryptionConfigAlreadyExists":
            raise capo_cloudfront.errors.field_level_encryption_config_already_exists.FieldLevelEncryptionConfigAlreadyExists.from_xml(
                error_el, message
            )
        case "InconsistentQuantities":
            raise capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities.from_xml(
                error_el, message
            )
        case "InvalidArgument":
            raise capo_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                error_el, message
            )
        case "NoSuchFieldLevelEncryptionProfile":
            raise capo_cloudfront.errors.no_such_field_level_encryption_profile.NoSuchFieldLevelEncryptionProfile.from_xml(
                error_el, message
            )
        case "QueryArgProfileEmpty":
            raise capo_cloudfront.errors.query_arg_profile_empty.QueryArgProfileEmpty.from_xml(
                error_el, message
            )
        case "TooManyFieldLevelEncryptionConfigs":
            raise capo_cloudfront.errors.too_many_field_level_encryption_configs.TooManyFieldLevelEncryptionConfigs.from_xml(
                error_el, message
            )
        case "TooManyFieldLevelEncryptionContentTypeProfiles":
            raise capo_cloudfront.errors.too_many_field_level_encryption_content_type_profiles.TooManyFieldLevelEncryptionContentTypeProfiles.from_xml(
                error_el, message
            )
        case "TooManyFieldLevelEncryptionQueryArgProfiles":
            raise capo_cloudfront.errors.too_many_field_level_encryption_query_arg_profiles.TooManyFieldLevelEncryptionQueryArgProfiles.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.create_field_level_encryption_config_result.CreateFieldLevelEncryptionConfigResult:
    out: capo_cloudfront.types.create_field_level_encryption_config_result.CreateFieldLevelEncryptionConfigResult = {
        "field_level_encryption": capo_cloudfront.types.field_level_encryption.deserialize_xml(
            fromstring(response.read())
        )
    }  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = response.headers["Location"]
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.create_field_level_encryption_config_result.CreateFieldLevelEncryptionConfigResult:
    out: capo_cloudfront.types.create_field_level_encryption_config_result.CreateFieldLevelEncryptionConfigResult = {
        "field_level_encryption": capo_cloudfront.types.field_level_encryption.deserialize_xml(
            fromstring(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = response.headers["Location"]
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudfront._auth._signers.Signer | None:
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
            sigv4_config = capo_cloudfront._auth._sigv4.build_sigv4_auth_scheme(
                "cloudfront", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_cloudfront._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudfront.types.create_field_level_encryption_config_request.CreateFieldLevelEncryptionConfigRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/field-level-encryption"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    payload_root = Element("_")
    capo_cloudfront.types.field_level_encryption_config.serialize_xml(
        input_["field_level_encryption_config"],
        payload_root,
        "FieldLevelEncryptionConfig",
    )
    body: bytes | None = tostring(payload_root[0])
    headers["content-type"] = "application/xml"
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


def create_field_level_encryption_config(
    options: OperationOptions,
    input_: capo_cloudfront.types.create_field_level_encryption_config_request.CreateFieldLevelEncryptionConfigRequest,
) -> tuple[
    capo_cloudfront.types.create_field_level_encryption_config_result.CreateFieldLevelEncryptionConfigResult,
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


async def async_create_field_level_encryption_config(
    options: AsyncOperationOptions,
    input_: capo_cloudfront.types.create_field_level_encryption_config_request.CreateFieldLevelEncryptionConfigRequest,
) -> tuple[
    capo_cloudfront.types.create_field_level_encryption_config_result.CreateFieldLevelEncryptionConfigResult,
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
