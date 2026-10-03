"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UpdateAppVersionResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.entity_version
    import capo_resiliencehub.types.physical_resource


class UpdateAppVersionResourceResponse(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: "capo_resiliencehub.types.entity_version.EntityVersion"
    """<p>Resilience Hub application version.</p>"""
    physical_resource: NotRequired[
        "capo_resiliencehub.types.physical_resource.PhysicalResource"
    ]
    """<p>Defines a physical resource. A physical resource is a resource that exists in your account. It can be identified using an Amazon Resource Name (ARN) or a Resilience Hub-native identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppVersionResourceResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["appVersion"] = value["app_version"]
    if "physical_resource" in value:
        import capo_resiliencehub.types.physical_resource

        out["physicalResource"] = (
            capo_resiliencehub.types.physical_resource.serialize_json(
                value["physical_resource"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAppVersionResourceResponse:
    out: UpdateAppVersionResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("UpdateAppVersionResourceResponse.app_arn required")
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError(
            "UpdateAppVersionResourceResponse.app_version required"
        )
    if data.get("physicalResource") is not None:
        import capo_resiliencehub.types.physical_resource

        out["physical_resource"] = (
            capo_resiliencehub.types.physical_resource.deserialize_json(
                data["physicalResource"]
            )
        )
    return out
