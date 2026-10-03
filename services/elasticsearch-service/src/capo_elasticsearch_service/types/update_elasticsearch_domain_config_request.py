"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpdateElasticsearchDomainConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.advanced_options
    import capo_elasticsearch_service.types.advanced_security_options_input
    import capo_elasticsearch_service.types.auto_tune_options
    import capo_elasticsearch_service.types.automated_snapshot_pause_request_options
    import capo_elasticsearch_service.types.cognito_options
    import capo_elasticsearch_service.types.deployment_strategy_options
    import capo_elasticsearch_service.types.domain_endpoint_options
    import capo_elasticsearch_service.types.domain_engine_mode
    import capo_elasticsearch_service.types.domain_name
    import capo_elasticsearch_service.types.domain_use_case
    import capo_elasticsearch_service.types.dry_run
    import capo_elasticsearch_service.types.ebs_options
    import capo_elasticsearch_service.types.elasticsearch_cluster_config
    import capo_elasticsearch_service.types.encryption_at_rest_options
    import capo_elasticsearch_service.types.log_publishing_options
    import capo_elasticsearch_service.types.node_to_node_encryption_options
    import capo_elasticsearch_service.types.policy_document
    import capo_elasticsearch_service.types.snapshot_options
    import capo_elasticsearch_service.types.vpc_options


class UpdateElasticsearchDomainConfigRequest(TypedDict, closed=True):
    domain_name: "capo_elasticsearch_service.types.domain_name.DomainName"
    """<p>The name of the Elasticsearch domain that you are updating. </p>"""
    elasticsearch_cluster_config: NotRequired[
        "capo_elasticsearch_service.types.elasticsearch_cluster_config.ElasticsearchClusterConfig"
    ]
    """<p>The type and number of instances to instantiate for the domain cluster.</p>"""
    ebs_options: NotRequired["capo_elasticsearch_service.types.ebs_options.EBSOptions"]
    """<p>Specify the type and size of the EBS volume that you want to use. </p>"""
    snapshot_options: NotRequired[
        "capo_elasticsearch_service.types.snapshot_options.SnapshotOptions"
    ]
    """<p>Option to set the time, in UTC format, for the daily automated snapshot. Default value is <code>0</code> hours. </p>"""
    vpc_options: NotRequired["capo_elasticsearch_service.types.vpc_options.VPCOptions"]
    """<p>Options to specify the subnets and security groups for VPC endpoint. For more information, see <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-creating-vpc" target="_blank">Creating a VPC</a> in <i>VPC Endpoints for Amazon Elasticsearch Service Domains</i></p>"""
    cognito_options: NotRequired[
        "capo_elasticsearch_service.types.cognito_options.CognitoOptions"
    ]
    """<p>Options to specify the Cognito user and identity pools for Kibana authentication. For more information, see <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html" target="_blank">Amazon Cognito Authentication for Kibana</a>.</p>"""
    advanced_options: NotRequired[
        "capo_elasticsearch_service.types.advanced_options.AdvancedOptions"
    ]
    """<p>Modifies the advanced option to allow references to indices in an HTTP request body. Must be <code>false</code> when configuring access to individual sub-resources. By default, the value is <code>true</code>. See <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options" target="_blank">Configuration Advanced Options</a> for more information.</p>"""
    access_policies: NotRequired[
        "capo_elasticsearch_service.types.policy_document.PolicyDocument"
    ]
    """<p>IAM access policy as a JSON-formatted string.</p>"""
    log_publishing_options: NotRequired[
        "capo_elasticsearch_service.types.log_publishing_options.LogPublishingOptions"
    ]
    """<p>Map of <code>LogType</code> and <code>LogPublishingOption</code>, each containing options to publish a given type of Elasticsearch log.</p>"""
    domain_endpoint_options: NotRequired[
        "capo_elasticsearch_service.types.domain_endpoint_options.DomainEndpointOptions"
    ]
    """<p>Options to specify configuration that will be applied to the domain endpoint.</p>"""
    advanced_security_options: NotRequired[
        "capo_elasticsearch_service.types.advanced_security_options_input.AdvancedSecurityOptionsInput"
    ]
    """<p>Specifies advanced security options.</p>"""
    node_to_node_encryption_options: NotRequired[
        "capo_elasticsearch_service.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
    ]
    """<p>Specifies the NodeToNodeEncryptionOptions.</p>"""
    encryption_at_rest_options: NotRequired[
        "capo_elasticsearch_service.types.encryption_at_rest_options.EncryptionAtRestOptions"
    ]
    """<p>Specifies the Encryption At Rest Options.</p>"""
    auto_tune_options: NotRequired[
        "capo_elasticsearch_service.types.auto_tune_options.AutoTuneOptions"
    ]
    """<p>Specifies Auto-Tune options.</p>"""
    dry_run: NotRequired["capo_elasticsearch_service.types.dry_run.DryRun"]
    """<p> This flag, when set to True, specifies whether the <code>UpdateElasticsearchDomain</code> request should return the results of validation checks without actually applying the change. This flag, when set to True, specifies the deployment mechanism through which the update shall be applied on the domain. This will not actually perform the Update. </p>"""
    deployment_strategy_options: NotRequired[
        "capo_elasticsearch_service.types.deployment_strategy_options.DeploymentStrategyOptions"
    ]
    """<p>Specifies the deployment strategy options.</p>"""
    automated_snapshot_pause_options: NotRequired[
        "capo_elasticsearch_service.types.automated_snapshot_pause_request_options.AutomatedSnapshotPauseRequestOptions"
    ]
    """<p>Specifies the automated snapshot pause options for the domain.</p> <important> <p>Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.</p> </important> <p>Maximum suspension duration: 3 days.</p>"""
    use_case: NotRequired[
        "capo_elasticsearch_service.types.domain_use_case.DomainUseCase"
    ]
    """<p>The primary use case for the domain. For valid values, see <code>DomainUseCase</code>.</p>"""
    engine_mode: NotRequired[
        "capo_elasticsearch_service.types.domain_engine_mode.DomainEngineMode"
    ]
    """<p>The engine mode for the domain. For valid values and requirements, see <code>DomainEngineMode</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateElasticsearchDomainConfigRequest) -> dict:
    out: dict = {}
    if "elasticsearch_cluster_config" in value:
        import capo_elasticsearch_service.types.elasticsearch_cluster_config

        out["ElasticsearchClusterConfig"] = (
            capo_elasticsearch_service.types.elasticsearch_cluster_config.serialize_json(
                value["elasticsearch_cluster_config"]
            )
        )
    if "ebs_options" in value:
        import capo_elasticsearch_service.types.ebs_options

        out["EBSOptions"] = capo_elasticsearch_service.types.ebs_options.serialize_json(
            value["ebs_options"]
        )
    if "snapshot_options" in value:
        import capo_elasticsearch_service.types.snapshot_options

        out["SnapshotOptions"] = (
            capo_elasticsearch_service.types.snapshot_options.serialize_json(
                value["snapshot_options"]
            )
        )
    if "vpc_options" in value:
        import capo_elasticsearch_service.types.vpc_options

        out["VPCOptions"] = capo_elasticsearch_service.types.vpc_options.serialize_json(
            value["vpc_options"]
        )
    if "cognito_options" in value:
        import capo_elasticsearch_service.types.cognito_options

        out["CognitoOptions"] = (
            capo_elasticsearch_service.types.cognito_options.serialize_json(
                value["cognito_options"]
            )
        )
    if "advanced_options" in value:
        import capo_elasticsearch_service.types.advanced_options

        out["AdvancedOptions"] = (
            capo_elasticsearch_service.types.advanced_options.serialize_json(
                value["advanced_options"]
            )
        )
    if "access_policies" in value:
        out["AccessPolicies"] = value["access_policies"]
    if "log_publishing_options" in value:
        import capo_elasticsearch_service.types.log_publishing_options

        out["LogPublishingOptions"] = (
            capo_elasticsearch_service.types.log_publishing_options.serialize_json(
                value["log_publishing_options"]
            )
        )
    if "domain_endpoint_options" in value:
        import capo_elasticsearch_service.types.domain_endpoint_options

        out["DomainEndpointOptions"] = (
            capo_elasticsearch_service.types.domain_endpoint_options.serialize_json(
                value["domain_endpoint_options"]
            )
        )
    if "advanced_security_options" in value:
        import capo_elasticsearch_service.types.advanced_security_options_input

        out["AdvancedSecurityOptions"] = (
            capo_elasticsearch_service.types.advanced_security_options_input.serialize_json(
                value["advanced_security_options"]
            )
        )
    if "node_to_node_encryption_options" in value:
        import capo_elasticsearch_service.types.node_to_node_encryption_options

        out["NodeToNodeEncryptionOptions"] = (
            capo_elasticsearch_service.types.node_to_node_encryption_options.serialize_json(
                value["node_to_node_encryption_options"]
            )
        )
    if "encryption_at_rest_options" in value:
        import capo_elasticsearch_service.types.encryption_at_rest_options

        out["EncryptionAtRestOptions"] = (
            capo_elasticsearch_service.types.encryption_at_rest_options.serialize_json(
                value["encryption_at_rest_options"]
            )
        )
    if "auto_tune_options" in value:
        import capo_elasticsearch_service.types.auto_tune_options

        out["AutoTuneOptions"] = (
            capo_elasticsearch_service.types.auto_tune_options.serialize_json(
                value["auto_tune_options"]
            )
        )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    if "deployment_strategy_options" in value:
        import capo_elasticsearch_service.types.deployment_strategy_options

        out["DeploymentStrategyOptions"] = (
            capo_elasticsearch_service.types.deployment_strategy_options.serialize_json(
                value["deployment_strategy_options"]
            )
        )
    if "automated_snapshot_pause_options" in value:
        import capo_elasticsearch_service.types.automated_snapshot_pause_request_options

        out["AutomatedSnapshotPauseOptions"] = (
            capo_elasticsearch_service.types.automated_snapshot_pause_request_options.serialize_json(
                value["automated_snapshot_pause_options"]
            )
        )
    if "use_case" in value:
        import capo_elasticsearch_service.types.domain_use_case

        out["UseCase"] = (
            capo_elasticsearch_service.types.domain_use_case.serialize_json(
                value["use_case"]
            )
        )
    if "engine_mode" in value:
        import capo_elasticsearch_service.types.domain_engine_mode

        out["EngineMode"] = (
            capo_elasticsearch_service.types.domain_engine_mode.serialize_json(
                value["engine_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateElasticsearchDomainConfigRequest:
    out: UpdateElasticsearchDomainConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("ElasticsearchClusterConfig") is not None:
        import capo_elasticsearch_service.types.elasticsearch_cluster_config

        out["elasticsearch_cluster_config"] = (
            capo_elasticsearch_service.types.elasticsearch_cluster_config.deserialize_json(
                data["ElasticsearchClusterConfig"]
            )
        )
    if data.get("EBSOptions") is not None:
        import capo_elasticsearch_service.types.ebs_options

        out["ebs_options"] = (
            capo_elasticsearch_service.types.ebs_options.deserialize_json(
                data["EBSOptions"]
            )
        )
    if data.get("SnapshotOptions") is not None:
        import capo_elasticsearch_service.types.snapshot_options

        out["snapshot_options"] = (
            capo_elasticsearch_service.types.snapshot_options.deserialize_json(
                data["SnapshotOptions"]
            )
        )
    if data.get("VPCOptions") is not None:
        import capo_elasticsearch_service.types.vpc_options

        out["vpc_options"] = (
            capo_elasticsearch_service.types.vpc_options.deserialize_json(
                data["VPCOptions"]
            )
        )
    if data.get("CognitoOptions") is not None:
        import capo_elasticsearch_service.types.cognito_options

        out["cognito_options"] = (
            capo_elasticsearch_service.types.cognito_options.deserialize_json(
                data["CognitoOptions"]
            )
        )
    if data.get("AdvancedOptions") is not None:
        import capo_elasticsearch_service.types.advanced_options

        out["advanced_options"] = (
            capo_elasticsearch_service.types.advanced_options.deserialize_json(
                data["AdvancedOptions"]
            )
        )
    if data.get("AccessPolicies") is not None:
        out["access_policies"] = data["AccessPolicies"]
    if data.get("LogPublishingOptions") is not None:
        import capo_elasticsearch_service.types.log_publishing_options

        out["log_publishing_options"] = (
            capo_elasticsearch_service.types.log_publishing_options.deserialize_json(
                data["LogPublishingOptions"]
            )
        )
    if data.get("DomainEndpointOptions") is not None:
        import capo_elasticsearch_service.types.domain_endpoint_options

        out["domain_endpoint_options"] = (
            capo_elasticsearch_service.types.domain_endpoint_options.deserialize_json(
                data["DomainEndpointOptions"]
            )
        )
    if data.get("AdvancedSecurityOptions") is not None:
        import capo_elasticsearch_service.types.advanced_security_options_input

        out["advanced_security_options"] = (
            capo_elasticsearch_service.types.advanced_security_options_input.deserialize_json(
                data["AdvancedSecurityOptions"]
            )
        )
    if data.get("NodeToNodeEncryptionOptions") is not None:
        import capo_elasticsearch_service.types.node_to_node_encryption_options

        out["node_to_node_encryption_options"] = (
            capo_elasticsearch_service.types.node_to_node_encryption_options.deserialize_json(
                data["NodeToNodeEncryptionOptions"]
            )
        )
    if data.get("EncryptionAtRestOptions") is not None:
        import capo_elasticsearch_service.types.encryption_at_rest_options

        out["encryption_at_rest_options"] = (
            capo_elasticsearch_service.types.encryption_at_rest_options.deserialize_json(
                data["EncryptionAtRestOptions"]
            )
        )
    if data.get("AutoTuneOptions") is not None:
        import capo_elasticsearch_service.types.auto_tune_options

        out["auto_tune_options"] = (
            capo_elasticsearch_service.types.auto_tune_options.deserialize_json(
                data["AutoTuneOptions"]
            )
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    if data.get("DeploymentStrategyOptions") is not None:
        import capo_elasticsearch_service.types.deployment_strategy_options

        out["deployment_strategy_options"] = (
            capo_elasticsearch_service.types.deployment_strategy_options.deserialize_json(
                data["DeploymentStrategyOptions"]
            )
        )
    if data.get("AutomatedSnapshotPauseOptions") is not None:
        import capo_elasticsearch_service.types.automated_snapshot_pause_request_options

        out["automated_snapshot_pause_options"] = (
            capo_elasticsearch_service.types.automated_snapshot_pause_request_options.deserialize_json(
                data["AutomatedSnapshotPauseOptions"]
            )
        )
    if data.get("UseCase") is not None:
        import capo_elasticsearch_service.types.domain_use_case

        out["use_case"] = (
            capo_elasticsearch_service.types.domain_use_case.deserialize_json(
                data["UseCase"]
            )
        )
    if data.get("EngineMode") is not None:
        import capo_elasticsearch_service.types.domain_engine_mode

        out["engine_mode"] = (
            capo_elasticsearch_service.types.domain_engine_mode.deserialize_json(
                data["EngineMode"]
            )
        )
    return out
