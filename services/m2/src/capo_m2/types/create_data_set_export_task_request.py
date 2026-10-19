"""Generated from Smithy shape ``com.amazonaws.m2#CreateDataSetExportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.client_token
    import capo_m2.types.data_set_export_config
    import capo_m2.types.identifier
    import capo_m2.types.kms_key_id


class CreateDataSetExportTaskRequest(TypedDict, closed=True):
    application_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application for which you want to export data sets.</p>"""
    export_config: "capo_m2.types.data_set_export_config.DataSetExportConfig"
    """<p>The data set export task configuration.</p>"""
    client_token: NotRequired["capo_m2.types.client_token.ClientToken"]
    """<p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a data set export. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires.</p>"""
    kms_key_id: NotRequired["capo_m2.types.kms_key_id.KMSKeyId"]
    """<p>The identifier of a customer managed key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSetExportTaskRequest) -> dict:
    out: dict = {}
    import capo_m2.types.data_set_export_config

    out["exportConfig"] = capo_m2.types.data_set_export_config.serialize_json(
        value["export_config"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> CreateDataSetExportTaskRequest:
    out: CreateDataSetExportTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("exportConfig") is not None:
        import capo_m2.types.data_set_export_config

        out["export_config"] = capo_m2.types.data_set_export_config.deserialize_json(
            data["exportConfig"]
        )
    else:
        import capo_m2.types._unknown

        out["export_config"] = capo_m2.types._unknown.UnknownUnionMember("")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
