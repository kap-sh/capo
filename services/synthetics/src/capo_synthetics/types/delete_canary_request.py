"""Generated from Smithy shape ``com.amazonaws.synthetics#DeleteCanaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.boolean
    import capo_synthetics.types.canary_name


class DeleteCanaryRequest(TypedDict, closed=True):
    name: "capo_synthetics.types.canary_name.CanaryName"
    """<p>The name of the canary that you want to delete. To find the names of your canaries, use <a href="https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html">DescribeCanaries</a>.</p>"""
    delete_lambda: "capo_synthetics.types.boolean.boolean"
    """<p>Specifies whether to also delete the Lambda functions and layers used by this canary. The default is <code>false</code>.</p> <p>Your setting for this parameter is used only if the canary doesn't have <code>AUTOMATIC</code> for its <code>ProvisionedResourceCleanup</code> field. If that field is set to <code>AUTOMATIC</code>, then the Lambda functions and layers will be deleted when this canary is deleted. </p> <p>Type: Boolean</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCanaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCanaryRequest:
    out: DeleteCanaryRequest = {}  # type: ignore[typeddict-item]
    return out
