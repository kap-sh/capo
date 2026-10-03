"""Generated from Smithy shape ``com.amazonaws.batch#LogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.log_configuration_options_map
    import capo_batch.types.log_driver
    import capo_batch.types.secret_list


class LogConfiguration(TypedDict, closed=True):
    log_driver: NotRequired["capo_batch.types.log_driver.LogDriver"]
    """<p>The log driver to use for the container. The valid values that are listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default.</p> <p>The supported log drivers are <code>awsfirelens</code>, <code>awslogs</code>, <code>fluentd</code>, <code>gelf</code>, <code>json-file</code>, <code>journald</code>, <code>logentries</code>, <code>syslog</code>, and <code>splunk</code>.</p> <note> <p>Jobs that are running on Fargate resources are restricted to the <code>awslogs</code> and <code>splunk</code> log drivers.</p> </note> <dl> <dt>awsfirelens</dt> <dd> <p>Specifies the firelens logging driver. For more information on configuring Firelens, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html">Send Amazon ECS logs to an Amazon Web Services service or Amazon Web Services Partner</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </dd> <dt>awslogs</dt> <dd> <p>Specifies the Amazon CloudWatch Logs logging driver. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/using_awslogs.html">Using the awslogs log driver</a> in the <i>Batch User Guide</i> and <a href="https://docs.docker.com/config/containers/logging/awslogs/">Amazon CloudWatch Logs logging driver</a> in the Docker documentation.</p> </dd> <dt>fluentd</dt> <dd> <p>Specifies the Fluentd logging driver. For more information including usage and options, see <a href="https://docs.docker.com/config/containers/logging/fluentd/">Fluentd logging driver</a> in the <i>Docker documentation</i>.</p> </dd> <dt>gelf</dt> <dd> <p>Specifies the Graylog Extended Format (GELF) logging driver. For more information including usage and options, see <a href="https://docs.docker.com/config/containers/logging/gelf/">Graylog Extended Format logging driver</a> in the <i>Docker documentation</i>.</p> </dd> <dt>journald</dt> <dd> <p>Specifies the journald logging driver. For more information including usage and options, see <a href="https://docs.docker.com/config/containers/logging/journald/">Journald logging driver</a> in the <i>Docker documentation</i>.</p> </dd> <dt>json-file</dt> <dd> <p>Specifies the JSON file logging driver. For more information including usage and options, see <a href="https://docs.docker.com/config/containers/logging/json-file/">JSON File logging driver</a> in the <i>Docker documentation</i>.</p> </dd> <dt>splunk</dt> <dd> <p>Specifies the Splunk logging driver. For more information including usage and options, see <a href="https://docs.docker.com/config/containers/logging/splunk/">Splunk logging driver</a> in the <i>Docker documentation</i>.</p> </dd> <dt>syslog</dt> <dd> <p>Specifies the syslog logging driver. For more information including usage and options, see <a href="https://docs.docker.com/config/containers/logging/syslog/">Syslog logging driver</a> in the <i>Docker documentation</i>.</p> </dd> </dl> <note> <p>If you have a custom driver that's not listed earlier that you want to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that's <a href="https://github.com/aws/amazon-ecs-agent">available on GitHub</a> and customize it to work with that driver. We encourage you to submit pull requests for changes that you want to have included. However, Amazon Web Services doesn't currently support running modified copies of this software.</p> </note> <p>This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: <code>sudo docker version | grep "Server API version"</code> </p>"""
    options: NotRequired[
        "capo_batch.types.log_configuration_options_map.LogConfigurationOptionsMap"
    ]
    """<p>The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: <code>sudo docker version | grep "Server API version"</code> </p>"""
    secret_options: NotRequired["capo_batch.types.secret_list.SecretList"]
    """<p>The secrets to pass to the log configuration. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html">Specifying sensitive data</a> in the <i>Batch User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogConfiguration) -> dict:
    out: dict = {}
    if "log_driver" in value:
        import capo_batch.types.log_driver

        out["logDriver"] = capo_batch.types.log_driver.serialize_json(
            value["log_driver"]
        )
    if "options" in value:
        import capo_batch.types.log_configuration_options_map

        out["options"] = capo_batch.types.log_configuration_options_map.serialize_json(
            value["options"]
        )
    if "secret_options" in value:
        import capo_batch.types.secret_list

        out["secretOptions"] = capo_batch.types.secret_list.serialize_json(
            value["secret_options"]
        )
    return out


def deserialize_json(data: dict) -> LogConfiguration:
    out: LogConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("logDriver") is not None:
        import capo_batch.types.log_driver

        out["log_driver"] = capo_batch.types.log_driver.deserialize_json(
            data["logDriver"]
        )
    if data.get("options") is not None:
        import capo_batch.types.log_configuration_options_map

        out["options"] = (
            capo_batch.types.log_configuration_options_map.deserialize_json(
                data["options"]
            )
        )
    if data.get("secretOptions") is not None:
        import capo_batch.types.secret_list

        out["secret_options"] = capo_batch.types.secret_list.deserialize_json(
            data["secretOptions"]
        )
    return out
