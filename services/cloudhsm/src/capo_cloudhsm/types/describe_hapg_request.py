"""Generated from Smithy shape ``com.amazonaws.cloudhsm#DescribeHapgRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm.types.hapg_arn


class DescribeHapgRequest(TypedDict, closed=True):
    hapg_arn: "capo_cloudhsm.types.hapg_arn.HapgArn"
    """<p>The ARN of the high-availability partition group to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHapgRequest) -> dict:
    out: dict = {}
    out["HapgArn"] = value["hapg_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHapgRequest:
    out: DescribeHapgRequest = {}  # type: ignore[typeddict-item]
    if data.get("HapgArn") is not None:
        out["hapg_arn"] = data["HapgArn"]
    else:
        out["hapg_arn"] = ""
    return out
