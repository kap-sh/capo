"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBInstance``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_rds._auth._signers
import capo_rds._auth._sigv4
import capo_rds._protocol.eventstream
import capo_rds.errors.authorization_not_found_fault
import capo_rds.errors.backup_policy_not_found_fault
import capo_rds.errors.certificate_not_found_fault
import capo_rds.errors.db_instance_already_exists_fault
import capo_rds.errors.db_instance_not_found_fault
import capo_rds.errors.db_parameter_group_not_found_fault
import capo_rds.errors.db_security_group_not_found_fault
import capo_rds.errors.db_upgrade_dependency_failure_fault
import capo_rds.errors.domain_not_found_fault
import capo_rds.errors.insufficient_db_instance_capacity_fault
import capo_rds.errors.invalid_db_cluster_state_fault
import capo_rds.errors.invalid_db_instance_state_fault
import capo_rds.errors.invalid_db_security_group_state_fault
import capo_rds.errors.invalid_vpc_network_state_fault
import capo_rds.errors.kms_key_not_accessible_fault
import capo_rds.errors.network_type_not_supported
import capo_rds.errors.option_group_not_found_fault
import capo_rds.errors.provisioned_iops_not_available_in_az_fault
import capo_rds.errors.storage_quota_exceeded_fault
import capo_rds.errors.storage_type_not_supported_fault
import capo_rds.errors.tenant_database_quota_exceeded_fault
import capo_rds.errors.vpc_encryption_control_violation_exception
import capo_rds.types.automation_mode
import capo_rds.types.cloudwatch_logs_export_configuration
import capo_rds.types.database_insights_mode
import capo_rds.types.db_instance
import capo_rds.types.db_security_group_name_list
import capo_rds.types.master_user_authentication_type
import capo_rds.types.modify_additional_storage_volumes_list
import capo_rds.types.modify_db_instance_message
import capo_rds.types.modify_db_instance_result
import capo_rds.types.processor_feature_list
import capo_rds.types.replica_mode
import capo_rds.types.string_list
import capo_rds.types.tag_specification_list
import capo_rds.types.vpc_security_group_id_list
from capo_rds._protocol.errors import find_error_element, parse_error_metadata
from capo_rds._protocol.xml import fromstring
from capo_rds._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_rds._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_rds.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "AuthorizationNotFound":
            raise capo_rds.errors.authorization_not_found_fault.AuthorizationNotFoundFault.from_query(
                error_el, message
            )
        case "BackupPolicyNotFoundFault":
            raise capo_rds.errors.backup_policy_not_found_fault.BackupPolicyNotFoundFault.from_query(
                error_el, message
            )
        case "CertificateNotFound":
            raise capo_rds.errors.certificate_not_found_fault.CertificateNotFoundFault.from_query(
                error_el, message
            )
        case "DBInstanceAlreadyExists":
            raise capo_rds.errors.db_instance_already_exists_fault.DBInstanceAlreadyExistsFault.from_query(
                error_el, message
            )
        case "DBInstanceNotFound":
            raise capo_rds.errors.db_instance_not_found_fault.DBInstanceNotFoundFault.from_query(
                error_el, message
            )
        case "DBParameterGroupNotFound":
            raise capo_rds.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault.from_query(
                error_el, message
            )
        case "DBSecurityGroupNotFound":
            raise capo_rds.errors.db_security_group_not_found_fault.DBSecurityGroupNotFoundFault.from_query(
                error_el, message
            )
        case "DBUpgradeDependencyFailure":
            raise capo_rds.errors.db_upgrade_dependency_failure_fault.DBUpgradeDependencyFailureFault.from_query(
                error_el, message
            )
        case "DomainNotFoundFault":
            raise capo_rds.errors.domain_not_found_fault.DomainNotFoundFault.from_query(
                error_el, message
            )
        case "InsufficientDBInstanceCapacity":
            raise capo_rds.errors.insufficient_db_instance_capacity_fault.InsufficientDBInstanceCapacityFault.from_query(
                error_el, message
            )
        case "InvalidDBClusterStateFault":
            raise capo_rds.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault.from_query(
                error_el, message
            )
        case "InvalidDBInstanceState":
            raise capo_rds.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault.from_query(
                error_el, message
            )
        case "InvalidDBSecurityGroupState":
            raise capo_rds.errors.invalid_db_security_group_state_fault.InvalidDBSecurityGroupStateFault.from_query(
                error_el, message
            )
        case "InvalidVPCNetworkStateFault":
            raise capo_rds.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault.from_query(
                error_el, message
            )
        case "KMSKeyNotAccessibleFault":
            raise capo_rds.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault.from_query(
                error_el, message
            )
        case "NetworkTypeNotSupported":
            raise capo_rds.errors.network_type_not_supported.NetworkTypeNotSupported.from_query(
                error_el, message
            )
        case "OptionGroupNotFoundFault":
            raise capo_rds.errors.option_group_not_found_fault.OptionGroupNotFoundFault.from_query(
                error_el, message
            )
        case "ProvisionedIopsNotAvailableInAZFault":
            raise capo_rds.errors.provisioned_iops_not_available_in_az_fault.ProvisionedIopsNotAvailableInAZFault.from_query(
                error_el, message
            )
        case "StorageQuotaExceeded":
            raise capo_rds.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault.from_query(
                error_el, message
            )
        case "StorageTypeNotSupported":
            raise capo_rds.errors.storage_type_not_supported_fault.StorageTypeNotSupportedFault.from_query(
                error_el, message
            )
        case "TenantDatabaseQuotaExceeded":
            raise capo_rds.errors.tenant_database_quota_exceeded_fault.TenantDatabaseQuotaExceededFault.from_query(
                error_el, message
            )
        case "VpcEncryptionControlViolationException":
            raise capo_rds.errors.vpc_encryption_control_violation_exception.VpcEncryptionControlViolationException.from_query(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_rds.types.modify_db_instance_result.ModifyDBInstanceResult:
    root = fromstring(response.read())
    result = root.find("ModifyDBInstanceResult")
    out: capo_rds.types.modify_db_instance_result.ModifyDBInstanceResult = (
        capo_rds.types.modify_db_instance_result.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_rds.types.modify_db_instance_result.ModifyDBInstanceResult:
    root = fromstring(await response.aread())
    result = root.find("ModifyDBInstanceResult")
    out: capo_rds.types.modify_db_instance_result.ModifyDBInstanceResult = (
        capo_rds.types.modify_db_instance_result.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_rds._auth._signers.Signer | None:
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
            sigv4_config = capo_rds._auth._sigv4.build_sigv4_auth_scheme(
                "rds", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_rds._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_rds.types.modify_db_instance_message.ModifyDBInstanceMessage,
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
    pairs.append(("Action", "ModifyDBInstance"))
    pairs.append(("Version", "2014-10-31"))
    capo_rds.types.modify_db_instance_message.serialize_query(input_, pairs, "")
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


def modify_db_instance(
    options: OperationOptions,
    input_: capo_rds.types.modify_db_instance_message.ModifyDBInstanceMessage,
) -> tuple[
    capo_rds.types.modify_db_instance_result.ModifyDBInstanceResult, zapros.Response
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


async def async_modify_db_instance(
    options: AsyncOperationOptions,
    input_: capo_rds.types.modify_db_instance_message.ModifyDBInstanceMessage,
) -> tuple[
    capo_rds.types.modify_db_instance_result.ModifyDBInstanceResult, zapros.Response
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
