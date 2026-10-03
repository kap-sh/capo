"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UpdateAppVersionAppComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.additional_info_map
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.string255


class UpdateAppVersionAppComponentRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    id: "capo_resiliencehub.types.string255.String255"
    """<p>Identifier of the Application Component.</p>"""
    name: NotRequired["capo_resiliencehub.types.string255.String255"]
    """<p>Name of the Application Component.</p>"""
    type: NotRequired["capo_resiliencehub.types.string255.String255"]
    """<p>Type of Application Component. For more information about the types of Application Component, see <a href="https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.grouping.html">Grouping resources in an AppComponent</a>.</p>"""
    additional_info: NotRequired[
        "capo_resiliencehub.types.additional_info_map.AdditionalInfoMap"
    ]
    """<p>Currently, there is no supported additional information for Application Components.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppVersionAppComponentRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "additional_info" in value:
        import capo_resiliencehub.types.additional_info_map

        out["additionalInfo"] = (
            capo_resiliencehub.types.additional_info_map.serialize_json(
                value["additional_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAppVersionAppComponentRequest:
    out: UpdateAppVersionAppComponentRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "UpdateAppVersionAppComponentRequest.app_arn required"
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateAppVersionAppComponentRequest.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("additionalInfo") is not None:
        import capo_resiliencehub.types.additional_info_map

        out["additional_info"] = (
            capo_resiliencehub.types.additional_info_map.deserialize_json(
                data["additionalInfo"]
            )
        )
    return out
