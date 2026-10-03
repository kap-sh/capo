"""Generated from Smithy shape ``com.amazonaws.opensearch#CreateDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.advanced_options
    import capo_opensearch.types.advanced_security_options_input
    import capo_opensearch.types.aiml_options_input
    import capo_opensearch.types.auto_tune_options_input
    import capo_opensearch.types.automated_snapshot_pause_request_options
    import capo_opensearch.types.cluster_config
    import capo_opensearch.types.cognito_options
    import capo_opensearch.types.deployment_strategy_options
    import capo_opensearch.types.domain_endpoint_options
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.domain_use_case
    import capo_opensearch.types.ebs_options
    import capo_opensearch.types.encryption_at_rest_options
    import capo_opensearch.types.engine_mode
    import capo_opensearch.types.identity_center_options_input
    import capo_opensearch.types.ip_address_type
    import capo_opensearch.types.log_publishing_options
    import capo_opensearch.types.node_to_node_encryption_options
    import capo_opensearch.types.off_peak_window_options
    import capo_opensearch.types.policy_document
    import capo_opensearch.types.snapshot_options
    import capo_opensearch.types.software_update_options
    import capo_opensearch.types.tag_list
    import capo_opensearch.types.version_string
    import capo_opensearch.types.vpc_options


class CreateDomainRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>Name of the OpenSearch Service domain to create. Domain names are unique across the domains owned by an account within an Amazon Web Services Region.</p>"""
    engine_version: NotRequired["capo_opensearch.types.version_string.VersionString"]
    """<p>String of format Elasticsearch_X.Y or OpenSearch_X.Y to specify the engine version for the OpenSearch Service domain. For example, <code>OpenSearch_1.0</code> or <code>Elasticsearch_7.9</code>. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomains">Creating and managing Amazon OpenSearch Service domains</a>.</p>"""
    cluster_config: NotRequired["capo_opensearch.types.cluster_config.ClusterConfig"]
    """<p>Container for the cluster configuration of a domain.</p>"""
    ebs_options: NotRequired["capo_opensearch.types.ebs_options.EBSOptions"]
    """<p>Container for the parameters required to enable EBS-based storage for an OpenSearch Service domain.</p>"""
    access_policies: NotRequired["capo_opensearch.types.policy_document.PolicyDocument"]
    """<p>Identity and Access Management (IAM) policy document specifying the access policies for the new domain.</p>"""
    ip_address_type: NotRequired["capo_opensearch.types.ip_address_type.IPAddressType"]
    """<p>Specify either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If you set your IP address type to dual stack, you can't change your address type later.</p>"""
    snapshot_options: NotRequired[
        "capo_opensearch.types.snapshot_options.SnapshotOptions"
    ]
    """<p>DEPRECATED. Container for the parameters required to configure automated snapshots of domain indexes.</p>"""
    vpc_options: NotRequired["capo_opensearch.types.vpc_options.VPCOptions"]
    """<p>Container for the values required to configure VPC access domains. If you don't specify these values, OpenSearch Service creates the domain with a public endpoint. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html">Launching your Amazon OpenSearch Service domains using a VPC</a>.</p>"""
    cognito_options: NotRequired["capo_opensearch.types.cognito_options.CognitoOptions"]
    """<p>Key-value pairs to configure Amazon Cognito authentication. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html">Configuring Amazon Cognito authentication for OpenSearch Dashboards</a>.</p>"""
    encryption_at_rest_options: NotRequired[
        "capo_opensearch.types.encryption_at_rest_options.EncryptionAtRestOptions"
    ]
    """<p>Key-value pairs to enable encryption at rest.</p>"""
    node_to_node_encryption_options: NotRequired[
        "capo_opensearch.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
    ]
    """<p>Enables node-to-node encryption.</p>"""
    advanced_options: NotRequired[
        "capo_opensearch.types.advanced_options.AdvancedOptions"
    ]
    """<p>Key-value pairs to specify advanced configuration options. The following key-value pairs are supported:</p> <ul> <li> <p> <code>"rest.action.multi.allow_explicit_index": "true" | "false"</code> - Note the use of a string rather than a boolean. Specifies whether explicit references to indexes are allowed inside the body of HTTP requests. If you want to configure access policies for domain sub-resources, such as specific indexes and domain APIs, you must disable this property. Default is true.</p> </li> <li> <p> <code>"indices.fielddata.cache.size": "80" </code> - Note the use of a string rather than a boolean. Specifies the percentage of heap space allocated to field data. Default is unbounded.</p> </li> <li> <p> <code>"indices.query.bool.max_clause_count": "1024"</code> - Note the use of a string rather than a boolean. Specifies the maximum number of clauses allowed in a Lucene boolean query. Default is 1,024. Queries with more than the permitted number of clauses result in a <code>TooManyClauses</code> error.</p> </li> <li> <p> <code>"override_main_response_version": "true" | "false"</code> - Note the use of a string rather than a boolean. Specifies whether the domain reports its version as 7.10 to allow Elasticsearch OSS clients and plugins to continue working with it. Default is false when creating a domain and true when upgrading a domain.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options">Advanced cluster parameters</a>.</p>"""
    log_publishing_options: NotRequired[
        "capo_opensearch.types.log_publishing_options.LogPublishingOptions"
    ]
    """<p>Key-value pairs to configure log publishing.</p>"""
    domain_endpoint_options: NotRequired[
        "capo_opensearch.types.domain_endpoint_options.DomainEndpointOptions"
    ]
    """<p>Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.</p>"""
    advanced_security_options: NotRequired[
        "capo_opensearch.types.advanced_security_options_input.AdvancedSecurityOptionsInput"
    ]
    """<p>Options for fine-grained access control.</p>"""
    identity_center_options: NotRequired[
        "capo_opensearch.types.identity_center_options_input.IdentityCenterOptionsInput"
    ]
    """<p>Configuration options for enabling and managing IAM Identity Center integration within a domain.</p>"""
    tag_list: NotRequired["capo_opensearch.types.tag_list.TagList"]
    """<p>List of tags to add to the domain upon creation.</p>"""
    auto_tune_options: NotRequired[
        "capo_opensearch.types.auto_tune_options_input.AutoTuneOptionsInput"
    ]
    """<p>Options for Auto-Tune.</p>"""
    off_peak_window_options: NotRequired[
        "capo_opensearch.types.off_peak_window_options.OffPeakWindowOptions"
    ]
    """<p>Specifies a daily 10-hour time block during which OpenSearch Service can perform configuration changes on the domain, including service software updates and Auto-Tune enhancements that require a blue/green deployment. If no options are specified, the default start time of 10:00 P.M. local time (for the Region that the domain is created in) is used.</p>"""
    software_update_options: NotRequired[
        "capo_opensearch.types.software_update_options.SoftwareUpdateOptions"
    ]
    """<p>Software update options for the domain.</p>"""
    aiml_options: NotRequired[
        "capo_opensearch.types.aiml_options_input.AIMLOptionsInput"
    ]
    """<p>Options for all machine learning features for the specified domain.</p>"""
    deployment_strategy_options: NotRequired[
        "capo_opensearch.types.deployment_strategy_options.DeploymentStrategyOptions"
    ]
    """<p>Specifies the deployment strategy options for the domain.</p>"""
    automated_snapshot_pause_options: NotRequired[
        "capo_opensearch.types.automated_snapshot_pause_request_options.AutomatedSnapshotPauseRequestOptions"
    ]
    """<p>Specifies the automated snapshot pause options for the domain.</p> <important> <p>Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.</p> </important> <p>Maximum suspension duration: 3 days.</p>"""
    use_case: NotRequired["capo_opensearch.types.domain_use_case.DomainUseCase"]
    """<p>The primary use case for the domain. For valid values, see <code>DomainUseCase</code>.</p>"""
    engine_mode: NotRequired["capo_opensearch.types.engine_mode.EngineMode"]
    """<p>The engine mode for the domain. For valid values and requirements, see <code>EngineMode</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "cluster_config" in value:
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
        import capo_opensearch.types.vpc_options

        out["VPCOptions"] = capo_opensearch.types.vpc_options.serialize_json(
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
    if "domain_endpoint_options" in value:
        import capo_opensearch.types.domain_endpoint_options

        out["DomainEndpointOptions"] = (
            capo_opensearch.types.domain_endpoint_options.serialize_json(
                value["domain_endpoint_options"]
            )
        )
    if "advanced_security_options" in value:
        import capo_opensearch.types.advanced_security_options_input

        out["AdvancedSecurityOptions"] = (
            capo_opensearch.types.advanced_security_options_input.serialize_json(
                value["advanced_security_options"]
            )
        )
    if "identity_center_options" in value:
        import capo_opensearch.types.identity_center_options_input

        out["IdentityCenterOptions"] = (
            capo_opensearch.types.identity_center_options_input.serialize_json(
                value["identity_center_options"]
            )
        )
    if "tag_list" in value:
        import capo_opensearch.types.tag_list

        out["TagList"] = capo_opensearch.types.tag_list.serialize_json(
            value["tag_list"]
        )
    if "auto_tune_options" in value:
        import capo_opensearch.types.auto_tune_options_input

        out["AutoTuneOptions"] = (
            capo_opensearch.types.auto_tune_options_input.serialize_json(
                value["auto_tune_options"]
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
    if "aiml_options" in value:
        import capo_opensearch.types.aiml_options_input

        out["AIMLOptions"] = capo_opensearch.types.aiml_options_input.serialize_json(
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
        import capo_opensearch.types.automated_snapshot_pause_request_options

        out["AutomatedSnapshotPauseOptions"] = (
            capo_opensearch.types.automated_snapshot_pause_request_options.serialize_json(
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


def deserialize_json(data: dict) -> CreateDomainRequest:
    out: CreateDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("CreateDomainRequest.domain_name required")
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("ClusterConfig") is not None:
        import capo_opensearch.types.cluster_config

        out["cluster_config"] = capo_opensearch.types.cluster_config.deserialize_json(
            data["ClusterConfig"]
        )
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
        import capo_opensearch.types.vpc_options

        out["vpc_options"] = capo_opensearch.types.vpc_options.deserialize_json(
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
    if data.get("DomainEndpointOptions") is not None:
        import capo_opensearch.types.domain_endpoint_options

        out["domain_endpoint_options"] = (
            capo_opensearch.types.domain_endpoint_options.deserialize_json(
                data["DomainEndpointOptions"]
            )
        )
    if data.get("AdvancedSecurityOptions") is not None:
        import capo_opensearch.types.advanced_security_options_input

        out["advanced_security_options"] = (
            capo_opensearch.types.advanced_security_options_input.deserialize_json(
                data["AdvancedSecurityOptions"]
            )
        )
    if data.get("IdentityCenterOptions") is not None:
        import capo_opensearch.types.identity_center_options_input

        out["identity_center_options"] = (
            capo_opensearch.types.identity_center_options_input.deserialize_json(
                data["IdentityCenterOptions"]
            )
        )
    if data.get("TagList") is not None:
        import capo_opensearch.types.tag_list

        out["tag_list"] = capo_opensearch.types.tag_list.deserialize_json(
            data["TagList"]
        )
    if data.get("AutoTuneOptions") is not None:
        import capo_opensearch.types.auto_tune_options_input

        out["auto_tune_options"] = (
            capo_opensearch.types.auto_tune_options_input.deserialize_json(
                data["AutoTuneOptions"]
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
    if data.get("AIMLOptions") is not None:
        import capo_opensearch.types.aiml_options_input

        out["aiml_options"] = capo_opensearch.types.aiml_options_input.deserialize_json(
            data["AIMLOptions"]
        )
    if data.get("DeploymentStrategyOptions") is not None:
        import capo_opensearch.types.deployment_strategy_options

        out["deployment_strategy_options"] = (
            capo_opensearch.types.deployment_strategy_options.deserialize_json(
                data["DeploymentStrategyOptions"]
            )
        )
    if data.get("AutomatedSnapshotPauseOptions") is not None:
        import capo_opensearch.types.automated_snapshot_pause_request_options

        out["automated_snapshot_pause_options"] = (
            capo_opensearch.types.automated_snapshot_pause_request_options.deserialize_json(
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
