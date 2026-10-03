"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DescribeComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_version_arn


class DescribeComponentRequest(TypedDict, closed=True):
    arn: "capo_greengrassv2.types.component_version_arn.ComponentVersionARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the component version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeComponentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeComponentRequest:
    out: DescribeComponentRequest = {}  # type: ignore[typeddict-item]
    return out
