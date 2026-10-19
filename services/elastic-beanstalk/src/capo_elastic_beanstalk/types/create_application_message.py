"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#CreateApplicationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.application_resource_lifecycle_config
    import capo_elastic_beanstalk.types.description
    import capo_elastic_beanstalk.types.tags


class CreateApplicationMessage(TypedDict, closed=True):
    application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName"
    """<p>The name of the application. Must be unique within your account.</p>"""
    description: NotRequired["capo_elastic_beanstalk.types.description.Description"]
    """<p>Your description of the application.</p>"""
    resource_lifecycle_config: NotRequired[
        "capo_elastic_beanstalk.types.application_resource_lifecycle_config.ApplicationResourceLifecycleConfig"
    ]
    """<p>Specifies an application resource lifecycle configuration to prevent your application from accumulating too many versions.</p>"""
    tags: NotRequired["capo_elastic_beanstalk.types.tags.Tags"]
    """<p>Specifies the tags applied to the application.</p> <p>Elastic Beanstalk applies these tags only to the application. Environments that you create in the application don't inherit the tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateApplicationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ApplicationName", str(value["application_name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "resource_lifecycle_config" in value:
        import capo_elastic_beanstalk.types.application_resource_lifecycle_config

        capo_elastic_beanstalk.types.application_resource_lifecycle_config.serialize_query(
            value["resource_lifecycle_config"],
            pairs,
            f"{key_prefix}ResourceLifecycleConfig",
        )
    if "tags" in value:
        import capo_elastic_beanstalk.types.tags

        capo_elastic_beanstalk.types.tags.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateApplicationMessage:
    out: CreateApplicationMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        out["application_name"] = ""
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_resource_lifecycle_config = el.find("ResourceLifecycleConfig")
    if child_resource_lifecycle_config is not None:
        import capo_elastic_beanstalk.types.application_resource_lifecycle_config

        out["resource_lifecycle_config"] = (
            capo_elastic_beanstalk.types.application_resource_lifecycle_config.deserialize_query(
                child_resource_lifecycle_config
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elastic_beanstalk.types.tags

        out["tags"] = capo_elastic_beanstalk.types.tags.deserialize_query(child_tags)
    return out
