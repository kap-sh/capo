"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListApplicationRevisionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.next_token
    import capo_codedeploy.types.revision_location_list


class ListApplicationRevisionsOutput(TypedDict, closed=True):
    revisions: NotRequired[
        "capo_codedeploy.types.revision_location_list.RevisionLocationList"
    ]
    """<p>A list of locations that contain the matching revisions.</p>"""
    next_token: NotRequired["capo_codedeploy.types.next_token.NextToken"]
    """<p>If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list application revisions call to return the next set of application revisions in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationRevisionsOutput) -> dict:
    out: dict = {}
    if "revisions" in value:
        import capo_codedeploy.types.revision_location_list

        out["revisions"] = (
            capo_codedeploy.types.revision_location_list.serialize_aws_json_1_1(
                value["revisions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationRevisionsOutput:
    out: ListApplicationRevisionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("revisions") is not None:
        import capo_codedeploy.types.revision_location_list

        out["revisions"] = (
            capo_codedeploy.types.revision_location_list.deserialize_aws_json_1_1(
                data["revisions"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListApplicationRevisionsOutput) -> dict:
    out: dict = {}
    if "revisions" in value:
        import capo_codedeploy.types.revision_location_list

        out["revisions"] = capo_codedeploy.types.revision_location_list.serialize_cbor(
            value["revisions"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListApplicationRevisionsOutput:
    out: ListApplicationRevisionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("revisions") is not None:
        import capo_codedeploy.types.revision_location_list

        out["revisions"] = (
            capo_codedeploy.types.revision_location_list.deserialize_cbor(
                data["revisions"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
