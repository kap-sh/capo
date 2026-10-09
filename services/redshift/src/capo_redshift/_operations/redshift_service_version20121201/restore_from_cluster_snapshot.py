"""Generated from Smithy shape ``com.amazonaws.redshift#RestoreFromClusterSnapshot``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import capo_redshift._auth._signers
import capo_redshift._auth._sigv4
import capo_redshift._protocol.eventstream
import capo_redshift.errors.access_to_snapshot_denied_fault
import capo_redshift.errors.cluster_already_exists_fault
import capo_redshift.errors.cluster_parameter_group_not_found_fault
import capo_redshift.errors.cluster_quota_exceeded_fault
import capo_redshift.errors.cluster_security_group_not_found_fault
import capo_redshift.errors.cluster_snapshot_not_found_fault
import capo_redshift.errors.cluster_subnet_group_not_found_fault
import capo_redshift.errors.dependent_service_access_denied_fault
import capo_redshift.errors.dependent_service_request_throttling_fault
import capo_redshift.errors.dependent_service_unavailable_fault
import capo_redshift.errors.hsm_client_certificate_not_found_fault
import capo_redshift.errors.hsm_configuration_not_found_fault
import capo_redshift.errors.insufficient_cluster_capacity_fault
import capo_redshift.errors.invalid_cluster_snapshot_state_fault
import capo_redshift.errors.invalid_cluster_subnet_group_state_fault
import capo_redshift.errors.invalid_cluster_track_fault
import capo_redshift.errors.invalid_elastic_ip_fault
import capo_redshift.errors.invalid_reserved_node_state_fault
import capo_redshift.errors.invalid_restore_fault
import capo_redshift.errors.invalid_subnet
import capo_redshift.errors.invalid_tag_fault
import capo_redshift.errors.invalid_vpc_network_state_fault
import capo_redshift.errors.ipv6_cidr_block_not_found_fault
import capo_redshift.errors.limit_exceeded_fault
import capo_redshift.errors.number_of_nodes_per_cluster_limit_exceeded_fault
import capo_redshift.errors.number_of_nodes_quota_exceeded_fault
import capo_redshift.errors.redshift_idc_application_not_exists_fault
import capo_redshift.errors.reserved_node_already_exists_fault
import capo_redshift.errors.reserved_node_already_migrated_fault
import capo_redshift.errors.reserved_node_not_found_fault
import capo_redshift.errors.reserved_node_offering_not_found_fault
import capo_redshift.errors.snapshot_schedule_not_found_fault
import capo_redshift.errors.tag_limit_exceeded_fault
import capo_redshift.errors.unauthorized_operation
import capo_redshift.errors.unsupported_operation_fault
import capo_redshift.types.aqua_configuration_status
import capo_redshift.types.cluster
import capo_redshift.types.cluster_security_group_name_list
import capo_redshift.types.iam_role_arn_list
import capo_redshift.types.restore_from_cluster_snapshot_message
import capo_redshift.types.restore_from_cluster_snapshot_result
import capo_redshift.types.vpc_security_group_id_list
from capo_redshift._protocol.errors import find_error_element, parse_error_metadata
from capo_redshift._protocol.xml import fromstring
from capo_redshift._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_redshift._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
    raise_error,
)
from capo_redshift.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "AccessToSnapshotDenied":
            raise capo_redshift.errors.access_to_snapshot_denied_fault.AccessToSnapshotDeniedFault.from_query(
                error_el, message
            )
        case "ClusterAlreadyExists":
            raise capo_redshift.errors.cluster_already_exists_fault.ClusterAlreadyExistsFault.from_query(
                error_el, message
            )
        case "ClusterParameterGroupNotFound":
            raise capo_redshift.errors.cluster_parameter_group_not_found_fault.ClusterParameterGroupNotFoundFault.from_query(
                error_el, message
            )
        case "ClusterQuotaExceeded":
            raise capo_redshift.errors.cluster_quota_exceeded_fault.ClusterQuotaExceededFault.from_query(
                error_el, message
            )
        case "ClusterSecurityGroupNotFound":
            raise capo_redshift.errors.cluster_security_group_not_found_fault.ClusterSecurityGroupNotFoundFault.from_query(
                error_el, message
            )
        case "ClusterSnapshotNotFound":
            raise capo_redshift.errors.cluster_snapshot_not_found_fault.ClusterSnapshotNotFoundFault.from_query(
                error_el, message
            )
        case "ClusterSubnetGroupNotFoundFault":
            raise capo_redshift.errors.cluster_subnet_group_not_found_fault.ClusterSubnetGroupNotFoundFault.from_query(
                error_el, message
            )
        case "DependentServiceAccessDenied":
            raise capo_redshift.errors.dependent_service_access_denied_fault.DependentServiceAccessDeniedFault.from_query(
                error_el, message
            )
        case "DependentServiceRequestThrottlingFault":
            raise capo_redshift.errors.dependent_service_request_throttling_fault.DependentServiceRequestThrottlingFault.from_query(
                error_el, message
            )
        case "DependentServiceUnavailableFault":
            raise capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault.from_query(
                error_el, message
            )
        case "HsmClientCertificateNotFoundFault":
            raise capo_redshift.errors.hsm_client_certificate_not_found_fault.HsmClientCertificateNotFoundFault.from_query(
                error_el, message
            )
        case "HsmConfigurationNotFoundFault":
            raise capo_redshift.errors.hsm_configuration_not_found_fault.HsmConfigurationNotFoundFault.from_query(
                error_el, message
            )
        case "InsufficientClusterCapacity":
            raise capo_redshift.errors.insufficient_cluster_capacity_fault.InsufficientClusterCapacityFault.from_query(
                error_el, message
            )
        case "InvalidClusterSnapshotState":
            raise capo_redshift.errors.invalid_cluster_snapshot_state_fault.InvalidClusterSnapshotStateFault.from_query(
                error_el, message
            )
        case "InvalidClusterSubnetGroupStateFault":
            raise capo_redshift.errors.invalid_cluster_subnet_group_state_fault.InvalidClusterSubnetGroupStateFault.from_query(
                error_el, message
            )
        case "InvalidClusterTrack":
            raise capo_redshift.errors.invalid_cluster_track_fault.InvalidClusterTrackFault.from_query(
                error_el, message
            )
        case "InvalidElasticIpFault":
            raise capo_redshift.errors.invalid_elastic_ip_fault.InvalidElasticIpFault.from_query(
                error_el, message
            )
        case "InvalidReservedNodeState":
            raise capo_redshift.errors.invalid_reserved_node_state_fault.InvalidReservedNodeStateFault.from_query(
                error_el, message
            )
        case "InvalidRestore":
            raise capo_redshift.errors.invalid_restore_fault.InvalidRestoreFault.from_query(
                error_el, message
            )
        case "InvalidSubnet":
            raise capo_redshift.errors.invalid_subnet.InvalidSubnet.from_query(
                error_el, message
            )
        case "InvalidTagFault":
            raise capo_redshift.errors.invalid_tag_fault.InvalidTagFault.from_query(
                error_el, message
            )
        case "InvalidVPCNetworkStateFault":
            raise capo_redshift.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault.from_query(
                error_el, message
            )
        case "Ipv6CidrBlockNotFoundFault":
            raise capo_redshift.errors.ipv6_cidr_block_not_found_fault.Ipv6CidrBlockNotFoundFault.from_query(
                error_el, message
            )
        case "LimitExceededFault":
            raise capo_redshift.errors.limit_exceeded_fault.LimitExceededFault.from_query(
                error_el, message
            )
        case "NumberOfNodesPerClusterLimitExceeded":
            raise capo_redshift.errors.number_of_nodes_per_cluster_limit_exceeded_fault.NumberOfNodesPerClusterLimitExceededFault.from_query(
                error_el, message
            )
        case "NumberOfNodesQuotaExceeded":
            raise capo_redshift.errors.number_of_nodes_quota_exceeded_fault.NumberOfNodesQuotaExceededFault.from_query(
                error_el, message
            )
        case "RedshiftIdcApplicationNotExists":
            raise capo_redshift.errors.redshift_idc_application_not_exists_fault.RedshiftIdcApplicationNotExistsFault.from_query(
                error_el, message
            )
        case "ReservedNodeAlreadyExists":
            raise capo_redshift.errors.reserved_node_already_exists_fault.ReservedNodeAlreadyExistsFault.from_query(
                error_el, message
            )
        case "ReservedNodeAlreadyMigrated":
            raise capo_redshift.errors.reserved_node_already_migrated_fault.ReservedNodeAlreadyMigratedFault.from_query(
                error_el, message
            )
        case "ReservedNodeNotFound":
            raise capo_redshift.errors.reserved_node_not_found_fault.ReservedNodeNotFoundFault.from_query(
                error_el, message
            )
        case "ReservedNodeOfferingNotFound":
            raise capo_redshift.errors.reserved_node_offering_not_found_fault.ReservedNodeOfferingNotFoundFault.from_query(
                error_el, message
            )
        case "SnapshotScheduleNotFound":
            raise capo_redshift.errors.snapshot_schedule_not_found_fault.SnapshotScheduleNotFoundFault.from_query(
                error_el, message
            )
        case "TagLimitExceededFault":
            raise capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault.from_query(
                error_el, message
            )
        case "UnauthorizedOperation":
            raise capo_redshift.errors.unauthorized_operation.UnauthorizedOperation.from_query(
                error_el, message
            )
        case "UnsupportedOperation":
            raise capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault.from_query(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_redshift.types.restore_from_cluster_snapshot_result.RestoreFromClusterSnapshotResult:
    root = fromstring(response.read())
    result = root.find("RestoreFromClusterSnapshotResult")
    out: capo_redshift.types.restore_from_cluster_snapshot_result.RestoreFromClusterSnapshotResult = capo_redshift.types.restore_from_cluster_snapshot_result.deserialize_query(
        result if result is not None else root
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_redshift.types.restore_from_cluster_snapshot_result.RestoreFromClusterSnapshotResult:
    root = fromstring(await response.aread())
    result = root.find("RestoreFromClusterSnapshotResult")
    out: capo_redshift.types.restore_from_cluster_snapshot_result.RestoreFromClusterSnapshotResult = capo_redshift.types.restore_from_cluster_snapshot_result.deserialize_query(
        result if result is not None else root
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_redshift._auth._signers.Signer | None:
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
            sigv4_config = capo_redshift._auth._sigv4.build_sigv4_auth_scheme(
                "redshift", options.region, endpoint_scheme
            )
            if sigv4_config is not None:
                return capo_redshift._auth._signers.SigV4Signer(
                    options.credentials_provider, auth_scheme=sigv4_config
                )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_redshift.types.restore_from_cluster_snapshot_message.RestoreFromClusterSnapshotMessage,
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
    pairs.append(("Action", "RestoreFromClusterSnapshot"))
    pairs.append(("Version", "2012-12-01"))
    capo_redshift.types.restore_from_cluster_snapshot_message.serialize_query(
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


def restore_from_cluster_snapshot(
    options: OperationOptions,
    input_: capo_redshift.types.restore_from_cluster_snapshot_message.RestoreFromClusterSnapshotMessage,
) -> tuple[
    capo_redshift.types.restore_from_cluster_snapshot_result.RestoreFromClusterSnapshotResult,
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


async def async_restore_from_cluster_snapshot(
    options: AsyncOperationOptions,
    input_: capo_redshift.types.restore_from_cluster_snapshot_message.RestoreFromClusterSnapshotMessage,
) -> tuple[
    capo_redshift.types.restore_from_cluster_snapshot_result.RestoreFromClusterSnapshotResult,
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
