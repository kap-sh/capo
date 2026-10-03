"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppVersionAppComponentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_component_list
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.entity_version
    import capo_resiliencehub.types.next_token


class ListAppVersionAppComponentsResponse(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: "capo_resiliencehub.types.entity_version.EntityVersion"
    """<p>Resilience Hub application version.</p>"""
    app_components: NotRequired[
        "capo_resiliencehub.types.app_component_list.AppComponentList"
    ]
    """<p>Defines an Application Component.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppVersionAppComponentsResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["appVersion"] = value["app_version"]
    if "app_components" in value:
        import capo_resiliencehub.types.app_component_list

        out["appComponents"] = (
            capo_resiliencehub.types.app_component_list.serialize_json(
                value["app_components"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppVersionAppComponentsResponse:
    out: ListAppVersionAppComponentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "ListAppVersionAppComponentsResponse.app_arn required"
        )
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError(
            "ListAppVersionAppComponentsResponse.app_version required"
        )
    if data.get("appComponents") is not None:
        import capo_resiliencehub.types.app_component_list

        out["app_components"] = (
            capo_resiliencehub.types.app_component_list.deserialize_json(
                data["appComponents"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
