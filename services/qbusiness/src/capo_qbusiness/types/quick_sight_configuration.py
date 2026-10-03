"""Generated from Smithy shape ``com.amazonaws.qbusiness#QuickSightConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.client_namespace


class QuickSightConfiguration(TypedDict, closed=True):
    client_namespace: "capo_qbusiness.types.client_namespace.ClientNamespace"
    """<p>The Amazon Quick Suite namespace that is used as the identity provider. For more information about Quick Suite namespaces, see <a href="https://docs.aws.amazon.com/quicksight/latest/developerguide/namespace-operations.html">Namespace operations</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickSightConfiguration) -> dict:
    out: dict = {}
    out["clientNamespace"] = value["client_namespace"]
    return out


def deserialize_json(data: dict) -> QuickSightConfiguration:
    out: QuickSightConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("clientNamespace") is not None:
        out["client_namespace"] = data["clientNamespace"]
    else:
        raise DeserializationError("QuickSightConfiguration.client_namespace required")
    return out
