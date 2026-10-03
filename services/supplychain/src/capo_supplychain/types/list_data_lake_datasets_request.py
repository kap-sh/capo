"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataLakeDatasetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset_max_results
    import capo_supplychain.types.data_lake_dataset_next_token
    import capo_supplychain.types.data_lake_namespace_name
    import capo_supplychain.types.uuid


class ListDataLakeDatasetsRequest(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    namespace: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName"
    """<p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>"""
    next_token: NotRequired[
        "capo_supplychain.types.data_lake_dataset_next_token.DataLakeDatasetNextToken"
    ]
    """<p>The pagination token to fetch next page of datasets.</p>"""
    max_results: (
        "capo_supplychain.types.data_lake_dataset_max_results.DataLakeDatasetMaxResults"
    )
    """<p>The max number of datasets to fetch in this paginated request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataLakeDatasetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataLakeDatasetsRequest:
    out: ListDataLakeDatasetsRequest = {}  # type: ignore[typeddict-item]
    return out
