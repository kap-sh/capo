"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ImageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.image_build_configuration
    import capo_elastic_beanstalk.types.image_source


class ImageConfiguration(TypedDict, closed=True):
    source: NotRequired["capo_elastic_beanstalk.types.image_source.ImageSource"]
    """<p>The location of a container image that you built and pushed to a container registry yourself. Elastic Beanstalk deploys the image without a build step.</p> <p>If you specify <code>Source</code>, don't specify <code>Build</code> or the request's <code>SourceBundle</code> parameter.</p>"""
    build: NotRequired[
        "capo_elastic_beanstalk.types.image_build_configuration.ImageBuildConfiguration"
    ]
    """<p>Settings that Elastic Beanstalk uses to build a container image from the source bundle of the application version.</p> <p>If you specify <code>Build</code>, also specify the request's <code>SourceBundle</code> parameter, and don't specify <code>Source</code>.</p> <p>To build the image when you create the application version instead of on first deployment, also set <code>Process</code> to <code>true</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ImageConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source" in value:
        import capo_elastic_beanstalk.types.image_source

        capo_elastic_beanstalk.types.image_source.serialize_query(
            value["source"], pairs, f"{key_prefix}Source"
        )
    if "build" in value:
        import capo_elastic_beanstalk.types.image_build_configuration

        capo_elastic_beanstalk.types.image_build_configuration.serialize_query(
            value["build"], pairs, f"{key_prefix}Build"
        )


def deserialize_query(el: Element) -> ImageConfiguration:
    out: ImageConfiguration = {}  # type: ignore[typeddict-item]
    child_source = el.find("Source")
    if child_source is not None:
        import capo_elastic_beanstalk.types.image_source

        out["source"] = capo_elastic_beanstalk.types.image_source.deserialize_query(
            child_source
        )
    child_build = el.find("Build")
    if child_build is not None:
        import capo_elastic_beanstalk.types.image_build_configuration

        out["build"] = (
            capo_elastic_beanstalk.types.image_build_configuration.deserialize_query(
                child_build
            )
        )
    return out
