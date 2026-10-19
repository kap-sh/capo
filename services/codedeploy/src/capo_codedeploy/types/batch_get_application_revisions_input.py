"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetApplicationRevisionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.application_name
    import capo_codedeploy.types.revision_location_list


class BatchGetApplicationRevisionsInput(TypedDict, closed=True):
    application_name: "capo_codedeploy.types.application_name.ApplicationName"
    """<p>The name of an CodeDeploy application about which to get revision information.</p>"""
    revisions: "capo_codedeploy.types.revision_location_list.RevisionLocationList"
    """<p>An array of <code>RevisionLocation</code> objects that specify information to get about the application revisions, including type and location. The maximum number of <code>RevisionLocation</code> objects you can specify is 25.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetApplicationRevisionsInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    import capo_codedeploy.types.revision_location_list

    out["revisions"] = (
        capo_codedeploy.types.revision_location_list.serialize_aws_json_1_1(
            value["revisions"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetApplicationRevisionsInput:
    out: BatchGetApplicationRevisionsInput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    else:
        out["application_name"] = ""
    if data.get("revisions") is not None:
        import capo_codedeploy.types.revision_location_list

        out["revisions"] = (
            capo_codedeploy.types.revision_location_list.deserialize_aws_json_1_1(
                data["revisions"]
            )
        )
    else:
        out["revisions"] = []
    return out
