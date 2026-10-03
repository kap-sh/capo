"""Generated from Smithy shape ``com.amazonaws.sns#PutDataProtectionPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.attribute_value
    import capo_sns.types.topic_arn


class PutDataProtectionPolicyInput(TypedDict, closed=True):
    resource_arn: "capo_sns.types.topic_arn.topicARN"
    """<p>The ARN of the topic whose <code>DataProtectionPolicy</code> you want to add or update.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the Amazon Web Services General Reference.</p>"""
    data_protection_policy: "capo_sns.types.attribute_value.attributeValue"
    """<p>The JSON serialization of the topic's <code>DataProtectionPolicy</code>.</p> <p>The <code>DataProtectionPolicy</code> must be in JSON string format.</p> <p>Length Constraints: Maximum length of 30,720.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PutDataProtectionPolicyInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ResourceArn", str(value["resource_arn"])))
    pairs.append(
        (f"{key_prefix}DataProtectionPolicy", str(value["data_protection_policy"]))
    )


def deserialize_query(el: Element) -> PutDataProtectionPolicyInput:
    out: PutDataProtectionPolicyInput = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    else:
        raise DeserializationError("PutDataProtectionPolicyInput.resource_arn required")
    child_data_protection_policy = el.find("DataProtectionPolicy")
    if child_data_protection_policy is not None:
        out["data_protection_policy"] = str(child_data_protection_policy.text or "")
    else:
        raise DeserializationError(
            "PutDataProtectionPolicyInput.data_protection_policy required"
        )
    return out
