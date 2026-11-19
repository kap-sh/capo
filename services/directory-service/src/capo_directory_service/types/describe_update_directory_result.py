"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeUpdateDirectoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.next_token
    import capo_directory_service.types.update_activities


class DescribeUpdateDirectoryResult(TypedDict, closed=True):
    update_activities: NotRequired[
        "capo_directory_service.types.update_activities.UpdateActivities"
    ]
    """<p> The list of update activities on a directory for the requested update type. </p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p> If not null, more results are available. Pass this value for the <code>NextToken</code> parameter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUpdateDirectoryResult) -> dict:
    out: dict = {}
    if "update_activities" in value:
        import capo_directory_service.types.update_activities

        out["UpdateActivities"] = (
            capo_directory_service.types.update_activities.serialize_aws_json_1_1(
                value["update_activities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUpdateDirectoryResult:
    out: DescribeUpdateDirectoryResult = {}  # type: ignore[typeddict-item]
    if data.get("UpdateActivities") is not None:
        import capo_directory_service.types.update_activities

        out["update_activities"] = (
            capo_directory_service.types.update_activities.deserialize_aws_json_1_1(
                data["UpdateActivities"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeUpdateDirectoryResult) -> dict:
    out: dict = {}
    if "update_activities" in value:
        import capo_directory_service.types.update_activities

        out["UpdateActivities"] = (
            capo_directory_service.types.update_activities.serialize_cbor(
                value["update_activities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeUpdateDirectoryResult:
    out: DescribeUpdateDirectoryResult = {}  # type: ignore[typeddict-item]
    if data.get("UpdateActivities") is not None:
        import capo_directory_service.types.update_activities

        out["update_activities"] = (
            capo_directory_service.types.update_activities.deserialize_cbor(
                data["UpdateActivities"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
