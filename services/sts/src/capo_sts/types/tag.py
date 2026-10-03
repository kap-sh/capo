"""Generated from Smithy shape ``com.amazonaws.sts#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sts._protocol.xml import Element
from capo_sts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sts.types.tag_key_type
    import capo_sts.types.tag_value_type


class Tag(TypedDict, closed=True):
    key: "capo_sts.types.tag_key_type.tagKeyType"
    """<p>The key for a session tag.</p> <p>You can pass up to 50 session tags. The plain text session tag keys can’t exceed 128 characters. For these and additional limits, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length">IAM and STS Character Limits</a> in the <i>IAM User Guide</i>.</p>"""
    value: "capo_sts.types.tag_value_type.tagValueType"
    """<p>The value for a session tag.</p> <p>You can pass up to 50 session tags. The plain text session tag values can’t exceed 256 characters. For these and additional limits, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length">IAM and STS Character Limits</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Tag, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Key", str(value["key"])))
    pairs.append((f"{key_prefix}Value", str(value["value"])))


def deserialize_query(el: Element) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    else:
        raise DeserializationError("Tag.key required")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    else:
        raise DeserializationError("Tag.value required")
    return out
