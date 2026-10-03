"""Generated from Smithy shape ``com.amazonaws.ecs#FirelensConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.firelens_configuration_options_map
    import capo_ecs.types.firelens_configuration_type


class FirelensConfiguration(TypedDict, closed=True):
    type: "capo_ecs.types.firelens_configuration_type.FirelensConfigurationType"
    """<p>The log router to use. The valid values are <code>fluentd</code> or <code>fluentbit</code>.</p>"""
    options: NotRequired[
        "capo_ecs.types.firelens_configuration_options_map.FirelensConfigurationOptionsMap"
    ]
    """<p>The options to use when configuring the log router. This field is optional and can be used to specify a custom configuration file or to add additional metadata, such as the task, task definition, cluster, and container instance details to the log event. If specified, the syntax to use is <code>"options":{"enable-ecs-log-metadata":"true|false","config-file-type:"s3|file","config-file-value":"arn:aws:s3:::mybucket/fluent.conf|filepath"}</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html#firelens-taskdef">Creating a task definition that uses a FireLens configuration</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>Tasks hosted on Fargate only support the <code>file</code> configuration file type.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirelensConfiguration) -> dict:
    out: dict = {}
    import capo_ecs.types.firelens_configuration_type

    out["type"] = capo_ecs.types.firelens_configuration_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "options" in value:
        import capo_ecs.types.firelens_configuration_options_map

        out["options"] = (
            capo_ecs.types.firelens_configuration_options_map.serialize_aws_json_1_1(
                value["options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FirelensConfiguration:
    out: FirelensConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_ecs.types.firelens_configuration_type

        out["type"] = (
            capo_ecs.types.firelens_configuration_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    else:
        raise DeserializationError("FirelensConfiguration.type required")
    if data.get("options") is not None:
        import capo_ecs.types.firelens_configuration_options_map

        out["options"] = (
            capo_ecs.types.firelens_configuration_options_map.deserialize_aws_json_1_1(
                data["options"]
            )
        )
    return out
