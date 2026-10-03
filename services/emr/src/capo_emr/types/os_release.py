"""Generated from Smithy shape ``com.amazonaws.emr#OSRelease``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.string


class OSRelease(TypedDict, closed=True):
    label: NotRequired["capo_emr.types.string.String"]
    """<p>The Amazon Linux release specified for a cluster in the RunJobFlow request. The format is as shown in <a href="https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-20220218.html"> <i>Amazon Linux 2 Release Notes</i> </a>. For example, 2.0.20220218.1.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OSRelease) -> dict:
    out: dict = {}
    if "label" in value:
        out["Label"] = value["label"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OSRelease:
    out: OSRelease = {}  # type: ignore[typeddict-item]
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    return out
