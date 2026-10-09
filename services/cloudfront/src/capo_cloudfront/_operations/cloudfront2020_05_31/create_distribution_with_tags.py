"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateDistributionWithTags``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudfront._auth._signers
import capo_cloudfront._auth._sigv4
import capo_cloudfront._protocol.eventstream
import capo_cloudfront.errors.access_denied
import capo_cloudfront.errors.cname_already_exists
import capo_cloudfront.errors.continuous_deployment_policy_in_use
import capo_cloudfront.errors.distribution_already_exists
import capo_cloudfront.errors.entity_not_found
import capo_cloudfront.errors.illegal_field_level_encryption_config_association_with_cache_behavior
import capo_cloudfront.errors.illegal_origin_access_configuration
import capo_cloudfront.errors.inconsistent_quantities
import capo_cloudfront.errors.invalid_argument
import capo_cloudfront.errors.invalid_default_root_object
import capo_cloudfront.errors.invalid_domain_name_for_origin_access_control
import capo_cloudfront.errors.invalid_error_code
import capo_cloudfront.errors.invalid_forward_cookies
import capo_cloudfront.errors.invalid_function_association
import capo_cloudfront.errors.invalid_geo_restriction_parameter
import capo_cloudfront.errors.invalid_headers_for_s3_origin
import capo_cloudfront.errors.invalid_lambda_function_association
import capo_cloudfront.errors.invalid_location_code
import capo_cloudfront.errors.invalid_minimum_protocol_version
import capo_cloudfront.errors.invalid_origin
import capo_cloudfront.errors.invalid_origin_access_control
import capo_cloudfront.errors.invalid_origin_access_identity
import capo_cloudfront.errors.invalid_origin_keepalive_timeout
import capo_cloudfront.errors.invalid_origin_read_timeout
import capo_cloudfront.errors.invalid_protocol_settings
import capo_cloudfront.errors.invalid_query_string_parameters
import capo_cloudfront.errors.invalid_relative_path
import capo_cloudfront.errors.invalid_required_protocol
import capo_cloudfront.errors.invalid_response_code
import capo_cloudfront.errors.invalid_tagging
import capo_cloudfront.errors.invalid_ttl_order
import capo_cloudfront.errors.invalid_viewer_certificate
import capo_cloudfront.errors.invalid_web_acl_id
import capo_cloudfront.errors.missing_body
import capo_cloudfront.errors.no_such_cache_policy
import capo_cloudfront.errors.no_such_continuous_deployment_policy
import capo_cloudfront.errors.no_such_field_level_encryption_config
import capo_cloudfront.errors.no_such_origin
import capo_cloudfront.errors.no_such_origin_request_policy
import capo_cloudfront.errors.no_such_realtime_log_config
import capo_cloudfront.errors.no_such_response_headers_policy
import capo_cloudfront.errors.realtime_log_config_owner_mismatch
import capo_cloudfront.errors.too_many_cache_behaviors
import capo_cloudfront.errors.too_many_certificates
import capo_cloudfront.errors.too_many_cookie_names_in_white_list
import capo_cloudfront.errors.too_many_distribution_cnam_es
import capo_cloudfront.errors.too_many_distributions
import capo_cloudfront.errors.too_many_distributions_associated_to_cache_policy
import capo_cloudfront.errors.too_many_distributions_associated_to_field_level_encryption_config
import capo_cloudfront.errors.too_many_distributions_associated_to_key_group
import capo_cloudfront.errors.too_many_distributions_associated_to_origin_access_control
import capo_cloudfront.errors.too_many_distributions_associated_to_origin_request_policy
import capo_cloudfront.errors.too_many_distributions_associated_to_response_headers_policy
import capo_cloudfront.errors.too_many_distributions_with_function_associations
import capo_cloudfront.errors.too_many_distributions_with_lambda_associations
import capo_cloudfront.errors.too_many_distributions_with_single_function_arn
import capo_cloudfront.errors.too_many_function_associations
import capo_cloudfront.errors.too_many_headers_in_forwarded_values
import capo_cloudfront.errors.too_many_key_groups_associated_to_distribution
import capo_cloudfront.errors.too_many_lambda_function_associations
import capo_cloudfront.errors.too_many_origin_custom_headers
import capo_cloudfront.errors.too_many_origin_groups_per_distribution
import capo_cloudfront.errors.too_many_origins
import capo_cloudfront.errors.too_many_query_string_parameters
import capo_cloudfront.errors.too_many_trusted_signers
import capo_cloudfront.errors.trusted_key_group_does_not_exist
import capo_cloudfront.errors.trusted_signer_does_not_exist
import capo_cloudfront.types.create_distribution_with_tags_request
import capo_cloudfront.types.create_distribution_with_tags_result
import capo_cloudfront.types.distribution
import capo_cloudfront.types.distribution_config_with_tags
from capo_cloudfront._protocol.errors import find_error_element, parse_error_metadata
from capo_cloudfront._protocol.xml import Element, fromstring, tostring
from capo_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudfront._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_cloudfront.errors import UnknownServiceError

STATUS_CODE_TO_CODE = {401: "RealtimeLogConfigOwnerMismatch", 403: "AccessDenied"}


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
            raise capo_cloudfront.errors.access_denied.AccessDenied.from_xml(
                error_el, message
            )
        case "CNAMEAlreadyExists":
            raise capo_cloudfront.errors.cname_already_exists.CNAMEAlreadyExists.from_xml(
                error_el, message
            )
        case "ContinuousDeploymentPolicyInUse":
            raise capo_cloudfront.errors.continuous_deployment_policy_in_use.ContinuousDeploymentPolicyInUse.from_xml(
                error_el, message
            )
        case "DistributionAlreadyExists":
            raise capo_cloudfront.errors.distribution_already_exists.DistributionAlreadyExists.from_xml(
                error_el, message
            )
        case "EntityNotFound":
            raise capo_cloudfront.errors.entity_not_found.EntityNotFound.from_xml(
                error_el, message
            )
        case "IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior":
            raise capo_cloudfront.errors.illegal_field_level_encryption_config_association_with_cache_behavior.IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior.from_xml(
                error_el, message
            )
        case "IllegalOriginAccessConfiguration":
            raise capo_cloudfront.errors.illegal_origin_access_configuration.IllegalOriginAccessConfiguration.from_xml(
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
        case "InvalidDefaultRootObject":
            raise capo_cloudfront.errors.invalid_default_root_object.InvalidDefaultRootObject.from_xml(
                error_el, message
            )
        case "InvalidDomainNameForOriginAccessControl":
            raise capo_cloudfront.errors.invalid_domain_name_for_origin_access_control.InvalidDomainNameForOriginAccessControl.from_xml(
                error_el, message
            )
        case "InvalidErrorCode":
            raise capo_cloudfront.errors.invalid_error_code.InvalidErrorCode.from_xml(
                error_el, message
            )
        case "InvalidForwardCookies":
            raise capo_cloudfront.errors.invalid_forward_cookies.InvalidForwardCookies.from_xml(
                error_el, message
            )
        case "InvalidFunctionAssociation":
            raise capo_cloudfront.errors.invalid_function_association.InvalidFunctionAssociation.from_xml(
                error_el, message
            )
        case "InvalidGeoRestrictionParameter":
            raise capo_cloudfront.errors.invalid_geo_restriction_parameter.InvalidGeoRestrictionParameter.from_xml(
                error_el, message
            )
        case "InvalidHeadersForS3Origin":
            raise capo_cloudfront.errors.invalid_headers_for_s3_origin.InvalidHeadersForS3Origin.from_xml(
                error_el, message
            )
        case "InvalidLambdaFunctionAssociation":
            raise capo_cloudfront.errors.invalid_lambda_function_association.InvalidLambdaFunctionAssociation.from_xml(
                error_el, message
            )
        case "InvalidLocationCode":
            raise capo_cloudfront.errors.invalid_location_code.InvalidLocationCode.from_xml(
                error_el, message
            )
        case "InvalidMinimumProtocolVersion":
            raise capo_cloudfront.errors.invalid_minimum_protocol_version.InvalidMinimumProtocolVersion.from_xml(
                error_el, message
            )
        case "InvalidOrigin":
            raise capo_cloudfront.errors.invalid_origin.InvalidOrigin.from_xml(
                error_el, message
            )
        case "InvalidOriginAccessControl":
            raise capo_cloudfront.errors.invalid_origin_access_control.InvalidOriginAccessControl.from_xml(
                error_el, message
            )
        case "InvalidOriginAccessIdentity":
            raise capo_cloudfront.errors.invalid_origin_access_identity.InvalidOriginAccessIdentity.from_xml(
                error_el, message
            )
        case "InvalidOriginKeepaliveTimeout":
            raise capo_cloudfront.errors.invalid_origin_keepalive_timeout.InvalidOriginKeepaliveTimeout.from_xml(
                error_el, message
            )
        case "InvalidOriginReadTimeout":
            raise capo_cloudfront.errors.invalid_origin_read_timeout.InvalidOriginReadTimeout.from_xml(
                error_el, message
            )
        case "InvalidProtocolSettings":
            raise capo_cloudfront.errors.invalid_protocol_settings.InvalidProtocolSettings.from_xml(
                error_el, message
            )
        case "InvalidQueryStringParameters":
            raise capo_cloudfront.errors.invalid_query_string_parameters.InvalidQueryStringParameters.from_xml(
                error_el, message
            )
        case "InvalidRelativePath":
            raise capo_cloudfront.errors.invalid_relative_path.InvalidRelativePath.from_xml(
                error_el, message
            )
        case "InvalidRequiredProtocol":
            raise capo_cloudfront.errors.invalid_required_protocol.InvalidRequiredProtocol.from_xml(
                error_el, message
            )
        case "InvalidResponseCode":
            raise capo_cloudfront.errors.invalid_response_code.InvalidResponseCode.from_xml(
                error_el, message
            )
        case "InvalidTagging":
            raise capo_cloudfront.errors.invalid_tagging.InvalidTagging.from_xml(
                error_el, message
            )
        case "InvalidTTLOrder":
            raise capo_cloudfront.errors.invalid_ttl_order.InvalidTTLOrder.from_xml(
                error_el, message
            )
        case "InvalidViewerCertificate":
            raise capo_cloudfront.errors.invalid_viewer_certificate.InvalidViewerCertificate.from_xml(
                error_el, message
            )
        case "InvalidWebACLId":
            raise capo_cloudfront.errors.invalid_web_acl_id.InvalidWebACLId.from_xml(
                error_el, message
            )
        case "MissingBody":
            raise capo_cloudfront.errors.missing_body.MissingBody.from_xml(
                error_el, message
            )
        case "NoSuchCachePolicy":
            raise capo_cloudfront.errors.no_such_cache_policy.NoSuchCachePolicy.from_xml(
                error_el, message
            )
        case "NoSuchContinuousDeploymentPolicy":
            raise capo_cloudfront.errors.no_such_continuous_deployment_policy.NoSuchContinuousDeploymentPolicy.from_xml(
                error_el, message
            )
        case "NoSuchFieldLevelEncryptionConfig":
            raise capo_cloudfront.errors.no_such_field_level_encryption_config.NoSuchFieldLevelEncryptionConfig.from_xml(
                error_el, message
            )
        case "NoSuchOrigin":
            raise capo_cloudfront.errors.no_such_origin.NoSuchOrigin.from_xml(
                error_el, message
            )
        case "NoSuchOriginRequestPolicy":
            raise capo_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy.from_xml(
                error_el, message
            )
        case "NoSuchRealtimeLogConfig":
            raise capo_cloudfront.errors.no_such_realtime_log_config.NoSuchRealtimeLogConfig.from_xml(
                error_el, message
            )
        case "NoSuchResponseHeadersPolicy":
            raise capo_cloudfront.errors.no_such_response_headers_policy.NoSuchResponseHeadersPolicy.from_xml(
                error_el, message
            )
        case "RealtimeLogConfigOwnerMismatch":
            raise capo_cloudfront.errors.realtime_log_config_owner_mismatch.RealtimeLogConfigOwnerMismatch.from_xml(
                error_el, message
            )
        case "TooManyCacheBehaviors":
            raise capo_cloudfront.errors.too_many_cache_behaviors.TooManyCacheBehaviors.from_xml(
                error_el, message
            )
        case "TooManyCertificates":
            raise capo_cloudfront.errors.too_many_certificates.TooManyCertificates.from_xml(
                error_el, message
            )
        case "TooManyCookieNamesInWhiteList":
            raise capo_cloudfront.errors.too_many_cookie_names_in_white_list.TooManyCookieNamesInWhiteList.from_xml(
                error_el, message
            )
        case "TooManyDistributionCNAMEs":
            raise capo_cloudfront.errors.too_many_distribution_cnam_es.TooManyDistributionCNAMEs.from_xml(
                error_el, message
            )
        case "TooManyDistributions":
            raise capo_cloudfront.errors.too_many_distributions.TooManyDistributions.from_xml(
                error_el, message
            )
        case "TooManyDistributionsAssociatedToCachePolicy":
            raise capo_cloudfront.errors.too_many_distributions_associated_to_cache_policy.TooManyDistributionsAssociatedToCachePolicy.from_xml(
                error_el, message
            )
        case "TooManyDistributionsAssociatedToFieldLevelEncryptionConfig":
            raise capo_cloudfront.errors.too_many_distributions_associated_to_field_level_encryption_config.TooManyDistributionsAssociatedToFieldLevelEncryptionConfig.from_xml(
                error_el, message
            )
        case "TooManyDistributionsAssociatedToKeyGroup":
            raise capo_cloudfront.errors.too_many_distributions_associated_to_key_group.TooManyDistributionsAssociatedToKeyGroup.from_xml(
                error_el, message
            )
        case "TooManyDistributionsAssociatedToOriginAccessControl":
            raise capo_cloudfront.errors.too_many_distributions_associated_to_origin_access_control.TooManyDistributionsAssociatedToOriginAccessControl.from_xml(
                error_el, message
            )
        case "TooManyDistributionsAssociatedToOriginRequestPolicy":
            raise capo_cloudfront.errors.too_many_distributions_associated_to_origin_request_policy.TooManyDistributionsAssociatedToOriginRequestPolicy.from_xml(
                error_el, message
            )
        case "TooManyDistributionsAssociatedToResponseHeadersPolicy":
            raise capo_cloudfront.errors.too_many_distributions_associated_to_response_headers_policy.TooManyDistributionsAssociatedToResponseHeadersPolicy.from_xml(
                error_el, message
            )
        case "TooManyDistributionsWithFunctionAssociations":
            raise capo_cloudfront.errors.too_many_distributions_with_function_associations.TooManyDistributionsWithFunctionAssociations.from_xml(
                error_el, message
            )
        case "TooManyDistributionsWithLambdaAssociations":
            raise capo_cloudfront.errors.too_many_distributions_with_lambda_associations.TooManyDistributionsWithLambdaAssociations.from_xml(
                error_el, message
            )
        case "TooManyDistributionsWithSingleFunctionARN":
            raise capo_cloudfront.errors.too_many_distributions_with_single_function_arn.TooManyDistributionsWithSingleFunctionARN.from_xml(
                error_el, message
            )
        case "TooManyFunctionAssociations":
            raise capo_cloudfront.errors.too_many_function_associations.TooManyFunctionAssociations.from_xml(
                error_el, message
            )
        case "TooManyHeadersInForwardedValues":
            raise capo_cloudfront.errors.too_many_headers_in_forwarded_values.TooManyHeadersInForwardedValues.from_xml(
                error_el, message
            )
        case "TooManyKeyGroupsAssociatedToDistribution":
            raise capo_cloudfront.errors.too_many_key_groups_associated_to_distribution.TooManyKeyGroupsAssociatedToDistribution.from_xml(
                error_el, message
            )
        case "TooManyLambdaFunctionAssociations":
            raise capo_cloudfront.errors.too_many_lambda_function_associations.TooManyLambdaFunctionAssociations.from_xml(
                error_el, message
            )
        case "TooManyOriginCustomHeaders":
            raise capo_cloudfront.errors.too_many_origin_custom_headers.TooManyOriginCustomHeaders.from_xml(
                error_el, message
            )
        case "TooManyOriginGroupsPerDistribution":
            raise capo_cloudfront.errors.too_many_origin_groups_per_distribution.TooManyOriginGroupsPerDistribution.from_xml(
                error_el, message
            )
        case "TooManyOrigins":
            raise capo_cloudfront.errors.too_many_origins.TooManyOrigins.from_xml(
                error_el, message
            )
        case "TooManyQueryStringParameters":
            raise capo_cloudfront.errors.too_many_query_string_parameters.TooManyQueryStringParameters.from_xml(
                error_el, message
            )
        case "TooManyTrustedSigners":
            raise capo_cloudfront.errors.too_many_trusted_signers.TooManyTrustedSigners.from_xml(
                error_el, message
            )
        case "TrustedKeyGroupDoesNotExist":
            raise capo_cloudfront.errors.trusted_key_group_does_not_exist.TrustedKeyGroupDoesNotExist.from_xml(
                error_el, message
            )
        case "TrustedSignerDoesNotExist":
            raise capo_cloudfront.errors.trusted_signer_does_not_exist.TrustedSignerDoesNotExist.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.create_distribution_with_tags_result.CreateDistributionWithTagsResult:
    out: capo_cloudfront.types.create_distribution_with_tags_result.CreateDistributionWithTagsResult = {
        "distribution": capo_cloudfront.types.distribution.deserialize_xml(
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
) -> capo_cloudfront.types.create_distribution_with_tags_result.CreateDistributionWithTagsResult:
    out: capo_cloudfront.types.create_distribution_with_tags_result.CreateDistributionWithTagsResult = {
        "distribution": capo_cloudfront.types.distribution.deserialize_xml(
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
    input_: capo_cloudfront.types.create_distribution_with_tags_request.CreateDistributionWithTagsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/distribution?WithTags"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    payload_root = Element("_")
    capo_cloudfront.types.distribution_config_with_tags.serialize_xml(
        input_["distribution_config_with_tags"],
        payload_root,
        "DistributionConfigWithTags",
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


def create_distribution_with_tags(
    options: OperationOptions,
    input_: capo_cloudfront.types.create_distribution_with_tags_request.CreateDistributionWithTagsRequest,
) -> tuple[
    capo_cloudfront.types.create_distribution_with_tags_result.CreateDistributionWithTagsResult,
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


async def async_create_distribution_with_tags(
    options: AsyncOperationOptions,
    input_: capo_cloudfront.types.create_distribution_with_tags_request.CreateDistributionWithTagsRequest,
) -> tuple[
    capo_cloudfront.types.create_distribution_with_tags_result.CreateDistributionWithTagsResult,
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
