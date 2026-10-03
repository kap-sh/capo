"""Generated from Smithy shape ``com.amazonaws.ec2#PerformanceFactorReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class PerformanceFactorReference(TypedDict, closed=True):
    instance_family: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance family to use as a baseline reference.</p> <note> <p>Ensure that you specify the correct value for the instance family. The instance family is everything before the period (<code>.</code>) in the instance type name. For example, in the instance type <code>c6i.large</code>, the instance family is <code>c6i</code>, not <code>c6</code>. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html">Amazon EC2 instance type naming conventions</a> in <i>Amazon EC2 Instance Types</i>.</p> </note> <p>The following instance families are <i>not supported</i> for performance protection:</p> <ul> <li> <p> <code>c1</code> </p> </li> <li> <p> <code>g3</code> | <code>g3s</code> </p> </li> <li> <p> <code>hpc7g</code> </p> </li> <li> <p> <code>m1</code> | <code>m2</code> </p> </li> <li> <p> <code>mac1</code> | <code>mac2</code> | <code>mac2-m1ultra</code> | <code>mac2-m2</code> | <code>mac2-m2pro</code> </p> </li> <li> <p> <code>p3dn</code> | <code>p4d</code> | <code>p5</code> </p> </li> <li> <p> <code>t1</code> </p> </li> <li> <p> <code>u-12tb1</code> | <code>u-18tb1</code> | <code>u-24tb1</code> | <code>u-3tb1</code> | <code>u-6tb1</code> | <code>u-9tb1</code> | <code>u7i-12tb</code> | <code>u7in-16tb</code> | <code>u7in-24tb</code> | <code>u7in-32tb</code> </p> </li> </ul> <p>If you enable performance protection by specifying a supported instance family, the returned instance types will exclude the above unsupported instance families.</p> <p>If you specify an unsupported instance family as a value for baseline performance, the API returns an empty response for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements">GetInstanceTypesFromInstanceRequirements</a> and an exception for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet">CreateFleet</a>, <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet">RequestSpotFleet</a>, <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFleet">ModifyFleet</a>, and <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySpotFleetRequest">ModifySpotFleetRequest</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PerformanceFactorReference, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_family" in value:
        pairs.append((f"{key_prefix}InstanceFamily", str(value["instance_family"])))


def deserialize_ec2_query(el: Element) -> PerformanceFactorReference:
    out: PerformanceFactorReference = {}  # type: ignore[typeddict-item]
    child_instance_family = el.find("instanceFamily")
    if child_instance_family is not None:
        out["instance_family"] = str(child_instance_family.text or "")
    return out
