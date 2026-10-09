"""Generated from Smithy shape ``com.amazonaws.codecommit#TestRepositoryTriggers``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_codecommit._auth._signers
import capo_codecommit._auth._sigv4
import capo_codecommit._protocol.eventstream
import capo_codecommit.errors.encryption_integrity_checks_failed_exception
import capo_codecommit.errors.encryption_key_access_denied_exception
import capo_codecommit.errors.encryption_key_disabled_exception
import capo_codecommit.errors.encryption_key_not_found_exception
import capo_codecommit.errors.encryption_key_unavailable_exception
import capo_codecommit.errors.invalid_repository_name_exception
import capo_codecommit.errors.invalid_repository_trigger_branch_name_exception
import capo_codecommit.errors.invalid_repository_trigger_custom_data_exception
import capo_codecommit.errors.invalid_repository_trigger_destination_arn_exception
import capo_codecommit.errors.invalid_repository_trigger_events_exception
import capo_codecommit.errors.invalid_repository_trigger_name_exception
import capo_codecommit.errors.invalid_repository_trigger_region_exception
import capo_codecommit.errors.maximum_branches_exceeded_exception
import capo_codecommit.errors.maximum_repository_triggers_exceeded_exception
import capo_codecommit.errors.repository_does_not_exist_exception
import capo_codecommit.errors.repository_name_required_exception
import capo_codecommit.errors.repository_trigger_branch_name_list_required_exception
import capo_codecommit.errors.repository_trigger_destination_arn_required_exception
import capo_codecommit.errors.repository_trigger_events_list_required_exception
import capo_codecommit.errors.repository_trigger_name_required_exception
import capo_codecommit.errors.repository_triggers_list_required_exception
import capo_codecommit.types.repository_trigger_execution_failure_list
import capo_codecommit.types.repository_trigger_name_list
import capo_codecommit.types.repository_triggers_list
import capo_codecommit.types.test_repository_triggers_input
import capo_codecommit.types.test_repository_triggers_output
from capo_codecommit._protocol.errors import parse_error_metadata_json
from capo_codecommit._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_codecommit._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_codecommit.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "EncryptionIntegrityChecksFailedException":
            raise capo_codecommit.errors.encryption_integrity_checks_failed_exception.EncryptionIntegrityChecksFailedException.from_aws_json_1_1(
                data, message
            )
        case "EncryptionKeyAccessDeniedException":
            raise capo_codecommit.errors.encryption_key_access_denied_exception.EncryptionKeyAccessDeniedException.from_aws_json_1_1(
                data, message
            )
        case "EncryptionKeyDisabledException":
            raise capo_codecommit.errors.encryption_key_disabled_exception.EncryptionKeyDisabledException.from_aws_json_1_1(
                data, message
            )
        case "EncryptionKeyNotFoundException":
            raise capo_codecommit.errors.encryption_key_not_found_exception.EncryptionKeyNotFoundException.from_aws_json_1_1(
                data, message
            )
        case "EncryptionKeyUnavailableException":
            raise capo_codecommit.errors.encryption_key_unavailable_exception.EncryptionKeyUnavailableException.from_aws_json_1_1(
                data, message
            )
        case "InvalidRepositoryNameException":
            raise capo_codecommit.errors.invalid_repository_name_exception.InvalidRepositoryNameException.from_aws_json_1_1(
                data, message
            )
        case "InvalidRepositoryTriggerBranchNameException":
            raise capo_codecommit.errors.invalid_repository_trigger_branch_name_exception.InvalidRepositoryTriggerBranchNameException.from_aws_json_1_1(
                data, message
            )
        case "InvalidRepositoryTriggerCustomDataException":
            raise capo_codecommit.errors.invalid_repository_trigger_custom_data_exception.InvalidRepositoryTriggerCustomDataException.from_aws_json_1_1(
                data, message
            )
        case "InvalidRepositoryTriggerDestinationArnException":
            raise capo_codecommit.errors.invalid_repository_trigger_destination_arn_exception.InvalidRepositoryTriggerDestinationArnException.from_aws_json_1_1(
                data, message
            )
        case "InvalidRepositoryTriggerEventsException":
            raise capo_codecommit.errors.invalid_repository_trigger_events_exception.InvalidRepositoryTriggerEventsException.from_aws_json_1_1(
                data, message
            )
        case "InvalidRepositoryTriggerNameException":
            raise capo_codecommit.errors.invalid_repository_trigger_name_exception.InvalidRepositoryTriggerNameException.from_aws_json_1_1(
                data, message
            )
        case "InvalidRepositoryTriggerRegionException":
            raise capo_codecommit.errors.invalid_repository_trigger_region_exception.InvalidRepositoryTriggerRegionException.from_aws_json_1_1(
                data, message
            )
        case "MaximumBranchesExceededException":
            raise capo_codecommit.errors.maximum_branches_exceeded_exception.MaximumBranchesExceededException.from_aws_json_1_1(
                data, message
            )
        case "MaximumRepositoryTriggersExceededException":
            raise capo_codecommit.errors.maximum_repository_triggers_exceeded_exception.MaximumRepositoryTriggersExceededException.from_aws_json_1_1(
                data, message
            )
        case "RepositoryDoesNotExistException":
            raise capo_codecommit.errors.repository_does_not_exist_exception.RepositoryDoesNotExistException.from_aws_json_1_1(
                data, message
            )
        case "RepositoryNameRequiredException":
            raise capo_codecommit.errors.repository_name_required_exception.RepositoryNameRequiredException.from_aws_json_1_1(
                data, message
            )
        case "RepositoryTriggerBranchNameListRequiredException":
            raise capo_codecommit.errors.repository_trigger_branch_name_list_required_exception.RepositoryTriggerBranchNameListRequiredException.from_aws_json_1_1(
                data, message
            )
        case "RepositoryTriggerDestinationArnRequiredException":
            raise capo_codecommit.errors.repository_trigger_destination_arn_required_exception.RepositoryTriggerDestinationArnRequiredException.from_aws_json_1_1(
                data, message
            )
        case "RepositoryTriggerEventsListRequiredException":
            raise capo_codecommit.errors.repository_trigger_events_list_required_exception.RepositoryTriggerEventsListRequiredException.from_aws_json_1_1(
                data, message
            )
        case "RepositoryTriggerNameRequiredException":
            raise capo_codecommit.errors.repository_trigger_name_required_exception.RepositoryTriggerNameRequiredException.from_aws_json_1_1(
                data, message
            )
        case "RepositoryTriggersListRequiredException":
            raise capo_codecommit.errors.repository_triggers_list_required_exception.RepositoryTriggersListRequiredException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_codecommit.types.test_repository_triggers_output.TestRepositoryTriggersOutput:
    out: capo_codecommit.types.test_repository_triggers_output.TestRepositoryTriggersOutput = capo_codecommit.types.test_repository_triggers_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_codecommit.types.test_repository_triggers_output.TestRepositoryTriggersOutput:
    out: capo_codecommit.types.test_repository_triggers_output.TestRepositoryTriggersOutput = capo_codecommit.types.test_repository_triggers_output.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_codecommit._auth._signers.Signer | None:
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
            sigv4_config = capo_codecommit._auth._sigv4.build_sigv4_auth_scheme(
                "codecommit", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_codecommit._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_codecommit.types.test_repository_triggers_input.TestRepositoryTriggersInput,
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
    headers["X-Amz-Target"] = "CodeCommit_20150413.TestRepositoryTriggers"
    body: bytes | None = json.dumps(
        capo_codecommit.types.test_repository_triggers_input.serialize_aws_json_1_1(
            input_
        ),
        allow_nan=False,
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
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


def test_repository_triggers(
    options: OperationOptions,
    input_: capo_codecommit.types.test_repository_triggers_input.TestRepositoryTriggersInput,
) -> tuple[
    capo_codecommit.types.test_repository_triggers_output.TestRepositoryTriggersOutput,
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


async def async_test_repository_triggers(
    options: AsyncOperationOptions,
    input_: capo_codecommit.types.test_repository_triggers_input.TestRepositoryTriggersInput,
) -> tuple[
    capo_codecommit.types.test_repository_triggers_output.TestRepositoryTriggersOutput,
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
