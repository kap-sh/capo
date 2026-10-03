"""Generated from Smithy shape ``com.amazonaws.resiliencehub#PublishAppVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.entity_version


class PublishAppVersionRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    version_name: NotRequired["capo_resiliencehub.types.entity_version.EntityVersion"]
    """<p>Name of the application version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishAppVersionRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    return out


def deserialize_json(data: dict) -> PublishAppVersionRequest:
    out: PublishAppVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("PublishAppVersionRequest.app_arn required")
    if data.get("versionName") is not None:
        out["version_name"] = data["versionName"]
    return out
