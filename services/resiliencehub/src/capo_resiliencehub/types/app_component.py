"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.additional_info_map
    import capo_resiliencehub.types.entity_name255
    import capo_resiliencehub.types.string255


class AppComponent(TypedDict, closed=True):
    name: "capo_resiliencehub.types.entity_name255.EntityName255"
    """<p>Name of the Application Component.</p>"""
    type: "capo_resiliencehub.types.string255.String255"
    """<p>The type of Application Component.</p>"""
    id: NotRequired["capo_resiliencehub.types.entity_name255.EntityName255"]
    """<p>Identifier of the Application Component.</p>"""
    additional_info: NotRequired[
        "capo_resiliencehub.types.additional_info_map.AdditionalInfoMap"
    ]
    """<p>Additional configuration parameters for an Resilience Hub application. If you want to implement <code>additionalInfo</code> through the Resilience Hub console rather than using an API call, see <a href="https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html">Configure the application configuration parameters</a>.</p> <note> <p>Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.</p> <p>Key: <code>"failover-regions"</code> </p> <p>Value: <code>"[{"region":"&lt;REGION&gt;", "accounts":[{"id":"&lt;ACCOUNT_ID&gt;"}]}]"</code> </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppComponent) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "additional_info" in value:
        import capo_resiliencehub.types.additional_info_map

        out["additionalInfo"] = (
            capo_resiliencehub.types.additional_info_map.serialize_json(
                value["additional_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> AppComponent:
    out: AppComponent = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AppComponent.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AppComponent.type required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("additionalInfo") is not None:
        import capo_resiliencehub.types.additional_info_map

        out["additional_info"] = (
            capo_resiliencehub.types.additional_info_map.deserialize_json(
                data["additionalInfo"]
            )
        )
    return out
