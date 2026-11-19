"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetApplicationRevisionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.application_name
    import capo_codedeploy.types.generic_revision_info
    import capo_codedeploy.types.revision_location


class GetApplicationRevisionOutput(TypedDict, closed=True):
    application_name: NotRequired[
        "capo_codedeploy.types.application_name.ApplicationName"
    ]
    """<p>The name of the application that corresponds to the revision.</p>"""
    revision: NotRequired["capo_codedeploy.types.revision_location.RevisionLocation"]
    """<p>Additional information about the revision, including type and location.</p>"""
    revision_info: NotRequired[
        "capo_codedeploy.types.generic_revision_info.GenericRevisionInfo"
    ]
    """<p>General information about the revision.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApplicationRevisionOutput) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "revision" in value:
        import capo_codedeploy.types.revision_location

        out["revision"] = (
            capo_codedeploy.types.revision_location.serialize_aws_json_1_1(
                value["revision"]
            )
        )
    if "revision_info" in value:
        import capo_codedeploy.types.generic_revision_info

        out["revisionInfo"] = (
            capo_codedeploy.types.generic_revision_info.serialize_aws_json_1_1(
                value["revision_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApplicationRevisionOutput:
    out: GetApplicationRevisionOutput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    if data.get("revision") is not None:
        import capo_codedeploy.types.revision_location

        out["revision"] = (
            capo_codedeploy.types.revision_location.deserialize_aws_json_1_1(
                data["revision"]
            )
        )
    if data.get("revisionInfo") is not None:
        import capo_codedeploy.types.generic_revision_info

        out["revision_info"] = (
            capo_codedeploy.types.generic_revision_info.deserialize_aws_json_1_1(
                data["revisionInfo"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetApplicationRevisionOutput) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "revision" in value:
        import capo_codedeploy.types.revision_location

        out["revision"] = capo_codedeploy.types.revision_location.serialize_cbor(
            value["revision"]
        )
    if "revision_info" in value:
        import capo_codedeploy.types.generic_revision_info

        out["revisionInfo"] = (
            capo_codedeploy.types.generic_revision_info.serialize_cbor(
                value["revision_info"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetApplicationRevisionOutput:
    out: GetApplicationRevisionOutput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    if data.get("revision") is not None:
        import capo_codedeploy.types.revision_location

        out["revision"] = capo_codedeploy.types.revision_location.deserialize_cbor(
            data["revision"]
        )
    if data.get("revisionInfo") is not None:
        import capo_codedeploy.types.generic_revision_info

        out["revision_info"] = (
            capo_codedeploy.types.generic_revision_info.deserialize_cbor(
                data["revisionInfo"]
            )
        )
    return out
