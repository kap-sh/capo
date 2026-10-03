"""Generated from Smithy shape ``com.amazonaws.supplychain#GetDataLakeDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset_name
    import capo_supplychain.types.data_lake_namespace_name
    import capo_supplychain.types.uuid


class GetDataLakeDatasetRequest(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    namespace: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName"
    """<p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>"""
    name: "capo_supplychain.types.data_lake_dataset_name.DataLakeDatasetName"
    """<p>The name of the dataset. For <b>asc</b> namespace, the name must be one of the supported data entities under <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataLakeDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataLakeDatasetRequest:
    out: GetDataLakeDatasetRequest = {}  # type: ignore[typeddict-item]
    return out
