"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#UpdateApplicationResourceLifecycleMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_beanstalk._protocol.xml import Element
from capo_elastic_beanstalk.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.application_resource_lifecycle_config


class UpdateApplicationResourceLifecycleMessage(TypedDict, closed=True):
    application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName"
    """<p>The name of the application.</p>"""
    resource_lifecycle_config: "capo_elastic_beanstalk.types.application_resource_lifecycle_config.ApplicationResourceLifecycleConfig"
    """<p>The lifecycle configuration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateApplicationResourceLifecycleMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ApplicationName", str(value["application_name"])))
    import capo_elastic_beanstalk.types.application_resource_lifecycle_config

    capo_elastic_beanstalk.types.application_resource_lifecycle_config.serialize_query(
        value["resource_lifecycle_config"],
        pairs,
        f"{key_prefix}ResourceLifecycleConfig",
    )


def deserialize_query(el: Element) -> UpdateApplicationResourceLifecycleMessage:
    out: UpdateApplicationResourceLifecycleMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        out["application_name"] = ""
    child_resource_lifecycle_config = el.find("ResourceLifecycleConfig")
    if child_resource_lifecycle_config is not None:
        import capo_elastic_beanstalk.types.application_resource_lifecycle_config

        out["resource_lifecycle_config"] = (
            capo_elastic_beanstalk.types.application_resource_lifecycle_config.deserialize_query(
                child_resource_lifecycle_config
            )
        )
    else:
        raise DeserializationError(
            "UpdateApplicationResourceLifecycleMessage.resource_lifecycle_config required"
        )
    return out
