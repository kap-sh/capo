"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceDrift``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.difference_type
    import capo_resiliencehub.types.entity_id
    import capo_resiliencehub.types.entity_version
    import capo_resiliencehub.types.resource_identifier


class ResourceDrift(TypedDict, closed=True):
    app_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the application whose resources have drifted. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: NotRequired["capo_resiliencehub.types.entity_version.EntityVersion"]
    """<p>Version of the application whose resources have drifted.</p>"""
    reference_id: NotRequired["capo_resiliencehub.types.entity_id.EntityId"]
    """<p>Reference identifier of the resource drift.</p>"""
    resource_identifier: NotRequired[
        "capo_resiliencehub.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>Identifier of the drifted resource.</p>"""
    diff_type: NotRequired["capo_resiliencehub.types.difference_type.DifferenceType"]
    """<p>Indicates if the resource was added or removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDrift) -> dict:
    out: dict = {}
    if "app_arn" in value:
        out["appArn"] = value["app_arn"]
    if "app_version" in value:
        out["appVersion"] = value["app_version"]
    if "reference_id" in value:
        out["referenceId"] = value["reference_id"]
    if "resource_identifier" in value:
        import capo_resiliencehub.types.resource_identifier

        out["resourceIdentifier"] = (
            capo_resiliencehub.types.resource_identifier.serialize_json(
                value["resource_identifier"]
            )
        )
    if "diff_type" in value:
        import capo_resiliencehub.types.difference_type

        out["diffType"] = capo_resiliencehub.types.difference_type.serialize_json(
            value["diff_type"]
        )
    return out


def deserialize_json(data: dict) -> ResourceDrift:
    out: ResourceDrift = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    if data.get("referenceId") is not None:
        out["reference_id"] = data["referenceId"]
    if data.get("resourceIdentifier") is not None:
        import capo_resiliencehub.types.resource_identifier

        out["resource_identifier"] = (
            capo_resiliencehub.types.resource_identifier.deserialize_json(
                data["resourceIdentifier"]
            )
        )
    if data.get("diffType") is not None:
        import capo_resiliencehub.types.difference_type

        out["diff_type"] = capo_resiliencehub.types.difference_type.deserialize_json(
            data["diffType"]
        )
    return out
