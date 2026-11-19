"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListApplicationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.applications_list
    import capo_codedeploy.types.next_token


class ListApplicationsOutput(TypedDict, closed=True):
    applications: NotRequired[
        "capo_codedeploy.types.applications_list.ApplicationsList"
    ]
    """<p>A list of application names.</p>"""
    next_token: NotRequired["capo_codedeploy.types.next_token.NextToken"]
    """<p>If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list applications call to return the next set of applications in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationsOutput) -> dict:
    out: dict = {}
    if "applications" in value:
        import capo_codedeploy.types.applications_list

        out["applications"] = (
            capo_codedeploy.types.applications_list.serialize_aws_json_1_1(
                value["applications"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationsOutput:
    out: ListApplicationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("applications") is not None:
        import capo_codedeploy.types.applications_list

        out["applications"] = (
            capo_codedeploy.types.applications_list.deserialize_aws_json_1_1(
                data["applications"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListApplicationsOutput) -> dict:
    out: dict = {}
    if "applications" in value:
        import capo_codedeploy.types.applications_list

        out["applications"] = capo_codedeploy.types.applications_list.serialize_cbor(
            value["applications"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListApplicationsOutput:
    out: ListApplicationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("applications") is not None:
        import capo_codedeploy.types.applications_list

        out["applications"] = capo_codedeploy.types.applications_list.deserialize_cbor(
            data["applications"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
