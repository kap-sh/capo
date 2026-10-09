"""Generated from Smithy shape ``com.amazonaws.eks#AckConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.ack_disabled_services_list
    import capo_eks.types.boxed_boolean


class AckConfigResponse(TypedDict, closed=True):
    enable_cross_namespace: NotRequired["capo_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates whether ACK controllers resolve resource references to resources in a different Kubernetes namespace. This value reflects the setting that's in effect, and is <code>false</code> if you never specified a value. Capabilities that were using cross-namespace references before this setting became available have this value set to <code>true</code>, so their behavior is unchanged.</p>"""
    disabled_services: NotRequired[
        "capo_eks.types.ack_disabled_services_list.AckDisabledServicesList"
    ]
    """<p>The list of ACK service names whose controllers are turned off for this capability. Existing custom resource definitions remain installed, and resources of a disabled service aren't reconciled until the service is re-enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AckConfigResponse) -> dict:
    out: dict = {}
    if "enable_cross_namespace" in value:
        out["enableCrossNamespace"] = value["enable_cross_namespace"]
    if "disabled_services" in value:
        import capo_eks.types.ack_disabled_services_list

        out["disabledServices"] = (
            capo_eks.types.ack_disabled_services_list.serialize_json(
                value["disabled_services"]
            )
        )
    return out


def deserialize_json(data: dict) -> AckConfigResponse:
    out: AckConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("enableCrossNamespace") is not None:
        out["enable_cross_namespace"] = data["enableCrossNamespace"]
    if data.get("disabledServices") is not None:
        import capo_eks.types.ack_disabled_services_list

        out["disabled_services"] = (
            capo_eks.types.ack_disabled_services_list.deserialize_json(
                data["disabledServices"]
            )
        )
    return out
