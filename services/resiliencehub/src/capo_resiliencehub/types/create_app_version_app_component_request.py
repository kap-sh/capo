"""Generated from Smithy shape ``com.amazonaws.resiliencehub#CreateAppVersionAppComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.additional_info_map
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.client_token
    import capo_resiliencehub.types.string255


class CreateAppVersionAppComponentRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    id: NotRequired["capo_resiliencehub.types.string255.String255"]
    """<p>Identifier of the Application Component.</p>"""
    name: "capo_resiliencehub.types.string255.String255"
    """<p>Name of the Application Component.</p>"""
    type: "capo_resiliencehub.types.string255.String255"
    """<p>Type of Application Component. For more information about the types of Application Component, see <a href="https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.grouping.html">Grouping resources in an AppComponent</a>.</p>"""
    additional_info: NotRequired[
        "capo_resiliencehub.types.additional_info_map.AdditionalInfoMap"
    ]
    """<p>Currently, there is no supported additional information for Application Components.</p>"""
    client_token: NotRequired["capo_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppVersionAppComponentRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    if "id" in value:
        out["id"] = value["id"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    if "additional_info" in value:
        import capo_resiliencehub.types.additional_info_map

        out["additionalInfo"] = (
            capo_resiliencehub.types.additional_info_map.serialize_json(
                value["additional_info"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAppVersionAppComponentRequest:
    out: CreateAppVersionAppComponentRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "CreateAppVersionAppComponentRequest.app_arn required"
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAppVersionAppComponentRequest.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateAppVersionAppComponentRequest.type required")
    if data.get("additionalInfo") is not None:
        import capo_resiliencehub.types.additional_info_map

        out["additional_info"] = (
            capo_resiliencehub.types.additional_info_map.deserialize_json(
                data["additionalInfo"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
