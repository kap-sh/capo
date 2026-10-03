"""Generated from Smithy shape ``com.amazonaws.iam#TagInstanceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.instance_profile_name_type
    import capo_iam.types.tag_list_type


class TagInstanceProfileRequest(TypedDict, closed=True):
    instance_profile_name: (
        "capo_iam.types.instance_profile_name_type.instanceProfileNameType"
    )
    """<p>The name of the IAM instance profile to which you want to add tags.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tags: "capo_iam.types.tag_list_type.tagListType"
    """<p>The list of tags that you want to attach to the IAM instance profile. Each tag consists of a key name and an associated value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagInstanceProfileRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}InstanceProfileName", str(value["instance_profile_name"]))
    )
    import capo_iam.types.tag_list_type

    capo_iam.types.tag_list_type.serialize_query(
        value["tags"], pairs, f"{key_prefix}Tags"
    )


def deserialize_query(el: Element) -> TagInstanceProfileRequest:
    out: TagInstanceProfileRequest = {}  # type: ignore[typeddict-item]
    child_instance_profile_name = el.find("InstanceProfileName")
    if child_instance_profile_name is not None:
        out["instance_profile_name"] = str(child_instance_profile_name.text or "")
    else:
        raise DeserializationError(
            "TagInstanceProfileRequest.instance_profile_name required"
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_iam.types.tag_list_type

        out["tags"] = capo_iam.types.tag_list_type.deserialize_query(child_tags)
    else:
        raise DeserializationError("TagInstanceProfileRequest.tags required")
    return out
