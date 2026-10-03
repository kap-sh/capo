"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.amazon_resource_name
    import capo_config_service.types.recorder_name
    import capo_config_service.types.recording_group
    import capo_config_service.types.recording_mode
    import capo_config_service.types.recording_scope
    import capo_config_service.types.scope_configuration
    import capo_config_service.types.service_principal
    import capo_config_service.types.string


class ConfigurationRecorder(TypedDict, closed=True):
    arn: NotRequired[
        "capo_config_service.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the specified configuration recorder.</p>"""
    name: NotRequired["capo_config_service.types.recorder_name.RecorderName"]
    """<p>The name of the configuration recorder.</p> <p>For customer managed configuration recorders, Config automatically assigns the name of "default" when creating a configuration recorder if you do not specify a name at creation time.</p> <p>For service-linked configuration recorders, Config automatically assigns a name that has the prefix "<code>AWSConfigurationRecorderFor</code>" to a new service-linked configuration recorder.</p> <note> <p> <b>Changing the name of a configuration recorder</b> </p> <p>To change the name of the customer managed configuration recorder, you must delete it and create a new customer managed configuration recorder with a new name.</p> <p>You cannot change the name of a service-linked configuration recorder.</p> </note>"""
    role_arn: NotRequired["capo_config_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role assumed by Config and used by the specified configuration recorder.</p> <note> <p> <b>The server will reject a request without a defined <code>roleARN</code> for the configuration recorder</b> </p> <p>While the API model does not require this field, the server will reject a request without a defined <code>roleARN</code> for the configuration recorder.</p> <p> <b>Policies and compliance results</b> </p> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html">IAM policies</a> and <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html">other policies managed in Organizations</a> can impact whether Config has permissions to record configuration changes for your resources. Additionally, rules directly evaluate the configuration of a resource and rules don't take into account these policies when running evaluations. Make sure that the policies in effect align with how you intend to use Config.</p> <p> <b>Keep Minimum Permisions When Reusing an IAM role</b> </p> <p>If you use an Amazon Web Services service that uses Config, such as Security Hub CSPM or Control Tower, and an IAM role has already been created, make sure that the IAM role that you use when setting up Config keeps the same minimum permissions as the pre-existing IAM role. You must do this to ensure that the other Amazon Web Services service continues to run as expected. </p> <p>For example, if Control Tower has an IAM role that allows Config to read S3 objects, make sure that the same permissions are granted to the IAM role you use when setting up Config. Otherwise, it may interfere with how Control Tower operates.</p> <p> <b>The service-linked IAM role for Config must be used for service-linked configuration recorders</b> </p> <p>For service-linked configuration recorders, you must use the service-linked IAM role for Config: <a href="https://docs.aws.amazon.com/config/latest/developerguide/using-service-linked-roles.html">AWSServiceRoleForConfig</a>.</p> </note>"""
    recording_group: NotRequired[
        "capo_config_service.types.recording_group.RecordingGroup"
    ]
    """<p>Specifies which resource types are in scope for the configuration recorder to record.</p> <note> <p> <b> High Number of Config Evaluations</b> </p> <p>You might notice increased activity in your account during your initial month recording with Config when compared to subsequent months. During the initial bootstrapping process, Config runs evaluations on all the resources in your account that you have selected for Config to record.</p> <p>If you are running ephemeral workloads, you may see increased activity from Config as it records configuration changes associated with creating and deleting these temporary resources. An <i>ephemeral workload</i> is a temporary use of computing resources that are loaded and run when needed. Examples include Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances, Amazon EMR jobs, and Auto Scaling.</p> <p>If you want to avoid the increased activity from running ephemeral workloads, you can set up the configuration recorder to exclude these resource types from being recorded, or run these types of workloads in a separate account with Config turned off to avoid increased configuration recording and rule evaluations.</p> </note>"""
    recording_mode: NotRequired[
        "capo_config_service.types.recording_mode.RecordingMode"
    ]
    """<p>Specifies the default recording frequency for the configuration recorder. Config supports <i>Continuous recording</i> and <i>Daily recording</i>.</p> <ul> <li> <p>Continuous recording allows you to record configuration changes continuously whenever a change occurs.</p> </li> <li> <p>Daily recording allows you to receive a configuration item (CI) representing the most recent state of your resources over the last 24-hour period, only if it’s different from the previous CI recorded. </p> </li> </ul> <note> <p> <b>Some resource types require continuous recording</b> </p> <p>Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous.</p> </note> <p>You can also override the recording frequency for specific resource types.</p>"""
    recording_scope: NotRequired[
        "capo_config_service.types.recording_scope.RecordingScope"
    ]
    """<p>Specifies whether the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html">ConfigurationItems</a> in scope for the specified configuration recorder are recorded for free (<code>INTERNAL</code>) or if it impacts the costs to your bill (<code>PAID</code>).</p>"""
    service_principal: NotRequired[
        "capo_config_service.types.service_principal.ServicePrincipal"
    ]
    """<p>For service-linked configuration recorders, specifies the linked Amazon Web Services service for the configuration recorder.</p>"""
    connector_arn: NotRequired[
        "capo_config_service.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the connector that specifies the connection between a third-party cloud service provider and Config.</p>"""
    scope_configuration: NotRequired[
        "capo_config_service.types.scope_configuration.ScopeConfiguration"
    ]
    """<p>Specifies the scope of resources to record from the third-party cloud service provider connected through the connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationRecorder) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "role_arn" in value:
        out["roleARN"] = value["role_arn"]
    if "recording_group" in value:
        import capo_config_service.types.recording_group

        out["recordingGroup"] = (
            capo_config_service.types.recording_group.serialize_aws_json_1_1(
                value["recording_group"]
            )
        )
    if "recording_mode" in value:
        import capo_config_service.types.recording_mode

        out["recordingMode"] = (
            capo_config_service.types.recording_mode.serialize_aws_json_1_1(
                value["recording_mode"]
            )
        )
    if "recording_scope" in value:
        import capo_config_service.types.recording_scope

        out["recordingScope"] = (
            capo_config_service.types.recording_scope.serialize_aws_json_1_1(
                value["recording_scope"]
            )
        )
    if "service_principal" in value:
        out["servicePrincipal"] = value["service_principal"]
    if "connector_arn" in value:
        out["connectorArn"] = value["connector_arn"]
    if "scope_configuration" in value:
        import capo_config_service.types.scope_configuration

        out["scopeConfiguration"] = (
            capo_config_service.types.scope_configuration.serialize_aws_json_1_1(
                value["scope_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationRecorder:
    out: ConfigurationRecorder = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("roleARN") is not None:
        out["role_arn"] = data["roleARN"]
    if data.get("recordingGroup") is not None:
        import capo_config_service.types.recording_group

        out["recording_group"] = (
            capo_config_service.types.recording_group.deserialize_aws_json_1_1(
                data["recordingGroup"]
            )
        )
    if data.get("recordingMode") is not None:
        import capo_config_service.types.recording_mode

        out["recording_mode"] = (
            capo_config_service.types.recording_mode.deserialize_aws_json_1_1(
                data["recordingMode"]
            )
        )
    if data.get("recordingScope") is not None:
        import capo_config_service.types.recording_scope

        out["recording_scope"] = (
            capo_config_service.types.recording_scope.deserialize_aws_json_1_1(
                data["recordingScope"]
            )
        )
    if data.get("servicePrincipal") is not None:
        out["service_principal"] = data["servicePrincipal"]
    if data.get("connectorArn") is not None:
        out["connector_arn"] = data["connectorArn"]
    if data.get("scopeConfiguration") is not None:
        import capo_config_service.types.scope_configuration

        out["scope_configuration"] = (
            capo_config_service.types.scope_configuration.deserialize_aws_json_1_1(
                data["scopeConfiguration"]
            )
        )
    return out
