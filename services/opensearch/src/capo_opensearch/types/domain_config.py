"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.access_policies_status
    import capo_opensearch.types.advanced_options_status
    import capo_opensearch.types.advanced_security_options_status
    import capo_opensearch.types.aiml_options_status
    import capo_opensearch.types.auto_tune_options_status
    import capo_opensearch.types.automated_snapshot_pause_options_status
    import capo_opensearch.types.change_progress_details
    import capo_opensearch.types.cluster_config_status
    import capo_opensearch.types.cognito_options_status
    import capo_opensearch.types.deployment_strategy_options_status
    import capo_opensearch.types.domain_endpoint_options_status
    import capo_opensearch.types.ebs_options_status
    import capo_opensearch.types.encryption_at_rest_options_status
    import capo_opensearch.types.engine_mode_status
    import capo_opensearch.types.identity_center_options_status
    import capo_opensearch.types.ip_address_type_status
    import capo_opensearch.types.log_publishing_options_status
    import capo_opensearch.types.modifying_properties_list
    import capo_opensearch.types.node_to_node_encryption_options_status
    import capo_opensearch.types.off_peak_window_options_status
    import capo_opensearch.types.snapshot_options_status
    import capo_opensearch.types.software_update_options_status
    import capo_opensearch.types.use_case_status
    import capo_opensearch.types.version_status
    import capo_opensearch.types.vpc_derived_info_status


class DomainConfig(TypedDict, closed=True):
    engine_version: NotRequired["capo_opensearch.types.version_status.VersionStatus"]
    """<p>The OpenSearch or Elasticsearch version that the domain is running.</p>"""
    cluster_config: NotRequired[
        "capo_opensearch.types.cluster_config_status.ClusterConfigStatus"
    ]
    """<p>Container for the cluster configuration of a the domain.</p>"""
    ebs_options: NotRequired[
        "capo_opensearch.types.ebs_options_status.EBSOptionsStatus"
    ]
    """<p>Container for EBS options configured for the domain.</p>"""
    access_policies: NotRequired[
        "capo_opensearch.types.access_policies_status.AccessPoliciesStatus"
    ]
    """<p>Specifies the access policies for the domain.</p>"""
    ip_address_type: NotRequired[
        "capo_opensearch.types.ip_address_type_status.IPAddressTypeStatus"
    ]
    """<p>Choose either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If you set your IP address type to dual stack, you can't change your address type later.</p>"""
    snapshot_options: NotRequired[
        "capo_opensearch.types.snapshot_options_status.SnapshotOptionsStatus"
    ]
    """<p>DEPRECATED. Container for parameters required to configure automated snapshots of domain indexes.</p>"""
    vpc_options: NotRequired[
        "capo_opensearch.types.vpc_derived_info_status.VPCDerivedInfoStatus"
    ]
    """<p>The current VPC options for the domain and the status of any updates to their configuration.</p>"""
    cognito_options: NotRequired[
        "capo_opensearch.types.cognito_options_status.CognitoOptionsStatus"
    ]
    """<p>Container for Amazon Cognito options for the domain.</p>"""
    encryption_at_rest_options: NotRequired[
        "capo_opensearch.types.encryption_at_rest_options_status.EncryptionAtRestOptionsStatus"
    ]
    """<p>Key-value pairs to enable encryption at rest.</p>"""
    node_to_node_encryption_options: NotRequired[
        "capo_opensearch.types.node_to_node_encryption_options_status.NodeToNodeEncryptionOptionsStatus"
    ]
    """<p>Whether node-to-node encryption is enabled or disabled.</p>"""
    advanced_options: NotRequired[
        "capo_opensearch.types.advanced_options_status.AdvancedOptionsStatus"
    ]
    """<p>Key-value pairs to specify advanced configuration options. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options">Advanced options</a>.</p>"""
    log_publishing_options: NotRequired[
        "capo_opensearch.types.log_publishing_options_status.LogPublishingOptionsStatus"
    ]
    """<p>Key-value pairs to configure log publishing.</p>"""
    domain_endpoint_options: NotRequired[
        "capo_opensearch.types.domain_endpoint_options_status.DomainEndpointOptionsStatus"
    ]
    """<p>Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.</p>"""
    advanced_security_options: NotRequired[
        "capo_opensearch.types.advanced_security_options_status.AdvancedSecurityOptionsStatus"
    ]
    """<p>Container for fine-grained access control settings for the domain.</p>"""
    identity_center_options: NotRequired[
        "capo_opensearch.types.identity_center_options_status.IdentityCenterOptionsStatus"
    ]
    """<p>Configuration options for enabling and managing IAM Identity Center integration within a domain.</p>"""
    auto_tune_options: NotRequired[
        "capo_opensearch.types.auto_tune_options_status.AutoTuneOptionsStatus"
    ]
    """<p>Container for Auto-Tune settings for the domain.</p>"""
    change_progress_details: NotRequired[
        "capo_opensearch.types.change_progress_details.ChangeProgressDetails"
    ]
    """<p>Container for information about the progress of an existing configuration change.</p>"""
    off_peak_window_options: NotRequired[
        "capo_opensearch.types.off_peak_window_options_status.OffPeakWindowOptionsStatus"
    ]
    """<p>Container for off-peak window options for the domain.</p>"""
    software_update_options: NotRequired[
        "capo_opensearch.types.software_update_options_status.SoftwareUpdateOptionsStatus"
    ]
    """<p>Software update options for the domain.</p>"""
    modifying_properties: NotRequired[
        "capo_opensearch.types.modifying_properties_list.ModifyingPropertiesList"
    ]
    """<p>Information about the domain properties that are currently being modified.</p>"""
    aiml_options: NotRequired[
        "capo_opensearch.types.aiml_options_status.AIMLOptionsStatus"
    ]
    """<p>Container for parameters required to enable all machine learning features.</p>"""
    deployment_strategy_options: NotRequired[
        "capo_opensearch.types.deployment_strategy_options_status.DeploymentStrategyOptionsStatus"
    ]
    """<p>Specifies <code>DeploymentStrategyOptions</code> for the domain.</p>"""
    automated_snapshot_pause_options: NotRequired[
        "capo_opensearch.types.automated_snapshot_pause_options_status.AutomatedSnapshotPauseOptionsStatus"
    ]
    """<p>Specifies <code>AutomatedSnapshotPauseOptions</code> for the domain.</p>"""
    use_case: NotRequired["capo_opensearch.types.use_case_status.UseCaseStatus"]
    """<p>The use case configured for the domain.</p>"""
    engine_mode: NotRequired[
        "capo_opensearch.types.engine_mode_status.EngineModeStatus"
    ]
    """<p>The engine mode configured for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainConfig) -> dict:
    out: dict = {}
    if "engine_version" in value:
        import capo_opensearch.types.version_status

        out["EngineVersion"] = capo_opensearch.types.version_status.serialize_json(
            value["engine_version"]
        )
    if "cluster_config" in value:
        import capo_opensearch.types.cluster_config_status

        out["ClusterConfig"] = (
            capo_opensearch.types.cluster_config_status.serialize_json(
                value["cluster_config"]
            )
        )
    if "ebs_options" in value:
        import capo_opensearch.types.ebs_options_status

        out["EBSOptions"] = capo_opensearch.types.ebs_options_status.serialize_json(
            value["ebs_options"]
        )
    if "access_policies" in value:
        import capo_opensearch.types.access_policies_status

        out["AccessPolicies"] = (
            capo_opensearch.types.access_policies_status.serialize_json(
                value["access_policies"]
            )
        )
    if "ip_address_type" in value:
        import capo_opensearch.types.ip_address_type_status

        out["IPAddressType"] = (
            capo_opensearch.types.ip_address_type_status.serialize_json(
                value["ip_address_type"]
            )
        )
    if "snapshot_options" in value:
        import capo_opensearch.types.snapshot_options_status

        out["SnapshotOptions"] = (
            capo_opensearch.types.snapshot_options_status.serialize_json(
                value["snapshot_options"]
            )
        )
    if "vpc_options" in value:
        import capo_opensearch.types.vpc_derived_info_status

        out["VPCOptions"] = (
            capo_opensearch.types.vpc_derived_info_status.serialize_json(
                value["vpc_options"]
            )
        )
    if "cognito_options" in value:
        import capo_opensearch.types.cognito_options_status

        out["CognitoOptions"] = (
            capo_opensearch.types.cognito_options_status.serialize_json(
                value["cognito_options"]
            )
        )
    if "encryption_at_rest_options" in value:
        import capo_opensearch.types.encryption_at_rest_options_status

        out["EncryptionAtRestOptions"] = (
            capo_opensearch.types.encryption_at_rest_options_status.serialize_json(
                value["encryption_at_rest_options"]
            )
        )
    if "node_to_node_encryption_options" in value:
        import capo_opensearch.types.node_to_node_encryption_options_status

        out["NodeToNodeEncryptionOptions"] = (
            capo_opensearch.types.node_to_node_encryption_options_status.serialize_json(
                value["node_to_node_encryption_options"]
            )
        )
    if "advanced_options" in value:
        import capo_opensearch.types.advanced_options_status

        out["AdvancedOptions"] = (
            capo_opensearch.types.advanced_options_status.serialize_json(
                value["advanced_options"]
            )
        )
    if "log_publishing_options" in value:
        import capo_opensearch.types.log_publishing_options_status

        out["LogPublishingOptions"] = (
            capo_opensearch.types.log_publishing_options_status.serialize_json(
                value["log_publishing_options"]
            )
        )
    if "domain_endpoint_options" in value:
        import capo_opensearch.types.domain_endpoint_options_status

        out["DomainEndpointOptions"] = (
            capo_opensearch.types.domain_endpoint_options_status.serialize_json(
                value["domain_endpoint_options"]
            )
        )
    if "advanced_security_options" in value:
        import capo_opensearch.types.advanced_security_options_status

        out["AdvancedSecurityOptions"] = (
            capo_opensearch.types.advanced_security_options_status.serialize_json(
                value["advanced_security_options"]
            )
        )
    if "identity_center_options" in value:
        import capo_opensearch.types.identity_center_options_status

        out["IdentityCenterOptions"] = (
            capo_opensearch.types.identity_center_options_status.serialize_json(
                value["identity_center_options"]
            )
        )
    if "auto_tune_options" in value:
        import capo_opensearch.types.auto_tune_options_status

        out["AutoTuneOptions"] = (
            capo_opensearch.types.auto_tune_options_status.serialize_json(
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
        import capo_opensearch.types.off_peak_window_options_status

        out["OffPeakWindowOptions"] = (
            capo_opensearch.types.off_peak_window_options_status.serialize_json(
                value["off_peak_window_options"]
            )
        )
    if "software_update_options" in value:
        import capo_opensearch.types.software_update_options_status

        out["SoftwareUpdateOptions"] = (
            capo_opensearch.types.software_update_options_status.serialize_json(
                value["software_update_options"]
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
        import capo_opensearch.types.aiml_options_status

        out["AIMLOptions"] = capo_opensearch.types.aiml_options_status.serialize_json(
            value["aiml_options"]
        )
    if "deployment_strategy_options" in value:
        import capo_opensearch.types.deployment_strategy_options_status

        out["DeploymentStrategyOptions"] = (
            capo_opensearch.types.deployment_strategy_options_status.serialize_json(
                value["deployment_strategy_options"]
            )
        )
    if "automated_snapshot_pause_options" in value:
        import capo_opensearch.types.automated_snapshot_pause_options_status

        out["AutomatedSnapshotPauseOptions"] = (
            capo_opensearch.types.automated_snapshot_pause_options_status.serialize_json(
                value["automated_snapshot_pause_options"]
            )
        )
    if "use_case" in value:
        import capo_opensearch.types.use_case_status

        out["UseCase"] = capo_opensearch.types.use_case_status.serialize_json(
            value["use_case"]
        )
    if "engine_mode" in value:
        import capo_opensearch.types.engine_mode_status

        out["EngineMode"] = capo_opensearch.types.engine_mode_status.serialize_json(
            value["engine_mode"]
        )
    return out


def deserialize_json(data: dict) -> DomainConfig:
    out: DomainConfig = {}  # type: ignore[typeddict-item]
    if data.get("EngineVersion") is not None:
        import capo_opensearch.types.version_status

        out["engine_version"] = capo_opensearch.types.version_status.deserialize_json(
            data["EngineVersion"]
        )
    if data.get("ClusterConfig") is not None:
        import capo_opensearch.types.cluster_config_status

        out["cluster_config"] = (
            capo_opensearch.types.cluster_config_status.deserialize_json(
                data["ClusterConfig"]
            )
        )
    if data.get("EBSOptions") is not None:
        import capo_opensearch.types.ebs_options_status

        out["ebs_options"] = capo_opensearch.types.ebs_options_status.deserialize_json(
            data["EBSOptions"]
        )
    if data.get("AccessPolicies") is not None:
        import capo_opensearch.types.access_policies_status

        out["access_policies"] = (
            capo_opensearch.types.access_policies_status.deserialize_json(
                data["AccessPolicies"]
            )
        )
    if data.get("IPAddressType") is not None:
        import capo_opensearch.types.ip_address_type_status

        out["ip_address_type"] = (
            capo_opensearch.types.ip_address_type_status.deserialize_json(
                data["IPAddressType"]
            )
        )
    if data.get("SnapshotOptions") is not None:
        import capo_opensearch.types.snapshot_options_status

        out["snapshot_options"] = (
            capo_opensearch.types.snapshot_options_status.deserialize_json(
                data["SnapshotOptions"]
            )
        )
    if data.get("VPCOptions") is not None:
        import capo_opensearch.types.vpc_derived_info_status

        out["vpc_options"] = (
            capo_opensearch.types.vpc_derived_info_status.deserialize_json(
                data["VPCOptions"]
            )
        )
    if data.get("CognitoOptions") is not None:
        import capo_opensearch.types.cognito_options_status

        out["cognito_options"] = (
            capo_opensearch.types.cognito_options_status.deserialize_json(
                data["CognitoOptions"]
            )
        )
    if data.get("EncryptionAtRestOptions") is not None:
        import capo_opensearch.types.encryption_at_rest_options_status

        out["encryption_at_rest_options"] = (
            capo_opensearch.types.encryption_at_rest_options_status.deserialize_json(
                data["EncryptionAtRestOptions"]
            )
        )
    if data.get("NodeToNodeEncryptionOptions") is not None:
        import capo_opensearch.types.node_to_node_encryption_options_status

        out["node_to_node_encryption_options"] = (
            capo_opensearch.types.node_to_node_encryption_options_status.deserialize_json(
                data["NodeToNodeEncryptionOptions"]
            )
        )
    if data.get("AdvancedOptions") is not None:
        import capo_opensearch.types.advanced_options_status

        out["advanced_options"] = (
            capo_opensearch.types.advanced_options_status.deserialize_json(
                data["AdvancedOptions"]
            )
        )
    if data.get("LogPublishingOptions") is not None:
        import capo_opensearch.types.log_publishing_options_status

        out["log_publishing_options"] = (
            capo_opensearch.types.log_publishing_options_status.deserialize_json(
                data["LogPublishingOptions"]
            )
        )
    if data.get("DomainEndpointOptions") is not None:
        import capo_opensearch.types.domain_endpoint_options_status

        out["domain_endpoint_options"] = (
            capo_opensearch.types.domain_endpoint_options_status.deserialize_json(
                data["DomainEndpointOptions"]
            )
        )
    if data.get("AdvancedSecurityOptions") is not None:
        import capo_opensearch.types.advanced_security_options_status

        out["advanced_security_options"] = (
            capo_opensearch.types.advanced_security_options_status.deserialize_json(
                data["AdvancedSecurityOptions"]
            )
        )
    if data.get("IdentityCenterOptions") is not None:
        import capo_opensearch.types.identity_center_options_status

        out["identity_center_options"] = (
            capo_opensearch.types.identity_center_options_status.deserialize_json(
                data["IdentityCenterOptions"]
            )
        )
    if data.get("AutoTuneOptions") is not None:
        import capo_opensearch.types.auto_tune_options_status

        out["auto_tune_options"] = (
            capo_opensearch.types.auto_tune_options_status.deserialize_json(
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
        import capo_opensearch.types.off_peak_window_options_status

        out["off_peak_window_options"] = (
            capo_opensearch.types.off_peak_window_options_status.deserialize_json(
                data["OffPeakWindowOptions"]
            )
        )
    if data.get("SoftwareUpdateOptions") is not None:
        import capo_opensearch.types.software_update_options_status

        out["software_update_options"] = (
            capo_opensearch.types.software_update_options_status.deserialize_json(
                data["SoftwareUpdateOptions"]
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
        import capo_opensearch.types.aiml_options_status

        out["aiml_options"] = (
            capo_opensearch.types.aiml_options_status.deserialize_json(
                data["AIMLOptions"]
            )
        )
    if data.get("DeploymentStrategyOptions") is not None:
        import capo_opensearch.types.deployment_strategy_options_status

        out["deployment_strategy_options"] = (
            capo_opensearch.types.deployment_strategy_options_status.deserialize_json(
                data["DeploymentStrategyOptions"]
            )
        )
    if data.get("AutomatedSnapshotPauseOptions") is not None:
        import capo_opensearch.types.automated_snapshot_pause_options_status

        out["automated_snapshot_pause_options"] = (
            capo_opensearch.types.automated_snapshot_pause_options_status.deserialize_json(
                data["AutomatedSnapshotPauseOptions"]
            )
        )
    if data.get("UseCase") is not None:
        import capo_opensearch.types.use_case_status

        out["use_case"] = capo_opensearch.types.use_case_status.deserialize_json(
            data["UseCase"]
        )
    if data.get("EngineMode") is not None:
        import capo_opensearch.types.engine_mode_status

        out["engine_mode"] = capo_opensearch.types.engine_mode_status.deserialize_json(
            data["EngineMode"]
        )
    return out
