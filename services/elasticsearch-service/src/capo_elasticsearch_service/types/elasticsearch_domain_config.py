"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ElasticsearchDomainConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.access_policies_status
    import capo_elasticsearch_service.types.advanced_options_status
    import capo_elasticsearch_service.types.advanced_security_options_status
    import capo_elasticsearch_service.types.auto_tune_options_status
    import capo_elasticsearch_service.types.automated_snapshot_pause_options_status
    import capo_elasticsearch_service.types.change_progress_details
    import capo_elasticsearch_service.types.cognito_options_status
    import capo_elasticsearch_service.types.deployment_strategy_options_status
    import capo_elasticsearch_service.types.domain_endpoint_options_status
    import capo_elasticsearch_service.types.ebs_options_status
    import capo_elasticsearch_service.types.elasticsearch_cluster_config_status
    import capo_elasticsearch_service.types.elasticsearch_version_status
    import capo_elasticsearch_service.types.encryption_at_rest_options_status
    import capo_elasticsearch_service.types.engine_mode_status
    import capo_elasticsearch_service.types.log_publishing_options_status
    import capo_elasticsearch_service.types.modifying_properties_list
    import capo_elasticsearch_service.types.node_to_node_encryption_options_status
    import capo_elasticsearch_service.types.snapshot_options_status
    import capo_elasticsearch_service.types.use_case_status
    import capo_elasticsearch_service.types.vpc_derived_info_status


class ElasticsearchDomainConfig(TypedDict, closed=True):
    elasticsearch_version: NotRequired[
        "capo_elasticsearch_service.types.elasticsearch_version_status.ElasticsearchVersionStatus"
    ]
    """<p>String of format X.Y to specify version for the Elasticsearch domain.</p>"""
    elasticsearch_cluster_config: NotRequired[
        "capo_elasticsearch_service.types.elasticsearch_cluster_config_status.ElasticsearchClusterConfigStatus"
    ]
    """<p>Specifies the <code>ElasticsearchClusterConfig</code> for the Elasticsearch domain.</p>"""
    ebs_options: NotRequired[
        "capo_elasticsearch_service.types.ebs_options_status.EBSOptionsStatus"
    ]
    """<p>Specifies the <code>EBSOptions</code> for the Elasticsearch domain.</p>"""
    access_policies: NotRequired[
        "capo_elasticsearch_service.types.access_policies_status.AccessPoliciesStatus"
    ]
    """<p>IAM access policy as a JSON-formatted string.</p>"""
    snapshot_options: NotRequired[
        "capo_elasticsearch_service.types.snapshot_options_status.SnapshotOptionsStatus"
    ]
    """<p>Specifies the <code>SnapshotOptions</code> for the Elasticsearch domain.</p>"""
    vpc_options: NotRequired[
        "capo_elasticsearch_service.types.vpc_derived_info_status.VPCDerivedInfoStatus"
    ]
    """<p>The <code>VPCOptions</code> for the specified domain. For more information, see <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html" target="_blank">VPC Endpoints for Amazon Elasticsearch Service Domains</a>.</p>"""
    cognito_options: NotRequired[
        "capo_elasticsearch_service.types.cognito_options_status.CognitoOptionsStatus"
    ]
    """<p>The <code>CognitoOptions</code> for the specified domain. For more information, see <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html" target="_blank">Amazon Cognito Authentication for Kibana</a>.</p>"""
    encryption_at_rest_options: NotRequired[
        "capo_elasticsearch_service.types.encryption_at_rest_options_status.EncryptionAtRestOptionsStatus"
    ]
    """<p>Specifies the <code>EncryptionAtRestOptions</code> for the Elasticsearch domain.</p>"""
    node_to_node_encryption_options: NotRequired[
        "capo_elasticsearch_service.types.node_to_node_encryption_options_status.NodeToNodeEncryptionOptionsStatus"
    ]
    """<p>Specifies the <code>NodeToNodeEncryptionOptions</code> for the Elasticsearch domain.</p>"""
    advanced_options: NotRequired[
        "capo_elasticsearch_service.types.advanced_options_status.AdvancedOptionsStatus"
    ]
    """<p>Specifies the <code>AdvancedOptions</code> for the domain. See <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options" target="_blank">Configuring Advanced Options</a> for more information.</p>"""
    log_publishing_options: NotRequired[
        "capo_elasticsearch_service.types.log_publishing_options_status.LogPublishingOptionsStatus"
    ]
    """<p>Log publishing options for the given domain.</p>"""
    domain_endpoint_options: NotRequired[
        "capo_elasticsearch_service.types.domain_endpoint_options_status.DomainEndpointOptionsStatus"
    ]
    """<p>Specifies the <code>DomainEndpointOptions</code> for the Elasticsearch domain.</p>"""
    advanced_security_options: NotRequired[
        "capo_elasticsearch_service.types.advanced_security_options_status.AdvancedSecurityOptionsStatus"
    ]
    """<p>Specifies <code>AdvancedSecurityOptions</code> for the domain. </p>"""
    auto_tune_options: NotRequired[
        "capo_elasticsearch_service.types.auto_tune_options_status.AutoTuneOptionsStatus"
    ]
    """<p>Specifies <code>AutoTuneOptions</code> for the domain. </p>"""
    change_progress_details: NotRequired[
        "capo_elasticsearch_service.types.change_progress_details.ChangeProgressDetails"
    ]
    """<p>Specifies change details of the domain configuration change.</p>"""
    modifying_properties: NotRequired[
        "capo_elasticsearch_service.types.modifying_properties_list.ModifyingPropertiesList"
    ]
    """<p>Information about the domain properties that are currently being modified.</p>"""
    deployment_strategy_options: NotRequired[
        "capo_elasticsearch_service.types.deployment_strategy_options_status.DeploymentStrategyOptionsStatus"
    ]
    """<p>Specifies <code>DeploymentStrategyOptions</code> for the domain. </p>"""
    automated_snapshot_pause_options: NotRequired[
        "capo_elasticsearch_service.types.automated_snapshot_pause_options_status.AutomatedSnapshotPauseOptionsStatus"
    ]
    """<p>Specifies <code>AutomatedSnapshotPauseOptions</code> for the domain. </p>"""
    use_case: NotRequired[
        "capo_elasticsearch_service.types.use_case_status.UseCaseStatus"
    ]
    """<p>The use case configured for the domain.</p>"""
    engine_mode: NotRequired[
        "capo_elasticsearch_service.types.engine_mode_status.EngineModeStatus"
    ]
    """<p>The engine mode configured for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElasticsearchDomainConfig) -> dict:
    out: dict = {}
    if "elasticsearch_version" in value:
        import capo_elasticsearch_service.types.elasticsearch_version_status

        out["ElasticsearchVersion"] = (
            capo_elasticsearch_service.types.elasticsearch_version_status.serialize_json(
                value["elasticsearch_version"]
            )
        )
    if "elasticsearch_cluster_config" in value:
        import capo_elasticsearch_service.types.elasticsearch_cluster_config_status

        out["ElasticsearchClusterConfig"] = (
            capo_elasticsearch_service.types.elasticsearch_cluster_config_status.serialize_json(
                value["elasticsearch_cluster_config"]
            )
        )
    if "ebs_options" in value:
        import capo_elasticsearch_service.types.ebs_options_status

        out["EBSOptions"] = (
            capo_elasticsearch_service.types.ebs_options_status.serialize_json(
                value["ebs_options"]
            )
        )
    if "access_policies" in value:
        import capo_elasticsearch_service.types.access_policies_status

        out["AccessPolicies"] = (
            capo_elasticsearch_service.types.access_policies_status.serialize_json(
                value["access_policies"]
            )
        )
    if "snapshot_options" in value:
        import capo_elasticsearch_service.types.snapshot_options_status

        out["SnapshotOptions"] = (
            capo_elasticsearch_service.types.snapshot_options_status.serialize_json(
                value["snapshot_options"]
            )
        )
    if "vpc_options" in value:
        import capo_elasticsearch_service.types.vpc_derived_info_status

        out["VPCOptions"] = (
            capo_elasticsearch_service.types.vpc_derived_info_status.serialize_json(
                value["vpc_options"]
            )
        )
    if "cognito_options" in value:
        import capo_elasticsearch_service.types.cognito_options_status

        out["CognitoOptions"] = (
            capo_elasticsearch_service.types.cognito_options_status.serialize_json(
                value["cognito_options"]
            )
        )
    if "encryption_at_rest_options" in value:
        import capo_elasticsearch_service.types.encryption_at_rest_options_status

        out["EncryptionAtRestOptions"] = (
            capo_elasticsearch_service.types.encryption_at_rest_options_status.serialize_json(
                value["encryption_at_rest_options"]
            )
        )
    if "node_to_node_encryption_options" in value:
        import capo_elasticsearch_service.types.node_to_node_encryption_options_status

        out["NodeToNodeEncryptionOptions"] = (
            capo_elasticsearch_service.types.node_to_node_encryption_options_status.serialize_json(
                value["node_to_node_encryption_options"]
            )
        )
    if "advanced_options" in value:
        import capo_elasticsearch_service.types.advanced_options_status

        out["AdvancedOptions"] = (
            capo_elasticsearch_service.types.advanced_options_status.serialize_json(
                value["advanced_options"]
            )
        )
    if "log_publishing_options" in value:
        import capo_elasticsearch_service.types.log_publishing_options_status

        out["LogPublishingOptions"] = (
            capo_elasticsearch_service.types.log_publishing_options_status.serialize_json(
                value["log_publishing_options"]
            )
        )
    if "domain_endpoint_options" in value:
        import capo_elasticsearch_service.types.domain_endpoint_options_status

        out["DomainEndpointOptions"] = (
            capo_elasticsearch_service.types.domain_endpoint_options_status.serialize_json(
                value["domain_endpoint_options"]
            )
        )
    if "advanced_security_options" in value:
        import capo_elasticsearch_service.types.advanced_security_options_status

        out["AdvancedSecurityOptions"] = (
            capo_elasticsearch_service.types.advanced_security_options_status.serialize_json(
                value["advanced_security_options"]
            )
        )
    if "auto_tune_options" in value:
        import capo_elasticsearch_service.types.auto_tune_options_status

        out["AutoTuneOptions"] = (
            capo_elasticsearch_service.types.auto_tune_options_status.serialize_json(
                value["auto_tune_options"]
            )
        )
    if "change_progress_details" in value:
        import capo_elasticsearch_service.types.change_progress_details

        out["ChangeProgressDetails"] = (
            capo_elasticsearch_service.types.change_progress_details.serialize_json(
                value["change_progress_details"]
            )
        )
    if "modifying_properties" in value:
        import capo_elasticsearch_service.types.modifying_properties_list

        out["ModifyingProperties"] = (
            capo_elasticsearch_service.types.modifying_properties_list.serialize_json(
                value["modifying_properties"]
            )
        )
    if "deployment_strategy_options" in value:
        import capo_elasticsearch_service.types.deployment_strategy_options_status

        out["DeploymentStrategyOptions"] = (
            capo_elasticsearch_service.types.deployment_strategy_options_status.serialize_json(
                value["deployment_strategy_options"]
            )
        )
    if "automated_snapshot_pause_options" in value:
        import capo_elasticsearch_service.types.automated_snapshot_pause_options_status

        out["AutomatedSnapshotPauseOptions"] = (
            capo_elasticsearch_service.types.automated_snapshot_pause_options_status.serialize_json(
                value["automated_snapshot_pause_options"]
            )
        )
    if "use_case" in value:
        import capo_elasticsearch_service.types.use_case_status

        out["UseCase"] = (
            capo_elasticsearch_service.types.use_case_status.serialize_json(
                value["use_case"]
            )
        )
    if "engine_mode" in value:
        import capo_elasticsearch_service.types.engine_mode_status

        out["EngineMode"] = (
            capo_elasticsearch_service.types.engine_mode_status.serialize_json(
                value["engine_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> ElasticsearchDomainConfig:
    out: ElasticsearchDomainConfig = {}  # type: ignore[typeddict-item]
    if data.get("ElasticsearchVersion") is not None:
        import capo_elasticsearch_service.types.elasticsearch_version_status

        out["elasticsearch_version"] = (
            capo_elasticsearch_service.types.elasticsearch_version_status.deserialize_json(
                data["ElasticsearchVersion"]
            )
        )
    if data.get("ElasticsearchClusterConfig") is not None:
        import capo_elasticsearch_service.types.elasticsearch_cluster_config_status

        out["elasticsearch_cluster_config"] = (
            capo_elasticsearch_service.types.elasticsearch_cluster_config_status.deserialize_json(
                data["ElasticsearchClusterConfig"]
            )
        )
    if data.get("EBSOptions") is not None:
        import capo_elasticsearch_service.types.ebs_options_status

        out["ebs_options"] = (
            capo_elasticsearch_service.types.ebs_options_status.deserialize_json(
                data["EBSOptions"]
            )
        )
    if data.get("AccessPolicies") is not None:
        import capo_elasticsearch_service.types.access_policies_status

        out["access_policies"] = (
            capo_elasticsearch_service.types.access_policies_status.deserialize_json(
                data["AccessPolicies"]
            )
        )
    if data.get("SnapshotOptions") is not None:
        import capo_elasticsearch_service.types.snapshot_options_status

        out["snapshot_options"] = (
            capo_elasticsearch_service.types.snapshot_options_status.deserialize_json(
                data["SnapshotOptions"]
            )
        )
    if data.get("VPCOptions") is not None:
        import capo_elasticsearch_service.types.vpc_derived_info_status

        out["vpc_options"] = (
            capo_elasticsearch_service.types.vpc_derived_info_status.deserialize_json(
                data["VPCOptions"]
            )
        )
    if data.get("CognitoOptions") is not None:
        import capo_elasticsearch_service.types.cognito_options_status

        out["cognito_options"] = (
            capo_elasticsearch_service.types.cognito_options_status.deserialize_json(
                data["CognitoOptions"]
            )
        )
    if data.get("EncryptionAtRestOptions") is not None:
        import capo_elasticsearch_service.types.encryption_at_rest_options_status

        out["encryption_at_rest_options"] = (
            capo_elasticsearch_service.types.encryption_at_rest_options_status.deserialize_json(
                data["EncryptionAtRestOptions"]
            )
        )
    if data.get("NodeToNodeEncryptionOptions") is not None:
        import capo_elasticsearch_service.types.node_to_node_encryption_options_status

        out["node_to_node_encryption_options"] = (
            capo_elasticsearch_service.types.node_to_node_encryption_options_status.deserialize_json(
                data["NodeToNodeEncryptionOptions"]
            )
        )
    if data.get("AdvancedOptions") is not None:
        import capo_elasticsearch_service.types.advanced_options_status

        out["advanced_options"] = (
            capo_elasticsearch_service.types.advanced_options_status.deserialize_json(
                data["AdvancedOptions"]
            )
        )
    if data.get("LogPublishingOptions") is not None:
        import capo_elasticsearch_service.types.log_publishing_options_status

        out["log_publishing_options"] = (
            capo_elasticsearch_service.types.log_publishing_options_status.deserialize_json(
                data["LogPublishingOptions"]
            )
        )
    if data.get("DomainEndpointOptions") is not None:
        import capo_elasticsearch_service.types.domain_endpoint_options_status

        out["domain_endpoint_options"] = (
            capo_elasticsearch_service.types.domain_endpoint_options_status.deserialize_json(
                data["DomainEndpointOptions"]
            )
        )
    if data.get("AdvancedSecurityOptions") is not None:
        import capo_elasticsearch_service.types.advanced_security_options_status

        out["advanced_security_options"] = (
            capo_elasticsearch_service.types.advanced_security_options_status.deserialize_json(
                data["AdvancedSecurityOptions"]
            )
        )
    if data.get("AutoTuneOptions") is not None:
        import capo_elasticsearch_service.types.auto_tune_options_status

        out["auto_tune_options"] = (
            capo_elasticsearch_service.types.auto_tune_options_status.deserialize_json(
                data["AutoTuneOptions"]
            )
        )
    if data.get("ChangeProgressDetails") is not None:
        import capo_elasticsearch_service.types.change_progress_details

        out["change_progress_details"] = (
            capo_elasticsearch_service.types.change_progress_details.deserialize_json(
                data["ChangeProgressDetails"]
            )
        )
    if data.get("ModifyingProperties") is not None:
        import capo_elasticsearch_service.types.modifying_properties_list

        out["modifying_properties"] = (
            capo_elasticsearch_service.types.modifying_properties_list.deserialize_json(
                data["ModifyingProperties"]
            )
        )
    if data.get("DeploymentStrategyOptions") is not None:
        import capo_elasticsearch_service.types.deployment_strategy_options_status

        out["deployment_strategy_options"] = (
            capo_elasticsearch_service.types.deployment_strategy_options_status.deserialize_json(
                data["DeploymentStrategyOptions"]
            )
        )
    if data.get("AutomatedSnapshotPauseOptions") is not None:
        import capo_elasticsearch_service.types.automated_snapshot_pause_options_status

        out["automated_snapshot_pause_options"] = (
            capo_elasticsearch_service.types.automated_snapshot_pause_options_status.deserialize_json(
                data["AutomatedSnapshotPauseOptions"]
            )
        )
    if data.get("UseCase") is not None:
        import capo_elasticsearch_service.types.use_case_status

        out["use_case"] = (
            capo_elasticsearch_service.types.use_case_status.deserialize_json(
                data["UseCase"]
            )
        )
    if data.get("EngineMode") is not None:
        import capo_elasticsearch_service.types.engine_mode_status

        out["engine_mode"] = (
            capo_elasticsearch_service.types.engine_mode_status.deserialize_json(
                data["EngineMode"]
            )
        )
    return out
