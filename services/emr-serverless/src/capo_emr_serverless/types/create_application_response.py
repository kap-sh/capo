"""Generated from Smithy shape ``com.amazonaws.emrserverless#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_arn
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.application_name


class CreateApplicationResponse(TypedDict, closed=True):
    application_id: "capo_emr_serverless.types.application_id.ApplicationId"
    """<p>The output contains the application ID.</p>"""
    name: NotRequired["capo_emr_serverless.types.application_name.ApplicationName"]
    """<p>The output contains the name of the application.</p>"""
    arn: "capo_emr_serverless.types.application_arn.ApplicationArn"
    """<p>The output contains the ARN of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    if "name" in value:
        out["name"] = value["name"]
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        out["application_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
