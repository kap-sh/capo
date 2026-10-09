"""Generated from Smithy shape ``com.amazonaws.eks#AckConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.ack_disabled_services_list
    import capo_eks.types.boxed_boolean


class AckConfigRequest(TypedDict, closed=True):
    enable_cross_namespace: NotRequired["capo_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether ACK controllers resolve resource references to resources in a different Kubernetes namespace. Set this value to <code>true</code> to allow references to resolve to resources in another namespace. If you don't specify this value, or you omit the <code>ack</code> configuration entirely, the capability is created with this value set to <code>false</code> and references must remain within the same namespace.</p>"""
    disabled_services: NotRequired[
        "capo_eks.types.ack_disabled_services_list.AckDisabledServicesList"
    ]
    """<p>A list of ACK service names whose controllers are turned off for this capability, for example <code>s3</code>, <code>ec2</code>, and <code>iam</code>. Resources of a disabled service aren't reconciled until you re-enable the service. To keep all services enabled, omit this field or specify an empty list. An unrecognized service name is accepted and stored but turns nothing off, and <code>DescribeCapability</code> returns the list exactly as you supplied it. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/create-ack-capability.html#ack-configuration-options">ACK capability configuration options</a> in the <i>Amazon EKS User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AckConfigRequest) -> dict:
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


def deserialize_json(data: dict) -> AckConfigRequest:
    out: AckConfigRequest = {}  # type: ignore[typeddict-item]
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
