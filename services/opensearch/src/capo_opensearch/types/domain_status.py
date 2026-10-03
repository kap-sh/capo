"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.advanced_options
    import capo_opensearch.types.advanced_security_options
    import capo_opensearch.types.aiml_options_output
    import capo_opensearch.types.arn
    import capo_opensearch.types.auto_tune_options_output
    import capo_opensearch.types.automated_snapshot_pause_options
    import capo_opensearch.types.boolean
    import capo_opensearch.types.change_progress_details
    import capo_opensearch.types.cluster_config
    import capo_opensearch.types.cognito_options
    import capo_opensearch.types.deployment_strategy_options
    import capo_opensearch.types.domain_endpoint_options
    import capo_opensearch.types.domain_id
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.domain_processing_status_type
    import capo_opensearch.types.domain_use_case
    import capo_opensearch.types.ebs_options
    import capo_opensearch.types.encryption_at_rest_options
    import capo_opensearch.types.endpoints_map
    import capo_opensearch.types.engine_mode
    import capo_opensearch.types.hosted_zone_id
    import capo_opensearch.types.identity_center_options
    import capo_opensearch.types.ip_address_type
    import capo_opensearch.types.log_publishing_options
    import capo_opensearch.types.modifying_properties_list
    import capo_opensearch.types.node_to_node_encryption_options
    import capo_opensearch.types.off_peak_window_options
    import capo_opensearch.types.policy_document
    import capo_opensearch.types.service_software_options
    import capo_opensearch.types.service_url
    import capo_opensearch.types.snapshot_options
    import capo_opensearch.types.software_update_options
    import capo_opensearch.types.version_string
    import capo_opensearch.types.vpc_derived_info


class DomainStatus(TypedDict, closed=True):
    domain_id: "capo_opensearch.types.domain_id.DomainId"
    """<p>Unique identifier for the domain.</p>"""
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>Name of the domain. Domain names are unique across all domains owned by the same account within an Amazon Web Services Region.</p>"""
    arn: "capo_opensearch.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the domain. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html">IAM identifiers </a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>"""
    created: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Creation status of an OpenSearch Service domain. True if domain creation is complete. False if domain creation is still in progress.</p>"""
    deleted: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Deletion status of an OpenSearch Service domain. True if domain deletion is complete. False if domain deletion is still in progress. Once deletion is complete, the status of the domain is no longer returned.</p>"""
    endpoint: NotRequired["capo_opensearch.types.service_url.ServiceUrl"]
    """<p>Domain-specific endpoint used to submit index, search, and data upload requests to the domain.</p>"""
    endpoint_v2: NotRequired["capo_opensearch.types.service_url.ServiceUrl"]
    """<p>If <code>IPAddressType</code> to set to <code>dualstack</code>, a version 2 domain endpoint is provisioned. This endpoint functions like a normal endpoint, except that it works with both IPv4 and IPv6 IP addresses. Normal endpoints work only with IPv4 IP addresses. </p>"""
    endpoints: NotRequired["capo_opensearch.types.endpoints_map.EndpointsMap"]
    """<p>The key-value pair that exists if the OpenSearch Service domain uses VPC endpoints. For example:</p> <ul> <li> <p> <b>IPv4 IP addresses</b> - <code>'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'</code> </p> </li> <li> <p> <b>Dual stack IP addresses</b> - <code>'vpcv2':'vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.aos.us-east-1.on.aws'</code> </p> </li> </ul>"""
    domain_endpoint_v2_hosted_zone_id: NotRequired[
        "capo_opensearch.types.hosted_zone_id.HostedZoneId"
    ]
    """<p>The dual stack hosted zone ID for the domain. </p>"""
    processing: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>The status of the domain configuration. True if OpenSearch Service is processing configuration changes. False if the configuration is active.</p>"""
    upgrade_processing: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>The status of a domain version upgrade to a new version of OpenSearch or Elasticsearch. True if OpenSearch Service is in the process of a version upgrade. False if the configuration is active.</p>"""
    engine_version: NotRequired["capo_opensearch.types.version_string.VersionString"]
    """<p>Version of OpenSearch or Elasticsearch that the domain is running, in the format <code>Elasticsearch_X.Y</code> or <code>OpenSearch_X.Y</code>.</p>"""
    cluster_config: "capo_opensearch.types.cluster_config.ClusterConfig"
    """<p>Container for the cluster configuration of the domain.</p>"""
    ebs_options: NotRequired["capo_opensearch.types.ebs_options.EBSOptions"]
    """<p>Container for EBS-based storage settings for the domain.</p>"""
    access_policies: NotRequired["capo_opensearch.types.policy_document.PolicyDocument"]
    """<p>Identity and Access Management (IAM) policy document specifying the access policies for the domain.</p>"""
    ip_address_type: NotRequired["capo_opensearch.types.ip_address_type.IPAddressType"]
    """<p>The type of IP addresses supported by the endpoint for the domain.</p>"""
    snapshot_options: NotRequired[
        "capo_opensearch.types.snapshot_options.SnapshotOptions"
    ]
    """<p>DEPRECATED. Container for parameters required to configure automated snapshots of domain indexes.</p>"""
    vpc_options: NotRequired["capo_opensearch.types.vpc_derived_info.VPCDerivedInfo"]
    """<p>The VPC configuration for the domain.</p>"""
    cognito_options: NotRequired["capo_opensearch.types.cognito_options.CognitoOptions"]
    """<p>Key-value pairs to configure Amazon Cognito authentication for OpenSearch Dashboards.</p>"""
    encryption_at_rest_options: NotRequired[
        "capo_opensearch.types.encryption_at_rest_options.EncryptionAtRestOptions"
    ]
    """<p>Encryption at rest settings for the domain.</p>"""
    node_to_node_encryption_options: NotRequired[
        "capo_opensearch.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
    ]
    """<p>Whether node-to-node encryption is enabled or disabled.</p>"""
    advanced_options: NotRequired[
        "capo_opensearch.types.advanced_options.AdvancedOptions"
    ]
    """<p>Key-value pairs that specify advanced configuration options.</p>"""
    log_publishing_options: NotRequired[
        "capo_opensearch.types.log_publishing_options.LogPublishingOptions"
    ]
    """<p>Log publishing options for the domain.</p>"""
    service_software_options: NotRequired[
        "capo_opensearch.types.service_software_options.ServiceSoftwareOptions"
    ]
    """<p>The current status of the domain's service software.</p>"""
    domain_endpoint_options: NotRequired[
        "capo_opensearch.types.domain_endpoint_options.DomainEndpointOptions"
    ]
    """<p>Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.</p>"""
    advanced_security_options: NotRequired[
        "capo_opensearch.types.advanced_security_options.AdvancedSecurityOptions"
    ]
    """<p>Settings for fine-grained access control.</p>"""
    identity_center_options: NotRequired[
        "capo_opensearch.types.identity_center_options.IdentityCenterOptions"
    ]
    """<p>Configuration options for controlling IAM Identity Center integration within a domain.</p>"""
    auto_tune_options: NotRequired[
        "capo_opensearch.types.auto_tune_options_output.AutoTuneOptionsOutput"
    ]
    """<p>Auto-Tune settings for the domain.</p>"""
    change_progress_details: NotRequired[
        "capo_opensearch.types.change_progress_details.ChangeProgressDetails"
    ]
    """<p>Information about a configuration change happening on the domain.</p>"""
    off_peak_window_options: NotRequired[
        "capo_opensearch.types.off_peak_window_options.OffPeakWindowOptions"
    ]
    """<p>Options that specify a custom 10-hour window during which OpenSearch Service can perform configuration changes on the domain.</p>"""
    software_update_options: NotRequired[
        "capo_opensearch.types.software_update_options.SoftwareUpdateOptions"
    ]
    """<p>Service software update options for the domain.</p>"""
    domain_processing_status: NotRequired[
        "capo_opensearch.types.domain_processing_status_type.DomainProcessingStatusType"
    ]
    """<p>The status of any changes that are currently in progress for the domain.</p>"""
    modifying_properties: NotRequired[
        "capo_opensearch.types.modifying_properties_list.ModifyingPropertiesList"
    ]
    """<p>Information about the domain properties that are currently being modified.</p>"""
    aiml_options: NotRequired[
        "capo_opensearch.types.aiml_options_output.AIMLOptionsOutput"
    ]
    """<p>Container for parameters required to enable all machine learning features.</p>"""
    deployment_strategy_options: NotRequired[
        "capo_opensearch.types.deployment_strategy_options.DeploymentStrategyOptions"
    ]
    """<p>The current status of the domain's deployment strategy options.</p>"""
    automated_snapshot_pause_options: NotRequired[
        "capo_opensearch.types.automated_snapshot_pause_options.AutomatedSnapshotPauseOptions"
    ]
    """<p>The current status of the domain's automated snapshot pause options.</p>"""
    use_case: NotRequired["capo_opensearch.types.domain_use_case.DomainUseCase"]
    """<p>The primary use case for the domain.</p>"""
    engine_mode: NotRequired["capo_opensearch.types.engine_mode.EngineMode"]
    """<p>The engine mode for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainStatus) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["DomainName"] = value["domain_name"]
    out["ARN"] = value["arn"]
    if "created" in value:
        out["Created"] = value["created"]
    if "deleted" in value:
        out["Deleted"] = value["deleted"]
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    if "endpoint_v2" in value:
        out["EndpointV2"] = value["endpoint_v2"]
    if "endpoints" in value:
        import capo_opensearch.types.endpoints_map

        out["Endpoints"] = capo_opensearch.types.endpoints_map.serialize_json(
            value["endpoints"]
        )
    if "domain_endpoint_v2_hosted_zone_id" in value:
        out["DomainEndpointV2HostedZoneId"] = value["domain_endpoint_v2_hosted_zone_id"]
    if "processing" in value:
        out["Processing"] = value["processing"]
    if "upgrade_processing" in value:
        out["UpgradeProcessing"] = value["upgrade_processing"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    import capo_opensearch.types.cluster_config

    out["ClusterConfig"] = capo_opensearch.types.cluster_config.serialize_json(
        value["cluster_config"]
    )
    if "ebs_options" in value:
        import capo_opensearch.types.ebs_options

        out["EBSOptions"] = capo_opensearch.types.ebs_options.serialize_json(
            value["ebs_options"]
        )
    if "access_policies" in value:
        out["AccessPolicies"] = value["access_policies"]
    if "ip_address_type" in value:
        import capo_opensearch.types.ip_address_type

        out["IPAddressType"] = capo_opensearch.types.ip_address_type.serialize_json(
            value["ip_address_type"]
        )
    if "snapshot_options" in value:
        import capo_opensearch.types.snapshot_options

        out["SnapshotOptions"] = capo_opensearch.types.snapshot_options.serialize_json(
            value["snapshot_options"]
        )
    if "vpc_options" in value:
        import capo_opensearch.types.vpc_derived_info

        out["VPCOptions"] = capo_opensearch.types.vpc_derived_info.serialize_json(
            value["vpc_options"]
        )
    if "cognito_options" in value:
        import capo_opensearch.types.cognito_options

        out["CognitoOptions"] = capo_opensearch.types.cognito_options.serialize_json(
            value["cognito_options"]
        )
    if "encryption_at_rest_options" in value:
        import capo_opensearch.types.encryption_at_rest_options

        out["EncryptionAtRestOptions"] = (
            capo_opensearch.types.encryption_at_rest_options.serialize_json(
                value["encryption_at_rest_options"]
            )
        )
    if "node_to_node_encryption_options" in value:
        import capo_opensearch.types.node_to_node_encryption_options

        out["NodeToNodeEncryptionOptions"] = (
            capo_opensearch.types.node_to_node_encryption_options.serialize_json(
                value["node_to_node_encryption_options"]
            )
        )
    if "advanced_options" in value:
        import capo_opensearch.types.advanced_options

        out["AdvancedOptions"] = capo_opensearch.types.advanced_options.serialize_json(
            value["advanced_options"]
        )
    if "log_publishing_options" in value:
        import capo_opensearch.types.log_publishing_options

        out["LogPublishingOptions"] = (
            capo_opensearch.types.log_publishing_options.serialize_json(
                value["log_publishing_options"]
            )
        )
    if "service_software_options" in value:
        import capo_opensearch.types.service_software_options

        out["ServiceSoftwareOptions"] = (
            capo_opensearch.types.service_software_options.serialize_json(
                value["service_software_options"]
            )
        )
    if "domain_endpoint_options" in value:
        import capo_opensearch.types.domain_endpoint_options

        out["DomainEndpointOptions"] = (
            capo_opensearch.types.domain_endpoint_options.serialize_json(
                value["domain_endpoint_options"]
            )
        )
    if "advanced_security_options" in value:
        import capo_opensearch.types.advanced_security_options

        out["AdvancedSecurityOptions"] = (
            capo_opensearch.types.advanced_security_options.serialize_json(
                value["advanced_security_options"]
            )
        )
    if "identity_center_options" in value:
        import capo_opensearch.types.identity_center_options

        out["IdentityCenterOptions"] = (
            capo_opensearch.types.identity_center_options.serialize_json(
                value["identity_center_options"]
            )
        )
    if "auto_tune_options" in value:
        import capo_opensearch.types.auto_tune_options_output

        out["AutoTuneOptions"] = (
            capo_opensearch.types.auto_tune_options_output.serialize_json(
                value["auto_tune_options"]
            )
        )
    if "change_progress_details" in value:
        import capo_opensearch.types.change_progress_details

        out["ChangeProgressDetails"] = (
            capo_opensearch.types.change_progress_details.serialize_json(
                value["change_progress_details"]
            )
        )
    if "off_peak_window_options" in value:
        import capo_opensearch.types.off_peak_window_options

        out["OffPeakWindowOptions"] = (
            capo_opensearch.types.off_peak_window_options.serialize_json(
                value["off_peak_window_options"]
            )
        )
    if "software_update_options" in value:
        import capo_opensearch.types.software_update_options

        out["SoftwareUpdateOptions"] = (
            capo_opensearch.types.software_update_options.serialize_json(
                value["software_update_options"]
            )
        )
    if "domain_processing_status" in value:
        import capo_opensearch.types.domain_processing_status_type

        out["DomainProcessingStatus"] = (
            capo_opensearch.types.domain_processing_status_type.serialize_json(
                value["domain_processing_status"]
            )
        )
    if "modifying_properties" in value:
        import capo_opensearch.types.modifying_properties_list

        out["ModifyingProperties"] = (
            capo_opensearch.types.modifying_properties_list.serialize_json(
                value["modifying_properties"]
            )
        )
    if "aiml_options" in value:
        import capo_opensearch.types.aiml_options_output

        out["AIMLOptions"] = capo_opensearch.types.aiml_options_output.serialize_json(
            value["aiml_options"]
        )
    if "deployment_strategy_options" in value:
        import capo_opensearch.types.deployment_strategy_options

        out["DeploymentStrategyOptions"] = (
            capo_opensearch.types.deployment_strategy_options.serialize_json(
                value["deployment_strategy_options"]
            )
        )
    if "automated_snapshot_pause_options" in value:
        import capo_opensearch.types.automated_snapshot_pause_options

        out["AutomatedSnapshotPauseOptions"] = (
            capo_opensearch.types.automated_snapshot_pause_options.serialize_json(
                value["automated_snapshot_pause_options"]
            )
        )
    if "use_case" in value:
        import capo_opensearch.types.domain_use_case

        out["UseCase"] = capo_opensearch.types.domain_use_case.serialize_json(
            value["use_case"]
        )
    if "engine_mode" in value:
        import capo_opensearch.types.engine_mode

        out["EngineMode"] = capo_opensearch.types.engine_mode.serialize_json(
            value["engine_mode"]
        )
    return out


def deserialize_json(data: dict) -> DomainStatus:
    out: DomainStatus = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError("DomainStatus.domain_id required")
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("DomainStatus.domain_name required")
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    else:
        raise DeserializationError("DomainStatus.arn required")
    if data.get("Created") is not None:
        out["created"] = data["Created"]
    if data.get("Deleted") is not None:
        out["deleted"] = data["Deleted"]
    if data.get("Endpoint") is not None:
        out["endpoint"] = data["Endpoint"]
    if data.get("EndpointV2") is not None:
        out["endpoint_v2"] = data["EndpointV2"]
    if data.get("Endpoints") is not None:
        import capo_opensearch.types.endpoints_map

        out["endpoints"] = capo_opensearch.types.endpoints_map.deserialize_json(
            data["Endpoints"]
        )
    if data.get("DomainEndpointV2HostedZoneId") is not None:
        out["domain_endpoint_v2_hosted_zone_id"] = data["DomainEndpointV2HostedZoneId"]
    if data.get("Processing") is not None:
        out["processing"] = data["Processing"]
    if data.get("UpgradeProcessing") is not None:
        out["upgrade_processing"] = data["UpgradeProcessing"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("ClusterConfig") is not None:
        import capo_opensearch.types.cluster_config

        out["cluster_config"] = capo_opensearch.types.cluster_config.deserialize_json(
            data["ClusterConfig"]
        )
    else:
        raise DeserializationError("DomainStatus.cluster_config required")
    if data.get("EBSOptions") is not None:
        import capo_opensearch.types.ebs_options

        out["ebs_options"] = capo_opensearch.types.ebs_options.deserialize_json(
            data["EBSOptions"]
        )
    if data.get("AccessPolicies") is not None:
        out["access_policies"] = data["AccessPolicies"]
    if data.get("IPAddressType") is not None:
        import capo_opensearch.types.ip_address_type

        out["ip_address_type"] = capo_opensearch.types.ip_address_type.deserialize_json(
            data["IPAddressType"]
        )
    if data.get("SnapshotOptions") is not None:
        import capo_opensearch.types.snapshot_options

        out["snapshot_options"] = (
            capo_opensearch.types.snapshot_options.deserialize_json(
                data["SnapshotOptions"]
            )
        )
    if data.get("VPCOptions") is not None:
        import capo_opensearch.types.vpc_derived_info

        out["vpc_options"] = capo_opensearch.types.vpc_derived_info.deserialize_json(
            data["VPCOptions"]
        )
    if data.get("CognitoOptions") is not None:
        import capo_opensearch.types.cognito_options

        out["cognito_options"] = capo_opensearch.types.cognito_options.deserialize_json(
            data["CognitoOptions"]
        )
    if data.get("EncryptionAtRestOptions") is not None:
        import capo_opensearch.types.encryption_at_rest_options

        out["encryption_at_rest_options"] = (
            capo_opensearch.types.encryption_at_rest_options.deserialize_json(
                data["EncryptionAtRestOptions"]
            )
        )
    if data.get("NodeToNodeEncryptionOptions") is not None:
        import capo_opensearch.types.node_to_node_encryption_options

        out["node_to_node_encryption_options"] = (
            capo_opensearch.types.node_to_node_encryption_options.deserialize_json(
                data["NodeToNodeEncryptionOptions"]
            )
        )
    if data.get("AdvancedOptions") is not None:
        import capo_opensearch.types.advanced_options

        out["advanced_options"] = (
            capo_opensearch.types.advanced_options.deserialize_json(
                data["AdvancedOptions"]
            )
        )
    if data.get("LogPublishingOptions") is not None:
        import capo_opensearch.types.log_publishing_options

        out["log_publishing_options"] = (
            capo_opensearch.types.log_publishing_options.deserialize_json(
                data["LogPublishingOptions"]
            )
        )
    if data.get("ServiceSoftwareOptions") is not None:
        import capo_opensearch.types.service_software_options

        out["service_software_options"] = (
            capo_opensearch.types.service_software_options.deserialize_json(
                data["ServiceSoftwareOptions"]
            )
        )
    if data.get("DomainEndpointOptions") is not None:
        import capo_opensearch.types.domain_endpoint_options

        out["domain_endpoint_options"] = (
            capo_opensearch.types.domain_endpoint_options.deserialize_json(
                data["DomainEndpointOptions"]
            )
        )
    if data.get("AdvancedSecurityOptions") is not None:
        import capo_opensearch.types.advanced_security_options

        out["advanced_security_options"] = (
            capo_opensearch.types.advanced_security_options.deserialize_json(
                data["AdvancedSecurityOptions"]
            )
        )
    if data.get("IdentityCenterOptions") is not None:
        import capo_opensearch.types.identity_center_options

        out["identity_center_options"] = (
            capo_opensearch.types.identity_center_options.deserialize_json(
                data["IdentityCenterOptions"]
            )
        )
    if data.get("AutoTuneOptions") is not None:
        import capo_opensearch.types.auto_tune_options_output

        out["auto_tune_options"] = (
            capo_opensearch.types.auto_tune_options_output.deserialize_json(
                data["AutoTuneOptions"]
            )
        )
    if data.get("ChangeProgressDetails") is not None:
        import capo_opensearch.types.change_progress_details

        out["change_progress_details"] = (
            capo_opensearch.types.change_progress_details.deserialize_json(
                data["ChangeProgressDetails"]
            )
        )
    if data.get("OffPeakWindowOptions") is not None:
        import capo_opensearch.types.off_peak_window_options

        out["off_peak_window_options"] = (
            capo_opensearch.types.off_peak_window_options.deserialize_json(
                data["OffPeakWindowOptions"]
            )
        )
    if data.get("SoftwareUpdateOptions") is not None:
        import capo_opensearch.types.software_update_options

        out["software_update_options"] = (
            capo_opensearch.types.software_update_options.deserialize_json(
                data["SoftwareUpdateOptions"]
            )
        )
    if data.get("DomainProcessingStatus") is not None:
        import capo_opensearch.types.domain_processing_status_type

        out["domain_processing_status"] = (
            capo_opensearch.types.domain_processing_status_type.deserialize_json(
                data["DomainProcessingStatus"]
            )
        )
    if data.get("ModifyingProperties") is not None:
        import capo_opensearch.types.modifying_properties_list

        out["modifying_properties"] = (
            capo_opensearch.types.modifying_properties_list.deserialize_json(
                data["ModifyingProperties"]
            )
        )
    if data.get("AIMLOptions") is not None:
        import capo_opensearch.types.aiml_options_output

        out["aiml_options"] = (
            capo_opensearch.types.aiml_options_output.deserialize_json(
                data["AIMLOptions"]
            )
        )
    if data.get("DeploymentStrategyOptions") is not None:
        import capo_opensearch.types.deployment_strategy_options

        out["deployment_strategy_options"] = (
            capo_opensearch.types.deployment_strategy_options.deserialize_json(
                data["DeploymentStrategyOptions"]
            )
        )
    if data.get("AutomatedSnapshotPauseOptions") is not None:
        import capo_opensearch.types.automated_snapshot_pause_options

        out["automated_snapshot_pause_options"] = (
            capo_opensearch.types.automated_snapshot_pause_options.deserialize_json(
                data["AutomatedSnapshotPauseOptions"]
            )
        )
    if data.get("UseCase") is not None:
        import capo_opensearch.types.domain_use_case

        out["use_case"] = capo_opensearch.types.domain_use_case.deserialize_json(
            data["UseCase"]
        )
    if data.get("EngineMode") is not None:
        import capo_opensearch.types.engine_mode

        out["engine_mode"] = capo_opensearch.types.engine_mode.deserialize_json(
            data["EngineMode"]
        )
    return out
