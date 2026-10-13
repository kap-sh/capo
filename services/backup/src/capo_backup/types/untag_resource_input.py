"""Generated from Smithy shape ``com.amazonaws.backup#UntagResourceInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_backup.types.arn.ARN"
    """<p>An ARN that uniquely identifies a resource. The format of the ARN depends on the type of the tagged resource.</p> <p>ARNs that do not include <code>backup</code> are incompatible with tagging. <code>TagResource</code> and <code>UntagResource</code> with invalid ARNs will result in an error. Acceptable ARN content can include <code>arn:aws:backup:us-east</code>. Invalid ARN content may look like <code>arn:aws:ec2:us-east</code>.</p>"""
    tag_key_list: "capo_backup.types.tag_key_list.TagKeyList"
    """<p>The keys to identify which key-value tags to remove from a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    import capo_backup.types.tag_key_list

    out["TagKeyList"] = capo_backup.types.tag_key_list.serialize_json(
        value["tag_key_list"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("TagKeyList") is not None:
        import capo_backup.types.tag_key_list

        out["tag_key_list"] = capo_backup.types.tag_key_list.deserialize_json(
            data["TagKeyList"]
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_key_list required")
    return out


def redact_sensitive(value: UntagResourceInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tag_key_list" in value:
        out["tag_key_list"] = "*** Sensitive Data Redacted ***"
    return out
