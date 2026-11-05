"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DefaultAmi``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.ami_architecture
    import capo_elastic_beanstalk.types.image_id


class DefaultAmi(TypedDict, closed=True):
    architecture: NotRequired[
        "capo_elastic_beanstalk.types.ami_architecture.AmiArchitecture"
    ]
    """<p>The processor architecture of the AMI.</p>"""
    image_id: NotRequired["capo_elastic_beanstalk.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DefaultAmi, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "architecture" in value:
        import capo_elastic_beanstalk.types.ami_architecture

        capo_elastic_beanstalk.types.ami_architecture.serialize_query(
            value["architecture"], pairs, f"{key_prefix}Architecture"
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))


def deserialize_query(el: Element) -> DefaultAmi:
    out: DefaultAmi = {}  # type: ignore[typeddict-item]
    child_architecture = el.find("Architecture")
    if child_architecture is not None:
        import capo_elastic_beanstalk.types.ami_architecture

        out["architecture"] = (
            capo_elastic_beanstalk.types.ami_architecture.deserialize_query(
                child_architecture
            )
        )
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    return out
