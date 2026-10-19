"""Generated from Smithy shape ``com.amazonaws.appflow#SalesforceSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.boolean
    import capo_appflow.types.object
    import capo_appflow.types.salesforce_data_transfer_api


class SalesforceSourceProperties(TypedDict, closed=True):
    object: "capo_appflow.types.object.Object"
    """<p> The object specified in the Salesforce flow source. </p>"""
    enable_dynamic_field_update: "capo_appflow.types.boolean.Boolean"
    """<p> The flag that enables dynamic fetching of new (recently added) fields in the Salesforce objects while running a flow. </p>"""
    include_deleted_records: "capo_appflow.types.boolean.Boolean"
    """<p> Indicates whether Amazon AppFlow includes deleted files in the flow run. </p>"""
    data_transfer_api: NotRequired[
        "capo_appflow.types.salesforce_data_transfer_api.SalesforceDataTransferApi"
    ]
    """<p>Specifies which Salesforce API is used by Amazon AppFlow when your flow transfers data from Salesforce.</p> <dl> <dt>AUTOMATIC</dt> <dd> <p>The default. Amazon AppFlow selects which API to use based on the number of records that your flow transfers from Salesforce. If your flow transfers fewer than 1,000,000 records, Amazon AppFlow uses Salesforce REST API. If your flow transfers 1,000,000 records or more, Amazon AppFlow uses Salesforce Bulk API 2.0.</p> <p>Each of these Salesforce APIs structures data differently. If Amazon AppFlow selects the API automatically, be aware that, for recurring flows, the data output might vary from one flow run to the next. For example, if a flow runs daily, it might use REST API on one day to transfer 900,000 records, and it might use Bulk API 2.0 on the next day to transfer 1,100,000 records. For each of these flow runs, the respective Salesforce API formats the data differently. Some of the differences include how dates are formatted and null values are represented. Also, Bulk API 2.0 doesn't transfer Salesforce compound fields.</p> <p>By choosing this option, you optimize flow performance for both small and large data transfers, but the tradeoff is inconsistent formatting in the output.</p> </dd> <dt>BULKV2</dt> <dd> <p>Amazon AppFlow uses only Salesforce Bulk API 2.0. This API runs asynchronous data transfers, and it's optimal for large sets of data. By choosing this option, you ensure that your flow writes consistent output, but you optimize performance only for large data transfers.</p> <p>Note that Bulk API 2.0 does not transfer Salesforce compound fields.</p> </dd> <dt>REST_SYNC</dt> <dd> <p>Amazon AppFlow uses only Salesforce REST API. By choosing this option, you ensure that your flow writes consistent output, but you decrease performance for large data transfers that are better suited for Bulk API 2.0. In some cases, if your flow attempts to transfer a vary large set of data, it might fail wituh a timed out error.</p> </dd> </dl>"""


# --- restJson1 ser/de ---
def serialize_json(value: SalesforceSourceProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    out["enableDynamicFieldUpdate"] = value.get("enable_dynamic_field_update", False)
    out["includeDeletedRecords"] = value.get("include_deleted_records", False)
    if "data_transfer_api" in value:
        import capo_appflow.types.salesforce_data_transfer_api

        out["dataTransferApi"] = (
            capo_appflow.types.salesforce_data_transfer_api.serialize_json(
                value["data_transfer_api"]
            )
        )
    return out


def deserialize_json(data: dict) -> SalesforceSourceProperties:
    out: SalesforceSourceProperties = {}  # type: ignore[typeddict-item]
    if data.get("object") is not None:
        out["object"] = data["object"]
    else:
        out["object"] = ""
    if data.get("enableDynamicFieldUpdate") is not None:
        out["enable_dynamic_field_update"] = data["enableDynamicFieldUpdate"]
    else:
        out["enable_dynamic_field_update"] = False
    if data.get("includeDeletedRecords") is not None:
        out["include_deleted_records"] = data["includeDeletedRecords"]
    else:
        out["include_deleted_records"] = False
    if data.get("dataTransferApi") is not None:
        import capo_appflow.types.salesforce_data_transfer_api

        out["data_transfer_api"] = (
            capo_appflow.types.salesforce_data_transfer_api.deserialize_json(
                data["dataTransferApi"]
            )
        )
    return out
