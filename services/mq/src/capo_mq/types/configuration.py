"""Generated from Smithy shape ``com.amazonaws.mq#Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__map_of__string
    import capo_mq.types.__string
    import capo_mq.types.__timestamp_iso8601
    import capo_mq.types.authentication_strategy
    import capo_mq.types.configuration_revision
    import capo_mq.types.engine_type


class Configuration(TypedDict, closed=True):
    arn: NotRequired["capo_mq.types.__string.__string"]
    """<p>Required. The ARN of the configuration.</p>"""
    authentication_strategy: NotRequired[
        "capo_mq.types.authentication_strategy.AuthenticationStrategy"
    ]
    """<p>Optional. The authentication strategy associated with the configuration. The default is SIMPLE.</p>"""
    created: NotRequired["capo_mq.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>Required. The date and time of the configuration revision.</p>"""
    description: NotRequired["capo_mq.types.__string.__string"]
    """<p>Required. The description of the configuration.</p>"""
    engine_type: NotRequired["capo_mq.types.engine_type.EngineType"]
    """<p>Required. The type of broker engine. Currently, Amazon MQ supports ACTIVEMQ and RABBITMQ.</p>"""
    engine_version: NotRequired["capo_mq.types.__string.__string"]
    """<p>The broker engine version. Defaults to the latest available version for the specified broker engine type. For a list of supported engine versions, see the <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html">ActiveMQ version management</a> and the <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html">RabbitMQ version management</a> sections in the Amazon MQ Developer Guide.</p>"""
    id: NotRequired["capo_mq.types.__string.__string"]
    """<p>Required. The unique ID that Amazon MQ generates for the configuration.</p>"""
    latest_revision: NotRequired[
        "capo_mq.types.configuration_revision.ConfigurationRevision"
    ]
    """<p>Required. The latest revision of the configuration.</p>"""
    name: NotRequired["capo_mq.types.__string.__string"]
    """<p>Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.</p>"""
    tags: NotRequired["capo_mq.types.__map_of__string.__mapOf__string"]
    """<p>The list of all tags associated with this configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Configuration) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "authentication_strategy" in value:
        import capo_mq.types.authentication_strategy

        out["authenticationStrategy"] = (
            capo_mq.types.authentication_strategy.serialize_json(
                value["authentication_strategy"]
            )
        )
    if "created" in value:
        import capo_mq.types.__timestamp_iso8601

        out["created"] = capo_mq.types.__timestamp_iso8601.serialize_json(
            value["created"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "engine_type" in value:
        import capo_mq.types.engine_type

        out["engineType"] = capo_mq.types.engine_type.serialize_json(
            value["engine_type"]
        )
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "id" in value:
        out["id"] = value["id"]
    if "latest_revision" in value:
        import capo_mq.types.configuration_revision

        out["latestRevision"] = capo_mq.types.configuration_revision.serialize_json(
            value["latest_revision"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import capo_mq.types.__map_of__string

        out["tags"] = capo_mq.types.__map_of__string.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Configuration:
    out: Configuration = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("authenticationStrategy") is not None:
        import capo_mq.types.authentication_strategy

        out["authentication_strategy"] = (
            capo_mq.types.authentication_strategy.deserialize_json(
                data["authenticationStrategy"]
            )
        )
    if data.get("created") is not None:
        import capo_mq.types.__timestamp_iso8601

        out["created"] = capo_mq.types.__timestamp_iso8601.deserialize_json(
            data["created"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("engineType") is not None:
        import capo_mq.types.engine_type

        out["engine_type"] = capo_mq.types.engine_type.deserialize_json(
            data["engineType"]
        )
    if data.get("engineVersion") is not None:
        out["engine_version"] = data["engineVersion"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("latestRevision") is not None:
        import capo_mq.types.configuration_revision

        out["latest_revision"] = capo_mq.types.configuration_revision.deserialize_json(
            data["latestRevision"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("tags") is not None:
        import capo_mq.types.__map_of__string

        out["tags"] = capo_mq.types.__map_of__string.deserialize_json(data["tags"])
    return out
