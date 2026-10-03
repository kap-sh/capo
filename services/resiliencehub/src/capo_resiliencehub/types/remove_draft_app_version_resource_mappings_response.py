"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RemoveDraftAppVersionResourceMappingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.entity_version


class RemoveDraftAppVersionResourceMappingsResponse(TypedDict, closed=True):
    app_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: NotRequired["capo_resiliencehub.types.entity_version.EntityVersion"]
    """<p>The version of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveDraftAppVersionResourceMappingsResponse) -> dict:
    out: dict = {}
    if "app_arn" in value:
        out["appArn"] = value["app_arn"]
    if "app_version" in value:
        out["appVersion"] = value["app_version"]
    return out


def deserialize_json(data: dict) -> RemoveDraftAppVersionResourceMappingsResponse:
    out: RemoveDraftAppVersionResourceMappingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    return out
