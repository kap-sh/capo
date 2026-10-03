"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DeleteAppVersionAppComponentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_component
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.entity_version


class DeleteAppVersionAppComponentResponse(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: "capo_resiliencehub.types.entity_version.EntityVersion"
    """<p>Resilience Hub application version.</p>"""
    app_component: NotRequired["capo_resiliencehub.types.app_component.AppComponent"]
    """<p>List of Application Components that belong to this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppVersionAppComponentResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["appVersion"] = value["app_version"]
    if "app_component" in value:
        import capo_resiliencehub.types.app_component

        out["appComponent"] = capo_resiliencehub.types.app_component.serialize_json(
            value["app_component"]
        )
    return out


def deserialize_json(data: dict) -> DeleteAppVersionAppComponentResponse:
    out: DeleteAppVersionAppComponentResponse = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "DeleteAppVersionAppComponentResponse.app_arn required"
        )
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError(
            "DeleteAppVersionAppComponentResponse.app_version required"
        )
    if data.get("appComponent") is not None:
        import capo_resiliencehub.types.app_component

        out["app_component"] = capo_resiliencehub.types.app_component.deserialize_json(
            data["appComponent"]
        )
    return out
