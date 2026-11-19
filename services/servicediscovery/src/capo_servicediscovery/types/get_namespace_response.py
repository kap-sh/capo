"""Generated from Smithy shape ``com.amazonaws.servicediscovery#GetNamespaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.namespace


class GetNamespaceResponse(TypedDict, closed=True):
    namespace: NotRequired["capo_servicediscovery.types.namespace.Namespace"]
    """<p>A complex type that contains information about the specified namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetNamespaceResponse) -> dict:
    out: dict = {}
    if "namespace" in value:
        import capo_servicediscovery.types.namespace

        out["Namespace"] = capo_servicediscovery.types.namespace.serialize_aws_json_1_1(
            value["namespace"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetNamespaceResponse:
    out: GetNamespaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        import capo_servicediscovery.types.namespace

        out["namespace"] = (
            capo_servicediscovery.types.namespace.deserialize_aws_json_1_1(
                data["Namespace"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetNamespaceResponse) -> dict:
    out: dict = {}
    if "namespace" in value:
        import capo_servicediscovery.types.namespace

        out["Namespace"] = capo_servicediscovery.types.namespace.serialize_cbor(
            value["namespace"]
        )
    return out


def deserialize_cbor(data: dict) -> GetNamespaceResponse:
    out: GetNamespaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        import capo_servicediscovery.types.namespace

        out["namespace"] = capo_servicediscovery.types.namespace.deserialize_cbor(
            data["Namespace"]
        )
    return out
