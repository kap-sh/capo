"""Generated from Smithy shape ``com.amazonaws.resiliencehub#PublishAppVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.entity_version
    import capo_resiliencehub.types.long_optional


class PublishAppVersionResponse(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: NotRequired["capo_resiliencehub.types.entity_version.EntityVersion"]
    """<p>The version of the application.</p>"""
    identifier: NotRequired["capo_resiliencehub.types.long_optional.LongOptional"]
    """<p>Identifier of the application version.</p>"""
    version_name: NotRequired["capo_resiliencehub.types.entity_version.EntityVersion"]
    """<p>Name of the application version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishAppVersionResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    if "app_version" in value:
        out["appVersion"] = value["app_version"]
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    return out


def deserialize_json(data: dict) -> PublishAppVersionResponse:
    out: PublishAppVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("PublishAppVersionResponse.app_arn required")
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    if data.get("versionName") is not None:
        out["version_name"] = data["versionName"]
    return out
