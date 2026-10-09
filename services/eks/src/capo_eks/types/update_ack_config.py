"""Generated from Smithy shape ``com.amazonaws.eks#UpdateAckConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.ack_disabled_services_list
    import capo_eks.types.boxed_boolean


class UpdateAckConfig(TypedDict, closed=True):
    enable_cross_namespace: NotRequired["capo_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether ACK controllers resolve resource references to resources in a different Kubernetes namespace. Set this value to <code>false</code> to require references to remain within the same namespace, or <code>true</code> to allow cross-namespace references. If you omit this field, the current value is unchanged.</p>"""
    disabled_services: NotRequired[
        "capo_eks.types.ack_disabled_services_list.AckDisabledServicesList"
    ]
    """<p>An updated list of ACK service names whose controllers are turned off for this capability. This list replaces the previous list instead of merging with it, so specify the complete set of services that you want turned off. If you omit this field, the previous list is unchanged. To turn all services back on, specify an empty list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAckConfig) -> dict:
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


def deserialize_json(data: dict) -> UpdateAckConfig:
    out: UpdateAckConfig = {}  # type: ignore[typeddict-item]
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
