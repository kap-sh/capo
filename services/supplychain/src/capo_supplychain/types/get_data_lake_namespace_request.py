"""Generated from Smithy shape ``com.amazonaws.supplychain#GetDataLakeNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_namespace_name
    import capo_supplychain.types.uuid


class GetDataLakeNamespaceRequest(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    name: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName"
    """<p>The name of the namespace. Besides the namespaces user created, you can also specify the pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - Pre-defined namespace containing Amazon Web Services Supply Chain supported datasets, see <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - Pre-defined namespace containing datasets with custom user-defined schemas.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataLakeNamespaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataLakeNamespaceRequest:
    out: GetDataLakeNamespaceRequest = {}  # type: ignore[typeddict-item]
    return out
