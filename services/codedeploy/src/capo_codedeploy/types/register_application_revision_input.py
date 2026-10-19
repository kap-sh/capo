"""Generated from Smithy shape ``com.amazonaws.codedeploy#RegisterApplicationRevisionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codedeploy.types.application_name
    import capo_codedeploy.types.description
    import capo_codedeploy.types.revision_location


class RegisterApplicationRevisionInput(TypedDict, closed=True):
    application_name: "capo_codedeploy.types.application_name.ApplicationName"
    """<p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>"""
    description: NotRequired["capo_codedeploy.types.description.Description"]
    """<p>A comment about the revision.</p>"""
    revision: "capo_codedeploy.types.revision_location.RevisionLocation"
    """<p>Information about the application revision to register, including type and location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterApplicationRevisionInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_codedeploy.types.revision_location

    out["revision"] = capo_codedeploy.types.revision_location.serialize_aws_json_1_1(
        value["revision"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterApplicationRevisionInput:
    out: RegisterApplicationRevisionInput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    else:
        out["application_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("revision") is not None:
        import capo_codedeploy.types.revision_location

        out["revision"] = (
            capo_codedeploy.types.revision_location.deserialize_aws_json_1_1(
                data["revision"]
            )
        )
    else:
        raise DeserializationError("RegisterApplicationRevisionInput.revision required")
    return out
