"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.data_source_id
    import capo_kendra.types.data_source_name
    import capo_kendra.types.data_source_status
    import capo_kendra.types.data_source_type
    import capo_kendra.types.language_code
    import capo_kendra.types.timestamp


class DataSourceSummary(TypedDict, closed=True):
    name: NotRequired["capo_kendra.types.data_source_name.DataSourceName"]
    """<p>The name of the data source.</p>"""
    id: NotRequired["capo_kendra.types.data_source_id.DataSourceId"]
    """<p>The identifier for the data source.</p>"""
    type: NotRequired["capo_kendra.types.data_source_type.DataSourceType"]
    """<p>The type of the data source.</p>"""
    created_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the data source connector was created.</p>"""
    updated_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the data source connector was last updated.</p>"""
    status: NotRequired["capo_kendra.types.data_source_status.DataSourceStatus"]
    """<p>The status of the data source. When the status is <code>ACTIVE</code> the data source is ready to use.</p>"""
    language_code: NotRequired["capo_kendra.types.language_code.LanguageCode"]
    """<p>The code for a language. This shows a supported language for all documents in the data source. English is supported by default. For more information on supported languages, including their codes, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html">Adding documents in languages other than English</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import capo_kendra.types.data_source_type

        out["Type"] = capo_kendra.types.data_source_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "created_at" in value:
        import capo_kendra.types.timestamp

        out["CreatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_kendra.types.timestamp

        out["UpdatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "status" in value:
        import capo_kendra.types.data_source_status

        out["Status"] = capo_kendra.types.data_source_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSourceSummary:
    out: DataSourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Type") is not None:
        import capo_kendra.types.data_source_type

        out["type"] = capo_kendra.types.data_source_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("CreatedAt") is not None:
        import capo_kendra.types.timestamp

        out["created_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_kendra.types.timestamp

        out["updated_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if data.get("Status") is not None:
        import capo_kendra.types.data_source_status

        out["status"] = capo_kendra.types.data_source_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("LanguageCode") is not None:
        out["language_code"] = data["LanguageCode"]
    return out
