"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceAttributeUpdates``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.non_empty_string


class InstanceAttributeUpdates(TypedDict, closed=True):
    bundle_id: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the bundle to update the instance to.</p> <p>Specify one of the following values for the bundle ID:</p> <ul> <li> <p> <b> <code>auto</code> </b> – Updates an instance that runs on a previous-generation bundle to the newer-generation equivalent of that bundle. For example, specify <code>auto</code> to update an instance that runs on <code>small_2_0</code> to <code>small_3_0</code>.</p> </li> <li> <p> <b>Newer-generation bundle ID</b> – Updates an instance that runs on a previous-generation bundle to the specified bundle. For example, specify <code>small_3_0</code> to update an instance that runs on <code>small_2_0</code> to <code>small_3_0</code>.</p> </li> <li> <p> <b>Original bundle ID</b> – Updates an instance to the previous-generation bundle that it ran on before an earlier update. For example, specify <code>small_2_0</code> to return an instance that runs on <code>small_3_0</code> to <code>small_2_0</code>.</p> </li> </ul> <note> <p>The instance must be in the <code>stopped</code> state to update its bundle.</p> <p>There is no additional cost to update an instance to a newer-generation bundle.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceAttributeUpdates) -> dict:
    out: dict = {}
    if "bundle_id" in value:
        out["bundleId"] = value["bundle_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceAttributeUpdates:
    out: InstanceAttributeUpdates = {}  # type: ignore[typeddict-item]
    if data.get("bundleId") is not None:
        out["bundle_id"] = data["bundleId"]
    return out
