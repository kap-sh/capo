"""Generated from Smithy shape ``com.amazonaws.sts#PolicyDescriptorType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.arn_type


class PolicyDescriptorType(TypedDict, closed=True):
    arn: NotRequired["capo_sts.types.arn_type.arnType"]
    """<p>The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy for the role. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyDescriptorType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "arn" in value:
        pairs.append((f"{key_prefix}arn", str(value["arn"])))


def deserialize_query(el: Element) -> PolicyDescriptorType:
    out: PolicyDescriptorType = {}  # type: ignore[typeddict-item]
    child_arn = el.find("arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
