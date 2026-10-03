"""Generated from Smithy shape ``com.amazonaws.autoscaling#PerformanceFactorReferenceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.string


class PerformanceFactorReferenceRequest(TypedDict, closed=True):
    instance_family: NotRequired["capo_auto_scaling.types.string.String"]
    """<p> The instance family to use as a baseline reference. </p> <note> <p>Make sure that you specify the correct value for the instance family. The instance family is everything before the period (.) in the instance type name. For example, in the instance <code>c6i.large</code>, the instance family is <code>c6i</code>, not <code>c6</code>. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html">Amazon EC2 instance type naming conventions</a> in <i>Amazon EC2 Instance Types</i>.</p> </note> <p>The following instance types are <i>not supported</i> for performance protection.</p> <ul> <li> <p> <code>c1</code> </p> </li> <li> <p> <code>g3| g3s</code> </p> </li> <li> <p> <code>hpc7g</code> </p> </li> <li> <p> <code>m1| m2</code> </p> </li> <li> <p> <code>mac1 | mac2 | mac2-m1ultra | mac2-m2 | mac2-m2pro</code> </p> </li> <li> <p> <code>p3dn | p4d | p5</code> </p> </li> <li> <p> <code>t1</code> </p> </li> <li> <p> <code>u-12tb1 | u-18tb1 | u-24tb1 | u-3tb1 | u-6tb1 | u-9tb1 | u7i-12tb | u7in-16tb | u7in-24tb | u7in-32tb</code> </p> </li> </ul> <p>If you performance protection by specifying a supported instance family, the returned instance types will exclude the preceding unsupported instance families.</p> <p>If you specify an unsupported instance family as a value for baseline performance, the API returns an empty response.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PerformanceFactorReferenceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_family" in value:
        pairs.append((f"{key_prefix}InstanceFamily", str(value["instance_family"])))


def deserialize_query(el: Element) -> PerformanceFactorReferenceRequest:
    out: PerformanceFactorReferenceRequest = {}  # type: ignore[typeddict-item]
    child_instance_family = el.find("InstanceFamily")
    if child_instance_family is not None:
        out["instance_family"] = str(child_instance_family.text or "")
    return out
