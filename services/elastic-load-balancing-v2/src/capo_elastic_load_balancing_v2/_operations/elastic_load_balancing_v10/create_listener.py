"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CreateListener``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_elastic_load_balancing_v2._auth._signers
import capo_elastic_load_balancing_v2._auth._sigv4
import capo_elastic_load_balancing_v2._protocol.eventstream
import capo_elastic_load_balancing_v2.errors.alpn_policy_not_supported_exception
import capo_elastic_load_balancing_v2.errors.certificate_not_found_exception
import capo_elastic_load_balancing_v2.errors.duplicate_listener_exception
import capo_elastic_load_balancing_v2.errors.incompatible_protocols_exception
import capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception
import capo_elastic_load_balancing_v2.errors.invalid_load_balancer_action_exception
import capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception
import capo_elastic_load_balancing_v2.errors.ssl_policy_not_found_exception
import capo_elastic_load_balancing_v2.errors.target_group_association_limit_exception
import capo_elastic_load_balancing_v2.errors.target_group_not_found_exception
import capo_elastic_load_balancing_v2.errors.too_many_actions_exception
import capo_elastic_load_balancing_v2.errors.too_many_certificates_exception
import capo_elastic_load_balancing_v2.errors.too_many_listeners_exception
import capo_elastic_load_balancing_v2.errors.too_many_registrations_for_target_id_exception
import capo_elastic_load_balancing_v2.errors.too_many_tags_exception
import capo_elastic_load_balancing_v2.errors.too_many_targets_exception
import capo_elastic_load_balancing_v2.errors.too_many_unique_target_groups_per_load_balancer_exception
import capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception
import capo_elastic_load_balancing_v2.errors.trust_store_not_ready_exception
import capo_elastic_load_balancing_v2.errors.unsupported_protocol_exception
import capo_elastic_load_balancing_v2.types.actions
import capo_elastic_load_balancing_v2.types.alpn_policy_name
import capo_elastic_load_balancing_v2.types.certificate_list
import capo_elastic_load_balancing_v2.types.create_listener_input
import capo_elastic_load_balancing_v2.types.create_listener_output
import capo_elastic_load_balancing_v2.types.listeners
import capo_elastic_load_balancing_v2.types.mutual_authentication_attributes
import capo_elastic_load_balancing_v2.types.protocol_enum
import capo_elastic_load_balancing_v2.types.tag_list
from capo_elastic_load_balancing_v2._protocol.errors import (
    find_error_element,
    parse_error_metadata,
)
from capo_elastic_load_balancing_v2._protocol.xml import (
    fromstring,
)
from capo_elastic_load_balancing_v2._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_elastic_load_balancing_v2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_elastic_load_balancing_v2.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "ALPNPolicyNotFound":
            raise capo_elastic_load_balancing_v2.errors.alpn_policy_not_supported_exception.ALPNPolicyNotSupportedException.from_query(
                error_el, message
            )
        case "CertificateNotFound":
            raise capo_elastic_load_balancing_v2.errors.certificate_not_found_exception.CertificateNotFoundException.from_query(
                error_el, message
            )
        case "DuplicateListener":
            raise capo_elastic_load_balancing_v2.errors.duplicate_listener_exception.DuplicateListenerException.from_query(
                error_el, message
            )
        case "IncompatibleProtocols":
            raise capo_elastic_load_balancing_v2.errors.incompatible_protocols_exception.IncompatibleProtocolsException.from_query(
                error_el, message
            )
        case "InvalidConfigurationRequest":
            raise capo_elastic_load_balancing_v2.errors.invalid_configuration_request_exception.InvalidConfigurationRequestException.from_query(
                error_el, message
            )
        case "InvalidLoadBalancerAction":
            raise capo_elastic_load_balancing_v2.errors.invalid_load_balancer_action_exception.InvalidLoadBalancerActionException.from_query(
                error_el, message
            )
        case "LoadBalancerNotFound":
            raise capo_elastic_load_balancing_v2.errors.load_balancer_not_found_exception.LoadBalancerNotFoundException.from_query(
                error_el, message
            )
        case "SSLPolicyNotFound":
            raise capo_elastic_load_balancing_v2.errors.ssl_policy_not_found_exception.SSLPolicyNotFoundException.from_query(
                error_el, message
            )
        case "TargetGroupAssociationLimit":
            raise capo_elastic_load_balancing_v2.errors.target_group_association_limit_exception.TargetGroupAssociationLimitException.from_query(
                error_el, message
            )
        case "TargetGroupNotFound":
            raise capo_elastic_load_balancing_v2.errors.target_group_not_found_exception.TargetGroupNotFoundException.from_query(
                error_el, message
            )
        case "TooManyActions":
            raise capo_elastic_load_balancing_v2.errors.too_many_actions_exception.TooManyActionsException.from_query(
                error_el, message
            )
        case "TooManyCertificates":
            raise capo_elastic_load_balancing_v2.errors.too_many_certificates_exception.TooManyCertificatesException.from_query(
                error_el, message
            )
        case "TooManyListeners":
            raise capo_elastic_load_balancing_v2.errors.too_many_listeners_exception.TooManyListenersException.from_query(
                error_el, message
            )
        case "TooManyRegistrationsForTargetId":
            raise capo_elastic_load_balancing_v2.errors.too_many_registrations_for_target_id_exception.TooManyRegistrationsForTargetIdException.from_query(
                error_el, message
            )
        case "TooManyTags":
            raise capo_elastic_load_balancing_v2.errors.too_many_tags_exception.TooManyTagsException.from_query(
                error_el, message
            )
        case "TooManyTargets":
            raise capo_elastic_load_balancing_v2.errors.too_many_targets_exception.TooManyTargetsException.from_query(
                error_el, message
            )
        case "TooManyUniqueTargetGroupsPerLoadBalancer":
            raise capo_elastic_load_balancing_v2.errors.too_many_unique_target_groups_per_load_balancer_exception.TooManyUniqueTargetGroupsPerLoadBalancerException.from_query(
                error_el, message
            )
        case "TrustStoreNotFound":
            raise capo_elastic_load_balancing_v2.errors.trust_store_not_found_exception.TrustStoreNotFoundException.from_query(
                error_el, message
            )
        case "TrustStoreNotReady":
            raise capo_elastic_load_balancing_v2.errors.trust_store_not_ready_exception.TrustStoreNotReadyException.from_query(
                error_el, message
            )
        case "UnsupportedProtocol":
            raise capo_elastic_load_balancing_v2.errors.unsupported_protocol_exception.UnsupportedProtocolException.from_query(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_elastic_load_balancing_v2.types.create_listener_output.CreateListenerOutput:
    root = fromstring(response.read())
    result = root.find("CreateListenerResult")
    out: capo_elastic_load_balancing_v2.types.create_listener_output.CreateListenerOutput = capo_elastic_load_balancing_v2.types.create_listener_output.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_elastic_load_balancing_v2.types.create_listener_output.CreateListenerOutput:
    root = fromstring(await response.aread())
    result = root.find("CreateListenerResult")
    out: capo_elastic_load_balancing_v2.types.create_listener_output.CreateListenerOutput = capo_elastic_load_balancing_v2.types.create_listener_output.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_elastic_load_balancing_v2._auth._signers.Signer | None:
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
            sigv4_config = (
                capo_elastic_load_balancing_v2._auth._sigv4.build_sigv4_auth_scheme(
                    "elasticloadbalancing", options.region, endpoint_scheme
                )
            )
            if sigv4_config is not None:
                return capo_elastic_load_balancing_v2._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_elastic_load_balancing_v2.types.create_listener_input.CreateListenerInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "CreateListener"))
    pairs.append(("Version", "2015-12-01"))
    capo_elastic_load_balancing_v2.types.create_listener_input.serialize_query(
        input_, pairs, ""
    )
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
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


def create_listener(
    options: OperationOptions,
    input_: capo_elastic_load_balancing_v2.types.create_listener_input.CreateListenerInput,
) -> tuple[
    capo_elastic_load_balancing_v2.types.create_listener_output.CreateListenerOutput,
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


async def async_create_listener(
    options: AsyncOperationOptions,
    input_: capo_elastic_load_balancing_v2.types.create_listener_input.CreateListenerInput,
) -> tuple[
    capo_elastic_load_balancing_v2.types.create_listener_output.CreateListenerOutput,
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
