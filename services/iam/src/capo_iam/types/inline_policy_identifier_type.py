"""Generated from Smithy shape ``com.amazonaws.iam#InlinePolicyIdentifierType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.attachment_name
    import capo_iam.types.attachment_type
    import capo_iam.types.policy_name_type


class InlinePolicyIdentifierType(TypedDict, closed=True):
    policy_name: "capo_iam.types.policy_name_type.policyNameType"
    """<p>The name of the inline policy.</p>"""
    attachment_type: "capo_iam.types.attachment_type.AttachmentType"
    """<p>The type of IAM entity that the inline policy is attached to.</p>"""
    attachment_name: "capo_iam.types.attachment_name.AttachmentName"
    """<p>The name of the IAM user, group, or role that the inline policy is attached to. Wildcard characters are supported to match multiple entities: use at most one <code>*</code> (matches any sequence of characters, including none), and any number of <code>?</code> (each matches exactly one character).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InlinePolicyIdentifierType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}PolicyName", str(value["policy_name"])))
    import capo_iam.types.attachment_type

    capo_iam.types.attachment_type.serialize_query(
        value["attachment_type"], pairs, f"{key_prefix}AttachmentType"
    )
    pairs.append((f"{key_prefix}AttachmentName", str(value["attachment_name"])))


def deserialize_query(el: Element) -> InlinePolicyIdentifierType:
    out: InlinePolicyIdentifierType = {}  # type: ignore[typeddict-item]
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    else:
        out["policy_name"] = ""
    child_attachment_type = el.find("AttachmentType")
    if child_attachment_type is not None:
        import capo_iam.types.attachment_type

        out["attachment_type"] = capo_iam.types.attachment_type.deserialize_query(
            child_attachment_type
        )
    else:
        import typing

        out["attachment_type"] = typing.cast(
            "capo_iam.types.attachment_type.AttachmentType", ""
        )
    child_attachment_name = el.find("AttachmentName")
    if child_attachment_name is not None:
        out["attachment_name"] = str(child_attachment_name.text or "")
    else:
        out["attachment_name"] = ""
    return out
