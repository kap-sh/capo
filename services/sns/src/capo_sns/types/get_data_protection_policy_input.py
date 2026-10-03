"""Generated from Smithy shape ``com.amazonaws.sns#GetDataProtectionPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.topic_arn


class GetDataProtectionPolicyInput(TypedDict, closed=True):
    resource_arn: "capo_sns.types.topic_arn.topicARN"
    """<p>The ARN of the topic whose <code>DataProtectionPolicy</code> you want to get.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the Amazon Web Services General Reference.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetDataProtectionPolicyInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ResourceArn", str(value["resource_arn"])))


def deserialize_query(el: Element) -> GetDataProtectionPolicyInput:
    out: GetDataProtectionPolicyInput = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    else:
        raise DeserializationError("GetDataProtectionPolicyInput.resource_arn required")
    return out
