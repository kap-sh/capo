"""Generated from Smithy shape ``com.amazonaws.codecommit#CreateCommit``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_codecommit._auth._signers
import capo_codecommit._auth._sigv4
import capo_codecommit._protocol.eventstream
import capo_codecommit.errors.branch_does_not_exist_exception
import capo_codecommit.errors.branch_name_is_tag_name_exception
import capo_codecommit.errors.branch_name_required_exception
import capo_codecommit.errors.commit_message_length_exceeded_exception
import capo_codecommit.errors.directory_name_conflicts_with_file_name_exception
import capo_codecommit.errors.encryption_integrity_checks_failed_exception
import capo_codecommit.errors.encryption_key_access_denied_exception
import capo_codecommit.errors.encryption_key_disabled_exception
import capo_codecommit.errors.encryption_key_not_found_exception
import capo_codecommit.errors.encryption_key_unavailable_exception
import capo_codecommit.errors.file_content_and_source_file_specified_exception
import capo_codecommit.errors.file_content_size_limit_exceeded_exception
import capo_codecommit.errors.file_does_not_exist_exception
import capo_codecommit.errors.file_entry_required_exception
import capo_codecommit.errors.file_mode_required_exception
import capo_codecommit.errors.file_name_conflicts_with_directory_name_exception
import capo_codecommit.errors.file_path_conflicts_with_submodule_path_exception
import capo_codecommit.errors.folder_content_size_limit_exceeded_exception
import capo_codecommit.errors.invalid_branch_name_exception
import capo_codecommit.errors.invalid_deletion_parameter_exception
import capo_codecommit.errors.invalid_email_exception
import capo_codecommit.errors.invalid_file_mode_exception
import capo_codecommit.errors.invalid_parent_commit_id_exception
import capo_codecommit.errors.invalid_path_exception
import capo_codecommit.errors.invalid_repository_name_exception
import capo_codecommit.errors.maximum_file_entries_exceeded_exception
import capo_codecommit.errors.name_length_exceeded_exception
import capo_codecommit.errors.no_change_exception
import capo_codecommit.errors.parent_commit_does_not_exist_exception
import capo_codecommit.errors.parent_commit_id_outdated_exception
import capo_codecommit.errors.parent_commit_id_required_exception
import capo_codecommit.errors.path_required_exception
import capo_codecommit.errors.put_file_entry_conflict_exception
import capo_codecommit.errors.repository_does_not_exist_exception
import capo_codecommit.errors.repository_name_required_exception
import capo_codecommit.errors.restricted_source_file_exception
import capo_codecommit.errors.same_path_request_exception
import capo_codecommit.errors.source_file_or_content_required_exception
import capo_codecommit.types.create_commit_input
import capo_codecommit.types.create_commit_output
import capo_codecommit.types.delete_file_entries
import capo_codecommit.types.files_metadata
import capo_codecommit.types.put_file_entries
import capo_codecommit.types.set_file_mode_entries
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
        case "BranchDoesNotExistException":
            raise capo_codecommit.errors.branch_does_not_exist_exception.BranchDoesNotExistException.from_aws_json_1_1(
                data, message
            )
        case "BranchNameIsTagNameException":
            raise capo_codecommit.errors.branch_name_is_tag_name_exception.BranchNameIsTagNameException.from_aws_json_1_1(
                data, message
            )
        case "BranchNameRequiredException":
            raise capo_codecommit.errors.branch_name_required_exception.BranchNameRequiredException.from_aws_json_1_1(
                data, message
            )
        case "CommitMessageLengthExceededException":
            raise capo_codecommit.errors.commit_message_length_exceeded_exception.CommitMessageLengthExceededException.from_aws_json_1_1(
                data, message
            )
        case "DirectoryNameConflictsWithFileNameException":
            raise capo_codecommit.errors.directory_name_conflicts_with_file_name_exception.DirectoryNameConflictsWithFileNameException.from_aws_json_1_1(
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
        case "FileContentAndSourceFileSpecifiedException":
            raise capo_codecommit.errors.file_content_and_source_file_specified_exception.FileContentAndSourceFileSpecifiedException.from_aws_json_1_1(
                data, message
            )
        case "FileContentSizeLimitExceededException":
            raise capo_codecommit.errors.file_content_size_limit_exceeded_exception.FileContentSizeLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "FileDoesNotExistException":
            raise capo_codecommit.errors.file_does_not_exist_exception.FileDoesNotExistException.from_aws_json_1_1(
                data, message
            )
        case "FileEntryRequiredException":
            raise capo_codecommit.errors.file_entry_required_exception.FileEntryRequiredException.from_aws_json_1_1(
                data, message
            )
        case "FileModeRequiredException":
            raise capo_codecommit.errors.file_mode_required_exception.FileModeRequiredException.from_aws_json_1_1(
                data, message
            )
        case "FileNameConflictsWithDirectoryNameException":
            raise capo_codecommit.errors.file_name_conflicts_with_directory_name_exception.FileNameConflictsWithDirectoryNameException.from_aws_json_1_1(
                data, message
            )
        case "FilePathConflictsWithSubmodulePathException":
            raise capo_codecommit.errors.file_path_conflicts_with_submodule_path_exception.FilePathConflictsWithSubmodulePathException.from_aws_json_1_1(
                data, message
            )
        case "FolderContentSizeLimitExceededException":
            raise capo_codecommit.errors.folder_content_size_limit_exceeded_exception.FolderContentSizeLimitExceededException.from_aws_json_1_1(
                data, message
            )
        case "InvalidBranchNameException":
            raise capo_codecommit.errors.invalid_branch_name_exception.InvalidBranchNameException.from_aws_json_1_1(
                data, message
            )
        case "InvalidDeletionParameterException":
            raise capo_codecommit.errors.invalid_deletion_parameter_exception.InvalidDeletionParameterException.from_aws_json_1_1(
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
        case "InvalidParentCommitIdException":
            raise capo_codecommit.errors.invalid_parent_commit_id_exception.InvalidParentCommitIdException.from_aws_json_1_1(
                data, message
            )
        case "InvalidPathException":
            raise capo_codecommit.errors.invalid_path_exception.InvalidPathException.from_aws_json_1_1(
                data, message
            )
        case "InvalidRepositoryNameException":
            raise capo_codecommit.errors.invalid_repository_name_exception.InvalidRepositoryNameException.from_aws_json_1_1(
                data, message
            )
        case "MaximumFileEntriesExceededException":
            raise capo_codecommit.errors.maximum_file_entries_exceeded_exception.MaximumFileEntriesExceededException.from_aws_json_1_1(
                data, message
            )
        case "NameLengthExceededException":
            raise capo_codecommit.errors.name_length_exceeded_exception.NameLengthExceededException.from_aws_json_1_1(
                data, message
            )
        case "NoChangeException":
            raise capo_codecommit.errors.no_change_exception.NoChangeException.from_aws_json_1_1(
                data, message
            )
        case "ParentCommitDoesNotExistException":
            raise capo_codecommit.errors.parent_commit_does_not_exist_exception.ParentCommitDoesNotExistException.from_aws_json_1_1(
                data, message
            )
        case "ParentCommitIdOutdatedException":
            raise capo_codecommit.errors.parent_commit_id_outdated_exception.ParentCommitIdOutdatedException.from_aws_json_1_1(
                data, message
            )
        case "ParentCommitIdRequiredException":
            raise capo_codecommit.errors.parent_commit_id_required_exception.ParentCommitIdRequiredException.from_aws_json_1_1(
                data, message
            )
        case "PathRequiredException":
            raise capo_codecommit.errors.path_required_exception.PathRequiredException.from_aws_json_1_1(
                data, message
            )
        case "PutFileEntryConflictException":
            raise capo_codecommit.errors.put_file_entry_conflict_exception.PutFileEntryConflictException.from_aws_json_1_1(
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
        case "RestrictedSourceFileException":
            raise capo_codecommit.errors.restricted_source_file_exception.RestrictedSourceFileException.from_aws_json_1_1(
                data, message
            )
        case "SamePathRequestException":
            raise capo_codecommit.errors.same_path_request_exception.SamePathRequestException.from_aws_json_1_1(
                data, message
            )
        case "SourceFileOrContentRequiredException":
            raise capo_codecommit.errors.source_file_or_content_required_exception.SourceFileOrContentRequiredException.from_aws_json_1_1(
                data, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_codecommit.types.create_commit_output.CreateCommitOutput:
    out: capo_codecommit.types.create_commit_output.CreateCommitOutput = (
        capo_codecommit.types.create_commit_output.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_codecommit.types.create_commit_output.CreateCommitOutput:
    out: capo_codecommit.types.create_commit_output.CreateCommitOutput = (
        capo_codecommit.types.create_commit_output.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
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
    input_: capo_codecommit.types.create_commit_input.CreateCommitInput,
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
    headers["X-Amz-Target"] = "CodeCommit_20150413.CreateCommit"
    body: bytes | None = json.dumps(
        capo_codecommit.types.create_commit_input.serialize_aws_json_1_1(input_),
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


def create_commit(
    options: OperationOptions,
    input_: capo_codecommit.types.create_commit_input.CreateCommitInput,
) -> tuple[
    capo_codecommit.types.create_commit_output.CreateCommitOutput, zapros.Response
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


async def async_create_commit(
    options: AsyncOperationOptions,
    input_: capo_codecommit.types.create_commit_input.CreateCommitInput,
) -> tuple[
    capo_codecommit.types.create_commit_output.CreateCommitOutput, zapros.Response
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
