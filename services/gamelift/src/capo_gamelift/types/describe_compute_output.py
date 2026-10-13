"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeComputeOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.compute


class DescribeComputeOutput(TypedDict, closed=True):
    compute: NotRequired["capo_gamelift.types.compute.Compute"]
    """<p>The set of properties for the requested compute resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeComputeOutput) -> dict:
    out: dict = {}
    if "compute" in value:
        import capo_gamelift.types.compute

        out["Compute"] = capo_gamelift.types.compute.serialize_aws_json_1_1(
            value["compute"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeComputeOutput:
    out: DescribeComputeOutput = {}  # type: ignore[typeddict-item]
    if data.get("Compute") is not None:
        import capo_gamelift.types.compute

        out["compute"] = capo_gamelift.types.compute.deserialize_aws_json_1_1(
            data["Compute"]
        )
    return out


def redact_sensitive(value: DescribeComputeOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "compute" in value:
        import capo_gamelift.types.compute

        out["compute"] = capo_gamelift.types.compute.redact_sensitive(value["compute"])
    return out
