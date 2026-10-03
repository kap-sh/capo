"""Generated from Smithy shape ``com.amazonaws.mwaa#CreateEnvironmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mwaa.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mwaa.types.airflow_configuration_options
    import capo_mwaa.types.airflow_version
    import capo_mwaa.types.endpoint_management
    import capo_mwaa.types.environment_class
    import capo_mwaa.types.environment_name
    import capo_mwaa.types.iam_role_arn
    import capo_mwaa.types.kms_key
    import capo_mwaa.types.logging_configuration_input
    import capo_mwaa.types.max_webservers
    import capo_mwaa.types.max_workers
    import capo_mwaa.types.min_webservers
    import capo_mwaa.types.min_workers
    import capo_mwaa.types.network_configuration
    import capo_mwaa.types.relative_path
    import capo_mwaa.types.s3_bucket_arn
    import capo_mwaa.types.s3_object_version
    import capo_mwaa.types.schedulers
    import capo_mwaa.types.tag_map
    import capo_mwaa.types.webserver_access_mode
    import capo_mwaa.types.weekly_maintenance_window_start


class CreateEnvironmentInput(TypedDict, closed=True):
    name: "capo_mwaa.types.environment_name.EnvironmentName"
    """<p>The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.</p>"""
    execution_role_arn: "capo_mwaa.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the execution role for your environment. An execution role is an Amazon Web Services Identity and Access Management (IAM) role that grants MWAA permission to access Amazon Web Services services and resources used by your environment. For example, <code>arn:aws:iam::123456789:role/my-execution-role</code>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html">Amazon MWAA Execution role</a>.</p>"""
    source_bucket_arn: "capo_mwaa.types.s3_bucket_arn.S3BucketArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored. For example, <code>arn:aws:s3:::my-airflow-bucket-unique-name</code>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html">Create an Amazon S3 bucket for Amazon MWAA</a>.</p>"""
    dag_s3_path: "capo_mwaa.types.relative_path.RelativePath"
    """<p>The relative path to the DAGs folder on your Amazon S3 bucket. For example, <code>dags</code>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html">Adding or updating DAGs</a>.</p>"""
    network_configuration: "capo_mwaa.types.network_configuration.NetworkConfiguration"
    """<p>The VPC networking components used to secure and enable network traffic between the Amazon Web Services resources for your environment. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html">About networking on Amazon MWAA</a>.</p>"""
    plugins_s3_path: NotRequired["capo_mwaa.types.relative_path.RelativePath"]
    """<p>The relative path to the <code>plugins.zip</code> file on your Amazon S3 bucket. For example, <code>plugins.zip</code>. If specified, then the <code>plugins.zip</code> version is required. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html">Installing custom plugins</a>.</p>"""
    plugins_s3_object_version: NotRequired[
        "capo_mwaa.types.s3_object_version.S3ObjectVersion"
    ]
    """<p>The version of the plugins.zip file on your Amazon S3 bucket. You must specify a version each time a plugins.zip file is updated. For more information, refer to <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html">How S3 Versioning works</a>.</p>"""
    requirements_s3_path: NotRequired["capo_mwaa.types.relative_path.RelativePath"]
    """<p>The relative path to the <code>requirements.txt</code> file on your Amazon S3 bucket. For example, <code>requirements.txt</code>. If specified, then a version is required. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html">Installing Python dependencies</a>.</p>"""
    requirements_s3_object_version: NotRequired[
        "capo_mwaa.types.s3_object_version.S3ObjectVersion"
    ]
    """<p>The version of the <code>requirements.txt</code> file on your Amazon S3 bucket. You must specify a version each time a requirements.txt file is updated. For more information, refer to <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html">How S3 Versioning works</a>.</p>"""
    startup_script_s3_path: NotRequired["capo_mwaa.types.relative_path.RelativePath"]
    """<p>The relative path to the startup shell script in your Amazon S3 bucket. For example, <code>s3://mwaa-environment/startup.sh</code>.</p> <p> Amazon MWAA runs the script as your environment starts, and before running the Apache Airflow process. You can use this script to install dependencies, modify Apache Airflow configuration options, and set environment variables. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html">Using a startup script</a>. </p>"""
    startup_script_s3_object_version: NotRequired[
        "capo_mwaa.types.s3_object_version.S3ObjectVersion"
    ]
    """<p>The version of the startup shell script in your Amazon S3 bucket. You must specify the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html">version ID</a> that Amazon S3 assigns to the file every time you update the script. </p> <p> Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example: </p> <p> <code>3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo</code> </p> <p> For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html">Using a startup script</a>. </p>"""
    airflow_configuration_options: NotRequired[
        "capo_mwaa.types.airflow_configuration_options.AirflowConfigurationOptions"
    ]
    """<p>A list of key-value pairs containing the Apache Airflow configuration options you want to attach to your environment. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html">Apache Airflow configuration options</a>.</p>"""
    environment_class: NotRequired["capo_mwaa.types.environment_class.EnvironmentClass"]
    """<p>The environment class type. Valid values: <code>mw1.micro</code>, <code>mw1.small</code>, <code>mw1.medium</code>, <code>mw1.large</code>, <code>mw1.xlarge</code>, and <code>mw1.2xlarge</code>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html">Amazon MWAA environment class</a>.</p>"""
    max_workers: NotRequired["capo_mwaa.types.max_workers.MaxWorkers"]
    """<p>The maximum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the <code>MaxWorkers</code> field. For example, <code>20</code>. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the one worker that is included with your environment, or the number you specify in <code>MinWorkers</code>.</p>"""
    kms_key: NotRequired["capo_mwaa.types.kms_key.KmsKey"]
    """<p>The Amazon Web Services Key Management Service (KMS) key to encrypt the data in your environment. You can use an Amazon Web Services owned CMK, or a Customer managed CMK (advanced). For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/create-environment.html">Create an Amazon MWAA environment</a>.</p>"""
    airflow_version: NotRequired["capo_mwaa.types.airflow_version.AirflowVersion"]
    """<p>The Apache Airflow version for your environment. If no value is specified, it defaults to the latest version. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/airflow-versions.html">Apache Airflow versions on Amazon Managed Workflows for Apache Airflow (Amazon MWAA)</a>.</p> <p>Valid values: <code>2.7.2</code>, <code>2.8.1</code>, <code>2.9.2</code>, <code>2.10.1</code>, <code>2.10.3</code>, <code>2.11.0</code>, and <code>3.0.6</code>.</p>"""
    logging_configuration: NotRequired[
        "capo_mwaa.types.logging_configuration_input.LoggingConfigurationInput"
    ]
    """<p>Defines the Apache Airflow logs to send to CloudWatch Logs.</p>"""
    weekly_maintenance_window_start: NotRequired[
        "capo_mwaa.types.weekly_maintenance_window_start.WeeklyMaintenanceWindowStart"
    ]
    """<p>The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time to start weekly maintenance updates of your environment in the following format: <code>DAY:HH:MM</code>. For example: <code>TUE:03:30</code>. You can specify a start time in 30 minute increments only.</p>"""
    tags: NotRequired["capo_mwaa.types.tag_map.TagMap"]
    """<p>The key-value tag pairs you want to associate to your environment. For example, <code>"Environment": "Staging"</code>. For more information, refer to <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a>.</p>"""
    webserver_access_mode: NotRequired[
        "capo_mwaa.types.webserver_access_mode.WebserverAccessMode"
    ]
    """<p>Defines the access mode for the Apache Airflow <i>web server</i>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html">Apache Airflow access modes</a>.</p> <p>If set to <code>PUBLIC_AND_PRIVATE</code>, creates both a public network load balancer (NLB) for browser access and a private VPC endpoint (VPCE) for worker-to-webserver communication. This mode is only available for Apache Airflow version 3.2 and later.</p>"""
    min_workers: NotRequired["capo_mwaa.types.min_workers.MinWorkers"]
    """<p>The minimum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the <code>MaxWorkers</code> field. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the worker count you specify in the <code>MinWorkers</code> field. For example, <code>2</code>.</p>"""
    schedulers: NotRequired["capo_mwaa.types.schedulers.Schedulers"]
    """<p>The number of Apache Airflow schedulers to run in your environment. Valid values:</p> <ul> <li> <p>v2 - For environments larger than mw1.micro, accepts values from <code>2</code> to <code>5</code>. Defaults to <code>2</code> for all environment sizes except mw1.micro, which defaults to <code>1</code>.</p> </li> <li> <p>v1 - Accepts <code>1</code>.</p> </li> </ul>"""
    endpoint_management: NotRequired[
        "capo_mwaa.types.endpoint_management.EndpointManagement"
    ]
    """<p>Defines whether the VPC endpoints configured for the environment are created, and managed, by the customer or by Amazon MWAA. If set to <code>SERVICE</code>, Amazon MWAA will create and manage the required VPC endpoints in your VPC. If set to <code>CUSTOMER</code>, you must create, and manage, the VPC endpoints for your VPC. If you choose to create an environment in a shared VPC, you must set this value to <code>CUSTOMER</code>. In a shared VPC deployment, the environment will remain in <code>PENDING</code> status until you create the VPC endpoints. If you do not take action to create the endpoints within 72 hours, the status will change to <code>CREATE_FAILED</code>. You can delete the failed environment and create a new one.</p>"""
    min_webservers: NotRequired["capo_mwaa.types.min_webservers.MinWebservers"]
    """<p> The minimum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for <code>MaxWebservers</code> when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. As the transaction-per-second rate, and the network load, decrease, Amazon MWAA disposes of the additional web servers, and scales down to the number set in <code>MinxWebserers</code>. </p> <p>Valid values: For environments larger than mw1.micro, accepts values from <code>2</code> to <code>5</code>. Defaults to <code>2</code> for all environment sizes except mw1.micro, which defaults to <code>1</code>.</p>"""
    max_webservers: NotRequired["capo_mwaa.types.max_webservers.MaxWebservers"]
    """<p> The maximum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for <code>MaxWebservers</code> when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. For example, in scenarios where your workload requires network calls to the Apache Airflow REST API with a high transaction-per-second (TPS) rate, Amazon MWAA will increase the number of web servers up to the number set in <code>MaxWebserers</code>. As TPS rates decrease Amazon MWAA disposes of the additional web servers, and scales down to the number set in <code>MinxWebserers</code>. </p> <p>Valid values: For environments larger than mw1.micro, accepts values from <code>2</code> to <code>5</code>. Defaults to <code>2</code> for all environment sizes except mw1.micro, which defaults to <code>1</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentInput) -> dict:
    out: dict = {}
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    out["SourceBucketArn"] = value["source_bucket_arn"]
    out["DagS3Path"] = value["dag_s3_path"]
    import capo_mwaa.types.network_configuration

    out["NetworkConfiguration"] = capo_mwaa.types.network_configuration.serialize_json(
        value["network_configuration"]
    )
    if "plugins_s3_path" in value:
        out["PluginsS3Path"] = value["plugins_s3_path"]
    if "plugins_s3_object_version" in value:
        out["PluginsS3ObjectVersion"] = value["plugins_s3_object_version"]
    if "requirements_s3_path" in value:
        out["RequirementsS3Path"] = value["requirements_s3_path"]
    if "requirements_s3_object_version" in value:
        out["RequirementsS3ObjectVersion"] = value["requirements_s3_object_version"]
    if "startup_script_s3_path" in value:
        out["StartupScriptS3Path"] = value["startup_script_s3_path"]
    if "startup_script_s3_object_version" in value:
        out["StartupScriptS3ObjectVersion"] = value["startup_script_s3_object_version"]
    if "airflow_configuration_options" in value:
        import capo_mwaa.types.airflow_configuration_options

        out["AirflowConfigurationOptions"] = (
            capo_mwaa.types.airflow_configuration_options.serialize_json(
                value["airflow_configuration_options"]
            )
        )
    if "environment_class" in value:
        out["EnvironmentClass"] = value["environment_class"]
    if "max_workers" in value:
        out["MaxWorkers"] = value["max_workers"]
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    if "airflow_version" in value:
        out["AirflowVersion"] = value["airflow_version"]
    if "logging_configuration" in value:
        import capo_mwaa.types.logging_configuration_input

        out["LoggingConfiguration"] = (
            capo_mwaa.types.logging_configuration_input.serialize_json(
                value["logging_configuration"]
            )
        )
    if "weekly_maintenance_window_start" in value:
        out["WeeklyMaintenanceWindowStart"] = value["weekly_maintenance_window_start"]
    if "tags" in value:
        import capo_mwaa.types.tag_map

        out["Tags"] = capo_mwaa.types.tag_map.serialize_json(value["tags"])
    if "webserver_access_mode" in value:
        out["WebserverAccessMode"] = value["webserver_access_mode"]
    if "min_workers" in value:
        out["MinWorkers"] = value["min_workers"]
    if "schedulers" in value:
        out["Schedulers"] = value["schedulers"]
    if "endpoint_management" in value:
        out["EndpointManagement"] = value["endpoint_management"]
    if "min_webservers" in value:
        out["MinWebservers"] = value["min_webservers"]
    if "max_webservers" in value:
        out["MaxWebservers"] = value["max_webservers"]
    return out


def deserialize_json(data: dict) -> CreateEnvironmentInput:
    out: CreateEnvironmentInput = {}  # type: ignore[typeddict-item]
    if data.get("ExecutionRoleArn") is not None:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        raise DeserializationError("CreateEnvironmentInput.execution_role_arn required")
    if data.get("SourceBucketArn") is not None:
        out["source_bucket_arn"] = data["SourceBucketArn"]
    else:
        raise DeserializationError("CreateEnvironmentInput.source_bucket_arn required")
    if data.get("DagS3Path") is not None:
        out["dag_s3_path"] = data["DagS3Path"]
    else:
        raise DeserializationError("CreateEnvironmentInput.dag_s3_path required")
    if data.get("NetworkConfiguration") is not None:
        import capo_mwaa.types.network_configuration

        out["network_configuration"] = (
            capo_mwaa.types.network_configuration.deserialize_json(
                data["NetworkConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEnvironmentInput.network_configuration required"
        )
    if data.get("PluginsS3Path") is not None:
        out["plugins_s3_path"] = data["PluginsS3Path"]
    if data.get("PluginsS3ObjectVersion") is not None:
        out["plugins_s3_object_version"] = data["PluginsS3ObjectVersion"]
    if data.get("RequirementsS3Path") is not None:
        out["requirements_s3_path"] = data["RequirementsS3Path"]
    if data.get("RequirementsS3ObjectVersion") is not None:
        out["requirements_s3_object_version"] = data["RequirementsS3ObjectVersion"]
    if data.get("StartupScriptS3Path") is not None:
        out["startup_script_s3_path"] = data["StartupScriptS3Path"]
    if data.get("StartupScriptS3ObjectVersion") is not None:
        out["startup_script_s3_object_version"] = data["StartupScriptS3ObjectVersion"]
    if data.get("AirflowConfigurationOptions") is not None:
        import capo_mwaa.types.airflow_configuration_options

        out["airflow_configuration_options"] = (
            capo_mwaa.types.airflow_configuration_options.deserialize_json(
                data["AirflowConfigurationOptions"]
            )
        )
    if data.get("EnvironmentClass") is not None:
        out["environment_class"] = data["EnvironmentClass"]
    if data.get("MaxWorkers") is not None:
        out["max_workers"] = data["MaxWorkers"]
    if data.get("KmsKey") is not None:
        out["kms_key"] = data["KmsKey"]
    if data.get("AirflowVersion") is not None:
        out["airflow_version"] = data["AirflowVersion"]
    if data.get("LoggingConfiguration") is not None:
        import capo_mwaa.types.logging_configuration_input

        out["logging_configuration"] = (
            capo_mwaa.types.logging_configuration_input.deserialize_json(
                data["LoggingConfiguration"]
            )
        )
    if data.get("WeeklyMaintenanceWindowStart") is not None:
        out["weekly_maintenance_window_start"] = data["WeeklyMaintenanceWindowStart"]
    if data.get("Tags") is not None:
        import capo_mwaa.types.tag_map

        out["tags"] = capo_mwaa.types.tag_map.deserialize_json(data["Tags"])
    if data.get("WebserverAccessMode") is not None:
        out["webserver_access_mode"] = data["WebserverAccessMode"]
    if data.get("MinWorkers") is not None:
        out["min_workers"] = data["MinWorkers"]
    if data.get("Schedulers") is not None:
        out["schedulers"] = data["Schedulers"]
    if data.get("EndpointManagement") is not None:
        out["endpoint_management"] = data["EndpointManagement"]
    if data.get("MinWebservers") is not None:
        out["min_webservers"] = data["MinWebservers"]
    if data.get("MaxWebservers") is not None:
        out["max_webservers"] = data["MaxWebservers"]
    return out
