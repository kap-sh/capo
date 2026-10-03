"""Generated from Smithy shape ``com.amazonaws.mq#CreateConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__map_of__string
    import capo_mq.types.__string
    import capo_mq.types.authentication_strategy
    import capo_mq.types.engine_type


class CreateConfigurationRequest(TypedDict, closed=True):
    authentication_strategy: NotRequired[
        "capo_mq.types.authentication_strategy.AuthenticationStrategy"
    ]
    """<p>Optional. The authentication strategy associated with the configuration. The default is SIMPLE.</p>"""
    engine_type: NotRequired["capo_mq.types.engine_type.EngineType"]
    """<p>Required. The type of broker engine. Currently, Amazon MQ supports ACTIVEMQ and RABBITMQ.</p>"""
    engine_version: NotRequired["capo_mq.types.__string.__string"]
    """<p>The broker engine version. Defaults to the latest available version for the specified broker engine type. For more information, see the <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html">ActiveMQ version management</a> and the <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html">RabbitMQ version management</a> sections in the Amazon MQ Developer Guide.</p>"""
    name: NotRequired["capo_mq.types.__string.__string"]
    """<p>Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.</p>"""
    tags: NotRequired["capo_mq.types.__map_of__string.__mapOf__string"]
    """<p>Create tags when creating the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationRequest) -> dict:
    out: dict = {}
    if "authentication_strategy" in value:
        import capo_mq.types.authentication_strategy

        out["authenticationStrategy"] = (
            capo_mq.types.authentication_strategy.serialize_json(
                value["authentication_strategy"]
            )
        )
    if "engine_type" in value:
        import capo_mq.types.engine_type

        out["engineType"] = capo_mq.types.engine_type.serialize_json(
            value["engine_type"]
        )
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import capo_mq.types.__map_of__string

        out["tags"] = capo_mq.types.__map_of__string.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConfigurationRequest:
    out: CreateConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("authenticationStrategy") is not None:
        import capo_mq.types.authentication_strategy

        out["authentication_strategy"] = (
            capo_mq.types.authentication_strategy.deserialize_json(
                data["authenticationStrategy"]
            )
        )
    if data.get("engineType") is not None:
        import capo_mq.types.engine_type

        out["engine_type"] = capo_mq.types.engine_type.deserialize_json(
            data["engineType"]
        )
    if data.get("engineVersion") is not None:
        out["engine_version"] = data["engineVersion"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("tags") is not None:
        import capo_mq.types.__map_of__string

        out["tags"] = capo_mq.types.__map_of__string.deserialize_json(data["tags"])
    return out
