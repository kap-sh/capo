"""Generated from Smithy shape ``com.amazonaws.ecs#LogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.log_configuration_options_map
    import capo_ecs.types.log_driver
    import capo_ecs.types.secret_list


class LogConfiguration(TypedDict, closed=True):
    log_driver: "capo_ecs.types.log_driver.LogDriver"
    """<p>The log driver to use for the container.</p> <p>For tasks on Fargate, the supported log drivers are <code>awslogs</code>, <code>splunk</code>, and <code>awsfirelens</code>.</p> <p>For tasks hosted on Amazon EC2 instances, the supported log drivers are <code>awslogs</code>, <code>fluentd</code>, <code>gelf</code>, <code>json-file</code>, <code>journald</code>, <code>syslog</code>, <code>splunk</code>, and <code>awsfirelens</code>.</p> <p>For more information about using the <code>awslogs</code> log driver, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html">Send Amazon ECS logs to CloudWatch</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>For more information about using the <code>awsfirelens</code> log driver, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html">Send Amazon ECS logs to an Amazon Web Services service or Amazon Web Services Partner</a>.</p> <note> <p>If you have a custom driver that isn't listed, you can fork the Amazon ECS container agent project that's <a href="https://github.com/aws/amazon-ecs-agent">available on GitHub</a> and customize it to work with that driver. We encourage you to submit pull requests for changes that you would like to have included. However, we don't currently provide support for running modified copies of this software.</p> </note>"""
    options: NotRequired[
        "capo_ecs.types.log_configuration_options_map.LogConfigurationOptionsMap"
    ]
    """<p>The configuration options to send to the log driver.</p> <p>The options you can specify depend on the log driver. Some of the options you can specify when you use the <code>awslogs</code> log driver to route logs to Amazon CloudWatch include the following:</p> <dl> <dt>awslogs-create-group</dt> <dd> <p>Required: No</p> <p>Specify whether you want the log group to be created automatically. If this option isn't specified, it defaults to <code>false</code>.</p> <note> <p>Your IAM policy must include the <code>logs:CreateLogGroup</code> permission before you attempt to use <code>awslogs-create-group</code>.</p> </note> </dd> <dt>awslogs-region</dt> <dd> <p>Required: Yes</p> <p>Specify the Amazon Web Services Region that the <code>awslogs</code> log driver is to send your Docker logs to. You can choose to send all of your logs from clusters in different Regions to a single region in CloudWatch Logs. This is so that they're all visible in one location. Otherwise, you can separate them by Region for more granularity. Make sure that the specified log group exists in the Region that you specify with this option.</p> </dd> <dt>awslogs-group</dt> <dd> <p>Required: Yes</p> <p>Make sure to specify a log group that the <code>awslogs</code> log driver sends its log streams to.</p> </dd> <dt>awslogs-stream-prefix</dt> <dd> <p>Required: Yes, when using Fargate.Optional when using EC2.</p> <p>Use the <code>awslogs-stream-prefix</code> option to associate a log stream with the specified prefix, the container name, and the ID of the Amazon ECS task that the container belongs to. If you specify a prefix with this option, then the log stream takes the format <code>prefix-name/container-name/ecs-task-id</code>.</p> <p>If you don't specify a prefix with this option, then the log stream is named after the container ID that's assigned by the Docker daemon on the container instance. Because it's difficult to trace logs back to the container that sent them with just the Docker container ID (which is only available on the container instance), we recommend that you specify a prefix with this option.</p> <p>For Amazon ECS services, you can use the service name as the prefix. Doing so, you can trace log streams to the service that the container belongs to, the name of the container that sent them, and the ID of the task that the container belongs to.</p> <p>You must specify a stream-prefix for your logs to have your logs appear in the Log pane when using the Amazon ECS console.</p> </dd> <dt>awslogs-datetime-format</dt> <dd> <p>Required: No</p> <p>This option defines a multiline start pattern in Python <code>strftime</code> format. A log message consists of a line that matches the pattern and any following lines that don’t match the pattern. The matched line is the delimiter between log messages.</p> <p>One example of a use case for using this format is for parsing output such as a stack dump, which might otherwise be logged in multiple entries. The correct pattern allows it to be captured in a single entry.</p> <p>For more information, see <a href="https://docs.docker.com/config/containers/logging/awslogs/#awslogs-datetime-format">awslogs-datetime-format</a>.</p> <p>You cannot configure both the <code>awslogs-datetime-format</code> and <code>awslogs-multiline-pattern</code> options.</p> <note> <p>Multiline logging performs regular expression parsing and matching of all log messages. This might have a negative impact on logging performance.</p> </note> </dd> <dt>awslogs-multiline-pattern</dt> <dd> <p>Required: No</p> <p>This option defines a multiline start pattern that uses a regular expression. A log message consists of a line that matches the pattern and any following lines that don’t match the pattern. The matched line is the delimiter between log messages.</p> <p>For more information, see <a href="https://docs.docker.com/config/containers/logging/awslogs/#awslogs-multiline-pattern">awslogs-multiline-pattern</a>.</p> <p>This option is ignored if <code>awslogs-datetime-format</code> is also configured.</p> <p>You cannot configure both the <code>awslogs-datetime-format</code> and <code>awslogs-multiline-pattern</code> options.</p> <note> <p>Multiline logging performs regular expression parsing and matching of all log messages. This might have a negative impact on logging performance.</p> </note> </dd> </dl> <p>The following options apply to all supported log drivers.</p> <dl> <dt>mode</dt> <dd> <p>Required: No</p> <p>Valid values: <code>non-blocking</code> | <code>blocking</code> </p> <p>This option defines the delivery mode of log messages from the container to the log driver specified using <code>logDriver</code>. The delivery mode you choose affects application availability when the flow of logs from container is interrupted.</p> <p>If you use the <code>blocking</code> mode and the flow of logs is interrupted, calls from container code to write to the <code>stdout</code> and <code>stderr</code> streams will block. The logging thread of the application will block as a result. This may cause the application to become unresponsive and lead to container healthcheck failure. </p> <p>If you use the <code>non-blocking</code> mode, the container's logs are instead stored in an in-memory intermediate buffer configured with the <code>max-buffer-size</code> option. This prevents the application from becoming unresponsive when logs cannot be sent. We recommend using this mode if you want to ensure service availability and are okay with some log loss. For more information, see <a href="http://aws.amazon.com/blogs/containers/preventing-log-loss-with-non-blocking-mode-in-the-awslogs-container-log-driver/">Preventing log loss with non-blocking mode in the <code>awslogs</code> container log driver</a>.</p> <p>You can set a default <code>mode</code> for all containers in a specific Amazon Web Services Region by using the <code>defaultLogDriverMode</code> account setting. If you don't specify the <code>mode</code> option or configure the account setting, Amazon ECS will default to the <code>non-blocking</code> mode. For more information about the account setting, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#default-log-driver-mode">Default log driver mode</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>On June 25, 2025, Amazon ECS changed the default log driver mode from <code>blocking</code> to <code>non-blocking</code> to prioritize task availability over logging. To continue using the <code>blocking</code> mode after this change, do one of the following:</p> <ul> <li> <p>Set the <code>mode</code> option in your container definition's <code>logConfiguration</code> as <code>blocking</code>.</p> </li> <li> <p>Set the <code>defaultLogDriverMode</code> account setting to <code>blocking</code>.</p> </li> </ul> </note> </dd> <dt>max-buffer-size</dt> <dd> <p>Required: No</p> <p>Default value: <code>10m</code> </p> <p>When <code>non-blocking</code> mode is used, the <code>max-buffer-size</code> log option controls the size of the buffer that's used for intermediate message storage. Make sure to specify an adequate buffer size based on your application. When the buffer fills up, further logs cannot be stored. Logs that cannot be stored are lost. </p> </dd> </dl> <p>To route logs using the <code>splunk</code> log router, you need to specify a <code>splunk-token</code> and a <code>splunk-url</code>.</p> <p>When you use the <code>awsfirelens</code> log router to route logs to an Amazon Web Services Service or Amazon Web Services Partner Network destination for log storage and analytics, you can set the <code>log-driver-buffer-limit</code> option to limit the number of events that are buffered in memory, before being sent to the log router container. It can help to resolve potential log loss issue because high throughput might result in memory running out for the buffer inside of Docker.</p> <p>Other options you can specify when using <code>awsfirelens</code> to route logs depend on the destination. When you export logs to Amazon Data Firehose, you can specify the Amazon Web Services Region with <code>region</code> and a name for the log stream with <code>delivery_stream</code>.</p> <p>When you export logs to Amazon Kinesis Data Streams, you can specify an Amazon Web Services Region with <code>region</code> and a data stream name with <code>stream</code>.</p> <p> When you export logs to Amazon OpenSearch Service, you can specify options like <code>Name</code>, <code>Host</code> (OpenSearch Service endpoint without protocol), <code>Port</code>, <code>Index</code>, <code>Type</code>, <code>Aws_auth</code>, <code>Aws_region</code>, <code>Suppress_Type_Name</code>, and <code>tls</code>. For more information, see <a href="http://aws.amazon.com/blogs/containers/under-the-hood-firelens-for-amazon-ecs-tasks/">Under the hood: FireLens for Amazon ECS Tasks</a>.</p> <p>When you export logs to Amazon S3, you can specify the bucket using the <code>bucket</code> option. You can also specify <code>region</code>, <code>total_file_size</code>, <code>upload_timeout</code>, and <code>use_put_object</code> as options.</p> <p>This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: <code>sudo docker version --format '{{.Server.APIVersion}}'</code> </p>"""
    secret_options: NotRequired["capo_ecs.types.secret_list.SecretList"]
    """<p>The secrets to pass to the log configuration. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html">Specifying sensitive data</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogConfiguration) -> dict:
    out: dict = {}
    import capo_ecs.types.log_driver

    out["logDriver"] = capo_ecs.types.log_driver.serialize_aws_json_1_1(
        value["log_driver"]
    )
    if "options" in value:
        import capo_ecs.types.log_configuration_options_map

        out["options"] = (
            capo_ecs.types.log_configuration_options_map.serialize_aws_json_1_1(
                value["options"]
            )
        )
    if "secret_options" in value:
        import capo_ecs.types.secret_list

        out["secretOptions"] = capo_ecs.types.secret_list.serialize_aws_json_1_1(
            value["secret_options"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogConfiguration:
    out: LogConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("logDriver") is not None:
        import capo_ecs.types.log_driver

        out["log_driver"] = capo_ecs.types.log_driver.deserialize_aws_json_1_1(
            data["logDriver"]
        )
    else:
        raise DeserializationError("LogConfiguration.log_driver required")
    if data.get("options") is not None:
        import capo_ecs.types.log_configuration_options_map

        out["options"] = (
            capo_ecs.types.log_configuration_options_map.deserialize_aws_json_1_1(
                data["options"]
            )
        )
    if data.get("secretOptions") is not None:
        import capo_ecs.types.secret_list

        out["secret_options"] = capo_ecs.types.secret_list.deserialize_aws_json_1_1(
            data["secretOptions"]
        )
    return out
