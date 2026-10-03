"""Generated from Smithy shape ``com.amazonaws.batch#FirelensConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.firelens_configuration_options_map
    import capo_batch.types.firelens_configuration_type


class FirelensConfiguration(TypedDict, closed=True):
    type: NotRequired[
        "capo_batch.types.firelens_configuration_type.FirelensConfigurationType"
    ]
    """<p>The log router to use. The valid values are <code>fluentd</code> or <code>fluentbit</code>.</p>"""
    options: NotRequired[
        "capo_batch.types.firelens_configuration_options_map.FirelensConfigurationOptionsMap"
    ]
    """<p>The options to use when configuring the log router. This field is optional and can be used to specify a custom configuration file or to add additional metadata, such as the task, task definition, cluster, and container instance details to the log event. If specified, the syntax to use is <code>"options":{"enable-ecs-log-metadata":"true|false","config-file-type:"s3|file","config-file-value":"arn:aws:s3:::mybucket/fluent.conf|filepath"}</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html#firelens-taskdef">Creating a task definition that uses a FireLens configuration</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirelensConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_batch.types.firelens_configuration_type

        out["type"] = capo_batch.types.firelens_configuration_type.serialize_json(
            value["type"]
        )
    if "options" in value:
        import capo_batch.types.firelens_configuration_options_map

        out["options"] = (
            capo_batch.types.firelens_configuration_options_map.serialize_json(
                value["options"]
            )
        )
    return out


def deserialize_json(data: dict) -> FirelensConfiguration:
    out: FirelensConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_batch.types.firelens_configuration_type

        out["type"] = capo_batch.types.firelens_configuration_type.deserialize_json(
            data["type"]
        )
    if data.get("options") is not None:
        import capo_batch.types.firelens_configuration_options_map

        out["options"] = (
            capo_batch.types.firelens_configuration_options_map.deserialize_json(
                data["options"]
            )
        )
    return out
