"""Generated from Smithy shape ``com.amazonaws.gamelift#ListBuildsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.build_status
    import capo_gamelift.types.non_empty_string
    import capo_gamelift.types.positive_integer


class ListBuildsInput(TypedDict, closed=True):
    status: NotRequired["capo_gamelift.types.build_status.BuildStatus"]
    """<p>Build status to filter results by. To retrieve all builds, leave this parameter empty.</p> <p>Possible build statuses include the following:</p> <ul> <li> <p> <b>INITIALIZED</b> -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value. </p> </li> <li> <p> <b>READY</b> -- The game build has been successfully uploaded. You can now create new fleets for this build.</p> </li> <li> <p> <b>FAILED</b> -- The game build upload failed. You cannot create new fleets for this build. </p> </li> </ul>"""
    limit: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBuildsInput) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_gamelift.types.build_status

        out["Status"] = capo_gamelift.types.build_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBuildsInput:
    out: ListBuildsInput = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_gamelift.types.build_status

        out["status"] = capo_gamelift.types.build_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListBuildsInput) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_gamelift.types.build_status

        out["Status"] = capo_gamelift.types.build_status.serialize_cbor(value["status"])
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListBuildsInput:
    out: ListBuildsInput = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_gamelift.types.build_status

        out["status"] = capo_gamelift.types.build_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
