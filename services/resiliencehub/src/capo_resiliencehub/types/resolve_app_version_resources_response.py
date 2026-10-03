"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResolveAppVersionResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.entity_version
    import capo_resiliencehub.types.resource_resolution_status_type
    import capo_resiliencehub.types.string255


class ResolveAppVersionResourcesResponse(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: "capo_resiliencehub.types.entity_version.EntityVersion"
    """<p>The version of the application.</p>"""
    resolution_id: "capo_resiliencehub.types.string255.String255"
    """<p>The identifier for a specific resolution.</p>"""
    status: "capo_resiliencehub.types.resource_resolution_status_type.ResourceResolutionStatusType"
    """<p>Status of the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResolveAppVersionResourcesResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["appVersion"] = value["app_version"]
    out["resolutionId"] = value["resolution_id"]
    import capo_resiliencehub.types.resource_resolution_status_type

    out["status"] = (
        capo_resiliencehub.types.resource_resolution_status_type.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> ResolveAppVersionResourcesResponse:
    out: ResolveAppVersionResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "ResolveAppVersionResourcesResponse.app_arn required"
        )
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError(
            "ResolveAppVersionResourcesResponse.app_version required"
        )
    if data.get("resolutionId") is not None:
        out["resolution_id"] = data["resolutionId"]
    else:
        raise DeserializationError(
            "ResolveAppVersionResourcesResponse.resolution_id required"
        )
    if data.get("status") is not None:
        import capo_resiliencehub.types.resource_resolution_status_type

        out["status"] = (
            capo_resiliencehub.types.resource_resolution_status_type.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ResolveAppVersionResourcesResponse.status required")
    return out
