"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeVolumesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.next_token
    import capo_fsx.types.volumes


class DescribeVolumesResponse(TypedDict, closed=True):
    volumes: NotRequired["capo_fsx.types.volumes.Volumes"]
    """<p>Returned after a successful <code>DescribeVolumes</code> operation, describing each volume.</p>"""
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeVolumesResponse) -> dict:
    out: dict = {}
    if "volumes" in value:
        import capo_fsx.types.volumes

        out["Volumes"] = capo_fsx.types.volumes.serialize_aws_json_1_1(value["volumes"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeVolumesResponse:
    out: DescribeVolumesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Volumes") is not None:
        import capo_fsx.types.volumes

        out["volumes"] = capo_fsx.types.volumes.deserialize_aws_json_1_1(
            data["Volumes"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeVolumesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "volumes" in value:
        import capo_fsx.types.volumes

        out["volumes"] = capo_fsx.types.volumes.redact_sensitive(value["volumes"])
    return out
