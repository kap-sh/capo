"""Generated from Smithy shape ``com.amazonaws.docdb#CreateEventSubscription``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_docdb._auth._signers
import capo_docdb._auth._sigv4
import capo_docdb._protocol.eventstream
import capo_docdb.errors.event_subscription_quota_exceeded_fault
import capo_docdb.errors.sns_invalid_topic_fault
import capo_docdb.errors.sns_no_authorization_fault
import capo_docdb.errors.sns_topic_arn_not_found_fault
import capo_docdb.errors.source_not_found_fault
import capo_docdb.errors.subscription_already_exist_fault
import capo_docdb.errors.subscription_category_not_found_fault
import capo_docdb.types.create_event_subscription_message
import capo_docdb.types.create_event_subscription_result
import capo_docdb.types.event_categories_list
import capo_docdb.types.event_subscription
import capo_docdb.types.source_ids_list
import capo_docdb.types.tag_list
from capo_docdb._protocol.errors import find_error_element, parse_error_metadata
from capo_docdb._protocol.xml import fromstring
from capo_docdb._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_docdb._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_docdb.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "EventSubscriptionQuotaExceeded":
            raise capo_docdb.errors.event_subscription_quota_exceeded_fault.EventSubscriptionQuotaExceededFault.from_query(
                error_el, message
            )
        case "SNSInvalidTopic":
            raise capo_docdb.errors.sns_invalid_topic_fault.SNSInvalidTopicFault.from_query(
                error_el, message
            )
        case "SNSNoAuthorization":
            raise capo_docdb.errors.sns_no_authorization_fault.SNSNoAuthorizationFault.from_query(
                error_el, message
            )
        case "SNSTopicArnNotFound":
            raise capo_docdb.errors.sns_topic_arn_not_found_fault.SNSTopicArnNotFoundFault.from_query(
                error_el, message
            )
        case "SourceNotFound":
            raise capo_docdb.errors.source_not_found_fault.SourceNotFoundFault.from_query(
                error_el, message
            )
        case "SubscriptionAlreadyExist":
            raise capo_docdb.errors.subscription_already_exist_fault.SubscriptionAlreadyExistFault.from_query(
                error_el, message
            )
        case "SubscriptionCategoryNotFound":
            raise capo_docdb.errors.subscription_category_not_found_fault.SubscriptionCategoryNotFoundFault.from_query(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_docdb.types.create_event_subscription_result.CreateEventSubscriptionResult:
    root = fromstring(response.read())
    result = root.find("CreateEventSubscriptionResult")
    out: capo_docdb.types.create_event_subscription_result.CreateEventSubscriptionResult = capo_docdb.types.create_event_subscription_result.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_docdb.types.create_event_subscription_result.CreateEventSubscriptionResult:
    root = fromstring(await response.aread())
    result = root.find("CreateEventSubscriptionResult")
    out: capo_docdb.types.create_event_subscription_result.CreateEventSubscriptionResult = capo_docdb.types.create_event_subscription_result.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_docdb._auth._signers.Signer | None:
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
            sigv4_config = capo_docdb._auth._sigv4.build_sigv4_auth_scheme(
                "rds", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_docdb._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_docdb.types.create_event_subscription_message.CreateEventSubscriptionMessage,
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
    pairs.append(("Action", "CreateEventSubscription"))
    pairs.append(("Version", "2014-10-31"))
    capo_docdb.types.create_event_subscription_message.serialize_query(
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


def create_event_subscription(
    options: OperationOptions,
    input_: capo_docdb.types.create_event_subscription_message.CreateEventSubscriptionMessage,
) -> tuple[
    capo_docdb.types.create_event_subscription_result.CreateEventSubscriptionResult,
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


async def async_create_event_subscription(
    options: AsyncOperationOptions,
    input_: capo_docdb.types.create_event_subscription_message.CreateEventSubscriptionMessage,
) -> tuple[
    capo_docdb.types.create_event_subscription_result.CreateEventSubscriptionResult,
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
