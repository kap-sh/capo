"""Generated from Smithy shape ``com.amazonaws.m2#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.arn
    import capo_m2.types.identifier
    import capo_m2.types.version


class CreateApplicationResponse(TypedDict, closed=True):
    application_arn: "capo_m2.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    application_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique application identifier.</p>"""
    application_version: "capo_m2.types.version.Version"
    """<p>The version number of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    out["applicationArn"] = value["application_arn"]
    out["applicationId"] = value["application_id"]
    out["applicationVersion"] = value["application_version"]
    return out


def deserialize_json(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("applicationArn") is not None:
        out["application_arn"] = data["applicationArn"]
    else:
        out["application_arn"] = ""
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        out["application_id"] = ""
    if data.get("applicationVersion") is not None:
        out["application_version"] = data["applicationVersion"]
    else:
        out["application_version"] = 0
    return out
