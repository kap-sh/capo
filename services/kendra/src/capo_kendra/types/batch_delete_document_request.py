"""Generated from Smithy shape ``com.amazonaws.kendra#BatchDeleteDocumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.data_source_sync_job_metric_target
    import capo_kendra.types.document_id_list
    import capo_kendra.types.index_id


class BatchDeleteDocumentRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index that contains the documents to delete.</p>"""
    document_id_list: "capo_kendra.types.document_id_list.DocumentIdList"
    """<p>One or more identifiers for documents to delete from the index.</p>"""
    data_source_sync_job_metric_target: NotRequired[
        "capo_kendra.types.data_source_sync_job_metric_target.DataSourceSyncJobMetricTarget"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteDocumentRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    import capo_kendra.types.document_id_list

    out["DocumentIdList"] = capo_kendra.types.document_id_list.serialize_aws_json_1_1(
        value["document_id_list"]
    )
    if "data_source_sync_job_metric_target" in value:
        import capo_kendra.types.data_source_sync_job_metric_target

        out["DataSourceSyncJobMetricTarget"] = (
            capo_kendra.types.data_source_sync_job_metric_target.serialize_aws_json_1_1(
                value["data_source_sync_job_metric_target"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteDocumentRequest:
    out: BatchDeleteDocumentRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("DocumentIdList") is not None:
        import capo_kendra.types.document_id_list

        out["document_id_list"] = (
            capo_kendra.types.document_id_list.deserialize_aws_json_1_1(
                data["DocumentIdList"]
            )
        )
    else:
        out["document_id_list"] = []
    if data.get("DataSourceSyncJobMetricTarget") is not None:
        import capo_kendra.types.data_source_sync_job_metric_target

        out["data_source_sync_job_metric_target"] = (
            capo_kendra.types.data_source_sync_job_metric_target.deserialize_aws_json_1_1(
                data["DataSourceSyncJobMetricTarget"]
            )
        )
    return out
