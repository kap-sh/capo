"""Generated from Smithy shape ``com.amazonaws.codecommit#MergePullRequestBySquash``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_codecommit._auth._signers
import capo_codecommit._auth._sigv4
import capo_codecommit._protocol.eventstream
import capo_codecommit.errors.commit_message_length_exceeded_exception
import capo_codecommit.errors.concurrent_reference_update_exception
import capo_codecommit.errors.encryption_integrity_checks_failed_exception
import capo_codecommit.errors.encryption_key_access_denied_exception
import capo_codecommit.errors.encryption_key_disabled_exception
import capo_codecommit.errors.encryption_key_not_found_exception
import capo_codecommit.errors.encryption_key_unavailable_exception
import capo_codecommit.errors.file_content_size_limit_exceeded_exception
import capo_codecommit.errors.folder_content_size_limit_exceeded_exception
import capo_codecommit.errors.invalid_commit_id_exception
import capo_codecommit.errors.invalid_conflict_detail_level_exception
import capo_codecommit.errors.invalid_conflict_resolution_exception
import capo_codecommit.errors.invalid_conflict_resolution_strategy_exception
import capo_codecommit.errors.invalid_email_exception
import capo_codecommit.errors.invalid_file_mode_exception
import capo_codecommit.errors.invalid_path_exception
import capo_codecommit.errors.invalid_pull_request_id_exception
import capo_codecommit.errors.invalid_replacement_content_exception
import capo_codecommit.errors.invalid_replacement_type_exception
import capo_codecommit.errors.invalid_repository_name_exception
import capo_codecommit.errors.manual_merge_required_exception
import capo_codecommit.errors.maximum_conflict_resolution_entries_exceeded_exception
import capo_codecommit.errors.maximum_file_content_to_load_exceeded_exception
import capo_codecommit.errors.maximum_items_to_compare_exceeded_exception
import capo_codecommit.errors.multiple_conflict_resolution_entries_exception
import capo_codecommit.errors.name_length_exceeded_exception
import capo_codecommit.errors.path_required_exception
import capo_codecommit.errors.pull_request_already_closed_exception
import capo_codecommit.errors.pull_request_approval_rules_not_satisfied_exception
import capo_codecommit.errors.pull_request_does_not_exist_exception
import capo_codecommit.errors.pull_request_id_required_exception
import capo_codecommit.errors.replacement_content_required_exception
import capo_codecommit.errors.replacement_type_required_exception
import capo_codecommit.errors.repository_does_not_exist_exception
import capo_codecommit.errors.repository_name_required_exception
import capo_codecommit.errors.repository_not_associated_with_pull_request_exception
import capo_codecommit.errors.tip_of_source_reference_is_different_exception
import capo_codecommit.errors.tips_divergence_exceeded_exception
import capo_codecommit.types.conflict_detail_level_type_enum
import capo_codecommit.types.conflict_resolution
import capo_codecommit.types.conflict_resolution_strategy_type_enum
import capo_codecommit.types.merge_pull_request_by_squash_input
import capo_codecommit.types.merge_pull_request_by_squash_output
import capo_codecommit.types.pull_request
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
        case "CommitMessageLengthExceededException":
            raise capo_codecommit.errors.commit_message_length_exceeded_exception.CommitMessageLengthExceededException.from_aws_json_1_1(
                data, message
            )
        case "ConcurrentReferenceUpdateException":
            raise capo_codecommit.errors.concurrent_reference_update_exception.ConcurrentReferenceUpdateException.from_aws_json_1_1(
                data, message
            )
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
        case "FileContentSizeLimitExceededException":
            raise capo_codecommit.errors.file_content_size_limit_exceeded_exception.FileContentSizeLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "FolderContentSizeLimitExceededException":
            raise capo_codecommit.errors.folder_content_size_limit_exceeded_exception.FolderContentSizeLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "InvalidCommitIdException":
            raise capo_codecommit.errors.invalid_commit_id_exception.InvalidCommitIdException.from_aws_json_1_1(
                data, message
            )
        case "InvalidConflictDetailLevelException":
            raise capo_codecommit.errors.invalid_conflict_detail_level_exception.InvalidConflictDetailLevelException.from_aws_json_1_1(
                data, message
            )
        case "InvalidConflictResolutionException":
            raise capo_codecommit.errors.invalid_conflict_resolution_exception.InvalidConflictResolutionException.from_aws_json_1_1(
                data, message
            )
        case "InvalidConflictResolutionStrategyException":
            raise capo_codecommit.errors.invalid_conflict_resolution_strategy_exception.InvalidConflictResolutionStrategyException.from_aws_json_1_1(
                data, message
            )
        case "InvalidEmailException":
            raise capo_codecommit.errors.invalid_email_exception.InvalidEmailException.from_aws_json_1_1(
                data, message
            )
        case "InvalidFileModeException":
            raise capo_codecommit.errors.invalid_file_mode_exception.InvalidFileModeException.from_aws_json_1_1(
                data, message
            )
        case "InvalidPathException":
            raise capo_codecommit.errors.invalid_path_exception.InvalidPathException.from_aws_json_1_1(
                data, message
            )
        case "InvalidPullRequestIdException":
            raise capo_codecommit.errors.invalid_pull_request_id_exception.InvalidPullRequestIdException.from_aws_json_1_1(
                data, message
            )
        case "InvalidReplacementContentException":
            raise capo_codecommit.errors.invalid_replacement_content_exception.InvalidReplacementContentException.from_aws_json_1_1(
                data, message
            )
        case "InvalidReplacementTypeException":
            raise capo_codecommit.errors.invalid_replacement_type_exception.InvalidReplacementTypeException.from_aws_json_1_1(
                data, message
            )
        case "InvalidRepositoryNameException":
            raise capo_codecommit.errors.invalid_repository_name_exception.InvalidRepositoryNameException.from_aws_json_1_1(
                data, message
            )
        case "ManualMergeRequiredException":
            raise capo_codecommit.errors.manual_merge_required_exception.ManualMergeRequiredException.from_aws_json_1_1(
                data, message
            )
        case "MaximumConflictResolutionEntriesExceededException":
            raise capo_codecommit.errors.maximum_conflict_resolution_entries_exceeded_exception.MaximumConflictResolutionEntriesExceededException.from_aws_json_1_1(
                data, message
            )
        case "MaximumFileContentToLoadExceededException":
            raise capo_codecommit.errors.maximum_file_content_to_load_exceeded_exception.MaximumFileContentToLoadExceededException.from_aws_json_1_1(
                data, message
            )
        case "MaximumItemsToCompareExceededException":
            raise capo_codecommit.errors.maximum_items_to_compare_exceeded_exception.MaximumItemsToCompareExceededException.from_aws_json_1_1(
                data, message
            )
        case "MultipleConflictResolutionEntriesException":
            raise capo_codecommit.errors.multiple_conflict_resolution_entries_exception.MultipleConflictResolutionEntriesException.from_aws_json_1_1(
                data, message
            )
        case "NameLengthExceededException":
            raise capo_codecommit.errors.name_length_exceeded_exception.NameLengthExceededException.from_aws_json_1_1(
                data, message
            )
        case "PathRequiredException":
            raise capo_codecommit.errors.path_required_exception.PathRequiredException.from_aws_json_1_1(
                data, message
            )
        case "PullRequestAlreadyClosedException":
            raise capo_codecommit.errors.pull_request_already_closed_exception.PullRequestAlreadyClosedException.from_aws_json_1_1(
                data, message
            )
        case "PullRequestApprovalRulesNotSatisfiedException":
            raise capo_codecommit.errors.pull_request_approval_rules_not_satisfied_exception.PullRequestApprovalRulesNotSatisfiedException.from_aws_json_1_1(
                data, message
            )
        case "PullRequestDoesNotExistException":
            raise capo_codecommit.errors.pull_request_does_not_exist_exception.PullRequestDoesNotExistException.from_aws_json_1_1(
                data, message
            )
        case "PullRequestIdRequiredException":
            raise capo_codecommit.errors.pull_request_id_required_exception.PullRequestIdRequiredException.from_aws_json_1_1(
                data, message
            )
        case "ReplacementContentRequiredException":
            raise capo_codecommit.errors.replacement_content_required_exception.ReplacementContentRequiredException.from_aws_json_1_1(
                data, message
            )
        case "ReplacementTypeRequiredException":
            raise capo_codecommit.errors.replacement_type_required_exception.ReplacementTypeRequiredException.from_aws_json_1_1(
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
        case "RepositoryNotAssociatedWithPullRequestException":
            raise capo_codecommit.errors.repository_not_associated_with_pull_request_exception.RepositoryNotAssociatedWithPullRequestException.from_aws_json_1_1(
                data, message
            )
        case "TipOfSourceReferenceIsDifferentException":
            raise capo_codecommit.errors.tip_of_source_reference_is_different_exception.TipOfSourceReferenceIsDifferentException.from_aws_json_1_1(
                data, message
            )
        case "TipsDivergenceExceededException":
            raise capo_codecommit.errors.tips_divergence_exceeded_exception.TipsDivergenceExceededException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_codecommit.types.merge_pull_request_by_squash_output.MergePullRequestBySquashOutput:
    out: capo_codecommit.types.merge_pull_request_by_squash_output.MergePullRequestBySquashOutput = capo_codecommit.types.merge_pull_request_by_squash_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_codecommit.types.merge_pull_request_by_squash_output.MergePullRequestBySquashOutput:
    out: capo_codecommit.types.merge_pull_request_by_squash_output.MergePullRequestBySquashOutput = capo_codecommit.types.merge_pull_request_by_squash_output.deserialize_aws_json_1_1(
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
    input_: capo_codecommit.types.merge_pull_request_by_squash_input.MergePullRequestBySquashInput,
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
    headers["X-Amz-Target"] = "CodeCommit_20150413.MergePullRequestBySquash"
    body: bytes | None = json.dumps(
        capo_codecommit.types.merge_pull_request_by_squash_input.serialize_aws_json_1_1(
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


def merge_pull_request_by_squash(
    options: OperationOptions,
    input_: capo_codecommit.types.merge_pull_request_by_squash_input.MergePullRequestBySquashInput,
) -> tuple[
    capo_codecommit.types.merge_pull_request_by_squash_output.MergePullRequestBySquashOutput,
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


async def async_merge_pull_request_by_squash(
    options: AsyncOperationOptions,
    input_: capo_codecommit.types.merge_pull_request_by_squash_input.MergePullRequestBySquashInput,
) -> tuple[
    capo_codecommit.types.merge_pull_request_by_squash_output.MergePullRequestBySquashOutput,
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
