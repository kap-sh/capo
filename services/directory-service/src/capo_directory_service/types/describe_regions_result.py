"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeRegionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.next_token
    import capo_directory_service.types.regions_description


class DescribeRegionsResult(TypedDict, closed=True):
    regions_description: NotRequired[
        "capo_directory_service.types.regions_description.RegionsDescription"
    ]
    """<p>List of Region information related to the directory for each replicated Region.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>If not null, more results are available. Pass this value for the <code>NextToken</code> parameter in a subsequent call to <a>DescribeRegions</a> to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRegionsResult) -> dict:
    out: dict = {}
    if "regions_description" in value:
        import capo_directory_service.types.regions_description

        out["RegionsDescription"] = (
            capo_directory_service.types.regions_description.serialize_aws_json_1_1(
                value["regions_description"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRegionsResult:
    out: DescribeRegionsResult = {}  # type: ignore[typeddict-item]
    if data.get("RegionsDescription") is not None:
        import capo_directory_service.types.regions_description

        out["regions_description"] = (
            capo_directory_service.types.regions_description.deserialize_aws_json_1_1(
                data["RegionsDescription"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeRegionsResult) -> dict:
    out: dict = {}
    if "regions_description" in value:
        import capo_directory_service.types.regions_description

        out["RegionsDescription"] = (
            capo_directory_service.types.regions_description.serialize_cbor(
                value["regions_description"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeRegionsResult:
    out: DescribeRegionsResult = {}  # type: ignore[typeddict-item]
    if data.get("RegionsDescription") is not None:
        import capo_directory_service.types.regions_description

        out["regions_description"] = (
            capo_directory_service.types.regions_description.deserialize_cbor(
                data["RegionsDescription"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
