"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetApplicationRevisionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.application_name
    import capo_codedeploy.types.error_message
    import capo_codedeploy.types.revision_info_list


class BatchGetApplicationRevisionsOutput(TypedDict, closed=True):
    application_name: NotRequired[
        "capo_codedeploy.types.application_name.ApplicationName"
    ]
    """<p>The name of the application that corresponds to the revisions.</p>"""
    error_message: NotRequired["capo_codedeploy.types.error_message.ErrorMessage"]
    """<p>Information about errors that might have occurred during the API call.</p>"""
    revisions: NotRequired["capo_codedeploy.types.revision_info_list.RevisionInfoList"]
    """<p>Additional information about the revisions, including the type and location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetApplicationRevisionsOutput) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "revisions" in value:
        import capo_codedeploy.types.revision_info_list

        out["revisions"] = (
            capo_codedeploy.types.revision_info_list.serialize_aws_json_1_1(
                value["revisions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetApplicationRevisionsOutput:
    out: BatchGetApplicationRevisionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("revisions") is not None:
        import capo_codedeploy.types.revision_info_list

        out["revisions"] = (
            capo_codedeploy.types.revision_info_list.deserialize_aws_json_1_1(
                data["revisions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchGetApplicationRevisionsOutput) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "revisions" in value:
        import capo_codedeploy.types.revision_info_list

        out["revisions"] = capo_codedeploy.types.revision_info_list.serialize_cbor(
            value["revisions"]
        )
    return out


def deserialize_cbor(data: dict) -> BatchGetApplicationRevisionsOutput:
    out: BatchGetApplicationRevisionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("revisions") is not None:
        import capo_codedeploy.types.revision_info_list

        out["revisions"] = capo_codedeploy.types.revision_info_list.deserialize_cbor(
            data["revisions"]
        )
    return out
